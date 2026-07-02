# Skill And Prompt Guide Generator Prompt

Target tool: Local Codex curator prompt

Purpose: generate public-safe skills, prompt-guide, Codex, Claude Code, and MCP
guide updates from vetted candidate sources.

Every generated skill guide must include:

- What the skill does.
- Which tool it is for.
- How to install it, only if verified from official docs.
- How to test it.
- Safe example use cases.
- Unsafe or inappropriate use cases.
- Required files.
- Expected folder structure.
- Common errors.
- How to uninstall or disable it.
- Public repository safety notes.

Every generated prompt guide must include:

- Target model or tool.
- Purpose.
- Full prompt.
- Optional shorter version.
- Why the prompt works.
- Failure cases.
- Output-format constraints.
- Safety boundaries.
- Evaluation method.
- Revision checklist.

General constraints:

- Do not add dependencies.
- Do not invent current product behavior.
- Mark fast-changing details as official-doc verification items.
- Keep beginner guidance practical and auditable.
- Include source references and license/source status.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `.github/codex/prompts/skill-guide-generator.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `skill guide generator` state what decision, workflow, or reusable behavior it supports?
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
