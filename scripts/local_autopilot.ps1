param(
    [ValidateSet("status", "scout", "prompt", "local-codex", "full-safe")]
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
    $runId = (& gh run list --workflow $Workflow --limit 1 --json databaseId --jq ".[0].databaseId").Trim()
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($runId)) {
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

function Use-CodexBranch {
    param([string]$BranchName)
    $existing = (& git branch --list $BranchName).Trim()
    if ($LASTEXITCODE -ne 0) {
        throw "git branch lookup failed."
    }
    if ($existing) {
        Invoke-Native git @("switch", $BranchName)
    } else {
        Invoke-Native git @("switch", "-c", $BranchName)
    }
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
    Write-Host "Next step: run local-codex mode to create a local branch and start Codex manually."
}

function Invoke-LocalCodex {
    Assert-CleanTree
    Assert-CommandAvailable "codex"
    Switch-ToMainAndPull
    Use-CodexBranch $Branch
    Copy-LatestCuratorPrompt | Out-Null
    Write-Host "Starting Codex on branch $Branch. No commits will be made by this script."
    & codex
    if ($LASTEXITCODE -ne 0) {
        throw "codex exited with code $LASTEXITCODE."
    }
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
    Write-Host "Next step: use -Mode scout, -Mode prompt, or -Mode full-safe when the tree is clean."
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
        Invoke-LocalCodex
    }
    "full-safe" {
        Invoke-Scout
        Invoke-Prompt
        Invoke-LocalCodex
    }
}
