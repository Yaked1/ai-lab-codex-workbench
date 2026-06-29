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
