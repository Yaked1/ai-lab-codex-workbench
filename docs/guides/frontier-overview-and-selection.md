# Frontier overview and selection

[← Frontier models index](frontier-models-and-multimodal-systems-2026.md)

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

## Announcement-Style Release Dossiers
This section rewrites the model catalog in the form of substantive launch dossiers. Each entry
combines the announcement story, product positioning, disclosed architecture, capabilities,
benchmark and result interpretation, access and economics, deployment consequences, limitations,
and a practical verdict. It deliberately refuses the most common release-post trick: presenting
an undisclosed field as though confident adjectives were a technical specification.

The entries are not substitutes for the later architecture tables. They are the narrative layer
that explains why a release exists, what changed relative to the preceding market, which results
matter, and what a builder should actually measure. Vendor benchmark claims are labeled in the
prose; independent numbers retain their evaluator and harness; preview systems retain their
preview status; unreleased systems remain watchlist entries.

### How to read each release dossier

| Block | Purpose |
| --- | --- |
| Release card | Exact identity, status, role, interface, context, price, weights, and architecture disclosure |
| Launch story | What the vendor is claiming changed and why the model exists |
| Capabilities | Concrete task and tool surface rather than broad adjectives |
| Benchmarks and results | Vendor claims, independent measurements, harness effects, and non-comparable rows |
| Deployment and evaluation | What must be recorded to reproduce or purchase intelligently |
| Limits and unknowns | Facts the sources do not establish |
| Practical verdict | A bounded recommendation rather than a universal winner claim |

### GPT-5.6 Sol: OpenAI’s flagship tier for frontier professional work

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-07-09 |
| Release state | Generally available across documented GPT-5.6 surfaces, subject to plan and product limits |
| Model identifier | `gpt-5.6-sol` |
| Intended role | Highest-capability GPT-5.6 tier |
| Modalities and product surface | Hosted multimodal reasoning and tool use; exact modality matrix depends on surface |
| Context or generation envelope | 1.05M input tokens; 128K maximum output |
| Pricing | $5 input / $30 output per million API tokens |
| Weights and license | Closed; no public checkpoint or first-party quantization |
| Architecture disclosure | Undisclosed. OpenAI does not publish parameter count, layer count, attention topology, expert routing, or training-token totals. |

#### Launch story

GPT-5.6 Sol is the model OpenAI places at the top of the GPT-5.6 family: the tier intended for
difficult research, software engineering, scientific analysis, computer use, browsing,
documents, spreadsheets, and presentation work where failure costs more than latency. The
announcement is less about a single benchmark crown than a broader claim that professional work
quality can improve at the same time as tool efficiency.

#### Capabilities and product behavior

The launch emphasizes long-horizon knowledge work, agentic browsing, computer use,
source-grounded research, coding, editable office artifacts, complex visual layouts, and
tool-mediated workflows. Sol supports the family reasoning settings through `max`; supported
products may add `ultra` orchestration, which coordinates multiple agents and must not be
misreported as a larger single-model checkpoint.

#### Benchmarks, results, and what they actually establish

OpenAI reports 92.2% on BrowseComp and 62.6% on OSWorld 2.0 for Sol, describing both as
state-of-the-art launch results. OpenAI also reports that the OSWorld result exceeds Opus 4.8
while using 85% fewer output tokens. Artificial Analysis separately reports 58.9 on Intelligence
Index v4.1 and 80 in its Codex Coding Agent Index for Sol Max. Those independent numbers include
the Codex harness and Max effort; they are not bare API scores and are not Sol Ultra results.

#### Deployment and evaluation consequences

Use Sol when the task is ambiguous, cross-domain, expensive to get wrong, or difficult to
validate with one deterministic check. Log model ID, reasoning effort, orchestration mode,
tools, token use, wall time, retries, and human correction. For production economics, remember
that requests above the published long-context billing threshold, cache writes, tool traces, and
agent coordination can dominate the headline token price.

#### Limits, unknowns, and misleading shortcuts to avoid

OpenAI has not disclosed whether Sol is dense or MoE, its total or active parameters, its
transformer depth, its attention and KV-head counts, the structure of its multimodal encoders,
its training data mixture, or the serving precision. Product polish and benchmark strength do
not reveal those internals.

#### Practical verdict

Sol is the default candidate for the hardest GPT-5.6 work, but it should earn its extra cost on
a matched task set. A cheaper tier with a strict validator can still be the better engineering
choice.

### GPT-5.6 Terra: The balanced GPT-5.6 tier for daily engineering and professional workflows

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-07-09 |
| Release state | Available through documented API, Work, and Codex paths; account and rollout restrictions can apply |
| Model identifier | `gpt-5.6-terra` |
| Intended role | Balanced capability, latency, and price |
| Modalities and product surface | Hosted multimodal reasoning and tool use by product surface |
| Context or generation envelope | 1.05M input tokens; 128K maximum output |
| Pricing | $2.50 input / $15 output per million API tokens |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed; no public checkpoint dimensions or quantization choices |

#### Launch story

Terra is the deliberately practical member of the GPT-5.6 family. OpenAI positions it for
everyday repository work, documents, analysis, and tool-heavy tasks where Luna may be too
constrained and Sol may be economically excessive. The important launch idea is not that Terra
is “half a Sol,” but that it occupies its own price-performance envelope.

#### Capabilities and product behavior

Terra inherits the family’s long context, tool use, structured professional work, coding,
browsing, and reasoning controls. In Codex it is especially relevant for multi-file repairs,
test updates, refactors, source synthesis, and routine agent loops. Supported products can
expose Ultra orchestration, but Terra Ultra is a multi-agent configuration rather than a seventh
API reasoning value.

#### Benchmarks, results, and what they actually establish

OpenAI states that Terra surpasses GPT-5.5 performance at lower cost in its launch analysis.
Artificial Analysis reports Terra Max at 55 on Intelligence Index v4.1 and 77 in the Codex
Coding Agent Index, three points behind Sol Max in that coding composite while carrying a much
lower measured task cost. The result is evidence for a strong balanced tier, not proof that
every Terra run will be within three points of Sol.

#### Deployment and evaluation consequences

Terra is the strongest default for broad but bounded engineering work. Begin at Medium or High,
require inspect-first behavior, name the exact test command, and escalate to Max only when a
measurable failure remains. Ultra is appropriate only when workstreams can be separated without
agents colliding on the same mutable state.

#### Limits, unknowns, and misleading shortcuts to avoid

As with Sol, network topology, active parameter count, training recipe, attention mechanism, and
serving precision remain undisclosed. The lower price cannot be used to infer distillation,
quantization, or a smaller dense backbone.

#### Practical verdict

Terra is likely to deliver the best cost-adjusted result for many real repositories and office
workflows. The rational default is Terra first, then Sol when evidence shows the task needs more
headroom.

### GPT-5.6 Luna: OpenAI’s fastest and least expensive GPT-5.6 tier

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-07-09 |
| Release state | Available on documented API and Codex surfaces; no Luna Ultra in the checked local catalog |
| Model identifier | `gpt-5.6-luna` |
| Intended role | High-throughput execution, extraction, classification, and bounded subagent work |
| Modalities and product surface | Hosted multimodal and tool-capable behavior varies by surface |
| Context or generation envelope | 1.05M input tokens; 128K maximum output |
| Pricing | $1 input / $6 output per million API tokens |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

Luna is the speed-and-volume tier of GPT-5.6. Its announcement matters because OpenAI is not
treating low cost as synonymous with non-reasoning utility: Luna supports the same published API
reasoning ladder through `max`, allowing developers to spend more test-time computation on a
cheaper checkpoint when the workload benefits.

#### Capabilities and product behavior

Luna is suited to extraction, classification, repetitive code edits, bounded transformations,
metadata work, high-volume document processing, and subagent roles inside a larger workflow. It
can also handle small features and source packets when the output contract and validator are
explicit.

#### Benchmarks, results, and what they actually establish

OpenAI says Luna nearly matches GPT-5.5 peak performance at less than half the estimated cost in
the launch comparison. Artificial Analysis reports 51.2 on Intelligence Index v4.1 and 75 in the
Codex Coding Agent Index at Max. The coding score is only five points below Sol in that dated
composite, but the gap can widen on tasks that demand ambiguous architectural judgment, deep
visual reasoning, or difficult recovery.

#### Deployment and evaluation consequences

Use Luna when correctness can be tested cheaply and failures can be retried or escalated. Keep
prompts narrow, schemas explicit, and tool permissions minimal. For large batches, measure
first-pass validity, retry rate, latency distribution, and correction time rather than
celebrating the cheapest token price while paying humans to repair malformed outputs.

#### Limits, unknowns, and misleading shortcuts to avoid

OpenAI does not disclose whether Luna is a distilled model, a separately trained checkpoint, a
sparse model, or a quantized hosted variant. The local catalog’s absence of Luna Ultra is a
product fact, not evidence of an architectural limitation.

#### Practical verdict

Luna is a serious production tier, not merely a toy fast model. It becomes impressive when
paired with validators and disciplined escalation.

### Claude Fable 5: Anthropic’s generally available Mythos-class frontier model with conservative safeguards

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-06-09; redeployed 2026-07-01 |
| Release state | Generally available again after a temporary access suspension |
| Model identifier | Claude Platform Fable 5 identifier as documented in the live model catalog |
| Intended role | Anthropic’s highest-capability generally available model in this snapshot |
| Modalities and product surface | Text, vision, coding, tools, long-horizon agents, and product-integrated workflows |
| Context or generation envelope | Published 1M-context policy in the cited Anthropic documentation |
| Pricing | $10 input / $50 output per million tokens |
| Weights and license | Closed |
| Architecture disclosure | Anthropic calls it Mythos-class but does not disclose checkpoint dimensions |

#### Launch story

Fable 5 is Anthropic’s attempt to make its strongest underlying model broadly usable while
adding a safeguard layer for capability areas where misuse risk rises sharply. The launch story
therefore has two inseparable parts: frontier performance and product routing. A request can
target Fable yet be handled by Opus 4.8 when safeguards trigger, with the user notified.

#### Capabilities and product behavior

Anthropic highlights sustained autonomous work, software engineering, analytical knowledge work,
vision, memory, scientific research, complex browser tasks, CAD, simulation, and long-running
game or environment interaction. The company says the longer and more complex the task, the
larger Fable’s lead over prior Claude models.

#### Benchmarks, results, and what they actually establish

