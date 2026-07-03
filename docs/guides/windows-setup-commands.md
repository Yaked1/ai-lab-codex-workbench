# Windows Setup Commands

This guide collects safe, Windows-friendly commands for this repository and for local prompt-guide experiments. It avoids Docker, WSL, local model hosting, GPU-heavy setups, and dependency-heavy beginner workflows.

Run commands from PowerShell unless a tool's official documentation says otherwise.

## Beginner Path

1. Open PowerShell in the repository root.
2. Run `git status`.
3. Run the repository validation commands.
4. Create local prompt-guide folders only inside the repository.
5. Avoid install commands until you have verified official docs and understand what will change.

## Advanced Path

Use the advanced path when maintaining a workshop or a shared public repo.

1. Keep setup commands in Markdown and review them like code.
2. Separate verified repo-local commands from placeholders.
3. Add "verify in official documentation" for fast-changing tools.
4. Avoid global installs unless there is a clear reason.
5. Do not write secrets into commands, shell history, docs, or screenshots.
6. Run repo checks after changing docs or prompt guides.

## Repository Baseline Commands

Safe commands for this repo:

```powershell
git status
git branch
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Review commands:

```powershell
git diff --stat
git diff
```

Branch command:

```powershell
git switch -c agent/short-task-name
```

Use a public-safe branch name. Do not include account IDs, private project names, school portals, or internal ticket numbers.

## Local Prompt Guide Folders

Safe local folder creation:

```powershell
New-Item -ItemType Directory -Path .\prompt-guides -Force
New-Item -ItemType Directory -Path .\prompt-guides\agent-tasks -Force
New-Item -ItemType Directory -Path .\prompt-guides\skills -Force
New-Item -ItemType Directory -Path .\prompt-guides\audits -Force
New-Item -ItemType File -Path .\prompt-guides\README.md -Force
```

Inspect the result:

```powershell
Get-ChildItem -Path .\prompt-guides -Recurse
```

These commands are safe because they create local folders and an empty README in the current repository. They do not install packages or change system settings.

## Reading Existing Prompt Templates

```powershell
Get-ChildItem -Path .\prompts -Recurse -Filter *.md
Get-Content -Path .\prompts\codex\docs-update.goal.md
```

Use `Get-Content` for inspection. Do not paste secrets into prompt templates.

## Public Prompt Pack Clone Workflow

Use only with public repositories that you intend to inspect before use.

```powershell
# Replace placeholders before use.
# Verify the repository is public and appropriate before cloning.
New-Item -ItemType Directory -Path .\vendor_imports -Force
git clone https://github.com/OWNER/PUBLIC-PROMPT-PACK.git .\vendor_imports\PUBLIC-PROMPT-PACK
Get-ChildItem -Path .\vendor_imports\PUBLIC-PROMPT-PACK
```

After cloning:

```powershell
rg -n "\.env|token|secret|password|private key|api key|credential" .\vendor_imports\PUBLIC-PROMPT-PACK
rg -n "http://|https://" .\vendor_imports\PUBLIC-PROMPT-PACK
```

Review cloned content before copying anything into this repo. Do not run scripts from a prompt pack unless you understand them and the maintainer approves.

## Placeholder Tool Commands

These examples are intentionally placeholders. They are useful for documentation shape, not as final setup instructions.

```powershell
# Verify this command in official docs before running.
# Replace placeholders before use.
# Do not paste secrets into commands.
npx TOOL_NAME@latest --help

# Verify this command in official docs before running.
# Replace placeholders before use.
npm view PACKAGE_NAME version
```

Avoid beginner defaults that require Docker, WSL, local model hosting, GPUs, or large dependency trees. Prefer browser, IDE, CLI, or cloud workflows documented by the tool provider.

## Codex-Oriented Commands

Repo-local commands that are safe here:

```powershell
Get-ChildItem -Path .\prompts\codex
Get-Content -Path .\docs\codex\00-start-here.md
Get-Content -Path .\docs\codex\01-codex-goal-workflow.md
```

For current Codex CLI install, login, skill, model, or configuration behavior, verify official documentation before teaching exact commands.

## Claude Code-Oriented Commands

Repo-local SKILL.md-style practice commands:

```powershell
New-Item -ItemType Directory -Path .\prompt-guides\skills\docs-review -Force
New-Item -ItemType File -Path .\prompt-guides\skills\docs-review\SKILL.md -Force
Get-ChildItem -Path .\prompt-guides\skills\docs-review
```

For current Claude Code install, slash-command, or skills behavior, verify official documentation before teaching exact commands.

## MCP Safety Commands

There is no universal safe MCP install command. Treat MCP setup as tool-specific and verify official documentation first.

Safe inspection habit:

```powershell
# Inspect local configuration files only if they are inside this repository.
Get-ChildItem -Path . -Filter "*mcp*" -Recurse
```

Before enabling an MCP server, document:

- What resources it can read.
- What tools it can call.
- Whether any tool can write, delete, send email, spend money, or access private data.
- Where credentials are stored.
- How to disable the server.

## Common Mistakes

| Mistake | Risk | Safer alternative |
| --- | --- | --- |
| Running install commands from a random guide | Stale or unsafe setup. | Verify official docs first. |
| Pasting tokens into command lines | Shell history and logs may expose secrets. | Use approved secret management outside Git. |
| Creating prompt folders in private user paths for a public demo | Private paths leak into docs. | Use repo-relative paths in examples. |
| Running scripts from cloned prompt packs | Unknown code execution. | Inspect first, copy only understood Markdown. |
| Using Docker or WSL as a beginner default | Heavy setup and confusing failure modes. | Use lightweight repo-local commands. |

## Review Checklist

- [ ] Commands are PowerShell-friendly.
- [ ] Commands are clearly labeled as safe, cautious, or placeholder.
- [ ] Placeholder commands say "Verify this command in official docs before running."
- [ ] Placeholder commands say "Replace placeholders before use."
- [ ] Commands do not include secrets or private paths.
- [ ] Commands do not install dependencies unless explicitly approved.
- [ ] Commands do not modify workflow YAML or system settings.
- [ ] Public docs do not include exact pricing, plan access, model availability, or platform support claims.

## Failure Modes

| Failure mode | Signal | Recovery |
| --- | --- | --- |
| Command not found | Tool is not installed or PATH differs. | Verify official setup docs and avoid guessing. |
| Permission error | Command writes outside repo or protected location. | Stop and use a repo-local path. |
| Network or auth prompt | Command reaches an external service. | Confirm the command is necessary and public-safe. |
| Generated lock file appears | Install command changed repo state. | Stop and ask whether dependencies are allowed. |
| Secret appears in terminal output | Credential exposure risk. | Stop, do not paste it into chat, rotate if needed. |
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/guides/windows-setup-commands.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `windows setup commands` state what decision, workflow, or reusable behavior it supports?
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
