# Task Spec

## Task title


## Objective


## Files Codex should inspect first

- `AGENTS.md`
- `README.md`

## Included scope

-

## Excluded scope

- Do not edit secrets or `.env` files.
- Do not install dependencies without approval.
- Do not delete files.
- Do not change unrelated folders.

## Success criteria

- [ ]
- [ ] Checks pass.
- [ ] Final response lists files changed and commands run.

## Local checks

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```
