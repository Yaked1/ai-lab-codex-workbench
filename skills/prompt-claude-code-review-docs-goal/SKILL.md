---
name: prompt-claude-code-review-docs-goal
description: Adapt the Claude Code Goal: Review Documentation prompt template from prompts/claude-code/review-docs.goal.md with scope, safety, and verification intact.
category: prompts
source:
  - prompts/claude-code/review-docs.goal.md
---

# Claude Code Goal: Review Documentation

## Trigger

Use this skill when a task should reuse the prompt template in `prompts/claude-code/review-docs.goal.md` and the human wants the template adapted without dropping its scope, safety, verification, or final-report rules. Do not use this skill for unrelated work or as permission to broaden
the task beyond the files and actions the human requested.

## Purpose

Turn the source prompt template into an executable work order for the current task while preserving the repository's public-safety and evidence requirements.

## Inputs

- The user's current task or question.
- The source file: `prompts/claude-code/review-docs.goal.md`.
- Any files, tools, or outputs explicitly named by the user.
- The verification commands that apply to the touched area.

## Scope

Allowed: read the source file, follow its public-safe workflow guidance, and
edit only files that the current task explicitly brings into scope.

Forbidden unless explicitly approved: secrets, `.env` files, credentials,
private links, private local paths, dependency additions, workflow YAML edits,
destructive commands, direct pushes to protected branches, and broad rewrites
outside the current task.

## Procedure

1. Read `prompts/claude-code/review-docs.goal.md` in full before adapting it.
2. Fill every placeholder with task-specific context from the human or the repository.
3. Preserve included scope, excluded scope, safety boundaries, verification steps, success criteria, failure cases, and final-report format.
4. Remove irrelevant examples, but do not weaken safety or review requirements.
5. If the adapted prompt would require secrets, private paths, new dependencies, workflow changes, or destructive commands, stop and ask for explicit approval.
6. Run the verification listed below if any repository files changed.

## Verification

For repository edits, run the strongest relevant subset of:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

For read-only use, verify by citing the source file and clearly separating
source facts from assumptions or recommendations.

## Failure Cases

- The source file is missing, unreadable, or no longer matches the task.
- The task needs current external product behavior that has not been verified
  in official docs.
- The requested change would touch secrets, private data, dependencies,
  workflow YAML, or destructive commands without explicit approval.
- Verification fails for a reason outside the current task's scope.
- The source guide and the human's request conflict; ask for direction instead
  of guessing.

## Final Report

- Source used: `prompts/claude-code/review-docs.goal.md`.
- Files changed, if any.
- Commands run and whether they passed.
- Current-claim or official-doc verification items left unresolved.
- Remaining risks or skipped checks.

## Disable Path

Remove `skills/prompt-claude-code-review-docs-goal/` from the installed harness location, or remove this
folder from the repository together with its `skills/manifest.json` entry and
`skills/INDEX.md` row in the same reviewed change.
