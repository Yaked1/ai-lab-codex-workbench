# OpenCode Agent Task Template

## Target Tool

OpenCode.

## Purpose

Use this template for a small OpenCode task, especially read-only repository exploration or provider-flexible agent experiments.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Task | "Summarize the repo and propose one docs improvement" |
| Mode | "Read-only first" |
| Files | `README.md`, `docs/` |
| Provider notes | "Do not expose credentials" |

## Full Prompt

```text
Target tool:
OpenCode

Goal:
[TASK]

Starting mode:
Start read-only for first use:
- Summarize the repository.
- Identify the files that would need changes.
- Propose a short plan.
- Wait for approval before editing.

Boundaries:
- Read AGENTS.md.
- Stay inside this repository.
- Do not install dependencies.
- Do not edit secrets, .env files, private links, or unrelated folders.
- Do not print environment variables.
- Do not run destructive commands.
- Keep provider credentials outside the repository.
- Do not make exact pricing, model, or provider claims unless verified.

Success criteria:
- Read-only summary is accurate.
- Proposed edits are scoped.
- No files change before approval.
- After approved edits, checks pass or failures are reported.

Validation after approved edits:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

Final response:
- Summary
- Files changed or proposed
- Commands run
- Checks run
- Provider/setup assumptions
- Remaining risks
```

## Short Version

```text
Use OpenCode read-only first for [TASK]. Read AGENTS.md, summarize repo, propose files and plan, wait before editing, keep credentials out of Git, run checks after edits, and report assumptions and risks.
```

## Success Criteria

- First pass is read-only.
- Provider credentials are not exposed.
- Edits are approved and scoped.
- Checks pass after edits.

## Safety Boundaries

- No environment variable printing.
- No secrets.
- No dependency installation.
- No destructive commands.
- No unverified provider claims.

## Verification

```powershell
git diff
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
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
| Provider auth fails | Report without exposing credentials. |
| Tool wants broad permissions | Decline and narrow scope. |
| Edits occur before approval | Stop and review diff. |
| Windows install path is unclear | Verify official docs before teaching. |
