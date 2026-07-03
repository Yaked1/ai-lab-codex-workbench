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
