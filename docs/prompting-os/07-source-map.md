# Source Map and Synthesis

Prompting OS consolidates shared patterns from public prompting projects and the uploaded playbook ZIPs. It uses them as inspiration, not as copied text.

## Public Source Patterns

| Source | Common pattern extracted |
| --- | --- |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Technique taxonomy, RAG/agents coverage, image prompting categories, broad learning path. |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | Practical recipes, code-adjacent examples, evaluation mindset, runnable workflows. |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Test cases, prompt comparisons, regression checks, adversarial evaluations. |
| Microsoft Prompty | Prompt assets with metadata, inputs, model settings, and portability. |
| Instructor | Schema-first structured outputs and validation-driven prompting. |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Clear instructions, examples, step-by-step learning, hallucination reduction. |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Lesson sequencing, beginner checkpoints, projects, and workshop-style progression. |
| [brexhq/prompt-engineering](https://github.com/brexhq/prompt-engineering) | Production discipline, constraints, safety, decomposition, and operational clarity. |
| Guidance | Programmatic prompting and constrained generation. |
| DSPy | Language-model programs, signatures, metrics, and optimization. |
| [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | Role/task variety and prompt library organization. |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | Modular instructions, agents, skills, hooks, workflows, and plugins for coding agents. |
| [trigaten/Learn_Prompting](https://github.com/trigaten/Learn_Prompting) | Education-first glossary, citations, and learning-path structure. |
| [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) | Hands-on technique tutorials, ambiguity handling, security, and evaluation examples. |

## Current GitHub Scan Rules

The 2026-06-30 GitHub scan looked for repositories with at least one of these
durable assets:

- A start-here path for beginners.
- A technique taxonomy or lesson sequence.
- Concrete prompt examples with inputs and expected behavior.
- Agent instructions, skills, or reusable workflow assets.
- Safety notes for secrets, prompt injection, leakage, and unsupported claims.
- Evaluation, regression, or red-team guidance.
- Clear source or license status.

Repos without these assets may still be useful, but they should stay in the
reference list instead of shaping the core docs.

Leak-derived repositories such as
[`asgeirtj/system_prompts_leaks`](https://github.com/asgeirtj/system_prompts_leaks)
may be used only as structural benchmarks: long standalone files, categorized
folders, source/status metadata, version history, and dense technical
organization. Do not copy, mirror, summarize in detail, or package leaked
prompt contents. The local behavior, evidence, and package-parity targets are in
`11-comprehensiveness-benchmark.md`.

## Uploaded ZIP Patterns

| ZIP family | Useful pattern |
| --- | --- |
| `Prompt-Engineering-Guide-main.zip` | Technique taxonomy, coding examples, RAG/agent categories, and broad learning path. |
| `openai-openai-cookbook.zip` and runnable cookbook-style repos | Practical recipes, tool use, structured output, and validation-by-execution mindset. |
| `microsoft-generative-ai-for-beginners.zip` and workshop repos | Beginner lesson sequencing, checkpoints, and classroom-friendly project progression. |
| `GoogleCloudPlatform-generative-ai.zip` and cloud sample repos | Cloud/multimodal examples that should remain optional and official-doc verified. |
| `nidhinjs-prompt-master.zip` | Load-bearing prompt design, anti-pattern detection, and tool-specific template adaptation. |
| `stop-slop-main.zip` | Anti-slop editorial pass: remove filler, unsupported claims, and generic AI voice. |
| `gjtjx-awesome-structued-prompts.zip` and structured prompt collections | Role/task/schema organization; structure only, no prompt-dump mirroring. |
| `promptslab-Awesome-Prompt-Engineering.zip` | Source map across papers, tools, courses, benchmarks, and communities. |
| `JindongGu-Awesome-Prompting-on-Vision-Language-Model.zip` | Vision-language prompting categories and multimodal task distinctions. |
| `YingqingHe-Awesome-LLMs-meet-Multimodal-Generation.zip` and multimodal generation surveys | Generation/editing/agent/safety categories across image, video, audio, and multimodal systems. |
| MCP and browser/agent bridge repos | Permission boundaries, diagnostics, tool-routing, and read/write trust separation. |

## What Prompting Repositories Have In Common

Strong prompting repositories usually contain:

- A clear start-here guide.
- A theory layer.
- A technique catalog.
- Copy-ready templates.
- Examples.
- Model-specific notes.
- Evaluation criteria.
- Failure modes.
- Source references.
- Maintenance/release notes.

Weak prompting repositories usually contain:

- Giant prompt lists with no tests.
- Roles without constraints.
- Unsupported claims.
- No source policy.
- No update path.
- No failure analysis.
- No distinction between chat, coding, RAG, tool, and image models.

## What Prompting OS Adds

Prompting OS improves the common pattern by adding:

- The OS metaphor: kernel, drivers, memory manager, permissions, package manager, test suite.
- Model-family drivers instead of one universal magic prompt.
- Context/RAG ledgers.
- Claude Code and Codex skill patterns.
- Image prompting split by diffusion, autoregressive, reasoning-integrated, and revision workflows.
- Evaluation and optimization loops.
- Safe synthesis rules for public sources.

## Safe Synthesis Rules

1. Extract concepts, not bulk text.
2. Prefer reusable schemas and workflows.
3. Do not mirror prompt dumps.
4. Do not copy leaked system prompts.
5. Mark fast-changing claims for verification.
6. Keep examples generic and public-safe.
7. Include failure modes and evaluation.
8. Maintain changelogs and version notes.

## Final Principle

Prompting is not a bag of tricks. It is interface design for unstable intelligence. Treat it like engineering, teaching, writing, testing, and risk management fused into one deeply inconvenient craft.
