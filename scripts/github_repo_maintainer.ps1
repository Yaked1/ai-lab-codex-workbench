<#
.SYNOPSIS
    Preview, check, safely fix, stage, commit, push, and open pull requests for GitHub repositories.

.DESCRIPTION
    This script is intentionally conservative. It analyzes the current Git repository,
    detects safe validation commands, optionally runs safe autofixes, stages only
    allowed changed files, commits, pushes, and creates a pull request with the
    GitHub CLI.

    It does not install dependencies, force-push, merge pull requests, delete
    branches, stage secrets, or stage private-looking files. Write operations
    require -Apply. Push and PR creation require -Push and/or -CreatePR.

.EXAMPLES
    # Inspect only
    .\scripts\github_repo_maintainer.ps1 -Mode status

    # Run detected checks
    .\scripts\github_repo_maintainer.ps1 -Mode check

    # Run safe autofix and checks, but do not stage or commit unless -Apply is set
    .\scripts\github_repo_maintainer.ps1 -Mode full

    # Safely fix, stage selected changed files, commit, push, and create a PR
    .\scripts\github_repo_maintainer.ps1 -Mode full -Apply -Push -CreatePR `
        -Branch agent/maintain-docs `
        -CommitMessage "chore: run repository maintenance" `
        -PrTitle "Repository maintenance"
#>

[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [ValidateSet("status", "check", "fix", "commit", "pr", "full")]
    [string]$Mode = "status",

    [string]$BaseBranch = "main",

    [string]$Branch = "",

    [string]$CommitMessage = "",

    [string]$PrTitle = "",

    [string]$PrBodyFile = "",

    [string[]]$Include = @(),

    [string[]]$Exclude = @(),

    [int]$MaxFiles = 100,

    [int]$MaxSecretScanBytes = 1048576,

    [int]$IssueNumber = 0,

    [switch]$Apply,

    [switch]$Push,

    [switch]$CreatePR,

    [switch]$AllowMain,

    [switch]$AllowAllChanges,

    [switch]$AllowDeletedFiles,

    [switch]$SkipChecks,

    [switch]$SkipAutofix
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Script:CheckResults = New-Object System.Collections.Generic.List[string]
$Script:ActionsTaken = New-Object System.Collections.Generic.List[string]
$Script:Warnings = New-Object System.Collections.Generic.List[string]

function Write-Section {
    param([string]$Title)
    Write-Host ""
    Write-Host "== $Title =="
}

function Write-Info {
    param([string]$Message)
    Write-Host "[info] $Message"
}

function Write-WarnLine {
    param([string]$Message)
    $Script:Warnings.Add($Message) | Out-Null
    Write-Host "[warn] $Message" -ForegroundColor Yellow
}

function Test-CommandAvailable {
    param([string]$Name)
    return [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

function Assert-CommandAvailable {
    param([string]$Name)
    if (-not (Test-CommandAvailable $Name)) {
        throw "Required command '$Name' was not found on PATH."
    }
}

function Invoke-Native {
    param(
        [string]$File,
        [string[]]$Arguments,
        [switch]$AllowFailure
    )

    Write-Host "> $File $($Arguments -join ' ')"
    # Send the command's output to the host so it is shown but does NOT leak into this
    # function's output stream. Without Out-Host, callers doing `$code = Invoke-Native ...`
    # would capture @(stdout..., exitCode) and misread the exit code (e.g. a passing check
    # read as a failure).
    & $File @Arguments | Out-Host
    $exitCode = if ($null -eq $LASTEXITCODE) { 0 } else { $LASTEXITCODE }
    if ($exitCode -ne 0 -and -not $AllowFailure) {
        throw "$File failed with exit code $exitCode."
    }
    return $exitCode
}

function Invoke-Capture {
    param(
        [string]$File,
        [string[]]$Arguments,
        [switch]$AllowFailure
    )

    $output = & $File @Arguments
    $exitCode = if ($null -eq $LASTEXITCODE) { 0 } else { $LASTEXITCODE }
    if ($exitCode -ne 0 -and -not $AllowFailure) {
        throw "$File $($Arguments -join ' ') failed with exit code $exitCode."
    }
    return @($output)
}

function Resolve-PythonCommand {
    foreach ($candidate in @("py", "python", "python3")) {
        if (Test-CommandAvailable $candidate) {
            return $candidate
        }
    }
    return $null
}

function Invoke-Python {
    param([string[]]$Arguments)

    $python = Resolve-PythonCommand
    if (-not $python) {
        Write-WarnLine "Python was not found on PATH; skipping Python command: $($Arguments -join ' ')"
        return 127
    }
    return Invoke-Native $python $Arguments -AllowFailure
}

function Get-RepoRoot {
    Assert-CommandAvailable "git"
    $rootLines = @(Invoke-Capture git @("rev-parse", "--show-toplevel"))
    $root = if ($rootLines.Count -gt 0) { [string]$rootLines[0] } else { "" }
    if ([string]::IsNullOrWhiteSpace($root)) {
        throw "This directory is not inside a Git repository."
    }
    return $root.Trim()
}

function Get-CurrentBranch {
    $branchLines = @(Invoke-Capture git @("branch", "--show-current"))
    $branch = if ($branchLines.Count -gt 0) { [string]$branchLines[0] } else { "" }
    if ([string]::IsNullOrWhiteSpace($branch)) {
        throw "Could not determine the current Git branch. Detached HEAD is not supported."
    }
    return $branch.Trim()
}

function Get-ChangedPaths {
    $lines = Invoke-Capture git @("status", "--porcelain=v1")
    $items = New-Object System.Collections.Generic.List[object]

    foreach ($lineRaw in $lines) {
        $line = [string]$lineRaw
        if ($line.Length -lt 4) {
            continue
        }

        $statusCode = $line.Substring(0, 2)
        $path = $line.Substring(3).Trim()
        if ($path -match " -> ") {
            $parts = $path -split " -> ", 2
            $path = $parts[1]
        }
        $path = $path.Trim('"') -replace "\\", "/"
        $isDeleted = $statusCode.Contains("D")

        $items.Add([pscustomobject]@{
            Status = $statusCode
            Path = $path
            Deleted = $isDeleted
        }) | Out-Null
    }

    # @() on a generic List[object] throws "Argument types do not match" in PowerShell 7.4+.
    # Use .ToArray(); the leading comma keeps the result an array through the return unroll.
    return ,$items.ToArray()
}

function Test-WildcardAny {
    param(
        [string]$Path,
        [string[]]$Patterns
    )

    foreach ($pattern in $Patterns) {
        if ($Path -like $pattern) {
            return $true
        }
    }
    return $false
}

function Test-BlockedPath {
    param([string]$Path)

    $p = ($Path -replace "\\", "/").ToLowerInvariant()
    $parts = @($p -split "/" | Where-Object { $_ })

    $blockedNames = @(
        ".git", ".hg", ".svn", ".env", ".venv", "venv", "node_modules",
        "__pycache__", ".pytest_cache", ".mypy_cache", ".cache", ".idea", ".vscode",
        "secret", "secrets", "private", "credentials", "browser-profiles"
    )

    foreach ($part in $parts) {
        if ($blockedNames -contains $part) {
            return "blocked path segment '$part'"
        }
        if ($part.StartsWith(".env.")) {
            return "environment file"
        }
        if ($part.StartsWith("secret.") -or $part.StartsWith("secret-")) {
            return "secret-looking file name"
        }
        if ($part.StartsWith("private.") -or $part.StartsWith("private-")) {
            return "private-looking file name"
        }
    }

    $blockedSuffixes = @(
        ".7z", ".bak", ".bin", ".ckpt", ".db", ".gguf", ".gz", ".h5",
        ".joblib", ".key", ".log", ".onnx", ".p12", ".pem", ".pfx", ".pickle",
        ".pkl", ".pth", ".pt", ".pyc", ".pyo", ".rar", ".safetensors", ".sqlite",
        ".tar", ".tgz", ".tmp", ".zip"
    )

    foreach ($suffix in $blockedSuffixes) {
        if ($p.EndsWith($suffix)) {
            return "blocked suffix '$suffix'"
        }
    }

    return $null
}

function Test-TextFileLikely {
    param([string]$Path)

    $textSuffixes = @(
        ".md", ".txt", ".json", ".yml", ".yaml", ".toml", ".ini", ".ps1", ".py",
        ".js", ".ts", ".tsx", ".jsx", ".html", ".css", ".scss", ".xml", ".csv",
        ".go", ".rs", ".java", ".cs", ".rb", ".php", ".sh", ".bat", ".cmd"
    )
    $suffix = [System.IO.Path]::GetExtension($Path).ToLowerInvariant()
    return $textSuffixes -contains $suffix
}

function Test-SecretLikeContent {
    param(
        [string]$Root,
        [string]$Path
    )

    if (-not (Test-TextFileLikely $Path)) {
        return $false
    }

    $full = Join-Path $Root $Path
    if (-not (Test-Path -LiteralPath $full -PathType Leaf)) {
        return $false
    }

    $item = Get-Item -LiteralPath $full
    if ($item.Length -gt $MaxSecretScanBytes) {
        Write-WarnLine "Skipping secret scan for large file: $Path"
        return $false
    }

    $text = Get-Content -LiteralPath $full -Raw -ErrorAction Stop
    $patterns = @(
        "-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----",
        "ghp_[A-Za-z0-9_]{20,}",
        "github_pat_[A-Za-z0-9_]{20,}",
        "sk-[A-Za-z0-9]{24,}",
        "xox[baprs]-[A-Za-z0-9-]{20,}"
    )

    foreach ($pattern in $patterns) {
        if ($text -match $pattern) {
            return $true
        }
    }
    return $false
}

function Select-StageablePaths {
    param(
        [string]$Root,
        [object[]]$Changed
    )

    $selected = New-Object System.Collections.Generic.List[string]

    foreach ($entry in $Changed) {
        $path = [string]$entry.Path
        if ([string]::IsNullOrWhiteSpace($path)) {
            continue
        }

        if ($Include.Count -gt 0 -and -not (Test-WildcardAny $path $Include)) {
            Write-Info "Skipping outside include rules: $path"
            continue
        }

        if ($Exclude.Count -gt 0 -and (Test-WildcardAny $path $Exclude)) {
            Write-WarnLine "Skipping excluded path: $path"
            continue
        }

        if ($entry.Deleted -and -not $AllowDeletedFiles) {
            Write-WarnLine "Skipping deleted file without -AllowDeletedFiles: $path"
            continue
        }

        $blockedReason = Test-BlockedPath $path
        if ($blockedReason) {
            Write-WarnLine ("Skipping {0}: {1}" -f $path, $blockedReason)
            continue
        }

        if (-not $AllowAllChanges -and (Test-SecretLikeContent $Root $path)) {
            Write-WarnLine ("Skipping {0}: secret-looking content detected" -f $path)
            continue
        }

        $selected.Add($path) | Out-Null
    }

    return @($selected | Select-Object -Unique)
}

function Get-DetectedCheckCommands {
    param([string]$Root)

    $commands = New-Object System.Collections.Generic.List[object]

    if (Test-Path -LiteralPath (Join-Path $Root "scripts/repo_health_check.py")) {
        $commands.Add([pscustomobject]@{ File = "PYTHON"; Args = @("scripts/repo_health_check.py"); Name = "repo health check" }) | Out-Null
    }

    if (Test-Path -LiteralPath (Join-Path $Root "scripts/safe_autofix.py")) {
        $commands.Add([pscustomobject]@{ File = "PYTHON"; Args = @("scripts/safe_autofix.py", "--check"); Name = "safe autofix check" }) | Out-Null
    }

    if (Test-Path -LiteralPath (Join-Path $Root "tests")) {
        $commands.Add([pscustomobject]@{ File = "PYTHON"; Args = @("-m", "unittest", "discover", "-s", "tests"); Name = "unit tests" }) | Out-Null
    }

    if (Test-Path -LiteralPath (Join-Path $Root "package.json")) {
        if (Test-CommandAvailable "npm") {
            $commands.Add([pscustomobject]@{ File = "npm"; Args = @("test", "--if-present"); Name = "npm test" }) | Out-Null
        } else {
            Write-WarnLine "package.json found but npm is not on PATH."
        }
    }

    if (Test-Path -LiteralPath (Join-Path $Root "go.mod")) {
        if (Test-CommandAvailable "go") {
            $commands.Add([pscustomobject]@{ File = "go"; Args = @("test", "./..."); Name = "go tests" }) | Out-Null
        } else {
            Write-WarnLine "go.mod found but go is not on PATH."
        }
    }

    if (Test-Path -LiteralPath (Join-Path $Root "Cargo.toml")) {
        if (Test-CommandAvailable "cargo") {
            $commands.Add([pscustomobject]@{ File = "cargo"; Args = @("test"); Name = "cargo tests" }) | Out-Null
        } else {
            Write-WarnLine "Cargo.toml found but cargo is not on PATH."
        }
    }

    $solutionFiles = Get-ChildItem -LiteralPath $Root -Filter "*.sln" -File -ErrorAction SilentlyContinue
    $projectFiles = Get-ChildItem -LiteralPath $Root -Filter "*.csproj" -File -ErrorAction SilentlyContinue
    if (($solutionFiles -or $projectFiles) -and (Test-CommandAvailable "dotnet")) {
        $commands.Add([pscustomobject]@{ File = "dotnet"; Args = @("test"); Name = "dotnet tests" }) | Out-Null
    }

    # See Get-ChangedPaths: @() on a List[object] is broken in PS 7.4+; use .ToArray() instead.
    return ,$commands.ToArray()
}

function Invoke-DetectedChecks {
    param([string]$Root)

    if ($SkipChecks) {
        Write-WarnLine "Skipping checks because -SkipChecks was provided."
        return
    }

    Write-Section "Running detected checks"
    $commands = Get-DetectedCheckCommands $Root
    if (-not $commands -or $commands.Count -eq 0) {
        Write-WarnLine "No check commands were detected."
        return
    }

    foreach ($command in $commands) {
        $name = [string]$command.Name
        $file = [string]$command.File
        $args = [string[]]$command.Args
        $exitCode = 0

        if ($file -eq "PYTHON") {
            $exitCode = Invoke-Python $args
        } else {
            $exitCode = Invoke-Native $file $args -AllowFailure
        }

        if ($exitCode -eq 0) {
            $Script:CheckResults.Add("PASS: $name") | Out-Null
        } else {
            $Script:CheckResults.Add("FAIL: $name (exit $exitCode)") | Out-Null
            throw "Check failed: $name. Fix it before committing or rerun with narrower scope after review."
        }
    }
}

function Invoke-SafeAutofix {
    param([string]$Root)

    if ($SkipAutofix) {
        Write-WarnLine "Skipping autofix because -SkipAutofix was provided."
        return
    }

    $autofix = Join-Path $Root "scripts/safe_autofix.py"
    if (-not (Test-Path -LiteralPath $autofix)) {
        Write-WarnLine "No scripts/safe_autofix.py found; skipping safe autofix."
        return
    }

    Write-Section "Running safe autofix"
    $exitCode = Invoke-Python @("scripts/safe_autofix.py", "--write")
    if ($exitCode -ne 0) {
        throw "Safe autofix failed with exit code $exitCode."
    }
    $Script:ActionsTaken.Add("Ran scripts/safe_autofix.py --write") | Out-Null
}

function Ensure-Branch {
    param([string]$RequestedBranch)

    $current = Get-CurrentBranch
    if ($current -eq $BaseBranch -and -not $AllowMain) {
        $target = $RequestedBranch
        if ([string]::IsNullOrWhiteSpace($target)) {
            $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
            $target = "agent/repo-maintenance-$timestamp"
        }

        # Creating/switching a branch is a write action: never do it in preview (no -Apply).
        if (-not $Apply) {
            Write-WarnLine "Preview only: would create and switch to work branch '$target' (on base branch '$BaseBranch'). Use -Apply to create it."
            return $current
        }

        Write-Section "Creating work branch"
        Invoke-Native git @("switch", "-c", $target) | Out-Null
        $Script:ActionsTaken.Add("Created branch $target") | Out-Null
        return $target
    }

    if (-not [string]::IsNullOrWhiteSpace($RequestedBranch) -and $RequestedBranch -ne $current) {
        if (-not $Apply) {
            Write-WarnLine "Preview only: would switch to branch '$RequestedBranch'. Use -Apply to switch."
            return $current
        }

        Write-Section "Switching branch"
        $exists = Invoke-Capture git @("branch", "--list", $RequestedBranch) -AllowFailure
        if ($exists -and -not [string]::IsNullOrWhiteSpace(($exists -join ""))) {
            Invoke-Native git @("switch", $RequestedBranch) | Out-Null
            $Script:ActionsTaken.Add("Switched to branch $RequestedBranch") | Out-Null
        } else {
            Invoke-Native git @("switch", "-c", $RequestedBranch) | Out-Null
            $Script:ActionsTaken.Add("Created branch $RequestedBranch") | Out-Null
        }
        return $RequestedBranch
    }

    if ($current -eq $BaseBranch -and $AllowMain) {
        Write-WarnLine "Continuing on base branch '$BaseBranch' because -AllowMain was provided."
    }

    return (Get-CurrentBranch)
}

function Stage-SelectedChanges {
    param(
        [string]$Root,
        [string[]]$Paths
    )

    if (-not $Paths -or $Paths.Count -eq 0) {
        throw "No stageable paths found. Review git status and include/exclude rules."
    }

    if ($Paths.Count -gt $MaxFiles) {
        throw "Refusing to stage $($Paths.Count) files because it exceeds -MaxFiles $MaxFiles. Use narrower -Include rules or raise -MaxFiles after review."
    }

    Write-Section "Stageable paths"
    foreach ($path in $Paths) {
        Write-Host "  $path"
    }

    if (-not $Apply) {
        Write-WarnLine "Preview only: not staging because -Apply was not provided."
        return
    }

    Write-Section "Staging selected paths"
    Invoke-Native git (@("add", "--") + $Paths) | Out-Null
    $Script:ActionsTaken.Add("Staged $($Paths.Count) path(s)") | Out-Null
}

function Test-StagedChangesExist {
    $staged = Invoke-Capture git @("diff", "--cached", "--name-only")
    return [bool]($staged -and ($staged | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) }))
}

function New-CommitMessage {
    if (-not [string]::IsNullOrWhiteSpace($CommitMessage)) {
        return $CommitMessage
    }

    $staged = Invoke-Capture git @("diff", "--cached", "--name-only")
    $joined = ($staged -join "`n")

    if ($joined -match "(^|`n)docs/") {
        return "docs: run repository maintenance"
    }
    if ($joined -match "(^|`n)scripts/") {
        return "chore: update repository automation"
    }
    if ($joined -match "(^|`n)tests/") {
        return "test: update repository checks"
    }
    return "chore: run repository maintenance"
}

