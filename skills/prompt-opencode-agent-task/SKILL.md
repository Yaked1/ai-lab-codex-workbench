---
name: prompt-opencode-agent-task
description: Adapt the OpenCode Agent Task Template prompt template from prompts/opencode/agent-task.md with scope, safety, and verification intact.
category: prompts
source:
  - prompts/opencode/agent-task.md
---

# OpenCode Agent Task Template

## Trigger

Use this skill when a task should reuse the prompt template in `prompts/opencode/agent-task.md` and the human wants the template adapted without dropping its scope, safety, verification, or final-report rules. Do not use this skill for unrelated work or as permission to broaden
the task beyond the files and actions the human requested.

## Purpose

Turn the source prompt template into an executable work order for the current task while preserving the repository's public-safety and evidence requirements.

## Inputs

- The user's current task or question.
- The source file: `prompts/opencode/agent-task.md`.
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

1. Read `prompts/opencode/agent-task.md` in full before adapting it.
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

- Source used: `prompts/opencode/agent-task.md`.
- Files changed, if any.
- Commands run and whether they passed.
- Current-claim or official-doc verification items left unresolved.
- Remaining risks or skipped checks.

## Disable Path

Remove `skills/prompt-opencode-agent-task/` from the installed harness location, or remove this
folder from the repository together with its `skills/manifest.json` entry and
`skills/INDEX.md` row in the same reviewed change.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **installable agent skill** surface. During broad
maintenance, reviewers should treat `skills/prompt-opencode-agent-task/SKILL.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `prompt opencode agent task` state what decision, workflow, or reusable behavior it supports?
- Are included scope, excluded scope, and unsafe actions clear enough for an
  agent or contributor to follow?
- Are examples public-safe, repository-relative, and free of private data?
- Are fast-changing product or platform claims phrased conservatively or marked
  for official-doc verification?
- Does the file point to the next artifact a reader should inspect: a command,
  template, test, manifest, package, or deeper guide?
- Could a reviewer cite this file in a PR review and know what evidence proves
  the work is complete?

Keep future edits focused on stronger evidence, clearer failure modes, better
navigation, and safer automation boundaries. Do not add length unless the new
material makes the repository easier to operate, teach, audit, or recover.
<!-- RESEARCH-GRADE-EXPANSION:END -->
