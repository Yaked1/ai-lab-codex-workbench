# Open and specialist frontier models

[← Frontier models index](frontier-models-and-multimodal-systems-2026.md)

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

DeepSeek publishes both base and instruction checkpoints through its official
Hugging Face organization. The [V4-Pro model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
and [V4-Pro base configuration](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-Base/blob/main/config.json)
provide enough implementation detail to distinguish a weight release from the
hosted service. The table below is **confirmed from those artifacts as checked
2026-07-12**. Flash values come from the same official V4 model card; fields not
published for Flash are left unknown rather than copied from Pro.

| Architecture field | V4-Pro | V4-Flash |
| --- | --- | --- |
| Model class | Sparse decoder-only MoE (`DeepseekV4ForCausalLM`) | Sparse decoder-only MoE |
| Total / activated parameters | 1.6T / 49B per token | 284B / 13B per token |
| Context | 1,048,576 tokens | 1,048,576 tokens |
| Transformer layers | 61 | Not stated in the checked model card |
| Hidden width | 7,168 | Not stated in the checked model card |
| Attention | Hybrid Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) | Same V4 family design; exact Flash config should be checked separately |
| Attention configuration | 128 query heads, one KV head, 512 head dimension; 64 index heads of dimension 128 selecting top 1,024 positions | Not stated in the checked model card |
| MoE routing | 384 routed experts plus one shared expert; six routed experts active per token | Active-parameter count published; expert topology not copied from Pro |
| MoE feed-forward width | 3,072 | Not stated in the checked model card |
| Positional/context scaling | 65,536 original sequence length, factor-16 extension to 1M, RoPE theta 10,000 | 1M supported; exact scaling config not stated here |
| Vocabulary | 129,280 | Not stated in the checked model card |
| Released precision | Base: FP8 mixed; instruction: expert weights FP4 and most other weights FP8 | Same published base/instruction precision policy |
| Checked Hugging Face repository footprint | 865 GB across 64 Safetensors shards | 160 GB across 46 Safetensors shards |

The hybrid attention is not a marketing synonym for ordinary grouped-query
attention. DeepSeek says CSA and HCA reduce the V4-Pro single-token inference
FLOPs at 1M context to 27% of V3.2 and reduce KV-cache use to 10%. These are
**vendor measurements**, not independently reproduced numbers. The configuration
also exposes Manifold-Constrained Hyper-Connections (`hc_mult=4`, 20 Sinkhorn
iterations), three hash layers, query and output LoRA ranks, and a 128-token
window. Those details matter to runtime authors but do not imply that generic
Transformers or a legacy DeepSeek-V3 server can load the model correctly.

#### Released precision, checkpoint scale, and community quantizations

The official instruction checkpoint is already mixed low precision: expert
parameters are FP4 while most remaining tensors are FP8. Calling every smaller
conversion simply "4-bit" hides which tensors were requantized, which stayed at
higher precision, and what calibration method was used. Record the exact repo,
revision, tensor formats, runtime, kernel support, and context used. The official
model page links a Hugging Face quantization tree, but those downstream GGUF,
AWQ, or other conversions are community artifacts unless DeepSeek publishes
them in its own organization. Treat their size and quality claims separately.

A 1.6T-total-parameter sparse model does not fit on hardware as if it were a
49B dense model. The active count approximates per-token compute, while all
experts still require storage and an expert-parallel loading strategy. Likewise,
the 284B Flash checkpoint is not a typical single-GPU 13B model. Capacity plans
must include stored weights, non-expert tensors, KV cache, router/expert-parallel
communication, batch size, output length, runtime workspace, and safety/service
overhead. DeepSeek's release does not provide one universal minimum GPU count,
so this guide does not invent one.

#### Vendor benchmark snapshot and interpretation

