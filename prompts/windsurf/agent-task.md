# Windsurf Agent Task Template

Use this template for a small Windsurf or current vendor-successor IDE agent task. Verify current product documentation before teaching exact UI steps.

## Goal

```text
Describe one focused task here.
```

## First Step

Ask the agent to explain the relevant folder or files before editing. Approve edits only after the plan is clear.

## Boundaries

- Read `AGENTS.md`.
- Keep edits inside this repository.
- Do not edit secrets, `.env` files, credentials, browser profiles, private links, or unrelated files.
- Do not install dependencies.
- Do not run destructive commands.
- Do not accept large generated diffs without reading them.

## Validation

Run:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Response

Include changed files, commands run, checks run, and tool claims that need manual verification.
