# Frontier sources and method

[← Frontier models index](frontier-models-and-multimodal-systems-2026.md)

## How the Expanded Technical Dossiers Are Structured

The short family summaries above are useful for orientation, but they are not
sufficient for architecture review, deployment planning, benchmark comparison,
or procurement. The expanded dossiers later in this guide use one common
schema so that a closed API model, an open-weight checkpoint, a speech system,
and a video generator are not compared as though they disclosed the same kind
of evidence.

Every expanded dossier tries to answer the following questions:

1. **Identity and status.** What is the exact model or product name, release
   state, model identifier, access surface, and checked date?
2. **Architecture.** Is the checkpoint dense or Mixture-of-Experts? How many
   total and active parameters, transformer layers, attention heads, key/value
   heads, experts, active experts, vision/audio layers, and context positions
   are publicly documented?
3. **Generation method.** Is output autoregressive, diffusion-based,
   full-duplex streaming, retrieval-augmented, tool-mediated, or undisclosed?
4. **Training and post-training.** What does the vendor disclose about
   pretraining scale, reinforcement learning, distillation, safety tuning,
   multimodal alignment, speculative decoding, or reasoning controls?
5. **Performance.** Which results are vendor claims, which are independent,
   which include an agent harness or fallback, and which cannot be compared
   because the evaluator, tools, token budget, or judge differs?
6. **Deployment.** Are weights available? Under what license? Which reference
   precisions, first-party quantizations, runtimes, context limits, and hardware
   assumptions are documented?
7. **Failure modes.** What is likely to break in long context, tool loops,
   structured output, multimodal grounding, streaming, editing, or physical
   control?
8. **Unknowns.** Which requested facts remain undisclosed rather than being
   reverse-engineered from branding, UI behavior, or third-party speculation?

### Architecture disclosure scale

| Level | Meaning | What this guide is allowed to report |
| --- | --- | --- |
| A | Public weights plus a first-party configuration and model card | Exact layer, head, expert, context, tensor type, and checkpoint facts from the named revision |
| B | Public technical report or detailed system card without weights | Vendor-described architecture and training methods, but not unreported checkpoint dimensions |
| C | Product/API documentation only | Modalities, limits, tools, price, and product controls; parameter count and internal topology remain unknown |
| D | Announcement or preview with limited technical material | Only explicitly announced capabilities and restrictions; no deployment recipe is inferred |
| U | Unconfirmed | No stable factual model entry is created until a primary source appears |

A closed model can still be excellent while receiving a Level C architecture
rating. The rating measures disclosure, not intelligence. Likewise, an open
checkpoint can disclose every tensor dimension and still perform poorly on a
particular task. Humanity has somehow managed to confuse transparency,
capability, popularity, and marketing volume into one number often enough that
this guide keeps them deliberately separate.

### Rules for architecture tables

For open-weight systems, the tables use the vendor's model card and the exact
configuration files linked in the Sources section. A configuration describes a
checkpoint artifact, not necessarily every detail of the training run or hosted
service. Parameter totals can also include embeddings, routers, vision towers,
audio encoders, projectors, and output heads that are not obvious from a single
`hidden_size × layer_count` calculation.

For closed systems, an entry of **Undisclosed** is a result, not a missing
paragraph. The guide does not infer MoE routing from pricing, parameter count
from latency, attention type from context length, or diffusion versus
autoregression from visual artifacts. Those guesses can be interesting research
hypotheses, but they are not product facts.

### Rules for benchmark tables

Benchmark rows retain five pieces of context whenever the source provides them:
model identifier, effort or reasoning mode, harness, evaluator/version, and
fallback behavior. A score without those fields should be treated as a lead for
further testing, not a procurement verdict. Vendor numbers remain vendor claims
even when the chart is beautifully typeset. Independent numbers remain specific
to the independent evaluator's harness rather than becoming universal properties
of the bare checkpoint.


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



Additional primary architecture/configuration sources used by the expanded dossiers:

- [DeepSeek-V4 technical report](https://arxiv.org/abs/2606.19348), including total/active parameter counts and million-token efficiency claims.
- [DeepSeek-V4-Pro first-party configuration](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/config.json).
- [DeepSeek-V4-Flash first-party configuration](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash/blob/main/config.json).
- [Z.ai GLM-5 series repository](https://github.com/zai-org/GLM-5), including GLM-5.2 architecture, checkpoints, effort controls, and vendor benchmark setup.
- [GLM-5.2 first-party configuration](https://huggingface.co/zai-org/GLM-5.2/blob/main/config.json).
- [GLM-5.2 FP8 checkpoint configuration](https://huggingface.co/zai-org/GLM-5.2-FP8/blob/main/config.json).
- [Mistral Medium 3.5 first-party model card](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B).
- [Mistral Medium 3.5 first-party configuration](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/config.json).
- [Mistral Small 4 first-party model card](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603).
- [Mistral Small 4 first-party configuration](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603/blob/main/config.json).
- [Mistral Small 4 first-party NVFP4 checkpoint](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-NVFP4).
- [Leanstral 1.5 first-party checkpoint](https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B).
- [Gemma 4 E2B configuration](https://huggingface.co/google/gemma-4-E2B/blob/main/config.json).
- [Gemma 4 E4B configuration](https://huggingface.co/google/gemma-4-E4B/blob/main/config.json).
- [Gemma 4 12B configuration](https://huggingface.co/google/gemma-4-12B/blob/main/config.json).
- [Gemma 4 26B-A4B configuration](https://huggingface.co/google/gemma-4-26B-A4B/blob/main/config.json).
- [Gemma 4 31B configuration](https://huggingface.co/google/gemma-4-31B/blob/main/config.json).
- [DiffusionGemma 26B-A4B instruction checkpoint configuration](https://huggingface.co/google/diffusiongemma-26B-A4B-it/blob/main/config.json).


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
<!-- frontier-migration-boundary -->