Anthropic describes state-of-the-art performance on nearly all tested capability benchmarks and
cites partner results in coding, finance, trading analysis, visual reconstruction, and
long-horizon tasks. Artificial Analysis reports Fable Max with fallback at 59.9 on Intelligence
Index v4.1 and 77 in the Claude Code coding-agent composite. AA-Briefcase also places it
strongly on rubric completion and analytical quality. Every public score must retain the “with
fallback” qualifier when routing was possible.

#### Deployment and evaluation consequences

Fable suits high-value analytical work, difficult codebase changes, research, and professional
artifacts where its price is justified and occasional fallback is acceptable. Evaluation logs
should record requested model, effort, product surface, fallback notice, tools, and final
outcome. A sensitive-domain test must not quietly mix Fable and Opus outputs into one
pure-checkpoint claim.

#### Limits, unknowns, and misleading shortcuts to avoid

Dense versus MoE, parameter counts, layers, attention design, training tokens, multimodal
encoders, and internal effort allocation remain undisclosed. “Mythos-class” is a product family
label, not a public architecture specification.

#### Practical verdict

Fable 5 is one of the strongest systems in the guide, but it is a safeguarded routed product.
That distinction is central, not a footnote.

### Claude Opus 4.8: Anthropic’s premium closed model for demanding coding, analysis, and agent work

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-05-28 |
| Release state | Generally available in documented Claude surfaces |
| Model identifier | Claude Opus 4.8 model identifier from the current Anthropic catalog |
| Intended role | High-capability premium Claude model and documented Fable fallback |
| Modalities and product surface | Text, vision, tools, Claude Code, Cowork, and professional workflows |
| Context or generation envelope | Published 1M-context policy in the cited documentation |
| Pricing | $5 input / $25 output per million tokens |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

Opus 4.8 remains important even after Fable 5 because it offers a cleaner named-checkpoint
comparison, a lower API price, and a mature place inside Claude Code and other Anthropic
products. It also serves as the documented fallback for some safeguarded Fable requests, giving
it an operational role beyond ordinary model selection.

#### Capabilities and product behavior

Anthropic positions Opus for difficult coding, long-horizon agents, document analysis, financial
work, research, and finished professional artifacts. In Claude Code, its behavior includes
repository inspection, terminal use, patches, test execution, and iterative recovery, but those
actions belong to the harness rather than the bare API checkpoint.

#### Benchmarks, results, and what they actually establish

Artificial Analysis reports 55.7 on Intelligence Index v4.1 at Max and 73 in the Claude Code
Coding Agent Index. The coding figure includes Claude Code’s system prompt, tools, permissions,
caching, file editor, and terminal loop. The model is therefore best compared either in the same
harness or through a separately controlled API evaluation.

#### Deployment and evaluation consequences

Use `xhigh` as the demanding coding and agentic starting point where Anthropic recommends it,
and reserve Max for task classes where measured quality gains justify additional latency and
token use. Track citation correctness, test success, spreadsheet or document operations, and
correction burden rather than relying on prose polish.

#### Limits, unknowns, and misleading shortcuts to avoid

Anthropic does not publish parameter counts, layers, head counts, MoE routing, training corpus,
or serving precision. Max is an effort label, not an architectural variant.

#### Practical verdict

Opus 4.8 is the dependable premium Claude reference point: expensive enough to require
measurement, but easier to attribute than a routed Fable product.

### Claude Sonnet 5: Anthropic’s agentic Sonnet release aimed at frontier performance per dollar

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-06-30 |
| Release state | Available across all Claude plans, Claude Code, and the Claude Platform |
| Model identifier | `claude-sonnet-5` |
| Intended role | Cost-sensitive agentic coding and professional work |
| Modalities and product surface | Text, vision, browser and terminal use when the product or host supplies those tools |
| Context or generation envelope | Current Claude context policy; exact surface limits should be checked live |
| Pricing | Introductory $2/$10 per million input/output tokens through 2026-08-31; then $3/$15 |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

Sonnet 5 is framed as a change in follow-through rather than merely another quality bump.
Anthropic’s launch emphasizes that it completes multi-step jobs that earlier Sonnet models
abandoned halfway, checks its work, navigates messy technical contexts, and reaches some Opus
4.8 capability levels at higher effort while preserving a lower cost envelope.

#### Capabilities and product behavior

The model targets software engineering, browser and computer use, research, enterprise
automation, legal analysis, live-data exploration, and brownfield debugging. Early-access
reports describe reproducing bugs, writing tests, implementing fixes, validating regressions,
and completing multi-application business workflows end to end. Those examples are partner
testimonials, not independently controlled benchmark replications.

#### Benchmarks, results, and what they actually establish

Anthropic publishes cost-performance curves on BrowseComp and OSWorld-Verified across effort
levels, showing Sonnet 5 as a strict improvement over Sonnet 4.6 and as overlapping Opus 4.8 on
some tasks. The company corrected its BrowseComp chart to use the standard 10M-token methodology
with compaction and programmatic tool calling. That correction is valuable evidence that
methodology can materially change headline performance.

#### Deployment and evaluation consequences

Sonnet 5 should be the first Claude candidate for routine agents, repository work, and knowledge
tasks when Fable or Opus economics are excessive. Pin the effort, tool schema, compaction
policy, token budget, and recovery loop. Re-evaluate pricing after the introductory period
rather than freezing a launch discount into a permanent comparison.

#### Limits, unknowns, and misleading shortcuts to avoid

No public parameter, layer, expert, attention, training-token, or quantization data exists in
the checked sources. Browser and terminal claims describe supported products and host
integrations, not powers automatically granted to a raw API call.

#### Practical verdict

Sonnet 5 is the practical Claude release: more autonomous than earlier Sonnet models and
potentially close to Opus on selected tasks, provided the harness and effort are recorded.

### DeepSeek-V4-Pro: DeepSeek’s 1.6T-total, 49B-active open MoE flagship

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-04-24 |
| Release state | Preview API and open weights |
| Model identifier | `deepseek-v4-pro` |
| Intended role | Open-weight frontier reasoning, coding, agents, and long context |
| Modalities and product surface | Text-focused API with thinking/non-thinking, JSON, tools, chat prefix, and completion interfaces |
| Context or generation envelope | 1M context; 384K maximum output in the current API table |
| Pricing | $0.435 cache-miss input / $0.87 output per million tokens in the checked pricing table |
| Weights and license | Open weights; exact license must be checked on the selected repository revision |
| Architecture disclosure | 1.6T total parameters, 49B active; sparse MoE with token-wise compression and DeepSeek Sparse Attention |

#### Launch story

DeepSeek-V4-Pro is the scale-heavy member of the V4 Preview release. Its announcement combines
an unusually large public checkpoint with a low active-parameter footprint, million-token
context, dual thinking modes, and an explicit claim that open models can compete with leading
closed systems in coding, reasoning, and world knowledge.

#### Capabilities and product behavior

The API supports OpenAI-compatible and Anthropic-compatible interfaces, tool calls, JSON output,
context caching, chat prefix completion, and Fill-in-the-Middle where documented. DeepSeek also
emphasizes integration with coding agents and long-context efficiency. Thinking and non-thinking
are separate operating modes and must be held constant in any comparison.

#### Benchmarks, results, and what they actually establish

DeepSeek claims open-source state of the art on agentic coding, leading open-model world
knowledge, and top-tier math, STEM, and coding performance. Those charts are vendor results
unless reproduced under a matching harness. The technical report and first-party configuration
are the correct sources for architecture, but benchmark procurement decisions should use a
frozen external task set.

#### Deployment and evaluation consequences

The 49B active figure describes per-token compute, not checkpoint storage. Hosting 1.6T
parameters requires aggressive sharding, expert parallelism, high-bandwidth interconnects, and
careful routing balance. A deployment report must name weight revision, precision, quantization,
runtime, expert-parallel topology, context cap, attention backend, hardware, throughput, and
quality regressions.

#### Limits, unknowns, and misleading shortcuts to avoid

“Open-sourced” does not by itself establish the license, commercial terms, supported
quantizations, or parity with DeepSeek’s hosted service. Long context and sparse attention also
do not guarantee accurate retrieval across one million tokens.

#### Practical verdict

V4-Pro is technically ambitious and unusually transparent at the checkpoint level, but it is a
data-center-scale open model, not a casual single-GPU download.

### DeepSeek-V4-Flash: A 284B-total, 13B-active V4 checkpoint optimized for speed and cost

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-04-24 |
| Release state | Preview API and open weights |
| Model identifier | `deepseek-v4-flash` |
| Intended role | Fast reasoning, simple agents, completion, and high-volume API work |
| Modalities and product surface | Text, thinking/non-thinking, JSON, tools, chat prefix, and FIM where supported |
| Context or generation envelope | 1M context; 384K maximum output |
| Pricing | $0.14 cache-miss input / $0.28 output per million tokens |
| Weights and license | Open weights; license must be verified on the exact artifact |
| Architecture disclosure | 284B total parameters, 13B active; V4 sparse-attention and MoE family |

#### Launch story

DeepSeek-V4-Flash is not presented as a tiny companion model. DeepSeek says its reasoning
approaches V4-Pro and that it can perform on par with Pro on simpler agent tasks, while using a
much smaller total and active parameter budget. That makes Flash the operationally interesting
part of the V4 release for many teams.

#### Capabilities and product behavior

Flash supports the same broad API mode split as Pro, including thinking and non-thinking
operation. The legacy `deepseek-chat` and `deepseek-reasoner` aliases temporarily route to Flash
non-thinking and thinking, with retirement scheduled for 2026-07-24. Production code should use
the explicit V4 ID rather than relying on compatibility aliases.

#### Benchmarks, results, and what they actually establish

Vendor materials claim reasoning close to Pro and parity on simple agent tasks. Those claims
should be tested with matched prompts, tool schemas, output caps, and deadlines. A non-thinking
FIM run must not be compared with a thinking chat agent and summarized as a pure model
difference.

#### Deployment and evaluation consequences

At 284B total, Flash still requires serious memory capacity even though only 13B parameters are
active per token. Expert routing lowers arithmetic but adds communication, routing, and
load-balancing costs. Test open checkpoints separately from the hosted API and document
precision, quantizer, runtime, hardware, batch size, and long-context memory.

#### Limits, unknowns, and misleading shortcuts to avoid

Preview status, hosted/self-hosted parity, license details, quantization quality, and exact
training data remain areas to verify. The inexpensive API rate can be overwhelmed by retries or
oversized million-token prompts.

