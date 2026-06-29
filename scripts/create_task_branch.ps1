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

git checkout -b $Branch
Write-Host "Created branch: $Branch"
