# Prompting OS

Prompting OS is a consolidated operating system for prompting almost any model family: chat models, reasoning models, coding agents, Claude Code, Codex, tool-using agents, RAG systems, structured-output systems, diffusion image models, autoregressive image models, multimodal models, and small/local models.

It is built from the patterns that strong prompting repositories share: clear task contracts, reusable prompt assets, examples, source discipline, context engineering, evaluation, repair loops, tool boundaries, and release-quality documentation.

It is not a prompt dump. Prompt dumps are mostly archaeology with better Markdown.

## Choose a Track

| Track | Time | Artifact | Observable check |
| --- | ---: | --- | --- |
| First working prompt | 15 minutes | One reviewed report | `python examples/first-reviewed-agent-task/check_report.py` prints `PASS` |
| Reliable agent task | About one hour | A scoped work order plus verified result | Relevant tests or rubric pass and the final diff/report is reviewed |
| Maintainer reference | As needed | Repository policy, evaluation, or release evidence | Full repository gates and owner-side evidence where required |

Start with [00-first-success.md](00-first-success.md). Continue with
[01-kernel.md](01-kernel.md), [03-context-engineering.md](03-context-engineering.md),
[06-evaluation-and-optimization.md](06-evaluation-and-optimization.md), and
[28-tool-permission-model.md](28-tool-permission-model.md) for the one-hour
track. The remaining modules are a reference library, not a mandatory beginner
procession.

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
10. Read `11-comprehensiveness-benchmark.md` before expanding the repository or focused ZIP for behavior and evidence coverage.
11. Read `12-prompt-pattern-library.md` for reusable prompt patterns.
12. Read `13-agent-operations-manual.md` before running long agent tasks.
13. Read `14-rag-and-tool-use-field-guide.md` before combining sources and tools.
14. Read `15-maintenance-and-release-manual.md` before release work.
15. Read `24-archive-corpus-source-map.md` when source-inspired expansion is in scope.
16. Read `28-tool-permission-model.md` before giving an agent tools, browsers, files, or package commands.
17. Read `32-completion-evidence-manual.md` before claiming a broad task is done.
18. Use `templates/` and `evals/` for practical reuse.

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
| `11-comprehensiveness-benchmark.md` | Public-safe behavior, evidence, and package-parity guidance. |
| `12-prompt-pattern-library.md` | Reusable task, source, agent, structured-output, visual, compression, and evaluation prompt patterns. |
| `13-agent-operations-manual.md` | Operational runbook for coding agents and tool-using agents, including dirty worktrees, staging, tool discipline, and package work. |
| `14-rag-and-tool-use-field-guide.md` | Source ledgers, RAG contracts, tool permission ladders, tool audits, and injection cases. |
| `15-maintenance-and-release-manual.md` | Prompt package versioning, release checks, changelog discipline, package manifests, and deprecation. |
| `16-comprehensive-examples.md` | Worked examples for docs updates, RAG answers, package expansion, bug fixes, prompt assets, image revisions, and evaluations. |
| `17-curriculum-and-workshops.md` | Workshop path, exercises, assessment rubric, instructor notes, and self-study plan. |
| `18-troubleshooting-and-debugging.md` | Failure classification, minimal reproductions, RAG/image/package debugging, and regression repair. |
| `19-model-specific-adaptation.md` | Adapting prompts across chat, reasoning, coding-agent, RAG, structured-output, image, and small/local model families. |
| `20-prompt-library-governance.md` | Prompt asset metadata, source status labels, review roles, package inclusion, metrics, and deprecation. |
| `21-checklists-and-templates.md` | Reusable checklists and templates for prompts, agents, sources, packages, releases, incidents, and README expansion. |
| `22-risk-register.md` | Prompting and agent risk table, scoring, controls, incident response, and closure criteria. |
| `23-quality-assurance-matrix.md` | QA levels, artifact-specific gates, evidence requirements, and completion checks. |
| `24-archive-corpus-source-map.md` | Sanitized source-corpus inventory, readable/unreadable archive handling, structural-use rules, and public-safe source labels. |
| `25-repository-expansion-playbook.md` | File audit tiers, batch planning, expansion patterns, evidence levels, and public-safety review for broad repository work. |
| `26-offline-package-reader-guide.md` | Role-based reading paths, offline package integrity checks, teaching routes, and package review without repository history. |
| `27-prompt-evaluation-datasets.md` | Dataset design for prompt templates, coding agents, RAG, structured output, image prompts, and package behavior. |
| `28-tool-permission-model.md` | Permission layers, command risk ladder, tool trust boundaries, RAG/browser/file permissions, and staging rules. |
| `29-source-grounded-writing-lab.md` | Source ledgers, claim classification, structural inspiration workflow, missing-evidence handling, and writing exercises. |
| `30-agent-review-and-red-team.md` | Diff review, prompt review, package review, RAG red-team cases, severity guidance, and adversarial review templates. |
| `31-workbench-maintainer-runbook.md` | Recurring maintainer operations for docs, prompts, packages, source policy, releases, triage, and evidence logs. |
| `32-completion-evidence-manual.md` | Requirement extraction, evidence states, package metrics, prompt-template evidence, and final report gates. |
| `33-prompt-library-indexing.md` | Prompt metadata, task-family taxonomy, risk labels, package inclusion, deprecation, and index maintenance. |
| `34-static-site-and-release-docs.md` | Offline-safe static site rules, release documentation structure, manifest review, and static-site/package linkage. |
| `35-workshop-assessment-bank.md` | Exercises and scoring rubrics for prompt contracts, source ledgers, permissions, RAG defense, package review, and public safety. |
| `36-prompt-metrics-and-telemetry.md` | Privacy-preserving metrics for prompt templates, agent tasks, RAG, packages, and final reports. |
| `37-failure-mode-catalog.md` | Prompt, coding-agent, source, package, documentation, tool-use, and review failure modes with repairs. |
| `templates/master-prompt-template.md` | A reusable master template with metadata, permissions, coding-agent, RAG, structured-output, and image variants. |
| `evals/prompt-quality-rubric.md` | A detailed scoring rubric and package gate for reusable prompt assets. |

