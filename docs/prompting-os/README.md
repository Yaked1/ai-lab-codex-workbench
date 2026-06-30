# Prompting OS

Prompting OS is a consolidated operating system for prompting almost any model family: chat models, reasoning models, coding agents, Claude Code, Codex, tool-using agents, RAG systems, structured-output systems, diffusion image models, autoregressive image models, multimodal models, and small/local models.

It is built from the patterns that strong prompting repositories share: clear task contracts, reusable prompt assets, examples, source discipline, context engineering, evaluation, repair loops, tool boundaries, and release-quality documentation.

It is not a prompt dump. Prompt dumps are mostly archaeology with better Markdown.

## Operating System Metaphor

| OS part | Prompting equivalent | Purpose |
| --- | --- | --- |
| Kernel | Goal, context, constraints, format, verification, failure behavior | The invariant rules of a good prompt. |
| Drivers | Model-family adapters | Adjust prompting for text, reasoning, coding, image, RAG, and local models. |
| Memory manager | Context engineering | Decides what to load, summarize, cite, discard, or preserve. |
| Filesystem | Prompt assets and templates | Stores reusable prompts with names, inputs, outputs, and tests. |
| Permissions | Tool and data boundaries | Controls read/write actions, private data, and risky operations. |
| Scheduler | Task decomposition | Splits work into inspect, plan, draft, verify, revise, and report. |
| Package manager | Skills and playbooks | Reusable Claude Code skills, Codex instructions, and workflow modules. |
| Test suite | Prompt evaluation | Golden cases, edge cases, regression checks, rubrics, and red-team cases. |
| Shell | User prompt interface | Turns intent into executable prompt work orders. |

## Core Law

A prompt is a contract for cognition under constraints.

The model should know:

1. What result to produce.
2. What context is trusted.
3. What actions are allowed.
4. What actions are forbidden.
5. What output shape is required.
6. How success will be checked.
7. What to do when uncertain.

Everything else is decoration, sometimes useful, often noisy, frequently wearing sunglasses indoors.

## Start Here

Use this path:

1. Read `01-kernel.md` for universal prompting principles.
2. Read `02-model-family-drivers.md` for adapting prompts to model types.
3. Read `03-context-engineering.md` for RAG, memory, and context discipline.
4. Read `04-agent-skills.md` for Claude Code, Codex, tool-use, and MCP patterns.
5. Read `05-image-prompting-engine.md` for diffusion and autoregressive image systems.
6. Read `06-evaluation-and-optimization.md` before trusting any prompt.
7. Read `08-production-prompt-architecture.md` before turning prompts into repeatable workflows.
8. Read `09-security-and-governance.md` before adding tools, RAG, automation, or release packages.
9. Read `10-evaluation-cookbook.md` before changing packaged prompts.
10. Read `11-comprehensiveness-benchmark.md` before expanding the repository or focused ZIP for depth.
11. Use `templates/` and `evals/` for practical reuse.

## Technical Module Map

| File | Use it for |
| --- | --- |
| `01-kernel.md` | Universal prompt contract: goal, context, constraints, method, format, verification, and failure behavior. |
| `02-model-family-drivers.md` | Adapting the same task across chat, reasoning, coding-agent, RAG, structured-output, image, and small/local models. |
| `03-context-engineering.md` | Context ledgers, RAG source boundaries, retrieval quality, compression, and rolling summaries. |
| `04-agent-skills.md` | Agent work orders, Claude Code skill structure, Codex `AGENTS.md` patterns, MCP prompts, and permission boundaries. |
| `05-image-prompting-engine.md` | Diffusion, autoregressive, reasoning-integrated, and revision-oriented image prompting. |
| `06-evaluation-and-optimization.md` | Prompt rubrics, optimization loops, critic-builder loops, and failure taxonomies. |
| `07-source-map.md` | Public source patterns, safe synthesis rules, and the current GitHub scan criteria. |
| `08-production-prompt-architecture.md` | Prompt asset specifications, prompt interfaces, versioning, telemetry, migration, and production readiness. |
| `09-security-and-governance.md` | Data classification, prompt injection defense, tool permission profiles, RAG governance, leak-derived content policy, and incident response. |
| `10-evaluation-cookbook.md` | Golden, edge, abuse, regression, RAG, image, coding-agent, and package quality evaluation recipes. |
| `11-comprehensiveness-benchmark.md` | Public-safe structural benchmark from a local `system_prompts_leaks` clone, with package-depth targets and review procedure. |
| `templates/master-prompt-template.md` | A reusable master template with metadata, permissions, coding-agent, RAG, structured-output, and image variants. |
| `evals/prompt-quality-rubric.md` | A detailed scoring rubric and package gate for reusable prompt assets. |

## Package Build

A maintainer can build a self-contained Prompting OS ZIP and manifest with:

```powershell
python scripts/create_prompting_os_package.py --version v1
```

Expected local outputs:

```text
release/packages/prompting-os-v1.zip
release/packages/prompting-os-v1-manifest.json
```

The package builder uses fixed ZIP timestamps, records SHA-256 hashes, stores paths relative to the repository root, and excludes caches, private-looking files, archives, environment files, and oversized files. The output folder is gitignored for generated manifests and archives so generated release assets do not drift into normal commits.

Use a temporary output directory when validating package behavior without touching `release/packages/`:

```powershell
python scripts/create_prompting_os_package.py --version v1 --output-dir .\dist\prompting-os
```

The package is intended to be substantial. The repository tests check that the
focused ZIP source has multiple long technical Markdown files, a large enough
total Markdown footprint, a non-trivial master template, a non-trivial rubric,
and the production/security/evaluation/comprehensiveness modules listed above.

## Inspired By

This synthesis is inspired by public projects and docs such as DAIR.AI Prompt Engineering Guide, OpenAI Cookbook, promptfoo, Microsoft beginner/workshop materials, Anthropic and other official vendor prompting docs, Prompt Master-style template libraries, Stop Slop-style anti-slop guides, structured prompt collections, vision-language prompting surveys, multimodal generation surveys, and MCP/agent bridge projects.

The safe rule: extract structures and concepts, not bulk text. Keep local archive paths out of public docs, and verify fast-changing tool behavior in official docs before publishing exact claims.
