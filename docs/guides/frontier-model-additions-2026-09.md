# Frontier Model Additions: September 2026

Checked: 2026-09-30

This supplement records model families that became current after the main
frontier guide's July 2026 research window, plus important open-model families
that the compact index did not previously cover. It is for developers and
reviewers choosing models for coding, agents, long-context work, or local
deployment. It is not a universal ranking.

Use this page with the [compact model list](frontier-model-list.md), the
[selection guide](frontier-overview-and-selection.md), and the
[evidence method](frontier-sources-and-method.md). Recheck every linked
first-party source before procurement or deployment: aliases, availability,
limits, licenses, and prices can change after the checked date.

## Scope and Evidence Rules

This update includes:

- current hosted frontier lines from OpenAI, Anthropic, and Google;
- current DeepSeek and Z.ai successors to families already in the guide; and
- major omitted open-weight families from OpenAI, Meta, Qwen, Mistral, and Ai2.

It does not attempt to catalog every checkpoint, fine-tune, media model, or
regional product surface. “Open-weight” means weights can be obtained under a
published license; it does not by itself mean that training data, training
code, or the complete development process is open. Vendor benchmark statements
below remain vendor claims unless explicitly described as independent.

## September Snapshot

| Provider | Current additions | Distribution at checked date | Primary decision |
| --- | --- | --- | --- |
| OpenAI | GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna | Hosted API | Capability, cost, and throughput tier |
| Anthropic | Claude Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 4.5 | Hosted API | Long-horizon depth versus latency and cost |
| Google | Gemini 3.8 Flash and Gemini 3.8 Live/TTS variants | Hosted API | Agentic text work versus real-time voice |
| DeepSeek | DeepSeek-V4.1-Flash | API plus published weights | Asymmetric MoE serving and native vision |
| Z.ai | GLM-5.3; GLM-5.3-Flash/FlashX service variants | Hosted/API; open-model lineage | Coding-agent migration and reasoning controls |
| OpenAI | gpt-oss-120b and gpt-oss-20b | Open weights, Apache 2.0 | Local reasoning under different hardware budgets |
| Meta | Llama 4 Scout and Maverick | Open weights under the Llama license | Long context and native multimodality |
| Qwen | Qwen3 and Qwen3-Coder | Open weights | General reasoning or agentic coding |
| Mistral | Mistral Large 3 and Ministral 3 | Open weights, Apache 2.0 | Large MoE or compact dense deployment |
| Ai2 | OLMo 3 and OLMo 3.1 | Fully open research artifacts | Auditability and reproducible model research |

## Hosted Frontier Additions

### OpenAI GPT-6 Family

OpenAI's current catalog routes demanding reasoning and coding to **GPT-6
Astra**, balanced complex work to **GPT-6.1 Sol**, and focused high-volume work
to **GPT-6 Luna**. The documented API identifiers are `gpt-6-astra`,
`gpt-6.1-sol`, and `gpt-6-luna`. All three accept text and image input and
produce text; the catalog reports a 1.05M-token context window and a 128K-token
maximum output for each.

| Model | First-party positioning | Reasoning settings listed | Practical starting point |
| --- | --- | --- | --- |
| GPT-6 Astra | Most capable model for demanding work | `low` through `max` | Hard coding, research synthesis, and evaluator-backed agents |
| GPT-6.1 Sol | Near-Astra performance at lower cost | `low` through `max` | Default candidate when quality and spend both matter |
| GPT-6 Luna | Efficient focused-work tier | `none` through `max` | High-volume extraction, classification, and bounded transformations |

The tier names are not evidence that one model dominates every workload.
Compare them using the same prompt, tools, effort, output cap, and retry policy.
For agent tests, separately record task success, tool-call validity, wall time,
and total tokens. Closed-model parameter counts and internal topology remain
undisclosed and must not be inferred from price or latency.

