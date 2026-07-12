# Current Plan: 2026 Frontier Model and Multimodal Coverage

## Goal

Expand every model section in the primary frontier guide into a source-backed
technical dossier covering architecture, performance, benchmarks, deployment,
evaluation, and limitations. Open-weight entries must include the exact layers,
attention and expert topology, parameter counts, precision, quantization,
checkpoint footprint, runtime, and hardware evidence published by model owners.

![GPT-5.6 effort controls by product surface](../assets/model-guides/gpt-5-6-effort-surfaces.svg)

[![Watch a hands-on test of GPT-5.6 Sol, Terra, and Luna](https://i.ytimg.com/vi/xDXX2M5DrO0/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-5-6-family-test)

*Third-party workflow context. Official documentation remains the authority for
model access, effort menus, and prices.*

## Scope

- Every GPT, Claude, Grok, Meta, Gemini, live-audio, image, video, specialist,
  open-weight, and robotics section in the primary guide.
- The guide's shared benchmark, quantization, deployment, uncertainty, and
  source-reference sections.

## Measurable Outcome

- Every audited model has a substantive, category-appropriate dossier rather
  than a one-row listing.
- The primary guide gives every model practical task fit, architecture disclosure
  status, integration boundary, evaluation method, published benchmark context,
  cost considerations, deployment implications, and failure modes.
- Every open-weight model records exact configuration fields and first-party
  quantizations where available; absent fields remain explicitly unknown.
- Research and citations remain first-party, dated, and explicit about gaps.
- Regression tests enforce guide depth, key taxonomy, and uncertainty rules.

## Phases

- [x] Inspect the current guide, pack, source ledger, and repository state.
- [x] Re-verify the official sources needed for expanded factual detail.
- [x] Establish announcement-style dossiers for every named model and variant.
- [x] Establish the cross-model architecture and deployment reference.
- [x] Deepen DeepSeek V4, GLM-5.2, Mistral Small 4, and Gemma 4 from first-party configurations.
- [x] Audit remaining open/specialist model architecture, quantization, and checkpoint fields.
- [x] Audit every closed/media/live/robotics dossier for performance, benchmark, and unknown-field depth.
- [x] Add broad dossier-schema and open-model architecture regression tests.
- [x] Run final repository validation and review the complete diff.
- [x] Commit and push the final audited expansion.

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

- Commits `4bd2ba7` and `5ef44b5` established the large dossier corpus now on
  `origin/main`; the current pass audits and deepens it rather than replacing it.
- The guide currently exceeds 38,000 words and contains more than 40 structured
  announcement dossiers. Length is not completion evidence; field coverage and
  claim support remain the acceptance criteria.
- The first current-pass additions record DeepSeek V4 Pro topology and mixed
  precision, GLM-5.2 IndexShare/MoE configuration, Mistral Small 4 checkpoint and
  NVFP4 details, and Gemma 4 PLE/QAT/memory evidence.

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
- The first inline Python section counter used a raw regular expression inside
  an f-string expression and failed with a syntax error. Moving the expression
  to a compiled variable fixed the audit.
- A Gemma patch initially targeted text that had moved after the two large guide
  expansion commits. The existing family dossier was preserved and extended at
  its current location instead.

## Status

The full field audit, repository validation, commit, and push are complete.
