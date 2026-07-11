# Current Plan: 2026 Model and Interface Update

## Goal

Publish a source-verified, public-safe update covering current model names,
interfaces, effort controls, pricing, prompting guidance, and a careful
Claude-versus-Codex comparison, then verify and commit the requested files.

## Phases

- [x] Inspect repository state, instructions, and existing work.
- [x] Verify official product, availability, interface, and pricing claims.
- [x] Verify independent benchmark evidence and document uncertainty.
- [x] Write focused guides, shorten and rebalance the README, and remove superseded claims.
- [x] Run repository checks, review the diff, and prepare the commit on `main`.

## Decisions

- The user-provided GPT-5.6 announcement was verified against OpenAI's official
  2026-07-09 release before use.
- X and other community posts are treated as leads or sentiment samples only.
- Sol Max benchmark results are not relabeled as Sol Ultra results.
- The pre-existing unstaged `CLAUDE.md` edit is preserved and excluded from the
  task commit.
- Available subagents were used for bounded research, but no model identity or
  effort was claimed because the subagent API did not expose those selectors.

## Errors and resolutions

- `rg.exe` could not launch in this PowerShell session. Searches used
  `Get-ChildItem` and `Select-String`.
- `memanto recall` reported no active MEMANTO agent. Repository and Codex
  memory files remained available.
- `codex debug models` invoked a blocked PowerShell wrapper. `codex.cmd debug
  models` succeeded.
- The first full test run failed eight README contract tests after the README
  was shortened. Required operational markers were restored, and the stale
  50KB minimum-size test was replaced with a 10KB to 25KB focused-entry-point
  contract. The focused and full suites then passed.

## Verification

- `python scripts/repo_health_check.py`: passed.
- `python scripts/safe_autofix.py --check`: passed.
- `python -m unittest discover -s tests`: 83 tests passed.
- `git diff --check`: passed for task files.

## Status

Complete. The task-related file set is ready for the requested commit on
`main`; the unrelated `CLAUDE.md` edit remains unstaged.
