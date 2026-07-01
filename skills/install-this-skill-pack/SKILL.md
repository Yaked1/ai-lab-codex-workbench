---
name: install-this-skill-pack
description: Use when a human wants to install one or more skills from this repository into Claude Code, Codex, or another agent harness, and needs the exact command for their setup.
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
- Which harness: `claude-code`, `codex`, `cursor`, `windsurf`, `aider`,
  `antigravity`, `github-copilot`, `opencode`, or `kilo-code`.
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

4. Read the installer's own output. For `claude-code` and `codex` it
   confirms a real target folder. For every other harness it stages a
   plain file and prints exactly where to paste it, because those tools
   have no native skill-loading mechanism today -- see the table in
   [skills/README.md](../README.md#installer-behavior).
5. If the human wants to verify the exact target path before trusting it,
   pass `-WhatIf` (PowerShell) or `--dry-run` (Python) to preview without
   writing anything.

## Verification

```powershell
.\scripts\install_skill.ps1 -List
python scripts/install_skill.py --list
```

After a real install, confirm the target file exists at the path the
installer printed (for example `Test-Path .claude\skills\<slug>\SKILL.md`).

## Failure Cases

- The requested `<slug>` is not in `skills/INDEX.md` -- list available
  skills instead of guessing a name.
- The target already exists and the human did not say to overwrite it --
  stop and ask before passing `-Force`.
- The harness has no confirmed native skill-loading path (most harnesses
  besides Claude Code) -- say so plainly and give the staged-file location
  instead of claiming an auto-install that does not exist.
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
