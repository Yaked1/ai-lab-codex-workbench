# Codex Prompt: Fix Bug

## Target Tool

OpenAI Codex CLI or Codex-style coding-agent goal mode.

## Purpose

Use this prompt when there is a specific reproducible bug and the safest fix is a small code, test, documentation, or prompt-template change.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{bug}` | The observed problem. | `safe_autofix.py --check misses missing final newlines` |
| `{reproduction}` | Exact steps that demonstrate the bug. | `Run command X; observe output Y` |
| `{expected}` | The correct behavior. | `Command reports the file and exits nonzero` |
| `{actual}` | The current behavior. | `Command exits 0` |
| `{suspected_files}` | Files/tests to inspect first. | `scripts/safe_autofix.py`, `tests/test_safe_autofix.py` |
| `{checks}` | Required validation. | `focused unittest plus repo checks` |

## Full Prompt

```text
/goal
Objective:
Fix this bug with the smallest safe change: {bug}

Reproduction:
{reproduction}

Expected behavior:
{expected}

Actual behavior:
{actual}

Mandatory first steps:
1. Run git status.
2. Read AGENTS.md fully.
3. Inspect {suspected_files} before editing.
4. Reproduce the bug if the reproduction is safe and available.
5. Identify pre-existing modified or untracked files and preserve user work.

Included scope:
- {suspected_files}
- A focused regression test if practical.
- Documentation or CHANGELOG.md only if user-visible behavior changes.

Excluded scope:
- Do not edit secrets, credentials, .env files, private links, private paths, browser profiles, or private data.
- Do not delete files.
- Do not install dependencies without explicit approval.
- Do not modify workflow YAML unless the bug is in workflow behavior and the user explicitly requested it.
- Do not refactor unrelated code.
- Do not make exact external product claims.

Safety boundaries:
- Explain the likely root cause briefly before or alongside the fix.
- Preserve existing intended behavior.
- Keep the diff narrow enough for one review.
- Stop if the bug cannot be reproduced and the fix would be speculative.

Verification steps:
- Run the focused reproduction or focused test first.
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --stat
- git diff

Success criteria:
- The reproduction no longer fails, or the reason it could not be rerun is reported.
- A focused test is added/updated when practical.
- Existing intended behavior is preserved.
- No unrelated files changed.
- {checks} pass or failures are honestly reported.

Final report format:
## Summary
## Git state
## Root cause
## Files changed
## Commands run
## Verification results
## Remaining risks
```

## Short Version

```text
Fix {bug} with the smallest safe change. Run git status, read AGENTS.md, inspect {suspected_files}, reproduce if safe, preserve user work, add/update a focused test if practical, avoid secrets/dependencies/workflows/unrelated refactors, run checks, inspect git diff, and report root cause, files, commands, checks, and risks.
```

## Included Scope

- Suspected implementation files.
- Focused tests that prove the bug fix.
- Minimal docs/changelog updates for user-visible behavior.

## Excluded Scope

- Broad refactors, dependencies, workflow YAML, unrelated cleanup, secrets, private data, and destructive git operations.

## Safety Boundaries

- Do not guess a fix when the bug cannot be understood.
- Do not hide failing checks.
- Do not broaden the task into nearby improvements.
- Do not claim a regression test exists unless it was added or already present and run.

## Verification Steps

```powershell
python -m unittest tests.test_name.TestCase.test_method
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --stat
git diff
```

Replace the focused unittest command with the actual relevant test.

## Final Report Format

```markdown
## Summary
## Git state
## Root cause
## Files changed
## Commands run
## Verification results
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Bug cannot be reproduced | Report exact commands tried and ask for more detail. |
| Fix requires a dependency | Stop and ask for approval. |
| Fix touches unrelated code | Split unrelated work into a follow-up. |
| Tests fail outside the touched area | Report them separately instead of rewriting the project. |
| Existing user changes conflict with the fix | Stop and ask how to proceed. |
