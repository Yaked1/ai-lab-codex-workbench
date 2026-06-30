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

## Skill Lifecycle

| Phase | Output | Review gate |
| --- | --- | --- |
| Idea | Short description of the repeated task. | Is this frequent enough to deserve a skill or guide? |
| Scope | Allowed files, forbidden files, tools, and commands. | Does the skill avoid secrets, private paths, and destructive actions? |
| Draft | `SKILL.md`, prompt guide, or tool-use instructions. | Does it include trigger, purpose, steps, failure cases, and verification? |
| Read-only test | Agent explains or reviews without editing. | Does it trigger at the right time and stay bounded? |
| Write-capable test | Agent edits a small fixture or docs page. | Are diffs scoped and checks run? |
| Package/release | Guide is linked and included where appropriate. | Are source status and changelog updated? |
| Maintenance | Periodic review against official docs and local checks. | Are stale commands removed or marked for verification? |

## Skill Or Prompt Guide Decision

Use a skill when:

- The same task recurs often.
- The agent needs a consistent procedure.
- References or helper scripts are useful.
- The workflow has non-obvious safety boundaries.

Use a prompt guide when:

- The task is occasional.
- The user should read and adapt the prompt manually.
- A single Markdown template is enough.
- Current product behavior is changing too quickly for a bundled skill.

Use normal documentation when:

- The material is mostly explanation.
- There is no agent action to repeat.
- The safest output is a checklist or review guide.

## Public Example Rules

Public examples should use:

- Placeholder paths such as `docs/example.md`.
- Placeholder tokens such as `<API_TOKEN>` only in explanatory text.
- Public-safe repository tasks.
- Read-only first runs.
- Checks that exist in this repository.
- Conservative product claims with official-doc verification notes.

Public examples should not use:

- Real private paths.
- Private memories.
- Hidden prompts.
- Browser profile data.
- Screenshots with account details.
- Commands that publish, delete, or spend money.

## Review Checklist

- [ ] The guide says when to use the skill and when not to use it.
- [ ] Source status is clear.
- [ ] Install/setup commands are official-doc verified or marked as placeholders.
- [ ] Safety boundaries are concrete.
- [ ] Failure modes are listed.
- [ ] Verification commands are present.
- [ ] The final report format is reviewable.
- [ ] The guide links back to prompt templates, Prompting OS, or workflow docs.
