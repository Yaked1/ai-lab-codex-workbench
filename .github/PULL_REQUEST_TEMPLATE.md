# Pull Request

## Summary

-

## Why this change is needed

-

## Files changed

-

## Checks run

- [ ] `python scripts/repo_health_check.py`
- [ ] `python scripts/safe_autofix.py --check`
- [ ] `python -m unittest discover -s tests`

## Safety review

- [ ] No secrets or credentials added.
- [ ] No unrelated files changed.
- [ ] No destructive commands required.
- [ ] No heavy dependencies added.

## Notes for reviewer

-
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `.github/PULL_REQUEST_TEMPLATE.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `PULL REQUEST TEMPLATE` state what decision, workflow, or reusable behavior it supports?
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
