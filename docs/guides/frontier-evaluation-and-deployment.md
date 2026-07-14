# Frontier evaluation and deployment

[← Frontier models index](frontier-models-and-multimodal-systems-2026.md)

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



## Comprehensive Architecture, Performance, and Deployment Dossiers

This section expands the concise entries into technical dossiers. It is
intentionally repetitive about evidence boundaries because the same mistake
recurs across model families: a product feature is mistaken for a model
architecture, a harness score is mistaken for a bare-checkpoint score, or an
open-weight label is mistaken for an inexpensive local deployment.

### GPT-5.6 Sol, Terra, and Luna: Architecture Disclosure and Performance Envelope

#### Publicly established model facts

| Field | GPT-5.6 Sol | GPT-5.6 Terra | GPT-5.6 Luna |
| --- | --- | --- | --- |
| Product role | Flagship | Balanced | Fastest/lowest-cost tier |
| API identifier | `gpt-5.6-sol` | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Context | 1.05M input tokens | 1.05M input tokens | 1.05M input tokens |
| Maximum output | 128K tokens | 128K tokens | 128K tokens |
| API reasoning values | `none`, `low`, `medium`, `high`, `xhigh`, `max` | Same | Same |
| Open weights | No | No | No |
| Architecture disclosure level | C | C | C |

