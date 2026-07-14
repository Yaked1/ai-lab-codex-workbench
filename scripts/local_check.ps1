$ErrorActionPreference = "Stop"

function Invoke-CheckedCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Command,
        [string[]]$Arguments = @()
    )

    & $Command @Arguments
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        exit $exitCode
    }
}

Write-Host "Running repository health check..."
Invoke-CheckedCommand -Command "python" -Arguments @("scripts/repo_health_check.py")

Write-Host "Running safe autofix check..."
Invoke-CheckedCommand -Command "python" -Arguments @("scripts/safe_autofix.py", "--check")

Write-Host "Running unit tests..."
Invoke-CheckedCommand -Command "python" -Arguments @("-m", "unittest", "discover", "-s", "tests")

Write-Host "All local checks passed. Miracles do happen, apparently."
exit 0
