# Current Plan: 2026 Frontier Model and Multimodal Coverage

## Goal

Expand every model section in the primary frontier guide into materially deeper,
task-oriented reference material. Preserve source boundaries: the added detail
must explain documented controls, evaluation methods, integration limits, and
failure modes without filling unknowns with plausible guesses.

![GPT-5.6 effort controls by product surface](../assets/model-guides/gpt-5-6-effort-surfaces.svg)

[![Watch a hands-on test of GPT-5.6 Sol, Terra, and Luna](https://i.ytimg.com/vi/xDXX2M5DrO0/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-5-6-family-test)

*Third-party workflow context. Official documentation remains the authority for
model access, effort menus, and prices.*

## Scope

- Every GPT, Claude, Grok, Meta, Gemini, live-audio, image, video, specialist,
  open-weight, and robotics section in the primary guide.
- Every file in `docs/guides/model-prompting/`, while keeping its index and
  source ledger coherent with the expanded primary guide.

## Measurable Outcome

- Every audited model has a substantive, category-appropriate dossier rather
  than a one-row listing.
- The primary guide and prompting pack give every model practical task fit,
  integration boundary, evaluation method, cost considerations where published,
  prompt patterns, and failure modes.
- Research and citations remain first-party, dated, and explicit about gaps.
- Regression tests enforce guide depth, key taxonomy, and uncertainty rules.

## Phases

- [x] Inspect the current guide, pack, source ledger, and repository state.
- [x] Re-verify the official sources needed for expanded factual detail.
- [x] Expand every model dossier and prompting guide with operational depth.
- [x] Strengthen depth and classification regression tests.
- [x] Validate the reviewed documentation change.
- [x] Commit and push the reviewed documentation change.

## Key Questions

1. What additional information is documented well enough to explain safely?
2. Which operational facts should remain unavailable or preview-only?
3. How can readers reproduce an evaluation without conflating specialist and
   general-purpose model measures?

## Decisions

- Use detailed subsections where the first-party source establishes facts; use
  explicit unknowns where it does not.
- Retain the existing categories, rather than forcing OCR, TTS, proof, and
  embodied reasoning into a frontier generalist ranking.
- Preserve Gemini 3.5 Pro as watchlist-only and Robostral Navigate as announced
  with limited public technical detail.

## Checkpoint Notes

- Previous source sweep establishes the starting source set. This expansion will
  re-open the load-bearing primary sources before adding detail.

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
- The direct Anthropic promotional-access support page was unavailable through
  the web reader, but the user supplied the current official wording and linked
  Claude Code terms: Fable access and the 50% Claude Code weekly-limit increase
  run through July 19, 2026 at 11:59:59 PM PT.

## Status

Expanded-dossier work is validated and committed; push to the established remote
is the final pending operation.
