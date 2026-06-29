# OpenCode Agent Task Template

Use this template for a small OpenCode task.

## Goal

```text
Describe the exact task here.
```

## Starting Mode

Start read-only for first use:

- Summarize the repository.
- Identify the files that would need changes.
- Propose a short plan.
- Wait for approval before editing.

## Boundaries

- Read `AGENTS.md`.
- Stay inside this repository.
- Do not install dependencies.
- Do not edit secrets, `.env` files, private links, or unrelated folders.
- Do not run destructive commands.

## Validation

After approved edits, run:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Response

Report changed files, commands run, checks run, and remaining risks.
