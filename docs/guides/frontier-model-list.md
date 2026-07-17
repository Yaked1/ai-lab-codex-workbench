# Frontier Model List

Checked: 2026-07-17

This is the compact index for model families covered by the repository's
frontier guides. It is a navigation and evidence-status list, not a universal
ranking. Prices, access, model IDs, architecture, and benchmark configurations
must be rechecked at the linked source pages before deployment.

## Hosted frontier reasoning and agent models

| Model | Status | Architecture disclosure | Primary repository coverage |
| --- | --- | --- | --- |
| GPT-5.6 Sol | Hosted proprietary | Undisclosed | [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md) |
| GPT-5.6 Terra | Hosted proprietary | Undisclosed | [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md) |
| GPT-5.6 Luna | Hosted proprietary | Undisclosed | [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md) |
| Claude Fable 5 | Hosted proprietary | Undisclosed | [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md) |
| Claude Opus 4.8 | Hosted proprietary | Undisclosed | [OpenAI and Anthropic frontier systems](frontier-openai-and-anthropic.md) |
| Claude Sonnet 5 | Hosted proprietary | Undisclosed | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| Kimi K3 | Hosted now; full weights announced by July 27, 2026 | 2.8T MoE; 16 / 896 experts active; KDA, AttnRes, Stable LatentMoE | [Kimi K3 frontier dossier](kimi-k3-frontier-dossier.md) |
| Grok 4.5 | Hosted proprietary | Undisclosed | [Frontier overview and selection](frontier-overview-and-selection.md) |
| Gemini 3.5 Flash | Hosted proprietary | Undisclosed | [Google, live, image, and media systems](frontier-google-and-media.md) |
| Meta Muse Spark 1.1 | Hosted proprietary | Undisclosed | [Frontier overview and selection](frontier-overview-and-selection.md) |

## Open-weight and announced-open frontier models

| Model | Status | Disclosed scale or specialization | Primary repository coverage |
| --- | --- | --- | --- |
| Kimi K3 | Weights announced, not yet inspectable on checked date | 2.8T total; 16 / 896 experts active | [Kimi K3 frontier dossier](kimi-k3-frontier-dossier.md) |
| DeepSeek-V4-Pro | Preview API and open weights | 1.6T total / 49B active | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| DeepSeek-V4-Flash | Preview API and open weights | 284B total / 13B active | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| GLM-5.2 | Open source | 744B total / 40B active | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| Mistral Medium 3.5 | Open weights | Dense 128B multimodal model | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| Mistral Small 4 | Open weights | 119B total / 6.5B active MoE | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| Gemma 4 family | Open weights | Multiple dense and sparse variants | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| DiffusionGemma | Experimental open model | 25.2B total / 3.8B active discrete diffusion | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |

## Specialist, live, image, video, music, and robotics systems

| Family or model | Category | Primary repository coverage |
| --- | --- | --- |
| Mistral OCR 4 | Document intelligence | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| Voxtral TTS | Speech synthesis | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| Leanstral 1.5 | Lean proof engineering | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| Robostral Navigate | Embodied navigation | [Open and specialist frontier models](frontier-open-and-specialist-models.md) |
| GPT-Live-1 and GPT-Live-1 Mini | Live voice | [Google, live, image, and media systems](frontier-google-and-media.md) |
| Gemini 3.5 Flash Live Translate | Simultaneous translation | [Google, live, image, and media systems](frontier-google-and-media.md) |
| GPT Image 2 | Image generation and editing | [Google, live, image, and media systems](frontier-google-and-media.md) |
| Nano Banana family | Image generation and editing | [Google, live, image, and media systems](frontier-google-and-media.md) |
| Seedream 5.0 Pro | Image generation and editing | [Google, live, image, and media systems](frontier-google-and-media.md) |
| Muse Image and Muse Video | Image and video | [Google, live, image, and media systems](frontier-google-and-media.md) |
| Veo 3.1 Lite Preview | Video generation | [Google, live, image, and media systems](frontier-google-and-media.md) |
| Lyria 3 family | Music generation | [Google, live, image, and media systems](frontier-google-and-media.md) |
| Gemini Robotics-ER 1.6 | Embodied-reasoning VLM | [Google, live, image, and media systems](frontier-google-and-media.md) |

## Evidence rules

- A hosted release and an open-weight checkpoint are separate availability facts.
- An announced weight date is not evidence that files or a license are already public.
- Vendor benchmark rows stay attached to their stated effort, harness, tools, and limits.
- Closed-model parameter counts remain unknown unless the vendor publishes them.
- A model or product-family name does not prove account access, regional access, or a stable API identifier.
- Recheck the dated dossier whenever a provider changes weights, pricing, effort modes, model IDs, or product access.