function Commit-StagedChanges {
    if (-not (Test-StagedChangesExist)) {
        Write-WarnLine "No staged changes to commit."
        return $false
    }

    $message = New-CommitMessage
    if ($IssueNumber -gt 0 -and $message -notmatch "#$IssueNumber") {
        $message = "$message (#$IssueNumber)"
    }

    if (-not $Apply) {
        Write-WarnLine "Preview only: not committing because -Apply was not provided. Commit message would be: $message"
        return $false
    }

    Write-Section "Committing"
    Invoke-Native git @("commit", "-m", $message) | Out-Null
    $Script:ActionsTaken.Add("Created commit: $message") | Out-Null
    return $true
}

function Push-Branch {
    param([string]$CurrentBranch)

    if (-not $Push -and -not $CreatePR) {
        Write-WarnLine "Not pushing because neither -Push nor -CreatePR was provided."
        return
    }

    if (-not $Apply) {
        Write-WarnLine "Preview only: not pushing because -Apply was not provided."
        return
    }

    Write-Section "Pushing branch"
    Invoke-Native git @("push", "-u", "origin", $CurrentBranch) | Out-Null
    $Script:ActionsTaken.Add("Pushed branch $CurrentBranch to origin") | Out-Null
}

function New-PrBody {
    param([string]$CurrentBranch)

    if (-not [string]::IsNullOrWhiteSpace($PrBodyFile)) {
        if (-not (Test-Path -LiteralPath $PrBodyFile -PathType Leaf)) {
            throw "PR body file was not found: $PrBodyFile"
        }
        return (Resolve-Path -LiteralPath $PrBodyFile).Path
    }

    $temp = New-TemporaryFile
    $issueLine = if ($IssueNumber -gt 0) { "`nRefs #$IssueNumber`n" } else { "" }
    $checks = if ($Script:CheckResults.Count -gt 0) { ($Script:CheckResults -join "`n- ") } else { "Not run or not detected." }
    $actions = if ($Script:ActionsTaken.Count -gt 0) { ($Script:ActionsTaken -join "`n- ") } else { "No write actions recorded." }
    $warnings = if ($Script:Warnings.Count -gt 0) { ($Script:Warnings -join "`n- ") } else { "None." }

    $body = @"
## Summary

Automated repository maintenance prepared from branch `$CurrentBranch`.
$issueLine
## Actions

- $actions

## Checks

- $checks

## Safety notes

- No force-push was performed.
- No merge was performed.
- Secret-looking and private-looking paths were excluded from staging.
- Review the diff before merging.

## Warnings / skipped items

- $warnings
"@

    Set-Content -LiteralPath $temp.FullName -Value $body -Encoding UTF8
    return $temp.FullName
}

