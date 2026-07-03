$ErrorActionPreference = "Stop"

Write-Host "Running repository health check..."
python scripts/repo_health_check.py

Write-Host "Running safe autofix check..."
python scripts/safe_autofix.py --check

Write-Host "Running unit tests..."
python -m unittest discover -s tests

Write-Host "All local checks passed. Miracles do happen, apparently."

<#
#>
