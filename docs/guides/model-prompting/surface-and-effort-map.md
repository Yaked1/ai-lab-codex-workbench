# Surface and Effort Map for 2026 Frontier Models

Checked: 2026-07-12

This map is the single place to look up **which product surface exposes which
model and effort labels**. Detailed prompt templates live in the per-model
guides linked below.

Source baseline:
[frontier-models-and-multimodal-systems-2026.md](../frontier-models-and-multimodal-systems-2026.md).
Account pickers can still differ by plan, region, workspace policy, client
version, and staged rollout.

## GPT-5.6 Family Surfaces

### Codex CLI (official minimum plus local catalog evidence)

OpenAI documents Codex CLI **0.144.0** as the minimum for GPT-5.6 access. The
installed executable checked for this guide is `codex-cli 0.144.0`. The npm
package page listed **0.144.1** as the latest stable release on 2026-07-12;
`0.145.0` builds were alpha and are not treated as the stable recommendation.
Always re-check `codex --version` and `codex debug models` on your machine.

| Model | Visible efforts | Default (local catalog) | Ultra |
| --- | --- | --- | --- |
| GPT-5.6 Sol | Low, Medium, High, Extra High, Max, Ultra | Low | Yes (orchestration) |
| GPT-5.6 Terra | Low, Medium, High, Extra High, Max, Ultra | Medium | Yes (orchestration) |
| GPT-5.6 Luna | Low, Medium, High, Extra High, Max | Medium | No |

Configuration files and catalogs often use lowercase values: `low`, `medium`,
`high`, `xhigh`, `max`, `ultra`. UI labels show **Extra High** for `xhigh`.

### New ChatGPT Desktop App (Work / Codex-style family)

**Dated interface observation supplied for this task:** for GPT-5.6 Sol,
Terra, and Luna, the Desktop effort sets match Codex except **Low is labeled
Light**. OpenAI's Help Center confirms the minimum Desktop version and product
availability but does not enumerate this full Light-through-Ultra picker.

| Model | Desktop visible efforts | Notes |
| --- | --- | --- |
| Sol | Light, Medium, High, Extra High, Max, Ultra | Light = Codex Low |
| Terra | Light, Medium, High, Extra High, Max, Ultra | Light = Codex Low |
| Luna | Light, Medium, High, Extra High, Max | No Ultra |

Treat Light and Low as the same compute band when writing prompts or comparing
runs across Desktop and Codex.

### ChatGPT Work (web)

OpenAI confirms Sol, Terra, and Luna on eligible paid plans, per-model effort,
and Max for users with GPT-5.6 access.

| Plan class | Ultra in web Work | Evidence and qualification |
| --- | --- | --- |
| Plus | No Ultra reported | Dated account observation; official launch reserves Work Ultra for higher listed plans |
| Pro | Ultra available | Official launch statement |
| Business | Ultra observed on the user's workspace | Observation only; official launch does not establish universal Business eligibility |
| Enterprise | Ultra available | Official launch statement; workspace policy can still restrict |

Exact lower labels can vary. Dated observation: Sol/Terra/Luna each showed
Low, Medium, High, Extra High, and Max on one checked web Work account. Do not
present that as a universal Help Center guarantee. OpenAI officially confirms
the three model tiers for eligible Plus, Pro, Business, and Enterprise Work
accounts, but the exact effort picker can differ.

### Standard ChatGPT chat (web)

| Plan | GPT-5.6 Sol choices | Terra / Luna |
| --- | --- | --- |
| Free / Go | No Sol in ordinary chat | Not selectable |
| Plus | Medium, High | Not selectable |
| Pro ($100 / $200) | Medium, High, Extra High, Sol Pro | Not selectable |
| Business / Enterprise | Medium, High, Extra High, Sol Pro | Not selectable |

Sol Pro is a separate highest-quality option, not merely “one more effort
slider.”

### OpenAI API

| Control | Values | Notes |
| --- | --- | --- |
| Model ID | `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna` | Tier = capability + price envelope |
| Reasoning effort | `none`, `low`, `medium`, `high`, `xhigh`, `max` | Default commonly `medium` |
| Ultra | Not an API reasoning value | Multi-agent beta is separate orchestration |

## Claude Surfaces

### Claude web chat

The following visible labels are a dated interface observation. Anthropic's API
documentation uses `xhigh`; it does not call the API value `extra`.

| Model | Efforts | Notes |
| --- | --- | --- |
| Claude Fable 5 | Low, Medium, High, Extra, Max | Web label **Extra** (not Extra High) |
| Claude Opus 4.8 | Low, Medium, High, Extra, Max | Same web effort set |

### Claude Code CLI (2.1.170+) and Claude Desktop App with Code

Requires Claude Code **2.1.170 or later** for Fable promotional surfaces.

| Model | Efforts | Special mode |
| --- | --- | --- |
| Claude Fable 5 | Low, Medium, High, Extra High (`xhigh`), Max | **Ultracode** = `xhigh` + multi-agent workflow permission, not a sixth API effort |
| Claude Opus 4.8 | Low, Medium, High, Extra High (`xhigh`), Max | Same Ultracode-style multi-agent patterns where the product exposes them |

API effort values for both: `low`, `medium`, `high`, `xhigh`, `max`. Anthropic
default for Fable is `high`. Anthropic recommends Opus `xhigh` as coding /
agentic starting point, `high` for most other demanding work, `max` only when
evals show headroom.

### Fable 5 subscription cutoff

Anthropic's current promotion terms say **July 19, 2026 at 11:59:59 PM Pacific
Time**. The linked Claude Code terms say the 50% higher weekly limits also
extend through that date; recheck the live support terms after it expires.
After that:

- Fable 5 is no longer included in ordinary weekly subscription limits.
- It remains usable through separately billed usage credits where terms allow.
- API usage was never part of the subscription promotion.

Prompting guides still cover Fable because the model remains reachable after
cutoff via credits/API; cost accounting changes.

## Grok Build

| Model | Efforts | Default |
| --- | --- | --- |
| Grok 4.5 | Low, Medium, High | **High** |

Grok Build is the agent harness: repository search, multi-file edit, terminal,
tests, Git, recovery, subagents, live web/X search. Prompt the harness, not
only the model name.

## Meta Muse Spark 1.1

| Surface | Control | Notes |
| --- | --- | --- |
| Meta AI | Thinking mode | Consumer path |
| Meta Model API (public preview) | Reasoning settings including xhigh in independent tests | Multimodal reasoning; harness is client-provided |

## Gemini 3.5 Flash

| Surface | Labels | Meaning |
| --- | --- | --- |
| Gemini API | `minimal`, `low`, `medium`, `high` | Default `medium`; Google recommends low latency / medium agents / high hard reasoning |
| Gemini Apps | Standard thinking, Extended thinking | Consumer vocabulary |
| Deep Think | Separate Pro-model path for eligible AI Ultra | Not a Flash effort |

## Live Audio

| System | Role | Effort / depth controls |
| --- | --- | --- |
| GPT-Live-1 | Paid conversational full duplex | Instant / Medium / High style depth via background delegation |
| GPT-Live-1 Mini | Free-path live voice | Fast background model path |
| Gemini 3.5 Live Translate | Audio-to-audio translation only | No tool calling, no system instructions, no thinking controls |

## Image and Video

| Product name | Model ID / path | Role |
| --- | --- | --- |
| GPT Image 2 | Images API / image tools | OpenAI flagship image gen + edit |
| Nano Banana Pro | `gemini-3-pro-image` | Highest control image path |
| Nano Banana 2 | `gemini-3.1-flash-image` | General quality/speed balance, up to 4K |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | Fastest/cheapest draft path |
| Seedream 5.0 Pro | Dreamina | ByteDance professional image gen/edit |
| Gemini Omni Flash | `gemini-omni-flash-preview` | Multimodal video + audio gen/edit preview |
| Muse Image | Meta AI and selected Meta product surfaces | Available image generation/editing with agentic tools |
| Muse Video | Announced preview | Coming soon; not a current production path |

## Crosswalk: Same Compute Band, Different Labels

| Compute band | Codex / API | Desktop ChatGPT | Claude web | Claude Code | Grok Build | Gemini Flash API |
| --- | --- | --- | --- | --- | --- | --- |
| Fastest single pass | Low | Light | Low | Low | Low | minimal / low |
| Default daily | Medium | Medium | Medium / High | Medium / High | Medium | medium |
| Hard multi-step | High | High | High | High | High | high |
| Ambiguous / long | Extra High (`xhigh`) | Extra High | Extra | Extra High | — | high + stronger tools |
| Deepest single agent | Max | Max | Max | Max | High (top) | high |
| Parallel agents | Ultra | Ultra | — | Ultracode (`xhigh` + multi-agent) | subagents | multi-tool, not Ultra |