function Create-PullRequest {
    param([string]$CurrentBranch)

    if (-not $CreatePR) {
        return
    }

    Assert-CommandAvailable "gh"

    if (-not $Apply) {
        Write-WarnLine "Preview only: not creating PR because -Apply was not provided."
        return
    }

    $title = $PrTitle
    if ([string]::IsNullOrWhiteSpace($title)) {
        $title = "Repository maintenance"
    }

    $bodyFile = New-PrBody $CurrentBranch

    Write-Section "Creating pull request"
    Invoke-Native gh @(
        "pr", "create",
        "--base", $BaseBranch,
        "--head", $CurrentBranch,
        "--title", $title,
        "--body-file", $bodyFile
    ) | Out-Null
    $Script:ActionsTaken.Add("Created pull request: $title") | Out-Null
}

function Show-RepositoryStatus {
    param([string]$Root)

    Write-Section "Repository status"
    Write-Info "Root: $Root"
    Invoke-Native git @("status", "--short", "--branch") | Out-Null

    Write-Section "Detected checks"
    $checks = Get-DetectedCheckCommands $Root
    if (-not $checks -or $checks.Count -eq 0) {
        Write-Host "  none"
    } else {
        foreach ($check in $checks) {
            $file = [string]$check.File
            $args = [string[]]$check.Args
            if ($file -eq "PYTHON") {
                $file = "py/python/python3"
            }
            Write-Host "  $($check.Name): $file $($args -join ' ')"
        }
    }

    if (Test-CommandAvailable "gh") {
        Write-Section "GitHub status"
        Invoke-Native gh @("repo", "view", "--json", "nameWithOwner", "--jq", ".nameWithOwner") -AllowFailure | Out-Null
        Invoke-Native gh @("issue", "list", "--limit", "5") -AllowFailure | Out-Null
        Invoke-Native gh @("pr", "list", "--limit", "5") -AllowFailure | Out-Null
    } else {
        Write-WarnLine "GitHub CLI 'gh' was not found; PR creation will be unavailable."
    }
}

