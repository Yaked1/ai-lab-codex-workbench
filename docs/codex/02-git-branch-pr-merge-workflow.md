# Git Branch, Pull Request, and Merge Workflow

## Local branch flow

```powershell
git status
git checkout -b agent/my-task
# run Codex task
git diff
.\scripts\local_check.ps1
git add .
git commit -m "Describe the change"
git push -u origin agent/my-task
gh pr create --fill
```

## PR review flow

1. Read the PR summary.
2. Check changed files.
3. Confirm no secrets are included.
4. Confirm CI passed.
5. Confirm the task matches the issue.
6. Merge only after review.

## Controlled merge

This repo includes `.github/workflows/merge-pr.yml`. It is manually triggered. It checks required PR checks, refuses draft PRs, and then merges using your selected method.

Manual merge is not a weakness. It is the small fence between automation and comedy.

## Emergency rollback

If a bad commit reaches `main`:

```powershell
git log --oneline
git revert <bad_commit_hash>
git push
```

Prefer `git revert` on shared branches. It preserves history and avoids causing extra confusion, because Git already contains enough of that.
