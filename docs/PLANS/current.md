# Current Plan: 2026 Frontier Model and Multimodal Coverage

## Goal

Audit the requested 2026 frontier, specialist, media, and embodied-reasoning
systems against current official sources. Expand the dated frontier essay and
prompting pack only for documented public surfaces, with a clear watchlist for
officially announced but unavailable systems.

![GPT-5.6 effort controls by product surface](../assets/model-guides/gpt-5-6-effort-surfaces.svg)

[![Watch a hands-on test of GPT-5.6 Sol, Terra, and Luna](https://i.ytimg.com/vi/xDXX2M5DrO0/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-5-6-family-test)

*Third-party workflow context. Official documentation remains the authority for
model access, effort menus, and prices.*

## Scope

- Claude Sonnet 5; DeepSeek V4 Pro and Flash; GLM-5.2.
- Mistral Medium 3.5, Small 4, OCR 4, Voxtral TTS, Leanstral 1.5, and
  Robostral Navigate.
- Gemma 4, DiffusionGemma, Veo 3.1 Lite, Lyria 3, Gemini Robotics-ER 1.6,
  and Gemini 3.5 Pro's release status.

## Measurable Outcome

- Every audit target has a documented outcome: released, preview, announced,
  or unconfirmed.
- Every new factual claim links to a visited official source and carries a
  checked date or a stated uncertainty.
- New prompting guides are indexed and contain task fit, tool boundaries,
  verification, failure modes, cost framing, and unsuitable uses.
- Regression tests protect the new guide set, taxonomy, watchlist, and links.

## Phases

- [x] Inspect the branch, existing essay, prompting pack, tests, and repository
  instructions.
- [x] Research every requested audit target through official sources.
- [x] Add source-conscious taxonomy, audit outcomes, and prompting guidance.
- [x] Update indexes and regression tests.
- [x] Run focused and full validation, review the diff, and commit on `main`.

## Key Questions

1. Which named systems have a documented public API or product surface?
2. Which specialist systems require different evaluation criteria from general
   language models?
3. Which facts are absent or conflict across official sources and must remain
   unknown?

## Decisions

- Preserve existing verified 2026 coverage and add grouped guides where models
  share an operational category.
- Use first-party sources for all release, identifier, availability, pricing,
  license, and capability claims. Do not add numerical benchmarks without an
  independent method.
- Keep Gemini 3.5 Pro on a watchlist because Google currently says only
  "coming soon" and provides no usable model identifier or access instructions.
- Keep Robostral Navigate out of production guidance because the official
  announcement is not paired with a documented public model surface.

## Checkpoint Notes

- Official-source sweep completed 2026-07-12. New release and access facts are
  linked in the frontier guide; no independent benchmark values were added.
- Gemini 3.5 Pro remains an official coming-soon watchlist entry. Robostral
  Navigate remains announced with limited public technical information.
- Focused prompting-guide tests, repository health, formatting check, full
  unit suite, and `git diff --check` passed before staging.

## Errors Encountered

- Initial parallel output truncated several guide bodies. Resolved by reading
  the files in smaller batches.
- The first `agent-reach doctor --json` output was omitted by the command batch.
  Resolved by running it separately; web access is available through Jina
  Reader and GitHub is available without authenticated extended features.
- PowerShell could not launch `rg.exe` in this session. The consistency scan
  used `Select-String` instead.
- `safe_autofix.py --check` requested deterministic wrapping in the new source
  ledger. `--write` applied only that formatting change and the diff was
  reviewed.

## Status

Documentation expansion is complete and validated. Commit only the listed
frontier-guide, prompting-guide, index, test, and plan changes; do not push.
