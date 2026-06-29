# Git Branch, Pull Request, and Merge Workflow

This guide shows the safe path from local branch to reviewed merge. It applies to Codex work and to other agent-generated changes.

## Local Branch Flow

Start clean or understand what is already changed:

```powershell
git status
```

Create a focused branch:

```powershell
git switch -c agent/my-task
```

Run the Codex task, then inspect the result:

```powershell
git diff
```

Run local checks:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Commit only expected files:

```powershell
git status
git add README.md docs prompts CHANGELOG.md
git commit -m "Expand AI agent guide docs"
```

Push and open a PR:

```powershell
git push -u origin agent/my-task
gh pr create --fill
```

## Branch Naming

Use:

```text
agent/<short-task-name>
```

Examples:

| Task | Branch |
| --- | --- |
| Expand Codex guide | `agent/expand-codex-guide` |
| Add safety checklist | `agent/add-safety-checklist` |
| Fix local check docs | `agent/fix-local-check-docs` |

Avoid private project names, account details, or vague names such as `agent/fixes`.

## Pull Request Body

A useful PR includes:

- Summary.
- Why it changed.
- Files touched.
- Commands run.
- Checks run.
- Known limitations.
- Claims that still need official-doc verification.

Template:

```markdown
## Summary
-

## Commands run
-

## Checks
- [ ] python scripts/repo_health_check.py
- [ ] python scripts/safe_autofix.py --check
- [ ] python -m unittest discover -s tests

## Known limitations
-
```

## PR Review Flow

1. Read the PR summary.
2. Check changed files.
3. Review the actual diff, not only the agent summary.
4. Confirm no secrets or private data were added.
5. Confirm no unrelated files changed.
6. Confirm local checks were reported.
7. Confirm CI passed.
8. Confirm external claims are conservative.
9. Confirm `CHANGELOG.md` is updated when useful.
10. Merge only after human review.

## CI Checks

CI runs on pull requests and verifies:

```powershell
python scripts/repo_health_check.py --ci
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

If CI fails:

- Open the failed job log.
- Find the first meaningful error.
- Fix the smallest related cause.
- Rerun the failed check locally when possible.
- Push a focused fix commit.

## Controlled Merge

This repo includes `.github/workflows/merge-pr.yml`. It is manually triggered and is intended for maintainers who want GitHub Actions to enforce required checks before merging.

The controlled merge workflow:

- Refuses draft PRs.
- Waits for required checks.
- Merges with the selected method.
- Deletes the branch when configured by the command.

Use it only after the diff has been reviewed.

## Squash Merge

For small learning tasks, prefer squash merge:

```powershell
gh pr merge <number> --squash --delete-branch
```

Squash merge keeps `main` readable by turning many small agent iteration commits into one clear commit.

Do not squash merge if:

- The PR is still a draft.
- CI failed.
- The diff is not reviewed.
- The PR contains unrelated changes.
- A secret or private link is present.

## Rollback

If a bad commit reaches `main`, prefer `git revert`:

```powershell
git log --oneline
git revert <bad_commit_hash>
git push
```

Why revert:

- It preserves shared history.
- It is understandable in public repos.
- It creates an audit trail.
- It avoids force-push risk.

After rollback:

- Run local checks.
- Check CI.
- Add a changelog or PR note when learners need to understand the change.

## Common Mistakes

| Mistake | Risk | Better habit |
| --- | --- | --- |
| Commit before reviewing `git diff` | Unrelated changes can slip in. | Review diff before `git add`. |
| Use `git add .` blindly | Generated or private files may be added. | Stage only expected files. |
| Merge because the PR summary looks good | Summary may omit issues. | Review full diff and CI logs. |
| Ignore changelog | Future readers miss context. | Update changelog for visible changes. |
| Force-push shared branch | Can disrupt collaborators. | Use revert for shared history. |
