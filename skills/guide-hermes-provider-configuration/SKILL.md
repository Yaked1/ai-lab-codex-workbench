---
name: guide-hermes-provider-configuration
description: Use the Hermes Agent Provider Configuration guide from docs/hermes/provider-configuration.md as a bounded, public-safe workflow.
category: hermes
source:
  - docs/hermes/provider-configuration.md
---

# Hermes Agent Provider Configuration

## Trigger

Use this skill when the task is about `docs/hermes/provider-configuration.md` or the topic covered by **Hermes Agent Provider Configuration**, and the source guide is the right local authority to inspect before acting. Do not use this skill for unrelated work or as permission to broaden
the task beyond the files and actions the human requested.

## Purpose

Convert the source guide into a short, repeatable operating procedure: read the authoritative document, keep work scoped, avoid unsupported claims, and report evidence clearly.

## Inputs

- The user's current task or question.
- The source file: `docs/hermes/provider-configuration.md`.
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

1. Read `docs/hermes/provider-configuration.md` in full before editing, summarizing, or applying it.
2. Read `AGENTS.md` if the task may change repository files.
3. Restate the specific goal, in-scope files, out-of-scope files, and verification commands.
4. Apply only the guidance relevant to the current task; link back to the source guide for deeper explanation instead of copying large sections.
5. Mark fast-changing product behavior, model availability, pricing, platform support, or setup details as official-doc verification items unless freshly checked.
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

- Source used: `docs/hermes/provider-configuration.md`.
- Files changed, if any.
- Commands run and whether they passed.
- Current-claim or official-doc verification items left unresolved.
- Remaining risks or skipped checks.

## Disable Path

Remove `skills/guide-hermes-provider-configuration/` from the installed harness location, or remove this
folder from the repository together with its `skills/manifest.json` entry and
`skills/INDEX.md` row in the same reviewed change.
