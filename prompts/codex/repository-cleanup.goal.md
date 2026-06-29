# Codex Prompt: Repository Cleanup

```text
/goal
Objective:
Clean up repository formatting and structure safely without changing meaning.

Allowed changes:
- Fix trailing whitespace.
- Ensure final newlines.
- Improve headings in docs.
- Update broken internal references if found.
- Remove obvious empty placeholder sections only if they are clearly useless.

Forbidden changes:
- Do not delete files.
- Do not change project purpose.
- Do not install dependencies.
- Do not edit secrets.
- Do not rewrite large sections unnecessarily.

Success criteria:
- python scripts/repo_health_check.py passes.
- python scripts/safe_autofix.py --check passes.
- python -m unittest discover -s tests passes.
- Diff is small and reviewable.

Final response:
- Summary
- Files changed
- Commands run
- Tests/checks run
- Remaining risks
```