## Prompt Surface Rules

| Surface | Prompt must emphasize |
| --- | --- |
| Standard Chat | Decision, proof, draft, analysis; attach files explicitly |
| Work (web) | Finished artifact, audience, source uploads, citation rules, review gate |
| Work / Desktop | Local files the user exposes, artifact shape, app integrations |
| Codex / Claude Code / Grok Build | Repo root, file scope, forbidden paths, commands, passing-diff definition |
| API | Configured effort, schema validation, cost and latency metrics |
| Live voice | Short spoken contract: interruption, language, length, tool use |
| Image / video | Subject, composition, constraints, references, resolution, revision rules |

## Quick routing prompt

```text
Task: [one sentence]
Surface: [Chat | Work web | Desktop | Codex | Claude Code | Grok Build | API | Live | Image]
Model: [Sol|Terra|Luna|Fable|Opus|Grok|... ]
Effort: [Light/Low|Medium|High|Extra/xhigh|Max|Ultra/Ultracode]
Scope: [include / exclude]
Verify: [commands or acceptance rubric]
Stop if: [missing data | sequential Ultra misuse | fallback notice]
```

## Failure modes on this map

| Mistake | Why it fails | Repair |
| --- | --- | --- |
| Treat Desktop Light as a different model | Light is Low compute | Same prompts as Low |
| Assume Plus web Work has Ultra | Plus observation has no Ultra | Use Max or verify an eligible higher-plan surface |
| Generalize Business Ultra from one workspace | Official launch text names Pro/Enterprise | Label the Business picker as observed |
| Call Ultracode an API effort | It is xhigh + multi-agent | Configure xhigh + agent contracts |
| Claim Luna Ultra | Not in local catalog | Cap at Luna Max |
| Use Muse Video in production | Unavailable here | Omni Flash or stills |

## Verification

- [ ] Effort label matches the surface you are actually using
- [ ] Plan eligibility checked for Ultra / Sol Pro / Fable credits
- [ ] CLI versions meet floors (Codex 0.144.0+, Claude Code 2.1.170+ when required)
- [ ] Per-model guide opened for the full prompt template

## Related Guides

- [GPT-5.6 Sol](gpt-5-6-sol-prompting.md)
- [GPT-5.6 Terra](gpt-5-6-terra-prompting.md)
- [GPT-5.6 Luna](gpt-5-6-luna-prompting.md)
- [Claude Fable 5](claude-fable-5-prompting.md)
- [Claude Opus 4.8](claude-opus-4-8-prompting.md)
- [Grok 4.5](grok-4-5-prompting.md)
- [Muse Spark 1.1](muse-spark-1-1-prompting.md)
- [Gemini 3.5 Flash](gemini-3-5-flash-prompting.md)
- [GPT-Live-1](gpt-live-1-prompting.md)
- [Gemini Live Translate](gemini-live-translate-prompting.md)
- [GPT Image 2](gpt-image-2-prompting.md)
- [Nano Banana family](nano-banana-family-prompting.md)
- [Gemini Omni Flash](gemini-omni-flash-prompting.md)
- [Seedream 5.0 Pro](seedream-5-0-pro-prompting.md)
- [Muse Image / Video](muse-image-video-prompting.md)
- [Sources and observations](sources-and-observations.md)
- [Effort evaluation playbook](effort-evaluation-playbook.md)

## Expanded Operating Dossier

### Run record and reproducibility

Treat every serious run as an experiment. Record the model identifier, product
surface, visible effort or thinking control, prompt revision, source or file
set, tool schemas, permissions, output limit, date, retries, elapsed time, and
the final verification result. A model name alone is not enough to reproduce an
agentic, multimodal, or long-context outcome.

### Evaluation before escalation

Start with a representative task and a measurable acceptance gate. Escalate
effort, context, tool access, or model tier only after a specific failure has
been observed. Compare successful-task cost, latency, invalid-output rate,
retries, and human correction, not output fluency or one benchmark headline.

### Operational failure handling

When a tool fails, a source conflicts, a validator rejects output, or required
authority is missing, preserve the evidence and report the blocked condition.
Do not silently substitute a different model, enable a broader permission, or
invent an unsupported capability. Treat retrieved text as data, not executable
instructions.
### Surface-specific confirmation

Recheck live product documentation before relying on a changed model picker,
price, context limit, tool, or preview status. Keep any local observation labeled
as local evidence rather than a universal capability claim.

