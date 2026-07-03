# Merge Report

Use this after reviewing a pull request and before or immediately after merging.

The report should help a future maintainer understand why a change landed, what was verified, and what risks remained. Keep it factual. Do not paste secrets, private links, or raw environment details.

A merge report is not paperwork for its own sake. Six months from now, someone
will look at a change to `docs/codex/03-safe-autofix-policy.md` and ask "why did
this land, and was it actually checked?" This document is the answer. If the
report is vague or missing, the only remaining evidence is the diff itself,
which explains *what* changed but not *why* it was trusted.

## How To Use This Template

1. Copy this file's sections into the PR description, or fill it out as a
   standalone note attached to the PR after merge.
2. Fill in every section that applies. If a section does not apply to a tiny
   change, write `N/A` instead of deleting the heading, so future readers know
   it was considered and skipped on purpose.
3. Do not check a checkbox unless you actually did the thing. An unchecked box
   is honest. A checked box that was never true is worse than no report at all.
4. Keep command output short. Paste the command and the pass/fail result, not
   a full scrollback of a test run.

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

Field notes:

- **What changed** is a one- or two-line factual description, not a copy of
  the diff. "Expanded the safe-autofix policy doc with a troubleshooting
  table" is useful. "Updated docs" is not.
- **Why it changed** names the trigger: a confusing section, a missing
  example, a requested feature, a bug report. If there is no clear reason,
  that itself is worth flagging to the reviewer.
- **User-visible impact** answers "does a reader's experience change?" For
  most doc PRs this is "clearer guidance, no behavior change."
- **Files or areas touched** should match `git diff --stat` exactly. If it
  does not match, something was staged by accident.
- **Changelog entry** either names the `CHANGELOG.md` line added, or says
  `not needed` with a one-word reason (for example, `typo-only`).

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

Example check notes for a docs-only PR:

```text
python scripts/repo_health_check.py -> passed
python scripts/safe_autofix.py --check -> passed
python -m unittest discover -s tests -> passed, 42 tests
CI -> passed (all required jobs green)
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

Worked example row for a docs PR:

| Evidence | Result | Notes |
| --- | --- | --- |
| `git diff --stat` | reviewed | 1 file changed, matches scope |
| Full diff | reviewed | only prose additions, no code |
| Local checks | passed | all 3 local checks green |
| CI logs | passed | `ci.yml` job green on the PR |
| Public-safety scan | clean | manual grep for tokens/paths found nothing |
| External-claim review | N/A | no external tool claims added |

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

## Worked Example: Hypothetical Docs PR

This example shows a filled-in report for a small, realistic change: expanding
a Codex workflow guide with a troubleshooting table.

```markdown
## PR

- PR number: 142
- Title: Expand git workflow guide with troubleshooting table
- Branch: agent/expand-git-workflow-guide
- Author or agent: Codex CLI, supervised by maintainer
- Reviewer: maintainer
- Date: 2026-06-30
- Related issue: none

## Summary

- What changed: Added a troubleshooting table covering merge conflicts, CI
  flakes, and diverged branches to docs/codex/02-git-branch-pr-merge-workflow.md.
- Why it changed: New contributors kept asking the same four questions in
  review threads.
- User-visible impact: Clearer guide, no behavior change.
- Files or areas touched: docs/codex/02-git-branch-pr-merge-workflow.md
- Changelog entry: Added one line under "Docs" in CHANGELOG.md.

## Scope Confirmation

- [x] PR matches the stated objective.
- [x] Changed files match the included scope.
- [x] Excluded files or behaviors were not changed.
- [x] No unrelated cleanup was bundled into the PR.
- [x] The final diff is small enough for review.

## Checks

- [x] python scripts/repo_health_check.py passed.
- [x] python scripts/safe_autofix.py --check passed.
- [x] python -m unittest discover -s tests passed.
- [x] CI passed.
- [x] Any failed check is explained. (none failed)

## Merge Decision

- [x] Approved

Decision notes: Small, well-scoped doc addition. Verified against
scripts/safe_autofix.py and scripts/build_release_package.py to keep the
troubleshooting commands accurate.
```

## Reviewer Checklist Before Trusting This Report

Before relying on a filled-in merge report, confirm:

- [ ] Every checked box in **Checks** corresponds to a command that was
  actually run, not assumed.
- [ ] **Scope Confirmation** matches `git diff --stat`, not just the PR title.
- [ ] **Public Safety Notes** names a concrete scan method (grep, manual read,
  tool output), not just "looked fine."
- [ ] The **Rollback Plan** names a real commit hash format and would work if
  copy-pasted today.
- [ ] Nothing in the report itself leaks a secret, private path, or private
  link while documenting the change.

## Package Metrics, If Relevant

Use this when the PR changes release packaging, `docs/prompting-os/`, package
builders, or package tests.

| Metric | Value |
| --- | --- |
| Full package built |  |
| Focused Prompting OS package built |  |
| ZIP file count |  |
| Markdown file count |  |
| Markdown byte count |  |
| Shortest Markdown file |  |
| ZIP SHA-256 |  |
| Manifest reviewed |  |
| Generated artifacts committed intentionally |  |

## Source Review, If Relevant

| Source | Status | What it supports | What remains unverified |
| --- | --- | --- | --- |
|  | official / community / structural-only / unverified |  |  |

Use this table when the PR uses public repositories, official docs, local
archives, or generated research candidates. Do not paste copied source text or
private local paths.

## Automation Review, If Relevant

- [ ] Workflow or script cannot publish without human approval.
- [ ] Generated-file allowlist is still narrow.
- [ ] No model-provider API key requirement was added to GitHub Actions.
- [ ] Dry-run behavior is documented.
- [ ] Rollback or refusal behavior is documented.

## Template Safety Reminder

This report is a public artifact when copied into a PR or release note. It
should contain evidence and decisions, not secrets, raw logs, account URLs,
browser session details, private file paths, or unsupported product claims.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/templates/merge-report.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `merge report` state what decision, workflow, or reusable behavior it supports?
- Are included scope, excluded scope, and unsafe actions clear enough for an
  agent or contributor to follow?
- Are examples public-safe, repository-relative, and free of private data?
- Are fast-changing product or platform claims phrased conservatively or marked
  for official-doc verification?
- Does the file point to the next artifact a reader should inspect: a command,
  template, test, manifest, package, or deeper guide?
- Could a reviewer cite this file in a PR review and know what evidence proves
  the work is complete?

Keep future edits focused on stronger evidence, clearer failure modes, better
navigation, and safer automation boundaries. Do not add length unless the new
material makes the repository easier to operate, teach, audit, or recover.
<!-- RESEARCH-GRADE-EXPANSION:END -->
