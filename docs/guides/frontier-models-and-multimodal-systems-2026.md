# Frontier Models and Multimodal Systems in 2026

Checked: 2026-07-12

This guide explains the GPT-5.6 family, current Claude, DeepSeek, GLM, Mistral,
Google open-model, media, robotics, live-audio, image, and video systems. It now
contains announcement-style release dossiers for every named model and major
variant, alongside the architecture, benchmark, quantization, and deployment
reference sections. It is
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



## Subject pages

This landing page keeps stable anchors for the pre-split guide. Full
subject content lives in the bounded pages below.

- [Frontier sources and method](frontier-sources-and-method.md)
- [Frontier overview and selection](frontier-overview-and-selection.md)
- [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md)
- [Open and specialist frontier models](frontier-open-and-specialist-models.md)
- [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md)
- [Google, live, image, and media systems](frontier-google-and-media.md)

## Compatibility anchors

Each anchor below preserves a pre-split heading target. Follow the
linked subject page for the full section body.

<a id="frontier-models-and-multimodal-systems-in-2026"></a>

**Frontier Models and Multimodal Systems in 2026** → [Frontier models landing](frontier-models-and-multimodal-systems-2026.md#frontier-models-and-multimodal-systems-in-2026)

<a id="how-the-expanded-technical-dossiers-are-structured"></a>

**How the Expanded Technical Dossiers Are Structured** → [Frontier sources and method](frontier-sources-and-method.md#how-the-expanded-technical-dossiers-are-structured)

<a id="architecture-disclosure-scale"></a>

**Architecture disclosure scale** → [Frontier sources and method](frontier-sources-and-method.md#architecture-disclosure-scale)

<a id="rules-for-architecture-tables"></a>

**Rules for architecture tables** → [Frontier sources and method](frontier-sources-and-method.md#rules-for-architecture-tables)

<a id="rules-for-benchmark-tables"></a>

**Rules for benchmark tables** → [Frontier sources and method](frontier-sources-and-method.md#rules-for-benchmark-tables)

<a id="prompting-guides-for-these-models"></a>

**Prompting Guides for These Models** → [Frontier overview and selection](frontier-overview-and-selection.md#prompting-guides-for-these-models)

<a id="the-short-answer"></a>

**The Short Answer** → [Frontier overview and selection](frontier-overview-and-selection.md#the-short-answer)

<a id="announcement-style-release-dossiers"></a>

**Announcement-Style Release Dossiers** → [Frontier overview and selection](frontier-overview-and-selection.md#announcement-style-release-dossiers)

<a id="how-to-read-each-release-dossier"></a>

**How to read each release dossier** → [Frontier overview and selection](frontier-overview-and-selection.md#how-to-read-each-release-dossier)

<a id="gpt-56-sol-openais-flagship-tier-for-frontier-professional-work"></a>

**GPT-5.6 Sol: OpenAI’s flagship tier for frontier professional work** → [Frontier overview and selection](frontier-overview-and-selection.md#gpt-56-sol-openais-flagship-tier-for-frontier-professional-work)

<a id="gpt-56-terra-the-balanced-gpt-56-tier-for-daily-engineering-and-professional-workflows"></a>

**GPT-5.6 Terra: The balanced GPT-5.6 tier for daily engineering and professional workflows** → [Frontier overview and selection](frontier-overview-and-selection.md#gpt-56-terra-the-balanced-gpt-56-tier-for-daily-engineering-and-professional-workflows)

<a id="gpt-56-luna-openais-fastest-and-least-expensive-gpt-56-tier"></a>

**GPT-5.6 Luna: OpenAI’s fastest and least expensive GPT-5.6 tier** → [Frontier overview and selection](frontier-overview-and-selection.md#gpt-56-luna-openais-fastest-and-least-expensive-gpt-56-tier)

<a id="claude-fable-5-anthropics-generally-available-mythos-class-frontier-model-with-conservative-safeguards"></a>

**Claude Fable 5: Anthropic’s generally available Mythos-class frontier model with conservative safeguards** → [Frontier overview and selection](frontier-overview-and-selection.md#claude-fable-5-anthropics-generally-available-mythos-class-frontier-model-with-conservative-safeguards)

<a id="claude-opus-48-anthropics-premium-closed-model-for-demanding-coding-analysis-and-agent-work"></a>

**Claude Opus 4.8: Anthropic’s premium closed model for demanding coding, analysis, and agent work** → [Frontier overview and selection](frontier-overview-and-selection.md#claude-opus-48-anthropics-premium-closed-model-for-demanding-coding-analysis-and-agent-work)

<a id="claude-sonnet-5-anthropics-agentic-sonnet-release-aimed-at-frontier-performance-per-dollar"></a>

**Claude Sonnet 5: Anthropic’s agentic Sonnet release aimed at frontier performance per dollar** → [Frontier overview and selection](frontier-overview-and-selection.md#claude-sonnet-5-anthropics-agentic-sonnet-release-aimed-at-frontier-performance-per-dollar)

<a id="deepseek-v4-pro-deepseeks-16t-total-49b-active-open-moe-flagship"></a>

**DeepSeek-V4-Pro: DeepSeek’s 1.6T-total, 49B-active open MoE flagship** → [Frontier overview and selection](frontier-overview-and-selection.md#deepseek-v4-pro-deepseeks-16t-total-49b-active-open-moe-flagship)

<a id="deepseek-v4-flash-a-284b-total-13b-active-v4-checkpoint-optimized-for-speed-and-cost"></a>

**DeepSeek-V4-Flash: A 284B-total, 13B-active V4 checkpoint optimized for speed and cost** → [Frontier overview and selection](frontier-overview-and-selection.md#deepseek-v4-flash-a-284b-total-13b-active-v4-checkpoint-optimized-for-speed-and-cost)

<a id="glm-52-zais-744b-total-40b-active-long-horizon-moe-flagship"></a>

**GLM-5.2: Z.ai’s 744B-total, 40B-active long-horizon MoE flagship** → [Frontier overview and selection](frontier-overview-and-selection.md#glm-52-zais-744b-total-40b-active-long-horizon-moe-flagship)

<a id="mistral-medium-35-a-dense-128b-open-weight-multimodal-model-for-coding-and-agents"></a>

**Mistral Medium 3.5: A dense 128B open-weight multimodal model for coding and agents** → [Frontier overview and selection](frontier-overview-and-selection.md#mistral-medium-35-a-dense-128b-open-weight-multimodal-model-for-coding-and-agents)

<a id="mistral-small-4-a-119b-total-65b-active-multimodal-moe-with-first-party-nvfp4"></a>

**Mistral Small 4: A 119B-total, 6.5B-active multimodal MoE with first-party NVFP4** → [Frontier overview and selection](frontier-overview-and-selection.md#mistral-small-4-a-119b-total-65b-active-multimodal-moe-with-first-party-nvfp4)

<a id="mistral-ocr-4-a-document-intelligence-service-built-around-structured-extraction-rather-than-chat-scores"></a>

**Mistral OCR 4: A document-intelligence service built around structured extraction rather than chat scores** → [Frontier overview and selection](frontier-overview-and-selection.md#mistral-ocr-4-a-document-intelligence-service-built-around-structured-extraction-rather-than-chat-scores)

<a id="voxtral-tts-mistrals-open-4b-streaming-speech-model-with-voice-adaptation"></a>

**Voxtral TTS: Mistral’s open 4B streaming speech model with voice adaptation** → [Frontier overview and selection](frontier-overview-and-selection.md#voxtral-tts-mistrals-open-4b-streaming-speech-model-with-voice-adaptation)

<a id="leanstral-15-a-119b-total-65b-active-model-specialized-for-lean-4-proof-engineering"></a>

**Leanstral 1.5: A 119B-total, 6.5B-active model specialized for Lean 4 proof engineering** → [Frontier overview and selection](frontier-overview-and-selection.md#leanstral-15-a-119b-total-65b-active-model-specialized-for-lean-4-proof-engineering)

<a id="robostral-navigate-mistrals-announced-embodied-navigation-system"></a>

**Robostral Navigate: Mistral’s announced embodied-navigation system** → [Frontier overview and selection](frontier-overview-and-selection.md#robostral-navigate-mistrals-announced-embodied-navigation-system)

<a id="gemma-4-e2b-ultra-mobile-effective-parameter-model"></a>

**Gemma 4 E2B: Ultra-mobile effective-parameter model** → [Frontier overview and selection](frontier-overview-and-selection.md#gemma-4-e2b-ultra-mobile-effective-parameter-model)

<a id="gemma-4-e4b-higher-capability-mobile-and-edge-model"></a>

**Gemma 4 E4B: Higher-capability mobile and edge model** → [Frontier overview and selection](frontier-overview-and-selection.md#gemma-4-e4b-higher-capability-mobile-and-edge-model)

<a id="gemma-4-12b-unified-multimodal-workstation-model"></a>

**Gemma 4 12B: Unified multimodal workstation model** → [Frontier overview and selection](frontier-overview-and-selection.md#gemma-4-12b-unified-multimodal-workstation-model)

<a id="gemma-4-26b-a4b-sparse-high-throughput-reasoning-model"></a>

**Gemma 4 26B-A4B: Sparse high-throughput reasoning model** → [Frontier overview and selection](frontier-overview-and-selection.md#gemma-4-26b-a4b-sparse-high-throughput-reasoning-model)

<a id="gemma-4-31b-largest-dense-gemma-4-model"></a>

**Gemma 4 31B: Largest dense Gemma 4 model** → [Frontier overview and selection](frontier-overview-and-selection.md#gemma-4-31b-largest-dense-gemma-4-model)

<a id="diffusiongemma-26b-a4b-googles-experimental-blockwise-discrete-diffusion-text-generator"></a>

**DiffusionGemma 26B-A4B: Google’s experimental blockwise discrete-diffusion text generator** → [Frontier overview and selection](frontier-overview-and-selection.md#diffusiongemma-26b-a4b-googles-experimental-blockwise-discrete-diffusion-text-generator)

<a id="grok-45-spacexais-fast-frontier-model-for-coding-agents-and-knowledge-work"></a>

**Grok 4.5: SpaceXAI’s fast frontier model for coding, agents, and knowledge work** → [Frontier overview and selection](frontier-overview-and-selection.md#grok-45-spacexais-fast-frontier-model-for-coding-agents-and-knowledge-work)

<a id="meta-muse-spark-11-metas-million-token-reasoning-model-for-personal-agents-and-multi-agent-orchestration"></a>

**Meta Muse Spark 1.1: Meta’s million-token reasoning model for personal agents and multi-agent orchestration** → [Frontier overview and selection](frontier-overview-and-selection.md#meta-muse-spark-11-metas-million-token-reasoning-model-for-personal-agents-and-multi-agent-orchestration)

<a id="gemini-35-flash-googles-stable-high-speed-frontier-model-for-agents-and-coding"></a>

**Gemini 3.5 Flash: Google’s stable high-speed frontier model for agents and coding** → [Frontier overview and selection](frontier-overview-and-selection.md#gemini-35-flash-googles-stable-high-speed-frontier-model-for-agents-and-coding)

<a id="gpt-live-1-openais-full-duplex-conversational-model-for-continuous-listening-and-speaking"></a>

**GPT-Live-1: OpenAI’s full-duplex conversational model for continuous listening and speaking** → [Frontier overview and selection](frontier-overview-and-selection.md#gpt-live-1-openais-full-duplex-conversational-model-for-continuous-listening-and-speaking)

<a id="gpt-live-1-mini-the-lower-cost-live-conversation-path-for-broad-access"></a>

**GPT-Live-1 Mini: The lower-cost live-conversation path for broad access** → [Frontier overview and selection](frontier-overview-and-selection.md#gpt-live-1-mini-the-lower-cost-live-conversation-path-for-broad-access)

<a id="gemini-35-flash-live-translate-googles-preview-simultaneous-translation-model-for-more-than-70-languages"></a>

**Gemini 3.5 Flash Live Translate: Google’s preview simultaneous-translation model for more than 70 languages** → [Frontier overview and selection](frontier-overview-and-selection.md#gemini-35-flash-live-translate-googles-preview-simultaneous-translation-model-for-more-than-70-languages)

<a id="gpt-image-2-openais-state-of-the-art-image-generation-and-editing-model"></a>

**GPT Image 2: OpenAI’s state-of-the-art image generation and editing model** → [Frontier overview and selection](frontier-overview-and-selection.md#gpt-image-2-openais-state-of-the-art-image-generation-and-editing-model)

<a id="nano-banana-2-googles-general-purpose-gemini-31-flash-image-model"></a>

**Nano Banana 2: Google’s general-purpose Gemini 3.1 Flash Image model** → [Frontier overview and selection](frontier-overview-and-selection.md#nano-banana-2-googles-general-purpose-gemini-31-flash-image-model)

<a id="nano-banana-pro-googles-gemini-3-pro-image-model-for-maximum-control-and-professional-layouts"></a>

**Nano Banana Pro: Google’s Gemini 3 Pro Image model for maximum control and professional layouts** → [Frontier overview and selection](frontier-overview-and-selection.md#nano-banana-pro-googles-gemini-3-pro-image-model-for-maximum-control-and-professional-layouts)

<a id="nano-banana-2-lite-googles-ultra-low-latency-gemini-31-flash-lite-image-model"></a>

**Nano Banana 2 Lite: Google’s ultra-low-latency Gemini 3.1 Flash Lite Image model** → [Frontier overview and selection](frontier-overview-and-selection.md#nano-banana-2-lite-googles-ultra-low-latency-gemini-31-flash-lite-image-model)

<a id="seedream-50-pro-bytedance-dreaminas-professional-image-generation-and-editing-system"></a>

**Seedream 5.0 Pro: ByteDance Dreamina’s professional image generation and editing system** → [Frontier overview and selection](frontier-overview-and-selection.md#seedream-50-pro-bytedance-dreaminas-professional-image-generation-and-editing-system)

<a id="muse-image-metas-agentic-image-generation-and-editing-model-with-search-and-coding-tools"></a>

**Muse Image: Meta’s agentic image generation and editing model with search and coding tools** → [Frontier overview and selection](frontier-overview-and-selection.md#muse-image-metas-agentic-image-generation-and-editing-model-with-search-and-coding-tools)

<a id="muse-video-metas-preview-video-model-focused-on-fidelity-native-audio-and-physical-motion"></a>

**Muse Video: Meta’s preview video model focused on fidelity, native audio, and physical motion** → [Frontier overview and selection](frontier-overview-and-selection.md#muse-video-metas-preview-video-model-focused-on-fidelity-native-audio-and-physical-motion)

<a id="veo-31-lite-preview-googles-lower-cost-developer-video-model-with-audio-output"></a>

**Veo 3.1 Lite Preview: Google’s lower-cost developer video model with audio output** → [Frontier overview and selection](frontier-overview-and-selection.md#veo-31-lite-preview-googles-lower-cost-developer-video-model-with-audio-output)

<a id="lyria-3-clip-preview-googles-30-second-music-generation-model"></a>

**Lyria 3 Clip Preview: Google’s 30-second music generation model** → [Frontier overview and selection](frontier-overview-and-selection.md#lyria-3-clip-preview-googles-30-second-music-generation-model)

<a id="lyria-3-pro-preview-googles-longer-form-prompted-music-model"></a>

**Lyria 3 Pro Preview: Google’s longer-form prompted music model** → [Frontier overview and selection](frontier-overview-and-selection.md#lyria-3-pro-preview-googles-longer-form-prompted-music-model)

<a id="gemini-omni-flash-preview-googles-conversational-video-generation-and-editing-model"></a>

**Gemini Omni Flash Preview: Google’s conversational video generation and editing model** → [Frontier overview and selection](frontier-overview-and-selection.md#gemini-omni-flash-preview-googles-conversational-video-generation-and-editing-model)

<a id="gemini-robotics-er-16-googles-preview-embodied-reasoning-vlm-for-perception-and-high-level-robot-planning"></a>

**Gemini Robotics-ER 1.6: Google’s preview embodied-reasoning VLM for perception and high-level robot planning** → [Frontier overview and selection](frontier-overview-and-selection.md#gemini-robotics-er-16-googles-preview-embodied-reasoning-vlm-for-perception-and-high-level-robot-planning)

<a id="gemini-35-pro-googles-announced-but-unreleased-next-pro-model"></a>

**Gemini 3.5 Pro: Google’s announced but unreleased next Pro model** → [Frontier overview and selection](frontier-overview-and-selection.md#gemini-35-pro-googles-announced-but-unreleased-next-pro-model)

<a id="gpt-56-is-a-family-not-a-ladder-of-nicknames"></a>

**GPT-5.6 Is a Family, Not a Ladder of Nicknames** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#gpt-56-is-a-family-not-a-ladder-of-nicknames)

<a id="standard-chatgpt-chat"></a>

**Standard ChatGPT Chat** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#standard-chatgpt-chat)

<a id="work-and-codex"></a>

**Work and Codex** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#work-and-codex)

<a id="api"></a>

**API** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#api)

<a id="what-each-gpt-56-effort-is-for"></a>

**What Each GPT-5.6 Effort Is For** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#what-each-gpt-56-effort-is-for)

<a id="sol-at-low-medium-high-extra-high-max-and-ultra"></a>

**Sol at Low, Medium, High, Extra High, Max, and Ultra** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#sol-at-low-medium-high-extra-high-max-and-ultra)

<a id="terra-at-low-medium-high-extra-high-max-and-ultra"></a>

**Terra at Low, Medium, High, Extra High, Max, and Ultra** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#terra-at-low-medium-high-extra-high-max-and-ultra)

<a id="luna-at-low-medium-high-extra-high-and-max"></a>

**Luna at Low, Medium, High, Extra High, and Max** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#luna-at-low-medium-high-extra-high-and-max)

<a id="prompt-patterns-by-interface"></a>

**Prompt Patterns by Interface** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#prompt-patterns-by-interface)

<a id="price-context-and-caching"></a>

**Price, Context, and Caching** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#price-context-and-caching)

<a id="safeguards-and-reliability"></a>

**Safeguards and Reliability** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#safeguards-and-reliability)

<a id="watch-gpt-56-family-testing"></a>

**Watch: GPT-5.6 Family Testing** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#watch-gpt-56-family-testing)

<a id="claude-fable-5-and-claude-opus-48"></a>

**Claude Fable 5 and Claude Opus 4.8** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#claude-fable-5-and-claude-opus-48)

<a id="the-july-19-subscription-access-update"></a>

**The July 19 Subscription Access Update** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#the-july-19-subscription-access-update)

<a id="price-context-and-fallback"></a>

**Price, Context, and Fallback** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#price-context-and-fallback)

<a id="claude-opus-48-as-model-and-claude-code-configuration"></a>

**Claude Opus 4.8 as Model and Claude Code Configuration** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#claude-opus-48-as-model-and-claude-code-configuration)

<a id="claude-sonnet-5"></a>

**Claude Sonnet 5** → [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md#claude-sonnet-5)

<a id="coding-agentic-and-cost-efficient-model-additions"></a>

**Coding, Agentic, and Cost-Efficient Model Additions** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#coding-agentic-and-cost-efficient-model-additions)

<a id="deepseek-v4-pro-and-deepseek-v4-flash"></a>

**DeepSeek-V4-Pro and DeepSeek-V4-Flash** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#deepseek-v4-pro-and-deepseek-v4-flash)

<a id="glm-52"></a>

**GLM-5.2** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#glm-52)

<a id="current-mistral-family-by-workload"></a>

**Current Mistral Family by Workload** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#current-mistral-family-by-workload)

<a id="google-open-media-and-robotics-systems"></a>

**Google Open, Media, and Robotics Systems** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#google-open-media-and-robotics-systems)

<a id="watchlist-gemini-35-pro"></a>

**Watchlist: Gemini 3.5 Pro** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#watchlist-gemini-35-pro)

<a id="detailed-dossiers-for-the-newly-audited-systems"></a>

**Detailed Dossiers for the Newly Audited Systems** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#detailed-dossiers-for-the-newly-audited-systems)

<a id="claude-sonnet-5-product-surface-work-shape-and-review-discipline"></a>

**Claude Sonnet 5: Product Surface, Work Shape, and Review Discipline** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#claude-sonnet-5-product-surface-work-shape-and-review-discipline)

<a id="deepseek-v4-pro-and-deepseek-v4-flash-preview-apis-with-deliberate-modes"></a>

**DeepSeek-V4-Pro and DeepSeek-V4-Flash: Preview APIs With Deliberate Modes** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#deepseek-v4-pro-and-deepseek-v4-flash-preview-apis-with-deliberate-modes)

<a id="glm-52-long-horizon-claims-need-long-horizon-evidence"></a>

**GLM-5.2: Long-Horizon Claims Need Long-Horizon Evidence** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#glm-52-long-horizon-claims-need-long-horizon-evidence)

<a id="mistral-medium-35-and-mistral-small-4-generalist-models-with-different-operating-envelopes"></a>

**Mistral Medium 3.5 and Mistral Small 4: Generalist Models With Different Operating Envelopes** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#mistral-medium-35-and-mistral-small-4-generalist-models-with-different-operating-envelopes)

<a id="mistral-ocr-4-document-intelligence-must-be-tested-as-extraction"></a>

**Mistral OCR 4: Document Intelligence Must Be Tested as Extraction** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#mistral-ocr-4-document-intelligence-must-be-tested-as-extraction)

<a id="voxtral-tts-speech-quality-consent-and-deployment-are-separate-decisions"></a>

**Voxtral TTS: Speech Quality, Consent, and Deployment Are Separate Decisions** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#voxtral-tts-speech-quality-consent-and-deployment-are-separate-decisions)

<a id="leanstral-15-treat-the-compiler-as-the-evaluator"></a>

**Leanstral 1.5: Treat the Compiler as the Evaluator** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#leanstral-15-treat-the-compiler-as-the-evaluator)

<a id="robostral-navigate-an-announcement-is-not-a-production-contract"></a>

**Robostral Navigate: An Announcement Is Not a Production Contract** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#robostral-navigate-an-announcement-is-not-a-production-contract)

<a id="gemma-4-open-weights-shift-responsibility-to-the-builder"></a>

**Gemma 4: Open Weights Shift Responsibility to the Builder** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#gemma-4-open-weights-shift-responsibility-to-the-builder)

<a id="diffusiongemma-a-different-generation-process-not-an-automatic-upgrade"></a>

**DiffusionGemma: A Different Generation Process, Not an Automatic Upgrade** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#diffusiongemma-a-different-generation-process-not-an-automatic-upgrade)

<a id="veo-31-lite-preview-video-is-a-sequence-not-a-single-frame"></a>

**Veo 3.1 Lite Preview: Video Is a Sequence, Not a Single Frame** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#veo-31-lite-preview-video-is-a-sequence-not-a-single-frame)

<a id="lyria-3-music-generation-needs-musical-and-rights-aware-evaluation"></a>

**Lyria 3: Music Generation Needs Musical and Rights-Aware Evaluation** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#lyria-3-music-generation-needs-musical-and-rights-aware-evaluation)

<a id="gemini-robotics-er-16-high-level-embodied-reasoning-not-motor-authority"></a>

**Gemini Robotics-ER 1.6: High-Level Embodied Reasoning, Not Motor Authority** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#gemini-robotics-er-16-high-level-embodied-reasoning-not-motor-authority)

<a id="gemini-35-pro-keep-the-watchlist-useful-without-pretending-it-is-released"></a>

**Gemini 3.5 Pro: Keep the Watchlist Useful Without Pretending It Is Released** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#gemini-35-pro-keep-the-watchlist-useful-without-pretending-it-is-released)

<a id="grok-45-in-grok-build"></a>

**Grok 4.5 in Grok Build** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#grok-45-in-grok-build)

<a id="artificial-analysis-what-the-scores-do-and-do-not-mean"></a>

**Artificial Analysis: What the Scores Do and Do Not Mean** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#artificial-analysis-what-the-scores-do-and-do-not-mean)

<a id="intelligence-index-v41"></a>

**Intelligence Index v4.1** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#intelligence-index-v41)

<a id="coding-agent-index"></a>

**Coding Agent Index** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#coding-agent-index)

<a id="aa-briefcase-and-other-useful-views"></a>

**AA-Briefcase and Other Useful Views** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#aa-briefcase-and-other-useful-views)

<a id="meta-muse-spark-11"></a>

**Meta Muse Spark 1.1** → [Open and specialist frontier models](frontier-open-and-specialist-models.md#meta-muse-spark-11)

<a id="gemini-35-flash"></a>

**Gemini 3.5 Flash** → [Google, live, image, and media systems](frontier-google-and-media.md#gemini-35-flash)

<a id="gpt-live-1-and-gemini-35-live-translate"></a>

**GPT-Live-1 and Gemini 3.5 Live Translate** → [Google, live, image, and media systems](frontier-google-and-media.md#gpt-live-1-and-gemini-35-live-translate)

<a id="gpt-live-1-and-gpt-live-1-mini"></a>

**GPT-Live-1 and GPT-Live-1 Mini** → [Google, live, image, and media systems](frontier-google-and-media.md#gpt-live-1-and-gpt-live-1-mini)

<a id="gemini-35-flash-live-translate"></a>

**Gemini 3.5 Flash Live Translate** → [Google, live, image, and media systems](frontier-google-and-media.md#gemini-35-flash-live-translate)

<a id="image-and-video-models"></a>

**Image and Video Models** → [Google, live, image, and media systems](frontier-google-and-media.md#image-and-video-models)

<a id="gpt-image-2"></a>

**GPT Image 2** → [Google, live, image, and media systems](frontier-google-and-media.md#gpt-image-2)

<a id="nano-banana-2-nano-banana-pro-and-nano-banana-2-lite"></a>

**Nano Banana 2, Nano Banana Pro, and Nano Banana 2 Lite** → [Google, live, image, and media systems](frontier-google-and-media.md#nano-banana-2-nano-banana-pro-and-nano-banana-2-lite)

<a id="seedream-50-pro"></a>

**Seedream 5.0 Pro** → [Google, live, image, and media systems](frontier-google-and-media.md#seedream-50-pro)

<a id="muse-image-and-muse-video"></a>

**Muse Image and Muse Video** → [Google, live, image, and media systems](frontier-google-and-media.md#muse-image-and-muse-video)

<a id="image-model-videos"></a>

**Image-model videos** → [Google, live, image, and media systems](frontier-google-and-media.md#image-model-videos)

<a id="gemini-omni-flash"></a>

**Gemini Omni Flash** → [Google, live, image, and media systems](frontier-google-and-media.md#gemini-omni-flash)

<a id="extended-operating-guidance-for-the-established-families"></a>

**Extended Operating Guidance for the Established Families** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#extended-operating-guidance-for-the-established-families)

<a id="gpt-56-sol-terra-and-luna"></a>

**GPT-5.6 Sol, Terra, and Luna** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gpt-56-sol-terra-and-luna)

<a id="claude-fable-5-and-claude-opus-48-1"></a>

**Claude Fable 5 and Claude Opus 4.8** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#claude-fable-5-and-claude-opus-48-1)

<a id="grok-45-and-muse-spark-11"></a>

**Grok 4.5 and Muse Spark 1.1** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#grok-45-and-muse-spark-11)

<a id="gemini-35-flash-1"></a>

**Gemini 3.5 Flash** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gemini-35-flash-1)

<a id="gpt-live-1-gpt-live-1-mini-and-gemini-live-translate"></a>

**GPT-Live-1, GPT-Live-1 Mini, and Gemini Live Translate** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gpt-live-1-gpt-live-1-mini-and-gemini-live-translate)

<a id="gpt-image-2-nano-banana-seedream-and-muse-image"></a>

**GPT Image 2, Nano Banana, Seedream, and Muse Image** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gpt-image-2-nano-banana-seedream-and-muse-image)

<a id="muse-video-veo-lyria-and-gemini-omni-flash"></a>

**Muse Video, Veo, Lyria, and Gemini Omni Flash** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#muse-video-veo-lyria-and-gemini-omni-flash)

<a id="comprehensive-architecture-performance-and-deployment-dossiers"></a>

**Comprehensive Architecture, Performance, and Deployment Dossiers** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#comprehensive-architecture-performance-and-deployment-dossiers)

<a id="gpt-56-sol-terra-and-luna-architecture-disclosure-and-performance-envelope"></a>

**GPT-5.6 Sol, Terra, and Luna: Architecture Disclosure and Performance Envelope** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gpt-56-sol-terra-and-luna-architecture-disclosure-and-performance-envelope)

<a id="claude-fable-5-safeguarded-frontier-model-with-an-evaluation-routing-caveat"></a>

**Claude Fable 5: Safeguarded Frontier Model With an Evaluation Routing Caveat** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#claude-fable-5-safeguarded-frontier-model-with-an-evaluation-routing-caveat)

<a id="claude-opus-48-closed-checkpoint-strong-agent-harness-cleaner-attribution"></a>

**Claude Opus 4.8: Closed Checkpoint, Strong Agent Harness, Cleaner Attribution** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#claude-opus-48-closed-checkpoint-strong-agent-harness-cleaner-attribution)

<a id="claude-sonnet-5-cost-sensitive-agentic-model-with-limited-architecture-disclosure"></a>

**Claude Sonnet 5: Cost-Sensitive Agentic Model With Limited Architecture Disclosure** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#claude-sonnet-5-cost-sensitive-agentic-model-with-limited-architecture-disclosure)

<a id="deepseek-v4-pro-and-deepseek-v4-flash-open-moe-architecture-in-detail"></a>

**DeepSeek-V4-Pro and DeepSeek-V4-Flash: Open MoE Architecture in Detail** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#deepseek-v4-pro-and-deepseek-v4-flash-open-moe-architecture-in-detail)

<a id="glm-52-744b-a40b-moe-with-indexshare-sparse-attention"></a>

**GLM-5.2: 744B-A40B MoE With IndexShare Sparse Attention** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#glm-52-744b-a40b-moe-with-indexshare-sparse-attention)

<a id="mistral-medium-35-dense-128b-multimodal-transformer"></a>

**Mistral Medium 3.5: Dense 128B Multimodal Transformer** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#mistral-medium-35-dense-128b-multimodal-transformer)

<a id="mistral-small-4-119b-a65b-moe-with-first-party-nvfp4"></a>

**Mistral Small 4: 119B-A6.5B MoE With First-Party NVFP4** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#mistral-small-4-119b-a65b-moe-with-first-party-nvfp4)

<a id="leanstral-15-same-moe-family-specialized-post-training"></a>

**Leanstral 1.5: Same MoE Family, Specialized Post-Training** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#leanstral-15-same-moe-family-specialized-post-training)

<a id="mistral-ocr-4-service-architecture-is-undisclosed-output-structure-is-the-product"></a>

**Mistral OCR 4: Service Architecture Is Undisclosed, Output Structure Is the Product** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#mistral-ocr-4-service-architecture-is-undisclosed-output-structure-is-the-product)

<a id="voxtral-tts-public-4b-speech-checkpoint-deployment-and-consent-matrix"></a>

**Voxtral TTS: Public 4B Speech Checkpoint, Deployment and Consent Matrix** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#voxtral-tts-public-4b-speech-checkpoint-deployment-and-consent-matrix)

<a id="gemma-4-family-variant-by-variant-architecture"></a>

**Gemma 4 Family: Variant-by-Variant Architecture** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gemma-4-family-variant-by-variant-architecture)

<a id="diffusiongemma-26b-a4b-blockwise-discrete-diffusion"></a>

**DiffusionGemma 26B-A4B: Blockwise Discrete Diffusion** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#diffusiongemma-26b-a4b-blockwise-discrete-diffusion)

<a id="grok-45-closed-model-openly-tool-centric-product-evaluation"></a>

**Grok 4.5: Closed Model, Openly Tool-Centric Product Evaluation** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#grok-45-closed-model-openly-tool-centric-product-evaluation)

<a id="meta-muse-spark-11-fast-hosted-reasoning-with-undisclosed-checkpoint-topology"></a>

**Meta Muse Spark 1.1: Fast Hosted Reasoning With Undisclosed Checkpoint Topology** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#meta-muse-spark-11-fast-hosted-reasoning-with-undisclosed-checkpoint-topology)

<a id="gemini-35-flash-hosted-multimodal-agent-model-with-tool-surface-separation"></a>

**Gemini 3.5 Flash: Hosted Multimodal Agent Model With Tool-Surface Separation** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gemini-35-flash-hosted-multimodal-agent-model-with-tool-surface-separation)

<a id="gpt-live-1-and-gpt-live-1-mini-full-duplex-system-architecture"></a>

**GPT-Live-1 and GPT-Live-1 Mini: Full-Duplex System Architecture** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gpt-live-1-and-gpt-live-1-mini-full-duplex-system-architecture)

<a id="gemini-35-flash-live-translate-streaming-translation-pipeline"></a>

**Gemini 3.5 Flash Live Translate: Streaming Translation Pipeline** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gemini-35-flash-live-translate-streaming-translation-pipeline)

<a id="gpt-image-2-product-capabilities-without-a-public-architecture-claim"></a>

**GPT Image 2: Product Capabilities Without a Public Architecture Claim** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gpt-image-2-product-capabilities-without-a-public-architecture-claim)

<a id="nano-banana-2-nano-banana-pro-and-nano-banana-2-lite-1"></a>

**Nano Banana 2, Nano Banana Pro, and Nano Banana 2 Lite** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#nano-banana-2-nano-banana-pro-and-nano-banana-2-lite-1)

<a id="seedream-50-pro-limited-first-party-english-technical-disclosure"></a>

**Seedream 5.0 Pro: Limited First-Party English Technical Disclosure** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#seedream-50-pro-limited-first-party-english-technical-disclosure)

<a id="muse-image-and-muse-video-1"></a>

**Muse Image and Muse Video** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#muse-image-and-muse-video-1)

<a id="veo-31-lite-preview-hosted-video-generation-with-explicit-product-limits"></a>

**Veo 3.1 Lite Preview: Hosted Video Generation With Explicit Product Limits** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#veo-31-lite-preview-hosted-video-generation-with-explicit-product-limits)

<a id="lyria-3-music-generation-product-not-a-text-model-benchmark-entry"></a>

**Lyria 3: Music-Generation Product, Not a Text-Model Benchmark Entry** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#lyria-3-music-generation-product-not-a-text-model-benchmark-entry)

<a id="gemini-omni-flash-unified-multimodal-service-with-closed-architecture"></a>

**Gemini Omni Flash: Unified Multimodal Service With Closed Architecture** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gemini-omni-flash-unified-multimodal-service-with-closed-architecture)

<a id="gemini-robotics-er-16-reasoning-model-above-a-safety-controller"></a>

**Gemini Robotics-ER 1.6: Reasoning Model Above a Safety Controller** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#gemini-robotics-er-16-reasoning-model-above-a-safety-controller)

<a id="robostral-navigate-research-watchlist-until-an-interface-exists"></a>

**Robostral Navigate: Research Watchlist Until an Interface Exists** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#robostral-navigate-research-watchlist-until-an-interface-exists)

<a id="artificial-analysis-and-benchmark-engineering-expanded-reproducibility-rules"></a>

**Artificial Analysis and Benchmark Engineering: Expanded Reproducibility Rules** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#artificial-analysis-and-benchmark-engineering-expanded-reproducibility-rules)

<a id="open-weight-quantization-and-deployment-reference"></a>

**Open-Weight Quantization and Deployment Reference** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#open-weight-quantization-and-deployment-reference)

<a id="model-guide-completeness-matrix"></a>

**Model-Guide Completeness Matrix** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#model-guide-completeness-matrix)

<a id="how-to-choose-without-chasing-a-single-winner"></a>

**How to Choose Without Chasing a Single Winner** → [Frontier overview and selection](frontier-overview-and-selection.md#how-to-choose-without-chasing-a-single-winner)

<a id="uncertainties-and-known-limits"></a>

**Uncertainties and Known Limits** → [Frontier evaluation and deployment](frontier-evaluation-and-deployment.md#uncertainties-and-known-limits)

<a id="sources"></a>

**Sources** → [Frontier sources and method](frontier-sources-and-method.md#sources)

<a id="method"></a>

**Method** → [Frontier sources and method](frontier-sources-and-method.md#method)


Compatibility map: [frontier-models-compatibility-map.json](frontier-models-compatibility-map.json)
