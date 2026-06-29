# GitHub Copilot Agent Task Template

## Target Tool

GitHub Copilot coding agent or Copilot-assisted GitHub issue workflow.

## Purpose

Use this template for a small issue assignment that should produce a reviewable branch or pull request.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Issue title | "Expand public repo safety checklist" |
| Files expected | `docs/workflows/public-repo-safety.md` |
| Acceptance criteria | "Includes secret scan, links, CI logs" |
| Checks | GitHub Actions and local commands |

## Full Prompt / Issue Body

```text
Target tool:
GitHub Copilot coding agent

Issue goal:
[ONE SMALL REVIEWABLE TASK]

Expected files:
- [FILES]

Scope:
- Work only inside this repository.
- Keep the branch focused.
- Prefer documentation, tests, or small script changes.
- Do not edit secrets, .env files, credentials, private links, browser profiles, or unrelated files.
- Do not modify workflow YAML unless explicitly requested.
- Do not add dependencies without maintainer approval.
- Do not make exact pricing, model, plan, or platform claims unless verified in official docs.

Acceptance criteria:
- The diff solves the issue.
- No unrelated files are changed.
- Public safety rules still hold.
- GitHub Actions checks pass.
- The PR summary lists changed files, checks, and limitations.
- A human can understand the PR without reading the full agent conversation.

Required checks:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

PR review notes:
Before merge, inspect the diff, read Actions logs, confirm no private data appears, and squash merge only after review.
```

## Short Version

```text
Create a small PR for [TASK]. Touch only [FILES], avoid secrets/dependencies/workflow changes, keep claims conservative, require Actions checks, and include summary, checks, limitations, and verification gaps in the PR.
```

## Success Criteria

- PR is focused and understandable.
- Actions checks pass.
- No private data or secrets are present.
- Human reviewer can approve or request changes from the diff alone.

## Safety Boundaries

- No secrets.
- No private links.
- No unrelated files.
- No unapproved dependencies.
- No exact pricing/model/platform claims unless verified.
- No merge without human review.

## Verification

Ask the agent or reviewer to verify:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Also review GitHub Actions logs in the PR.

## Final Report Format

```markdown
## Summary
## Files changed
## Checks run
## GitHub Actions status
## Claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Agent opens a broad PR | Request changes and narrow the issue. |
| Actions fail | Read logs and fix the smallest related cause. |
| PR includes private data | Do not merge; remove and rotate any exposed secret. |
| Tool availability differs by plan | Mark for official-doc verification. |