The [OpenAI launch page](https://openai.com/index/gpt-5-6/),
[Help Center](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt),
and [API catalog](https://developers.openai.com/api/docs/models) establish the
family, product roles, context/output limits, reasoning controls, pricing, and
surface availability. They do **not** disclose total parameters, active
parameters, layer counts, hidden width, attention-head counts, key/value-head
counts, expert counts, routing topology, tokenizer training data, pretraining
compute, or the exact post-training recipe.

#### Architecture fields that remain undisclosed

| Requested field | Status | Why the guide does not estimate it |
| --- | --- | --- |
| Dense versus MoE | Undisclosed | Throughput and price do not uniquely identify topology |
| Total/active parameters | Undisclosed | No first-party checkpoint or technical report supplies the values |
| Transformer layers | Undisclosed | UI effort levels are inference controls, not network depth |
| Attention type and head counts | Undisclosed | A million-token context can be implemented through several unrelated methods |
| Vision/audio encoders | Undisclosed | Multimodal product behavior does not expose encoder construction |
| Training tokens and data mixture | Undisclosed | Product documentation does not publish a training corpus ledger |
| Quantization | Not applicable to users as a first-party checkpoint choice | Hosted serving precision is an internal service detail |

This disclosure boundary matters. Calling Sol a “larger MoE” or Luna a
“distilled dense model” may sound plausible, but no checked OpenAI source proves
those descriptions. The only defensible family relationship is functional:
OpenAI positions the tiers at different capability, latency, and price points.

#### Effort is test-time policy, not a new checkpoint

`low` through `max` control how much single-model reasoning and tool work the
selected tier performs. `ultra` is an orchestration mode in supported products,
not an API reasoning value and not evidence of a fourth GPT-5.6 checkpoint. A
reproducible report should therefore record three variables separately:

| Variable | Example | Measurement consequence |
| --- | --- | --- |
| Checkpoint/tier | Terra | Changes the capability and token-price envelope |
| Single-model effort | `high` | Changes reasoning/tool budget, latency, and likely output volume |
| Orchestration | Codex Ultra | Adds concurrent agents, synthesis, and coordination overhead |

A benchmark of Sol Max cannot be renamed Sol Ultra. An Ultra project can use
several agents and may outperform a Max run on decomposable work, but it also
changes the experimental object from one model invocation to an orchestrated
system.

#### Independent benchmark interpretation

The dated Artificial Analysis snapshot in this guide reports 58.9 for Sol Max,
55 for Terra Max, and 51.2 for Luna Max on Intelligence Index v4.1. In the Codex
Coding Agent Index it reports 80, 77, and 75 respectively. Those values support
three conclusions and no more:

1. In that evaluator and those Codex configurations, the tier ordering was Sol,
   Terra, then Luna.
2. The smaller tiers retained much of the coding-agent score at lower measured
   task cost.
3. The numbers include the Codex harness and Max effort, so they do not transfer
   automatically to bare API calls, ordinary Chat, Work, or Ultra.

The small gaps also argue against ritualistically selecting the most expensive
model. A bounded repository transformation with a deterministic test can be a
better Terra or Luna workload, while an ambiguous architecture investigation
with conflicting evidence is more likely to justify Sol.

#### Performance dimensions that the composite does not settle

| Dimension | Why it must be tested separately |
| --- | --- |
| Long-context retrieval | Capacity does not prove accurate retrieval near the middle or across conflicting documents |
| Structured output | JSON validity and schema adherence can differ from broad reasoning quality |
| Tool reliability | Call selection, argument validity, recovery, and permission handling depend on the host loop |
| Visual grounding | Coding and intelligence composites do not measure chart reading or pixel-level localization |
| Latency variance | Average time hides long tails caused by reasoning, tools, and service load |
| Safety routing | Refusals and additional checks can alter completion rates on sensitive domains |
| Multi-agent coordination | Ultra adds decomposition and merge failures not present in single-agent tests |

#### Recommended matched evaluation

Run the same 20 to 50 representative tasks at Luna High, Terra High, Sol High,
and the cheapest Max configuration that the budget permits. Freeze the system
prompt, source packet, tool schema, timeout, output validator, and retry policy.
Record task success, human correction minutes, input/output tokens, reasoning
or billed tokens where exposed, tool calls, wall time, and failure category.
Escalate a task class only when the next tier or effort produces a statistically
or operationally meaningful gain. This is less glamorous than declaring a
single champion, which is precisely why it is more useful.

### Claude Fable 5: Safeguarded Frontier Model With an Evaluation Routing Caveat

#### Disclosed product facts and undisclosed architecture

Anthropic's [Fable 5 and Mythos 5 announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5),
[effort documentation](https://platform.claude.com/docs/en/build-with-claude/effort),
and [pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
establish Fable's product position, API price, context policy, effort values,
and safeguard behavior. They do not publish weights or a checkpoint
configuration.

| Architecture field | Public status |
| --- | --- |
| Dense/MoE | Undisclosed |
| Total/active parameters | Undisclosed |
| Layers, width, attention heads, KV heads | Undisclosed |
| Context architecture | Undisclosed beyond the published product window |
| Training tokens and data composition | Undisclosed |
| Reasoning implementation | Undisclosed; effort is a product control, not a topology description |
| First-party quantizations | None for user deployment because weights are not released |

The term “Mythos-class” is a vendor family label. It should not be expanded into
an assumed parameter scale or hidden architecture unless Anthropic publishes a
technical report that does so.

#### Fallback changes the meaning of a score

Anthropic documents circumstances in which safeguarded requests can be handled
by Opus 4.8 with notice. Artificial Analysis labels its Fable configuration
“with fallback.” Therefore a Fable product score can measure a routed system,
not a pure underlying checkpoint. Evaluation logs should include:

- the requested model and effort;
- any visible fallback notice;
- the final model reported by the product where available;
- whether the task belonged to a domain likely to trigger additional review;
- whether the output was refused, partially completed, or rerouted.

Removing the fallback qualifier from a table is not simplification. It changes
the experiment.

#### Performance profile and practical use

The cited Intelligence Index result of 59.9 and Coding Agent Index result of 77
place the tested Fable Max product among the strongest systems in the snapshot.
Its AA-Briefcase lead in rubric and analytical quality suggests particular
strength in long-horizon knowledge work and finished professional artifacts.
Those outcomes still need task-level verification because a composite can hide
weakness in citation precision, spreadsheet manipulation, visual presentation,
or a specific programming language.

Use Fable when analytical depth, long-form synthesis, or sustained agent work
justifies the price and when the routing behavior is acceptable. Prefer a
cleaner Opus comparison when the purpose of the experiment is to isolate one
named checkpoint without the Fable fallback layer.

### Claude Opus 4.8: Closed Checkpoint, Strong Agent Harness, Cleaner Attribution

Opus 4.8 is also a Level C architecture disclosure model. Anthropic publishes
its price, product surfaces, context policy, effort controls, and recommended
use, but not weights, parameter counts, layers, or attention topology.

| Evaluation dimension | What is established | What remains unknown |
| --- | --- | --- |
| Intelligence Index | 55.7 at Max in the cited snapshot | Bare API result under a different prompt/harness |
| Coding Agent Index | 73 in Claude Code | Contribution of model versus Claude Code scaffold |
| API economics | $5/$25 per million input/output tokens in the cited pricing page | Hidden serving precision and provider utilization |
| Effort | `low` through `max`; `xhigh` recommended for demanding coding in cited guidance | Internal compute allocation per label |
| Fallback role | Documented target for specified Fable safeguards | Whether any unrelated request will route in a particular account/session |

Opus is valuable as a stable comparison point because it avoids claiming that
a routed Fable result belongs entirely to Fable. In repository work, however,
Claude Code's system prompt, edit protocol, terminal behavior, compaction, and
permission mode are part of the measured product. A fair API-versus-CLI test
must either reproduce those affordances or explicitly label the comparison as
model plus harness.

### Claude Sonnet 5: Cost-Sensitive Agentic Model With Limited Architecture Disclosure

The [Sonnet 5 launch](https://www.anthropic.com/news/claude-sonnet-5) establishes
its release date, `claude-sonnet-5` identifier, plan availability, introductory
pricing, browser/terminal positioning, and agentic focus. It does not disclose
checkpoint dimensions.

| Field | Status |
| --- | --- |
| Weights/license | Closed; hosted access |
| Dense/MoE and parameter count | Undisclosed |
| Layer/head counts | Undisclosed |
| Context limit | Use the current API/model page for the selected surface; do not infer from other Claude models |
| Tool capability | Product or application supplied; not inherent authority in a bare API call |
| Reasoning/effort menu | Verify against the live API or client; launch text is not a permanent cross-surface menu |
| Price | Introductory $2/$10 through 2026-08-31, then scheduled $3/$15 in the cited launch |

A proper Sonnet evaluation should compare not only answer quality but also
first-pass tool success, malformed-call rate, recovery after a failed command,
context compaction behavior, and human correction time. Because the launch
price changes on a known date, record both experiment date and the rate used in
cost calculations.

### DeepSeek-V4-Pro and DeepSeek-V4-Flash: Open MoE Architecture in Detail

DeepSeek supplies the strongest architecture disclosure in this guide through
the [V4 technical report](https://arxiv.org/abs/2606.19348), official
[release page](https://api-docs.deepseek.com/news/news260424), hosted
[pricing table](https://api-docs.deepseek.com/quick_start/pricing/), and
first-party checkpoint configurations for
[Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/config.json)
and [Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash/blob/main/config.json).

#### Core scale and topology

| Field | DeepSeek-V4-Pro | DeepSeek-V4-Flash |
| --- | ---: | ---: |
| Total parameters | 1.6T | 284B |
| Activated parameters per token | 49B | 13B |
| Architecture | Decoder-only MoE with compressed/sparse attention | Smaller decoder-only MoE with the same V4 design family |
| Transformer layers | 61 | 43 |
| Hidden size | 7168 | 4096 |
| Attention heads | 128 | 64 |
| KV heads | 1 | 1 |
| Routed experts | 384 | 256 |
| Shared experts | 1 | 1 |
| Routed experts selected per token | 6 | 6 |
| MoE intermediate size | 3072 | 2048 |
| Context positions | 1,048,576 | 1,048,576 |
| Next-token prediction auxiliary layers | 1 MTP layer | 1 MTP layer |
| Hash/index layers | 3 | 3 |
| Reference checkpoint quantization | FP8 E4M3, dynamic activation scaling, 128×128 weight blocks | Same published FP8 scheme; config also labels expert dtype `fp4` |
| License | MIT on the cited model repository | MIT on the cited model repository |

The parameter counts in the technical report and the structural fields in the
checkpoint configurations describe different aspects of the model. The total
parameter count includes the expert bank and other weights; active parameters
measure the approximate subset used per token. The six routed experts plus a
shared expert explain why active compute is far below stored parameter count.

#### Attention and long-context design

The V4 report describes token-wise compression plus DeepSeek Sparse Attention
(DSA). The checkpoint exposes one KV head, low-rank query/output projections,
index heads, top-k indexed retrieval, sliding-window parameters, and YaRN-style
RoPE extension from a shorter original context. The engineering objective is to
avoid full quadratic attention and a full-size KV cache over one million tokens.
DeepSeek reports that Pro at one million tokens uses 27% of the single-token
inference FLOPs and 10% of the KV cache of DeepSeek-V3.2. Those are vendor
measurements tied to the report's implementation and hardware assumptions.

The Flash configuration is especially explicit:

| Configuration item | Value | Operational meaning |
| --- | ---: | --- |
| `index_n_heads` | 64 | Learned index/scoring heads for sparse retrieval |
| `index_head_dim` | 128 | Per-index-head dimensionality |
| `index_topk` | 512 | Candidate positions retained by the sparse index path |
| `sliding_window` | 128 | Local attention span for the relevant local component |
| `q_lora_rank` | 1024 | Low-rank query projection rank |
| `o_lora_rank` | 1024 | Low-rank output projection rank |
| `qk_rope_head_dim` | 64 | Rotary-position sub-dimension |
| RoPE factor | 16 from 65,536 to 1,048,576 | Published extension configuration, not proof of perfect recall |

A one-million-token limit is a capacity claim. Evaluate retrieval accuracy,
conflict resolution, and latency at 32K, 128K, 512K, and 1M rather than assuming
quality is flat across the window.

#### Quantization and checkpoint size

The first-party files are FP8-oriented. Approximate raw weight storage can be
estimated from total parameters times bytes per stored parameter, but the
usable deployment footprint is larger because of metadata, scales, embeddings,
non-FP8 modules, runtime workspaces, expert parallelism, and KV cache. A 1.6T
checkpoint is a multi-node serving project even at one byte per parameter; it
is not a “run it on a gaming laptop” model because a quantized file exists.

Community GGUF, AWQ, GPTQ, FP4, or lower-bit conversions should be listed by
exact repository, revision, quantization recipe, and evaluation result. They
must not be described as first-party unless DeepSeek publishes them in its own
repository. Quantization can alter routing logits, expert selection, long-context
behavior, and reasoning stability even when short benchmarks appear unchanged.

#### Benchmark and mode discipline

DeepSeek publishes vendor benchmark charts for Pro and Flash. The guide keeps
those separate from independent results. Tests must hold thinking mode,
completion method, prompt, tool schema, output cap, and cache condition constant.
FIM is documented as a non-thinking path, so a Flash FIM score should not be
compared directly with a Pro thinking-agent score.

A useful local evaluation matrix includes:

- non-thinking JSON extraction with schema validation;
- thinking-mode repository diagnosis with a fixed tool budget;
- 128K and 1M retrieval tasks with planted evidence;
- throughput and first-token latency under the intended batch/concurrency;
- FP8 versus any selected quantization on the same prompt set;
- expert-parallel scaling and failure recovery across nodes.

### GLM-5.2: 744B-A40B MoE With IndexShare Sparse Attention

The [GLM-5 repository](https://github.com/zai-org/GLM-5),
[GLM-5.2 checkpoint](https://huggingface.co/zai-org/GLM-5.2), and
[configuration](https://huggingface.co/zai-org/GLM-5.2/blob/main/config.json)
provide Level A disclosure for the released model.

#### Architecture table

| Field | GLM-5.2 |
| --- | ---: |
| Total parameters | 744B |
| Active parameters | About 40B per token |
| Architecture | Decoder-only Mixture-of-Experts with DeepSeek Sparse Attention family mechanisms and IndexShare |
| Transformer layers | 78 |
| Hidden size | 6144 |
| Attention heads | 64 |
| KV heads | 64 |
| Head dimension | 192 in the main attention configuration |
| Routed experts | 256 |
| Shared experts | 1 |
| Active routed experts per token | 8 |
| MoE intermediate size | 2048 |
| Dense prefix | First 3 layers replace MoE with dense blocks |
| Context | 1M-token product/checkpoint target |
| MTP | 1 next-token prediction layer, improved for speculative decoding |
| Vocabulary | 154,880 |
| Reference precision | BF16 and first-party FP8 checkpoints |
| License | Repository/model-card license must be checked at the exact artifact; the cited release describes open weights and permissive use |

#### IndexShare and sparse-layer pattern

The configuration contains a 78-layer indexer pattern with early full attention,
shared indexers across groups of sparse-attention layers, and a final sparse
region. The repository describes IndexShare as reusing one indexer across every
four sparse layers, reducing per-token FLOPs by 2.9× at one million tokens. The
config exposes 32 index heads, 128-dimensional index heads, and top-k 2048.
Those values are checkpoint facts. The 2.9× figure is a vendor measurement.

The architecture also uses low-rank query projection (`q_lora_rank` 2048),
separate no-position and rotary query/key dimensions, a very high RoPE theta,
and an auxiliary MTP layer. The MTP improvement is reported to increase
speculative-decoding acceptance length by up to 20%. Serving software must
support the exact GLM MoE/DSA implementation; generic dense-transformer loaders
will not reproduce the model merely because they can read safetensors.

#### Benchmark claims and reproduction

Z.ai reports 81.0 on Terminal-Bench 2.1 and 62.1 on SWE-bench Pro, compared
with 62.0 and 58.4 for GLM-5.1 in its cited material. These are vendor results.
A reproduction record should include the agent harness, prompt scaffold,
container images, task exclusions, maximum turns, tool timeout, judge version,
and reasoning effort. GLM-5.2 supports High and Max thinking in the documented
coding surface; the repository states Max is the default unless High is
selected explicitly, and thinking can be disabled.

#### Deployment implications

At 744B total parameters, BF16 raw weight storage is roughly 1.5 TB before
runtime overhead. FP8 roughly halves the nominal weight bytes but still requires
substantial multi-accelerator memory plus expert-parallel communication. The
40B active figure reduces compute per token, not the need to store or stream the
expert bank. Practical deployment therefore depends on expert parallelism,
network bandwidth, routing balance, KV-cache policy, and framework maturity.

Pin the exact vLLM, SGLang, Transformers, KTransformers, or NPU backend version
listed by the model repository. Record BF16 versus FP8, tensor/expert parallel
layout, context cap, batch size, and whether speculative decoding is enabled.
A hosted API result and a self-hosted FP8 result are separate products.

### Mistral Medium 3.5: Dense 128B Multimodal Transformer

The [first-party model card](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)
and [configuration](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/config.json)
provide unusually detailed deployment information.

| Component | Published configuration |
| --- | --- |
| Text backbone | Dense 128B decoder-only transformer |
| Text layers | 88 |
| Hidden size | 12,288 |
| Attention heads | 96 |
| KV heads | 8, a grouped-query attention layout |
| Head dimension | 128 |
| Feed-forward intermediate size | 28,672 |
| Context | 262,144 positions |
| Vocabulary | 131,072 |
| Position scaling | YaRN-style extension from a 4,096-token original base with factor 64 |
| Vision tower | Pixtral-family encoder, 48 layers, hidden size 1,664, 16 heads, patch size 14 |
| Reference tensors | BF16 with an FP8 configuration for most text modules; vision tower/projector/output head excluded from conversion |
| License | Modified MIT with stated conditions in the model card |

The model is dense, so all 128B text parameters participate in each token's
forward pass rather than routing through a small expert subset. That makes its
compute and memory behavior very different from Mistral Small 4 despite the
“Medium” and “Small” labels. Grouped-query attention with 96 query heads and 8
KV heads reduces KV-cache growth relative to full multi-head attention.

Mistral warns that an earlier Transformers configuration caused long-context
performance degradation and that GGUF files generated from the incorrect
configuration can also be affected. This is a concrete example of why a local
model report must include the checkpoint revision and conversion date, not only
the marketing name.

The model card reports 91.4% on τ³-Telecom and 77.6% on SWE-bench Verified as
vendor results. Reproduction requires the exact agent framework and evaluator
versions. For local serving, Mistral documents vLLM/SGLang tensor parallelism,
reasoning parser/tool parser settings, and an EAGLE draft model for speculative
decoding. Evaluate EAGLE separately because speculative decoding should preserve
output distribution in principle but can expose implementation bugs or context
caps in practice.

The checked first-party Hugging Face tree reports **267 GB** because it contains
two equivalent three-shard naming layouts in the same repository. Each listed
weight layout is approximately 134 GB (about 50 + 50 + 34 GB). A downloader
should follow the model's index and runtime instructions rather than assuming
the repository total is the minimum unique weight payload.

### Mistral Small 4: 119B-A6.5B MoE With First-Party NVFP4

The [Mistral Small 4 model card](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603),
[configuration](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603/blob/main/config.json),
and [NVFP4 checkpoint](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-NVFP4)
provide Level A details.

| Field | Value |
| --- | ---: |
| Total parameters | 119B |
| Active parameters | 6.5B per token |
| Architecture | MoE multimodal decoder |
| Text layers | 36 |
| Hidden size | 4096 |
| Attention heads / KV heads | 32 / 32 |
| Routed experts | 128 |
| Active routed experts | 4 |
| Shared experts | 1 |
| Dense-prefix replacement | 0, so the published text stack is MoE throughout |
| MoE intermediate size | 2048 |
| Context advertised by model card | 256K |
| Configured maximum positions | 1,048,576 with YaRN scaling from 8,192; deployments should follow the supported product/runtime limit rather than assuming the full config value is validated |
| Vision tower | 24 layers, hidden size 1024, 16 heads, patch size 14 |
| Reference precision | BF16/FP8 checkpoint plus first-party post-training NVFP4 variant |
| License | Apache 2.0 |

The A6.5B label describes active compute, not storage. All 119B parameters still
need to be resident, sharded, or streamed. The four selected experts and one
shared expert reduce per-token arithmetic, while expert routing and
communication introduce their own latency and load-balancing costs.

The first-party NVFP4 checkpoint is valuable because its provenance and
conversion method are documented. It still needs matched quality evaluation
against the reference checkpoint. Measure routing stability, tool-call validity,
long-context retrieval, multilingual quality, vision grounding, and reasoning
at both `none` and `high`. Do not assume a four-bit file retains every behavior
because average benchmark loss is small.

Mistral reports a 40% reduction in end-to-end completion time and 3× throughput
against Mistral Small 3 in specified optimized setups. Those are vendor system
measurements, not portable constants. Hardware, batch size, speculative decoding,
attention backend, and quantization determine whether a local deployment sees
similar gains.

### Leanstral 1.5: Same MoE Family, Specialized Post-Training

Leanstral 1.5 uses the Mistral Small 4 architectural family: 119B total,
approximately 6.5B active, 128 experts with 4 routed experts active, 256K
context, and multimodal input. Its differentiator is specialized post-training
and agent tooling for Lean 4, not a wholly separate backbone.

The checked first-party repository is **121 GB**, split across seven consolidated
Safetensors shards, and is Apache 2.0 licensed. That owner-published footprint
is a download/storage fact, not a complete VRAM estimate; add cache, runtime,
tooling, and compiler-process memory.

The compiler is the authoritative evaluator. Report:

| Item | Required evidence |
| --- | --- |
| Formalization fidelity | Human review that the Lean theorem matches the intended natural-language statement |
| Proof validity | Exact Lean version, imports, project commit, and successful compilation command |
| Agent assistance | Tool/MCP version, number of attempts, diagnostics supplied to the model |
| Performance | First-pass compile rate, bounded-repair success, wall time, and human edits |
| Reproducibility | Final `.lean` file and dependency lock state |

A model can compile a proof of the wrong theorem. It can also explain a correct
mathematical idea while emitting invalid Lean. Those are separate failure modes
and should be scored separately.

### Mistral OCR 4: Service Architecture Is Undisclosed, Output Structure Is the Product

OCR 4 is a hosted Premier Document AI service, not an open checkpoint. Mistral
publishes the identifier, page pricing, paragraph bounding boxes, structural
labels, and product behavior, but not parameter count, layers, vision encoder,
OCR decoder, training corpus, or serving precision.

The correct technical dossier is therefore an extraction contract:

- accepted input formats and page limits;
- text, table, reading-order, block-label, and bounding-box outputs;
- language and handwriting behavior tested on the user's corpus;
- per-page and annotated-page cost;
- confidence/uncertainty handling where exposed;
- downstream validation for dates, totals, identifiers, and required fields;
- privacy, retention, and regional processing terms.

Measure character/word error only where it matters. For operational documents,
field accuracy, table-cell accuracy, reading order, bounding-box overlap, and
human correction minutes per page are often more useful.

### Voxtral TTS: Public 4B Speech Checkpoint, Deployment and Consent Matrix

The cited Mistral card identifies `voxtral-mini-tts-2603` as a 4B open-weight
speech model with nine languages, streaming, and approximately 90 ms
first-audio latency in the vendor setup. The architecture beyond the published
model size and interface is not fully detailed in the reviewed page, so layer
and head counts remain unreported here.

Deployment evaluation should separate:

| Layer | Measurements |
| --- | --- |
| Linguistic accuracy | Word and number errors, abbreviations, names, code-switching |
| Acoustic quality | Clipping, noise, timbre consistency, prosody, pacing |
| Streaming | Time to first audio, interruption behavior, tail latency, continuity |
| Voice adaptation | Consent, source-recording quality, identity similarity, misuse controls |
| Runtime | Precision/quantization, real-time factor, VRAM/RAM, batch throughput |

CC BY-NC 4.0, as listed in the source snapshot, is not a generic commercial-use
permission. Check the current license and hosted-service terms before shipping a
paid product. A technically possible voice clone is not automatically an
authorized or honest use.

### Gemma 4 Family: Variant-by-Variant Architecture

Google's [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
and first-party Hugging Face configurations expose dense and MoE variants with
hybrid local/global attention.

#### Text-backbone comparison

| Variant | Dense/MoE | Text layers | Hidden size | Query heads | KV heads | Global KV heads | Experts / active | Sliding window | Context |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| E2B | Dense, effective-parameter edge design | 35 | 1536 | 8 | 1 | Not separately set | None | 512 | 128K |
| E4B | Dense, effective-parameter edge design | 42 | 2560 | 8 | 2 | Not separately set | None | 512 | 128K |
| 12B | Dense | 48 | 3840 | 16 | 8 | 1 | None | 1024 | 256K |
| 26B A4B | MoE | 30 | 2816 | 16 | 8 | 2 | 128 experts / top 8 | 1024 | 256K |
| 31B | Dense | 60 | 5376 | 32 | 16 | 4 | None | 1024 | 256K |

The E2B/E4B names refer to effective operating footprints in Google's edge
model design rather than simply the total file parameter count. The 26B A4B is
the explicit MoE member: 128 experts with eight selected per token and a much
smaller expert intermediate width. The 12B and 31B are dense.

#### Hybrid attention pattern

Gemma 4 interleaves local sliding-window layers with full global-attention
layers, always ending on a global layer. The common large-model pattern is five
local layers followed by one global layer. Global layers use larger head
dimensions and proportional RoPE, while local layers use standard RoPE. This
reduces long-context cost while periodically allowing global information flow.

The design has runtime consequences. The published configs use 256-dimensional
local heads and 512-dimensional global heads for several variants. Some generic
FlashAttention paths historically assumed smaller uniform head dimensions, so
serving support must be verified in the exact runtime version. A model loading
successfully is not proof that the fastest or numerically correct attention
kernel was selected.

#### Effective parameters, official quantizations, and memory

Google explains that E2B and E4B use **Per-Layer Embeddings (PLE)**. Each decoder
layer receives its own small lookup embedding for every token. Those tables add
stored weights without adding the same matrix-multiplication cost as widening
every transformer block, which is why an "effective" parameter label is not the
same thing as checkpoint size. The 26B A4B has a different efficiency mechanism:
it is an MoE that loads the full 26B expert bank while selecting eight of 128
experts and activating about 4B parameters per token.

Google's checked memory table includes 20% loading overhead but excludes KV
cache and the rest of the application:

| Variant | BF16 | SFP8 | Q4_0 | Mobile | Mobile text-only |
| --- | ---: | ---: | ---: | ---: | ---: |
| E2B | 11.4 GB | 5.7 GB | 2.9 GB | 1.1 GB | 0.84 GB |
| E4B | 17.9 GB | 8.9 GB | 4.5 GB | 2.5 GB | 2.2 GB |
| 12B | 26.7 GB | 13.4 GB | 6.7 GB | Not listed | Not listed |
| 26B A4B | 57.7 GB | 28.8 GB | 14.4 GB | Not listed | Not listed |
| 31B | 69.9 GB | 34.9 GB | 17.5 GB | Not listed | Not listed |

The family has first-party quantization-aware-trained releases. Google documents
`-qat-q4_0-gguf` for llama.cpp and LM Studio, `-qat-w4a16-ct` Compressed Tensors
for vLLM/SGLang, `-qat-q4_0-unquantized` plus a matching `-assistant` drafter for
custom conversion and speculative decoding, and mobile builds for E2B/E4B.
Official Q4_0 GGUF and unquantized QAT artifacts cover all five sizes; the
checked W4A16 collection covers E2B, E4B, 12B, and 31B. Community AWQ, GPTQ,
MLX, EXL2, or alternative GGUF builds remain separate artifacts whose group
size, calibration set, excluded tensors, runtime, and benchmark retention must
be recorded.

#### Multimodal encoders

Gemma 4 variants include vision components and some variants include audio.
Examples from the first-party configs:

| Variant/component | Layers | Hidden size | Heads | Notes |
| --- | ---: | ---: | ---: | --- |
| E2B/E4B vision | 16 | 768 | 12 | Patch size 16; edge-oriented encoder |
| 26B/31B vision | 27 | 1152 | 16 | Patch size 16; 280 soft tokens per image |
| E2B/E4B audio | 12 | 1024 | 8 | Streaming/chunked audio encoder settings in config |
| 12B unified vision | Projector-style unified configuration | Output aligned to 3840 text width | Config-specific | The 12B release is described as encoder-free/unified; use its exact model class and processor |

Do not assume every Gemma 4 variant accepts identical modalities merely because
they share a family name. The model card and processor configuration for the
exact checkpoint decide whether audio, image, or video input is supported.

#### Memory, quantization, and deployment

Google publishes approximate four-bit memory planning figures. They are model
weight estimates, not full application footprints. Add KV cache, vision/audio
encoders, runtime workspace, tokenizer/processor state, batch buffers, and
framework overhead. Long context can dominate memory even when weights fit.

A deployment report should name the exact base or instruction-tuned checkpoint,
revision, BF16/FP16/FP8/int4 format, quantizer, group size, calibration set,
runtime, attention backend, hardware, context cap, batch size, and prompt
template. Compare quantized variants on both text and multimodal tasks because
keeping the language backbone stable does not guarantee that projector or
vision precision choices are harmless.

### DiffusionGemma 26B-A4B: Blockwise Discrete Diffusion

DiffusionGemma reuses the Gemma 4 26B-A4B MoE backbone but changes generation to
blockwise discrete diffusion. Its [model card](https://ai.google.dev/gemma/docs/diffusiongemma/model_card)
and [configuration](https://huggingface.co/google/diffusiongemma-26B-A4B-it/blob/main/config.json)
report:

| Field | Value |
| --- | ---: |
| Total / active parameters | 25.2B / 3.8B reported by Google |
| Text layers | 30 |
| Attention heads / KV heads | 16 / 8 |
| Experts / selected experts | 128 / 8 |
| Canvas length | 256 tokens |
| Context | Up to 256K |
| Generation | Iterative denoising over token blocks rather than only left-to-right next-token decoding |
| License | Apache 2.0 |
| Modal input | Text, image, and video input to text output |
| Checked instruction-checkpoint footprint | 51.7 GB across 11 Safetensors shards |

The canvas is the unit over which masked/noisy tokens can be refined in
parallel. Speed depends on number of denoising steps, canvas utilization,
hardware, batching, and kernel support. Google's “up to 4×” speed statement is a
vendor result, not a guarantee across every prompt or GPU.

Evaluation must add diffusion-specific metrics: block-boundary coherence,
revision stability across denoising steps, latency to first useful block,
end-to-end latency, layout/edit quality, and degradation on long sequential
reasoning. Compare against Gemma 4 26B-A4B under the same precision, hardware,
prompt set, and output length. The production-quality recommendation in Google's
material still favors standard Gemma 4 where output quality dominates latency.

### Grok 4.5: Closed Model, Openly Tool-Centric Product Evaluation

xAI publishes Grok 4.5's API price, reasoning levels, product position, and Grok
Build capabilities through its [launch](https://x.ai/news/grok-4-5),
[developer documentation](https://docs.x.ai/developers/grok-4-5), and
[CLI page](https://x.ai/cli). It does not publish weights, parameter counts,
layer counts, expert topology, or first-party quantizations.

The relevant technical object is model plus harness:

| Layer | Grok Build behavior to test |
| --- | --- |
| Repository discovery | File search accuracy, ignored paths, large-repo navigation |
| Editing | Patch locality, preservation of style, unrelated-change rate |
| Terminal | Command selection, timeout recovery, environment handling |
| Live web/X tools | Source quality, date filtering, quotation accuracy, prompt-injection resistance |
| Subagents | Task decomposition, duplicated work, merge conflicts, synthesis quality |
| Git | Status awareness, staging discipline, accidental destructive actions |

The cited independent results place Grok 4.5 High at 54 on Intelligence Index
and 76 in the Grok Build Coding Agent Index. Keep the “High” and “Grok Build”
labels attached. A bare API completion without search, terminal, or repository
access is not the tested configuration.

### Meta Muse Spark 1.1: Fast Hosted Reasoning With Undisclosed Checkpoint Topology

Meta's [announcement](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/)
establishes Thinking mode, multimodal reasoning, coding, computer-use
positioning, Meta AI availability, and Model API preview access. The reviewed
sources do not publish weights or a complete architecture table.

| Field | Status |
| --- | --- |
| Parameter count, layers, heads, experts | Undisclosed |
| Dense/MoE | Undisclosed |
| Context | 1M reported by Artificial Analysis for the tested API configuration |
| Price/throughput | $1.25/$4.25 and 116.3 output tokens/s in the dated independent listing |
| Reasoning mode | Thinking/xhigh label in the tested configuration; verify live API controls |
| Computer use | Requires a host environment and action policy; model access alone grants no device authority |

Muse's 51-point Intelligence result is close to Luna Max in the rounded
snapshot, but that does not imply equal coding-agent, GUI-control, visual, or
safety performance. Test computer use with an instrumented sandbox, explicit
action schema, forbidden-action list, screenshots/state logs, and deterministic
success conditions.

### Gemini 3.5 Flash: Hosted Multimodal Agent Model With Tool-Surface Separation

Google's [developer documentation](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5)
describes the model controls and supported tool paths. Architecture remains
closed: parameter count, dense/MoE topology, layers, attention heads, and
serving precision are undisclosed.

The model should be evaluated in at least three configurations:

1. text-only API with no tools;
2. function calling/code execution with a fixed host loop;
3. Google-supplied search, URL, file, maps, or computer-use integrations.

These configurations can produce substantially different outcomes. A model
that answers from memory is not the same system as one receiving search results
or executing code. Record `minimal`, `low`, `medium`, or `high`, and do not mix
those developer controls with consumer Standard/Extended thinking or Deep Think.

The dated independent score is 50.2 at High. Google's Terminal-Bench, GDPval-AA,
and MCP Atlas figures in the launch material are vendor claims. Compare them
only after matching benchmark version, harness, tools, token budget, and judge.

### GPT-Live-1 and GPT-Live-1 Mini: Full-Duplex System Architecture

OpenAI's [GPT-Live announcement](https://openai.com/index/introducing-gpt-live/)
and [system card](https://deploymentsafety.openai.com/gpt-live) describe a
continuous full-duplex architecture that listens while speaking and repeatedly
decides whether to pause, interrupt, respond, or call tools. They do not expose
parameter count, transformer depth, acoustic-token codec design, attention
heads, or checkpoint weights.

A live model is a control system, not merely text generation with speech added.
Evaluate:

| Category | Metrics |
| --- | --- |
| Turn management | Interruption latency, false interruptions, pause handling, overlap recovery |
| Speech quality | Intelligibility, pronunciation, prosody, clipping, language switching |
| Semantic quality | Factual correctness, instruction retention, uncertainty reporting |
| Tool delegation | Correct decision to call a tool or stronger text model, latency, result integration |
| Safety | Voice impersonation controls, refusal quality, prompt injection through audio |
| Network behavior | Jitter tolerance, packet loss, reconnect state, tail latency |

GPT-Live-1 Mini should be tested as its own latency/cost tier, not assumed to be
a linearly smaller Live-1. The public product positioning establishes a cheaper
or lighter role; internal topology remains unknown.

### Gemini 3.5 Flash Live Translate: Streaming Translation Pipeline

Live Translate is optimized for continuous language routing and translated
speech rather than open-ended conversation. Google documents supported use,
streaming behavior, and integration through the Live API, but not checkpoint
layers or parameter count.

A translation benchmark should use paired human transcripts and measure source
speech recognition errors, translation adequacy, named entities, numbers,
dates, code-switching, latency, speaker-turn preservation, and output-speech
intelligibility separately. End-to-end quality can fail at recognition,
translation, or synthesis; one aggregate preference score cannot locate the
cause.

### GPT Image 2: Product Capabilities Without a Public Architecture Claim

The [OpenAI model page](https://developers.openai.com/api/docs/models/gpt-image-2)
establishes the image-generation/editing interface and product limits. It does
not establish the frequently repeated claim that GPT Image 2 is fully
autoregressive over image patches, nor does it publish parameter count, layers,
attention topology, latent codec, diffusion stages, or checkpoint weights.

The architecture field therefore remains **undisclosed**. Visual artifacts or a
third-party description can motivate a hypothesis, but they cannot be promoted
to an OpenAI fact.

Evaluate the product on prompt adherence, typography, spatial relationships,
reference consistency, mask/edit precision, identity preservation where
permitted, resolution, latency, cost, refusal behavior, provenance metadata, and
commercial terms. Editing and first-pass generation should be scored separately.

### Nano Banana 2, Nano Banana Pro, and Nano Banana 2 Lite

Google's [image-generation guide](https://ai.google.dev/gemini-api/docs/image-generation)
and product announcements establish three product tiers. The reviewed sources
do not publish full denoiser/transformer architecture tables or weights.

| Variant | Product role to verify | Architecture status |
| --- | --- | --- |
| Nano Banana 2 | General image generation/editing tier | Closed/undisclosed topology |
| Nano Banana Pro | Higher-quality professional tier | Closed/undisclosed topology; associated product naming must not be confused with Lite |
| Nano Banana 2 Lite | Lower-cost/faster tier, also discussed with Gemini Omni Flash | Closed/undisclosed topology |

A matched image test should freeze prompt, aspect ratio, reference images,
seed where exposed, number of candidates, edit mask, and output resolution.
Score exact text rendering, object count, relative position, hands/faces only as
relevant to the task, style adherence, edit leakage, and consistency across
iterations. Do not use a preference Elo alone to claim factual diagram quality.

### Seedream 5.0 Pro: Limited First-Party English Technical Disclosure

The Dreamina product page establishes the model's consumer/product existence and
advertised capabilities. The checked English material does not provide a public
checkpoint, parameter count, architecture, training report, or a complete
benchmark methodology. This remains a Level D/C product dossier rather than an
open-model architecture entry.

For procurement, verify exact API availability, region, resolution, batch size,
price, editing/reference features, content policy, provenance, and commercial
rights on the day of use. Third-party image comparisons can reveal workflow
behavior but cannot establish internal architecture.

### Muse Image and Muse Video

Meta's [Muse announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
establishes the product family and stated multimodal generation goals. Muse
Image should be evaluated as an available image system only on the exact
surface documented; Muse Video remains “coming soon” in the checked snapshot
unless a later primary source provides a production identifier and access path.

Parameter count, layers, latent representation, diffusion/autoregressive method,
and training corpus are not established in the reviewed public material. The
responsible entry therefore focuses on availability, output limits, editing,
latency, safety, and provenance rather than pretending a marketing diagram is a
checkpoint configuration.

### Veo 3.1 Lite Preview: Hosted Video Generation With Explicit Product Limits

Google documents `veo-3.1-lite-generate-preview`, text/image input, video plus
audio output, one video per request, a 1,024-token prompt limit, and the absence
of 4K output or Extension in the cited preview page. Internal model architecture
is undisclosed.

Evaluate at the sequence level: motion continuity, object persistence, camera
obedience, scene transitions, audio synchronization, lip alignment when
relevant, temporal artifacts, edit continuity, and provenance. Save original
files because social-media compression can hide or create artifacts.

### Lyria 3: Music-Generation Product, Not a Text-Model Benchmark Entry

The cited guide documents `lyria-3-clip-preview` and `lyria-3-pro-preview`, text
and image prompting, MP3 stereo output, clip versus longer-song roles, and
structural/lyric capabilities. It does not publish network depth, parameter
count, codec, or generation topology.

Test musical form, rhythmic/harmonic consistency, vocal intelligibility,
pronunciation, instrumentation, transition quality, long-form repetition,
latency, editing continuity, and rights/provenance obligations. Keep the 44.1
kHz versus earlier 48 kHz documentation conflict visible until live output or
updated official documentation resolves it.

### Gemini Omni Flash: Unified Multimodal Service With Closed Architecture

Google presents Gemini Omni Flash as a unified multimodal model/service path.
The [model page](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
and [Omni guide](https://ai.google.dev/gemini-api/docs/omni) should be used for
current modalities, limits, tools, and identifiers. Parameter counts, layers,
expert topology, and codec design remain undisclosed.

An “omni” evaluation should not collapse all modalities into one score. Test
text reasoning, image understanding, audio understanding, speech generation,
image generation, and cross-modal continuity independently, then add integrated
workflows such as “inspect an image, discuss it by voice, and produce an edited
artifact.” Failures should be attributed to the specific stage.

### Gemini Robotics-ER 1.6: Reasoning Model Above a Safety Controller

Google documents `gemini-robotics-er-1.6-preview`, multimodal input, text
output, spatial reasoning, structured output, tool calls, and thinking budget.
It does not publish model weights or an architecture table.

The model belongs above, not inside, the lowest-level control loop. A safe stack
separates:

1. perception and semantic scene description;
2. high-level task decomposition;
3. validated function/action requests;
4. deterministic motion planning and collision avoidance;
5. hardware limits, emergency stop, and operator authority.

Benchmark perception, planning, tool schema validity, simulation success,
recovery, near misses, and human interventions separately. A correct route plan
is not evidence that direct motor commands are safe.

### Robostral Navigate: Research Watchlist Until an Interface Exists

Mistral's announcement establishes the name and embodied-navigation goal. The
reviewed public material does not establish a public model ID, API, weights,
license, sensor schema, action space, supported robot, simulation environment,
price, or safety procedure. No layer/parameter table can be responsibly filled.

Future evaluation should require a versioned simulator, sensor-noise model,
action frequency, collision definition, recovery policy, operator override, and
physical-transfer protocol before any deployment claim.

### Artificial Analysis and Benchmark Engineering: Expanded Reproducibility Rules

The independent scores in this guide are valuable because they compare live
systems under documented harnesses. They are still snapshots, not natural laws.

#### Minimum benchmark record

| Field | Example |
| --- | --- |
| Model | `gpt-5.6-terra` |
| Effort | Max |
| Harness | Codex |
| Benchmark/version | Terminal-Bench v2.1 |
| Tools | Shell, file editing, repository search |
| Context/output caps | Exact evaluator settings |
| Timeout/turn budget | Per task |
| Judge | Version and scoring procedure |
| Fallback | None or named routing behavior |
| Cost/time | Mean plus distribution where available |
| Date | Required because live models and services change |

#### Why one composite cannot select every model

- Coding agents need issue resolution, terminal reliability, repository
  understanding, and patch quality.
- Knowledge workers need source fidelity, calculation accuracy, artifact
  completeness, and presentation.
- Image models need prompt adherence, editing, text rendering, and visual
  consistency.
- Speech systems need intelligibility, latency, turn-taking, and acoustic
  quality.
- Robotics needs perception, planning, safety, intervention rate, and physical
  transfer.

The benchmark must resemble the intended work. Selecting a TTS system from a
coding score would be ridiculous, yet the same category error appears in less
obvious forms whenever a broad “intelligence” composite is treated as a universal
ranking.

### Open-Weight Quantization and Deployment Reference

#### Precision terminology

| Term | Typical meaning | Caveat |
| --- | --- | --- |
| BF16 | 16-bit floating weights/activations in many reference checkpoints | Runtime may keep selected accumulations or norms in FP32 |
| FP8 E4M3 | 8-bit floating format with 4 exponent and 3 mantissa bits | Scaling granularity and excluded modules matter |
| NVFP4 | NVIDIA-oriented 4-bit floating quantization | Requires compatible kernels/hardware and matched evaluation |
| INT8/INT4 | Integer quantization | Weight-only versus weight-and-activation methods behave differently |
| AWQ/GPTQ | Post-training weight quantization families | Calibration data and implementation affect quality |
| GGUF Q4/Q5/Q6 | llama.cpp ecosystem formats/quantizers | Naming does not guarantee identical quality across converters |
| FP4 expert dtype | Very low-precision expert storage/compute field in some MoE configs | Router, shared layers, attention, and activations may use other precisions |

#### Approximate raw-weight sizing

A rough lower bound is `parameter_count × bytes_per_parameter`. Thus 128B BF16
is about 256 GB of raw weights, 119B at one byte per parameter is about 119 GB,
744B FP8 is about 744 GB, and 1.6T FP8 is about 1.6 TB. These are not complete
VRAM requirements. Add scale metadata, non-quantized modules, runtime workspace,
KV cache, multimodal encoders, speculative-decoding models, and fragmentation.

For MoE systems, active parameters reduce arithmetic per token but do not remove
the storage requirement for the expert bank. Expert parallelism also adds
all-to-all communication. A model with 6.5B active parameters can still require
a server-class memory pool because 119B parameters must be available.

#### Required local-deployment record

Every local benchmark in this guide should be reproducible from:

- exact model repository and commit;
- base versus instruction/reasoning checkpoint;
- precision and quantization repository/recipe;
- tokenizer and chat template revision;
- inference runtime and commit/version;
- GPU/NPU/CPU model, count, memory, and interconnect;
- tensor, pipeline, and expert parallel settings;
- context limit, batch size, cache dtype, and attention backend;
- speculative-decoding model and settings;
- sampling/reasoning controls;
- prompt/tool harness and safety filters;
- task set, validator, and result files.

Without that record, “I ran model X locally” is an anecdote, not a benchmark.

### Model-Guide Completeness Matrix

| Model/system | Architecture depth in this guide | Benchmark depth | Deployment depth | Principal remaining unknown |
| --- | --- | --- | --- | --- |
| GPT-5.6 Sol/Terra/Luna | Product limits plus explicit undisclosed topology | Independent intelligence/coding interpretation | Hosted API/product controls | Parameters and network design |
| Fable 5 | Explicit closed-model boundary and fallback analysis | Independent intelligence/coding/briefcase | Hosted/API effort and price | Underlying checkpoint topology |
| Opus 4.8 | Closed boundary plus harness attribution | Intelligence and Claude Code | Hosted/API | Parameters/layers |
| Sonnet 5 | Closed boundary, price schedule, tools | Requires matched current eval | Hosted/API/Claude Code | Complete effort/context architecture |
| DeepSeek V4 Pro/Flash | Full MoE, layers, heads, experts, quantization | Vendor plus reproduction protocol | Multi-node FP8/open weights | Quantized variant quality |
| GLM-5.2 | Full MoE/DSA/IndexShare configuration | Vendor coding results plus protocol | BF16/FP8 multi-node | Independent matched evaluation |
| Mistral Medium 3.5 | Dense text and vision configs | Vendor agentic results plus protocol | BF16/FP8/EAGLE | Independent product comparison |
| Mistral Small 4 | MoE, vision, FP8/NVFP4 | Vendor speed/quality plus protocol | Open weights and quantized checkpoint | Long-context/runtime variance |
| Leanstral 1.5 | Shared Small 4 backbone plus specialization | Compiler-centered | Local/API tooling | Formalization fidelity at scale |
| Gemma 4 | Per-variant layers/heads/MoE/multimodal | Model-card results require matched tests | Open weights, local quantization | Runtime support across variants |
| DiffusionGemma | Full block-diffusion/MoE configuration | Speed claims plus diffusion-specific protocol | Open weights | Quality-speed frontier across hardware |
| Grok 4.5 | Closed boundary plus harness layers | Independent Grok Build score | Hosted API/CLI | Checkpoint topology |
| Muse Spark 1.1 | Closed boundary | Independent speed/cost/intelligence | Hosted preview | Computer-use reliability |
| Gemini 3.5 Flash | Closed boundary and tool separation | Independent plus vendor claims | Hosted Google tools | Checkpoint topology |
| GPT-Live | Full-duplex product architecture | Requires streaming benchmark | Hosted realtime | Codec/checkpoint topology |
| Image/video/music systems | Product limits and category-specific metrics | Preference/quality tests by modality | Hosted previews/APIs | Internal architecture and stable terms |
| Robotics systems | Safety-layer decomposition | Simulation/physical protocol | Preview/watchlist | Certified interfaces and operating limits |


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

<!-- frontier-migration-boundary -->
