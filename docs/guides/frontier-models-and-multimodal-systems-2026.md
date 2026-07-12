# Frontier Models and Multimodal Systems in 2026

Checked: 2026-07-12

This guide explains the GPT-5.6 family, current Claude, DeepSeek, GLM, Mistral,
Google open-model, media, robotics, live-audio, image, and video systems. It is
a dated research snapshot, not a promise that every model picker will look the
same on every account or an exhaustive catalog of every vendor release.

Facts are labeled by evidence type:

- **Official** means a vendor launch post, help article, API page, or live
  product catalog.
- **Independent** means a benchmark maintainer tested the model and published
  the method or configuration.
- **Local evidence** means a deterministic query of the Codex catalog installed
  in this checkout on the checked date.
- **Unconfirmed** means the checked public sources did not establish the claim.

Two additional labels matter throughout this guide. **Vendor claim** identifies
a result or qualitative statement published by the model maker but not
independently reproduced here. **Interpretation** identifies a recommendation
derived from the cited facts rather than a property guaranteed by a vendor.
Third-party videos are workflow evidence only. They do not establish prices,
plan eligibility, model IDs, architecture, or benchmark scores. The
[video research pack](../research/video-research-pack-2026-07-11.md) records
verified videos and discovery searches separately.

## Prompting Guides for These Models

For copy-ready work orders, effort playbooks, and surface-specific templates
for every model family in this essay, use the
[model and effort prompting pack](model-prompting/README.md). Start with the
[surface and effort map](model-prompting/surface-and-effort-map.md) when you
need Codex vs Desktop Light vs Work Ultra vs Claude Extra/xhigh labels.

## The Short Answer

GPT-5.6 is not one model with cosmetic speed buttons. Sol, Terra, and Luna are
three capability and price tiers, while effort controls how much work a tier
does before answering. Product surfaces then add another layer. Standard
ChatGPT exposes Sol reasoning choices. Work and Codex expose the family more
broadly. The API exposes model IDs and single-model reasoning levels. `ultra`
is different again because it coordinates agents rather than merely increasing
one model's reasoning setting.

Claude Fable 5 sits near Sol Max on broad independent intelligence testing and
below Sol Max in the current coding-agent composite, but its product safeguards
can route some requests to Opus 4.8. Grok 4.5 is a strong lower-cost coding
option in Grok Build. Gemini 3.5 Flash combines high throughput with agentic
performance. Muse Spark 1.1 is a fast, lower-cost Meta reasoning model. None of
those summaries means one model wins every math, engineering, coding, visual,
audio, or safety task.

![GPT-5.6 effort controls by product surface](../assets/model-guides/gpt-5-6-effort-surfaces.svg)

## GPT-5.6 Is a Family, Not a Ladder of Nicknames

OpenAI defines three durable tiers:

| Tier | Official role | Base API price per 1M input/output tokens | Practical starting point |
| --- | --- | ---: | --- |
| GPT-5.6 Sol | Flagship for the hardest professional work | $5 / $30 | Complex coding, research, science, design, and high-stakes synthesis |
| GPT-5.6 Terra | Balanced intelligence and cost | $2.50 / $15 | Daily repository work, documents, analysis, and tool-heavy tasks |
| GPT-5.6 Luna | Fastest and least expensive tier | $1 / $6 | High-volume extraction, bounded edits, classification, and subagents |

The tier and the effort answer different questions. The tier determines the
model family and its price-performance envelope. Effort tells that model how
aggressively to reason and use tools. A well-specified Luna task can beat a
poorly specified Sol task, but raising Luna's effort does not turn it into Sol.

### Standard ChatGPT Chat

OpenAI's current Help Center table says:

| Plan | GPT-5.6 Sol choices in ordinary Chat | What the plan label changes |
| --- | --- | --- |
| Plus | Medium and High | Included access and Plus usage allowance |
| Pro $100, often called Pro 5x | Medium, High, Extra High, and Sol Pro | Same model capabilities as Pro 20x, lower usage allowance |
| Pro $200, often called Pro 20x | Medium, High, Extra High, and Sol Pro | Same model capabilities as Pro 5x, higher usage allowance |
| Business and Enterprise | Medium, High, Extra High, and Sol Pro | Admin controls and workspace limits can apply |
| Free and Go | No GPT-5.6 Sol in ordinary Chat | GPT-5.5 Instant remains the ordinary fast path |

Medium, High, and Extra High use GPT-5.6 Sol. Pro uses GPT-5.6 Sol Pro, which
OpenAI presents as a separate highest-quality option for difficult, longer
workflows. Terra and Luna are not selectable in ordinary Chat. “Pro 5x” and
“Pro 20x” describe usage allowances, not different Sol effort menus.

### Work and Codex

The official launch post confirms Sol, Terra, and Luna for Plus, Pro, Business,
and Enterprise in Work and Codex. Free and Go receive Terra in Codex. It also
confirms per-model effort, `max` for users with GPT-5.6 access, Work `ultra`
for Pro and Enterprise, and Codex `ultra` for Plus and higher.

The exact lower menu labels are less cleanly documented. OpenAI's public Help
Center does not enumerate every Work menu on every client. The installed Codex
0.144.0 catalog does provide direct local evidence. The desktop interface uses
display labels while internal configuration can use lowercase values:

| Codex model | Visible local menu | Default in local catalog |
| --- | --- | --- |
| GPT-5.6 Sol | Low, Medium, High, Extra High, Max, Ultra | `low` |
| GPT-5.6 Terra | Low, Medium, High, Extra High, Max, Ultra | `medium` |
| GPT-5.6 Luna | Low, Medium, High, Extra High, Max | `medium` |

The current product label is **Low**, not "Light." User interfaces can display
**Extra High** while configuration files and model catalogs use `xhigh`.

The surfaces have related model controls but different jobs:

| Surface | Primary operating context | Access and artifact boundary |
| --- | --- | --- |
| Desktop Codex | Repository operation, shell commands, tests, patches, and Git | Works against an approved local workspace and produces repository changes |
| Desktop Work | Document and artifact production across approved local files and apps | Desktop integration can use local sources that the user exposes |
| Web Work | Cloud-hosted project work and artifacts | Does not directly open arbitrary local files; uploads and connected sources define scope |
| Standard Chat | Conversational answers and attached-file analysis | No repository or desktop control unless a separate product feature supplies it |

OpenAI documents the GPT-5.6 family and effort structure for Work and Codex,
but account pickers can still depend on plan, client version, workspace policy,
region, and staged rollout. On the checked web Work account, Sol, Terra, and
Luna each showed Low, Medium, High, Extra High, and Max. That exact menu is a
dated interface observation, not a universal Help Center guarantee. Desktop
Work follows the documented family and per-model effort structure, but this
guide does not infer an exact picker where official documentation and local
evidence do not enumerate it. OpenAI also says web Work and desktop Work
threads are separate at launch.

### API

The API model IDs are `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`.
Their published reasoning values are `none`, `low`, `medium`, `high`, `xhigh`,
and `max`. The API does not list `ultra` as a reasoning value. Multi-agent beta
in the Responses API is a separate orchestration capability. Model tier,
reasoning effort, and orchestration must therefore be configured and measured
as three different variables.

| API control | What it changes | What it does not imply |
| --- | --- | --- |
| Model ID | Sol, Terra, or Luna capability and token price | A particular reasoning effort |
| Reasoning value | Single-model time and compute allocation | Ultra or automatic parallel agents |
| Multi-agent beta | Concurrent subagents plus synthesis in one response | A new model tier |
| Programmatic Tool Calling | In-memory programs that coordinate tools and filter intermediate data | Unlimited tool permissions |
| Prompt caching | Reuse economics for stable prompt prefixes and explicit breakpoints | A larger context window |
| Context and output limits | 1.05M input context and 128K maximum output | Guaranteed useful recall across every token |

That distinction prevents a common benchmark error. Artificial Analysis tested
GPT-5.6 Sol Max in Codex. It did not test “Sol Ultra” as if Ultra were a larger
single-model effort. An Ultra run may do better or worse on a real project, but
the Max score cannot be relabeled.

## What Each GPT-5.6 Effort Is For

Effort should be chosen against a measurable outcome, not task anxiety.

| Effort | Best fit | Prompt shape | Main failure risk |
| --- | --- | --- | --- |
| `low` | Small edits, lookups, formatting, focused extraction | Exact input, one output, one check | Missing hidden dependencies |
| `medium` | Normal coding, research, and document tasks | Goal, files, constraints, acceptance tests | Under-scoping a genuinely hard task |
| `high` | Multi-file work, difficult debugging, source synthesis | Add failure cases, stronger checks, and decision criteria | More latency and tool use |
| `xhigh` | Hard architecture, long investigations, uncertain root causes | Give checkpoints, stop conditions, and evidence rules | Over-analysis on routine work |
| `max` | Frontier single-agent reasoning where errors are expensive | State the decision, alternatives, test matrix, and review gate | Large token and time cost |
| `ultra` | Parallelizable projects with separable workstreams | Define subtask boundaries and synthesis criteria | Coordination overhead and duplicated work |

### Sol at Low, Medium, High, Extra High, Max, and Ultra

Sol Low is useful when the task is easy to verify but still benefits from the
flagship model's judgment. Good examples are a narrow code review, a one-file
repair, or a sourced answer with a fixed schema. Give it a short scope and a
deterministic check.

Sol Medium is the default practical choice for ordinary professional work. It
has enough room for tool calls and correction without turning every task into
a long investigation. In standard Chat this is also the first GPT-5.6 Sol
reasoning level available to eligible users.

Sol High fits multi-step reasoning, difficult implementation, and work where
the first plausible answer needs testing. Ask it to inspect before editing,
name the acceptance tests, and require evidence for completion.

Sol Extra High or `xhigh` fits problems with real uncertainty: a cross-service
failure, an unfamiliar repository, a hard proof, or research where sources
conflict. Give it a decision log and explicit boundaries so the extra effort is
spent resolving uncertainty rather than expanding scope.

Sol Max is the deepest documented single-model effort. Use it for a final
architecture decision, difficult math or science work, a high-risk migration,
or a review where a missed defect is expensive. The prompt should state what
would falsify the answer and what evidence the reviewer must inspect.

Sol Ultra is an orchestration mode. OpenAI says the documented product mode
coordinates four agents in parallel by default, then has a primary agent
synthesize the work. Use it when the problem divides cleanly into independent
workstreams such as implementation, tests, documentation, source verification,
and adversarial review. It can reduce elapsed time when those streams can run
at once, but total token use can rise. Weak task boundaries can also create
duplicated investigation, conflicting edits, and expensive reconciliation. A
single tiny bug, a tightly sequential migration, or a task with one shared
mutable file is usually better at High or Max. OpenAI's API lets developers
build ultra-like workflows with multi-agent beta, but `ultra` itself is not an
API reasoning value.

### Terra at Low, Medium, High, Extra High, Max, and Ultra

Terra Low is a cost-aware executor for scoped tasks with clear inputs. It is a
good fit for deterministic repository edits, structured data cleanup, and
drafting from a supplied outline.

Terra Medium is the strongest default for routine work when cost matters. Use
it for daily coding, test updates, document synthesis, and tool use where the
acceptance criteria are already clear.

Terra High gives more room for debugging and multi-file reasoning. It is often
the right escalation when a Medium attempt found the relevant area but did not
close the issue.