#### Practical verdict

V4-Flash is one of the strongest candidates for low-cost open-model agents, provided the
evaluator resists mixing modes and pretending active parameters equal memory footprint.

### GLM-5.2: Z.ai’s 744B-total, 40B-active long-horizon MoE flagship

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-06-16 |
| Release state | Released with public weights and MIT license |
| Model identifier | `GLM-5.2` in official materials |
| Intended role | Long-horizon coding, reasoning, and agent engineering |
| Modalities and product surface | Text-centric agent and coding workflows; exact checkpoint capabilities depend on release artifact |
| Context or generation envelope | 1M tokens |
| Pricing | No current per-token price established in the reviewed release source |
| Weights and license | Public weights; MIT license |
| Architecture disclosure | 744B total, 40B active MoE; IndexShare sparse-attention design described by Z.ai |

#### Launch story

GLM-5.2 is presented as the point where “vibe coding” gives way to agentic engineering: a model
expected to maintain plans, state, tools, and verification across long projects rather than
merely emit a plausible patch. The release extends the 744B/40B-active GLM-5 scale with a
changed sparse-attention design and explicit High and Max coding-surface choices.

#### Capabilities and product behavior

Z.ai highlights long-horizon coding, repository operation, planning, tool use, context
retention, and difficult reasoning. Public weights and a permissive license make the model
relevant for sovereign deployment and custom agent stacks, but the operator must recreate the
tool loop, compaction, permissions, and safety system that a hosted product would otherwise
supply.

#### Benchmarks, results, and what they actually establish

The GLM release and repository publish coding and agent benchmark results with setup notes. They
remain vendor claims until reproduced with the same model revision, effort, tools, context,
timeout, and judge. Grok’s launch chart lists GLM-5.2 at 44% on DeepSWE 1.1 and 62.1% on
SWE-Bench Pro under the cited external configurations; those rows still belong to those specific
harnesses.

#### Deployment and evaluation consequences

A 744B checkpoint is a cluster-scale deployment despite only 40B active parameters. Plan for
expert parallelism, interconnect bandwidth, router imbalance, checkpoint storage, optimizer-free
inference memory, KV cache, and long-context attention cost. FP8 artifacts reduce storage and
bandwidth but require a matched accuracy evaluation.

#### Limits, unknowns, and misleading shortcuts to avoid

A million-token window is capacity, not a persistent memory guarantee. The reviewed release does
not establish a universal output cap, current API token price, or one canonical serving stack.

#### Practical verdict

GLM-5.2 is a major open-weight agent model for organizations that can afford the infrastructure
and operational discipline its scale demands.

### Mistral Medium 3.5: A dense 128B open-weight multimodal model for coding and agents

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-04-28 |
| Release state | Open weights under Modified MIT |
| Model identifier | `mistral-medium-3-5` |
| Intended role | Frontier-class generalist for coding, agents, and multimodal work |
| Modalities and product surface | Text and image in the documented model card |
| Context or generation envelope | 256K tokens |
| Pricing | $1.50 input / $7.50 output per million hosted tokens |
| Weights and license | Open; Modified MIT |
| Architecture disclosure | Dense 128B transformer; exact first-party configuration supplies layer, width, and attention dimensions |

#### Launch story

Mistral Medium 3.5 is the company’s argument that an open dense model can still occupy a useful
frontier-class position in an era dominated by sparse MoE releases. Its role is broad: coding,
multimodal understanding, agents, professional work, and self-deployment without forcing teams
into a trillion-parameter expert system.

#### Capabilities and product behavior

The documented surface includes chat, function calling, structured outputs, multimodal input,
and agent-oriented use cases. For coding, the relevant question is not whether the card says
“agentic,” but whether the chosen harness can inspect a repository, call tools correctly,
recover from failures, and satisfy a test suite.

#### Benchmarks, results, and what they actually establish

Mistral’s launch and model card provide vendor comparisons. Those results should be retained
with their prompt, precision, runtime, and harness. The model’s real advantage may appear in
deployment simplicity and predictable dense execution rather than a single composite score.

#### Deployment and evaluation consequences

Dense 128B means all parameters participate in each token, producing simpler routing behavior
but high arithmetic cost. Record BF16 or quantized format, tensor parallelism, context cap,
batch size, attention backend, vision-encoder precision, and tool adapter. Compare hosted and
self-hosted runs separately.

#### Limits, unknowns, and misleading shortcuts to avoid

Modified MIT is not identical to Apache 2.0; teams must read the actual terms. A 256K advertised
window does not prove reliable retrieval or affordable KV-cache growth.

#### Practical verdict

Medium 3.5 is the cleaner operational choice when a team wants a large open dense model and can
accept its compute cost in exchange for simpler execution than giant MoE systems.

### Mistral Small 4: A 119B-total, 6.5B-active multimodal MoE with first-party NVFP4

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-03-16 |
| Release state | Open weights under Apache 2.0 |
| Model identifier | `mistral-small-2603` |
| Intended role | Cost-sensitive multimodal agents and coding |
| Modalities and product surface | Text and image |
| Context or generation envelope | 256K tokens |
| Pricing | $0.15 input / $0.60 output per million hosted tokens |
| Weights and license | Open; Apache 2.0; first-party NVFP4 checkpoint available |
| Architecture disclosure | 119B total, about 6.5B active; 128 experts with routed and shared expert participation in the first-party configuration |

#### Launch story

Mistral Small 4 stretches the word “Small” until it becomes a philosophical question. The model
stores 119B parameters but activates roughly 6.5B per token, targeting strong reasoning, coding,
and multimodal performance at a much lower serving cost than a dense model of similar total
scale.

#### Capabilities and product behavior

The model is intended for agentic coding, multimodal analysis, function calling, structured
output, and high-throughput production. Mistral also provides a first-party NVFP4 checkpoint,
giving deployers a better provenance story than an anonymous community conversion.

#### Benchmarks, results, and what they actually establish

Mistral reports substantial completion-time and throughput gains over Mistral Small 3 in
optimized setups. These are vendor system measurements, so hardware, batching, speculative
decoding, quantization, and attention kernels must be matched before treating the gains as
portable.

#### Deployment and evaluation consequences

The A6.5B label describes active compute, not the amount of weight memory. All 119B parameters
must be resident, sharded, or streamed. Expert parallelism and routing can reduce arithmetic
while creating communication and imbalance costs. Compare reference and NVFP4 checkpoints on
coding, tool calls, long context, multilingual output, vision grounding, and reasoning.

#### Limits, unknowns, and misleading shortcuts to avoid

Quantization can alter router logits and expert selection even when broad perplexity loss
appears small. The word “Small” should not be used to promise laptop deployment without a
complete memory calculation.

#### Practical verdict

Small 4 is one of the most compelling open MoE releases in the guide because it combines low
active compute, a permissive license, multimodality, and first-party low-precision weights.

### Mistral OCR 4: A document-intelligence service built around structured extraction rather than chat scores

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-06-23 |
| Release state | Premier hosted service |
| Model identifier | `mistral-ocr-4-0` |
| Intended role | OCR, layout understanding, structural labels, and bounding boxes |
| Modalities and product surface | Documents and images to structured text and layout data |
| Context or generation envelope | Page-oriented service limits from the live documentation |
| Pricing | $4 per 1,000 pages or $5 per 1,000 annotated pages |
| Weights and license | Not public |
| Architecture disclosure | Undisclosed service architecture |

#### Launch story

OCR 4 is best understood as a product announcement for extraction infrastructure, not another
general-purpose model on a chatbot leaderboard. Mistral highlights paragraph bounding boxes,
structural block labels, reading order, and document-aware outputs that can feed downstream
validation or retrieval systems.

#### Capabilities and product behavior

The service targets native PDFs, scans, images, tables, forms, multilingual documents, and
layout-sensitive conversion. High-value use comes from preserving page provenance and
coordinates, not merely producing attractive Markdown.

#### Benchmarks, results, and what they actually establish

The guide does not claim a universal OCR accuracy number because the reviewed source does not
establish one across every language, scan quality, handwriting style, or document class. Teams
should build representative ground truth and measure character or word accuracy, field accuracy,
table-cell accuracy, reading order, block classification, bounding-box overlap, and correction
minutes per page.

#### Deployment and evaluation consequences

Use two stages for consequential documents: extraction with provenance, followed by
deterministic domain validation. Dates must parse, totals must reconcile, IDs must match
checksums, and uncertain fields must go to review. Cost should be measured per accepted
document, including preprocessing, retries, annotation mode, storage, and human correction.

#### Limits, unknowns, and misleading shortcuts to avoid

Parameter count, vision encoder, decoder design, training data, handwriting coverage, security
certifications, and self-hosted availability are not inferred.

#### Practical verdict

OCR 4 should win or lose on faithful extraction and reduced correction labor, not on whether its
output looks polished in a demo.

### Voxtral TTS: Mistral’s open 4B streaming speech model with voice adaptation

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-03-23 |
| Release state | Open weights and hosted service |
| Model identifier | `voxtral-mini-tts-2603` |
| Intended role | Low-latency multilingual speech synthesis |
| Modalities and product surface | Text and optional voice prompt to audio |
| Context or generation envelope | Speech-generation interface rather than a conventional long-text context claim |
| Pricing | Hosted generation pricing from the live Mistral pricing page |
| Weights and license | Open; checked catalog lists CC BY-NC 4.0 |
| Architecture disclosure | 4B parameters; deeper layer and head details are not fully established in the reviewed card |

#### Launch story

Voxtral TTS brings Mistral’s open-model strategy into speech generation. The launch combines
streaming, nine-language support, approximately 90 ms time to first audio in the vendor setup,
and zero-shot voice cloning from a prompt recording without requiring a transcript.

#### Capabilities and product behavior

The model supports controllable speech, multilingual generation, streaming output, and voice
adaptation. Those features should be evaluated separately for intelligibility, pronunciation,
prosody, pacing, latency, clipping, continuity, and voice similarity.

#### Benchmarks, results, and what they actually establish

No single text-model benchmark is relevant. Build scripts containing names, numbers,
abbreviations, domain terms, code-switching, emotional directions, and interruption cases.
Measure word and number errors, time to first audio, tail latency, real-time factor,
repeated-sample consistency, and listener preference.

#### Deployment and evaluation consequences

