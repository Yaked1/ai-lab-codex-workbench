# Notes: Model and Effort Prompting Guide Pack

Checked: 2026-07-12

## Existing Work Preserved

Grok created an indexed pack under `docs/guides/model-prompting/` with 17
Markdown files and `tests/test_model_prompting_guides.py`. The pack already has
distinct guides for GPT-5.6 tiers, Claude models, Grok Build, Muse Spark,
Gemini Flash, live audio, and media generation. It also links from the root
README, guide index, and frontier essay.

## Initial Audit

- Sol receives the longest guide because it has six desktop/Codex choices,
  standard Chat, API, and Ultra orchestration.
- Terra and Luna are shorter but include distinct effort strategies and routing
  rules.
- Claude guides distinguish web `Extra`, Code `xhigh`, Max, and multi-agent
  modes.
- Image-family guides are grouped where shared prompt kernels prevent repeated
  text, while individual model sections retain different use cases.
- The test suite checks file existence, core prompt structure, major effort
  labels, Nano Banana mappings, Fable cutoff language, and navigation.

## Claims Requiring Current Verification

- Latest Codex CLI version and whether `0.144.0` is a minimum or only a local
  snapshot.
- ChatGPT Desktop `Light` versus Codex `Low` labels.
- Exact web Work Ultra eligibility for Plus, Pro, Business, and Enterprise.
- Claude web and Code effort menus, Ultracode wording, and Fable transition.
- Muse Image availability and Muse Video unavailability.

## Verified Findings

- OpenAI Help lists Codex CLI `0.144.0` and ChatGPT Desktop Codex
  `26.707.30751` as the minimum versions for GPT-5.6.
- The local executable reports `codex-cli 0.144.0`; its live catalog exposes
  Sol and Terra through `ultra`, and Luna through `max`.
- The npm package page lists `@openai/codex` `0.144.1` as the current stable
  release on the checked date. Alpha `0.145.0` builds are not treated as the
  stable recommendation.
- OpenAI's launch post says ChatGPT Work Ultra is available to Pro and
  Enterprise users, while Codex Ultra is available to Plus and higher plans.
  The user's Business Ultra report is retained only as dated interface evidence
  because the official plan statement does not enumerate Business there.
- OpenAI Help documents Work model availability but does not enumerate every
  lower effort label for every client. Desktop `Light` and exact web Work menus
  therefore remain observed interface labels.
- Anthropic documents API efforts `low`, `medium`, `high`, `xhigh`, and `max`;
  `high` is the default. Ultracode is `xhigh` plus standing multi-agent workflow
  permission, not another API effort.
- Historical snapshot: Anthropic confirmed Fable access requires Claude Code
  `2.1.170` or later. Its July 12, 2026 deadline is superseded by the
  [current promotion terms](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access),
  updated July 13, 2026, which extend included promotional access through July
  19, 2026 at 11:59:59 PM PT. The separate 50% Claude Code weekly-limit
  increase ends at the same time, after which Fable remains available using
  usage credits.
- Meta officially launched Muse Image on Meta AI and selected Meta product
  surfaces. Muse Video is an announced preview that is coming soon, not a
  currently available production path.

## Command Errors and Resolutions

- `codex` and `npm` PowerShell shims were blocked by local execution policy.
  The local version and model catalog were read through `codex.cmd` instead.
- `npm.cmd view` could not write to the user npm cache inside this sandbox.
  The current stable version was verified from the public npm package page.

## Source Policy

- Vendor documentation establishes model names, interfaces, efforts, prices,
  availability, and architecture claims.
- The local Codex catalog establishes only the checked local client state.
- Artificial Analysis establishes only its own dated benchmark results.
- User-provided menu observations are recorded as observations, not universal
  availability.
- Unverified products remain in the pack only with an explicit unavailable or
  unconfirmed label.