Terra Extra High or `xhigh` suits broad but bounded engineering tasks. It can
inspect more callers, test more hypotheses, and verify more surfaces. Require
progress checkpoints so it does not drift into unrelated cleanup.

Terra Max is useful when Sol's price is hard to justify but the task still
needs the deepest Terra attempt. Artificial Analysis measured Terra Max at 55
on the Intelligence Index and 77 in the Codex coding-agent harness.

Terra Ultra is available in the local Codex catalog and should be treated as
parallel orchestration, not “Terra beyond Max.” It is attractive for bounded
multi-area work where several Terra agents can operate against stable
contracts and a final reviewer can reconcile their outputs. Terra's lower
token price can make this pattern practical, but parallel duplication can erase
the saving. High or Max is normally better when every step depends on the
previous one.

### Luna at Low, Medium, High, Extra High, and Max

Luna Low is for speed-sensitive, high-volume work with a simple correctness
test. Classification, metadata extraction, repeated small transformations, and
bounded subagent tasks are good examples.

Luna Medium is a fast daily driver for clear work orders. It can implement a
small feature, summarize a source packet, or update tests when the repository
pattern is already known.

Luna High is useful when speed still matters but the task has several steps or
requires tool use. Keep the output contract tight and give it examples of edge
cases.

Luna Extra High or `xhigh` is the deepest exploratory tier before Max. It makes
sense when a lower-cost model needs more search or verification but the task
does not justify Sol.

Luna Max is Luna's highest local Codex effort. Artificial Analysis measured it
at 51 on the Intelligence Index and 75 in the Codex coding-agent harness. The
local catalog does not expose Luna Ultra.

Across the family, a higher tier usually buys stronger judgment and coding
reliability, while a higher effort gives the selected tier more opportunity to
inspect context, call tools, test hypotheses, and revise. Neither guarantees a
better result. Long-context work can fail through poor retrieval or weak task
decomposition even inside a 1.05M-token window. Parallel delegation works best
when subtasks have independent inputs, explicit ownership, and a deterministic
synthesis gate. For bounded transformations, Luna or Terra with a clear test
often beats an expensive open-ended Sol run on cost and latency. For ambiguous
architecture, mathematics, engineering analysis, or high-risk synthesis, Sol
High through Max offers more useful headroom.

### Prompt Patterns by Interface

In Chat, ask for the reasoning product you want: a decision, proof, draft,
analysis, or critique. The model does not have a repository unless you supply
files or use a compatible product feature.

In Work, describe the finished artifact, its audience, its source files, and
the review gate. For example: “Produce a two-page decision memo from these
three documents. Keep every numeric claim traceable. Flag conflicts and end
with a recommendation.”

In Codex, describe observable repository state: exact scope, files that must
remain untouched, commands to run, and what a passing diff looks like. For
Ultra, add subtask boundaries and a synthesis rule.

In the API, select effort through configuration and measure it. Compare task
success, latency, output tokens, tool calls, and human correction time on your
own evaluation set. Do not assume a higher effort always improves a structured
or latency-sensitive task.

### Price, Context, and Caching

All three GPT-5.6 API tiers publish a 1.05M-token context window and 128K maximum
output. Requests above 272K input tokens are billed at 2x input and 1.5x output
for the full request. Cache writes cost 1.25x uncached input. Cache reads retain
the 90% cached-input discount. OpenAI also documents explicit cache breakpoints
and a minimum 30-minute cache life for GPT-5.6 and later.

Those headline rates do not predict project cost by themselves. Higher effort
can generate more reasoning tokens, more tool calls, and longer agent traces.
The right comparison is cost per successful task, including retries and human
correction.

### Safeguards and Reliability

OpenAI describes GPT-5.6 as combining model protections with real-time checks,
monitoring, and access controls. Higher capability does not remove refusals or
temporary restrictions. Biology, cyber, and other high-risk work can receive
additional checks. A reliable workflow should log what model ran, what effort
was selected, what tools were allowed, and whether a fallback occurred.

### Watch: GPT-5.6 Family Testing

