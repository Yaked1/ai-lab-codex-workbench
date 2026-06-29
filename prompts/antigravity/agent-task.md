# Google Antigravity Agent Task Template

Use this template for a bounded Antigravity agent task. Product behavior changes quickly, so verify current official documentation before relying on a specific feature, artifact type, or platform surface.

## Goal

Create a reviewed plan or small implementation for:

```text
Describe the exact task here.
```

## Agent Instructions

- Read `AGENTS.md` first.
- Produce a plan artifact before editing if the task touches more than one file.
- Keep work inside this repository.
- Use one branch for one task.
- Prefer documentation or testable small changes for first runs.

## Boundaries

- Do not expose secrets or private links.
- Do not modify GitHub workflow files unless explicitly requested.
- Do not run destructive automation.
- Do not let parallel agents edit overlapping files without review.

## Validation

Run:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Response

Return the plan or implementation summary, files changed, checks run, and any assumptions that require manual verification.
