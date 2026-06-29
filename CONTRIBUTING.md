# Contributing

This repository uses a safe, boring, effective workflow. Boring is good. Boring means fewer disasters wearing a hoodie.

## Workflow

1. Create or choose an issue.
2. Create a branch named `agent/<task-name>`.
3. Make a small change.
4. Run checks.
5. Commit.
6. Open a pull request.
7. Wait for CI.
8. Review the diff.
9. Merge manually or through the controlled merge workflow.

## Local checks

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

To apply safe formatting fixes:

```powershell
python scripts/safe_autofix.py --write
```

## Commit style

Use short factual commit messages:

```text
Add Codex task template
Fix README setup commands
Update safe autofix policy
```

## Do not contribute

- Secrets or API keys.
- Private personal documents.
- Huge generated files.
- Large model weights.
- Docker stacks unless the repository deliberately grows into that later.
- Unsafe automation that merges without review.