function Show-FinalReport {
    Write-Section "Final report"

    if ($Script:ActionsTaken.Count -gt 0) {
        Write-Host "Actions:"
        foreach ($item in $Script:ActionsTaken) {
            Write-Host "  - $item"
        }
    } else {
        Write-Host "Actions: none"
    }

    if ($Script:CheckResults.Count -gt 0) {
        Write-Host "Checks:"
        foreach ($item in $Script:CheckResults) {
            Write-Host "  - $item"
        }
    } else {
        Write-Host "Checks: none recorded"
    }

    if ($Script:Warnings.Count -gt 0) {
        Write-Host "Warnings:"
        foreach ($item in $Script:Warnings) {
            Write-Host "  - $item"
        }
    } else {
        Write-Host "Warnings: none"
    }

    Write-Host ""
    Write-Host "Review before merge:"
    Write-Host "  git status"
    Write-Host "  git diff --stat $BaseBranch...HEAD"
    Write-Host "  git diff $BaseBranch...HEAD"
}

$repoRoot = Get-RepoRoot
Set-Location -LiteralPath $repoRoot

Write-Section "GitHub repository maintainer"
Write-Info "Mode: $Mode"
Write-Info "Apply: $Apply"
Write-Info "Push: $Push"
Write-Info "CreatePR: $CreatePR"

