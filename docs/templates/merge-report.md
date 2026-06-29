# Merge Report

Use this after reviewing a pull request and before or immediately after merging.

## PR

- PR number:
- Title:
- Branch:
- Author or agent:
- Reviewer:

## Summary

- What changed:
- Why it changed:
- User-visible impact:

## Checks

- [ ] `python scripts/repo_health_check.py` passed.
- [ ] `python scripts/safe_autofix.py --check` passed.
- [ ] `python -m unittest discover -s tests` passed.
- [ ] CI passed.
- [ ] Any failed check is explained.

## Review

- [ ] Diff reviewed.
- [ ] No secrets.
- [ ] No private links.
- [ ] No personal data.
- [ ] No unrelated files.
- [ ] No unapproved dependency changes.
- [ ] No unrequested workflow YAML changes.
- [ ] External tool claims are conservative.
- [ ] Changelog updated when useful.

## Merge Method

- [ ] Squash
- [ ] Merge commit
- [ ] Rebase

Reason:

```text
[Why this merge method was chosen.]
```

## Rollback Plan

```powershell
git log --oneline
git revert <bad_commit_hash>
git push
```

Notes:

-

## Post-Merge Notes

- Branch deleted:
- Follow-up issue needed:
- Claims to verify later:
- Lessons for future prompts:
