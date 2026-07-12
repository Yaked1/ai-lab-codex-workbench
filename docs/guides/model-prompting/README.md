# Model and Effort Prompting Guides

Checked: 2026-07-12

This folder turns the dated frontier-model inventory into **actionable
prompting guides**. Each guide answers: which surface to use, which effort to
pick, what the prompt must contain, copy-ready templates, failure modes, and
how to prove the run worked.

Primary source for model facts, plan access, and product controls:

- [Frontier models and multimodal systems in 2026](../frontier-models-and-multimodal-systems-2026.md)
- [Current models, interfaces, and effort controls](../current-models-and-interfaces.md)

Product menus change by plan, region, app version, and rollout. Treat effort
labels in this pack as dated operational guidance, not a permanent product
catalog. Verify live pickers before writing public claims.

## Start Here

| If you need… | Open |
| --- | --- |
| Effort menus across Chat, Work, Desktop, Codex, API, Claude, Grok | [Surface and effort map](surface-and-effort-map.md) |
| Test whether a higher effort is worth it | [Effort evaluation playbook](effort-evaluation-playbook.md) |
| Audit which claims are official vs observed | [Sources and interface observations](sources-and-observations.md) |
| Flagship GPT-5.6 coding and synthesis | [GPT-5.6 Sol](gpt-5-6-sol-prompting.md) |
| Balanced GPT-5.6 daily driver | [GPT-5.6 Terra](gpt-5-6-terra-prompting.md) |
| Fast/cheap GPT-5.6 volume work | [GPT-5.6 Luna](gpt-5-6-luna-prompting.md) |
| Claude long-horizon / Mythos-class work | [Claude Fable 5](claude-fable-5-prompting.md) |
| Claude baseline without Fable fallback | [Claude Opus 4.8](claude-opus-4-8-prompting.md) |
| Claude agentic work at a lower dated API price | [Claude Sonnet 5](claude-sonnet-5-prompting.md) |
| Cost-efficient coding in Grok Build | [Grok 4.5](grok-4-5-prompting.md) |
| DeepSeek preview coding and structured API work | [DeepSeek V4](deepseek-v4-prompting.md) |
| GLM open-source long-horizon coding | [GLM-5.2](glm-5-2-prompting.md) |
| Mistral generalist, OCR, TTS, Lean, and robotics workload selection | [Current Mistral models](mistral-current-models-prompting.md) |
| Meta multimodal reasoning | [Muse Spark 1.1](muse-spark-1-1-prompting.md) |
| Google agentic Flash coding | [Gemini 3.5 Flash](gemini-3-5-flash-prompting.md) |
| Google open weights, video, music, and robotics | [Google open, media, and robotics](google-open-media-robotics-prompting.md) |
| Full-duplex voice | [GPT-Live-1](gpt-live-1-prompting.md) |
| Speech translation only | [Gemini Live Translate](gemini-live-translate-prompting.md) |
| Image generation / editing | [GPT Image 2](gpt-image-2-prompting.md), [Nano Banana family](nano-banana-family-prompting.md), [Seedream 5.0 Pro](seedream-5-0-pro-prompting.md), [Muse Image / Video](muse-image-video-prompting.md) |
| Multimodal video | [Gemini Omni Flash](gemini-omni-flash-prompting.md) |

## Universal Prompt Kernel

Every model in this pack still needs the same work-order kernel. Effort only
changes how much compute and tool budget the model gets; it does not invent a
missing goal or acceptance test.

```text
Goal:          one observable deliverable
Context:       files, sources, prior failures, environment
Scope:         include / exclude / do-not-touch
Constraints:   safety, style, deps, latency, cost
Method:        inspect -> plan if needed -> act -> verify
Format:        schema, length, report shape
Verification:  commands, tests, citations, screenshots
Failure:       stop conditions, escalate, or report-only
```

## Effort Escalation Rule

Escalate effort only when a lower run fails a real check, not when the task
feels important.

```text
low/light  -> medium -> high -> xhigh/extra -> max -> ultra/ultracode
```

Stop escalating when:

1. acceptance tests pass;
2. extra reasoning is repeating the same analysis;
3. the bottleneck is missing data, not model depth;
4. the work is sequential and cannot use parallel agents.

## Evidence Labels

| Label | Meaning |
| --- | --- |
| Official | Vendor launch post, help article, API page, or product catalog |
| Independent | Benchmark maintainer with published method |
| Local evidence | Checked against installed Codex catalog / dated interface observation |
| Interpretation | Recommendation derived from facts, not a guaranteed product property |
| Unconfirmed | Public sources did not establish the claim |

## Related Repository Paths

- Coding-agent craft: [../prompting-ai-coding-agents.md](../prompting-ai-coding-agents.md)
- Prompt audit: [../prompt-audit-checklist.md](../prompt-audit-checklist.md)
- Image patterns: [../../image-generation/prompting-patterns.md](../../image-generation/prompting-patterns.md)
- Live audio overview: [../live-audio-and-translation.md](../live-audio-and-translation.md)
- Model routing notes: [../../model-routing.md](../../model-routing.md)
- Evidence ledger: [sources-and-observations.md](sources-and-observations.md)
- Effort evaluation: [effort-evaluation-playbook.md](effort-evaluation-playbook.md)

## Maintenance

When a model menu or effort set changes:

1. Update [surface-and-effort-map.md](surface-and-effort-map.md) first.
2. Update the affected model guide's effort tables and templates.
3. Bump the `Checked:` date.
4. Keep architecture, pricing, and access claims labeled by evidence type.
5. Run `python -m unittest tests.test_model_prompting_guides` and the repo health check.

## Expanded Reading and Evaluation Standard

Each model page now includes an **Expanded Operating Dossier**. Read it after
the model-specific prompt template when a task has meaningful cost, autonomy,
multimodal, long-context, or safety consequences. The dossier keeps the same
evidence discipline as the main guide: product facts come from documented
surfaces, local menu observations are not universal, and recommendations remain
interpretation until tested against the reader's own work.

Use the same minimum run record across pages: model identifier, surface, effort
or thinking setting, prompt revision, context and sources, tools and permissions,
output limit, retries, latency, cost, validation output, and human correction.
This makes a comparison between two models or two efforts reviewable rather than
a collection of remembered impressions.

Do not force unrelated specialist systems into one score. OCR needs extraction
ground truth and correction metrics; TTS needs intelligibility, latency, consent,
and rights review; formal proofs need compiler acceptance; media needs original
output inspection; robotics needs simulation, independent safety controls, and
supervised transfer tests. A general chat benchmark cannot substitute for these
task-specific gates.

## Precision Standard for Every Run

Do not record a run as only `GPT-5.6 Sol High` or `Claude Fable 5 Max`.
Capability comes from the complete execution tuple:

```text
model + dated release state + plan + surface + harness version
+ effort/thinking + context + tools + permissions + prompt revision
+ output limit + validator + retry policy
```

Two runs using the same model can behave differently when one has repository
tools and the other is ordinary chat, one can launch agents and the other
cannot, or one workspace administrator has disabled an app. Every guide now
uses this minimum preflight record:

```text
Model ID:                    [exact picker name and API ID, if published]
Release / availability:     [stable | preview | promotion | announced]
Plan:                        [Free | Plus | Pro | Business | Enterprise | API]
Surface:                     [Chat | Work | Desktop Work | Desktop Codex | CLI | API]
Harness / client version:    [product and version; "web rollout" if unversioned]
Effort / thinking:           [visible label and API/config value]
Tools enabled:               [exact tools, apps, plugins, MCP servers, or none]
Permission boundary:         [read/write/network/approval limits]
Unknown or unverified:       [picker, price, architecture, quota, or none]
Evidence class:              [Official | Local evidence | Independent | Interpretation]
```

The production prompt then specifies objective, context, constraints, output
contract, verification, stop conditions, and retry or escalation. If any field
would change the permitted actions or billing path and is unknown, stop at
preflight and resolve it before execution.

## Task-First Routing

| Workload | Start with | Move up when | Do not substitute |
| --- | --- | --- | --- |
| Fast classification, extraction, or bounded transforms | Luna, Gemini Flash low/medium, or a documented specialist | Schema or factual checks fail after one prompt repair | Higher effort for missing inputs |
| Normal coding, document work, or multi-step analysis | Terra Medium, Sonnet, Grok Medium, Gemini Flash medium | Regression tests, traceability, or acceptance rubric fail | A benchmark headline for a local task eval |
| Hard debugging, architecture, synthesis, or final review | Sol High/Extra High, Fable High/xhigh, Opus high/xhigh | A frozen lower-effort run misses a reasoning-sensitive gate | Ultra when work cannot be split |
| Parallel repository or research streams | Sol/Terra Ultra or Claude Ultracode | Streams are independent with frozen interfaces | Ultra as a synonym for deeper single-agent thinking |
| Live conversation | GPT-Live-1 or Mini by plan and latency target | Background reasoning or tool delegation is required | Text-model effort labels for audio turn taking |
| Translation-only audio | Gemini Live Translate | The task is strictly speech translation | General assistant instructions or tool calls |
| Image or video production | Exact media model named in its guide | Reference fidelity, edit precision, or resolution gate fails | Text benchmark rankings |
| Formal proof, OCR, TTS, robotics | Exact specialist system | Domain validator requires a different system | Generalist prose quality as proof |

## Prompt and Evaluation Minimum

Every production template has five required blocks: objective, context,
constraints, output contract, and verification. Every serious run also has a
weighted rubric, auto-fail conditions, and a failure protocol. An attractive
answer receives no credit if it violates scope, uses an unapproved tool,
misstates the active model, fabricates a source, or skips a mandatory check.

Use no more than two prompt-repair passes before changing the model or effort.
Pass one repairs missing constraints or output shape. Pass two adds only the
evidence needed to repair the observed failure. After that, report the blocker
or run a declared routing experiment. Silent fallback is never acceptable.
