# AI Skills And Prompt Guides

This folder collects public-safe guide patterns for agent skills, prompt guides,
and tool-use workflows. It is for general readers, so every guide should be
clear about prerequisites, safety boundaries, failure modes, verification, and
source status.

## Guide Map

| Guide | Use it for |
| --- | --- |
| [Claude Code skills](claude-code.md) | Understanding Claude Code skill structure and safety checks. |
| [Codex skills](codex.md) | Creating public-safe Codex skills and skill-like repo workflows. |
| [MCP tool-use systems](mcp.md) | Connecting tools through MCP without overexposing private data. |
| [Prompt guides](prompt-guides.md) | Writing reusable prompts with evaluation and revision criteria. |

## Quality Bar

Every generated guide should include:

- What the tool, skill, or resource is.
- Beginner friendliness.
- Public-safe use cases.
- Installation commands only when verified.
- Placeholder commands when not verified.
- Windows-friendly notes.
- Linux/macOS notes when useful.
- API key or subscription requirements.
- Hardware requirements where relevant.
- Whether it is realistic for entry-level hardware.
- Safer lightweight alternatives.
- Failure modes.
- Evaluation checklist.
- Links/source references.
- License/source status.

## Public-Safe Defaults

- Start with read-only examples.
- Keep secrets out of the repository.
- Do not copy private skill folders or private prompt packs.
- Use branch, PR, checks, review, and merge for generated updates.
- Mark fast-changing product behavior as an official-doc verification item.
