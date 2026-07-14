param(
  [string]$RepoName = "ai-lab-codex-workbench",
  [ValidateSet("private", "public")]
  [string]$Visibility = "private",
  [string]$CommitMessage = "Initial Codex automation workbench",
  [switch]$Apply
)

$ErrorActionPreference = "Stop"

function ConvertTo-WindowsCommandLineArgument {
  param([AllowEmptyString()][string]$Value)

  if ($Value.Length -gt 0 -and $Value -notmatch '[\s"]') {
    return $Value
  }

  $builder = [System.Text.StringBuilder]::new()
  [void]$builder.Append('"')
  $backslashes = 0
  foreach ($character in $Value.ToCharArray()) {
    if ($character -eq '\') {
      $backslashes += 1
      continue
    }
    if ($character -eq '"') {
      [void]$builder.Append(('\' * (($backslashes * 2) + 1)))
      [void]$builder.Append('"')
      $backslashes = 0
      continue
    }
    if ($backslashes -gt 0) {
      [void]$builder.Append(('\' * $backslashes))
      $backslashes = 0
    }
    [void]$builder.Append($character)
  }
  if ($backslashes -gt 0) {
    [void]$builder.Append(('\' * ($backslashes * 2)))
  }
  [void]$builder.Append('"')
  return $builder.ToString()
}

function Invoke-GitCommand {
  param(
    [Parameter(Mandatory = $true)][string[]]$Arguments,
    [switch]$AllowFailure
  )

  $gitCommand = Get-Command git -CommandType Application -ErrorAction Stop |
    Select-Object -First 1
  $processInfo = [System.Diagnostics.ProcessStartInfo]::new()
  $processInfo.FileName = $gitCommand.Path
  $processInfo.WorkingDirectory = (Get-Location).Path
  $processInfo.UseShellExecute = $false
  $processInfo.CreateNoWindow = $true
  $processInfo.RedirectStandardOutput = $true
  $processInfo.RedirectStandardError = $true
  $gitArguments = @("-c", "core.quotepath=false") + $Arguments
  $processInfo.Arguments = ($gitArguments | ForEach-Object {
      ConvertTo-WindowsCommandLineArgument ([string]$_)
    }) -join " "

  $process = [System.Diagnostics.Process]::new()
  try {
    $process.StartInfo = $processInfo
    if (-not $process.Start()) {
      throw "Could not start Git."
    }
    $standardOutputTask = $process.StandardOutput.ReadToEndAsync()
    $standardErrorTask = $process.StandardError.ReadToEndAsync()
    $process.WaitForExit()
    $standardOutput = $standardOutputTask.GetAwaiter().GetResult()
    $standardError = $standardErrorTask.GetAwaiter().GetResult()
    $exitCode = $process.ExitCode
  }
  finally {
    $process.Dispose()
  }

  $result = [pscustomobject]@{
    ExitCode = $exitCode
    Stdout = $standardOutput
    Stderr = $standardError
  }
  if (-not $AllowFailure -and $result.ExitCode -ne 0) {
    $detail = $result.Stderr.Trim()
    if ([string]::IsNullOrWhiteSpace($detail)) {
      $detail = $result.Stdout.Trim()
    }
    throw "git $($Arguments -join ' ') failed with exit code $($result.ExitCode): $detail"
  }
  return $result
}

function Invoke-ToolCommand {
  param(
    [Parameter(Mandatory = $true)][string]$FilePath,
    [Parameter(Mandatory = $true)][string[]]$Arguments,
    [switch]$Quiet
  )

  $previousPreference = $ErrorActionPreference
  try {
    $ErrorActionPreference = "Continue"
    $output = & $FilePath @Arguments 2>&1
    $exitCode = $LASTEXITCODE
  }
  finally {
    $ErrorActionPreference = $previousPreference
  }
  if (-not $Quiet) {
    foreach ($line in @($output)) {
      Write-Host ([string]$line)
    }
  }
  return [pscustomobject]@{
    ExitCode = $exitCode
    Output = @($output)
  }
}

function ConvertFrom-GitPathOutput {
  param([string]$Output)

  $paths = @()
  foreach ($line in ($Output -split "`r?`n")) {
    if ([string]::IsNullOrWhiteSpace($line)) {
      continue
    }
    if ($line.StartsWith('"') -or $line.EndsWith('"')) {
      throw "Git reported a quoted path that this bootstrap cannot stage safely: $line"
    }
    if ([System.IO.Path]::IsPathRooted($line) -or $line -match '(^|/|\\)\.\.(/|\\|$)') {
      throw "Git reported a path outside the repository boundary: $line"
    }
    $paths += $line.Replace('\', '/')
  }
  return @($paths)
}

function Get-GitCandidatePaths {
  $outputs = @(
    (Invoke-GitCommand -Arguments @("diff", "--no-renames", "--name-only", "--relative", "--")).Stdout,
    (Invoke-GitCommand -Arguments @("diff", "--cached", "--no-renames", "--name-only", "--relative", "--")).Stdout,
    (Invoke-GitCommand -Arguments @("ls-files", "--others", "--exclude-standard", "--")).Stdout
  )
  $paths = foreach ($output in $outputs) {
    ConvertFrom-GitPathOutput -Output $output
  }
  return @($paths | Sort-Object -CaseSensitive -Unique)
}

function Get-FilesystemCandidatePaths {
  param([Parameter(Mandatory = $true)][string]$Root)

  $rootPrefix = $Root.TrimEnd('\', '/') + [System.IO.Path]::DirectorySeparatorChar
  $gitMetadataPath = Join-Path $Root ".git"
  $gitMetadataPrefix = $gitMetadataPath.TrimEnd('\', '/') +
    [System.IO.Path]::DirectorySeparatorChar
  $paths = foreach ($file in Get-ChildItem -LiteralPath $Root -File -Force -Recurse) {
    if (
      $file.FullName.Equals($gitMetadataPath, [System.StringComparison]::OrdinalIgnoreCase) -or
      $file.FullName.StartsWith($gitMetadataPrefix, [System.StringComparison]::OrdinalIgnoreCase)
    ) {
      continue
    }
    $file.FullName.Substring($rootPrefix.Length).Replace('\', '/')
  }
  return @($paths | Sort-Object -CaseSensitive -Unique)
}

function Find-GitMetadataPath {
  param([Parameter(Mandatory = $true)][string]$StartPath)

  $directory = [System.IO.DirectoryInfo]::new($StartPath)
  while ($null -ne $directory) {
    $candidate = Join-Path $directory.FullName ".git"
    if (Test-Path -LiteralPath $candidate) {
      return $candidate
    }
    $directory = $directory.Parent
  }
  return $null
}

function Assert-ExactPathSet {
  param(
    [Parameter(Mandatory = $true)][AllowEmptyCollection()][string[]]$Expected,
    [Parameter(Mandatory = $true)][AllowEmptyCollection()][string[]]$Actual,
    [Parameter(Mandatory = $true)][string]$FailureMessage
  )

  $expectedSorted = @($Expected | Sort-Object -CaseSensitive -Unique)
  $actualSorted = @($Actual | Sort-Object -CaseSensitive -Unique)
  if (($actualSorted -join "`n") -cne ($expectedSorted -join "`n")) {
    throw $FailureMessage
  }
}

function Get-CandidateFileSnapshot {
  param(
    [Parameter(Mandatory = $true)][string]$Root,
    [Parameter(Mandatory = $true)][AllowEmptyCollection()][string[]]$Paths
  )

  $snapshot = [ordered]@{}
  foreach ($path in $Paths) {
    $fullPath = Join-Path $Root $path
    if (-not (Test-Path -LiteralPath $fullPath)) {
      $snapshot[$path] = "<deleted>"
      continue
    }
    if (-not (Test-Path -LiteralPath $fullPath -PathType Leaf)) {
      throw "Candidate path is not a file and cannot be reviewed safely: $path"
    }
    $snapshot[$path] = (Get-FileHash -LiteralPath $fullPath -Algorithm SHA256).Hash
  }
  return $snapshot
}

function Assert-CandidateSnapshotUnchanged {
  param(
    [Parameter(Mandatory = $true)][string]$Root,
    [Parameter(Mandatory = $true)][AllowEmptyCollection()][string[]]$ExpectedPaths,
    [Parameter(Mandatory = $true)]$ExpectedSnapshot,
    [Parameter(Mandatory = $true)][bool]$HasRepository
  )

  [string[]]$actualPaths = @(
    if ($HasRepository) {
      Get-GitCandidatePaths
    }
    else {
      Get-FilesystemCandidatePaths -Root $Root
    }
  )
  Assert-ExactPathSet -Expected $ExpectedPaths -Actual $actualPaths `
    -FailureMessage "The candidate path set changed while health and secret checks were running. No files were staged."
  $actualSnapshot = Get-CandidateFileSnapshot -Root $Root -Paths $actualPaths
  foreach ($path in $ExpectedPaths) {
    if ($actualSnapshot[$path] -cne $ExpectedSnapshot[$path]) {
      throw "Candidate content changed while health and secret checks were running: $path. No files were staged."
    }
  }
}

function Get-GitWorktreeBlobSnapshot {
  param([Parameter(Mandatory = $true)][AllowEmptyCollection()][string[]]$Paths)

  $snapshot = [ordered]@{}
  foreach ($path in $Paths) {
    if (-not (Test-Path -LiteralPath $path)) {
      $snapshot[$path] = "<deleted>"
      continue
    }
    $blob = Invoke-GitCommand -Arguments @("hash-object", "--path=$path", "--", $path)
    $snapshot[$path] = $blob.Stdout.Trim()
  }
  return $snapshot
}

function Assert-BlobSnapshotUnchanged {
  param(
    [Parameter(Mandatory = $true)][AllowEmptyCollection()][string[]]$Paths,
    [Parameter(Mandatory = $true)]$ExpectedSnapshot,
    [Parameter(Mandatory = $true)]$ActualSnapshot,
    [Parameter(Mandatory = $true)][string]$FailureMessage
  )

  foreach ($path in $Paths) {
    if ($ActualSnapshot[$path] -cne $ExpectedSnapshot[$path]) {
      throw "$FailureMessage Path: $path"
    }
  }
}

function Assert-StagedBlobsMatchSnapshot {
  param(
    [Parameter(Mandatory = $true)][AllowEmptyCollection()][string[]]$Paths,
    [Parameter(Mandatory = $true)]$ExpectedSnapshot
  )

  foreach ($path in $Paths) {
    $stage = Invoke-GitCommand -Arguments @("ls-files", "--stage", "--", $path)
    $stageLines = @($stage.Stdout -split "`r?`n" | Where-Object { $_.Length -gt 0 })
    if ($ExpectedSnapshot[$path] -ceq "<deleted>") {
      if ($stageLines.Count -ne 0) {
        throw "The staged deletion does not match the reviewed candidate snapshot: $path"
      }
      continue
    }
    if ($stageLines.Count -ne 1 -or $stageLines[0] -notmatch '^[0-9]{6} ([0-9a-f]{40}|[0-9a-f]{64}) 0\t') {
      throw "Could not verify the staged blob for reviewed candidate: $path"
    }
    if ($Matches[1] -cne $ExpectedSnapshot[$path]) {
      throw "The staged bytes differ from the reviewed candidate snapshot: $path"
    }
  }
}

function Write-CandidatePaths {
  param([Parameter(Mandatory = $true)][AllowEmptyCollection()][string[]]$Paths)

  Write-Host "Candidate paths ($($Paths.Count)):"
  if ($Paths.Count -eq 0) {
    Write-Host "  (none)"
    return
  }
  foreach ($path in $Paths) {
    Write-Host "  - $path"
  }
}

function Assert-ExactStagedSet {
  param([Parameter(Mandatory = $true)][AllowEmptyCollection()][string[]]$Expected)

  [string[]]$actual = @(
    ConvertFrom-GitPathOutput -Output (
      Invoke-GitCommand -Arguments @("diff", "--cached", "--no-renames", "--name-only", "--relative", "--")
    ).Stdout
  )
  Assert-ExactPathSet -Expected $Expected -Actual $actual `
    -FailureMessage "The staged path set differs from the reviewed candidate path set. No commit was created."
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  throw "Git is not installed. Run: winget install Git.Git"
}
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
  throw "Python is not installed or is not available on PATH."
}

$startingDirectory = (Get-Location).Path
$repoProbe = Invoke-GitCommand -Arguments @("rev-parse", "--show-toplevel") -AllowFailure
$hasRepository = $repoProbe.ExitCode -eq 0
if (-not $hasRepository) {
  $existingMetadata = Find-GitMetadataPath -StartPath $startingDirectory
  if ($null -ne $existingMetadata) {
    throw "Git repository detection failed while existing Git metadata is present at '$existingMetadata'. Repair or remove that metadata explicitly before initializing a repository."
  }
  $probeDetail = ($repoProbe.Stderr + "`n" + $repoProbe.Stdout).Trim()
  if ($repoProbe.ExitCode -ne 128 -or $probeDetail -notmatch 'not a git repository') {
    throw "Could not safely determine whether this directory is a Git repository. git rev-parse exited $($repoProbe.ExitCode): $probeDetail"
  }
}
$repoRoot = if ($hasRepository) { $repoProbe.Stdout.Trim() } else { $startingDirectory }
Set-Location -LiteralPath $repoRoot

try {
  [string[]]$candidatePaths = @(
    if ($hasRepository) {
      Get-GitCandidatePaths
    }
    else {
      Get-FilesystemCandidatePaths -Root $repoRoot
    }
  )
  Write-CandidatePaths -Paths $candidatePaths
  $candidateSnapshot = Get-CandidateFileSnapshot -Root $repoRoot -Paths $candidatePaths
  $reviewedBlobSnapshot = if ($hasRepository) {
    Get-GitWorktreeBlobSnapshot -Paths $candidatePaths
  }
  else {
    $null
  }
  Assert-CandidateSnapshotUnchanged -Root $repoRoot -ExpectedPaths $candidatePaths `
    -ExpectedSnapshot $candidateSnapshot -HasRepository $hasRepository

  $health = Invoke-ToolCommand -FilePath "python" -Arguments @(
    "scripts/repo_health_check.py", "--root", $repoRoot
  )
  if ($health.ExitCode -ne 0) {
    $healthDetail = ($health.Output | ForEach-Object { [string]$_ }) -join [Environment]::NewLine
    throw "Repository health and secret checks failed with exit code $($health.ExitCode). No files were staged. $healthDetail"
  }
  Assert-CandidateSnapshotUnchanged -Root $repoRoot -ExpectedPaths $candidatePaths `
    -ExpectedSnapshot $candidateSnapshot -HasRepository $hasRepository
  if ($hasRepository) {
    $postHealthBlobSnapshot = Get-GitWorktreeBlobSnapshot -Paths $candidatePaths
    Assert-BlobSnapshotUnchanged -Paths $candidatePaths `
      -ExpectedSnapshot $reviewedBlobSnapshot -ActualSnapshot $postHealthBlobSnapshot `
      -FailureMessage "Candidate Git bytes changed while health and secret checks were running. No files were staged."
  }
  Write-Host "Repository health and secret checks passed."

  if (-not $Apply) {
    Write-Host "Preview only. No files were staged, committed, pushed, or published."
    Write-Host "Review the candidate list, then rerun with -Apply to authorize changes."
    exit 0
  }

  if (-not $hasRepository) {
    Invoke-GitCommand -Arguments @("init", "-b", "main") | Out-Null
    $hasRepository = $true
    [string[]]$candidatePaths = @(Get-GitCandidatePaths)
    Assert-ExactPathSet -Expected $candidateSnapshot.Keys -Actual $candidatePaths `
      -FailureMessage "The candidate path set changed while Git was initialized. No files were staged."
    Assert-CandidateSnapshotUnchanged -Root $repoRoot -ExpectedPaths $candidatePaths `
      -ExpectedSnapshot $candidateSnapshot -HasRepository $true
    $reviewedBlobSnapshot = Get-GitWorktreeBlobSnapshot -Paths $candidatePaths
    Assert-CandidateSnapshotUnchanged -Root $repoRoot -ExpectedPaths $candidatePaths `
      -ExpectedSnapshot $candidateSnapshot -HasRepository $true
    Write-Host "Git initialized. Final reviewed candidate set:"
    Write-CandidatePaths -Paths $candidatePaths
  }

  if ($candidatePaths.Count -gt 0) {
    $identity = Invoke-GitCommand -Arguments @("var", "GIT_AUTHOR_IDENT") -AllowFailure
    if ($identity.ExitCode -ne 0) {
      throw "Git commit identity is not configured. Set user.name and user.email, then rerun with -Apply. No files were staged."
    }
  }
  Write-Host "Apply was requested. Staging only the listed candidate paths."
  [string[]]$stageableCandidatePaths = @(
    foreach ($path in $candidatePaths) {
      if (Test-Path -LiteralPath $path) {
        $path
        continue
      }
      $indexProbe = Invoke-GitCommand -Arguments @("ls-files", "--error-unmatch", "--", $path) -AllowFailure
      if ($indexProbe.ExitCode -eq 0) {
        $path
      }
      elseif ($indexProbe.ExitCode -ne 1) {
        throw "Could not determine whether deleted candidate '$path' remains in the index."
      }
    }
  )
  if ($stageableCandidatePaths.Count -gt 0) {
    # Equivalent command: git add -A -- <reviewed candidate paths>
    $addArguments = @("add", "-A", "--") + $stageableCandidatePaths
    Invoke-GitCommand -Arguments $addArguments | Out-Null
  }
  Assert-ExactStagedSet -Expected $candidatePaths
  Assert-StagedBlobsMatchSnapshot -Paths $candidatePaths -ExpectedSnapshot $reviewedBlobSnapshot

  $stagedCheck = Invoke-GitCommand -Arguments @("diff", "--cached", "--quiet", "--exit-code") -AllowFailure
  if ($stagedCheck.ExitCode -eq 0) {
    Write-Host "No staged changes to commit."
  }
  elseif ($stagedCheck.ExitCode -eq 1) {
    $expectedTree = (Invoke-GitCommand -Arguments @("write-tree")).Stdout.Trim()
    $commit = Invoke-GitCommand -Arguments @("commit", "-m", $CommitMessage) -AllowFailure
    if ($commit.ExitCode -ne 0) {
      $detail = $commit.Stderr.Trim()
      throw "git commit failed after a non-empty staged-set check. Inspect the enabled hooks and Git output. $detail"
    }
    $committedTree = (Invoke-GitCommand -Arguments @("rev-parse", "HEAD^{tree}")).Stdout.Trim()
    if ($committedTree -cne $expectedTree) {
      throw "The commit tree differs from the reviewed staged tree. The local commit remains for inspection; no push was attempted."
    }
  }
  else {
    throw "Could not determine whether the staged index is empty. git diff exited $($stagedCheck.ExitCode)."
  }

  $head = Invoke-GitCommand -Arguments @("rev-parse", "--verify", "HEAD") -AllowFailure
  if ($head.ExitCode -ne 0) {
    throw "No commit exists to publish. Add a reviewed candidate and rerun with -Apply."
  }

  $existingRemote = Invoke-GitCommand -Arguments @("remote", "get-url", "origin") -AllowFailure
  if ($existingRemote.ExitCode -eq 0 -and -not [string]::IsNullOrWhiteSpace($existingRemote.Stdout)) {
    $remoteUrl = $existingRemote.Stdout.Trim()
    Write-Host "Remote 'origin' already points to $remoteUrl."
    $branch = (Invoke-GitCommand -Arguments @("branch", "--show-current")).Stdout.Trim()
    if ([string]::IsNullOrWhiteSpace($branch)) {
      throw "Could not determine the current branch to push. Resolve detached HEAD and rerun."
    }
    Write-Host "Pushing branch '$branch' instead of creating a new repository."
    Invoke-GitCommand -Arguments @("push", "-u", "origin", $branch) | Out-Null
  }
  else {
    if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
      throw "GitHub CLI is not installed. Run: winget install GitHub.cli"
    }
    $auth = Invoke-ToolCommand -FilePath "gh" -Arguments @("auth", "status") -Quiet
    if ($auth.ExitCode -ne 0) {
      $authDetail = ($auth.Output | ForEach-Object { [string]$_ }) -join [Environment]::NewLine
      throw "GitHub CLI is not signed in. Run: gh auth login. $authDetail"
    }
    $visibilityFlag = if ($Visibility -eq "public") { "--public" } else { "--private" }
    $create = Invoke-ToolCommand -FilePath "gh" -Arguments @(
      "repo", "create", $RepoName, $visibilityFlag, "--source", ".", "--remote", "origin", "--push"
    )
    if ($create.ExitCode -ne 0) {
      throw "gh repo create failed with exit code $($create.ExitCode)."
    }
    Write-Host "Repository created and pushed: $RepoName"
  }

  Write-Host "Now enable Actions PR creation if you want autofix PRs: Settings -> Actions -> General -> Workflow permissions."
}
finally {
  Set-Location -LiteralPath $startingDirectory
}
