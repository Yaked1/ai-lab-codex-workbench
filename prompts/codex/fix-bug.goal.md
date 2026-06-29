# Codex Prompt: Fix Bug

## Target Tool

OpenAI Codex.

## Purpose

Use this prompt when there is a specific reproducible bug and the safest fix is a small code, test, or documentation change.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Bug | "`safe_autofix.py --check` misses files without final newlines" |
| Reproduction | "Run command X and observe output Y" |
| Expected behavior | "Command reports the file" |
| Suspected files | `scripts/safe_autofix.py`, `tests/test_safe_autofix.py` |
| Required checks | Repo health, safe autofix check, unit tests |

## Full Prompt

```text
/goal
Objective:
Fix the following bug with the smallest safe change:
[BUG DESCRIPTION]

Reproduction:
[STEPS TO REPRODUCE]

Expected behavior:
[EXPECTED RESULT]

Actual behavior:
[ACTUAL RESULT]

Files to inspect first:
- AGENTS.md
- [SUSPECTED FILES]

Success criteria:
- The bug is fixed.
- Existing intended behavior is preserved.
- A focused test is added or updated if practical.
- No unrelated files changed.
- Local checks pass:
  - python scripts/repo_health_check.py
  - python scripts/safe_autofix.py --check
  - python -m unittest discover -s tests

Safety boundaries:
- Do not edit .env files, credentials, secrets, private links, or private data.
- Do not delete files.
- Do not install dependencies without approval.
- Do not modify workflow YAML unless the bug is in a workflow and the user requested it.
- Keep all changes inside this repository.

Workflow:
1. Run git status.
2. Inspect relevant files and tests before editing.
3. Explain the likely cause briefly.
4. Make the smallest fix.
5. Add or update a focused test if practical.
6. Run the focused test first, then the full local checks.
7. Report any unverified assumptions.

Final response:
- Summary
- Root cause
- Files changed
- Commands run
- Tests/checks run
- Remaining risks
```

## Short Version

```text
Fix [BUG] with the smallest safe change. Read AGENTS.md, inspect suspected files and tests first, preserve intended behavior, add/update a focused test if practical, run checks, and report root cause, files changed, commands, tests, and risks.
```

## Success Criteria

- Reproduction no longer fails.
- Test coverage is added or the reason for not adding it is stated.
- The fix is minimal.
- Checks pass or failures are honestly reported.

## Safety Boundaries

- No dependency installation without approval.
- No unrelated refactors.
- No broad cleanup.
- No secrets or private data.
- No workflow YAML edits unless explicitly in scope.

## Verification

Run the most focused relevant test first, then:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Report Format

```markdown
## Summary
## Root cause
## Files changed
## Commands run
## Tests/checks
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Bug cannot be reproduced | Report exact commands tried and ask for more detail. |
| Fix requires dependency install | Stop and ask for approval. |
| Fix touches unrelated code | Split the unrelated issue into a follow-up. |
| Tests fail outside the touched area | Report separately instead of rewriting the project. |
