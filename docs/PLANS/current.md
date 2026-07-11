# Current Plan: Frontier Models and Multimodal Systems

## Goal

Publish a source-checked long-form guide to GPT-5.6, Claude Fable 5, Grok 4.5,
Gemini 3.5, current image models, and live-audio systems, with original charts
and watchable embedded videos.

![Current Artificial Analysis benchmark snapshot](../assets/model-guides/aa-frontier-benchmark-2026-07-11.svg)

[![Watch the GPT-5.6, GPT-Live, Grok 4.5, and Muse Spark launch discussion](https://i.ytimg.com/vi/QjuuTHJKxWI/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#launch-discussion)

## Measurable Outcome

- One dated guide distinguishes confirmed facts, vendor claims, independent
  benchmarks, local interface evidence, and unresolved claims.
- GPT-5.6 interface and effort tables cover Chat, Work, Codex, and API without
  presenting account-specific observations as universal access.
- Original figures show the effort surface, current benchmark snapshot, and
  multimodal model map.
- The GitHub Pages gallery includes verified, embeddable videos for the major
  model groups covered by the guide.
- Deterministic tests cover asset links, accessibility metadata, source
  sections, model-name corrections, gallery anchors, and iframe sources.
- A dated video research pack covers every requested release with either
  verified metadata or an explicitly non-evidentiary discovery search.

## Phases

- [x] Inspect the current guides, media gallery, source ledgers, and branch.
- [x] Verify official OpenAI, Anthropic, SpaceXAI, Google, Meta, and ByteDance
  sources plus Artificial Analysis results.
- [x] Write the long-form guide and original figures.
- [x] Expand the embedded gallery and repository navigation.
- [x] Add regression coverage for the new assets, guide, and gallery entries.
- [x] Run the repository command suite and inspect every result.
- [x] Create the requested commit on `main`.

## Key Corrections

- Current Codex labels use `low`, not `light`.
- Nano Banana 2 is Gemini 3.1 Flash Image. Gemini 3 Pro Image is Nano Banana
  Pro.
- Artificial Analysis names its agentic coding composite the Coding Agent
  Index, not the Codex Index.
- Artificial Analysis tested GPT-5.6 Sol at `max`; `ultra` is a separate
  multi-agent product mode.
- OpenAI does not publicly document GPT Image 2 as a fully autoregressive
  architecture. That architecture claim remains unconfirmed.

## Existing Repository State

The earlier `CLAUDE.md` edit is already part of commit `cd09d15`; it is not an
unstaged file in this continuation. All new changes from this pass remain in
the requested all-changes staging scope.

## Status

Essay expansion, media classification, video research, figures, navigation,
provenance, and regression tests are complete. Verification on 2026-07-12:

- `python scripts/repo_health_check.py`: passed.
- `python scripts/safe_autofix.py --check`: no changes needed.
- `python -m unittest discover -s tests`: 94 tests passed.
- `git diff --check`: passed; Git only reported line-ending conversion notices.
- Focused model-media suite: 11 tests passed.
- Six SVG files parsed as XML and include non-empty titles and descriptions.
- Eleven gallery iframes use privacy-enhanced YouTube sources, lazy loading,
  descriptive titles, fullscreen support, and unique HTML anchors.
- The expected GitHub Pages media URL returned HTTP 200.
