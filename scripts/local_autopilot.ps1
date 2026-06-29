param(
    [ValidateSet("status", "scout", "prompt", "local-codex", "local-claude", "full-safe")]
    [string]$Mode = "status",

    [ValidateSet("skills", "prompt-guides", "image-guides", "model-guides", "hermes-agent", "all")]
    [string]$Scope = "hermes-agent",

    [bool]$DryRun = $true,

    [int]$MaxSources = 5,

    [string]$Branch = "codex/curate-research-guides",

    [switch]$AllowDirty
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Capture whether the caller passed -Branch before the switch runs so each
# local agent mode can fall back to its own default branch when it was omitted.
$BranchWasProvided = $PSBoundParameters.ContainsKey("Branch")

function Test-CommandAvailable {
    param([string]$Name)
    return [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

function Invoke-Native {
    param(
        [string]$File,
        [string[]]$Arguments
    )
    & $File @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$File failed with exit code $LASTEXITCODE."
    }
}

function Assert-CommandAvailable {
    param([string]$Name)
    if (-not (Test-CommandAvailable $Name)) {
        throw "Required command '$Name' was not found on PATH."
    }
}

function Assert-CleanTree {
    if ($AllowDirty) {
        Write-Host "AllowDirty is set; continuing with a dirty-tree override."
        return
    }
    $dirty = (& git status --porcelain)
    if ($LASTEXITCODE -ne 0) {
        throw "git status failed."
    }
    if ($dirty) {
        Write-Host "Working tree is dirty:"
        & git status --short
        throw "Refusing to continue. Commit, stash, or rerun with -AllowDirty after reviewing the risk."
    }
}

function Get-LatestMarkdown {
    param(
        [string]$Directory,
        [string]$Filter
    )
    if (-not (Test-Path -LiteralPath $Directory)) {
        return $null
    }
    return Get-ChildItem -LiteralPath $Directory -Filter $Filter -File |
        Sort-Object LastWriteTimeUtc, Name -Descending |
        Select-Object -First 1
}

function Show-LatestFiles {
    param(
        [string]$Title,
        [string]$Directory,
        [string]$Filter
    )
    Write-Host ""
    Write-Host $Title
    if (-not (Test-Path -LiteralPath $Directory)) {
        Write-Host "  none"
        return
    }
    $files = Get-ChildItem -LiteralPath $Directory -Filter $Filter -File |
        Sort-Object LastWriteTimeUtc, Name -Descending |
        Select-Object -First 5
    if (-not $files) {
        Write-Host "  none"
        return
    }
    foreach ($file in $files) {
        Write-Host "  $($file.FullName)"
    }
}

function Switch-ToMainAndPull {
    Invoke-Native git @("switch", "main")
    Invoke-Native git @("pull", "--ff-only", "origin", "main")
}

function Watch-LatestWorkflowRun {
    param([string]$Workflow)
    Assert-CommandAvailable "gh"
    Start-Sleep -Seconds 5
    $runIdRaw = & gh run list --workflow $Workflow --limit 1 --json databaseId --jq ".[0].databaseId"
    if ($LASTEXITCODE -ne 0) {
        throw "Could not query workflow runs for $Workflow."
    }
    # gh can return $null (no runs) or an array; coerce to a string before trimming
    # so this never calls .Trim() on a null-valued expression.
    $runId = if ($null -ne $runIdRaw) { ([string]$runIdRaw).Trim() } else { "" }
    if ([string]::IsNullOrWhiteSpace($runId)) {
        throw "Could not find a recent run for $Workflow."
    }
    Invoke-Native gh @("run", "watch", $runId, "--exit-status")
}

function Copy-LatestCuratorPrompt {
    $prompt = Get-LatestMarkdown "docs/research/curated" "curator-prompt-*.md"
    if (-not $prompt) {
        throw "No curator prompt was found in docs/research/curated."
    }
    $text = Get-Content -LiteralPath $prompt.FullName -Raw
    Set-Clipboard -Value $text
    Write-Host "Copied curator prompt to clipboard: $($prompt.FullName)"
    return $prompt
}

function Test-BranchExists {
    param([string]$Branch)
    $matched = & git branch --list $Branch
    if ($LASTEXITCODE -ne 0) {
        throw "git branch lookup failed."
    }
    # git branch --list returns $null when nothing matches; under Set-StrictMode
    # calling .Trim() on that null is the bug this guard removes. Treat $null,
    # an empty string, and a multi-line array uniformly.
    foreach ($line in @($matched)) {
        if (-not [string]::IsNullOrWhiteSpace($line)) {
            return $true
        }
    }
    return $false
}

function Use-AgentBranch {
    param([string]$Branch)
    if (Test-BranchExists $Branch) {
        Write-Host "Switching to existing branch $Branch."
        Invoke-Native git @("switch", $Branch)
    } else {
        Write-Host "Creating branch $Branch from main."
        Invoke-Native git @("switch", "-c", $Branch)
    }
}

function Merge-MainFastForward {
    # Bring in the latest main without creating a merge commit. A fast-forward
    # only succeeds when the branch has not diverged from main. After a previous
    # squash merge the curation branch will have diverged, so a failure here is
    # expected and non-fatal: warn and continue instead of aborting the run.
    & git merge --ff-only main
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Could not fast-forward main into this branch (it has diverged from main). Continuing without merging; rebase or recreate the branch if you need the latest main."
    } else {
        Write-Host "Merged the latest main into this branch with --ff-only."
    }
}

function Invoke-LocalAgent {
    param(
        [string]$Command,
        [string]$Branch
    )
    Assert-CleanTree
    Assert-CommandAvailable $Command
    Switch-ToMainAndPull
    Use-AgentBranch $Branch
    Merge-MainFastForward
    Copy-LatestCuratorPrompt | Out-Null
    Write-Host "Starting '$Command' on branch $Branch."
    Write-Host "This script makes no commits, never merges pull requests, never force-pushes, and never deletes branches."
    & $Command
    if ($LASTEXITCODE -ne 0) {
        throw "$Command exited with code $LASTEXITCODE."
    }
}

function Resolve-AgentBranch {
    param([string]$DefaultBranch)
    if ($BranchWasProvided) {
        return $Branch
    }
    return $DefaultBranch
}

function Invoke-Scout {
    Assert-CleanTree
    Assert-CommandAvailable "gh"
    Switch-ToMainAndPull
    Invoke-Native gh @("workflow", "run", "daily-research-scout.yml")
    Watch-LatestWorkflowRun "daily-research-scout.yml"
    Invoke-Native git @("pull", "--ff-only", "origin", "main")
    $report = Get-LatestMarkdown "docs/research/inbox" "*.md"
    if ($report) {
        Write-Host "Latest generated report: $($report.FullName)"
    }
    Write-Host "Next step: run prompt mode when you are ready to prepare a local curator prompt."
}

function Invoke-Prompt {
    Assert-CleanTree
    Assert-CommandAvailable "gh"
    Switch-ToMainAndPull
    $dryRunText = $DryRun.ToString().ToLowerInvariant()
    Invoke-Native gh @(
        "workflow", "run", "curator-prompt-prep.yml",
        "-f", "scope=$Scope",
        "-f", "dry_run=$dryRunText",
        "-f", "max_sources=$MaxSources"
    )
    Watch-LatestWorkflowRun "curator-prompt-prep.yml"
    Invoke-Native git @("pull", "--ff-only", "origin", "main")
    $prompt = Copy-LatestCuratorPrompt
    Write-Host "Prompt path: $($prompt.FullName)"
    Write-Host "Next step: run local-codex or local-claude mode to create a local branch and start your agent manually."
}

function Show-Status {
    Write-Host "Git status"
    Invoke-Native git @("status", "--short", "--branch")
    Write-Host ""
    Write-Host "Current branch"
    Invoke-Native git @("branch", "--show-current")

    if (Test-CommandAvailable "gh") {
        Write-Host ""
        Write-Host "Latest 5 GitHub workflow runs"
        & gh run list --limit 5
        Write-Host ""
        Write-Host "Open issues"
        & gh issue list --limit 10
    } else {
        Write-Host ""
        Write-Host "GitHub CLI not found; skipping workflow runs and issues."
    }

    Show-LatestFiles "Latest research inbox files" "docs/research/inbox" "*.md"
    Show-LatestFiles "Latest curator prompt files" "docs/research/curated" "curator-prompt-*.md"
    Write-Host ""
    Write-Host "Next step: use -Mode scout, -Mode prompt, -Mode local-codex, -Mode local-claude, or -Mode full-safe when the tree is clean."
}

Assert-CommandAvailable "git"

switch ($Mode) {
    "status" {
        Show-Status
    }
    "scout" {
        Invoke-Scout
    }
    "prompt" {
        Invoke-Prompt
    }
    "local-codex" {
        Invoke-LocalAgent -Command "codex" -Branch (Resolve-AgentBranch "codex/curate-research-guides")
    }
    "local-claude" {
        Invoke-LocalAgent -Command "claude" -Branch (Resolve-AgentBranch "claude/curate-research-guides")
    }
    "full-safe" {
        Invoke-Scout
        Invoke-Prompt
        Invoke-LocalAgent -Command "codex" -Branch (Resolve-AgentBranch "codex/curate-research-guides")
    }
}
