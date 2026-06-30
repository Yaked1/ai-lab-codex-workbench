# Windsurf Agent Task Template

## Target Tool

Windsurf or current vendor-supported IDE agent surface.

## Purpose

Use this template for a small IDE-agent task where current product documentation should be verified before teaching exact UI steps.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Task | "Explain docs/tools and improve one page" |
| Files | `docs/tools/windsurf.md` |
| Mode | "Explain first, edit after approval" |
| Checks | Repo health, safe autofix, unit tests |

## Full Prompt

```text
Target tool:
Windsurf

Goal:
[FOCUSED TASK]

First step:
Explain the relevant folder or files before editing. Propose a short plan and wait for approval before applying changes.

Boundaries:
- Read AGENTS.md.
- Keep edits inside this repository.
- Do not edit secrets, .env files, credentials, browser profiles, private links, or unrelated files.
- Do not install dependencies.
- Do not run destructive commands.
- Do not modify workflow YAML unless explicitly requested.
- Do not accept or apply large generated diffs without review.
- Do not make exact pricing, model, ownership, or platform claims unless verified in official docs.

Success criteria:
- Relevant files are explained.
- Plan is clear before edits.
- Diff is focused.
- Local checks pass or failures are reported.

Validation:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

Final response:
- Summary
- Files changed
- Commands run
- Checks run
- Tool claims needing manual verification
- Remaining risks
```

## Short Version

```text
Use Windsurf to [TASK]. Explain files first, wait for approval, edit only [FILES], avoid secrets/dependencies/workflow changes, run checks, and report verification gaps and risks.
```

## Included Scope

- Files or repository areas explicitly selected for the Windsurf task.
- The requested task and directly related docs or tests needed for consistency.
- Safe checks named by repository docs or the human.

## Excluded Scope

- Secrets, `.env` files, credentials, browser profiles, private links, and
  private machine paths.
- Dependency installation, workflow YAML, generated archives, and destructive
  commands unless explicitly approved.
- Exact current product claims unless verified in official docs.

## Success Criteria

- Explanation precedes editing.
- Diff is visible and reviewed.
- No private data appears.
- Checks pass after edits.
- Product claims are conservative.

## Safety Boundaries

- No private files or browser profiles.
- No broad generated diffs.
- No dependency installation.
- No workflow YAML changes unless requested.
- No exact product claims without verification.

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
## Tool claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Product docs changed | Verify official docs and update wording. |
| Diff is too large | Reject and ask for smaller scope. |
| Checks cannot be run in IDE | Run them in PowerShell before merging. |
| Private data appears | Stop, remove it, and follow security policy. |
