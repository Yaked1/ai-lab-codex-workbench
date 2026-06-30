# Prompting References

A curated, public-safe list of the prompting resources this workbench draws on.
Use them as inspiration and as the authority for fast-changing details. Read the
originals; this page summarizes what each is good for and links to it. It does
not copy their content.

How to read this list:

- **Official docs first.** When a vendor documents prompting for their own tool,
  that is the most reliable source for that tool.
- **Community guides for breadth.** Independent guides aggregate techniques
  across models and stay useful when you switch tools.
- **Evaluation tools for rigor.** A prompt you reuse is software; measure it.
- **Leak-derived collections: structural patterns only.** See the safety note at
  the end. Per this repo's [source policy](../research/source-policy.md), these
  may be referenced for structure and linked, never mirrored or republished.

## GitHub Research Snapshot

These public repositories were checked on 2026-06-30 and used as inspiration for
this workbench's structure. The point is not to copy their text. The point is to
learn the durable shapes that make prompting repositories useful.

| GitHub source | Durable pattern to study | How this repo applies it |
| --- | --- | --- |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Broad technique map covering basics, techniques, applications, RAG, agents, risks, papers, tools, notebooks, and datasets. | Keep the comprehensive guide organized as a curriculum instead of a loose prompt list. |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | Recipe-style examples, runnable code, clear environment assumptions, and source-linked documentation. | Pair prompts with validation commands, expected evidence, and honest setup notes. |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Lesson order, exercises, troubleshooting, and practice areas. | Give beginners a reading path, worked examples, failure modes, and self-check questions. |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Lesson catalog, build/learn distinction, checkpoints, translations, and classroom-friendly sequencing. | Keep README navigation role-based and split theory, practice, and maintenance docs. |
| [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | Large public prompt library, categorization, contribution flow, multiple data formats, and explicit licensing notes. | Treat reusable prompts as assets with metadata, inputs, safety boundaries, and review gates. |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | Community collection of instructions, agents, skills, hooks, workflows, and plugins. | Keep coding-agent guidance modular: instructions, skills, prompt templates, workflows, and tool boundaries. |
| [brexhq/prompt-engineering](https://github.com/brexhq/prompt-engineering) | Production framing, prompt limits, jailbreak/leak warnings, and operational safety. | Repeat the public-safety rule: never put secrets, private data, or hidden assumptions into prompts. |
| [trigaten/Learn_Prompting](https://github.com/trigaten/Learn_Prompting) | Education-first guide, glossary/citation habits, research references, and community contribution model. | Keep source references explicit and make beginner docs teach vocabulary before advanced tactics. |
| [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) | Hands-on technique catalog with tutorials, optimization, ambiguity handling, security, and evaluation. | Add prompt improvement loops and test cases before treating a prompt as reusable. |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Prompt, agent, and RAG evaluation; red-team checks; command-line and CI-style verification. | Use lightweight local rubrics by default and point advanced users toward formal eval tools when needed. |

Use this snapshot as a maintenance checklist. When adding a prompting guide,
ask which source pattern it follows: technique map, lesson, recipe, prompt
asset, agent instruction, safety warning, evaluation, or source map.

## Official Vendor Guides

| Resource | What to learn from it | Link |
| --- | --- | --- |
| Anthropic prompt engineering docs | Structured prompting, system prompts, XML tags, role and chain-of-thought patterns for Claude. | <https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview> |
| Anthropic interactive tutorial (`anthropics/prompt-eng-interactive-tutorial`) | Hands-on, lesson-by-lesson prompt design from basics to advanced. | <https://github.com/anthropics/prompt-eng-interactive-tutorial> |
| Anthropic prompt library | Concrete, categorized example prompts to adapt. | <https://docs.anthropic.com/en/resources/prompt-library/library> |
| Claude Code best practices | Agentic coding workflow, memory files, plan-first, subagents, MCP. | <https://www.anthropic.com/engineering/claude-code-best-practices> |
| OpenAI prompt engineering guide | Practice-oriented prompt design for reliable, controllable output. | <https://platform.openai.com/docs/guides/prompt-engineering> |
| OpenAI Cookbook (`openai/openai-cookbook`) | Worked examples and recipes, including tool use and structured output. | <https://github.com/openai/openai-cookbook> |
| Codex best practices and `AGENTS.md` | Durable agent instructions, approval modes, verify loops. | <https://developers.openai.com/codex/learn/best-practices> |
| Google prompting guidance | Vendor-side patterns for Gemini-family models. | <https://ai.google.dev/gemini-api/docs/prompting-intro> |

## Community Guides And Collections

| Resource | What to learn from it | Link |
| --- | --- | --- |
| dair-ai Prompt Engineering Guide | Comprehensive, model-agnostic, academically grounded; covers prompting, context engineering, RAG, and agents; updated frequently. | <https://github.com/dair-ai/Prompt-Engineering-Guide> |
| promptslab Awesome Prompt Engineering | Hand-curated index of papers, tools, and resources. | <https://github.com/promptslab/Awesome-Prompt-Engineering> |
| Prompt Master-style template libraries | Load-bearing prompts, task-specific templates, anti-patterns, and tool-specific adaptation. | Verify the active upstream repository before citing exact behavior. |
| Stop Slop-style anti-slop guides | Removing filler, generic confidence, and unsupported claims from AI-written content. | Verify the active upstream repository before citing exact behavior. |
| Structured prompt collections | Reusable role/task/schema organization patterns. | Treat as structure only; do not mirror prompt dumps. |
| Vision-language and multimodal prompting surveys | Differences between text, image, video, audio, and multimodal prompting. | Prefer source links and original summaries, not copied tables. |
| Awesome ChatGPT Prompts | A large set of role/persona prompt starters to study for framing patterns. | <https://github.com/f/awesome-chatgpt-prompts> |

## Evaluation And Quality Tools

| Resource | What to learn from it | Link |
| --- | --- | --- |
| promptfoo | Declarative prompt and agent testing: assertions, comparisons, regression checks. | <https://www.promptfoo.dev/docs/intro/> |

Use an evaluation tool when a prompt becomes part of a workflow. Keep a few known
inputs and expected behaviors and re-check them whenever you change the prompt.

## How This Repo Uses These Sources

This workbench turns the techniques above into a safe, reviewable workflow rather
than re-teaching them from scratch:

- The craft is distilled in [Prompting AI coding agents](prompting-ai-coding-agents.md).
- The tool-specific tricks are in [Coding agent power tips](coding-agent-power-tips.md).
- The safe work-order skeleton is in [Prompt engineering playbook](prompt-engineering-playbook.md).
- The source-to-repository synthesis path is in [Source-inspired prompting curriculum](source-inspired-prompting-curriculum.md).
- The review pass before sending is the [Prompt audit checklist](prompt-audit-checklist.md).

When a detail could be stale (a flag, a default, a feature name, pricing, model
availability), this repo links to the official source instead of asserting it.

## Safety Note On Leak-Derived Prompt Collections

Some popular repositories collect leaked or reverse-engineered system prompts
from commercial products. They can be educational for **structure** (how large
systems frame roles, tools, and guardrails), but they carry real risks: license
and copyright problems, stale or fabricated content, and unsafe instructions.

This repository's policy, defined in
[docs/research/source-policy.md](../research/source-policy.md) and
[docs/publication-policy.md](../publication-policy.md):

- Reference such collections for **structural patterns and public-safe summaries
  only**, with attribution and links.
- **Do not** mirror, vendor, or republish leaked prompts verbatim.
- **Do not** treat leaked content as authoritative; prefer official docs.
- Block sources that look like secret dumps, credential leaks, or exfiltration
  kits entirely.

In short: learn the shape, link the source, never copy the contents.
