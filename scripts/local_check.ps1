$ErrorActionPreference = "Stop"

Write-Host "Running repository health check..."
python scripts/repo_health_check.py

Write-Host "Running safe autofix check..."
python scripts/safe_autofix.py --check

Write-Host "Running unit tests..."
python -m unittest discover -s tests

Write-Host "All local checks passed. Miracles do happen, apparently."

<#
RESEARCH-GRADE-EXPANSION:BEGIN
Research-grade maintenance notes:
- Role: repository automation script.
- Review parameters, side effects, exit behavior, dry-run/apply boundaries, and failure output before changing this script.
- Keep examples public-safe and repository-relative; do not print secrets or inspect private machine state.
- When behavior changes, update tests or documented manual verification steps and record user-visible changes in the changelog.
RESEARCH-GRADE-EXPANSION:END
#>
