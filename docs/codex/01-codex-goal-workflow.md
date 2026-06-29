# Codex Goal Workflow

Use a Codex goal when a task requires more than a quick answer: fixing a bug, implementing a small feature, improving several docs, reviewing a PR, or preparing a branch for merge.

The point of a goal is not to make the agent unbounded. The point is to give it a durable, explicit objective with scope, safety boundaries, verification, and a final report.

## When To Use A Goal

| Task | Goal fit | Notes |
| --- | --- | --- |
| Fix one bug | Strong | Include reproduction steps and expected behavior. |
| Add one documentation guide | Strong | Include audience and required sections. |
| Expand prompt templates | Strong | Include shared template structure. |
| Review a PR | Strong | Make it read-only unless edits are requested. |
| Refactor one script | Medium | Require tests and small diff. |
| Build an entire app | Weak | Split into design, scaffold, and feature PRs. |
| Install many tools | Avoid | Too much setup and risk for one goal. |

## Standard Goal Shape

```text
Objective:
[One clear task.]

Context:
- Read AGENTS.md.
- Run git status.
- Inspect [files] before editing.

Included scope:
- [Allowed files/folders.]

Excluded scope:
- Do not edit .env or secrets.
- Do not delete files.
- Do not install dependencies without approval.
- Do not modify workflow YAML unless requested.
- Keep changes inside this repository.

Success criteria:
- [Criterion 1.]
- [Criterion 2.]
- Local checks pass.
- No unrelated files changed.
- Final response includes changed files and commands run.

Workflow:
1. Inspect relevant files.
2. Make a short plan.
3. Edit the smallest necessary files.
4. Run checks.
5. Fix related failures.
6. Report unverified claims and remaining risks.
```

## Good Goal Prompt Example

```text
Objective:
Expand docs/tools/codex.md into a practical guide for beginner Windows users.

Context:
- Read AGENTS.md.
- Inspect README.md and docs/tools/comparison-matrix.md.

Included scope:
- docs/tools/codex.md
- CHANGELOG.md if the change is user-visible.

Excluded scope:
- Do not edit workflow YAML.
- Do not add dependencies.
- Do not include exact pricing or unsupported model claims.

Success criteria:
- The guide includes what it is, best use cases, setup style, Windows suitability, safety risks, review checklist, alternatives, and official-doc verification notes.
- PowerShell examples are used where commands are needed.
- Local checks pass.

Verification:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
```

## Bad Goal Prompt Example

```text
Make this repo professional and fix anything you see.
```

Why it is weak:

- No included scope.
- No excluded scope.
- No success criteria.
- No safety boundaries.
- No verification commands.
- No definition of "professional."

## Goal Execution Checklist

- [ ] Start from the repository root.
- [ ] Run `git status`.
- [ ] Read `AGENTS.md`.
- [ ] Inspect relevant files before editing.
- [ ] Keep a minimal plan.
- [ ] Avoid unrelated cleanup.
- [ ] Run local checks.
- [ ] Review `git diff`.
- [ ] Update changelog when useful.
- [ ] Report remaining risks.

## Verification Commands

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

If safe autofix reports changes:

```powershell
python scripts/safe_autofix.py --write
python scripts/safe_autofix.py --check
```

Review the diff after any write command.

## Failure Modes

| Failure | Cause | Fix |
| --- | --- | --- |
| Agent edits unrelated files | Prompt scope too broad. | Re-scope and remove unrelated edits after review. |
| Checks not run | Goal did not require verification. | Add explicit commands to the prompt. |
| Tool claims are stale | Product behavior was assumed. | Reword with official-doc verification note. |
| Diff is too large | Task was not split. | Break into smaller PRs. |
| Final report is vague | Report format was not specified. | Require files changed, commands, checks, and risks. |

## Completion Report Format

Codex should end with:

```markdown
## Summary

## Files changed

## Commands run

## Tests/checks

## Remaining risks
```

For public docs work, add:

```markdown
## Claims needing manual verification
```
