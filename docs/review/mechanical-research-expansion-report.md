# Mechanical Research Expansion Report

This report makes the broad mechanical rewrite reviewable. It records
the deterministic expansion strategy, file-class handling, validation
expectations, and skip reasons for tracked repository files.

## Summary

- Tracked files inspected: 320
- Files carrying the expansion marker after this run: 314
- Files changed during the current expansion pass: 1
- Files already carrying the expansion marker before this pass: 313
- Files skipped with explicit reasons: 6
- Manifest: `docs/review/mechanical-research-expansion-manifest.json`

The current-pass modified count is expected to fall to zero on
idempotent reruns. Use the marker-coverage count, skipped-file list,
and staged `git diff --stat` to audit the full broad rewrite.

<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This report is itself part of the review evidence for the mechanical
rewrite. It should let a maintainer understand the broad diff without
opening every file first: what transformation ran, which files were
modified, which files were skipped, how to search the inserted markers,
and which validation commands must pass before staging or merging.

Reviewers should compare this report with the JSON manifest, `git diff
--stat`, and the validation output. If those artifacts disagree, treat
the task as incomplete until the mismatch is explained.
<!-- RESEARCH-GRADE-EXPANSION:END -->

## Review Strategy

- Markdown files receive a visible research-grade review addendum.
- Scripts, tests, workflows, and config files receive comment-only
  maintenance notes so behavior remains unchanged.
- Static HTML receives an offline-safe review section; CSS receives
  supporting local-only styling and notes.
- Strict JSON, legal text, placeholder files, and generated terminal
  captures are not rewritten; they are recorded as skipped.
- Every inserted block is marked with `RESEARCH-GRADE-EXPANSION` so
  reviewers can search and diff the broad pass mechanically.

## Marker-Covered Surface Classes

- GitHub Actions workflow: 9
- GitHub issue template: 4
- Hermes Agent guide: 9
- Prompting OS module: 41
- agent prompt template: 12
- agent workflow guide: 3
- image-generation guide: 8
- installable agent skill: 127
- offline static-site asset: 5
- repository automation script: 18
- repository regression test: 8
- repository support file: 52
- research data configuration: 2
- tool guide: 11
- top-level repository policy document: 5

## Skipped Files

- `--watch`: terminal help capture; not public guide source
- `LICENSE`: legal text should not be rewritten mechanically
- `data/research/candidates.json`: strict JSON data/manifest; comments are invalid and shape changes risk breaking loaders
- `docs/research/curated/.gitkeep`: placeholder file has no content surface
- `docs/research/inbox/.gitkeep`: placeholder file has no content surface
- `skills/manifest.json`: strict JSON data/manifest; comments are invalid and shape changes risk breaking loaders

## Validation Required After Running

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
git diff --cached --check
```

## Reviewer Search Commands

```powershell
rg -n "RESEARCH-GRADE-EXPANSION" README.md AGENTS.md CONTRIBUTING.md SECURITY.md docs prompts skills scripts tests .github
git diff --stat
git diff --cached --stat
```
