# Current Plan: Model and Effort Prompting Guide Pack

## Goal

Finish the prompting-guide pack started by Grok, using the dated frontier-model
essay as the main repository source and current official vendor documentation
for claims that can change. The finished pack must give each named model and
effort mode useful, surface-aware prompt patterns without forcing every guide
to the same length.

![GPT-5.6 effort controls by product surface](../assets/model-guides/gpt-5-6-effort-surfaces.svg)

[![Watch a hands-on test of GPT-5.6 Sol, Terra, and Luna](https://i.ytimg.com/vi/xDXX2M5DrO0/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-5-6-family-test)

*Third-party workflow context. Official documentation remains the authority for
model access, effort menus, and prices.*

## Scope

- GPT-5.6 Sol, Terra, and Luna across Codex CLI, ChatGPT Desktop, web Work,
  standard Chat, and API where supported.
- Claude Fable 5 and Opus 4.8 across Claude web, Claude Code, Desktop Code,
  API, and Fable's post-promotion usage-credit transition.
- Grok 4.5 in Grok Build.
- Meta Muse Spark 1.1, Muse Image, and the unavailable Muse Video path.
- Gemini 3.5 Flash, Gemini 3.5 Live Translate, and Gemini Omni Flash.
- GPT-Live-1, GPT-Live-1 Mini, GPT Image 2, Nano Banana Pro, Nano Banana 2,
  Nano Banana 2 Lite, and Seedream 5.0 Pro.

## Measurable Outcome

- Every named model is covered by an indexed prompting guide or a clearly
  separated model section in a family guide.
- Every documented or observed effort label is mapped to its product surface.
- Copy-ready prompts include scope, constraints, verification, and failure
  behavior rather than marketing prose alone.
- Official facts, dated interface observations, independent results,
  interpretations, and unconfirmed claims remain distinct.
- Tests enforce the required guide set, effort coverage, model-name mappings,
  source labels, navigation, and public-safety rules.

## Phases

- [x] Inspect the branch, existing essay, Grok-authored guide pack, tests, and
  repository instructions.
- [x] Verify changing product claims against current primary sources and the
  local Codex catalog/version evidence.
- [x] Correct surface and effort terminology without discarding useful Grok
  material.
- [x] Improve model guides according to task complexity and add missing depth
  only where it improves real prompting decisions.
- [x] Strengthen navigation, source notes, and regression tests.
- [x] Run focused and full repository verification, review the diff, and
  prepare the finished documentation change for commit.

## Key Questions

1. Which menus are official vendor documentation versus a dated local or user
   interface observation?
2. Does each effort section change the prompt strategy, or merely repeat a
   generic template?
3. Are Ultra and Ultracode described as orchestration instead of single-model
   effort values?
4. Are unavailable or undisclosed products clearly blocked from production
   guidance?
5. Can a reader select a model, surface, effort, prompt, and verification rule
   without reading the entire pack?

## Decisions

- Preserve the existing `docs/guides/model-prompting/` structure and improve it
  in place.
- Keep closely related image and live-audio variants in family guides when that
  avoids duplicated instructions, but give each model its own decision and
  prompt section.
- Treat Codex CLI `0.144.0` as both the official GPT-5.6 minimum and the local
  catalog snapshot. Record `0.144.1` separately as the latest stable npm release
  on the checked date.
- Treat Desktop `Light` and exact web Work menus as dated interface observations
  unless a current official help page enumerates them.
- Commit after all repository checks pass. Do not push unless explicitly asked.

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

All six phases are complete. Repository health and formatting checks passed,
all 113 unit tests passed, and `git diff --check` reported no errors. The
finished documentation change is ready for its requested commit.