Record checkpoint revision, precision or quantization, runtime, GPU, batch size, sample rate,
streaming chunk size, and real-time factor. Voice adaptation requires explicit permission from
the speaker, controlled source recordings, and clear disclosure when output is synthetic.

#### Limits, unknowns, and misleading shortcuts to avoid

CC BY-NC is not blanket commercial permission. Watermarking, identity protections, and
provenance behavior remain surface-specific unless documented.

#### Practical verdict

Voxtral TTS is technically attractive for custom speech systems, but consent and licensing are
as important as latency.

### Leanstral 1.5: A 119B-total, 6.5B-active model specialized for Lean 4 proof engineering

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-06-30 |
| Release state | Labs model with weights |
| Model identifier | `labs-leanstral-1-5` |
| Intended role | Automated theorem proving and autoformalization |
| Modalities and product surface | Lean code, mathematical text, repository context, and tool-mediated proof workflows |
| Context or generation envelope | 256K tokens |
| Pricing | Listed at $0 in the checked catalog |
| Weights and license | Public checkpoint in the Mistral Small 4 MoE family |
| Architecture disclosure | 119B total, about 6.5B active; specialized post-training rather than a wholly new backbone |

#### Launch story

Leanstral 1.5 is an announcement for formal proof engineering, not a claim that one model has
“solved mathematics.” Its backbone belongs to the Mistral Small 4 family; the release value
comes from specialized data, post-training, tool behavior, and repository-aware Lean workflows.

#### Capabilities and product behavior

The model targets proof search, code repair, theorem completion, autoformalization, use of
project lemmas, and multi-step interaction with the Lean compiler. It can propose statements and
proofs, but validity comes only from the pinned compiler and project environment.

#### Benchmarks, results, and what they actually establish

The correct result is a successfully compiled proof of the intended theorem. Measure first-pass
compile rate, success after bounded repair, unsupported-library hallucination, attempts, wall
time, and human edits. Separately review whether the formal statement faithfully captures the
natural-language mathematics.

#### Deployment and evaluation consequences

Pin the repository commit, Lean version, imports, dependency lock, model revision, prompt,
tool/MCP version, and compilation command. Preserve the final `.lean` artifact and diagnostic
transcript.

#### Limits, unknowns, and misleading shortcuts to avoid

A fluent mathematical explanation with invalid Lean is a failure. A valid proof of the wrong
formal statement is also a failure. Hosted zero price does not imply unlimited capacity or
permanent terms.

#### Practical verdict

Leanstral 1.5 is valuable precisely because the compiler can reject its mistakes. Formal
verification remains a workflow, not a model adjective.

### Robostral Navigate: Mistral’s announced embodied-navigation system

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-07-08 |
| Release state | Announcement with limited public technical material |
| Model identifier | No public model identifier established in the checked sources |
| Intended role | Embodied navigation research |
| Modalities and product surface | Expected perception and navigation inputs; exact interface undisclosed |
| Context or generation envelope | Undisclosed |
| Pricing | Undisclosed |
| Weights and license | No public weight download established |
| Architecture disclosure | Undisclosed |

#### Launch story

Robostral Navigate appears in the guide as an announcement-stage system rather than a deployable
product. Mistral identifies it as a model built for embodied navigation, but the public material
reviewed here does not yet provide the API contract, weight artifact, supported robots,
simulation interface, or safety procedure needed for production guidance.

#### Capabilities and product behavior

A future system in this category would need to separate scene understanding, mapping, route
planning, action selection, collision avoidance, recovery, and operator override. Success at
visual question answering or high-level planning would not prove safe motor control.

#### Benchmarks, results, and what they actually establish

A meaningful evaluation must record world or simulator version, sensor suite, action space,
latency, success definition, collision policy, recovery behavior, and transfer to physical
hardware. No general-chat benchmark should be treated as evidence of navigation safety.

#### Deployment and evaluation consequences

Do not connect an announcement-stage model directly to motors. Any future trial requires
simulation, independent safety control, hard motion limits, an emergency stop, monitoring,
staged authority, and a human operator.

#### Limits, unknowns, and misleading shortcuts to avoid

Identifier, API, pricing, license, weights, hardware support, output schema, and operating
envelope remain unknown.

#### Practical verdict

Keep Robostral Navigate on the watchlist until Mistral publishes an interface and safety
contract. An announcement is not a robot controller.

### Gemma 4 E2B: Ultra-mobile effective-parameter model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-04 launch family; model card updated 2026-06-26 |
| Release state | Open weights for pre-trained and instruction-tuned variants |
| Model identifier | First-party Google/Hugging Face identifier for Gemma 4 E2B |
| Intended role | Ultra-mobile effective-parameter model |
| Modalities and product surface | Text, image, video, audio input to text |
| Context or generation envelope | 128K |
| Pricing | Self-hosted economics; hosted availability varies by surface |
| Weights and license | Open weights with responsible commercial use under Gemma terms |
| Architecture disclosure | Dense edge design; 35 text layers; hidden size 1536; query/KV heads 8 / 1; hybrid local/global attention |

#### Launch story

Gemma 4 E2B is one member of Google’s five-model Gemma 4 release, a family built to cover mobile
devices, laptops, workstations, and servers without pretending that one checkpoint suits every
system. E2B is built for phones, browsers, IoT, and other constrained environments. Its
effective-parameter design makes deployment behavior as important as nominal model scale.
Evaluate on-device latency, thermals, memory pressure, modality activation, and quality after
mobile conversion.

#### Capabilities and product behavior

All Gemma 4 variants add configurable thinking, native system-role support, function calling,
multimodal understanding according to the exact variant, hybrid attention, and a dedicated draft
model for speculative decoding. The family supports more than 140 languages and increases
context to 128K or 256K by size.

#### Benchmarks, results, and what they actually establish

Google describes frontier-level performance at each size and publishes model-card benchmark
tables. Those are vendor results tied to specific checkpoints, prompts, and runtimes. Local
evaluation should freeze prompt templates and compare the reference checkpoint, quantized build,
and application wrapper separately.

#### Deployment and evaluation consequences

Approx. 11.4 GB BF16, 5.7 GB SFP8, 2.9 GB Q4_0; mobile footprints also published. Add KV cache,
runtime workspace, speculative draft model, multimodal encoders or projectors, batch buffers,
and framework overhead. Record exact revision, precision, quantizer, context cap, attention
backend, processor, device, and tokens per second.

#### Limits, unknowns, and misleading shortcuts to avoid

Open weights disclose far more than hosted APIs, but they do not disclose every training
example, guarantee runtime compatibility, or promise that a four-bit conversion preserves tool
calling, visual grounding, and long-context behavior.

#### Practical verdict

Gemma 4 E2B should be selected by hardware and task, not by family prestige. Its announcement
value is the combination of transparent architecture and a clearly targeted deployment envelope.

### Gemma 4 E4B: Higher-capability mobile and edge model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-04 launch family; model card updated 2026-06-26 |
| Release state | Open weights for pre-trained and instruction-tuned variants |
| Model identifier | First-party Google/Hugging Face identifier for Gemma 4 E4B |
| Intended role | Higher-capability mobile and edge model |
| Modalities and product surface | Text, image, video, audio input to text |
| Context or generation envelope | 128K |
| Pricing | Self-hosted economics; hosted availability varies by surface |
| Weights and license | Open weights with responsible commercial use under Gemma terms |
| Architecture disclosure | Dense edge design; 42 text layers; hidden size 2560; query/KV heads 8 / 2; hybrid local/global attention |

#### Launch story

Gemma 4 E4B is one member of Google’s five-model Gemma 4 release, a family built to cover mobile
devices, laptops, workstations, and servers without pretending that one checkpoint suits every
system. E4B trades additional memory and compute for stronger edge reasoning and multimodality.
It should be compared with E2B on the same device under the same thermal and power envelope
rather than on server throughput alone.

#### Capabilities and product behavior

All Gemma 4 variants add configurable thinking, native system-role support, function calling,
multimodal understanding according to the exact variant, hybrid attention, and a dedicated draft
model for speculative decoding. The family supports more than 140 languages and increases
context to 128K or 256K by size.

#### Benchmarks, results, and what they actually establish

Google describes frontier-level performance at each size and publishes model-card benchmark
tables. Those are vendor results tied to specific checkpoints, prompts, and runtimes. Local
evaluation should freeze prompt templates and compare the reference checkpoint, quantized build,
and application wrapper separately.

#### Deployment and evaluation consequences

Approx. 17.9 GB BF16, 8.9 GB SFP8, 4.5 GB Q4_0; mobile figures published. Add KV cache, runtime
workspace, speculative draft model, multimodal encoders or projectors, batch buffers, and
framework overhead. Record exact revision, precision, quantizer, context cap, attention backend,
processor, device, and tokens per second.

#### Limits, unknowns, and misleading shortcuts to avoid

Open weights disclose far more than hosted APIs, but they do not disclose every training
example, guarantee runtime compatibility, or promise that a four-bit conversion preserves tool
calling, visual grounding, and long-context behavior.

#### Practical verdict

Gemma 4 E4B should be selected by hardware and task, not by family prestige. Its announcement
value is the combination of transparent architecture and a clearly targeted deployment envelope.

### Gemma 4 12B: Unified multimodal workstation model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-04 launch family; model card updated 2026-06-26 |
| Release state | Open weights for pre-trained and instruction-tuned variants |
| Model identifier | First-party Google/Hugging Face identifier for Gemma 4 12B |
| Intended role | Unified multimodal workstation model |
| Modalities and product surface | Text, image, video, audio input to text |
| Context or generation envelope | 256K |
| Pricing | Self-hosted economics; hosted availability varies by surface |
| Weights and license | Open weights with responsible commercial use under Gemma terms |
| Architecture disclosure | Dense unified architecture; 48 text layers; hidden size 3840; query/KV heads 16 / 8; hybrid local/global attention |

#### Launch story

Gemma 4 12B is one member of Google’s five-model Gemma 4 release, a family built to cover mobile
devices, laptops, workstations, and servers without pretending that one checkpoint suits every
system. The 12B model uses a unified or encoder-free multimodal design described by Google,
replacing separate vision and audio encoders with direct projections. Runtime support must match
the exact model class and processor rather than assuming an older Gemma pipeline.

#### Capabilities and product behavior

All Gemma 4 variants add configurable thinking, native system-role support, function calling,
multimodal understanding according to the exact variant, hybrid attention, and a dedicated draft
model for speculative decoding. The family supports more than 140 languages and increases
context to 128K or 256K by size.

