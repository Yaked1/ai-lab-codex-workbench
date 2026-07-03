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
4. Reproduce the bug if the reproduction is safe and available. Capture the
   exact failing output before changing anything.
5. Identify pre-existing modified or untracked files and preserve user work.
6. Search for related open issues, TODO comments, or prior fixes in git log
   for the same files before assuming this is a new problem.
7. Form a root-cause hypothesis and state it before touching code. If the
   evidence does not support one clear hypothesis, say so and narrow scope
   instead of guessing.

Included scope:
- {suspected_files}
- A focused regression test if practical.
- Documentation or CHANGELOG.md only if user-visible behavior changes.

Excluded scope:
- Do not edit secrets, credentials, .env files, private links, private paths, browser profiles, or private data.
- Do not delete files.
- Do not install dependencies or modify package manager lock files without explicit approval.
- Do not modify anything under .github/workflows/ unless the bug is in workflow behavior and the user explicitly requested it.
- Do not refactor unrelated code, rename unrelated symbols, or reformat untouched files.
- Do not make exact external product claims.
- Do not fix a second, unrelated bug noticed along the way; report it instead.

Safety boundaries:
- Explain the likely root cause briefly before or alongside the fix.
- Preserve existing intended behavior for every other input path.
- Keep the diff narrow enough for one review.
- Stop if the bug cannot be reproduced and the fix would be speculative.
- Stop and ask if the smallest correct fix requires a new dependency instead
  of silently adding one.

Verification steps:
- Run the focused reproduction or focused test first, and capture before/after output.
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check
- git diff --stat
- git diff

Success criteria:
- The reproduction no longer fails, or the reason it could not be rerun is reported.
- A focused test is added/updated when practical, and it fails against the old code path (verified mentally or by temporary revert) before passing against the fix.
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

### Worked Example

```text
/goal
Objective:
Fix this bug with the smallest safe change: safe_autofix.py --check misses
files that are missing a final newline when the file has CRLF line endings.

Reproduction:
Create a file with CRLF endings and no trailing newline, then run
`python scripts/safe_autofix.py --check` and observe it reports no issues.

Expected behavior:
The command should report "Needs fix" for that file and exit 1.

Actual behavior:
The command exits 0 and reports "No safe formatting changes needed."

Mandatory first steps:
1. Run git status.
2. Read AGENTS.md fully.
3. Inspect scripts/safe_autofix.py and tests/test_safe_autofix.py before editing.
4. Reproduce the bug locally with a throwaway file in a temp directory and
   capture the exact command output.
5. Identify pre-existing modified or untracked files and preserve user work.
6. Check git log for scripts/safe_autofix.py for any prior newline-handling
   fixes before assuming this is new.
7. State the root-cause hypothesis: normalize_text() likely converts CRLF to
   LF before the final-newline check, masking the original file's state.

Included scope:
- scripts/safe_autofix.py
- tests/test_safe_autofix.py (add a CRLF-specific regression case)

Excluded scope:
- Do not edit secrets, credentials, .env files, private links, private
  paths, browser profiles, or private data.
- Do not delete files.
- Do not install dependencies.
- Do not modify anything under .github/workflows/.
- Do not refactor unrelated parts of safe_autofix.py.

Safety boundaries:
- Explain the root cause in the report before describing the fix.
- Preserve current behavior for LF-only files.
- Keep the diff limited to the newline-detection logic and its test.

Verification steps:
- Run the reproduction script before and after the fix.
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check
- git diff --stat
- git diff

Success criteria:
- The reproduction now correctly reports "Needs fix" and exits 1.
- A regression test for CRLF-without-trailing-newline exists and passes.
- LF-only file behavior is unchanged.
- All checks pass or failures are reported honestly.

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

- Broad refactors, unrelated cleanup, secrets, private data, and destructive git operations.
- Adding dependencies or modifying package manager lock files.
- Any change under `.github/workflows/` unless the bug is a workflow bug and was explicitly requested.

## Safety Boundaries

- Do not guess a fix when the bug cannot be understood.
- Do not hide failing checks.
- Do not broaden the task into nearby improvements.
- Do not claim a regression test exists unless it was added or already present and run.
- Do not add a dependency to work around a bug; report that the fix needs one and stop.

## Verification Steps

```powershell
python -m unittest tests.test_name.TestCase.test_method
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
git diff --stat
git diff
```

Replace the focused unittest command with the actual relevant test. If the
bug lives in a script with no dedicated test module yet, run the script
directly with the reproduction inputs and paste the output into the report
instead of inventing a passing test result.

## Success Criteria

- The reported bug is reproduced, explained, or bounded by current evidence.
- The smallest practical fix is implemented without unrelated rewrites.
- Focused and repository-level checks pass or failures are reported clearly.
- The final report includes root cause, changed files, commands, and risks.

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
| Fix requires a dependency bump or new package | Stop and ask for approval; do not add it silently. |
| Fix touches unrelated code | Split unrelated work into a follow-up. |
| Tests fail outside the touched area | Report them separately instead of rewriting the project. |
| Existing user changes conflict with the fix | Stop and ask how to proceed. |
| Root cause spans multiple files with no single clear owner | Name every implicated file, pick the smallest correct fix point, and note the others as follow-up risk. |
| The bug is actually expected behavior described inaccurately | Say so directly and propose a docs fix instead of a code fix. |
| The bug only reproduces in CI, not locally | Report the environment gap; do not claim a local-only fix resolves it. |
| The bug is in generated output (for example a release package) rather than source | Fix the generator, not the generated artifact, and regenerate to confirm. |
| The reported bug is actually in `.github/workflows/` behavior | Stop; workflow YAML changes require explicit user approval before editing. |

## Anti-Patterns

- Patching the symptom at the call site instead of the root cause in the
  function that produces the bad value. This tends to resurface the same
  bug at a different call site later.
- Writing the regression test after "confirming" the fix works, without
  ever seeing it fail. A test that has never failed does not prove
  anything.
- Widening the diff to "clean up while I'm here." A bug fix PR should be
  reviewable in isolation from unrelated style changes.
- Reporting "fixed" based on reading the code instead of running the
  reproduction and the test suite.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **agent prompt template** surface. During broad
maintenance, reviewers should treat `prompts/codex/fix-bug.goal.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `fix bug.goal` state what decision, workflow, or reusable behavior it supports?
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