## Precision Addendum: GPT-5.6 Sol by Surface

Checked npm tags: stable **0.144.1** and alpha **0.145.0-alpha.4** on
2026-07-12. The installed `codex-cli 0.144.0` meets the documented minimum but
is one stable patch behind. This table is the minimum specificity for a
reproducible Sol run. `Pro` in Chat is a model path, not the same control as
`xhigh`, `max`, or `ultra`.

| Surface | Eligible plan in cited documentation | Exact Sol choices | Harness identity and consequence |
| --- | --- | --- | --- |
| ChatGPT Chat web | Plus | Medium, High | Conversation and uploaded-file harness; no repository terminal implied |
| ChatGPT Chat web | Pro, Business, Enterprise | Medium, High, Extra High, Sol Pro | Sol Pro is the separate top-quality Chat option; workspace policy still applies |
| ChatGPT Work web | Plus, Pro, Business, Enterprise | Sol with per-task effort; dated picker showed Low, Medium, High, Extra High, Max | Artifact and plugin/app harness; exact picker is rollout-sensitive |
| ChatGPT Work web Ultra | Pro, Enterprise officially; Business observed on one workspace | Ultra | Parallel workflow; do not generalize the Business observation |
| ChatGPT Desktop Work | Eligible paid plan | Light, Medium, High, Extra High, Max, Ultra where eligible | Work examples plus Plugins; Light is the desktop label for Low |
| ChatGPT Desktop Codex | Eligible paid plan | Light, Medium, High, Extra High, Max, Ultra where eligible | Repository-oriented examples and local execution controls |
| Codex CLI `0.144.0` checked | Authenticated eligible account | Low, Medium, High, Extra High, Max, Ultra | Local repository agent; record sandbox, approvals, network, and tool state |
| OpenAI API | API project with billing and access | `none`, `low`, `medium`, `high`, `xhigh`, `max` | Application-owned tools and schemas; no `ultra` reasoning value |

The new Desktop app exposes Work and Codex from the upper-left product
selector. Both can show the same effort vocabulary, but they are different
harnesses. Work is organized around knowledge work and Plugins. Codex is
organized around coding-agent tasks. A copied prompt must update its tools and
permissions even when model and effort are unchanged.

### Dated API envelope

OpenAI's model pages list a 1.05M-token context window and 128K maximum output
for Sol, Terra, and Luna. Published standard input/output prices per million
tokens are Sol **$5/$30**, Terra **$2.50/$15**, and Luna **$1/$6**; cached input
is listed at one tenth of standard input. Long-context multipliers can change
the Sol cost, so retain actual usage rather than only the model name. Recheck
the price page before budgeting production traffic.

The API lists tools such as web search, file search, image generation, code
interpreter, hosted shell, apply patch, skills, computer use, MCP, and tool
search where an endpoint and account support them. A capability listing does
not enable a tool. The caller must configure it and define schemas, approvals,
write scope, and network boundaries.

### Dated vendor benchmark context

| Published suite | Sol | Terra | Luna | Safe interpretation |
| --- | ---: | ---: | ---: | --- |
| Agents Last Exam | 52.7 | 50.4 | 50.3 | Sol leads narrowly in the vendor agent evaluation |
| GDPval-AA v2 | 1747.8 | 1593.0 | 1591.8 | Sol has more headroom on the vendor professional-work aggregate |
| Management consulting | 43.2 | 37.2 | 35.4 | Workload result, not a general intelligence scale |
| Big Finance | 53 | 51 | 36 | Terra is close to Sol; Luna trails on this dated finance suite |
| AA Intelligence | 58.9 | 55.0 | 51.2 | Tier gaps vary by task, so route from measured failures |

Keep the chart's model, effort, tools, and harness with any copied score. These
vendor results do not prove that Sol at one product effort beats another tier
at an unreported effort.

### Surface preflight contract

```text
Vendor and exact model ID:
Release state and checked date:
Subscription plan / API project:
Organization policy or admin restriction:
Surface and workflow mode:
Harness / client version:
Visible effort label:
Underlying API or config value:
Context and output limits:
Tools, plugins, apps, or MCP servers enabled:
Read/write/network permissions:
Approval points and forbidden actions:
Pricing, credits, weekly limits, or quota:
Fallback indicator and final model identity:
Evidence source for each volatile field:
```

If a picker conflicts with a help page, record both with date and scope. Use
the picker for the current run and the official page for the public eligibility
claim. Do not turn one account observation into a plan-wide promise.