#### Benchmarks, results, and what they actually establish

Google describes frontier-level performance at each size and publishes model-card benchmark
tables. Those are vendor results tied to specific checkpoints, prompts, and runtimes. Local
evaluation should freeze prompt templates and compare the reference checkpoint, quantized build,
and application wrapper separately.

#### Deployment and evaluation consequences

Approx. 26.7 GB BF16, 13.4 GB SFP8, 6.7 GB Q4_0. Add KV cache, runtime workspace, speculative
draft model, multimodal encoders or projectors, batch buffers, and framework overhead. Record
exact revision, precision, quantizer, context cap, attention backend, processor, device, and
tokens per second.

#### Limits, unknowns, and misleading shortcuts to avoid

Open weights disclose far more than hosted APIs, but they do not disclose every training
example, guarantee runtime compatibility, or promise that a four-bit conversion preserves tool
calling, visual grounding, and long-context behavior.

#### Practical verdict

Gemma 4 12B should be selected by hardware and task, not by family prestige. Its announcement
value is the combination of transparent architecture and a clearly targeted deployment envelope.

### Gemma 4 26B-A4B: Sparse high-throughput reasoning model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-04 launch family; model card updated 2026-06-26 |
| Release state | Open weights for pre-trained and instruction-tuned variants |
| Model identifier | First-party Google/Hugging Face identifier for Gemma 4 26B-A4B |
| Intended role | Sparse high-throughput reasoning model |
| Modalities and product surface | Text and image, with exact variant modality support from the card |
| Context or generation envelope | 256K |
| Pricing | Self-hosted economics; hosted availability varies by surface |
| Weights and license | Open weights with responsible commercial use under Gemma terms |
| Architecture disclosure | MoE, 26B total / about 4B active; 30 text layers; hidden size 2816; query/KV heads 16 / 8; global KV 2; hybrid local/global attention |

#### Launch story

Gemma 4 26B-A4B is one member of Google’s five-model Gemma 4 release, a family built to cover
mobile devices, laptops, workstations, and servers without pretending that one checkpoint suits
every system. The 26B-A4B selects eight of 128 experts per token. Active compute is small
relative to total storage, making it attractive for throughput once the full checkpoint and
expert routing infrastructure are handled correctly.

#### Capabilities and product behavior

All Gemma 4 variants add configurable thinking, native system-role support, function calling,
multimodal understanding according to the exact variant, hybrid attention, and a dedicated draft
model for speculative decoding. The family supports more than 140 languages and increases
context to 128K or 256K by size.

#### Benchmarks, results, and what they actually establish

Google describes frontier-level performance at each size and publishes model-card benchmark
tables. Those are vendor results tied to specific checkpoints, prompts, and runtimes. Local
evaluation should freeze prompt templates and compare the reference checkpoint, quantized build,
and application wrapper separately.

#### Deployment and evaluation consequences

Approx. 57.7 GB BF16, 28.8 GB SFP8, 14.4 GB Q4_0. Add KV cache, runtime workspace, speculative
draft model, multimodal encoders or projectors, batch buffers, and framework overhead. Record
exact revision, precision, quantizer, context cap, attention backend, processor, device, and
tokens per second.

#### Limits, unknowns, and misleading shortcuts to avoid

Open weights disclose far more than hosted APIs, but they do not disclose every training
example, guarantee runtime compatibility, or promise that a four-bit conversion preserves tool
calling, visual grounding, and long-context behavior.

#### Practical verdict

Gemma 4 26B-A4B should be selected by hardware and task, not by family prestige. Its
announcement value is the combination of transparent architecture and a clearly targeted
deployment envelope.

### Gemma 4 31B: Largest dense Gemma 4 model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-04 launch family; model card updated 2026-06-26 |
| Release state | Open weights for pre-trained and instruction-tuned variants |
| Model identifier | First-party Google/Hugging Face identifier for Gemma 4 31B |
| Intended role | Largest dense Gemma 4 model |
| Modalities and product surface | Text and image input to text |
| Context or generation envelope | 256K |
| Pricing | Self-hosted economics; hosted availability varies by surface |
| Weights and license | Open weights with responsible commercial use under Gemma terms |
| Architecture disclosure | Dense; 60 text layers; hidden size 5376; query/KV heads 32 / 16; global KV 4; hybrid local/global attention |

#### Launch story

Gemma 4 31B is one member of Google’s five-model Gemma 4 release, a family built to cover mobile
devices, laptops, workstations, and servers without pretending that one checkpoint suits every
system. The 31B model is the dense workstation/server endpoint of the family. It avoids MoE
routing complexity but applies all 31B parameters per token, so quantization and optimized
attention become central to local usability.

#### Capabilities and product behavior

All Gemma 4 variants add configurable thinking, native system-role support, function calling,
multimodal understanding according to the exact variant, hybrid attention, and a dedicated draft
model for speculative decoding. The family supports more than 140 languages and increases
context to 128K or 256K by size.

#### Benchmarks, results, and what they actually establish

Google describes frontier-level performance at each size and publishes model-card benchmark
tables. Those are vendor results tied to specific checkpoints, prompts, and runtimes. Local
evaluation should freeze prompt templates and compare the reference checkpoint, quantized build,
and application wrapper separately.

#### Deployment and evaluation consequences

Approx. 69.9 GB BF16, 34.9 GB SFP8, 17.5 GB Q4_0. Add KV cache, runtime workspace, speculative
draft model, multimodal encoders or projectors, batch buffers, and framework overhead. Record
exact revision, precision, quantizer, context cap, attention backend, processor, device, and
tokens per second.

#### Limits, unknowns, and misleading shortcuts to avoid

Open weights disclose far more than hosted APIs, but they do not disclose every training
example, guarantee runtime compatibility, or promise that a four-bit conversion preserves tool
calling, visual grounding, and long-context behavior.

#### Practical verdict

Gemma 4 31B should be selected by hardware and task, not by family prestige. Its announcement
value is the combination of transparent architecture and a clearly targeted deployment envelope.

### DiffusionGemma 26B-A4B: Google’s experimental blockwise discrete-diffusion text generator

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-06-10 |
| Release state | Experimental open model under Apache 2.0 |
| Model identifier | `google/diffusiongemma-26B-A4B-it` |
| Intended role | Fast local generation research |
| Modalities and product surface | Text, image, and video input to text output |
| Context or generation envelope | Up to 256K; 256-token generation canvases |
| Pricing | Self-hosted |
| Weights and license | Open; Apache 2.0 |
| Architecture disclosure | 25.2B total / 3.8B active MoE; 30 layers, 16 query heads, 8 KV heads, 128 experts with 8 selected; blockwise discrete diffusion |

#### Launch story

DiffusionGemma changes the generation process rather than merely shrinking Gemma 4. It uses an
autoregressive encoder for prompt context and iteratively denoises token canvases with
bidirectional attention, allowing many output positions to be refined in parallel.

#### Capabilities and product behavior

The model supports thinking, text/image/video understanding, local execution, and parallel
generation over 256-token blocks. Google positions it for low-latency experimentation and
explicitly keeps standard Gemma 4 as the production-quality recommendation when output quality
is primary.

#### Benchmarks, results, and what they actually establish

Google advertises up to roughly four-times generation speed under specified conditions.
Reproduce that claim on the same hardware, precision, output length, denoising schedule, and
baseline. Add diffusion-specific metrics: block-boundary coherence, revision stability, time to
first useful block, end-to-end latency, and degradation on sequential reasoning.

#### Deployment and evaluation consequences

Google says quantized builds can fit within roughly 18 GB VRAM. Record the exact inference
stack, number of denoising steps, canvas utilization, accelerator, precision, batch size, and
quality comparison against Gemma 4 26B-A4B.

#### Limits, unknowns, and misleading shortcuts to avoid

Parallel canvas generation can trade coherence for speed, and cloud-scale batching may favor
autoregressive models differently from single-user local inference.

#### Practical verdict

DiffusionGemma is an important architecture experiment, not an automatic upgrade. Its success
depends on measured latency-quality tradeoffs.

### Grok 4.5: SpaceXAI’s fast frontier model for coding, agents, and knowledge work

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-07-08 |
| Release state | Available in Grok Build, Cursor, and API, with regional caveats at launch |
| Model identifier | `grok-4.5` |
| Intended role | Coding, engineering agents, office work, and live-search workflows |
| Modalities and product surface | Text, tools, repository operation, office artifacts, web and X search through supported products |
| Context or generation envelope | Long-context policy from live xAI documentation; inputs over 200K have separately reported economics |
| Pricing | $2 input / $6 output per million tokens |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed; xAI discloses training infrastructure and methods, not checkpoint dimensions |

#### Launch story

Grok 4.5 is positioned as SpaceXAI’s strongest model and the default engine in Grok Build. The
launch emphasizes engineering realism, fast inference, token efficiency, long agent rollouts,
office-document work, and training alongside Cursor rather than presenting the model only as a
chat upgrade.

#### Capabilities and product behavior

The model handles repository search, multi-file edits, terminal commands, tests, failure
recovery, subagents, web and X search, spreadsheets, Word documents, and PowerPoint. xAI reports
serving around 80 output tokens per second and says the model uses roughly half the steps of
comparable systems on selected tasks.

#### Benchmarks, results, and what they actually establish

xAI reports 62.0% on DeepSWE 1.0, 53% on DeepSWE 1.1, 29.0% on SWE Marathon, 83.3% on
Terminal-Bench 2.1, and 64.7% on SWE-Bench Pro in the cited launch configurations. It also
reports 15,954 average output tokens per SWE-Bench Pro task, about 4.2 times fewer than Opus 4.8
Max in that chart. Artificial Analysis reports 54 on Intelligence Index v4.1 and 76 in the Grok
Build coding composite. Harness and source differences must remain visible.

#### Deployment and evaluation consequences

A good Grok Build work order names repository root, allowed paths, commands, failure-recovery
rules, search boundaries, and final evidence. API users must supply their own tool loop and must
not assume the raw model automatically receives a terminal, browser, or X search.

#### Limits, unknowns, and misleading shortcuts to avoid

Parameter count, layers, MoE topology, context mechanism, serving precision, and training-token
totals are undisclosed. Launch benchmark charts mix vendor and external sources, so each row
needs its original methodology.

#### Practical verdict

Grok 4.5 is a strong price-speed-engineering release. Its practical ranking will depend heavily
on Grok Build’s harness reliability and the user’s need for live search.

