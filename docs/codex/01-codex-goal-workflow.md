# Codex Goal Workflow

Use Codex `/goal` when the task is larger than one normal response, such as fixing a bug, implementing a small feature, refactoring a module, improving documentation, or preparing a PR.

## Standard goal shape

```text
/goal
Objective:
[One clear task.]

Success criteria:
- [Criterion 1]
- [Criterion 2]
- Local checks pass.
- No unrelated files changed.

Safety boundaries:
- Do not edit `.env` or secrets.
- Do not delete files.
- Ask before installing dependencies.
- Keep all edits inside this repository.

Workflow:
1. Read AGENTS.md.
2. Run git status.
3. Inspect relevant files.
4. Plan minimal changes.
5. Edit only necessary files.
6. Run checks.
7. Fix failures if related.
8. Final report with changed files and commands run.
```

## Best tasks for `/goal`

| Task | Good `/goal` candidate? |
|---|---:|
| Fix one bug | Yes |
| Add one doc page | Yes |
| Refactor one script | Yes |
| Build entire app from nothing | Only with tight scope |
| Install ten tools | No |
| Clean entire computer | Absolutely not |

## Completion report format

Codex should end with:

```markdown
## Summary

## Files changed

## Commands run

## Tests/checks

## Remaining risks
```
