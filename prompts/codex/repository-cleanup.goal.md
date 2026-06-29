# Codex Prompt: Repository Cleanup

## Target Tool

OpenAI Codex.

## Purpose

Use this prompt for conservative cleanup that improves repository consistency without changing meaning, architecture, dependencies, or workflow behavior.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Cleanup type | "Fix Markdown headings and broken internal links" |
| Allowed files | `docs/`, `prompts/` |
| Forbidden files | `.github/workflows/`, `.env` |
| Validation | Safe autofix check and unit tests |

## Full Prompt

```text
/goal
Objective:
Clean up repository formatting and structure safely without changing meaning.

Allowed changes:
- Fix trailing whitespace.
- Ensure final newlines.
- Improve Markdown headings when the intent is obvious.
- Update broken internal references if found.
- Remove obvious empty placeholder sections only if they are clearly useless.
- Update CHANGELOG.md if the cleanup is user-visible.

Forbidden changes:
- Do not delete files.
- Do not change project purpose.
- Do not install dependencies.
- Do not edit secrets, .env files, private links, or private data.
- Do not rewrite large sections unnecessarily.
- Do not modify workflow YAML unless explicitly requested.
- Do not introduce exact pricing, model, or feature claims.

Success criteria:
- Repository meaning and behavior are preserved.
- Diff is small and reviewable.
- Local checks pass:
  - python scripts/repo_health_check.py
  - python scripts/safe_autofix.py --check
  - python -m unittest discover -s tests

Workflow:
1. Run git status.
2. Read AGENTS.md.
3. Inspect candidate files.
4. Prefer safe_autofix.py for whitespace cleanup.
5. Make only obvious manual cleanup.
6. Run checks.
7. Review git diff.

Final response:
- Summary
- Files changed
- Commands run
- Tests/checks run
- Remaining risks
```

## Short Version

```text
Clean up [AREA] without changing meaning. Keep edits small, do not delete files or add dependencies, run safe autofix/checks, review diff, and report files, commands, checks, and risks.
```

## Success Criteria

- Cleanup is deterministic or obviously editorial.
- No behavior changes unless explicitly requested.
- Diff is easy to review.
- Local checks pass.

## Safety Boundaries

- No deletion.
- No secrets.
- No dependency changes.
- No workflow YAML changes unless requested.
- No broad rewrites disguised as cleanup.

## Verification

```powershell
python scripts/safe_autofix.py --write
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff
```

## Final Report Format

```markdown
## Summary
## Files changed
## Commands run
## Tests/checks
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Cleanup becomes a rewrite | Stop and split into a docs task. |
| Unexpected files changed | Review and remove unrelated changes. |
| A file should be deleted | Ask for explicit approval. |
| Safe autofix changes many files | Review the full diff before committing. |
