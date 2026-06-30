# Aider Agent Task Template

## Target Tool

Aider.

## Purpose

Use this template for terminal pair programming where the human chooses the exact files that Aider may edit.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Selected files | `README.md`, `docs/tools/aider.md` |
| Task | "Improve beginner clarity in one section" |
| Out of scope | "No workflow YAML, no dependencies" |
| Checks | Repo health, safe autofix, unit tests |

## Before Starting

- Start from the repository root.
- Run `git status`.
- Add only the files needed for the task.
- Keep automatic commits disabled unless the maintainer explicitly wants them.
- Keep provider credentials outside the repository.

## Full Prompt

```text
Target tool:
Aider

Selected files:
[FILES ADDED TO AIDER]

Purpose:
[ONE-SENTENCE TASK]

Instructions:
- Read and follow AGENTS.md.
- Edit only the selected files.
- Keep the diff small and reviewable.
- Preserve existing meaning unless the task says otherwise.
- Do not add dependencies.
- Do not edit secrets, .env files, private links, or unrelated folders.
- Do not run destructive commands.
- Do not invent exact pricing, model, or platform claims.

Success criteria:
- The requested change is complete.
- No unselected files are changed.
- The diff is understandable.
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
- Remaining risks
```

## Short Version

```text
Edit only [FILES] to [TASK]. Follow AGENTS.md, keep the diff small, avoid secrets/dependencies/workflow changes, run checks, and report files, commands, checks, and risks.
```

## Included Scope

- Files explicitly added to the Aider session.
- The requested task and directly necessary local context.
- Local checks named by the human or repository docs.

## Excluded Scope

- Files not selected for the Aider session.
- Secrets, `.env` files, credentials, private links, and browser profiles.
- Dependency installation, workflow YAML, generated archives, and destructive
  commands unless explicitly approved.

## Success Criteria

- Only selected files changed.
- The task is complete.
- Local checks pass.
- Any provider or product claim is conservative.

## Safety Boundaries

- No unselected files.
- No secrets.
- No dependency installation.
- No destructive commands.
- No automatic commits unless explicitly requested.

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
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Aider needs another file | Ask before adding it. |
| Diff touches unselected files | Stop and review before commit. |
| Provider setup fails | Report setup issue without exposing credentials. |
| Checks fail | Fix related failure or report clearly. |