if ($CreatePR -and -not $Push) {
    Write-WarnLine "-CreatePR implies a branch must be pushed. The script will push when -Apply is set."
}

switch ($Mode) {
    "status" {
        Show-RepositoryStatus $repoRoot
        Show-FinalReport
        return
    }

    "check" {
        Show-RepositoryStatus $repoRoot
        Invoke-DetectedChecks $repoRoot
        Show-FinalReport
        return
    }

    "fix" {
        if (-not $Apply) {
            Write-WarnLine "Fix mode is preview-only without -Apply. Use -Apply to run safe autofix."
            Show-RepositoryStatus $repoRoot
            Show-FinalReport
            return
        }
        Ensure-Branch $Branch | Out-Null
        Invoke-SafeAutofix $repoRoot
        Invoke-DetectedChecks $repoRoot
        Show-FinalReport
        return
    }

    "commit" {
        $currentBranch = Ensure-Branch $Branch
        $changed = Get-ChangedPaths
        $paths = Select-StageablePaths $repoRoot $changed
        Stage-SelectedChanges $repoRoot $paths
        Commit-StagedChanges | Out-Null
        Show-FinalReport
        return
    }

    "pr" {
        $currentBranch = Ensure-Branch $Branch
        $changed = Get-ChangedPaths
        $paths = Select-StageablePaths $repoRoot $changed
        Stage-SelectedChanges $repoRoot $paths
        Commit-StagedChanges | Out-Null
        Push-Branch $currentBranch
        Create-PullRequest $currentBranch
        Show-FinalReport
        return
    }

    "full" {
        $currentBranch = Ensure-Branch $Branch
        if ($Apply) {
            Invoke-SafeAutofix $repoRoot
        } else {
            Write-WarnLine "Preview only: not running safe autofix because -Apply was not provided."
        }
        Invoke-DetectedChecks $repoRoot
        $changed = Get-ChangedPaths
        $paths = Select-StageablePaths $repoRoot $changed
        Stage-SelectedChanges $repoRoot $paths
        Commit-StagedChanges | Out-Null
        Push-Branch $currentBranch
        Create-PullRequest $currentBranch
        Show-FinalReport
        return
    }
}

<#
RESEARCH-GRADE-EXPANSION:BEGIN
Research-grade maintenance notes:
- Role: repository automation script.
- Review parameters, side effects, exit behavior, dry-run/apply boundaries, and failure output before changing this script.
- Keep examples public-safe and repository-relative; do not print secrets or inspect private machine state.
- When behavior changes, update tests or documented manual verification steps and record user-visible changes in the changelog.
RESEARCH-GRADE-EXPANSION:END
#>
