# Current Plan: Model Media and Benchmark Visuals

## Goal

Add verified, durable media to the repository's important model benchmark and
availability guides without treating marketing images or social posts as
independent evidence.

## Phases

- [x] Phase 1: Inspect repository state, rules, target guides, and media policy.
- [x] Phase 2: Research official visuals, benchmark data, X posts, and videos.
- [x] Phase 3: Create attributed local visuals and add watchable media links.
- [x] Phase 4: Verify provenance, links, tests, diff, and commit readiness.

## Key questions

1. Which media can be redistributed or embedded in a public GitHub repository?
2. Which benchmark values can support an original, correctly labeled chart?
3. Which videos add useful explanation without becoming evidence for claims?

## Decisions

- Prefer original local SVG diagrams derived from verified data over copied
  benchmark screenshots.
- Link to X posts instead of redistributing screenshots unless reuse permission
  is explicit.
- Use official vendor videos where available and label third-party videos.
- Preserve the pre-existing unstaged `CLAUDE.md` edit.

## Errors and resolutions

- `rg.exe` could not launch in this PowerShell session. Repository searches use
  `Get-ChildItem` and `Select-String`.
- A large patch failed because curly quotes were rendered with the wrong
  encoding. It was reapplied with stable Markdown heading anchors.

## Status

Complete. The source links, local SVG structure, provenance ledger, full test
suite, repository health check, safe-format check, and diff whitespace check
passed. The unrelated `CLAUDE.md` edit remains outside the task file set.

## Verification

- `python -m unittest tests.test_model_media`: 3 tests passed.
- `python scripts/repo_health_check.py`: passed.
- `python scripts/safe_autofix.py --check`: passed.
- `python -m unittest discover -s tests`: 86 tests passed.
- `git diff --check`: passed.
