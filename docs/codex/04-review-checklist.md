# Review Checklist

Use this before accepting Codex changes.

## Diff review

- [ ] The change solves the stated task.
- [ ] The diff is small enough to understand.
- [ ] No unrelated files changed.
- [ ] No secrets or private data added.
- [ ] No heavy dependency added without approval.
- [ ] No generated junk committed.

## Test review

- [ ] `repo_health_check.py` passed.
- [ ] `safe_autofix.py --check` passed.
- [ ] Unit tests passed.
- [ ] Any failure is explained honestly.

## Prompt review

- [ ] The Codex prompt had a clear objective.
- [ ] Success criteria were specific.
- [ ] Safety boundaries were included.
- [ ] The final report included files changed and commands run.

## Merge decision

Merge only when the PR is understandable, focused, and passing checks. Otherwise request changes. No need to be heroic. Heroes create maintenance debt.
