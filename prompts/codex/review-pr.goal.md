# Codex Prompt: Review Pull Request

```text
/goal
Objective:
Review the current branch or PR diff for correctness, safety, and maintainability.

Instructions:
- Read AGENTS.md.
- Run git status.
- Inspect git diff against main.
- Do not modify files unless explicitly asked.

Review checklist:
- Does the change solve the stated task?
- Are there unrelated edits?
- Are secrets or private files included?
- Are tests/checks adequate?
- Is the solution too complex?
- Is documentation updated when needed?

Output:
1. Verdict: approve/request changes/comment only
2. Summary
3. Risks
4. Required fixes
5. Optional improvements
6. Commands inspected or run
```