### Meta Muse Spark 1.1: Meta’s million-token reasoning model for personal agents and multi-agent orchestration

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-07-09 |
| Release state | Thinking mode in Meta AI and public preview through Meta Model API |
| Model identifier | Muse Spark 1.1 identifier from the live Meta API catalog |
| Intended role | Personal agents, computer use, coding, multimodal workflows, and orchestration |
| Modalities and product surface | Text, visual and audio understanding, tools, computer use, and subagents through supported surfaces |
| Context or generation envelope | 1M tokens with active context management and compaction |
| Pricing | Artificial Analysis reports $1.25 input / $4.25 output per million Meta API tokens |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

Muse Spark 1.1 is Meta’s shift from a reasoning model that answers tasks to a system trained to
organize them. The announcement centers on planning, delegation, context compaction,
cross-application computer use, coding, and the ability to operate either as the main agent or
as a disciplined subagent.

#### Capabilities and product behavior

Meta says the model zero-shot generalizes to native tools, MCP servers, and custom skills;
manages a million-token context; chooses between scripts and direct UI actions; navigates
changing interfaces; diagnoses codebase bugs; builds and validates web applications; and
combines visual or audio perception with action.

#### Benchmarks, results, and what they actually establish

Meta reports substantial gains over the original Muse Spark on internal coding and
personal-agent evaluations and describes competitiveness with leading alternatives. Artificial
Analysis reports 51 on Intelligence Index v4.1 and roughly 116.3 output tokens per second. Those
independent measurements do not establish equal performance to Luna, despite similar rounded
composite scores.

#### Deployment and evaluation consequences

Evaluate Muse in the exact agent surface that supplies tools, compaction, permissions, and
subagents. Record tool schemas, context-compaction events, UI actions, scripts, retries,
security prompts, and final task completion. Computer-use evaluations should include prompt
injection, changing state, recovery, and irreversible-action confirmation.

#### Limits, unknowns, and misleading shortcuts to avoid

Meta does not publish parameter count, layers, expert topology, multimodal encoder construction,
training tokens, or API-serving precision. Internal coding benchmarks are not externally
reproducible without the task set.

#### Practical verdict

Muse Spark 1.1 is an orchestration-first release whose value will be visible in long workflows,
not in a one-turn trivia contest.

### Gemini 3.5 Flash: Google’s stable high-speed frontier model for agents and coding

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-05-19 |
| Release state | Stable Gemini API model and broadly deployed Google product model |
| Model identifier | `gemini-3.5-flash` |
| Intended role | Rapid agent loops, coding, subagents, search, computer use, and high-scale workflows |
| Modalities and product surface | Text, image, audio, video and extensive tools according to the live model page |
| Context or generation envelope | Long context from the current model card; exact input/output limits should be read from the live API page |
| Pricing | Current Gemini API pricing varies by token band and service tier |
| Weights and license | Closed hosted model |
| Architecture disclosure | Undisclosed |

#### Launch story

Gemini 3.5 Flash is Google’s attempt to erase the old assumption that frontier intelligence must
be slow. The launch makes Flash the first release in a 3.5 series built around “intelligence
with action,” combining coding, long-horizon agents, subagent deployment, multimodal
understanding, and Google’s tool ecosystem.

#### Capabilities and product behavior

The developer surface supports Search, Maps, File Search, code execution, URL Context, function
calling, computer use, structured output, and other Gemini tools. Computer use became a built-in
path in June 2026, with optional safeguards for confirmation of sensitive actions and stopping
on indirect prompt injection.

#### Benchmarks, results, and what they actually establish

Google reports 76.2% on Terminal-Bench 2.1, 1656 Elo on GDPval-AA, 83.6% on MCP Atlas, and 84.2%
on CharXiv Reasoning. It also says the model runs around four times faster than other frontier
models in its comparison. Artificial Analysis reports 50.2 on Intelligence Index v4.1. Vendor
benchmark figures and independent composites must not be merged without matching harnesses.

#### Deployment and evaluation consequences

Use `minimal`, `low`, `medium`, or `high` reasoning according to task and latency needs,
recording the choice. Match tools, token budgets, timeouts, and confirmation policy when
comparing with Codex, Claude Code, or Grok Build. For computer use, implement action review,
prompt-injection defense, and irreversible-action gates.

#### Limits, unknowns, and misleading shortcuts to avoid

Google does not disclose parameter count, layers, MoE routing, encoder topology, training data,
or serving precision. Gemini 3.x does not support image segmentation in the cited developer
guide.

#### Practical verdict

Gemini 3.5 Flash is a formidable agent platform because of speed and tool breadth, but its
benchmark story only becomes meaningful when the same tools and deadlines are used across
competitors.

### GPT-Live-1: OpenAI’s full-duplex conversational model for continuous listening and speaking

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-07-08 |
| Release state | Available in documented paid ChatGPT voice paths and live product surfaces |
| Model identifier | GPT-Live-1 product/API identifier from current OpenAI documentation |
| Intended role | Natural real-time conversation with interruption, tools, and delegated reasoning |
| Modalities and product surface | Streaming audio in and audio out, with product-dependent visual or tool context |
| Context or generation envelope | Streaming session limits rather than a conventional document context headline |
| Pricing | Product and API pricing from current OpenAI live-model documentation |
| Weights and license | Closed |
| Architecture disclosure | OpenAI describes continuous full-duplex processing but does not publish checkpoint dimensions |

#### Launch story

GPT-Live-1 is announced as a conversation system that listens while it speaks, speaks while it
listens, and repeatedly decides whether to continue, pause, interrupt, or call a tool. The
architectural story is therefore system-level: a low-latency speech loop can delegate deeper
research or reasoning to a stronger text model without freezing the conversation.

#### Capabilities and product behavior

The model supports overlap, interruptions, pauses, emotional and acoustic cues, tool delegation,
and voice-native interaction. Medium and High product paths can route deeper work through a
current thinking model while the live model maintains the spoken exchange.

#### Benchmarks, results, and what they actually establish

Traditional text scores do not capture the release. Measure recognition accuracy, interruption
success, false interruption rate, pause handling, overlap recovery, time to first audio, time to
corrected answer after delegation, tool-call latency, transcript agreement, and conversation
completion under real network conditions.

#### Deployment and evaluation consequences

Record microphone and playback devices, codec, sample rate, packet size, network conditions,
echo cancellation, background noise, tool configuration, delegation model, transcript settings,
and privacy policy. Test multilingual names, numbers, rapid turn-taking, silence, and
two-speaker overlap.

#### Limits, unknowns, and misleading shortcuts to avoid

Transcripts may not be verbatim; background noise and fast overlap can reduce stability. The
launch does not disclose parameter count, layer design, audio tokenizer, acoustic encoder, or
one fixed end-to-end latency.

#### Practical verdict

GPT-Live-1 is a system architecture for conversation, not simply a text model with speech bolted
on. Evaluate the loop, not a transcript screenshot.

### GPT-Live-1 Mini: The lower-cost live-conversation path for broad access

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-07-08 |
| Release state | Documented free or entry path in the GPT-Live product family |
| Model identifier | GPT-Live-1 Mini identifier from live documentation |
| Intended role | Fast everyday voice conversation |
| Modalities and product surface | Streaming audio in and audio out |
| Context or generation envelope | Session-based |
| Pricing | Lower-cost/free-path economics by product surface |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

GPT-Live-1 Mini carries the live architecture into a lower-cost access tier. It is intended to
preserve natural interruption and continuous conversation while accepting a lower capability
ceiling than the full model.

#### Capabilities and product behavior

Mini is appropriate for everyday conversation, simple assistance, language practice, lightweight
support, and low-latency voice interfaces. Product routing can still use background models for
some tasks, so the visible result may reflect a system rather than one checkpoint.

#### Benchmarks, results, and what they actually establish

Compare Mini with GPT-Live-1 on identical audio: word and number accuracy, interruption
handling, false starts, pause respect, tool latency, emotional nuance, and successful
completion. Cost and latency should be reported alongside quality.

#### Deployment and evaluation consequences

Use Mini when the conversation itself matters more than difficult reasoning. Escalate complex
analysis to a stronger text or live path explicitly rather than allowing silent quality drift.

#### Limits, unknowns, and misleading shortcuts to avoid

OpenAI does not disclose topology, parameter scale, training data, or exact relationship to
GPT-Live-1. “Mini” is a product role, not a published architectural ratio.

#### Practical verdict

Mini is the volume voice tier. Its success is natural interaction per unit cost, not matching
the full model on every reasoning task.

### Gemini 3.5 Flash Live Translate: Google’s preview simultaneous-translation model for more than 70 languages

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026 |
| Release state | Public preview |
| Model identifier | `gemini-3.5-live-translate-preview` |
| Intended role | Streaming speech-to-speech translation |
| Modalities and product surface | Audio input to translated audio with optional transcripts |
| Context or generation envelope | Continuous streaming session |
| Pricing | Current Gemini Live API pricing |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed specialized streaming translation system |

#### Launch story

Live Translate is a narrow model announcement by design. Rather than exposing the general tool
and reasoning stack of Gemini 3.5 Flash, it focuses on low-latency interpretation with
predictable target-language routing, acoustic continuity, and optional transcripts.

#### Capabilities and product behavior

Google documents more than 70 languages, recommended 16 kHz mono PCM input, 24 kHz PCM output,
and roughly 100 ms input chunks. The model does not support tool calling, search grounding,
function calling, system instructions, or thinking controls.

#### Benchmarks, results, and what they actually establish

Test both directions for every target pair. Include names, numbers, technical terms, dialect
shifts, emotional tone, interruptions, long pauses, and overlapping speakers. Score meaning
preservation, latency, proper nouns, tone, omission, addition, and whether the system waits for
turn boundaries or translates continuously.

#### Deployment and evaluation consequences

Use stable audio capture, headphones, echo control, explicit BCP-47 target codes, and logs that
align source audio, translated audio, and transcript timestamps. Preview quotas and behavior can
change.

#### Limits, unknowns, and misleading shortcuts to avoid

It is not a general conversational agent and should not be ranked against GPT-Live-1 on tools or
open-ended reasoning. Architecture and training data are undisclosed.

#### Practical verdict

Live Translate should be judged as an interpreter: faithful, fast, stable, and clear, rather
than broadly intelligent.

