# Install one or more skills from skills/ into an agent harness.
#
# Native PowerShell only -- no new dependency was added to run this. Works
# two ways: from inside a clone of this repository (copies local files), or
# standalone after downloading just this script (fetches the specific
# skill's files over plain HTTPS from the public GitHub repo). This script
# never executes anything it downloads -- it only reads Markdown/JSON text
# and writes it to the target path.

param(
  [string]$Skill,
  [switch]$All,
  [ValidateSet("claude-code", "claude-code-cli", "claude-code-desktop", "codex", "codex-cli", "codex-desktop", "hermes", "cursor", "windsurf", "aider", "antigravity", "github-copilot", "opencode", "kilo-code", "mcp")]
  [string]$Harness,
  [ValidateSet("project", "user")]
  [string]$Scope = "project",
  [switch]$List,
  [switch]$Force,
  [switch]$WhatIf
)

$ErrorActionPreference = "Stop"

$RawBase = "https://raw.githubusercontent.com/Yaked1/ai-lab-codex-workbench/main"
$ClaudeCodeHarnesses = @("claude-code", "claude-code-cli", "claude-code-desktop")
$CodexHarnesses = @("codex", "codex-cli", "codex-desktop")
$HermesHarnesses = @("hermes")
$NativeHarnesses = $ClaudeCodeHarnesses + $CodexHarnesses + $HermesHarnesses
$FlattenedStagedHarnesses = @("cursor", "windsurf", "aider", "antigravity", "github-copilot", "opencode", "kilo-code", "mcp")

function Get-RepoRoot {
  $here = Split-Path -Parent $PSScriptRoot
  if (Test-Path (Join-Path $here "skills/manifest.json")) {
    return $here
  }
  return $null
}

function Get-Manifest($Root) {
  if ($Root) {
    return Get-Content (Join-Path $Root "skills/manifest.json") -Raw | ConvertFrom-Json
  }
  return (Invoke-WebRequest -Uri "$RawBase/skills/manifest.json" -UseBasicParsing).Content | ConvertFrom-Json
}

function Get-SkillText($Root, $RelativePath) {
  if ($Root) {
    return Get-Content (Join-Path $Root $RelativePath) -Raw
  }
  return (Invoke-WebRequest -Uri "$RawBase/$RelativePath" -UseBasicParsing).Content
}

function Strip-Frontmatter([string]$Text) {
  $lines = $Text -split "`r?`n"
  if ($lines[0] -ne "---") { return $Text }
  for ($i = 1; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -eq "---") {
      $body = ($lines[($i + 1)..($lines.Count - 1)] -join "`n").TrimStart("`n")
      return "$body`n"
    }
  }
  return $Text
}

function Get-TargetPath([string]$HarnessName, [string]$ScopeName, [string]$Slug) {
  if ($ClaudeCodeHarnesses -contains $HarnessName) {
    if ($ScopeName -eq "user") { return Join-Path $HOME ".claude/skills/$Slug/SKILL.md" }
    return ".claude/skills/$Slug/SKILL.md"
  }
  if ($CodexHarnesses -contains $HarnessName) {
    if ($ScopeName -eq "user") { return Join-Path $HOME ".agents/skills/$Slug/SKILL.md" }
    return ".agents/skills/$Slug/SKILL.md"
  }
  if ($HermesHarnesses -contains $HarnessName) {
    if ($ScopeName -eq "user") { return Join-Path $HOME ".hermes/skills/$Slug/SKILL.md" }
    return ".agent-skills/hermes/$Slug/SKILL.md"
  }
  return ".agent-skills/$HarnessName/$Slug.md"
}

function Install-OneSkill($Root, [string]$Slug, [string]$HarnessName, [string]$ScopeName, [bool]$ForceWrite, [bool]$Preview) {
  $relPath = "skills/$Slug/SKILL.md"
  $text = Get-SkillText $Root $relPath
  $dest = Get-TargetPath $HarnessName $ScopeName $Slug

  if ($FlattenedStagedHarnesses -contains $HarnessName) {
    $text = Strip-Frontmatter $text
  }

  if ((Test-Path $dest) -and -not $ForceWrite -and -not $Preview) {
    Write-Host "SKIP  ${Slug}: $dest already exists (use -Force to overwrite)"
    return
  }

  if ($Preview) {
    Write-Host "WOULD WRITE  $Slug -> $dest"
    return
  }

  $destDir = Split-Path -Parent $dest
  if ($destDir -and -not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
  }
  Set-Content -Path $dest -Value $text -NoNewline -Encoding utf8
  Write-Host "OK    $Slug -> $dest"

  if ($FlattenedStagedHarnesses -contains $HarnessName) {
    Write-Host "      $HarnessName has no confirmed native skill-loading path. Paste the staged file above into ${HarnessName}'s own custom-instructions/rules mechanism -- see docs/tools/$HarnessName.md for its current location."
  } elseif ($CodexHarnesses -contains $HarnessName) {
    Write-Host "      Codex reads local skills from .agents/skills (project) or ~/.agents/skills (user). The same skill files are available to Codex CLI, IDE extension, and Codex app sessions that scan that location."
  } elseif ($ClaudeCodeHarnesses -contains $HarnessName) {
    Write-Host "      Claude Code reads skills from .claude/skills (project) or ~/.claude/skills (user). Start or refresh Claude Code from the target repo and invoke the skill by name if needed."
  } elseif ($HermesHarnesses -contains $HarnessName) {
    if ($ScopeName -eq "user") {
      Write-Host "      Hermes reads local skills from ~/.hermes/skills. Use /skills list or /<skill-name> in Hermes to confirm it is available."
    } else {
      Write-Host "      Hermes project scope is staged as a real SKILL.md folder. Add this directory to skills.external_dirs in ~/.hermes/config.yaml, or install the public repo path with 'hermes skills install Yaked1/ai-lab-codex-workbench/skills/$Slug' after the skill is published."
    }
  }
}

$Root = Get-RepoRoot

if ($List) {
  $manifest = Get-Manifest $Root
  foreach ($entry in $manifest.skills) {
    "{0,-40} [{1,-16}] {2}" -f $entry.slug, $entry.category, $entry.description
  }
  Write-Host ""
  $allHarnesses = ($NativeHarnesses + $FlattenedStagedHarnesses) | Sort-Object
  Write-Host "$($manifest.skills.Count) skills. Harnesses: $($allHarnesses -join ', ')"
  exit 0
}

if (-not $Harness) {
  throw "-Harness is required unless -List is given."
}
if (-not $Skill -and -not $All) {
  throw "Either -Skill <slug> or -All is required."
}

$manifest = Get-Manifest $Root
$knownSlugs = $manifest.skills | ForEach-Object { $_.slug }

if ($All) {
  $slugs = $knownSlugs
} else {
  if ($knownSlugs -notcontains $Skill) {
    throw "Unknown skill slug '$Skill'. Run -List to see valid slugs."
  }
  $slugs = @($Skill)
}

foreach ($s in $slugs) {
  Install-OneSkill -Root $Root -Slug $s -HarnessName $Harness -ScopeName $Scope -ForceWrite $Force.IsPresent -Preview $WhatIf.IsPresent
}
