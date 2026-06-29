# GitHub Copilot Agent Task Template

Use this template for a small GitHub Copilot coding agent task or issue assignment.

## Issue Goal

```text
Describe one small, reviewable task. Include expected files and checks.
```

## Scope

- Work only inside this repository.
- Keep the branch focused.
- Prefer documentation, tests, or small script changes.
- Do not edit secrets, `.env` files, credentials, private links, or unrelated files.

## Acceptance Criteria

- The diff solves the issue.
- No unrelated files are changed.
- Public safety rules still hold.
- GitHub Actions checks pass.
- A human can understand the PR without reading the full agent conversation.

## Required Checks

Ask the agent or reviewer to verify:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## PR Review Notes

Before merge, inspect the diff, read Actions logs, confirm no private data appears, and squash merge only after review.
