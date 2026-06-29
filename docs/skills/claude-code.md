# Claude Code Skills

Source status: official-doc anchored. Verify current setup in the official
Claude Code skills documentation before teaching exact install or distribution
steps: <https://code.claude.com/docs/en/skills>

## What It Is

Claude Code skills are reusable instruction bundles that extend Claude Code for
specialized tasks. A skill can describe procedures, expected files, resources,
and scripts that Claude should load when the skill is relevant.

## Beginner Friendliness

Medium. Skills are useful after a learner understands normal Claude Code use,
Git branches, and review. Beginners should start with one read-only docs skill
before adding scripts or write-capable workflows.

## Installation

Use the official Claude Code skills documentation as the source of truth.

Placeholder until verified for a target environment:

```powershell
# Placeholder only. Verify the current official Claude Code skill path first.
New-Item -ItemType Directory -Path .\skills\example-skill -Force
New-Item -ItemType File -Path .\skills\example-skill\SKILL.md -Force
```

Do not publish exact global install commands unless they are checked against
official docs in the same PR.

## Required Files And Folder Shape

Typical skill bundles include:

```text
example-skill/
  SKILL.md
  references/
  scripts/
  assets/
```

Only `SKILL.md` should be mandatory for the simplest public example. Add scripts
only when they are necessary and safe to run.

## How To Test

- Ask Claude Code to explain when the skill should trigger.
- Run the skill on a read-only documentation task.
- Review the generated diff.
- Run repository checks if files changed.

## Safe Use Cases

- Documentation review.
- Prompt review.
- Release-note drafting.
- Public checklist generation.
- Read-only repository explanation.

## Unsafe Or Inappropriate Use Cases

- Secret extraction.
- Browser profile access.
- Private conversation summarization.
- Unreviewed edits to `.env`, credentials, or private files.
- Skills that encourage prompt leaking, jailbreaks, or bypass behavior.

## Common Errors

| Error | Likely cause | Response |
| --- | --- | --- |
| Skill does not trigger | Metadata or description is too vague. | Make the trigger case explicit. |
| Skill overreaches | The skill asks for broad edits. | Narrow the allowed files and actions. |
| Private paths appear | Local examples were copied into docs. | Replace with public placeholders. |

## Disable Or Uninstall

Remove the skill folder from the active skill location, or move it outside the
tool's configured skill path. Do not delete shared repo content unless that is
the explicit maintenance task.

## Public Repository Safety

- Keep examples generic.
- Do not commit private skills.
- Do not include real tokens, personal paths, account IDs, or private links.
- Include failure modes and verification steps in every public skill guide.
