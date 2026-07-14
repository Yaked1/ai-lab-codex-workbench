# Frontier Model Essay Research Notes

Checked: 2026-07-11

## Source Questions

1. Which GPT-5.6 models and efforts are confirmed on Chat, Work, Codex, and
   the API?
2. Which subscription, pricing, and cutoff claims are current?
3. Which Artificial Analysis results are directly comparable, and which embed
   a product harness or fallback?
4. Which multimodal model names and architecture claims are official?
5. Which videos are public, correctly titled, and embeddable?

## Confirmed Findings

- Standard ChatGPT uses GPT-5.6 Sol for Medium, High, and Extra High, with Sol
  Pro behind Pro. Plus includes Medium and High. Both Pro tiers have the same
  model capabilities; their 5x and 20x labels describe usage allowances.
- The launch post confirms Sol, Terra, and Luna in Work and Codex for eligible
  paid plans, `max` for users with GPT-5.6 access, Work `ultra` for Pro and
  Enterprise, and Codex `ultra` for Plus and higher.
- The local Codex 0.144.0 catalog exposes Sol and Terra at low, medium, high,
  xhigh, max, and ultra; Luna exposes low through max.
- The API exposes none, low, medium, high, xhigh, and max. Multi-agent beta is
  separate from API reasoning effort.
- Historical snapshot: the 2026-07-12 Fable deadline recorded here was
  superseded. Anthropic's [current promotion terms](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access),
  updated July 13, 2026, extend included promotional access through July 19,
  2026 at 11:59:59 PM PT. A separate 50% Claude Code weekly-limit increase ends
  at the same time. Afterward Fable remains available using usage credits; API
  use is always billed separately.
- Artificial Analysis Coding Agent Index: Sol Max in Codex 80, Terra Max 77,
  Fable Max with fallback in Claude Code 77, Grok 4.5 in Grok Build 76, Luna
  Max 75, and Opus 4.8 Max in Claude Code 73.
- Artificial Analysis Intelligence Index v4.1 launch snapshot: Fable Max with
  fallback 60, Sol Max 59, Opus 4.8 Max about 56, Terra Max 55, Grok 4.5 High
  54, Luna Max 51, Muse Spark 1.1 xhigh 51, and Gemini 3.5 Flash High 50.
- Gemini 3.5 Flash API thinking levels are minimal, low, medium, and high.
  Gemini Apps uses Standard and Extended labels where available.
- Nano Banana 2 is `gemini-3.1-flash-image`; Nano Banana Pro is
  `gemini-3-pro-image`; Nano Banana 2 Lite is
  `gemini-3.1-flash-lite-image`.
- Gemini Omni Flash starts with video output from multimodal inputs. Gemini
  3.5 Live Translate is an audio-only translation path supporting 70+
  languages.
- GPT-Live is vendor-described as continuous full duplex with separate
  delegation for deeper work.

## Unconfirmed or Qualified

- OpenAI does not enumerate every lower effort label for every Work surface in
  the public help pages. Desktop Work and web Work menus can vary by rollout,
  plan, workspace policy, and client version.
- GPT Image 2 is officially described as a state-of-the-art generation and
  editing model. Its claimed fully autoregressive internal architecture is not
  disclosed in the checked OpenAI documentation.
- Seedream 5.0 Pro is visible on ByteDance's Dreamina surface, but English
  first-party technical documentation is limited. Architecture claims require
  qualification.
- Live benchmark pages can change after this checked date. Every local chart
  must include its benchmark version, configuration, and date.

## Verified Video Set

All selected videos were public and `playable_in_embed=True` in `yt-dlp` on
2026-07-11.

| ID | Publisher | Role |
| --- | --- | --- |
| `Y9Wz2PV404E` | Anthropic | Official Fable 5 overview |
| `GrdEid8H6H4` | Every | Fable 5 hands-on |
| `tV5zXS78HzU` | IBM Technology | GPT-5.6 Sol discussion |
| `QjuuTHJKxWI` | ThursdAI | Launch-day discussion |
| `xDXX2M5DrO0` | AICodeKing | GPT-5.6 family test |
| `TdN-YdFLWvY` | Bijan Bowen | Gemini 3.5 Flash coding test |
| `5J6HCDEkg64` | ForrestKnight | Grok 4.5 coding test |
| `XCYYDhG9zKw` | Bijan Bowen | Muse Spark 1.1 test |
| `FDhx79PU5KQ` | Code And Create | Image-model comparison |
| `sWkGomJ3TLI` | OpenAI | Official ChatGPT Images 2.0 demo |
| `EAN5Cj347PY` | OpenAI | Official GPT-Live demo |

The image-model video `FDhx79PU5KQ` is not a Gemini Omni Flash demo. Topics
without a verified individual video are recorded as discovery searches in the
[video research pack](../research/video-research-pack-2026-07-11.md).

## Research Tool Notes

- `agent-reach doctor --json` found web access available and YouTube through
  `yt-dlp`; X was not configured and was not used for factual claims.
- The OpenAI Codex manual helper failed because the response omitted its
  expected `x-content-sha256` header. Official OpenAI launch, Help Center, and
  developer pages were used as the fallback.
