# Google, live, image, and media systems

[← Frontier models index](frontier-models-and-multimodal-systems-2026.md)

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

<!-- frontier-migration-boundary -->
