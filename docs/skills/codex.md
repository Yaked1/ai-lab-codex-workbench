# Codex Skills

Source status: official-doc anchored. Verify current behavior in OpenAI Codex
skills documentation before publishing exact setup claims:
<https://developers.openai.com/codex/skills>

## What It Is

Codex skills package task-specific instructions, resources, and optional scripts
so Codex can follow repeatable workflows. They are useful for recurring
documentation, review, testing, or research workflows when the boundaries are
clear.

## Beginner Friendliness

Medium. A learner should understand `AGENTS.md`, Git branches, local checks, and
PR review before creating write-capable skills.

## Installation

Use the official Codex skills documentation as the source of truth. If the
current supported path is not verified, publish placeholders only:

```powershell
# Placeholder only. Verify the current Codex skill location first.
New-Item -ItemType Directory -Path .\skills\docs-review -Force
New-Item -ItemType File -Path .\skills\docs-review\SKILL.md -Force
```

## Required Files And Folder Shape

```text
docs-review/
  SKILL.md
  references/
  scripts/
```

Keep `references/` and `scripts/` optional. If a script is included, document how
to run it, how to test it, and what files it may touch.

## How To Test

```powershell
git status
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

For a skill-specific test, ask Codex to run a read-only explanation task before
allowing edits.

## Safe Use Cases

- Public documentation curation.
- Prompt-template review.
- Source-safety review.
- Small script testing.
- PR summary drafting.

## Unsafe Or Inappropriate Use Cases

- Unrestricted daily publishing.
- Direct pushes to `main`.
- Secret scanning that prints secrets.
- Private folder indexing.
- Prompt leaking or jailbreak guidance.
- Broad workflow rewrites without a dedicated automation task.

## Common Errors

| Error | Likely cause | Response |
| --- | --- | --- |
| Codex edits too much | Skill lacks excluded scope. | Add explicit allowed and forbidden paths. |
| Commands are stale | Product behavior changed. | Mark as official-doc verification items. |
| Checks are skipped | Skill ends at drafting. | Require validation and final reporting. |

## Disable Or Uninstall

Move or remove the skill folder from the active Codex skill location. For a repo
example, remove it through a normal branch and PR.

## Public Repository Safety

- Keep skill docs public-safe.
- Do not commit private memories or hidden local config.
- Do not add dependencies unless explicitly approved.
- Keep generated guide updates behind branch, PR, checks, and review.
