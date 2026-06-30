# Cursor Agent Task Template

## Target Tool

Cursor Agent or Cursor Plan mode.

## Purpose

Use this template for a focused IDE-based task where the user can inspect plans and diffs before accepting changes.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Task | "Expand docs/workflows/public-repo-safety.md" |
| Mode | "Plan first, then edit after approval" |
| Files | `docs/workflows/public-repo-safety.md` |
| Checks | Repo health, safe autofix, unit tests |

## Full Prompt

```text
Target tool:
Cursor

Mode:
[Plan first / Agent edit after approval]

Goal:
Make this focused change:
[TASK]

Required context:
- Read AGENTS.md.
- Inspect the relevant files before editing.
- Keep the change scoped to the requested files.
- Prefer a plan first if the task touches more than one file.

Boundaries:
- Do not edit .env, credentials, browser profiles, private documents, private links, or unrelated folders.
- Do not install dependencies.
- Do not run destructive commands.
- Do not modify workflow YAML unless explicitly requested.
- Do not accept broad rewrites unless the task explicitly asks for them.
- Do not make exact pricing, model, or platform claims unless verified.

Success criteria:
- The task is complete.
- Diff is small and reviewable.
- External claims are conservative.
- Local checks pass or failures are reported.

Validation if files changed:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

Final response:
- Summary
- Files changed
- Commands run
- Checks run
- Claims needing manual verification
- Remaining risks
```

## Short Version

```text
Use Cursor to [TASK]. Read AGENTS.md, plan first, edit only [FILES], avoid secrets/dependencies/workflow changes, run checks, and report files, commands, verification gaps, and risks.
```

## Included Scope

- Files or repository areas explicitly selected for the Cursor task.
- Adjacent docs needed to preserve navigation and consistency.
- Local checks named in repository docs or by the human.

## Excluded Scope

- Secrets, `.env` files, credentials, browser profiles, private links, and
  private machine paths.
- Dependency installation, workflow YAML, generated archives, and destructive
  commands unless explicitly approved.
- Unsupported current product claims.

## Success Criteria

- Plan is understandable.
- Diff matches the approved scope.
- No private data or secrets are added.
- Checks pass after edits.

## Safety Boundaries

- No hidden broad rewrites.
- No private files or browser profiles.
- No unapproved dependencies.
- No workflow YAML changes unless requested.
- No exact external claims unless verified.

## Verification

```powershell
git diff
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Report Format

```markdown
## Summary
## Files changed
## Commands run
## Checks/tests
## Claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Cursor proposes too many files | Reject and ask for narrower scope. |
| Plan depends on unverified product facts | Mark claims for official-doc verification. |
| Checks cannot run in IDE | Run them in PowerShell before merging. |
| Diff includes unrelated edits | Revert those edits before PR. |
