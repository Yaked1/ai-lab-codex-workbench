# Google Antigravity Agent Task Template

## Target Tool

Google Antigravity.

## Purpose

Use this template for a bounded Antigravity task. Product behavior changes quickly, so verify current official documentation before relying on a specific feature, artifact type, agent mode, or platform surface.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Task | "Plan a documentation cleanup for docs/tools" |
| Mode | "Plan first, edit only after approval" |
| Files | `docs/tools/*.md` |
| Verification | Local checks |

## Full Prompt

```text
Target tool:
Google Antigravity

Goal:
Create a reviewed plan or small implementation for:
[TASK]

Mode:
[PLAN ONLY / PLAN THEN EDIT AFTER APPROVAL / SMALL IMPLEMENTATION]

Instructions:
- Read AGENTS.md first.
- Keep work inside this repository.
- Use one branch for one task.
- Produce a plan artifact before editing if the task touches more than one file.
- Prefer documentation or testable small changes for first runs.
- List exact files before editing.
- Keep external tool claims conservative and mark them for official-doc verification.

Boundaries:
- Do not expose secrets or private links.
- Do not modify GitHub workflow files unless explicitly requested.
- Do not add dependencies.
- Do not run destructive automation.
- Do not let parallel agents edit overlapping files without review.

Validation:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

Final response:
- Plan or implementation summary
- Files changed
- Commands/checks run
- Claims needing manual verification
- Remaining risks
```

## Short Version

```text
Use Antigravity to plan [TASK]. Read AGENTS.md, list files first, do not edit until approved, avoid secrets/dependencies/workflow changes, run checks after edits, and report verification gaps.
```

## Included Scope

- Files, plans, issue text, or repository areas explicitly named by the human.
- The requested task and adjacent documentation needed to keep links accurate.
- Verification steps that are safe and relevant to the edited area.

## Excluded Scope

- Secrets, `.env` files, credentials, private links, private paths, and browser
  profiles.
- Dependency installation, workflow YAML, generated archives, account actions,
  and destructive commands unless explicitly approved.
- Exact current product claims unless verified in official docs.

## Success Criteria

- Plan or implementation is bounded.
- File ownership is clear.
- No overlapping unreviewed agent edits.
- Local checks pass after edits.
- Product-specific claims are marked for official verification.

## Safety Boundaries

- No secrets or private links.
- No destructive automation.
- No broad parallel edits.
- No unverified setup claims.
- No workflow YAML changes unless requested.

## Verification

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Report Format

```markdown
## Summary
## Plan or files changed
## Commands/checks
## Claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Product behavior is unclear | Stop and verify official docs. |
| Agents propose overlapping edits | Assign file ownership or use one agent. |
| Task becomes broad | Split into smaller tasks. |
| Checks cannot run | Report why and what remains unverified. |
