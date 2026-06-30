# Archive Audit: GitHub_Downloads

Source: local ZIP archive folder inspected during repository curation. The
machine-specific path is intentionally not published.

This audit covers 25 archives. Six were pre-extracted in `extracted_files/` and inspected directly. The rest were read from the archive. Nine archives were unreadable by the built-in ZIP reader and are marked `BROKEN`.

## Usability

Use these columns when deciding whether to reference an archive in public docs or learning paths:
- `Public-safe`: safe to mention in a public guide without leaking secrets.
- `Usefulness`: how directly it improves prompting, agent workflows, image generation, or repo hygiene, not marketing or duplicate noise.
- `Usability`: can a beginner actually use this now, or is it archive-only / anecdote / relationship advice?

## Inventory

| Archive | Status | Primary README | Public-safe | Usefulness | Usability | Notes |
|---|---|---|---|---|---|---|
| `agent-coworker-main.zip` | Extracted | `agent-coworker-main/README.md` | Yes | High | Medium-High | Terminal-first AI coworker with WebSocket decoupled UI, TUI/CLI/desktop/web interfaces, skills/sub-agents, and provider support. Good teaching sample for multi-interface agent architecture. |
| `chromex-main.zip` | Extracted | `chromex-main/README.md` | Yes | High | Medium | Chrome MV3 side-panel assistant connected to Codex via local native bridge. Usable for browser-aware workflows, page-aware chat, and media inputs. |
| `CL4R1T4S-main.zip` | Not extracted | `CL4R1T4S-main/README.md` | Verify | Low | Low | Need to inspect README before classifying. Add classification after reading. |
| `claude-mem-9.0.12.zip` | Extracted | `claude-mem-9.0.12/README.md` | Yes | Medium-Low | Low | Persistent memory compression system for Claude Code. Interesting, but narrow beginner usefulness and not a beginner default. |
| `claw-code-main.zip` | Extracted | `claw-code-main/README.md` | No | Low | Low | Contains leaked-source narrative, brand amplifier text, and anecdotal media references. Treat as non-authoritative and avoid in public repo references. |
| `git-time-explorer-main.zip` | Not extracted | `git-time-explorer-main/README.md` | Yes | Medium | Medium | Windows-only git history browser and virtual-drive explorer. Useful for Windows beginners learning version history navigation. |
| `gjtjx-awesome-structued-prompts.zip` | Not extracted | `awesome-structued-prompts-main/README-en.md` | Yes | Medium | Medium | Structured prompt anthology for ChatGPT/Claude/Stable Diffusion/Midjourney. Usable for prompt design inspiration. |
| `JindongGu-Awesome-Prompting-on-Vision-Language-Model.zip` | Not extracted | `Awesome-Prompting-on-Vision-Language-Model-main/README.md` | Yes | High | Medium-High | Survey and paper list for VLM prompting. Strong reference value for multimodal image/generation prompting. |
| `langgptai-Awesome-Multimodal-Prompts.zip` | BROKEN | unknown | Unknown | Unknown | Unknown | Unreadable by the ZIP reader. Needs repair or extraction outside the script path. |
| `microsoft-Build25-LAB324.zip` | BROKEN | unknown | Unknown | Unknown | Unknown | Unreadable by the ZIP reader. Needs repair or extraction outside the script path. |
| `microsoft-generative-ai-for-beginners.zip` | BROKEN | unknown | Unknown | Unknown | Unknown | Unreadable by the ZIP reader. Needs repair or extraction outside the script path. |
| `nidhinjs-prompt-master.zip` | Not extracted | `prompt-master-main/README.md` | Yes | High | Medium-High | Prompt-engineering skill for Claude/Midjourney/audio/video and agent tools. High usefulness for prompt optimization. |
| `openai-openai-cookbook.zip` | BROKEN | unknown | Unknown | Unknown | Unknown | Unreadable by the ZIP reader. Needs repair or extraction outside the script path. |
| `page-agent-main.zip` | Extracted | `page-agent-main/README.md` | Yes | High | Medium | In-page GUI agent with natural-language web control and optional Chrome extension. Useful for SaaS copilot and automation patterns. |
| `Prompt-Engineering-Guide-main.zip` | Not extracted | `Prompt-Engineering-Guide-main/README.md` | Yes | High | High | Foundational prompt engineering guide with techniques, RAG, and agent prompting. Primary reference quality. |
| `promptslab-Awesome-Prompt-Engineering.zip` | Not extracted | `Awesome-Prompt-Engineering-main/README.md` | Yes | High | High | Curated prompt and context engineering resources with papers, tools, and provider docs. |
| `rsmdt-multimodal-mcp.zip` | Not extracted | `multimodal-mcp-main/README.md` | Yes | High | High | Unified multimodal MCP server for image/video/audio generation. Directly increases real tool usefulness. |
| `stop-slop-main.zip` | Not extracted | `stop-slop-main/README.md` | Yes | Medium-High | High | Claude/LLM skill that removes AI-tell prose patterns with before/after examples. Practical for improving prompt output quality. |
| `superpowers-main.zip` | Extracted | `superpowers-main/README.md` | Verify | Medium | Medium | Agent workflow skill with spec-first planning, TDD, subagent-driven execution. Needs leak-free adapter for this repo. |
| `YingqingHe-Awesome-LLMs-meet-Multimodal-Generation.zip` | Not extracted | `Awesome-LLMs-meet-Multimodal-Generation-main/README.md` | Yes | High | Medium | Survey of LLMs for multimodal generation and editing. Useful for image/video/audio prompting and eval study. |
| `Azure-Samples-visionary-lab.zip` | BROKEN | unknown | Unknown | Unknown | Unknown | Unreadable by the ZIP reader. Needs repair or extraction outside the script path. |
| `aws-samples-amazon-bedrock-samples.zip` | BROKEN | unknown | Unknown | Unknown | Unknown | Unreadable by the ZIP reader. Needs repair or extraction outside the script path. |
| `aws-samples-generative-ai-use-cases.zip` | BROKEN | unknown | Unknown | Unknown | Unknown | Unreadable by the ZIP reader. Needs repair or extraction outside the script path. |
| `aws-samples-sample-building-intelligent-multimodal-applications-with-Nova.zip` | BROKEN | unknown | Unknown | Unknown | Unknown | Unreadable by the ZIP reader. Needs repair or extraction outside the script path. |
| `GoogleCloudPlatform-generative-ai.zip` | BROKEN | unknown | Unknown | Unknown | Unknown | Unreadable by the ZIP reader. Needs repair or extraction outside the script path. |

## Key Findings

- Highest usefulness for this workbench:
  - `rsmdt-multimodal-mcp` as real MCP integration.
  - `Prompt-Engineering-Guide` and `promptslab-Awesome-Prompt-Engineering` as reference docs.
  - `page-agent-main` and `chromex-main` as browser-grounded agent examples.
  - `stop-slop-main` as prompt-output quality rule set.
- Weak or leak-derived items to avoid in public repo text:
  - `claw-code-main` uses leaked-source framing and unsafe public brand copy.
  - `claude-mem-9.0.12` is narrow capability and begins with crypto/promotion framing.
- Make-or-break for full coverage:
  - Repair or replace the nine broken ZIPs.
  - Inspect `CL4R1T4S-main`, `gjtjx-awesome-structued-prompts`, `git-time-explorer-main`, `nidhinjs-prompt-master`, `promptslab-Awesome-Prompt-Engineering`, `rsmdt-multimodal-mcp`, `stop-slop-main`, `superpowers-main`, `JindongGu-Awesome-Prompting-on-Vision-Language-Model`, and `YingqingHe-Awesome-LLMs-meet-Multimodal-Generation` in depth.
