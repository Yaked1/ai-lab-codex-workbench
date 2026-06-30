# Archived GitHub Downloads Catalog

Source archive: local ZIP archive folder inspected during repository curation.
The machine-specific path is intentionally not published.

This catalog summarizes each archive’s usefulness and learnings, with extraction or access results.

- Verified extraction or direct archive read.
- Extraction failure or tool access issue with extracted folder.
- No meaningful public documentation uncovered.

## Catalog

| Archive | Status | Usefulness | Notable Learning |
|---|---|---|---|
| `agent-coworker-main.zip` | Extracted | High | Local-first, provider-agnostic agent with decoupled UI/agent over WebSockets, desktop/TUI/CLI/web clients, skills/plugins, and sub-agents. Good architecture example for interface-independent tool use. |
| `aws-samples-amazon-bedrock-samples.zip` | Unreadable archive | Tool failure | Extraction or read failed with the ZIP parser access issue. Treat extraction status as unverified until repaired outside the failing tool path. |
| `aws-samples-generative-ai-use-cases.zip` | Unreadable archive | Tool failure | Extraction or read failed with the ZIP parser access issue. Treat extraction status as unverified until repaired outside the failing tool path. |
| `aws-samples-sample-building-intelligent-multimodal-applications-with-Nova.zip` | Unreadable archive | Tool failure | Extraction or read failed with the ZIP parser access issue. Treat extraction status as unverified until repaired outside the failing tool path. |
| `Azure-Samples-visionary-lab.zip` | Unreadable archive | Tool failure | Extraction or read failed with the ZIP parser access issue. Treat extraction status as unverified until repaired outside the failing tool path. |
| `chromex-main.zip` | Extracted | High | Browser-to-agent bridge example with Chrome-side panel integration and native host messaging. Useful for learning extension/agent boundaries and credential handling. |
| `CL4R1T4S-main.zip` | Extracted folder | Pending verdict | Folder exists but README read was not successful here. Manual follow-up needed. |
| `claude-mem-9.0.12.zip` | Extracted | Low | Memory/persistence layer for Claude Code with translations and hooks. Narrow payoff for this public guide. |
| `claw-code-main.zip` | Extracted | Low | Readme and tree reflect a leaked/fan-port narrative around Claude Code. Avoid as a teaching source. Useful only as a caution example. |
| `git-time-explorer-main.zip` | Extracted folder | Medium | Folder exists but README read was not successful here. Likely useful for Windows git browsing workflows. |
| `gjtjx-awesome-structued-prompts.zip` | Extracted folder | Medium-High | Folder exists but README read was not successful here. Appears to be a ChatGPT/Claude multimodal prompt cookbook fit for prompt-design review. |
| `GoogleCloudPlatform-generative-ai.zip` | Unreadable archive | Tool failure | Extraction read failed with the ZIP parser access issue. Treat extraction status as unverified until repaired outside the failing tool path. |
| `JindongGu-Awesome-Prompting-on-Vision-Language-Model.zip` | Verified read from archive | High | VLM prompting survey and paper list covering Flamingo, CLIP, BLIP-2, Stable Diffusion, multimodal agents, prompt types, and chain-of-thought/reasoning patterns. Strong reference for vision-language prompting documentation. |
| `langgptai-Awesome-Multimodal-Prompts.zip` | Unreadable archive | Tool failure | Extraction read failed with the ZIP parser access issue. Treat extraction status as unverified until repaired outside the failing tool path. |
| `microsoft-Build25-LAB324.zip` | Unreadable archive | Tool failure | Extraction read failed with the ZIP parser access issue. Treat extraction status as unverified until repaired outside the failing tool path. |
| `microsoft-generative-ai-for-beginners.zip` | Unreadable archive | Tool failure | Extraction read failed with the ZIP parser access issue. Treat extraction status as unverified until repaired outside the failing tool path. |
| `nidhinjs-prompt-master.zip` | Extracted folder | High | Folder exists but README read was not successful here. README preview indicates a prompt-writing skill with target tool, success criteria, safety boundaries, verification steps, final report format, and failure cases. Fits the repo’s prompt template rules. |
| `openai-openai-cookbook.zip` | Unreadable archive | Tool failure | Extraction read failed with the ZIP parser access issue. Treat extraction status as unverified until repaired outside the failing tool path. |
| `page-agent-main.zip` | Extracted | High | In-page agent with plain-text DOM manipulation, optional multi-page Chrome extension, and BYO LLM design. Good example for SaaS copilot and accessibility applications. |
| `Prompt-Engineering-Guide-main.zip` | Verified read from archive | High | Comprehensive prompt engineering guide with basics, techniques, RAG, autonomous agents, multimodal prompting, prompt injection, benchmark/tooling, and coursework. Useful for beginner-to-advanced curriculum links and safe-claim framing. |
| `promptslab-Awesome-Prompt-Engineering.zip` | Verified read from archive | High | Curated papers, tools, models, benchmarks, courses, and provider docs for prompt and context engineering. Useful for links sections and independent source references. |
| `rsmdt-multimodal-mcp.zip` | Verified read from archive | High | Single MCP interface for image, video, audio, transcription, and provider auto-discovery across OpenAI, xAI, Gemini, ElevenLabs, and BFL. Useful as a real tool-use example and prompt-review case. |
| `stop-slop-main.zip` | Verified read from archive | Medium-High | Audit skill for AI prose tells with banned phrases, structural clichés, scoring, and before/after examples. Directly supports prompt-output review and anti-slop editing. |
| `superpowers-main.zip` | Extracted | Medium | Spec-first planning, TDD, subagent execution, editor support. Good reference when the repo documents workflow quality and review boundaries. |
| `YingqingHe-Awesome-LLMs-meet-Multimodal-Generation.zip` | Verified read from archive | High | Survey of generation and editing across image, video, 3D, audio, and multimodal understanding. Useful prompt reference for generation and multimodal editing. |

## Usability Summary

Priority usability clusters from the archive:

- Prompt mastery: `Prompt-Engineering-Guide`, `promptslab-Awesome-Prompt-Engineering`, `nidhinjs-prompt-master`, `stop-slop-main`
- Multimodal prompting and generation: `JindongGu-Awesome-Prompting-on-Vision-Language-Model`, `YingqingHe-Awesome-LLMs-meet-Multimodal-Generation`
- Live agent/tool integration: `page-agent-main`, `chromex-main`, `agent-coworker-main`, `rsmdt-multimodal-mcp`
- Windows and workflow support: `git-time-explorer-main`
- Avoid in public docs: `claw-code-main`

## Repair Notes

Nine archives were not readable in this audit tool despite being stored in the archive folder. Recover those files before relying on `CL4R1T4S-main`, `gjtjx-awesome-structued-prompts`, `git-time-explorer-main`, and `nidhinjs-prompt-master`, and repair the unreadable tool-failure archives before using them in guidance.
