# OpenCode Agent Task Template

## Target Tool

OpenCode, the open-source, provider-flexible terminal/TUI coding agent.
Invoked from PowerShell as `opencode` (interactive TUI) or via its
non-interactive/CLI mode for a single instruction. Works with whichever
model provider you have configured (Anthropic, OpenAI, local, or other),
so this template treats the underlying model as an implementation detail
and focuses on repository-side scope and safety.

## Purpose

Use this template for a small OpenCode task, especially read-only
repository exploration, a provider-flexible agent experiment, or a bounded
documentation/script edit where you want a read-only pass before any file
is touched.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{task}` | The specific task or question. | `Summarize the repo and propose one docs improvement` |
| `{mode}` | Read-only-first or direct edit. | `Read-only first, wait for approval` |
| `{files}` | Files or directories in scope. | `README.md`, `docs/` |
| `{provider_notes}` | Provider/credential constraints. | `Do not print or log API keys; use the configured provider only` |
| `{checks}` | Local checks to run after any approved edit. | `repo health, safe autofix, unit tests` |

## Full Prompt

```text
Target tool:
OpenCode

Goal:
{task}

Starting mode:
{mode}
Start read-only for first use:
- Summarize the repository or the relevant area.
- Identify the files that would need changes.
- Propose a short, numbered plan.
- Wait for explicit approval before editing anything.

Boundaries:
- Read AGENTS.md before proposing a plan.
- Stay inside this repository; do not fetch or reference external
  repositories or private systems.
- Do not install dependencies or modify lock files.
- Do not edit .env, .env.*, credentials, private links, private paths, or
  any folder outside {files}.
- Do not print, log, or echo environment variables or provider credentials.
- Do not run destructive commands (no git reset --hard, no force-push, no
  recursive deletes).
- Keep provider credentials outside the repository and outside chat output.
- Do not state exact pricing, model, or provider capability claims unless
  verified against official docs; use conservative wording otherwise.
- {provider_notes}

Success criteria:
- The read-only summary is accurate and specific to {files}.
- The proposed plan is scoped to {task} and lists exact files.
- No file changes happen before explicit approval.
- After approved edits, checks pass or failures are reported with output.

Validation after approved edits (PowerShell):
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check

Final response:
- Summary
- Files changed or proposed
- Commands run
- Checks run and their result
- Provider/setup assumptions made during this session
- Remaining risks
```

## Short Version

```text
Use OpenCode read-only first for {task}. Read AGENTS.md, summarize {files},
propose a numbered plan, wait for approval before editing, never print
credentials, run the checks after approved edits, and report files,
commands, checks, provider assumptions, and risks.
```

## Included Scope

- Files or repository areas explicitly selected in `{files}`.
- A read-only summary and numbered plan produced before any edit.
- The requested task in `{task}` plus adjacent docs or tests needed for
  consistency once edits are approved.
- Safe local checks named in `{checks}` or in this repository's AGENTS.md.

## Excluded Scope

- Any file outside `{files}` that was not named in the approved plan.
- Secrets, `.env` / `.env.*` files, credentials, browser profiles, private
  links, and private machine paths.
- Dependency installation, GitHub Actions workflow YAML, generated
  archives, provider account or billing changes, and destructive commands,
  unless explicitly approved for this task.
- Printing or logging environment variables, API keys, or provider tokens
  under any circumstance.
- Unsupported current product or provider claims.

## Success Criteria

- The first pass is genuinely read-only: no file is modified before a plan
  is shown and approved.
- Provider credentials are never exposed in chat output, logs, or files.
- Approved edits match the plan exactly; no scope creep.
- Local checks pass after edits, or failures are reported honestly.

## Safety Boundaries

- No environment variable or credential printing, ever, even for debugging.
- No secrets, tokens, or `.env` contents in chat output or committed files.
- No dependency installation or lock file changes.
- No destructive commands without explicit human confirmation.
- No unverified provider or platform claims stated as current fact.
- Treat OpenCode's provider flexibility as a reason to double-check which
  provider/model is actually configured before trusting any
  capability-specific claim it makes about itself.

## Verification

```powershell
git status
git diff
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
```

## Final Report Format

```markdown
## Summary
## Files changed or proposed
## Commands run
## Checks/tests
## Provider/setup assumptions
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Provider authentication fails mid-session | Report the failure clearly without exposing the credential or token value. |
| The tool requests broad permissions (full filesystem access, unrestricted shell) | Decline and narrow the session to the files and commands actually needed. |
| Edits occur before explicit approval of the plan | Stop immediately, review `git diff`, and revert unapproved changes before continuing. |
| A Windows-specific install or configuration step is unclear or undocumented | Verify against official OpenCode docs before teaching or repeating the step as fact. |
| The plan silently expands to files outside `{files}` | Reject the plan and ask for a revision scoped back to the original file list. |
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **agent prompt template** surface. During broad
maintenance, reviewers should treat `prompts/opencode/agent-task.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `agent task` state what decision, workflow, or reusable behavior it supports?
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
