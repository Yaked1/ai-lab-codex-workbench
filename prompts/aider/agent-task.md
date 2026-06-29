# Aider Agent Task Template

Use this template for terminal pair programming with Aider.

## Before Starting

- Start from the repository root.
- Check `git status`.
- Add only the files needed for the task.
- Keep automatic commits disabled unless the maintainer explicitly wants them.

## Goal

```text
Make this specific change to the selected file or files.
```

## Boundaries

- Read and follow `AGENTS.md`.
- Do not edit files that were not selected for the task.
- Do not add dependencies.
- Do not touch secrets, `.env` files, private links, or unrelated folders.
- Do not run destructive commands.

## Validation

Run:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Response

Summarize the diff, checks run, and any remaining manual review needed.