Source: [OpenAI model catalog](https://developers.openai.com/api/docs/models).

### Anthropic Claude 5.x Line

Anthropic's current comparison table lists **Claude Fable 5.1**, **Claude Opus
5.5**, **Claude Sonnet 5.5**, and **Claude Haiku 4.5**. Anthropic recommends
Opus 5.5 as the general starting point and positions Fable 5.1 for demanding
reasoning or long-horizon work that remains short of the target on Opus.

| Model | First-party role | Context listed | Evaluation emphasis |
| --- | --- | --- | --- |
| Claude Fable 5.1 | Demanding reasoning and long-horizon agents | 1M | Completion reliability across long tool trajectories |
| Claude Opus 5.5 | Long-running agentic coding and knowledge work | 1M | Repository-scale correctness and review burden |
| Claude Sonnet 5.5 | Speed/intelligence balance | 1M | Quality-adjusted latency and cost |
| Claude Haiku 4.5 | Fastest current Claude tier | 200K | Tail latency, throughput, and escalation accuracy |

Fable, Opus, and Sonnet expose adaptive thinking in the checked comparison;
Haiku exposes extended thinking but not the same effort control. Treat that as
an interface difference, not a reason to normalize results after the fact.
Record the exact API model ID and effort behavior with every evaluation because
aliases and defaults can move. Architecture details remain undisclosed.

Source: [Anthropic models overview](https://platform.claude.com/docs/en/models/overview).

### Google Gemini 3.8 Family

Google describes **Gemini 3.8 Flash** as its most intelligent Flash model for
long-horizon software engineering, autonomous agents, and complex enterprise
workflows. The same catalog lists four specialist siblings:

- **Gemini 3.8 Live**, the default low-latency voice-agent model;
- **Gemini 3.8 Live Extended Thinking**, a higher-reasoning live model;
- **Gemini 3.8 Flash TTS**, the flagship expressive text-to-speech model; and
- **Gemini 3.8 Flash-Lite TTS**, the lower-cost high-volume speech tier.

Do not collapse these into one benchmark row. Flash should be evaluated on
task completion and tool use; Live on turn latency, interruptions, and recovery;
and TTS on intelligibility, pronunciation, speaker consistency, and consent.
The catalog also retains Gemini 3.7, 3.6, and 3.5 Flash, but those are prior or
legacy generations rather than the primary additions in this update.

Source: [Gemini API model catalog](https://ai.google.dev/gemini-api/docs/models).

## Updated Open and Open-Weight Frontier

### DeepSeek-V4.1-Flash

DeepSeek released **DeepSeek-V4.1-Flash** on September 10, 2026. Its release
notes describe a 552B-parameter MoE with a causal encoder-decoder design: 8B
parameters active for input and 16B active for output. The model supports
native visual input and is served as `deepseek-flash`.

The release is operationally important because it supersedes three entries or
watchlist states from the July guide. DeepSeek says V4-Flash and
V4-Flash-Vision-Exp are retired, their old identifiers temporarily route to
V4.1-Flash, and V4-Pro is being phased out. Therefore:

1. do not treat an old alias as proof that the old checkpoint still served;
2. pin and log the returned model/version metadata where the API exposes it;
3. repeat text and vision evaluations after the routing change; and
4. verify weight license, files, precision, and runtime support directly from
   the published checkpoint before planning local deployment.

DeepSeek reports that the new KV cache requires one quarter of the HBM and one
eighth of the SSD storage of the preceding generation. These ratios are vendor
claims, not a substitute for a workload-specific cache and throughput test.

The August **DeepSeek-V4-Flash-Vision-Exp** release remains useful historical
context: it introduced mixed text/image requests, but it should now be labeled
retired rather than recommended as a current deployment target.

Sources: [DeepSeek-V4.1-Flash release](https://api-docs.deepseek.com/news/news260910/),
[V4-Flash-Vision-Exp release](https://api-docs.deepseek.com/news/news260821/).

### GLM-5.3 and Service Variants

Z.ai describes **GLM-5.3** as its current flagship for software engineering and
agent work. It uses the same base model as GLM-5.2; Z.ai attributes the changes
to post-training rather than a new base architecture. The documented service
accepts text only, provides a 1M-token context window and 128K maximum output,
and always enables reasoning with `low`, `high`, or `max` effort.

This is a migration boundary. A client that sends
`thinking.type: "disabled"` must change it to `enabled` before switching the
model ID to `glm-5.3`, or the request fails. Re-run structured-output and tool
tests because the model is exposed through OpenAI-compatible, Responses-style,
and Anthropic-compatible protocols, and protocol compatibility does not prove
behavioral identity.

The current Z.ai catalog also names **GLM-5.3-Flash** and
**GLM-5.3-FlashX** service variants. Treat their latency, quota, and availability
as service facts to verify at request time; do not transfer the flagship's
benchmark claims or assume a separately downloadable checkpoint without a
model card and license.

Source: [GLM-5.3 documentation](https://docs.z.ai/guides/llm/glm-5.3).

### OpenAI gpt-oss

OpenAI's **gpt-oss-120b** and **gpt-oss-20b** add a local/open-weight path that
is distinct from the hosted GPT-6 family. The checked model page describes the
120B variant as 117B total parameters with 5.1B active parameters, fitting on a
single H100 GPU. It lists a 131,072-token context window, text-only I/O,
configurable reasoning effort, tool-oriented capabilities, and the Apache 2.0
license. The 20B sibling targets smaller hardware budgets.

For deployment, “fits” is only a starting claim. Record precision, runtime,
weights plus KV-cache memory, concurrency, prompt length, and tool parser.
Evaluate the two sizes on the same tasks before assuming the larger checkpoint
has a better quality-per-dollar result under the actual serving stack.

Sources: [gpt-oss-120b model page](https://developers.openai.com/api/docs/models/gpt-oss-120b),
[gpt-oss-20b model page](https://developers.openai.com/api/docs/models/gpt-oss-20b).

### Meta Llama 4

Meta's **Llama 4 Scout** and **Llama 4 Maverick** are natively multimodal,
open-weight models under Meta's Llama license. Meta positions Scout for long
documents and reports a 10M-token context window; Maverick is the stronger
image-and-text understanding model in the pair.

The 10M figure is a supported-window claim, not evidence that arbitrary
10M-token retrieval is accurate. Test answer localization at multiple depths,
distractor resistance, vision grounding, time to first token, and KV-cache
growth. Review the Llama license rather than describing these checkpoints as
Apache-licensed or fully open source.

Source: [Meta Llama 4 model page](https://dev.meta.ai/llama/models/llama-4).

### Qwen3 General Models

The original **Qwen3** release open-weights two MoE flagships:
**Qwen3-235B-A22B** and **Qwen3-30B-A3B**. It also includes dense 32B, 14B, 8B,
4B, 1.7B, and 0.6B variants. Qwen3 supports thinking and non-thinking modes,
which should be treated as distinct evaluation configurations.

Use the 235B/22B model when maximum open-model capability justifies a large
serving footprint; use the smaller MoE or dense models when memory, batching,
or edge constraints dominate. Never compare a thinking run with a non-thinking
run without recording mode and token budget.

Source: [Qwen3 announcement](https://qwenlm.github.io/blog/qwen3/).

### Qwen3-Coder

**Qwen3-Coder-480B-A35B-Instruct** is a 480B-total, 35B-active MoE specialized
for agentic coding. Qwen reports a native 256K context window and extension to
1M with extrapolation. Its pretraining description reports 7.5T tokens with a
70% code ratio, followed by execution-driven code reinforcement learning and
long-horizon agent reinforcement learning.

The extrapolated window is not equivalent to the native window. Repository
tests should report which regime was used and should include patch application,
test execution, regression avoidance, tool-loop recovery, and human review
time. Qwen Code is a related CLI, not part of the checkpoint; harness gains must
not be attributed to model weights alone.

Source: [Qwen3-Coder announcement](https://qwenlm.github.io/blog/qwen3-coder/).

### Mistral 3

The **Mistral 3** family contains **Mistral Large 3**, a 675B-total/41B-active
sparse MoE, and dense **Ministral 3** models at 14B, 8B, and 3B. Mistral released
the family under Apache 2.0 and provides Large 3 checkpoints in BF16 and an
NVFP4 format.

Large 3 belongs in multi-GPU or hosted evaluations; Ministral variants belong
in memory-bounded, private, edge, or high-throughput comparisons. Quantized and
full-precision results should remain separate because kernel support and
quantization error can change both speed and quality.

Source: [Mistral 3 announcement](https://mistral.ai/news/mistral-3/).

### Ai2 OLMo 3 and 3.1

Ai2's **OLMo 3** line emphasizes inspectability across the model flow rather
than weights alone. The December update adds **OLMo 3.1 Think 32B** and
**OLMo 3.1 Instruct 32B**. Ai2 describes Think as an extended reinforcement-
learning run and Instruct as the larger application of the OLMo 3 Instruct
recipe.

OLMo is the strongest fit in this supplement when the requirement is research
auditability, training artifacts, or reproducible study rather than merely a
downloadable checkpoint. Still pin exact revisions of weights, code, data, and
evaluation assets; “fully open” does not make moving branches reproducible.

Source: [Ai2 OLMo 3 and 3.1 announcement](https://allenai.org/blog/olmo3).

## Selection by Workload

| Workload | First candidates | Required comparison |
| --- | --- | --- |
| Highest-difficulty hosted coding | GPT-6 Astra, Claude Fable 5.1, Claude Opus 5.5 | Same harness, effort, tools, timeout, and review rubric |
| Balanced hosted coding | GPT-6.1 Sol, Claude Sonnet 5.5, Gemini 3.8 Flash | Success per dollar and wall-clock time, not token price alone |
| High-volume bounded work | GPT-6 Luna, Claude Haiku 4.5 | Escalation rate and silent-error rate |
| Real-time voice | Gemini 3.8 Live variants | End-to-end latency, interruptions, and recovery |
| Open-weight agentic coding | DeepSeek-V4.1-Flash, GLM-5.3, Qwen3-Coder | Runtime support, tool validity, and repository-level success |
| Local general reasoning | gpt-oss, Qwen3, Ministral 3 | Precision, memory, throughput, and task quality |
| Open multimodal/long context | Llama 4, DeepSeek-V4.1-Flash | Grounding and retrieval accuracy across context depth |
| Reproducible model research | OLMo 3.1 | Artifact completeness and revision pinning |

## Evaluation and Deployment Checklist

Before adopting a model from this supplement:

1. Record the exact model ID, snapshot or weight revision, checked date, region,
   endpoint, runtime, precision, and license.
2. Pin system prompts, tools, reasoning effort, context, output cap, sampling,
   retries, and timeouts.
3. Separate model-only, model-plus-tools, and full-agent-harness results.
4. Test representative tasks, adversarial failures, long-context retrieval,
   structured output, tool recovery, and cost/latency tails.
5. For open weights, measure weights, KV cache, runtime overhead, batch size,
   and actual accelerator memory rather than relying on parameter count alone.
6. Recheck aliases before and after a provider migration; an unchanged request
   string can route to a different checkpoint.
7. Preserve prompts, outputs, tool traces, test revisions, and evaluator rules
   so another reviewer can reproduce the comparison.

## Known Limits and Refresh Triggers

- Provider pages are first-party sources and can contain marketing claims.
- The hosted models do not publish enough architecture detail for parameter or
  topology comparisons.
- Availability can vary by account, region, plan, and API surface.
- Benchmark scores were intentionally not normalized across vendors because
  harnesses, budgets, judges, and dates differ.
- Refresh this page when a listed alias changes routing, a model is retired, a
  weight license changes, or a newer family becomes the recommended default.

## First-Party Source Index

- [OpenAI model catalog](https://developers.openai.com/api/docs/models)
- [Anthropic models overview](https://platform.claude.com/docs/en/models/overview)
- [Google Gemini models](https://ai.google.dev/gemini-api/docs/models)
- [DeepSeek-V4.1-Flash](https://api-docs.deepseek.com/news/news260910/)
- [Z.ai GLM-5.3](https://docs.z.ai/guides/llm/glm-5.3)
- [OpenAI gpt-oss-120b](https://developers.openai.com/api/docs/models/gpt-oss-120b)
- [Meta Llama 4](https://dev.meta.ai/llama/models/llama-4)
- [Qwen3](https://qwenlm.github.io/blog/qwen3/)
- [Qwen3-Coder](https://qwenlm.github.io/blog/qwen3-coder/)
- [Mistral 3](https://mistral.ai/news/mistral-3/)
- [Ai2 OLMo 3](https://allenai.org/blog/olmo3)
