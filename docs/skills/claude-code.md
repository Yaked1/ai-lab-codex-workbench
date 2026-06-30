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

## Skill Design Checklist

- [ ] The skill has a narrow trigger.
- [ ] `SKILL.md` can be read without private context.
- [ ] References are public-safe.
- [ ] Scripts are optional and documented.
- [ ] The skill starts read-only when possible.
- [ ] Write-capable actions name allowed files.
- [ ] The skill avoids hidden prompts, private memories, and credentials.
- [ ] The skill final report is reviewable.

## Example Read-Only Skill Brief

```markdown
# Public Docs Reviewer

Trigger:
Use when the user asks for a documentation review in this repository.

Procedure:
1. Read AGENTS.md.
2. Read README.md and requested docs.
3. Review for clarity, safety, source support, and verification.
4. Do not edit files.
5. Report findings first, ordered by severity.

Forbidden:
- Secrets.
- Private links.
- Private machine paths.
- Exact current tool claims without official-doc verification.
```

## Write-Capable Skill Gate

Before a Claude Code skill edits files:

1. It should name files in scope.
2. It should name files out of scope.
3. It should avoid dependency changes unless explicitly approved.
4. It should run or request the relevant checks.
5. It should report changed files and risks.

If those gates are missing, keep the skill read-only.

## Review Questions

- Does the skill trigger too broadly?
- Does it duplicate a normal prompt template?
- Are local examples generic and public-safe?
- Are source claims official-doc verified or conservative?
- Does the guide explain how to disable the skill?
- Does it state what to do when checks fail?
