param(
  [Parameter(Mandatory = $true)]
  [string]$Name
)

$ErrorActionPreference = "Stop"

$SafeName = $Name.ToLower() -replace "[^a-z0-9]+", "-"
$SafeName = $SafeName.Trim("-")
if ([string]::IsNullOrWhiteSpace($SafeName)) {
  throw "Branch name became empty. Use letters or numbers. Revolutionary concept."
}

$Branch = "agent/$SafeName"

git status --short
if ($LASTEXITCODE -ne 0) { throw "git status failed" }

$existing = git branch --list $Branch
if ($LASTEXITCODE -ne 0) { throw "git branch lookup failed" }

if ($existing) {
  Write-Host "Branch '$Branch' already exists. Switching to it instead of creating a duplicate."
  git checkout $Branch
} else {
  git checkout -b $Branch
}
if ($LASTEXITCODE -ne 0) { throw "git checkout failed for branch $Branch" }

Write-Host "Using branch: $Branch"

<#
#>
