# Model Media Provenance Ledger

Checked: 2026-07-11

## Answer

The repository uses six original SVGs derived from verified sources and
visible, clickable YouTube preview cards for public videos. The preview cards
load thumbnails from YouTube and open the corresponding embedded player on
this repository's GitHub Pages site; no video binary or thumbnail is stored in
Git. The repository does not rehost
Artificial Analysis charts, vendor launch graphics, or X screenshots.

![Availability map whose provenance is recorded below](../assets/model-guides/availability-map.svg)

[![Play the independent Every hands-on video about Fable 5](https://i.ytimg.com/vi/GrdEid8H6H4/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#fable-hands-on)

*Visible-media example covered by this ledger. Click the image to watch; the
video is third-party qualitative context.*

## Local assets

| Asset | Derivation | Source tier | Reuse status |
| --- | --- | --- | --- |
| `availability-map.svg` | Original summary of documented product surfaces. | Official vendor sources | Repository-created layout and text. |
| `aa-benchmark-comparison.svg` | Original bars using Intelligence Index v4.1 values Fable 60, Sol 59, Terra 55, Luna 51 and Coding Agent Index values Sol 80, Terra 77, Luna 75. | Independent | Repository-created chart; data attributed to Artificial Analysis. |
| `live-architecture.svg` | Original conceptual comparison of GPT-Live and Gemini Live Translate flows. | Official vendor sources | Repository-created diagram; not an implementation schematic. |
| `gpt-5-6-effort-surfaces.svg` | Original interface and effort map. | Official OpenAI sources plus a dated local Codex catalog query | Repository-created layout and text. |
| `aa-frontier-benchmark-2026-07-11.svg` | Original bars for the dated Intelligence and Coding Agent Index snapshot. | Independent and official launch data | Every coding score retains its harness and fallback label. |
| `multimodal-model-map-2026.svg` | Original taxonomy of current audio, image, and video systems. | Official vendor sources | Undisclosed architectures remain marked as such. |

## Linked visual and video media

| Media | Publisher | Evidence use | Reuse decision |
| --- | --- | --- | --- |
| [GPT-5.6 launch](https://openai.com/index/gpt-5-6/) | OpenAI, 2026-07-09 | Official availability, product visuals, vendor benchmarks | Link to the page; do not copy its artwork. |
| [Introducing GPT-Live](https://openai.com/index/introducing-gpt-live/) | OpenAI, 2026-07-08 | Official architecture claims and watchable demos | Link to on-page media. |
| [Fable 5 launch](https://www.anthropic.com/news/claude-fable-5-mythos-5) | Anthropic, 2026-06-09 | Official availability, visuals, and demos | Link to the page; do not hotlink its image CDN. |
| [Introducing Claude Fable 5](https://www.youtube.com/watch?v=Y9Wz2PV404E) | Anthropic, 2026-06-09 | Official watchable overview | Visible remote YouTube thumbnail linked to the public video. |
| [Grok 4.5 launch](https://x.ai/news/grok-4-5) | SpaceXAI, 2026-07-08 | Official availability, visuals, and demos | Link to the page. |
| [Gemini 3.5 Live Translate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/) | Google, 2026-06-09 | Official availability and watchable demos | Link to on-page videos. |
| [Fable 5 in GitHub Copilot](https://x.com/github/status/2064402372961484864) | GitHub on X, 2026-06-09 | Official platform availability signal | Link only; screenshot permission not found. |
| [Gemini Live Translate demo](https://x.com/GoogleDeepMind/status/2064366509216928102) | Google DeepMind on X, 2026-06-09 | Official social demonstration | Link only; screenshot permission not found. |
| [Fable 5 hands-on](https://www.youtube.com/watch?v=GrdEid8H6H4) | Every, 2026-06-09 | Third-party qualitative context | Visible remote YouTube thumbnail; not benchmark evidence. |
| [GPT-5.6 Sol explainer](https://www.youtube.com/watch?v=tV5zXS78HzU) | IBM Technology, 2026-07-03 | Third-party preview context | Visible remote YouTube thumbnail; verify launch facts elsewhere. |
| [GPT-5.6 launch-day discussion](https://www.youtube.com/watch?v=QjuuTHJKxWI) | ThursdAI, 2026-07-09 | Community reaction and GPT-Live discussion | Visible remote YouTube thumbnail; not factual authority. |
| [GPT-5.6 family test](https://www.youtube.com/watch?v=xDXX2M5DrO0) | AICodeKing | Third-party hands-on context | Embedded with a visible thumbnail; not access or pricing authority. |
| [Gemini 3.5 Flash coding test](https://www.youtube.com/watch?v=TdN-YdFLWvY) | Bijan Bowen | Third-party coding context | Embedded; official Google docs define model controls. |
| [Grok 4.5 coding test](https://www.youtube.com/watch?v=5J6HCDEkg64) | ForrestKnight | Third-party coding context | Embedded; SpaceXAI and Artificial Analysis support factual claims. |
| [Muse Spark 1.1 test](https://www.youtube.com/watch?v=XCYYDhG9zKw) | Bijan Bowen | Third-party hands-on context | Embedded; Meta and Artificial Analysis support factual claims. |
| [Image-model comparison](https://www.youtube.com/watch?v=FDhx79PU5KQ) | Code And Create | Qualitative image comparison | Embedded; readers should inspect prompts and outputs. |
| [Introducing ChatGPT Images 2.0](https://www.youtube.com/watch?v=sWkGomJ3TLI) | OpenAI | Official product demonstration | Embedded; not evidence of an undisclosed architecture. |
| [ChatGPT Voice powered by GPT-Live](https://www.youtube.com/watch?v=EAN5Cj347PY) | OpenAI | Official product demonstration | Embedded; architecture claims remain tied to the launch post. |

## Uncertainties

- A public web page or video is not automatically licensed for redistribution.
- X and YouTube content can be removed, region-blocked, or made non-embeddable.
- GitHub does not provide inline YouTube playback in repository Markdown. A
  thumbnail click opens the embedded player on this repository's GitHub Pages
  site, so the viewer does not navigate to YouTube.
- Live benchmark pages can change. The local chart therefore carries a checked
  date and benchmark version.
- All eleven selected videos were public and reported
  `playable_in_embed=True` in `yt-dlp` on the checked date.
- This ledger records a conservative documentation decision, not legal advice.

## Sources

- [Artificial Analysis: GPT-5.6 has landed](https://artificialanalysis.ai/articles/gpt-5-6-has-landed), published 2026-07-09.
- [Artificial Analysis: GPT-5.6 Sol](https://artificialanalysis.ai/models/gpt-5-6-sol), accessed 2026-07-11.
- [Artificial Analysis: Claude Fable 5](https://artificialanalysis.ai/models/claude-fable-5/), accessed 2026-07-11.
- [Artificial Analysis Terms of Use](https://artificialanalysis.ai/docs/legal/Terms-of-Use.pdf), revised 2024-04-28.
- Official vendor and media pages listed in the table above, accessed 2026-07-11.

## Method

Official pages were checked before social and community sources. Independent
benchmark values were included only when the score, configuration, and current
benchmark version were readable. Artwork was linked rather than copied when
reuse permission was absent or unclear.
