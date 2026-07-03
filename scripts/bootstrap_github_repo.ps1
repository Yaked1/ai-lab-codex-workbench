param(
  [string]$RepoName = "ai-lab-codex-workbench",
  [ValidateSet("private", "public")]
  [string]$Visibility = "private"
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  throw "Git is not installed. Run: winget install Git.Git"
}

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
  throw "GitHub CLI is not installed. Run: winget install GitHub.cli"
}

gh auth status *> $null
if ($LASTEXITCODE -ne 0) {
  throw "GitHub CLI is not signed in. Run: gh auth login"
}

if (-not (Test-Path ".git")) {
  git init
}

git add .
git commit -m "Initial Codex automation workbench" *> $null
if ($LASTEXITCODE -ne 0) {
  Write-Host "Nothing to commit or commit failed. Continuing cautiously."
}

$existingRemote = git remote get-url origin 2>$null
if ($LASTEXITCODE -eq 0 -and -not [string]::IsNullOrWhiteSpace($existingRemote)) {
  Write-Host "Remote 'origin' already points to $existingRemote."
  $branch = (git branch --show-current).Trim()
  if ([string]::IsNullOrWhiteSpace($branch)) {
    throw "Could not determine the current branch to push. Resolve detached HEAD and rerun."
  }
  Write-Host "Pushing branch '$branch' instead of creating a new repository."
  git push -u origin $branch
  if ($LASTEXITCODE -ne 0) { throw "git push failed for branch $branch." }
} else {
  $VisibilityFlag = if ($Visibility -eq "public") { "--public" } else { "--private" }
  gh repo create $RepoName $VisibilityFlag --source . --remote origin --push
  if ($LASTEXITCODE -ne 0) { throw "gh repo create failed." }
  Write-Host "Repository created and pushed: $RepoName"
}

Write-Host "Now enable Actions PR creation if you want autofix PRs: Settings -> Actions -> General -> Workflow permissions."

<#
#>
