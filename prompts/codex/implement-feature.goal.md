# Codex Prompt: Implement Feature

```text
/goal
Objective:
Implement this small feature:
[Describe feature.]

User context:
This project is for a Windows 11 student laptop. Prefer lightweight Python standard-library scripts, Markdown docs, GitHub Actions, and PowerShell commands. Avoid Docker, WSL, heavy local models, and large dependencies unless explicitly approved.

Success criteria:
- Feature is implemented in the smallest reasonable way.
- README or docs updated if user-facing behavior changes.
- Tests/checks are added or updated when practical.
- Local checks pass:
  - python scripts/repo_health_check.py
  - python scripts/safe_autofix.py --check
  - python -m unittest discover -s tests
- No unrelated files changed.

Safety boundaries:
- Do not edit secrets.
- Do not delete files.
- Ask before installing dependencies.
- Do not modify system settings.

Workflow:
1. Read AGENTS.md.
2. Run git status.
3. Inspect relevant files.
4. Plan briefly.
5. Implement.
6. Run checks.
7. Fix related failures.
8. Report results.
```