### GPT Image 2: OpenAI’s state-of-the-art image generation and editing model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026 |
| Release state | Available through OpenAI image-generation product and API paths |
| Model identifier | `gpt-image-2` |
| Intended role | High-quality generation, typography, editing, and reference consistency |
| Modalities and product surface | Text and image input to image output |
| Context or generation envelope | Image API controls rather than a text-model context claim |
| Pricing | Current OpenAI Images API pricing by size and quality |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed; no official source confirms a fully autoregressive or hybrid diffusion pipeline |

#### Launch story

GPT Image 2 is presented as an image system for production work rather than novelty prompts.
OpenAI emphasizes prompt adherence, typography, precise editing, reference consistency, and
high-fidelity image input, all of which should be inspected at original resolution.

#### Capabilities and product behavior

The model supports text-to-image generation, image-to-image editing, multiple sizes and aspect
ratios, detailed reference use, layout work, and tool-mediated image creation. In ChatGPT, a
reasoning model may help plan or rewrite a prompt, but that product behavior does not reveal the
generator’s architecture.

#### Benchmarks, results, and what they actually establish

Build a fixed suite for text rendering, object count, spatial constraints, identity consistency,
localized edits, multi-reference composition, style control, and iterative edit preservation.
Report success rate, human preference, edit leakage, text accuracy, latency, and cost.

#### Deployment and evaluation consequences

Keep prompts, references, seeds where available, sizes, quality settings, and edit histories.
Save original files because social-media compression hides typography and edge defects.

#### Limits, unknowns, and misleading shortcuts to avoid

OpenAI does not publish parameter count, latent space, image tokenizer, diffusion schedule,
autoregressive token order, or training corpus. Visual artifact patterns cannot prove the
architecture.

#### Practical verdict

GPT Image 2 should be treated as a high-control production image model with undisclosed
internals, not as evidence for a favorite architecture theory.

### Nano Banana 2: Google’s general-purpose Gemini 3.1 Flash Image model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026 |
| Release state | Current Gemini image-generation model |
| Model identifier | `gemini-3.1-flash-image` |
| Intended role | Balanced quality, speed, editing, reference consistency, and 4K output |
| Modalities and product surface | Text and image input to image output |
| Context or generation envelope | Image-generation request limits from the live API |
| Pricing | Current Gemini API image pricing |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

Nano Banana 2 is the mainstream member of Google’s current image family. It is designed to
combine quick iteration with better typography, search-grounded current knowledge, subject
consistency, editing, multiple references, and resolutions up to 4K.

#### Capabilities and product behavior

The model supports generation, targeted edits, search grounding where enabled, thinking controls
where documented, text rendering, localization, and iterative workflows. Search and thinking
must be recorded because they alter latency, cost, and the information available to the model.

#### Benchmarks, results, and what they actually establish

Compare it on poster text, diagrams, character identity, product mockups, object placement,
reference fidelity, and sequential edits. Use exact prompts and full-resolution outputs, and
distinguish current-knowledge success caused by Search from base-model behavior.

#### Deployment and evaluation consequences

Use Nano Banana 2 for general production and interactive editing. Preserve reference rights,
output provenance, and edit histories.

#### Limits, unknowns, and misleading shortcuts to avoid

Google does not disclose the image backbone, parameter count, training corpus, or whether
planning and rendering use separate internal models.

#### Practical verdict

Nano Banana 2 is the balanced Google image path, not Gemini 3 Pro Image under another name.

### Nano Banana Pro: Google’s Gemini 3 Pro Image model for maximum control and professional layouts

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026 |
| Release state | Available in supported Google product and API surfaces |
| Model identifier | `gemini-3-pro-image` |
| Intended role | Professional image generation, typography, localization, and complex composition |
| Modalities and product surface | Text and image input to image output |
| Context or generation envelope | Image request limits from current documentation |
| Pricing | Current Google image pricing |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

Nano Banana Pro is the quality-and-control endpoint of Google’s image family. Google emphasizes
world knowledge, typography, localization, complex layouts, and professional production rather
than the low-latency volume role of the Flash and Lite variants.

#### Capabilities and product behavior

Use it for dense posters, diagrams, localized campaigns, reference-heavy compositions,
consistent subjects, and edits where unmentioned content must remain stable.

#### Benchmarks, results, and what they actually establish

The correct comparison with Nano Banana 2 uses identical briefs, references, resolutions, and
scoring for text accuracy, layout, identity, edit leakage, prompt adherence, latency, and cost.
A prettier single sample is not an evaluation.

#### Deployment and evaluation consequences

Choose Pro when correction time and layout control matter more than generation speed. Keep
original exports and review text at 100% zoom.

#### Limits, unknowns, and misleading shortcuts to avoid

No public architecture, parameter, layer, tokenizer, or training-data details are established.
“Pro” is a product role, not proof of a separate rendering method.

#### Practical verdict

Nano Banana Pro is the Google choice for difficult image briefs where the cost of manual repair
exceeds the extra inference cost.

### Nano Banana 2 Lite: Google’s ultra-low-latency Gemini 3.1 Flash Lite Image model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-06-30 public update |
| Release state | Available through documented Gemini image surfaces |
| Model identifier | `gemini-3.1-flash-lite-image` |
| Intended role | High-volume drafts, brainstorming, and fast generation |
| Modalities and product surface | Text and image input to image output |
| Context or generation envelope | Image request limits from the live API |
| Pricing | Lowest-cost current Google image tier |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

Nano Banana 2 Lite is explicitly designed to sacrifice some control for speed and price. Google
targets approximately four-second generation in launch material and positions the model for
iteration, brainstorming, and high-volume workloads.

#### Capabilities and product behavior

It supports generation and editing, but is not optimized for many reference images or long
sequential editing chains. That boundary should be treated as a product-design fact rather than
challenged through increasingly elaborate prompts.

#### Benchmarks, results, and what they actually establish

Measure first-pass prompt adherence, text accuracy, edit success, reference count tolerance,
latency distribution, and accepted outputs per dollar. Compare on draft tasks, not only on the
hardest Pro-oriented layout.

#### Deployment and evaluation consequences

Use Lite as a draft engine with deterministic review and escalation to Nano Banana 2 or Pro for
difficult compositions.

#### Limits, unknowns, and misleading shortcuts to avoid

Lower latency does not disclose quantization, distillation, parameter count, or generator
architecture.

#### Practical verdict

Lite is useful when speed is the product. It is not an automatic replacement for Pro merely
because a launch demo returned quickly.

### Seedream 5.0 Pro: ByteDance Dreamina’s professional image generation and editing system

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026 |
| Release state | Available through the Dreamina product surface |
| Model identifier | Product identifier from Dreamina rather than a broadly documented public API ID |
| Intended role | Professional generation, editing, typography, layout, and reference control |
| Modalities and product surface | Text and image input to image output |
| Context or generation envelope | Product-specific |
| Pricing | Current Dreamina plan or credit pricing |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed; limited first-party English technical disclosure |

#### Launch story

Seedream 5.0 Pro is positioned as a professional creative model with generation, editing,
typography, reference control, production layouts, and prompt adherence. Its challenge for a
technical guide is evidence depth: the public English product material provides less
architecture and benchmark detail than several competitors.

#### Capabilities and product behavior

The model should be tested on typography, localized layouts, precise edits, product imagery,
subject consistency, multiple references, and prompt fidelity.

#### Benchmarks, results, and what they actually establish

No independent universal score is asserted here. Use exact prompts, references, aspect ratios,
and a blinded human rubric. Inspect original outputs for small text errors, boundary artifacts,
and reference drift.

#### Deployment and evaluation consequences

Record the Dreamina surface, plan, region, generation settings, references, and edit chain. Do
not extrapolate a web-product result to an undocumented API.

#### Limits, unknowns, and misleading shortcuts to avoid

Internal architecture, parameter scale, web search, reasoning, training data, watermarking, and
API availability require explicit current documentation.

#### Practical verdict

Seedream 5.0 Pro belongs in serious image comparisons, but its technical claims must remain
narrower than its marketing until first-party disclosure improves.

### Muse Image: Meta’s agentic image generation and editing model with search and coding tools

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-07-07 |
| Release state | Rolled out across Meta AI surfaces with geography and product differences |
| Model identifier | Meta product identifier from the current Model API where available |
| Intended role | Agentic generation, editing, multi-reference composition, and self-refinement |
| Modalities and product surface | Text, image references, tools, and image output |
| Context or generation envelope | Product-specific |
| Pricing | Meta product/API pricing where available |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

Muse Image is announced not merely as a renderer but as an agentic image system. Meta says it
can use search and coding tools, plan, self-refine, combine multiple references, and work with
Muse Spark to complete visual tasks that require both information gathering and generation.

#### Capabilities and product behavior

The product targets generation, editing, composition, reference control, grounded visual work,
and iterative improvement. Meta applies its Content Seal invisible provenance signal to images
created in Meta AI and on meta.ai.

#### Benchmarks, results, and what they actually establish

Meta presents arena and internal comparisons, but production evaluation still needs text
rendering, edit leakage, reference fidelity, factual grounding, identity consistency, latency,
and accepted-output cost. Tool-enabled results must be marked separately from base generation.

#### Deployment and evaluation consequences

Record the Meta surface, country, tool availability, search use, reference count, output
provenance, and editing history. Watermarking supports provenance but does not replace rights
review or factual checking.

#### Limits, unknowns, and misleading shortcuts to avoid

Checkpoint architecture, parameter count, renderer type, training corpus, and API parity across
Meta products are undisclosed.

#### Practical verdict

Muse Image’s differentiator is the agent around the generator. Test the entire workflow, not
only the final pixels.

### Muse Video: Meta’s preview video model focused on fidelity, native audio, and physical motion

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-07-07 announcement |
| Release state | Early preview / coming soon in this snapshot |
| Model identifier | No generally available production identifier established |
| Intended role | Video generation with native audio and agentic workflow integration |
| Modalities and product surface | Planned text and visual input to video with audio |
| Context or generation envelope | Undisclosed |
| Pricing | Undisclosed |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

Muse Video appears as Meta’s next multimodal generation step, with public emphasis on visual
fidelity, native audio, audio-video synchronization, and physically accurate fast motion. The
guide treats those as announced research goals rather than a production contract.

#### Capabilities and product behavior

Expected use cases include cinematic generation, synchronized sound, motion-heavy scenes,
editing, and integration with Muse Spark or Meta creative products.

#### Benchmarks, results, and what they actually establish

