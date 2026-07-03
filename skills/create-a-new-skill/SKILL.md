---
name: create-a-new-skill
description: Use when a task keeps recurring and deserves its own skill bundle in this repository's skills/ package, or when a human asks to author a new prompting skill from an existing doc, prompt template, or workflow.
category: meta
source:
  - docs/skills/README.md
  - skills/README.md
  - skills/use-codex-safely/SKILL.md
---

# Create A New Skill

## Trigger

Use this skill when: the same task has been done manually more than once
and would benefit from a repeatable procedure, or a human explicitly asks
for a new skill to be added to `skills/`. Do not use it for a one-off task
that will not recur, and do not use it to duplicate a skill that already
covers the same trigger -- check `skills/INDEX.md` first.

## Purpose

Turn a recurring task or an existing doc/prompt template into a properly
formed skill bundle that matches this repository's own format, so it can be
installed and reused the same way every other skill in `skills/` can. A
prompting skill is still a real skill: it must have a source file, trigger,
scope, procedure, verification, and disable path, not just a title or empty
scaffold.

## Inputs

- The recurring task, in one sentence, or the source doc/prompt template to
  package.
- A proposed `<slug>` (lower-kebab-case) that does not collide with an
  existing entry in `skills/INDEX.md`.
- A category: `tools`, `prompts`, `codex-workflow`, `hermes`,
  `image-generation`, `guides`, or `meta`.

## Scope

Allowed: creating exactly one new folder, `skills/<slug>/`, containing
`SKILL.md` (and, only if genuinely needed, a small `references/` or
`scripts/` folder); adding one row to `skills/INDEX.md` and one entry to
`skills/manifest.json`. Forbidden: editing any other existing skill,
editing the source guide the new skill packages, or editing anything under
`docs/` or `prompts/` as part of this task.

## Procedure

1. Check `skills/INDEX.md` for an existing skill with an overlapping
   trigger. If one exists, extend or correct it instead of adding a
   duplicate.
2. Identify the source guide(s) this skill will summarize -- a file under
   `docs/`, `prompts/`, or another skill. Read every source file in full.
3. Draft `skills/<slug>/SKILL.md` with the required frontmatter (`name`,
   `description`, `category`, `source`) and the nine required sections
   (`## Trigger` through `## Disable Path`) -- copy the structure of
   [skills/use-codex-safely/SKILL.md](../use-codex-safely/SKILL.md) as the
   pattern to follow.
4. Keep it short: 40-120 lines. If a point needs more explanation than
   that, link to the source guide instead of inlining it.
5. Apply every rule in [skills/README.md](../README.md#content-rules-inherited-from-agentsmd):
   no invented pricing/availability claims, no secrets or private paths,
   Windows PowerShell examples, no GPU/Docker/WSL as a default, and the
   Hermes-scope restriction if the skill is Hermes-related.
6. Add one row to `skills/INDEX.md` (slug, description, category, source)
   and one object to `skills/manifest.json` in the same shape as the
   existing entries.
7. Run verification before reporting done.

## Verification

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
python -m unittest tests.test_skills_package
```

`tests/test_skills_package.py` specifically checks frontmatter, required
sections, that every declared `source` path exists, and that
`skills/INDEX.md` has no orphaned or missing entries -- treat any failure
there as the new skill not being done yet.

## Failure Cases

- The proposed skill would duplicate an existing trigger -- extend the
  existing skill instead of adding a near-identical one.
- The source guide does not exist yet, or the task cannot point at a real
  file -- write the guide first (outside this skill's scope) rather than
  fabricating claims inside the skill body.
- The skill would need a new external dependency to be useful -- stop and
  ask for explicit approval; this repository's skills stay
  standard-library and dependency-free by default.
- The trigger is too broad ("use for all docs tasks") -- narrow it with a
  concrete example before publishing.

## Final Report

- The new skill's path, category, and one-line trigger.
- Source file(s) it packages.
- Whether `skills/INDEX.md` and `skills/manifest.json` were updated.
- Verification commands run and their results.
- Any current-product claim intentionally left marked for official-doc
  re-verification before publication.

## Disable Path

Delete the skill's folder under `skills/`, remove its row from
`skills/INDEX.md`, and remove its entry from `skills/manifest.json` in the
same change -- `tests/test_skills_package.py` will fail loudly if any one
of those three is forgotten.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **installable agent skill** surface. During broad
maintenance, reviewers should treat `skills/create-a-new-skill/SKILL.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `create a new skill` state what decision, workflow, or reusable behavior it supports?
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