[![Watch a hands-on test of GPT-5.6 Sol, Terra, and Luna](https://i.ytimg.com/vi/xDXX2M5DrO0/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-5-6-family-test)

*Third-party test by AICodeKing. Use it for workflow context, not as the source
for access, pricing, or benchmark claims.*

## Claude Fable 5 and Claude Opus 4.8

Anthropic describes Fable 5 as a Mythos-class model made available with an
additional safeguard layer. Its API effort values are `low`, `medium`, `high`,
`xhigh`, and `max`; `high` is the default. Claude Code's Ultracode is not a
sixth API effort. Anthropic documents it as `xhigh` plus standing permission
for multi-agent workflows.

### The July 19 Subscription Access Update

Anthropic's [Fable 5 promotional-access terms](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access)
state that the promotion is extended through **July 19, 2026 at 11:59:59 PM
PT**. Its linked [Claude Code weekly-limits promotion](https://support.claude.com/en/articles/15910845-claude-code-may-july-2026-weekly-limits-promotion)
states that the 50% increase to Claude Code weekly usage limits runs through the
same date. The promotion is available to Pro, Max, Team, and premium seats on
seat-based Enterprise plans where the organization enables it. Recheck the live
terms before a billing or availability decision because this is a dated
promotional condition, not a permanent product entitlement.

The promotion covers included subscription access rather than API usage. Do not
rewrite the extension as an API-price, regional-availability, Enterprise-policy,
or product-surface claim beyond the terms Anthropic publishes.

The promotion covers Claude web, mobile, Desktop, Cowork, Claude Code, Design,
Microsoft 365, Teams, and Tag where the account and organization are eligible.
Claude Code requires version 2.1.170 or later, and Cowork requires the latest
Claude Desktop version. Cowork on the web or desktop still requires the
eligible account and product access documented by Anthropic; the promotional
allowance does not convert API use into subscription use.

When the extended period ends, readers should check whether Fable leaves ordinary
included weekly subscription usage, remains available through separately billed
usage credits, and continues through the API at API rates. Those are distinct
surfaces, so a subscription-access update must not be rewritten as an API-price
or API-availability update without current official terms.

### Price, Context, and Fallback

Fable 5 costs $10 per million input tokens and $50 per million output tokens.
Opus 4.8 costs $5/$25. Anthropic currently keeps standard pricing across the
full 1M context window for both. Prompt-cache writes and data-residency choices
can add their own multipliers.

Fable's production safeguards matter to evaluation. Anthropic says flagged
cyber, biology, chemistry, or distillation requests can be handled by Opus 4.8
instead, with the user informed. Artificial Analysis therefore labels its
Fable configuration “with fallback.” That is a product result, not a pure
underlying-model score.

Fable's `low`, `medium`, `high`, `xhigh`, and `max` controls are single-model
effort values. Claude Code's Ultracode combines `xhigh` with standing permission
to use multi-agent workflows; it is not a sixth API effort. Low and Medium fit
bounded edits and inexpensive drafting. High is Anthropic's default. Extra
High fits harder coding and agentic work. Max is the expensive final attempt
when an evaluation shows that more computation improves the result. Because
fallback can change which model actually handles a sensitive prompt, serious
tests should record the visible fallback notice and avoid claiming a pure
Fable result when routing occurred.

### Claude Opus 4.8 as Model and Claude Code Configuration

Opus 4.8 remains a strong model in its own right and the documented fallback
for specified Fable safeguards. Anthropic recommends `xhigh` as the coding and
agentic starting point, `high` for most other demanding work, and `max` only
when evaluation shows useful headroom. For document analysis, long financial
work, and finished professional artifacts, model choice should be judged on
citation accuracy, spreadsheet or document operations, analytical quality,
and correction cost rather than prose fluency alone.

The official API price is $5 per million input tokens and $25 per million
output tokens, with the same published 1M context pricing rule cited above.
Fable costs twice as much per input token and twice as much per output token,
but pricing alone does not decide task cost because effort, retries, tool calls,
and fallback can dominate.

Artificial Analysis reports Opus 4.8 Max at 55.7 on Intelligence Index v4.1
and 73 in the Coding Agent Index **in Claude Code**. That coding number includes
Claude Code's system prompt, tools, permission model, terminal loop, and file
editing behavior. It is not a bare API-model score. Fable Max with fallback
scores higher in the dated intelligence and coding snapshots, while Opus offers
a cleaner comparison when the evaluator needs to avoid Fable's model-routing
layer.

## Claude Sonnet 5

**Official, checked 2026-07-12.** Anthropic released Claude Sonnet 5 on
2026-06-30. Its launch post says it is available on every Claude plan, in Claude
Code, and through the Claude Platform as `claude-sonnet-5`. The introductory API
price is $2 input / $10 output per million tokens through 2026-08-31, changing
to $3 / $15 afterward. These are vendor-published product facts, not an
independent cost or capability comparison.

Anthropic positions Sonnet 5 as its most agentic Sonnet model. It narrows the
gap to Opus 4.8 on some agentic tasks, but that positioning does not establish
that it replaces Fable 5 or Opus 4.8. The launch post confirms browser and
terminal tool use in the product description; it does not make a browser,
terminal, or agent harness available automatically to every API caller.

| Decision | Evidence-conscious guidance |
| --- | --- |
| Normal knowledge work and cost-sensitive coding | Start with Sonnet 5 where its lower dated API price is appropriate; supply an explicit deliverable and a verification step. |
| Long-running or tool-using work | Define the tool boundary, stop conditions, and recovery behavior. Record the product surface and actual tool configuration. |
| High-effort work | The checked launch source compares effort levels but does not publish a complete cross-surface effort menu. Confirm the live API or product control before claiming a particular value. |
| Fable or Opus comparison | Treat Sonnet, Fable, and Opus as distinct released models. Select with a matched task evaluation, not a family-name assumption. |

Use the [Sonnet 5 prompting guide](model-prompting/claude-sonnet-5-prompting.md)
for source-aware work orders and unsupported-use boundaries.

## Coding, Agentic, and Cost-Efficient Model Additions

### DeepSeek-V4-Pro and DeepSeek-V4-Flash

**Official preview, checked 2026-07-12.** DeepSeek's 2026-04-24 release and
current API documentation identify `deepseek-v4-pro` and `deepseek-v4-flash`.
Both are API-accessible through DeepSeek's OpenAI-compatible and
Anthropic-compatible endpoints, support thinking and non-thinking modes, JSON
output, tool calls, a 1M-token context, and a 384K maximum output. The current
pricing table lists $0.435/$0.87 input-cache-miss/output per million tokens for
Pro and $0.14/$0.28 for Flash; cache-hit prices and concurrency limits are
published separately in that same official table.

DeepSeek calls the release "Preview" and says the weights are available. This
guide therefore does not relabel either model stable merely because the API is
usable. The checked sources establish the announced total/active parameter
counts as vendor claims, but this guide does not restate a license because the
reviewed API pages did not establish one. `deepseek-chat` and
`deepseek-reasoner` are compatibility aliases scheduled for discontinuation on
2026-07-24 at 15:59 UTC, not new V4 product names.

### GLM-5.2

**Official released/open source, checked 2026-07-12.** Z.ai announced GLM-5.2
on 2026-06-16 as a flagship long-horizon model, with an MIT license, publicly
available weights, 1M context, Z.ai product access, and Coding Plan support.
The official guide uses the model name `GLM-5.2` and documents High and Max
thinking choices in its coding surfaces. It does not supply a current per-token
price or a maximum-output figure in the source reviewed here, so neither is
invented in this guide.

Z.ai's published coding results are **vendor claims**. They should not be
combined with independent benchmark or agent-harness results without matching
configuration, tools, context limit, and time limit. See the
[GLM-5.2 prompting guide](model-prompting/glm-5-2-prompting.md).

### Current Mistral Family by Workload

Mistral's current catalog has both generalist and specialist systems. They
should not share one leaderboard.

| System | Status and official identifier | Appropriate evaluation |
| --- | --- | --- |
| Mistral Medium 3.5 | Open weights, Modified MIT; `mistral-medium-3-5`; 256K context; $1.50/$7.50 per million input/output | Coding and agent workflows with the same tools, repository tasks, and correction budget |
| Mistral Small 4 | Open weights, Apache 2.0; `mistral-small-2603`; 119B total / 6.5B active; 256K; $0.15/$0.60 | Cost-sensitive multimodal, coding, and agent tasks, not the word "Small" alone |
| OCR 4 | Premier document service; `mistral-ocr-4-0`; paragraph bounding boxes and structural labels; $4/1,000 pages or $5/1,000 annotated pages | Extraction accuracy, tables, layout, bounding boxes, language coverage, and human correction |
| Voxtral TTS | Open weights, CC BY-NC 4.0; `voxtral-mini-tts-2603`; 9 languages; streaming and about 90 ms time-to-first-audio | Intelligibility, latency, pronunciation, voice-consent safeguards, and edit burden |
| Leanstral 1.5 | Labs model; `labs-leanstral-1-5`; Lean 4 specialization; 119B total / 6.5B active; 256K; listed free | Successfully compiled proofs, correction burden, and reproducible Lean project tests |
| Robostral Navigate | Officially announced 2026-07-08 as embodied navigation | Navigation, simulation transfer, safety constraints, and physical-robot validation, not general-chat scores |

The Mistral model cards establish the listed identifiers, published limits,
licensing labels, and prices. They do not establish every requested deployment,
handwriting, voice-identity, robot-hardware, or safety detail. In particular,
the reviewed Mistral announcement establishes Robostral Navigate's existence
but not a public API identifier, pricing, weight download, or operating terms.
It is therefore an **announced, limited-information system**, not production
guidance. See [Mistral current-model prompting](model-prompting/mistral-current-models-prompting.md).

### Google Open, Media, and Robotics Systems

| System | Classification | Confirmed, source-bounded facts |
| --- | --- | --- |
| Gemma 4 | Open-weight family | 2B, 4B, 12B, 26B A4B, and 31B variants; commercial use permitted; 128K small-model and 256K medium-model contexts; text/image inputs across the family, with audio and video support varying by variant |
| DiffusionGemma | Experimental open model | Apache 2.0; 25.2B total / 3.8B active; discrete diffusion; up to 256K context; 256-token canvases; intended for low-latency local experimentation rather than the default production-quality Gemma path |
| Veo 3.1 Lite | Public preview video API | `veo-3.1-lite-generate-preview`; text/image input; video with audio output; no 4K output or Extension in the reviewed model page |
| Lyria 3 | Public-preview music API family | `lyria-3-clip-preview` for 30-second clips and `lyria-3-pro-preview` for longer prompted songs; text/image input; MP3 stereo output |
| Gemini Robotics-ER 1.6 | Preview robotics VLM | `gemini-robotics-er-1.6-preview`; text/image/video/audio input and text output; current API page lists 131,072 input and 65,536 output tokens plus tool, structured-output, and thinking support |

Gemma is not an API edition of Gemini. Gemma 4 and DiffusionGemma are
open-weight systems intended for deployment choices that the builder controls;
Gemini media and robotics entries are hosted product surfaces with current
preview restrictions. DiffusionGemma's architecture is described by its official
model card, so this guide can distinguish its blockwise discrete-diffusion
generation from ordinary token-by-token autoregression without inference.

Veo, Lyria, OCR, theorem proving, and robotics require category-specific
evaluation. Video needs temporal consistency, audio, editing, and prompt
adherence; music needs structure, audio quality, prompt adherence, and edit
continuity; OCR needs extraction and layout fidelity; Leanstral needs valid
compiled proofs; robotics needs simulation, spatial reasoning, safety, and
real-world transfer. Embodied reasoning, high-level planning, and function
calling do **not** establish safe direct low-level motor control.

The current Lyria guide says 44.1 kHz output, while the March 25 API changelog
said 48 kHz. This is an official-source conflict. The table follows the current
guide and retains the discrepancy in [Uncertainties](#uncertainties-and-known-limits).
The Robotics-ER API page lists 131,072/65,536 limits while its model card uses
rounded 128K/64K figures; use the current API page for the integration limit.
See [Google open, media, and robotics prompting](model-prompting/google-open-media-robotics-prompting.md).

### Watchlist: Gemini 3.5 Pro

**Officially announced, unavailable, checked 2026-07-12.** Google's current
Gemini 3.5 page says only "3.5 Pro coming soon." The reviewed Google sources do
not provide a public or restricted API identifier, documented availability, or
access instructions. Gemini 3.5 Pro is therefore a watchlist item, not a model
entry, and this guide provides no price, context limit, tools, or prompting
template for it.

## Detailed Dossiers for the Newly Audited Systems

The tables above answer the first selection question. The dossiers below answer
the more consequential second question: what must be true about the task,
integration, evidence, and safety boundary before a reader should choose that
system. They deliberately contain more operational detail than a leaderboard.
They do not turn a vendor capability statement into a promise that a specific
deployment, account, agent harness, or local machine can reproduce it.

### Claude Sonnet 5: Product Surface, Work Shape, and Review Discipline

#### Confirmed product position

Anthropic's [June 30 launch post](https://www.anthropic.com/news/claude-sonnet-5)
identifies Sonnet 5 as an agentic Sonnet-class model, not a rename of Fable 5
or Opus 4.8. The release establishes three distinct access facts: it is the
default model for Free and Pro, is available to Max, Team, and Enterprise users,
and is available through Claude Code and the Claude Platform. The API identifier
is `claude-sonnet-5`. A reader should record the actual selected surface because
the model name alone does not establish account allowance, tool permissions,
connected services, or regional availability.

The launch's introductory price is $2 per million input tokens and $10 per
million output tokens through 2026-08-31. Anthropic says the standard price then
becomes $3/$15. That scheduled change means a cost evaluation needs two columns:
the rate used in the experiment and the date on which the decision will be
revisited. Do not compare a launch-period Sonnet run with another model's
standard rate and call the result a durable price ranking.

#### Capability claims and their boundaries

Anthropic describes browser and terminal tool use, planning, coding, and
autonomous operation as product capabilities. Those are **vendor claims** and
product-surface descriptions. They do not imply that a bare API call can browse,
edit a repository, run a shell, access credentials, or continue after a failed
command. Those behaviors require an application-provided tool schema, a
permission policy, and a loop that supplies tool results back to the model.

The launch compares effort levels and says higher-effort use can change the
cost-performance trade-off. The source does not enumerate a permanent effort
menu for every Claude client. Treat a visible picker as a dated observation,
verify its allowed values against the current product/API page, and record the
selected value in an evaluation log. Do not copy a Claude Code configuration
onto web chat or assume that an API setting grants a UI-only agent feature.

#### Suitable work and unsuitable shortcuts

Sonnet 5 is a plausible candidate for bounded knowledge work, source-grounded
analysis, coding with a controlled tool loop, and lower-cost comparisons against
other Claude-family models. A good evaluation has a defined artifact: a repaired
test, a decision memo with traceable sources, a validated data transform, or a
reviewable patch. The evaluator should capture task success, citations or test
results, tool calls, retries, wall time, output tokens, and human correction.

It is a poor choice for claiming that one vendor's benchmark score proves
universal superiority, for a production action with no human approval boundary,
or for a task whose required data has not been made available. If the tool loop
is missing, the correct comparison is text-only; if the tool loop differs, the
result is a product-and-harness comparison rather than a pure checkpoint score.

#### Long-context and agentic work order

For a long source packet, start with a source map: name the documents, their
authority, dates, conflict rules, and the exact decision required. Ask the model
to identify missing evidence and conflicts before producing synthesis. Require
a claim ledger or citations in the output so a reviewer can distinguish supplied
facts, inference, and unanswered questions. A large context window, if exposed
by a chosen surface, is capacity rather than a guarantee of relevant retrieval.

For a coding agent, require an inspect-first sequence: locate the failing
behavior, state the smallest hypothesis, name the regression test, make a
focused change, run the test, inspect the diff, then report remaining risk. The
prompt should name allowed paths, prohibited actions, command timeout behavior,
and what to do when a tool result contradicts the initial hypothesis. This is
more useful than a vague request to "be autonomous."

#### Safety, fallback, and evidence logging

The launch and its system-card references describe safety testing and cyber
safeguards. That does not make Sonnet 5 appropriate for bypassing a security
review, operating machinery, or completing a regulated action without the
surrounding controls. Log refusals, policy notices, altered tool permissions,
and model/version changes. A model response that was blocked, routed, or
partially completed is a meaningful evaluation outcome, not a failed detail to
hide.

### DeepSeek-V4-Pro and DeepSeek-V4-Flash: Preview APIs With Deliberate Modes

#### Release state and identifiers

DeepSeek's [V4 Preview release](https://api-docs.deepseek.com/news/news260424/)
calls both variants live and open-sourced while explicitly retaining the Preview
label. The current [pricing and model table](https://api-docs.deepseek.com/quick_start/pricing/)
identifies `deepseek-v4-pro` and `deepseek-v4-flash`, both API base URLs, and
the supported feature set. The release also says the models are available in
chat.deepseek.com under Expert Mode and Instant Mode. This is evidence of a
public usable surface, not evidence that every outside agent product has native,
well-tested support.

The models replace a compatibility period for `deepseek-chat` and
`deepseek-reasoner`: DeepSeek maps those aliases to Flash's non-thinking and
thinking modes until the stated 2026-07-24 15:59 UTC retirement. Production
integrations should use the explicit V4 identifiers, not rely on an alias whose
meaning and retirement date are documented by the provider.

#### Pro versus Flash is not only a price decision

DeepSeek publishes 1M context, 384K maximum output, JSON output, tool calls,
chat prefix completion, and Fill-in-the-Middle completion. It documents both
thinking and non-thinking modes. FIM is documented as non-thinking only. That
means an evaluator must hold mode constant when comparing code-completion
results: a Flash non-thinking FIM response and a Pro thinking chat response are
not the same workload.

The official table lists Flash at $0.14 cache-miss input and $0.28 output per
million tokens, and Pro at $0.435/$0.87. Cache-hit input is separately priced,
and account concurrency is listed as 2,500 for Flash and 500 for Pro. These
numbers are dated pricing inputs, not total task cost. Long prompts, hidden
reasoning, retries, tool calls, and failures to use a cacheable prompt prefix
can dominate the cost of a real agent run.

#### A reproducible mode-selection protocol

Choose non-thinking mode for a bounded transform whose answer can be validated
deterministically: a schema conversion, a formatting pass, a narrow FIM task,
or classification against an agreed label set. Give one input contract, one
output schema, explicit null/unknown handling, and a validator. If a result
fails the validator, preserve the failure rather than silently retrying on a
different model and reporting the best output as a single run.

Choose thinking mode only when the task requires planning, multi-step diagnosis,
or a tool-using loop that can check its own work. Bound the loop by max turns,
allowed tools, allowed paths, and a stop condition. Record whether a tool error,
timeout, malformed call, or user approval stop caused the outcome. The model's
tool-call feature does not decide whether the host actually executes a call.

#### Context management and quality checks

For 1M-context tasks, partition context into stable instructions, source index,
task-local evidence, and append-only tool results. Reuse stable prefixes when
the application supports caching. Then test retrieval deliberately: hide a few
known facts across the packet, ask a constrained question, and confirm the
answer against the source locations. Do not infer that the model remembered a
fact simply because it produced plausible prose.

Evaluate Pro and Flash using the same prompt, retrieval process, tool schema,
deadline, and reviewer rubric. Record the model identifier, date, thinking mode,
sampling settings where exposed, maximum output, context size, cache condition,
concurrency behavior, and all retries. Vendor benchmark charts can motivate
this evaluation, but are **vendor claims** until a matching independent harness
and configuration are available.

#### Open-source and deployment caution

DeepSeek's release says the weights are available. It does not let this guide
infer a license from the word open-sourced, claim a particular local hardware
requirement, or promise parity between hosted API and a self-hosted checkpoint.
Before local deployment, confirm the exact repository, license, precision,
runtime, safety controls, quantization, and test result for the selected build.

### GLM-5.2: Long-Horizon Claims Need Long-Horizon Evidence

#### What the official release establishes

Z.ai's [GLM-5.2 release](https://z.ai/blog/glm-5.2) presents the model as its
latest flagship for long-horizon tasks. It states a 1M-token context, MIT
license, publicly available weights, Z.ai access, Coding Plan availability, and
High/Max effort choices in the coding surface. The source also describes
long-context training, coding-agent positioning, and a changed sparse-attention
design. Those architecture and performance descriptions are vendor evidence;
they should not be used as proof of a workload's expected success rate.

The reviewed release does not publish a per-token API price or a general maximum
output for the exact deployment described here. The guide therefore leaves both
as **unknown** rather than extrapolating from an older GLM release or a reseller
price page. A user considering a purchase should check the product surface on
the day of use and note whether quota, subscription, API, or self-hosted costs
are being compared.

#### Meaning of long-horizon work

Long horizon does not mean pasting an entire repository into one request. It
means maintaining correct state across multiple observations, decisions, tool
results, revisions, and verification steps. A durable task should have a goal,
a non-goal list, a current-state summary, a source/file map, a milestone list,
an action boundary, and an acceptance test. Each milestone should create an
artifact that a later turn can inspect: a failing test, dependency map, design
decision, patch, benchmark table, or source ledger.

Use a compact running state rather than replaying every raw tool transcript.
After a meaningful step, summarize what changed, what was disproven, which files
or sources matter next, and what validation remains. Preserve links to the
underlying evidence so compaction does not turn uncertainty into an invented
fact. This procedure is portable to GLM-5.2, but it does not claim that every
product surface exposes the same memory or agent controls.

#### Effort selection and evaluation

Treat High and Max as an experimentally controlled cost/latency choice. Start
with a representative task at High. Escalate to Max only after measuring a
specific deficiency, such as an unclosed dependency chain, a failed regression,
or a source conflict that survives the bounded review. Compare task success,
elapsed time, output and tool volume, retries, and correction burden. A longer
trace is not evidence of a better result.

The official release reports several benchmark results and supplies some setup
details. Those values remain **vendor claims** in this guide. Never place them
beside an independent leaderboard score without keeping the evaluator, harness,
context limit, token budget, tool access, timeout, and judge model separate.

#### Deployment and failure boundaries

Open weights expand deployment options, but they also make the operator
responsible for runtime choice, GPU memory, quantization, throughput, data
handling, moderation, update policy, and incident response. Check the exact
weight artifact and license before deployment. For an agent, do not allow
network, secret, production, or destructive actions merely because the task is
long. When a task needs additional authority, stop with the unresolved decision
and evidence rather than consuming more context on an unauthorized action.

### Mistral Medium 3.5 and Mistral Small 4: Generalist Models With Different Operating Envelopes

Mistral's [Medium 3.5 model card](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04)
labels it an open-weight, frontier-class multimodal model optimized for agentic
and coding use cases. It lists `mistral-medium-3-5`, a 256K context, Modified
MIT licensing, and $1.50/$7.50 input/output per million tokens. The [Small 4
card](https://docs.mistral.ai/models/model-cards/mistral-small-4-0-26-03) lists
`mistral-small-2603`, 119B total and 6.5B active parameters, 256K context, and
$0.15/$0.60 pricing. These values describe documented service options, not a
guarantee that either model will be available with identical limits in every
region, account, or deployment runtime.

Choose between them with a matched workload, not their names. Define a fixed
repository task, source-analysis task, or structured-output task; keep the
prompt, tools, context selection, output cap, evaluation rubric, and retry
policy unchanged. Then compare task completion, time, cost, invalid-output rate,
tool-call errors, and reviewer correction. A lower token price can be defeated
by retries. A larger or more expensive model can be wasteful when a deterministic
validator shows a smaller model completes the work on the first pass.

For multimodal tasks, specify what the images or documents are evidence for,
which assertions must be checked against them, and what ambiguity must be
returned as unknown. For coding, include a path allow-list, an exact test command,
and a no-unrelated-cleanup rule. A model card's agents or function-calling label
does not grant a host application a shell, browser, network access, or write
permission. The application controls that boundary.

Both models are candidates for self-deployment because Mistral labels them open,
but hosted and self-hosted results must be kept separate. A self-hosted report
should name the exact weight revision, license, precision, quantization, runtime,
hardware, maximum context, sampling parameters, system prompt, tool adapter, and
safety filters. Without that record, a claim of equivalence to a hosted API run
is not reproducible.

### Mistral OCR 4: Document Intelligence Must Be Tested as Extraction

The [OCR 4 model card](https://docs.mistral.ai/models/model-cards/ocr-4-0)
identifies a Premier Document AI service with `mistral-ocr-4-0`, paragraph-level
bounding-box extraction, structural block labels, and listed prices of $4 per
1,000 pages or $5 per 1,000 annotated pages. These are useful product facts, but
they do not establish a universal accuracy score, handwriting guarantee,
language guarantee, self-hosted option, or security certification beyond what
the current documentation specifically says.

An OCR evaluation begins with a corpus that represents the real incoming mix:
scanned PDFs, native PDFs, photographs, tables, rotated pages, multilingual text,
stamps, forms, and damaged scans where applicable. Establish ground truth for a
small but diverse sample. Measure character or word accuracy only where it is
useful, then add field-extraction accuracy, table-cell accuracy, reading order,
block classification, bounding-box overlap, and human correction minutes per
page. A neat-looking Markdown transcription is not sufficient evidence that
numbers, headers, tables, or coordinates are reliable.

Use a two-stage workflow for high-consequence documents. First extract and keep
page/provenance data. Then validate fields with domain rules: dates parse, totals
reconcile, IDs match checksums, and required fields are present. Route uncertain
or contradictory fields to human review. Do not let an LLM "repair" a missing
number without recording that it is inference rather than OCR output.

Cost should be evaluated per accepted document, not merely per page. Include
preprocessing, retries, annotation mode, downstream parsing, storage, privacy
review, human correction, and the loss from an undetected error. Keep private
documents within approved data-handling boundaries and confirm the current
provider terms before uploading regulated or sensitive material.

### Voxtral TTS: Speech Quality, Consent, and Deployment Are Separate Decisions

The [Voxtral TTS card](https://docs.mistral.ai/models/model-cards/voxtral-tts-26-03)
lists an open v26.03 model, `voxtral-mini-tts-2603`, nine languages, zero-shot
voice cloning, streaming with approximately 90 ms time-to-first-audio, and no
transcript required for voice prompts. The current Mistral selection view lists
CC BY-NC 4.0 and 4B parameters, while the pricing page lists hosted generation
costs. Treat latency, language support, cloning, and pricing as current product
facts to recheck before deployment; they are not permission to imitate people
or create misleading audio.

A speech benchmark should separate intelligibility from preference. Prepare an
original script with names, numbers, abbreviations, domain terms, punctuation,
language switches, and emotional but non-deceptive delivery directions. Have
reviewers score word errors, number errors, pronunciation, prosody, pacing,
latency, clipping, and consistency across repeated output. For a streaming
system, measure time-to-first-audio, interruption behavior, audio continuity,
and tail latency independently.

Voice adaptation needs a documented consent path. Confirm that the speaker owns
or has authorized the source recording, explain the intended use, keep source
audio access controlled, and prevent a copied voice from being presented as a
live recording or person endorsement. Do not use a public figure, colleague, or
customer voice merely because a technical feature can accept it. Watermarking,
provenance, and voice-identity restrictions remain unknown unless documented by
the chosen surface.

### Leanstral 1.5: Treat the Compiler as the Evaluator

The [Leanstral 1.5 model card](https://docs.mistral.ai/models/model-cards/leanstral-1-5)
describes a Labs model for Lean 4 automated theorem proving and autoformalization.
It lists `labs-leanstral-1-5`, 119B total parameters, 6.5B active parameters,
256K context, and a listed zero price. The prior Leanstral card is retired in
favor of 1.5. These facts do not establish a general mathematical-reasoning rank,
a guaranteed proof success rate, local weight availability, or a right to run an
unreviewed proof in a safety-critical system.

The primary outcome is a valid compiled proof in a pinned Lean project. An
evaluation should record repository commit, Lean/compiler version, imports,
theorem statement, initial context, model configuration, number of attempts,
tool output, final proof file, and exact compilation command. Measure first-pass
compile success, success after bounded repair, unsupported-library hallucination,
time to proof, and human edits. A fluent explanation with an invalid term is a
failure, however mathematically plausible it sounds.

Keep proof search scoped. Give the theorem, known lemmas, permitted imports,
naming conventions, desired proof style, and a command that checks the artifact.
When autoformalizing natural language, separate the question "did the formal
statement faithfully represent the intended mathematics?" from "does Lean accept
the proof?" Both must be reviewed. Compiling an unintended theorem is not a
successful formalization.

### Robostral Navigate: An Announcement Is Not a Production Contract

Mistral's [news index](https://mistral.ai/news/) records the 2026-07-08
announcement of Robostral Navigate as its first model built for embodied
navigation. The public material reviewed for this guide does not establish a
model identifier, public API, license, weight download, output action schema,
simulation interface, supported robot hardware, pricing, rate limit, or safety
operating procedure. Those omissions are material, so they remain unknown.

The correct current use of this entry is a research watchlist and an evaluation
design, not a deployment recipe. A future navigation assessment should separate
visual scene understanding, map interpretation, high-level route planning,
action selection, low-level control, collision avoidance, recovery, and operator
override. Success in one layer does not prove success in another. Simulated
navigation should record world version, sensor noise, latency, action space,
success definition, collision policy, and failure recovery before any claim is
made about physical transfer.

No model output should directly control a physical robot without an independent
safety layer, hardware limits, emergency stop, operator authority, monitoring,
and staged validation. The difference between "suggest a route" and "send a
motor command" is an engineering and safety boundary, not a wording detail.

### Gemma 4: Open Weights Shift Responsibility to the Builder

Google's [Gemma 4 overview](https://ai.google.dev/gemma/docs/core) says the
family is provided with open weights for responsible commercial use. It lists
E2B, E4B, 12B, 26B A4B, and 31B variants, configurable thinking modes,
function-calling support, native system-role support, and a mix of text, image,
video, and audio inputs that varies by variant. It also gives 128K context for
small models and 256K for medium models. Gemma is distinct from hosted Gemini:
the builder selects the weights, runtime, quantization, system prompt, tools,
monitoring, and data boundary.

The published memory table illustrates why a model-selection decision is also a
systems decision. Approximate 4-bit memory requirements range from 2.9 GB for
E2B to 17.5 GB for 31B, with the 26B A4B entry at 14.4 GB; actual requirements
change with runtime, context, batch size, cache, and overhead. Use these figures
for early capacity planning, not as a promise that a laptop will serve a given
workload with acceptable latency.

Evaluate Gemma variants across three layers. First validate the base model on
the task with a frozen prompt and representative data. Then validate the runtime
and quantization, including throughput, memory pressure, numerical regressions,
and context behavior. Finally validate the application wrapper: system prompts,
retrieval, tool schemas, filters, logging, and permission gates. A failure at
the wrapper layer should not be reported as a model comparison without that
context.

### DiffusionGemma: A Different Generation Process, Not an Automatic Upgrade

Google's [DiffusionGemma model card](https://ai.google.dev/gemma/docs/diffusiongemma/model_card)
labels the model Apache 2.0 and documents a 25.2B-total/3.8B-active MoE design,
discrete text diffusion, up to 256K context, and 256-token canvases. Its launch
material describes a low-latency research role and warns that standard Gemma 4
remains the production-quality recommendation where output quality is primary.
That distinction should guide evaluation: this is not simply Gemma 4 with a
faster name.

The operational idea is blockwise iterative denoising rather than only a
left-to-right token stream. That can change latency, correction behavior, and
the kinds of local editing experiments worth testing. It also changes failure
analysis. Measure time-to-first-useful output, end-to-end latency, block-boundary
coherence, editing quality, long-form consistency, hardware utilization, and
quality against an agreed rubric. Do not infer a universal speedup from a vendor
claim on different hardware, precision, batch size, or workload.

For local experiments, pin the exact artifact and inference stack, document the
GPU/accelerator and precision, run a small safety and quality suite, and compare
against an autoregressive baseline under the same constraints. Use the model's
open status to improve reproducibility, not to remove privacy, safety, or
evaluation obligations.

### Veo 3.1 Lite Preview: Video Is a Sequence, Not a Single Frame

Google's [Veo 3.1 Lite Preview page](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview)
identifies `veo-3.1-lite-generate-preview`, text/image input, video-with-audio
output, a 1,024-token text-input limit, and one output video per request. The
page calls it high-efficiency and developer-first, but explicitly says it does
not support 4K output or Extension. It is a preview model: a working prototype
should retain the identifier, date, region/account condition, and observed
limits rather than assuming permanent production behavior.

Write a video brief in layers: subject and action, camera/framing, location and
time, visual continuity requirements, audio requirements, prohibited elements,
and the intended review rubric. Reference images should be rights-cleared and
their role stated: identity, composition, palette, object layout, or mood. Do
not expect an unmentioned attribute to stay fixed across edits merely because it
appeared in the first generation.

Evaluate temporal behavior, not just a still frame. Review prompt adherence,
motion plausibility, object persistence, scene transitions, lip/audio alignment
where relevant, visual artifacts, edit continuity, latency, price, and
provenance. Save original outputs and prompts. Compressed social clips can hide
frame artifacts and make comparisons misleading. Preview limitations should be
tested explicitly, never worked around by undocumented assumptions.

### Lyria 3: Music Generation Needs Musical and Rights-Aware Evaluation

The current [Lyria 3 guide](https://ai.google.dev/gemini-api/docs/music-generation)
documents two preview identifiers: `lyria-3-clip-preview` for 30-second clips
and `lyria-3-pro-preview` for longer songs. It says the models accept text and
image input and produce MP3 stereo audio, supports lyrics and structural output,
and uses the Interactions API. The current guide reports 44.1 kHz stereo audio;
the repository retains the older changelog's 48 kHz statement as an unresolved
official-source conflict rather than choosing a convenient number.

Use an original brief rather than copyrighted lyrics or a living artist's exact
style. State instrumental versus vocal intent, language, mood, tempo range,
instrumentation, structure, duration, and any text that must be pronounced. A
prompt in a target language can be used to request that language's lyrics, but
the generated words should be reviewed for intelligibility and appropriateness
before publication.

Score musical structure, chord/rhythm consistency, vocal intelligibility,
instrument balance, prompt adherence, repetition, transition quality, long-form
coherence, edit continuity, and rights/provenance obligations. Keep clip and
long-song results separate. A 30-second loop may excel at texture while telling
little about verse/chorus continuity. Check the live pricing, commercial terms,
and safety policy before a public or paid release.

### Gemini Robotics-ER 1.6: High-Level Embodied Reasoning, Not Motor Authority

Google's [Robotics-ER 1.6 guide](https://ai.google.dev/gemini-api/docs/robotics-overview)
documents preview identifier `gemini-robotics-er-1.6-preview`, multimodal input,
text output, spatial understanding, task decomposition, structured outputs, tool
use, and a configurable thinking budget. The current API page lists 131,072
input and 65,536 output tokens; its model card uses rounded 128K/64K figures.
The guide uses the current API page for integration planning and keeps the
discrepancy visible.

The model can be asked to identify objects, reason about relationships, sequence
high-level subtasks, call user-provided functions, or assist a robot controller.
Those are not the same as direct safe actuation. The controller must enforce
action limits, collision handling, sensor validation, stop behavior, operator
approval, and recovery. A function call is only a request until the host accepts
and safely executes it.

Design evaluations in layers. For perception, test object identity, location,
counting, and instrument/gauge reading with ground truth. For planning, test
constraint satisfaction, ordering, uncertainty reporting, and recovery from
missing objects. For tool use, test schema validity, authorization, timeouts,
and side-effect handling. For physical transfer, test only after simulation and
supervised trials, and log environment, sensor stream, model version, thinking
budget, operator decisions, near misses, and interventions.

Google explicitly warns that physical robots can cause damage and that safety
remains the user's responsibility. Do not deploy this preview model in
safety-critical work or represent its visual/spatial reasoning as a certification
of physical reliability.

### Gemini 3.5 Pro: Keep the Watchlist Useful Without Pretending It Is Released

The current [Google DeepMind Gemini page](https://deepmind.google/models/gemini/)
says only "3.5 Pro coming soon." This is enough to preserve a watchlist entry,
but it is not enough to create an API recipe, price table, context claim, effort
menu, tool matrix, or benchmark comparison. The absence of those details is the
current state of the research, not a gap to fill by pattern-matching Flash or
3.1 Pro identifiers.

Recheck this entry only when Google publishes a model page or catalog listing,
a public/restricted identifier, documented availability, and access instructions.
At that point, record release date, surface, region/plan limits, modalities,
context/output limits, tools, reasoning controls, pricing, safety material, and
benchmark methodology separately. Until then, do not let a consumer UI rumor or
a third-party list silently convert the watchlist into a product recommendation.

## Grok 4.5 in Grok Build

Grok 4.5 is the default Grok Build model. SpaceXAI documents low, medium, and
high reasoning, with high as the default. Base API pricing is $2 per million
input tokens and $6 per million output tokens. Artificial Analysis reports
that long inputs above 200K double those costs. That threshold is independent
benchmark reporting rather than a value reproduced in this guide from the
current xAI price table, so production users should check the live xAI pricing
page before deployment.

Grok Build is the agent harness around the model. Its documented workflow can
search a repository, edit multiple files, run terminal commands and tests,
inspect Git state, recover after a failed command, and delegate work to
subagents. xAI also documents live web and X-search tools. Those capabilities
change the product result: a capable model can still fail if the harness loses
command output, applies an unsafe patch, or never runs the right test. A good
Grok Build prompt therefore names the repository root, files in scope, commands
to run, failure-recovery rule, and final evidence required.

In Artificial Analysis, Grok 4.5 High scores 54 on Intelligence Index v4.1 and
76 in the Grok Build coding-agent harness. Its coding result trails Sol Max by
four points, Terra Max and Fable Max with fallback by one, leads Luna Max by
one, and leads Opus 4.8 Max in Claude Code by three in this dated composite.
Its published task cost is much lower than Sol, Fable, or Opus. Those gaps do
not make Grok universally better or worse: repository languages, terminal
recovery, live-search needs, safety policy, latency, and harness behavior can
reverse the practical ranking. The xAI launch post also publishes strong coding
results, but those charts remain vendor evidence rather than independent
confirmation.

[![Watch a 27-minute Grok 4.5 coding test](https://i.ytimg.com/vi/5J6HCDEkg64/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#grok-4-5-test)

*Third-party test by ForrestKnight. The cited xAI and Artificial Analysis
pages remain the authority for availability and measured scores.*

## Artificial Analysis: What the Scores Do and Do Not Mean

![Artificial Analysis Intelligence and Coding Agent Index snapshot](../assets/model-guides/aa-frontier-benchmark-2026-07-11.svg)

### Intelligence Index v4.1

The current composite covers GDPval-AA v2, tau3-Banking, Terminal-Bench v2.1,
SciCode, Humanity's Last Exam, GPQA Diamond, CritPt, AA-Omniscience, and
AA-LCR. It blends professional work, tool use, coding, science, knowledge,
physics, hallucination resistance, and long-context reasoning.

The components answer different questions. GDPval-AA tests valuable
professional work. GPQA Diamond, CritPt, and SciCode emphasize graduate-level
science, physics, and scientific coding. Humanity's Last Exam targets difficult
broad knowledge and reasoning. AA-Omniscience measures both correct answers and
appropriate uncertainty rather than rewarding confident guessing. AA-LCR probes
long-context retrieval and reasoning. A composite can rise because of strength
in one cluster while hiding weakness in another, so the subtests should be
matched to the intended workload.

The July launch snapshot puts Fable 5 Max with fallback at 59.9, Sol Max at
58.9, Opus 4.8 Max at 55.7, Terra Max at 55, Grok 4.5 High at 54, Luna Max at
51.2, Muse Spark 1.1 xhigh at 51, and Gemini 3.5 Flash High at 50.2. A one-point
gap in a composite should not be treated as a universal practical difference.

### Coding Agent Index

The coding composite pairs models with an agent harness and averages DeepSWE,
Terminal-Bench v2, and SWE-Atlas-QnA. The current comparison shows:

| Model and harness | Index | Cost/task | Time/task | Important qualifier |
| --- | ---: | ---: | ---: | --- |
| GPT-5.6 Sol Max in Codex | 80 | $7.08 | 10.2 min | Max, not Ultra |
| GPT-5.6 Terra Max in Codex | 77 | $2.76 | 8.4 min | Same composite, cheaper tier |
| Fable 5 Max in Claude Code | 77 | $11.75 | 23.5 min | Includes production fallback |
| Grok 4.5 High in Grok Build | 76 | about $2.49 | See live comparison | Different harness |
| GPT-5.6 Luna Max in Codex | 75 | $1.57 | 8.0 min | Lowest-cost GPT-5.6 result shown |
| Opus 4.8 Max in Claude Code | 73 | $7.70 | 23.1 min | No Fable fallback layer |

Harness choice affects tools, permissions, caching, prompt scaffolding, turns,
and orchestration. The Coding Agent Index is closer to a product workflow test
than a bare model exam. The repository keeps the harness name beside every
score for that reason.

The three coding components also reward different behavior. DeepSWE measures
software-engineering issue resolution, Terminal-Bench v2 exercises interactive
terminal operation, and SWE-Atlas-QnA tests repository understanding through
questions and answers. Artificial Analysis reports Sol at 69, 88, and 84 on
those three components; Terra at 67, 84, and 81; and Luna at 63, 80, and 81 in
the cited GPT-5.6 article. Those figures belong to the tested Codex
configurations. They should not be copied onto API calls or other agent
harnesses.

Cost per task, tokens used, and time per task are part of the engineering
decision. A higher index with twice the cost may still be right for a rare
high-stakes repair, while a slightly lower model can be better for thousands of
bounded tasks. Time is also harness-sensitive: parallel tool calls, command
latency, caching, retry policy, and fallback can all move it. No independent
Sol Ultra Coding Agent Index result is cited here, so the Sol Max result must
not be presented as an Ultra score.

### AA-Briefcase and Other Useful Views

AA-Briefcase tests long-horizon knowledge work and finished artifacts. Fable 5
Max leads the cited comparison with a 56% rubric score and 1764 Analytical
Quality Elo. Sol Max records a 42% rubric score and 1592 Analytical Quality Elo,
but leads Presentation Elo. That split is useful: factual and analytical task
completion is not the same measure as visual polish.

Artificial Analysis also publishes GDPval-AA v2, AA-Omniscience, AA-LCR,
agentic, legal, finance, automation, enterprise-operations, image, video, and
speech evaluations. Choose the view that matches the work. A coding index is a
poor way to select a translation model, and an image preference Elo is a poor
way to choose a repository agent.

AA-Briefcase separates rubric completion from Analytical Quality Elo and
Presentation Elo. The first asks whether required work was done, the second
compares reasoning and analysis, and the third compares the finished artifact's
presentation. That separation explains how one model can lead analytical work
while another produces a more polished-looking deliverable. None of those
measures alone captures reliability, safeguards, or user happiness. Those need
repeated task success, correction burden, refusal quality, and user studies.

## Meta Muse Spark 1.1

Meta describes Muse Spark 1.1 as a multimodal reasoning model for agentic work,
computer use, coding, and multimodal understanding. It is available in
Thinking mode in Meta AI and through the Meta Model API public preview. The
official product claim covers multimodal reasoning and action-oriented work;
it does not mean that every API client supplies a repository editor, browser,
or computer-control harness automatically.

Artificial Analysis reports Muse Spark 1.1 xhigh at 51 on Intelligence Index
v4.1, 116.3 output tokens per second, a 1M context window, and Meta API pricing
of $1.25/$4.25 per million input/output tokens. Its 51-point composite matches
the rounded Luna Max score but does not establish equal behavior in Codex,
computer use, or any specific repository task.

At those reported rates and throughput, Muse is positioned as a lower-cost,
fast reasoning option. Luna has a nearby rounded Intelligence score and a
measured Codex coding-agent result, Terra scores higher in both the dated
Intelligence and Codex snapshots, Grok adds a different live-search and CLI
harness, and Gemini 3.5 Flash exposes a broader documented developer-tool set.
Those comparisons are directional only. Equal rounded Intelligence values do
not establish equal coding reliability, GUI control, safety behavior, latency,
or repository completion.

[![Watch a 33-minute Muse Spark 1.1 test](https://i.ytimg.com/vi/XCYYDhG9zKw/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#muse-spark-test)

*Third-party test by Bijan Bowen. Meta and Artificial Analysis provide the
factual product and benchmark record.*

## Gemini 3.5 Flash

Gemini 3.5 Flash is Google's stable Flash model for agentic and coding work at
scale. The API uses `minimal`, `low`, `medium`, and `high`, with `medium` as the
default. Google recommends low for lower-latency work, medium for most complex
code and agents, and high for hard reasoning, math, and difficult coding.

Google's developer documentation lists Google Search, Maps, File Search, code
execution, URL Context, function calling, and computer use among the supported
tool paths. Tool availability still depends on the API and client being used;
the model name alone does not grant a browser or computer. The published model
surface supports long context, while useful long-context performance still
depends on retrieval, prompt structure, and tool results. Google described the
release as roughly four times faster than its preceding comparable path at
I/O 2026. That throughput statement is a vendor claim until reproduced under a
matching workload and service tier.

Gemini Apps uses a simpler consumer vocabulary where available:

| Gemini Apps label | Meaning |
| --- | --- |
| Standard thinking | Faster default for most questions |
| Extended thinking | More reasoning for complex problem solving |
| Deep Think | Separate Pro-model parallel reasoning for eligible AI Ultra use, not a Flash effort label |

Google's API and consumer labels should not be mixed. Standard and Extended
are interface choices. Minimal through High are developer controls. Deep Think
is not “Gemini 3.5 Flash Max.”

Artificial Analysis scores Gemini 3.5 Flash High at 50.2 on Intelligence Index
v4.1. Google's launch material reports 76.2% on Terminal-Bench 2.1, 1656 Elo on
GDPval-AA, and 83.6% on MCP Atlas, but those launch figures remain vendor
evidence unless independently reproduced under the same conditions.

Against GPT-5.6 Luna and Terra, Flash is not simply a midpoint on one ladder.
Luna and Terra have lower-level integration in Codex and measured Coding Agent
Index configurations; Gemini has its own API tools, consumer labels, pricing,
throughput, and Google product integrations. Choose by running the same coding
or agent task with equivalent tools, prompts, time limits, and correction
rules. Do not compare Google's vendor Terminal-Bench number directly with an
Artificial Analysis harness score as if the procedures were identical.

[![Watch a long Gemini 3.5 Flash coding test](https://i.ytimg.com/vi/TdN-YdFLWvY/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gemini-3-5-flash-test)

*Third-party test by Bijan Bowen. The official Google developer pages define
the model controls and supported tools.*

## GPT-Live-1 and Gemini 3.5 Live Translate

These systems both process streaming audio, but they solve different jobs.

### GPT-Live-1 and GPT-Live-1 Mini

GPT-Live is a conversational architecture. OpenAI says it continuously
processes input while generating output, can listen and speak at the same
time, and makes interaction decisions many times per second about speaking,
listening, pausing, interrupting, and using tools. That full-duplex loop is
designed to reduce the rigid turn-taking of older voice pipelines. Deeper
search or reasoning can be delegated to a stronger text model while the live
model maintains the conversation. These are official architectural
descriptions, not an independent reverse-engineering result, and a user-
interface animation does not disclose internal implementation.

OpenAI positions GPT-Live-1 for paid Go, Plus, and Pro users and GPT-Live-1
Mini for the free path. At launch, GPT-Live-1 Instant and Mini can use a fast
background model, while Medium and High route deeper work through the current
thinking model described by OpenAI. That delegation is distinct from the live
speech loop itself. The launch does not establish one fixed end-to-end latency:
network quality, speech length, tool calls, background reasoning, and
interruptions all affect response time.

Full duplex creates new failure modes. The system must distinguish a real
interruption from a cough or background speaker, respect a request to wait,
avoid answering during a thoughtful pause, and recover when two people speak
at once. OpenAI notes that transcripts may not be verbatim and that overlap,
background noise, and fast conversation can reduce stability. Independent
tests should therefore measure recognition accuracy, interruption success,
false starts, pause handling, translation continuity, tool-delegation latency,
and whether the spoken answer matches the visible transcript.

Safety and privacy are part of the product, not afterthoughts. OpenAI describes
voice-native safety training, real-time steering, predefined voices, and limits
on impersonation. Users should also account for microphone capture, transcript
and memory settings, web search, connected tools, regional policy, and the fact
that playing remote media or using live services sends data to the provider.

### Gemini 3.5 Flash Live Translate

Gemini 3.5 Flash Live Translate is a translation-specialized interpreter path.
The public-preview model ID is `gemini-3.5-live-translate-preview`. It accepts
audio input, emits translated audio plus optional transcripts, supports more
than 70 languages, and does not support tool calling, search grounding,
function calling, system instructions, or reasoning/thinking controls. Google
recommends 16 kHz mono PCM input, 24 kHz PCM output, and approximately 100 ms
input chunks.

For a consumer trial, Google says to open the Google Translate app on Android
or iOS, connect headphones, and choose Live translate. For a developer trial,
use the Google AI Studio Live Translate demo or connect through the Gemini Live
API with a target BCP-47 language code. The preview label matters: supported
behavior, quotas, and quality can change before a stable release.

An Arabic-English evaluation should test both directions with names, numbers,
technical vocabulary, dialect changes, emotional tone, interruptions, long
pauses, and overlapping speakers. It should record whether the system performs
continuous simultaneous translation or waits for turn boundaries, and whether
meaning, tone, and proper nouns survive. This is a recommended test protocol,
not a claim that the checked guide independently ran those trials.

GPT-Live-1 and Live Translate should not be ranked as identical products.
GPT-Live is a general conversational system with tools and delegated reasoning;
Live Translate is a narrower audio-to-audio translation model with predictable
language routing and no tool or thinking controls. The right comparison is
task-specific latency, speech accuracy, interruption behavior, tone retention,
privacy, and stability under the same audio conditions.

[![Watch OpenAI's GPT-Live demonstration](https://i.ytimg.com/vi/EAN5Cj347PY/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-live-official)

*Official OpenAI demonstration. The Google Live Translate guide links its own
AI Studio demo and product videos in the sources below.*

## Image and Video Models

![Current live-audio, image, and video model map](../assets/model-guides/multimodal-model-map-2026.svg)

### GPT Image 2

OpenAI documents GPT Image 2 as its state-of-the-art image generation and
editing model with text and image input, image output, flexible sizes, and
high-fidelity image inputs. It is available through the Images API and image
generation tool paths. The product documentation emphasizes typography,
prompt adherence, precise editing, and reference consistency, but those are
capabilities to evaluate with full-resolution outputs rather than guarantees
for every prompt.

The claim that GPT Image 2 is a “reasoning-integrated fully autoregressive
image model that reasons like a Transformer” is **unconfirmed**. The checked
OpenAI model and image guides do not publish that internal architecture. An
autoregressive image-token model would predict image tokens sequentially;
diffusion and latent diffusion iteratively denoise pixels or latent features.
A separate planning stage could reason before generation, while hidden prompt
rewriting could improve prompts without changing the generator architecture.
An interface “thinking” indicator could represent any of those product steps.
Observed behavior cannot identify which mechanism is used. Until OpenAI
publishes a technical source, the guide records the disclosed inputs, outputs,
controls, and quality goals, and marks architecture as undisclosed.

### Nano Banana 2, Nano Banana Pro, and Nano Banana 2 Lite

The official mapping is:

| Product name | Model ID | Role |
| --- | --- | --- |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | Fastest and cheapest, high-volume generation |
| Nano Banana 2 | `gemini-3.1-flash-image` | General-purpose balance of quality, speed, 4K, and editing |
| Nano Banana Pro | `gemini-3-pro-image` | Highest control, world knowledge, localization, and professional use |
| Original Nano Banana | `gemini-2.5-flash-image` | Legacy model Google recommends replacing |

Nano Banana 2 is not Gemini 3 Pro Image. Nano Banana Pro is Gemini 3 Pro Image.

#### Nano Banana 2

Nano Banana 2, officially Gemini 3.1 Flash Image, is the general-purpose path.
Google documents fast generation, search-grounded current knowledge, text
rendering, subject consistency, image editing, reference-image input, and
resolutions up to 4K. Thinking controls are available where the model and API
surface document them. Search and thinking should still be recorded in any
test because enabling them can change latency, cost, and output.

#### Nano Banana Pro

Nano Banana Pro, officially Gemini 3 Pro Image, targets higher-control
professional work. Google emphasizes world knowledge, localization,
typography, complex layouts, and production control. It should be compared
with Nano Banana 2 on the same brief and editable output requirements rather
than treated as a renamed version of the Flash model.

#### Nano Banana 2 Lite

Nano Banana 2 Lite, officially Gemini 3.1 Flash Lite Image, trades capability
for lower latency and price. Google positions it for iteration, brainstorming,
and high-volume use, with an approximately four-second generation target in
the official launch material. The same source warns that it is not optimized
for many reference images or long sequential editing. Those constraints make
it a draft engine, not an automatic replacement for Pro on complex layouts.

### Seedream 5.0 Pro

ByteDance's Dreamina surface presents Seedream 5.0 Pro as a professional image
generation and editing model. Public English technical documentation is less
detailed than the Google and OpenAI API pages, so claims about internal
reasoning, layer architecture, or web search should be attributed to the
product page and treated as vendor claims until a technical report is public.

This model is suitable for side-by-side evaluation on typography, layout,
reference consistency, targeted editing, and production control. The test set
should use the same prompts, aspect ratios, reference images, and human scoring
rubric across providers. Dreamina advertises text-to-image, image editing,
reference control, typography, production layouts, and prompt adherence. Those
claims should be checked on original full-resolution outputs. Compressed X or
YouTube frames can hide small text errors, edge artifacts, and reference drift.
The limited English first-party technical disclosure does not establish a
particular diffusion, autoregressive, or reasoning architecture.

### Muse Image and Muse Video

Meta launched Muse Image on July 7, 2026 across the Meta AI app and meta.ai,
Instagram Stories in the United States, and WhatsApp in limited countries,
with Facebook support announced as coming later. Meta describes Muse Image as
an agentic image-generation and editing model with search and coding tools,
self-refinement, multi-reference composition, and integration with Muse Spark.
Those tool and quality statements are vendor claims that should be tested on
the actual product surface used.

Muse Image also applies Meta's Content Seal invisible provenance signal to
images created in Meta AI and on meta.ai. A prompt should still state rights,
identity, factual-grounding, and output constraints; watermarking does not make
an unsafe or misleading request acceptable.

Muse Video is an early preview, not a currently available production path in
this snapshot. Meta says it is coming soon and identifies current work on
audio-video synchronization and physically accurate fast motion. The
repository therefore documents research and readiness checks but does not
publish a live production integration template. See the
[Muse Image and Muse Video prompting guide](model-prompting/muse-image-video-prompting.md).

### Image-model videos

[![Watch a GPT Image 2, Nano Banana 2, and Seedream comparison](https://i.ytimg.com/vi/FDhx79PU5KQ/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#image-model-comparison)

*Third-party comparison by Code And Create. Use identical prompts and inspect
the original outputs before accepting any winner claim. This video is an image-
model comparison only; it is not a Gemini Omni Flash demonstration.*

[![Watch OpenAI's 21-minute ChatGPT Images 2.0 introduction](https://i.ytimg.com/vi/sWkGomJ3TLI/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-image-2-official)

*Official OpenAI product demonstration.*

### Gemini Omni Flash

Gemini Omni Flash is a multimodal generative-video system, not an image-model
comparison. Google's preview API model ID is `gemini-omni-flash-preview`. It
can combine text, images, existing video, and prompt-described audio to produce
video with generated audio. Google documents conversational editing through
the Interactions API, including iterative changes intended to preserve
unmentioned parts of a clip. The product material also emphasizes character
and voice consistency, but those remain quality claims to test across multiple
edits and scenes.

Distribution spans the Gemini app, Flow, YouTube creation surfaces, and a paid
Gemini API preview. Google says image and text outputs are planned later; this
guide does not treat those planned outputs as current API capability. The
model page lists 3-to-10-second output at 720p and 24 frames per second, a
1,048,576-token context window, and video input up to 10 seconds for editing.
The detailed API guide also lists current limits: uploaded audio references
are unsupported, multi-video reasoning is unsupported, video extension and
interpolation are unsupported, and voice editing is unsupported. The schema
accepts video references up to three seconds but Google warns that the current model does not
process them correctly. Those are preview limitations, not an invitation to
infer undocumented workarounds.

The video research pack uses precise discovery searches for Gemini Omni Flash
official demos, full tests, Omni-versus-Veo comparisons, and Google I/O 2026.
No unrelated YouTube ID is relabeled as an Omni demonstration.

## Extended Operating Guidance for the Established Families

### GPT-5.6 Sol, Terra, and Luna

The GPT-5.6 family is a tier, effort, and surface decision. Sol is appropriate
when an error is expensive and the task has enough evidence to inspect; Terra is
the default for bounded engineering and research work; Luna is appropriate for
high-volume tasks with deterministic validation. The tier does not replace a
clear work order, and a higher effort does not repair missing context or unclear
authority.

For every family member, write the task in five parts: the observable result,
the allowed evidence and files, the excluded scope, the verification command or
review rubric, and the stop condition. A Sol architecture review should include
alternatives and falsifiers. A Terra repository repair should include tests and
paths. A Luna batch task should include a schema, a gold sample, and handling
for missing values. Record tier, effort, model ID, tool permissions, retries,
cost, latency, and human correction. That record matters more than a model-name
claim when two runs disagree.

Use Ultra only for separable workstreams. Give each worker exclusive ownership,
immutable inputs where possible, an explicit output contract, and a final
integration check. A parallel model run against one shared mutable area can add
duplicated investigation and merge failure without improving correctness. For a
linear diagnosis or a single risky migration, one high-effort agent with a
strong verification gate is usually easier to audit.

### Claude Fable 5 and Claude Opus 4.8

Fable 5's documented fallback behavior must be treated as part of the product
result. Log the chosen effort, visible fallback notice, task type, harness,
tool permissions, and final model identity where it is exposed. A routed run may
be useful but is not a pure Fable measurement. Opus 4.8 remains a useful
Claude-family baseline when that routing distinction would confound evaluation.

For knowledge work, split source extraction from recommendation writing. Give
the model an authority hierarchy, dates, claim ledger, and required uncertainty
section. For coding, require inspect-first behavior, a smallest-hypothesis rule,
a regression test, a focused diff, and a final command result. The model's
reasoning effort changes the search budget; it does not authorize deployment,
secrets, destructive operations, or unsupported tools.

Fable's promotional and usage-credit surfaces should not be collapsed into one
cost number. Record whether the work used a subscription allowance, billed
credits, or the API. Compare successful-task cost including retries, tool calls,
fallbacks, and review effort. A lower nominal rate can be outweighed by a
workflow that fails validation or requires repeated human correction.

### Grok 4.5 and Muse Spark 1.1

Grok Build and Muse Spark deployments are model-plus-harness systems. A coding
result depends on repository state, agent system prompt, terminal permissions,
network/search availability, tool loop, retry policy, and the human reviewer.
Keep those settings beside the model and effort label. Do not transfer an agent
benchmark result to a bare API request or another coding environment.

For Grok Build, define command recovery in advance: capture the failure, restate
the smallest next hypothesis, avoid unrelated cleanup, and stop after a bounded
number of attempts or missing authority. For Muse Spark, separate visual or
multimodal perception from planning, tool-call validity, and final task
completion. A coherent answer can still be grounded in the wrong image region,
call an invalid tool, or leave a repository change untested.

### Gemini 3.5 Flash

Gemini 3.5 Flash exposes developer thinking controls and a broad catalog of
tool paths, but a tool should be enabled only when the task needs it. Every
additional tool affects data handling, latency, cost, failure behavior, and
prompt-injection exposure. Begin with the smallest useful tool set and add a
tool only after an evaluation identifies a specific gap.

Keep consumer labels separate from API values. For an API evaluation, record
model ID, thinking setting, prompt version, source/context selection, tool
schemas, tool results, timeouts, output limits, retries, and the acceptance
result. Use the same tool boundary when comparing against another vendor. A
model that has search, code execution, or computer-use support in one surface
does not give those capabilities to every integration by name alone.

### GPT-Live-1, GPT-Live-1 Mini, and Gemini Live Translate

Live audio models must be tested as streaming systems. A transcript alone cannot
show recognition latency, interruptions, pause handling, overlap behavior, false
starts, spoken-output quality, or whether the voice response actually matches
the visible text. Record microphone, speaker route, client and model version,
network condition, language pair, noise condition, chunking, and end-to-end
latency distribution for every meaningful evaluation.

GPT-Live is a general conversational architecture with documented delegated
reasoning and tool behavior. Design prompts that state when the system should
listen, ask a clarifying question, wait, announce a tool action, and return to a
conversation after an interruption. Gemini Live Translate is narrower: assess
meaning preservation, terminology, proper nouns, tone, dialect shifts, and
simultaneous-turn behavior in both language directions. Do not infer general
web, function, or thinking controls for the translation preview where the
documented surface excludes them.

Privacy is part of the acceptance criteria. Review microphone capture,
transcripts, memory, connected tools, region, and the handling of third-party
voices before testing. In a sensitive setting, use a pre-approved corpus and a
clear consent process. If a translation is ambiguous, retain the original term
or ask for clarification rather than emitting a confident invented equivalent.

### GPT Image 2, Nano Banana, Seedream, and Muse Image

Image systems need separate generation and editing tests. Generation tests
should measure composition, typography, factual visual details, reference use,
prompt adherence, safety, rights, and output resolution. Editing tests should
measure localized change, preservation of unmentioned regions, identity and
reference consistency, mask/selection fidelity, and drift after several edits.
Save original full-resolution outputs, prompt metadata, references, tool settings,
and reviewer decisions; compressed previews conceal the defects that matter in
production.

GPT Image 2's internal architecture remains undisclosed in the checked sources.
Do not infer it from an interface thinking state or output behavior. Nano Banana
Lite, Nano Banana 2, and Nano Banana Pro should be compared on a shared output
contract rather than a family-name ladder: reference count, required text,
localization, aspect ratio, search/grounding choice, thinking configuration,
image-edit sequence, latency, and cost. Seedream claims require the same
full-resolution, rights-aware inspection because its technical disclosure is
more limited. Muse Image's Content Seal is provenance information, not proof of
truth, ownership, safety, or prompt compliance.

### Muse Video, Veo, Lyria, and Gemini Omni Flash

Video evaluation is inherently temporal. Judge motion plausibility, object and
character persistence, scene transitions, editing continuity, audio alignment,
frame artifacts, prompt adherence, latency, provenance, and the rights of every
input asset. Store the original clip, input images, prompt, model identifier,
preview/stable status, resolution, frame rate, duration, and every edit turn.
A visually strong still frame cannot prove that a clip is coherent.

Muse Video remains an announced/coming-soon system in this snapshot, so it has a
readiness checklist rather than a production recipe. Veo 3.1 Lite and Gemini
Omni Flash are preview systems whose published limitations belong in the test
plan. Do not reinterpret unavailable extension, interpolation, audio-reference,
or voice-edit behavior as an undocumented capability. Lyria is music generation,
not a video model: score musical structure, vocal intelligibility, arrangement,
repetition, language, edit continuity, output format, commercial terms, and
artist-style restrictions separately from video criteria.

## How to Choose Without Chasing a Single Winner

The following is an **interpretation** of the cited product controls and dated
evaluations, not a universal ranking:

| Decision area | Evidence to inspect | Practical reading of the current snapshot |
| --- | --- | --- |
| Mathematics and science | GPQA Diamond, CritPt, SciCode, full solution checks | Sol and Fable are strong broad candidates, but subtest and proof verification matter more than the one-point composite gap |
| Engineering and repositories | Coding Agent Index, terminal recovery, tests, diff quality | Sol Max in Codex leads the cited composite; Terra, Grok, Luna, Fable, and Opus trade score, cost, time, and harness behavior differently |
| Open-ended problem solving | Intelligence components, AA-Briefcase, correction burden | Fable leads the cited broad and analytical artifact views; Sol leads the coding composite and Presentation Elo cited here |
| Reliability | Repeated task success, retries, hallucination measures, regression tests | No single published number proves reliability for a private workload |
| Safeguards | Vendor system cards, refusal quality, fallback notices, audit logs | Fable's documented Opus fallback changes model identity; OpenAI and other vendors apply their own controls |
| User happiness | Preference studies, latency, edit burden, trust, predictable access | The checked sources do not provide a universal satisfaction ranking; local user studies are required |

Strengths and weaknesses are therefore conditional. Sol offers the strongest
cited coding-agent result and a broad product surface, but higher efforts and
Ultra can cost more and add coordination. Terra and Luna lower cost and latency
but have less headroom on the cited composites. Fable leads the dated broad
index and analytical artifact view, but is expensive and its fallback weakens
pure model comparisons. Opus is a more stable Claude baseline but trails Fable
and the GPT-5.6 coding configurations in the cited composite. Grok is
cost-efficient and search-aware in Grok Build, while its harness and safety
behavior must be tested for the intended repository. Muse and Gemini offer
different multimodal, throughput, and tool integrations that the coding table
does not capture.

For repository completion, start with the coding-agent index and then run your
own representative tasks. Sol Max currently has the strongest cited composite.
Terra and Luna offer lower task cost. Fable remains strong on long-horizon work
and AA-Briefcase but is more expensive and includes a fallback path. Grok 4.5
offers a strong cost-performance point in Grok Build. Opus 4.8 remains a useful
Claude baseline without the Fable safeguard layer.

For math and science, inspect GPQA, CritPt, SciCode, and task-specific error
analysis. A composite can hide a model that is excellent at one scientific
domain and weaker at another.

For professional documents, inspect AA-Briefcase rubric score, Analytical
Quality Elo, Presentation Elo, citation accuracy, and editability. A polished
slide deck can still contain a weak conclusion.

For live voice, choose a conversational full-duplex model when interaction and
tool delegation matter. Choose a translation model when the job is continuous
speech translation with predictable language routing.

For images, compare prompt adherence, typography, reference consistency,
editing precision, latency, price, resolution, safety policy, provenance
marking, and commercial terms. A blind preference leaderboard alone does not
measure whether a diagram is factually correct.

## Uncertainties and Known Limits

- Work and Codex UI menus can differ by plan, workspace policy, app version,
  region, and staged rollout. The local Codex catalog is evidence for this
  machine on the checked date, not every account.
- OpenAI's public pages confirm Work models and Max/Ultra eligibility but do
  not enumerate every lower Work label on every surface.
- Artificial Analysis pages are live and can update. The local charts preserve
  the checked date, benchmark version, model effort, harness, and fallback.
- Fable scores include the production Opus 4.8 fallback where Artificial
  Analysis labels it that way.
- Anthropic's promotional-access terms extend Fable 5 subscription access through
  July 19, 2026 at 11:59:59 PM PT, and the linked Claude Code promotion extends
  the 50% weekly-limit increase through the same date. Recheck the live terms
  before purchase or deployment decisions because promotional conditions can
  change.
- No independent source cited here tests Sol Ultra against Fable Max. Ultra is
  orchestration, while the benchmark uses Sol Max.
- GPT Image 2's claimed fully autoregressive architecture is not established in
  the checked OpenAI documentation.
- Seedream 5.0 Pro has limited English first-party technical disclosure.
- Muse Video is announced as coming soon; no available production surface or
  stable integration limits were confirmed for this snapshot.
- Gemini 3.5 Pro is officially described as coming soon, but Google has not
  provided a usable model surface, identifier, or access instructions.
- Robostral Navigate has an official announcement but no public API identifier,
  pricing, weights, operating terms, or hardware requirements in the sources
  reviewed here.
- Lyria 3's current generation guide says 44.1 kHz, while its March 25 API
  changelog says 48 kHz. The conflict is unresolved; verify the live API output
  format before setting a production audio contract.
- The current Robotics-ER API page lists 131,072/65,536 input/output tokens,
  while the April model card uses 128K/64K. The guide follows the newer API page
  for integration planning.
- Third-party videos are qualitative context. They are not the factual source
  for pricing, access, architecture, or benchmark scores.

## Sources

Primary sources, accessed 2026-07-11 unless noted:

- [OpenAI: GPT-5.6 launch](https://openai.com/index/gpt-5-6/), published 2026-07-09.
- [OpenAI Help: GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt).
- [OpenAI Help: ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275/).
- [OpenAI Help: ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers).
- [OpenAI API model catalog](https://developers.openai.com/api/docs/models).
- [OpenAI API: GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra).
- [OpenAI: Introducing GPT-Live](https://openai.com/index/introducing-gpt-live/), published 2026-07-08.
- [OpenAI Help: GPT-Live in ChatGPT](https://help.openai.com/en/articles/20001274/).
- [OpenAI: GPT-Live system card](https://deploymentsafety.openai.com/gpt-live).
- [OpenAI API: GPT Image 2](https://developers.openai.com/api/docs/models/gpt-image-2).
- [Anthropic: Claude Fable 5 and Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5).
- [Anthropic Help: Fable 5 promotional access](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access).
- [Anthropic API: effort controls](https://platform.claude.com/docs/en/build-with-claude/effort).
- [Anthropic API: pricing](https://platform.claude.com/docs/en/about-claude/pricing).
- [Anthropic: Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5), published 2026-06-30, accessed 2026-07-12.
- [DeepSeek: V4 Preview release](https://api-docs.deepseek.com/news/news260424/), published 2026-04-24, accessed 2026-07-12.
- [DeepSeek: models and pricing](https://api-docs.deepseek.com/quick_start/pricing/), accessed 2026-07-12.
- [Z.ai: GLM-5.2](https://z.ai/blog/glm-5.2), published 2026-06-16, accessed 2026-07-12.
- [Mistral: Mistral Medium 3.5 model card](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04), accessed 2026-07-12.
- [Mistral: Mistral Small 4 model card](https://docs.mistral.ai/models/model-cards/mistral-small-4-0-26-03), published 2026-03-16, accessed 2026-07-12.
- [Mistral: OCR 4 model card](https://docs.mistral.ai/models/model-cards/ocr-4-0), published 2026-06-23, accessed 2026-07-12.
- [Mistral: Voxtral TTS model card](https://docs.mistral.ai/models/model-cards/voxtral-tts-26-03), published 2026-03-23, accessed 2026-07-12.
- [Mistral: Leanstral 1.5 model card](https://docs.mistral.ai/models/model-cards/leanstral-1-5), published 2026-06-30, accessed 2026-07-12.
- [Mistral: model pricing and catalog](https://mistral.ai/pricing/api/), accessed 2026-07-12.
- [Mistral: latest news](https://mistral.ai/news/), accessed 2026-07-12; establishes the Robostral Navigate announcement dated 2026-07-08.
- [SpaceXAI: Introducing Grok 4.5](https://x.ai/news/grok-4-5).
- [SpaceXAI Docs: Grok 4.5](https://docs.x.ai/developers/grok-4-5).
- [SpaceXAI: Grok Build CLI](https://x.ai/cli).
- [SpaceXAI: Grok Build changelog](https://x.ai/build/changelog).
- [Meta: Introducing Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/).
- [Meta: Introducing Muse Image and Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), accessed 2026-07-12.
- [Google: Gemini 3.5 Flash changes](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5).
- [Google Gemini Apps Help: thinking levels](https://support.google.com/gemini/answer/16275805?hl=en).
- [Google: Live translation with Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api/live-translate).
- [Google: Gemini 3.5 Live Translate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/).
- [Google: Nano Banana image generation](https://ai.google.dev/gemini-api/docs/image-generation).
- [Google: Nano Banana 2](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/).
- [Google: Nano Banana 2 Lite and Gemini Omni Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/).
- [Google: Nano Banana Pro](https://blog.google/innovation-and-ai/products/nano-banana-pro/).
- [Google: Gemini Omni Flash API guide](https://ai.google.dev/gemini-api/docs/omni).
- [Google: Gemini Omni Flash model page](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash).
- [Google: Gemini Omni Flash and Flow](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates/).
- [Google AI for Developers: Gemma 4 overview](https://ai.google.dev/gemma/docs/core), accessed 2026-07-12.
- [Google AI for Developers: DiffusionGemma model card](https://ai.google.dev/gemma/docs/diffusiongemma/model_card), accessed 2026-07-12.
- [Google: Introducing DiffusionGemma](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/), published 2026-06-10, accessed 2026-07-12.
- [Google AI for Developers: Veo 3.1 Lite Preview](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview), accessed 2026-07-12.
- [Google AI for Developers: Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation), accessed 2026-07-12.
- [Google Gemini API changelog](https://ai.google.dev/gemini-api/docs/changelog), accessed 2026-07-12.
- [Google AI for Developers: Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview), accessed 2026-07-12.
- [Google DeepMind: Gemini 3.5](https://deepmind.google/models/gemini/), accessed 2026-07-12.
- [ByteDance Dreamina: Seedream 5.0 Pro](https://dreamina.capcut.com/seedream/seedream-5-0-pro).

Independent sources, accessed 2026-07-11:

- [Artificial Analysis: GPT-5.6 benchmarks](https://artificialanalysis.ai/articles/gpt-5-6-has-landed).
- [Artificial Analysis: Claude Code versus Codex](https://artificialanalysis.ai/agents/coding-agents/comparisons/claude-code-vs-codex).
- [Artificial Analysis: Grok 4.5](https://artificialanalysis.ai/articles/grok-4-5-brings-spacexai-to-the-the-intelligence-frontier).
- [Artificial Analysis: Muse Spark 1.1](https://artificialanalysis.ai/models/muse-spark-1-1).
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index).
- [Artificial Analysis coding-agent comparisons](https://artificialanalysis.ai/agents/coding-agents/comparisons).
- [Artificial Analysis: AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase).

## Method

Official sources establish names, product controls, rollout, pricing, and
vendor-described architecture. Artificial Analysis supplies independent model
and harness results. The local Codex catalog was queried through `codex debug
models` and filtered to the three GPT-5.6 model IDs. Videos were checked with
`yt-dlp`; every embedded selection was public and reported
`playable_in_embed=True` on the checked date. Original SVGs reproduce values
and relationships, not third-party chart artwork.

The [video research pack](../research/video-research-pack-2026-07-11.md)
records verified titles, channels, upload dates, roles, and limitations. It
also keeps discovery searches separate so an unverified result cannot silently
become evidence.
