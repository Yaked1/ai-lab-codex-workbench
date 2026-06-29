# Task Spec

Use this template before asking Codex or another AI coding agent to work.

## Task Title

```text
[Short public-safe title]
```

## Objective

```text
[One clear outcome. Avoid vague requests such as "improve everything."]
```

## Background

- Why this change is needed:
- Who benefits:
- Relevant issue or discussion:
- Tool intended for the task:

## Files The Agent Should Inspect First

- `AGENTS.md`
- `README.md`
- `[add relevant docs, scripts, or tests]`

## Included Scope

- [ ] `[file or folder]`
- [ ] `[specific behavior or section]`

## Excluded Scope

- [ ] Do not edit secrets or `.env` files.
- [ ] Do not install dependencies without approval.
- [ ] Do not delete files.
- [ ] Do not change unrelated folders.
- [ ] Do not modify workflow YAML unless explicitly requested.
- [ ] Do not add exact pricing, model, or platform claims without official-doc verification.

## Success Criteria

- [ ] The requested change is complete.
- [ ] The diff is focused.
- [ ] Beginner-facing docs are clear.
- [ ] Public-safety rules still hold.
- [ ] Checks pass or failures are honestly reported.
- [ ] Final response lists files changed, commands run, checks run, and remaining risks.

## Safety Boundaries

- Keep work inside this repository.
- Do not inspect private folders.
- Do not print environment variables.
- Do not add secrets, private links, or personal data.
- Ask before destructive commands.
- Ask before dependency installation.

## Local Checks

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Report Format

```markdown
## Summary

## Files changed

## Commands run

## Checks/tests

## Claims needing manual verification

## Remaining risks
```