Once available, test temporal consistency, object persistence, motion physics, audio
synchronization, dialogue alignment, edit continuity, latency, provenance, and cost. Still-image
preferences are insufficient.

#### Deployment and evaluation consequences

No integration recipe should be published until Meta provides an identifier, access method,
limits, pricing, and safety terms.

#### Limits, unknowns, and misleading shortcuts to avoid

Availability, API, architecture, duration, resolution, frame rate, extension, editing,
watermarking, and rights terms remain incomplete.

#### Practical verdict

Muse Video is a credible watchlist item, not yet a production recommendation.

### Veo 3.1 Lite Preview: Google’s lower-cost developer video model with audio output

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-03-31 |
| Release state | Public preview |
| Model identifier | `veo-3.1-lite-generate-preview` |
| Intended role | High-volume video generation and rapid iteration |
| Modalities and product surface | Text and image input to video with audio output |
| Context or generation envelope | 1,024 text-input tokens; one output video per request |
| Pricing | Lowest-cost Veo 3.1 tier in current Google pricing |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed hosted video model |

#### Launch story

Veo 3.1 Lite takes the core Veo 3.1 generation stack and packages it for scalable developer use.
Google emphasizes high fidelity, editing, cinematic control, generated audio, and lower cost,
while clearly withholding some premium features.

#### Capabilities and product behavior

The preview supports text-to-video and image-to-video with audio. The broader Veo 3.1 family can
generate 720p, 1080p, or 4K, but Lite does not support 4K or video Extension in the reviewed
documentation.

#### Benchmarks, results, and what they actually establish

Evaluate prompt adherence, motion plausibility, object persistence, camera control, temporal
artifacts, lip/audio alignment, edit continuity, latency, and price. Review complete sequences
frame by frame rather than selecting a flattering still.

#### Deployment and evaluation consequences

Record model ID, date, resolution, duration, references, audio brief, safety settings, region,
and original output. Preview behavior and limits can change.

#### Limits, unknowns, and misleading shortcuts to avoid

One video per request, no 4K, and no Extension are explicit current constraints. Architecture
and training data remain undisclosed.

#### Practical verdict

Veo 3.1 Lite is the volume developer path, valuable when its missing premium features are not
required.

### Lyria 3 Clip Preview: Google’s 30-second music generation model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-03-25 |
| Release state | Public preview |
| Model identifier | `lyria-3-clip-preview` |
| Intended role | Short musical ideas, loops, demos, and rapid iteration |
| Modalities and product surface | Text and image input to MP3 stereo audio |
| Context or generation envelope | 30-second clip-oriented generation |
| Pricing | Current Gemini API music pricing |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed music-generation system |

#### Launch story

Lyria 3 Clip is the quick-iteration member of Google’s music family. It is built for short
prompted clips where texture, hook, instrumentation, and immediate prompt adherence matter more
than long-form song structure.

#### Capabilities and product behavior

The model supports original lyrics, instrumental or vocal intent, mood, tempo, instrumentation,
and image-conditioned generation. The current guide reports 44.1 kHz stereo output, while an
older changelog reported 48 kHz; the discrepancy should remain visible until Google resolves it.

#### Benchmarks, results, and what they actually establish

Score musical structure within the short window, rhythm and harmony, vocal intelligibility,
prompt adherence, repetition, artifacts, and editability. A strong 30-second loop does not
establish verse-chorus coherence.

#### Deployment and evaluation consequences

Use original lyrics and rights-cleared references. Record prompt, model ID, sample rate, output
format, and commercial terms.

#### Limits, unknowns, and misleading shortcuts to avoid

Architecture, training data, stem access, exact provenance systems, and long-form continuity are
not inferred.

#### Practical verdict

Lyria 3 Clip is for ideas and short assets, not proof of full-song competence.

### Lyria 3 Pro Preview: Google’s longer-form prompted music model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-03-25 |
| Release state | Public preview |
| Model identifier | `lyria-3-pro-preview` |
| Intended role | Longer songs and structured musical generation |
| Modalities and product surface | Text and image input to MP3 stereo audio |
| Context or generation envelope | Longer prompted songs than the Clip model |
| Pricing | Current Gemini API music pricing |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed |

#### Launch story

Lyria 3 Pro extends the release from short clips into longer prompted songs, where structure,
transitions, lyric continuity, instrumentation, and repetition become substantially harder.

#### Capabilities and product behavior

Prompts can specify vocal or instrumental output, language, mood, tempo, instrumentation,
sections, duration, and original lyrics.

#### Benchmarks, results, and what they actually establish

Evaluate verse and chorus consistency, transitions, long-range harmonic and rhythmic coherence,
vocal intelligibility, pronunciation, repetition, edit continuity, and rights review. Keep Pro
and Clip results separate.

#### Deployment and evaluation consequences

Use a detailed original brief and save the generated audio with model/version metadata. Check
live commercial terms before publishing or monetizing output.

#### Limits, unknowns, and misleading shortcuts to avoid

No public parameter, architecture, training-corpus, or style-filter specification is established
in the guide.

#### Practical verdict

Lyria 3 Pro should be judged as a composition system, not by whether its first eight seconds
make an attractive demo.

### Gemini Omni Flash Preview: Google’s conversational video generation and editing model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-06-30 |
| Release state | Public preview on the paid Gemini API and selected Google products |
| Model identifier | `gemini-omni-flash-preview` |
| Intended role | Fast video generation, animation, native audio, and conversational editing |
| Modalities and product surface | Text, images, and existing video to video with generated audio |
| Context or generation envelope | 1,048,576-token context; current editing input and output limits from model page |
| Pricing | Current paid Gemini API preview pricing |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed unified multimodal service |

#### Launch story

Gemini Omni Flash is a video system organized around conversation. Google allows developers to
generate short clips, animate still images, and then iteratively refine the output through the
Interactions API while attempting to preserve parts of the video that were not mentioned in an
edit.

#### Capabilities and product behavior

The preview produces 3-to-10-second 720p video at 24 frames per second with generated audio. It
accepts text, images, and short existing video for editing. Google emphasizes character and
voice consistency, but those remain quality claims to test across multiple scenes and revisions.

#### Benchmarks, results, and what they actually establish

Measure generation adherence, temporal consistency, character identity, voice consistency, audio
synchronization, edit locality, preservation of untouched regions, latency, and cost.
Conversational editing requires a sequence-level evaluation, not independent prompts.

#### Deployment and evaluation consequences

Record every interaction, source media, requested change, output clip, model date, and preview
limitation. Validate rights and provenance for all input media.

#### Limits, unknowns, and misleading shortcuts to avoid

Uploaded audio references, multi-video reasoning, extension, interpolation, and voice editing
are unsupported in the reviewed preview. Some schema-accepted video references are documented as
not processing correctly.

#### Practical verdict

Omni Flash is a promising editable-video workflow, but preview limitations must be treated as
hard engineering constraints.

### Gemini Robotics-ER 1.6: Google’s preview embodied-reasoning VLM for perception and high-level robot planning

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | 2026-04-14 |
| Release state | Preview |
| Model identifier | `gemini-robotics-er-1.6-preview` |
| Intended role | Spatial understanding, object localization, task decomposition, and tool-mediated robotics |
| Modalities and product surface | Text, images, video, and audio input to text or structured outputs |
| Context or generation envelope | 131,072 input tokens; 65,536 output tokens |
| Pricing | Current Gemini API robotics pricing and consumption tiers |
| Weights and license | Closed |
| Architecture disclosure | Undisclosed VLM |

#### Launch story

Robotics-ER 1.6 brings Gemini’s reasoning and tool interfaces into physical-world planning.
Google emphasizes object and scene understanding, affordances, spatial and temporal reasoning,
structured coordinates, task decomposition, function calls, code execution, and adjustable
thinking budget.

#### Capabilities and product behavior

The model can identify objects, point or bound them, interpret instructions, sequence subtasks,
read instruments, reason about physical relationships, and request user-provided robot
functions. The output is still a model proposal until a controller validates and executes it.

#### Benchmarks, results, and what they actually establish

Separate perception accuracy, coordinate error, counting, gauge reading, constraint
satisfaction, plan quality, schema validity, recovery, simulation success, collisions, near
misses, and operator interventions. High-level benchmark success does not certify low-level
control.

#### Deployment and evaluation consequences

Place an independent safety controller between the model and hardware. Enforce action limits,
sensor checks, collision handling, confirmation, emergency stop, monitoring, and staged
simulation-to-real trials. Log model version, thinking budget, sensor stream, tool calls,
operator decisions, and interventions.

#### Limits, unknowns, and misleading shortcuts to avoid

Google explicitly warns that generative models make mistakes and robots can cause damage. The
architecture, training data, and physical reliability envelope remain undisclosed.

#### Practical verdict

Robotics-ER 1.6 is a planning and perception component, never the sole safety authority for a
physical machine.

### Gemini 3.5 Pro: Google’s announced but unreleased next Pro model

| Release field | Evidence-conscious record |
| --- | --- |
| Announcement / checked date | Watchlist as of 2026-07-12 |
| Release state | “Coming soon”; no documented public or restricted model ID in the checked sources |
| Model identifier | None established |
| Intended role | Future flagship Gemini Pro tier |
| Modalities and product surface | Undisclosed for the unreleased model |
| Context or generation envelope | Undisclosed |
| Pricing | Undisclosed |
| Weights and license | Closed expected, but release terms not announced |
| Architecture disclosure | Undisclosed |

#### Launch story

Gemini 3.5 Pro belongs in the guide only as a watchlist announcement. Google’s current model
page says it is coming soon, but does not provide a model identifier, access instructions,
price, context limit, tool matrix, effort controls, or benchmark methodology.

#### Capabilities and product behavior

No capabilities should be copied from Gemini 3.5 Flash, Gemini 3.1 Pro, Deep Think, or a
consumer UI rumor. Family naming does not establish the unreleased model’s interface.

#### Benchmarks, results, and what they actually establish

No benchmark table should be created until Google publishes results and methodology for the
released model. Third-party screenshots and picker observations are insufficient.

#### Deployment and evaluation consequences

Revisit this entry only after a model page or catalog listing establishes identifier,
availability, modalities, limits, tools, price, and safety material.

#### Limits, unknowns, and misleading shortcuts to avoid

Almost everything is unknown, which is the honest state of the evidence.

#### Practical verdict

A disciplined watchlist is more useful than a fictional prompting guide.


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

<!-- frontier-migration-boundary -->