## Review Routes

Use these routes when the package is opened for a specific job.

| Job | Read first | Then verify |
| --- | --- | --- |
| Expand the repository from a broad instruction file | `25-repository-expansion-playbook.md`, `24-archive-corpus-source-map.md`, `32-completion-evidence-manual.md` | Named reader paths, source map, examples, failure cases, tests, changelog. |
| Build or review the focused package | `15-maintenance-and-release-manual.md`, `26-offline-package-reader-guide.md`, `34-static-site-and-release-docs.md` | Required artifacts, source commit, ZIP/manifest path parity, SHA-256. |
| Write or audit prompt templates | `12-prompt-pattern-library.md`, `27-prompt-evaluation-datasets.md`, `33-prompt-library-indexing.md` | Required sections, examples, risk level, package inclusion, failure cases. |
| Run a coding-agent task | `13-agent-operations-manual.md`, `28-tool-permission-model.md`, `30-agent-review-and-red-team.md` | Worktree status, scoped files, commands, checks, public-safety scan. |
| Create source-grounded guidance | `03-context-engineering.md`, `14-rag-and-tool-use-field-guide.md`, `29-source-grounded-writing-lab.md` | Source ledger, source status, official-doc boundaries, unsupported claims. |
| Teach a workshop | `17-curriculum-and-workshops.md`, `26-offline-package-reader-guide.md`, `35-workshop-assessment-bank.md` | Exercises, scoring rubrics, package snapshot, no private examples. |

## Package Quality Contract

- Named core artifacts: kernel, production, security, evaluation, examples,
  troubleshooting, source map, master template, and rubric.
- Worked example: a filled prompt contract with observable checks.
- Failure case: expected rejection or recovery behavior.
- Verification command: `python -m unittest tests.test_prompting_os_package`.
- Source, manifest, and archive parity: identical paths from one `source_commit`,
  with relative names and per-file hashes.

## Public-Safe Source Use

The expanded package uses local archive inspection as a structural benchmark.
Public files should name archive sources only in sanitized form and should not
include local machine paths. Direct source text is not required for the package
to be useful. The safe workflow is:

1. Inspect source names, headings, file counts, package structure, tests,
   release notes, and safety boundaries.
2. Label source status: official, public community, local-readable,
   local-unreadable, structural-only, leak-derived, private, or unverified.
3. Write original guidance for this repository.
4. Avoid copying hidden prompts, private data, screenshots, local paths, or
   license-unclear prose.
5. Mark current product behavior, model availability, pricing, and platform
   support as items to verify in official docs.
6. Run public-safety scans before release.

When an archive cannot be inspected with standard tools, list it as skipped or
structural-only. Do not infer content from the file name.

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

Repository tests check the named artifacts, worked and failure examples,
verification path, source identity, and commit-exact package parity above.

## Inspired By

This synthesis is inspired by public projects and docs such as DAIR.AI Prompt Engineering Guide, OpenAI Cookbook, promptfoo, Microsoft beginner/workshop materials, Anthropic and other official vendor prompting docs, Prompt Master-style template libraries, Stop Slop-style anti-slop guides, structured prompt collections, vision-language prompting surveys, multimodal generation surveys, MCP/agent bridge projects, and public-safe structural inspection of local archive copies.

The safe rule: extract structures and concepts, not bulk text. Keep local archive paths out of public docs, and verify fast-changing tool behavior in official docs before publishing exact claims.
