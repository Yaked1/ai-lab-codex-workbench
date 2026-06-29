# Cursor Agent Task Template

Use this template for a small Cursor Agent or Plan mode task.

## Goal

Make this focused change:

```text
Describe the exact documentation, code, or workflow change here.
```

## Required Context

- Read `AGENTS.md`.
- Inspect the relevant files before editing.
- Keep the change scoped to the requested files.
- Prefer a plan first if the task touches more than one file.

## Boundaries

- Do not edit `.env`, credentials, browser profiles, private documents, or unrelated folders.
- Do not install dependencies.
- Do not run destructive commands.
- Do not accept broad rewrites unless the task explicitly asks for them.

## Validation

Run these if files changed:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Response

Summarize changed files, commands run, checks run, and remaining risks.
