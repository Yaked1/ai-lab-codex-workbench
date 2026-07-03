---
name: install-this-skill-pack
description: Use when a human wants to install one or more skills from this repository into Codex CLI/app, Claude Code CLI/project sessions, Hermes Agent, or another agent harness, and needs the exact command for their setup.
category: meta
source:
  - skills/README.md
  - scripts/install_skill.ps1
  - scripts/install_skill.py
---

# Install This Skill Pack

## Trigger

Use this skill when a human asks how to get a skill from this repository
running in their own agent harness -- "how do I install this," "download
this skill for Claude Code," or similar. Do not use it to explain what a
skill's content means -- that is the individual skill's own `SKILL.md`.

## Purpose

Give a human (or another agent acting on their behalf) the exact, minimal
command to copy a skill from this repository into their harness's real
skill-loading location, or, if that harness has no such location, into a
clearly labeled staging file with instructions for where to paste it.

## Inputs

- Which skill(s): a specific `<slug>` from `skills/INDEX.md`, or "all."
- Which harness: `codex-cli`, `codex-desktop`, `codex`,
  `claude-code-cli`, `claude-code-desktop`, `claude-code`, `hermes`,
  `cursor`, `windsurf`, `aider`, `antigravity`, `github-copilot`,
  `opencode`, `kilo-code`, or `mcp`.
- Install scope, if relevant: `project` (default) or `user`.
- Whether the human already has this repository cloned locally.

## Scope

This skill only runs `scripts/install_skill.ps1` or
`scripts/install_skill.py` with the inputs above. It never edits
`skills/`, never modifies the target harness's other configuration, and
never overwrites an existing installed skill without an explicit `-Force`
confirmation from the human.

## Procedure

1. Confirm the skill slug exists: `python scripts/install_skill.py --list`
   (or `.\scripts\install_skill.ps1 -List`).
2. If already inside a clone of this repository, run:

   ```powershell
   .\scripts\install_skill.ps1 -Skill <slug> -Harness <harness>
   ```

   Add `-Scope user` for a user-wide install where the harness supports it,
   and `-All` in place of `-Skill <slug>` to install every skill at once.
3. If not inside a clone, download and inspect the installer first, then
   run it -- never pipe a remote script directly into a shell:

   ```powershell
   Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Yaked1/ai-lab-codex-workbench/main/scripts/install_skill.ps1" -OutFile install_skill.ps1
   notepad install_skill.ps1
   .\install_skill.ps1 -Skill <slug> -Harness <harness>
   ```

4. Read the installer's own output. For Codex harnesses it writes
   `.agents/skills/<slug>/SKILL.md`; for Claude Code harnesses it writes
   `.claude/skills/<slug>/SKILL.md`; for Hermes user scope it writes
   `~/.hermes/skills/<slug>/SKILL.md`; for Hermes project scope it stages
   `.agent-skills/hermes/<slug>/SKILL.md` for `skills.external_dirs`.
   Other harnesses get a plain staged file and a paste location, because
   those tools have no native skill-loading mechanism today -- see the
   table in [skills/README.md](../README.md#installer-behavior).
5. If the human wants to verify the exact target path before trusting it,
   pass `-WhatIf` (PowerShell) or `--dry-run` (Python) to preview without
   writing anything.

## Verification

```powershell
.\scripts\install_skill.ps1 -List
python scripts/install_skill.py --list
```

After a real install, confirm the target file exists at the path the
installer printed, for example:

```powershell
Test-Path .agents\skills\<slug>\SKILL.md
Test-Path .claude\skills\<slug>\SKILL.md
Test-Path $HOME\.hermes\skills\<slug>\SKILL.md
```

## Failure Cases

- The requested `<slug>` is not in `skills/INDEX.md` -- list available
  skills instead of guessing a name.
- The target already exists and the human did not say to overwrite it --
  stop and ask before passing `-Force`.
- The harness has no confirmed native skill-loading path (most harnesses
  besides Codex, Claude Code, and Hermes) -- say so plainly and give the
  staged-file location instead of claiming an auto-install that does not
  exist.
- PowerShell's execution policy blocks the script -- point to this
  repository's own [docs/guides/windows-setup-commands.md](../../docs/guides/windows-setup-commands.md)
  troubleshooting section rather than silently bypassing policy with
  `-ExecutionPolicy Bypass` on the human's behalf.

## Final Report

- Skill(s) installed and target harness.
- Exact path written to (or staged to, for harnesses without a native
  loader).
- Whether an existing file was overwritten (and that `-Force` was
  explicitly requested).
- Any harness-specific manual step still required (e.g. pasting a staged
  file into a rules/instructions location).

## Disable Path

Delete the installed skill folder or staged file at the path the installer
printed. This does not affect `skills/` in this repository -- reinstalling
later is always available by re-running the same command.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **installable agent skill** surface. During broad
maintenance, reviewers should treat `skills/install-this-skill-pack/SKILL.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `install this skill pack` state what decision, workflow, or reusable behavior it supports?
- Are included scope, excluded scope, and unsafe actions clear enough for an
  agent or contributor to follow?
- Are examples public-safe, repository-relative, and free of private data?
- Are fast-changing product or platform claims phrased conservatively or marked
  for official-doc verification?
- Does the file point to the next artifact a reader should inspect: a command,
  template, test, manifest, package, or deeper guide?
- Could a reviewer cite this file in a PR review and know what evidence proves
  the work is complete?

Keep future edits focused on stronger evidence, clearer failure modes, better
navigation, and safer automation boundaries. Do not add length unless the new
material makes the repository easier to operate, teach, audit, or recover.
<!-- RESEARCH-GRADE-EXPANSION:END -->
