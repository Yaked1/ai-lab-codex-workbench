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

if (-not (Test-Path ".git")) {
  git init
}

git add .
try {
  git commit -m "Initial Codex automation workbench"
} catch {
  Write-Host "Nothing to commit or commit failed. Continuing cautiously."
}

$VisibilityFlag = if ($Visibility -eq "public") { "--public" } else { "--private" }

gh repo create $RepoName $VisibilityFlag --source . --remote origin --push

Write-Host "Repository created and pushed: $RepoName"
Write-Host "Now enable Actions PR creation if you want autofix PRs: Settings -> Actions -> General -> Workflow permissions."