DeepSeek's official card reports base-model results with the shot count and
metric. V4-Pro-Base reports 90.1 on five-shot MMLU, 73.5 on five-shot MMLU-Pro,
76.8 pass@1 on zero-shot HumanEval, 64.5 on four-shot MATH, and 51.5 on one-shot
LongBench-V2. Flash-Base reports 88.7, 68.3, 69.5, 57.4, and 44.7 respectively.
These are useful **vendor-reported results**, but they are not a single rank:
Pro does not lead Flash on every listed task, and none of these base-model rows
measure the hosted agent loop, tool schema, or Max reasoning mode.

Before local deployment, confirm the exact license file for the selected
checkpoint, pin the repository revision, validate the serving implementation
against the reference output, and rerun task-specific evaluations at the chosen
precision. Hosted API and local-weight results should remain separate because
system prompts, post-training, sampler settings, kernels, safety layers, and
model revisions can differ.

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

#### Weight architecture and checkpoint footprint

The official [GLM-5.2 model repository](https://huggingface.co/zai-org/GLM-5.2)
is MIT-licensed and identifies the model as `GlmMoeDsaForCausalLM`. Its
[configuration](https://huggingface.co/zai-org/GLM-5.2/blob/main/config.json)
turns the release's high-level sparse-attention claims into concrete deployment
facts. These values are from the repository revision checked 2026-07-12:

| Field | Published value |
| --- | --- |
| Architecture | Decoder-only sparse MoE with DeepSeek-style sparse attention (`glm_moe_dsa`) |
| Stored checkpoint | Approximately 1.51 TB across 282 Safetensors shards in the checked repository |
| Layers | 78 transformer layers; first three use dense MLPs, remaining layers use sparse MoE MLPs |
| Hidden / dense FFN width | 6,144 / 12,288 |
| MoE topology | 256 routed experts plus one shared expert; eight routed experts selected per token |
| Expert FFN width | 2,048 |
| Attention heads | 64 query and 64 KV heads; 192 base head dimension, 256 QK/value dimensions after split components |
| Sparse indexer | 32 index heads, 128-dimensional index heads, top-2,048 selection, index refreshed every four layers |
| Context | 1,048,576 positions |
| Position encoding | Interleaved RoPE, theta 8,000,000 |
| Vocabulary | 154,880 tokens; embeddings are not tied |
| Released dtype | BF16 tensors; router computation declared FP32 |
| Runtime paths documented by model owner | Transformers, vLLM, SGLang, and Docker Model Runner |

The config's layer lists show the architectural rhythm more precisely than the
phrase "sparse attention." The first three indexers are full. Later sparse
layers share one indexer for groups of four, with periodic full indexers. Z.ai
calls this IndexShare and reports a 2.9x reduction in per-token FLOPs at 1M
context. The configuration also contains one next-token-prediction draft layer;
the model card says the revised speculative-decoding layer improves accepted
draft length by up to 20%. Both efficiency figures are **vendor claims** and
depend on its implementation and workload.

The published 1.51 TB repository size is storage evidence, not an accelerator
memory recommendation. Self-hosting requires tensor and expert parallelism,
high-throughput interconnects, runtime workspace, and additional KV-cache memory.
Eight active routed experts reduce compute relative to evaluating all 256, but
all expert weights still need storage and an availability strategy. Community
quantizations linked by Hugging Face may reduce storage, but their calibration,
kernel compatibility, long-context quality, and benchmark retention must be
evaluated per artifact. Z.ai's official repository does not make every community
conversion an official GLM-5.2 release.

#### Vendor benchmark snapshot

The official model card reports GLM-5.2 at 40.5 on Humanity's Last Exam without
tools, 54.7 with tools, 20.9 on CritPt, and 99.2 on AIME 2026. These rows mix
different task types and sometimes tools; they are not interchangeable quality
percentages. The comparison table marks some competitor values with asterisks,
so a downstream summary must retain the card's footnotes, evaluator, prompting,
tool access, and token budget. Until a benchmark maintainer or independent lab
reproduces the exact GLM setup, these remain **vendor-reported results**.

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

#### Mistral Small 4 weight architecture

The official [Mistral Small 4 weight card](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)
and [configuration](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603/blob/main/config.json)
disclose substantially more than the API card. Small 4 is a multimodal sparse
MoE, not a dense 119B transformer. Its 119B stored parameters and 6.5B active
parameters describe different resource questions: the first drives checkpoint
storage and weight memory, while the second better approximates compute per
token.

| Field | Mistral Small 4 119B A6B |
| --- | --- |
| Text backbone | `mistral4`, 36 layers, hidden size 4,096 |
| MoE topology | 128 routed experts plus one shared expert; top four routed experts per token |
| Dense / expert FFN width | 12,288 / 2,048 |
| Attention | 32 query heads and 32 KV heads, 128-dimensional heads; Q-LoRA rank 1,024 and KV-LoRA rank 256 |
| Position encoding | YaRN factor 128 from an 8,192-token original window; RoPE theta 10,000 |
| Configured maximum | 1,048,576 positions in the weight config; product/model card advertises 256K supported context |
| Vocabulary | 131,072, untied embeddings |
| Vision tower | 24 layers, width 1,024, 16 heads, 14-pixel patches, image size up to 1,540 |
| Distributed checkpoint | Seven approximately 20 GB consolidated shards; Hugging Face tree reports roughly 242 GB total |
| Official precision paths | FP8 checkpoint and a separate NVFP4 checkpoint |
| License | Apache 2.0 for the checked weight repository |

The 1M `max_position_embeddings` value is a configuration ceiling, not evidence
that Mistral supports or evaluates every task at 1M. The owner-facing model card
states 256K, and the reference vLLM command uses `--max-model-len 262144`.
Deployment guidance should therefore use 256K unless a newer Mistral source
documents a validated higher limit. This is an example of why reading only
`config.json` can overstate a product contract.

Small 4 combines Instruct, reasoning, and Devstral-style agent behavior in one
checkpoint. The card exposes `reasoning_effort="none"` and `"high"`, a Mistral
reasoning parser, automatic tool choice, and function calls. It also publishes
an Eagle speculative-decoding head. Mistral reports 40% lower end-to-end time in
a latency-optimized setup and three times the requests per second in a
throughput-optimized setup versus Small 3; these are **vendor measurements**
whose hardware, batching, prompt lengths, and acceptance rate must accompany any
reuse.

#### Quantization and serving choices

The official FP8 repository is roughly 242 GB. Mistral's separate NVFP4 release
is the owner-published four-bit path and is intended to reduce memory use and
increase throughput, but the collection warns to expect lower long-context
performance. That warning should be part of an evaluation, not a footnote.
Hugging Face also lists community GGUF conversions for llama.cpp and LM Studio;
their quantization recipes and accuracy are not automatically endorsed by
Mistral. Record the converter, quantization type, tensor exceptions, file size,
runtime commit, and representative benchmark delta.

Mistral recommends vLLM for production serving and documents tensor parallelism,
Flash Attention with MLA, tool-call and reasoning parsers, batch-token limits,
and GPU-memory utilization. SGLang, Transformers, llama.cpp, and LM Studio are
also listed. Runtime support is version-sensitive: the card required a current
vLLM plus `mistral_common` 1.11.0 or later and, for Transformers at publication,
the development branch. A successful load is not enough; verify image input,
reasoning mode, tool-call JSON, 256K retrieval, throughput, and output quality.

#### What remains undisclosed for Medium 3.5

The checked Medium 3.5 API card establishes an open-weight label, context,
license class, modalities, and price, but it does not expose an official weight
configuration with total parameters, active parameters, layer count, expert
count, attention topology, tokenizer size, or owner-published quantization in
the sources reviewed here. Those fields remain **unknown**. Do not transfer
Small 4's 119B A6B architecture to Medium 3.5 merely because both are current
Mistral releases.

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

<!-- frontier-migration-boundary -->
