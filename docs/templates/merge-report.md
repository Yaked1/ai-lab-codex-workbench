# Merge Report

Use this after reviewing a pull request and before or immediately after merging.

The report should help a future maintainer understand why a change landed, what was verified, and what risks remained. Keep it factual. Do not paste secrets, private links, or raw environment details.

## PR

- PR number:
- Title:
- Branch:
- Author or agent:
- Reviewer:
- Date:
- Related issue:

## Summary

- What changed:
- Why it changed:
- User-visible impact:
- Files or areas touched:
- Changelog entry:

## Scope Confirmation

- [ ] PR matches the stated objective.
- [ ] Changed files match the included scope.
- [ ] Excluded files or behaviors were not changed.
- [ ] No unrelated cleanup was bundled into the PR.
- [ ] The final diff is small enough for review.

## Checks

- [ ] `python scripts/repo_health_check.py` passed.
- [ ] `python scripts/safe_autofix.py --check` passed.
- [ ] `python -m unittest discover -s tests` passed.
- [ ] CI passed.
- [ ] Any failed check is explained.

Check notes:

```text
[Paste short command names and outcomes, not secrets or noisy logs.]
```

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

## Evidence Reviewed

| Evidence | Result | Notes |
| --- | --- | --- |
| `git diff --stat` |  |  |
| Full diff |  |  |
| Local checks |  |  |
| CI logs |  |  |
| Public-safety scan |  |  |
| External-claim review |  |  |

## Public Safety Notes

- Secret or token-like examples found:
- Private links or private paths found:
- Screenshots or binary files added:
- Workflow permission changes:
- Dependency changes:
- Claims needing official-doc verification:

If none apply, write:

```text
No public-safety concerns found in review.
```

## Merge Method

- [ ] Squash
- [ ] Merge commit
- [ ] Rebase

Reason:

```text
[Why this merge method was chosen.]
```

## Merge Decision

- [ ] Approved
- [ ] Request changes
- [ ] Close without merge
- [ ] Defer for follow-up

Decision notes:

```text
[Short factual explanation.]
```

## Rollback Plan

```powershell
git log --oneline
git revert <bad_commit_hash>
git push
```

Notes:

-

## Follow-Up Work

- Required follow-up issues:
- Optional improvements:
- Claims to verify later:
- Documentation to update later:
- Tests or checks to strengthen later:

## Post-Merge Notes

- Branch deleted:
- Follow-up issue needed:
- Claims to verify later:
- Lessons for future prompts:

## Final Audit

- [ ] The merge report does not contain secrets or private data.
- [ ] The report does not claim checks passed unless they did.
- [ ] The report records any unverified claims.
- [ ] The report is short enough for a future maintainer to scan.
