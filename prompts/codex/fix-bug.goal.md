# Codex Prompt: Fix Bug

Paste this into Codex from the repository root.

```text
/goal
Objective:
Fix the following bug with the smallest safe change:
[Describe the bug here.]

Context:
- Read AGENTS.md first.
- Inspect the relevant files before editing.
- Preserve existing behavior unless it is clearly part of the bug.

Success criteria:
- The bug is fixed.
- A focused test is added or updated if practical.
- Local checks pass:
  - python scripts/repo_health_check.py
  - python scripts/safe_autofix.py --check
  - python -m unittest discover -s tests
- No unrelated files changed.

Safety boundaries:
- Do not edit `.env` or secrets.
- Do not delete files.
- Do not install dependencies without approval.
- Keep all changes inside this repository.

Final response:
- Summary
- Files changed
- Commands run
- Tests/checks run
- Remaining risks
```
