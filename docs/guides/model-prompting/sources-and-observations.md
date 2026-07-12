# Sources and Interface Observations

Checked: 2026-07-12

This ledger explains which prompting-pack claims come from official vendor
documentation, the local Codex catalog, a dated interface observation,
independent evaluation, or interpretation. It prevents a picker seen on one
account from becoming a universal product claim.

## Evidence Order

| Rank | Evidence | Use |
| ---: | --- | --- |
| 1 | Official help, model, pricing, or launch page | Names, access, effort values, prices, architecture claims |
| 2 | Live local catalog or product picker | Dated state of that client/account only |
| 3 | Independent benchmark with configuration | Performance of the named model plus harness |
| 4 | User-provided observation | A real lead that must retain its observation label |
| 5 | Interpretation | Routing and prompting advice derived from the above |

When two tiers conflict, keep both and narrow the claim. Do not silently choose
the more convenient menu.

## OpenAI and GPT-5.6

Official sources:

- [GPT-5.6 launch](https://openai.com/index/gpt-5-6/)
- [GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001354)
- [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275)
- [OpenAI model catalog](https://developers.openai.com/api/docs/models)
- [`@openai/codex` npm package](https://www.npmjs.com/package/@openai/codex)

Confirmed on the checked date:

- Codex CLI `0.144.0` is the minimum version listed for GPT-5.6. The installed
  executable is `0.144.0`; npm lists `0.144.1` as the current stable release.
- The local `codex debug models` catalog lists Sol and Terra at `low`,
  `medium`, `high`, `xhigh`, `max`, and `ultra`; Luna stops at `max`.
- The official launch says Work Ultra is available to Pro and Enterprise, and
  Codex Ultra to Plus and higher plans.
- Ultra coordinates agents. It is not an API `reasoning.effort` value.

Dated observations supplied for this task:

| Surface observation | How this pack records it |
| --- | --- |
| ChatGPT Desktop uses Light where Codex uses Low | User-observed label; map Light to the Low compute band |
| Plus web Work has no Ultra | User-observed, consistent with official Pro/Enterprise statement |
| Business web Work shows Ultra | User-observed workspace state; official launch text does not establish universal Business eligibility |

Prompting consequence: select the visible label, but write the prompt for the
underlying task band. A Light prompt should be as bounded as a Codex Low prompt.

## Anthropic and Claude

Official sources:

- [Effort controls](https://platform.claude.com/docs/en/build-with-claude/effort)
- [Prompting Claude Opus 4.8](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)
- [Fable 5 promotional access](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access)

Confirmed:

- API efforts are `low`, `medium`, `high`, `xhigh`, and `max`; `high` is the
  API default.
- Ultracode is `xhigh` plus standing permission for Claude Code to launch
  multi-agent workflows.
- Fable uses adaptive thinking. Opus 4.8 uses adaptive thinking when enabled;
  an API request without a thinking field can run without thinking.
- Anthropic recommends Opus `xhigh` for coding/agentic work and at least `high`
  for other intelligence-sensitive work. Large `max_tokens` budgets are needed
  for `xhigh` and `max` agentic runs.
- Fable promotional access ends July 12, 2026 at 11:59:59 PM PT. Fable remains
  available through usage credits where allowed; API billing is separate.

Claude web `Extra` and exact Code/Desktop picker labels are recorded as dated
surface observations where the API page only documents `xhigh`.

## SpaceXAI and Grok

Official sources:

- [Grok 4.5](https://x.ai/news/grok-4-5)
- [Grok 4.5 developer documentation](https://docs.x.ai/developers/grok-4-5)
- [Grok Build CLI](https://x.ai/cli)

The pack treats Low, Medium, and High with High as the Grok Build default. Any
coding score remains attached to the Grok Build harness rather than presented
as a bare-model result.

## Meta Muse

Official sources:

- [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/)
- [Muse Image and Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)

Muse Image is available on Meta AI and selected Meta surfaces. Meta describes
search and coding tools, self-refinement, multi-reference composition,
integration with Muse Spark, and Content Seal watermarking. Muse Video is a
preview announced as coming soon; the pack does not provide a production
template until an available surface and limits are documented.

## Google Gemini

Official sources:

- [Gemini 3.5 Flash changes](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5)
- [Gemini Live Translate](https://ai.google.dev/gemini-api/docs/live-api/live-translate)
- [Gemini image generation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni)

Model IDs and capability limits come from these pages. Standard and Extended
are consumer labels; `minimal` through `high` are API controls. Deep Think is
not a Gemini 3.5 Flash effort.

## OpenAI Live and Image

Official sources:

- [Introducing GPT-Live](https://openai.com/index/introducing-gpt-live/)
- [GPT-Live help](https://help.openai.com/en/articles/20001274/)
- [GPT Image 2](https://developers.openai.com/api/docs/models/gpt-image-2)

The prompts use disclosed product behavior. GPT Image 2's internal generator
architecture remains undisclosed; a visible thinking animation does not prove
autoregressive image-token generation.

## ByteDance Seedream

- [Dreamina Seedream 5.0 Pro](https://dreamina.capcut.com/seedream/seedream-5-0-pro)

English first-party technical detail is limited. The guide focuses on observed
generation and editing controls, not an inferred architecture.

## Failure Handling

| Failure | Required response |
| --- | --- |
| Official page omits exact picker | Label the menu as observed; include date and surface |
| User observation conflicts with official plan text | Keep both; do not generalize the observation |
| Model is preview or coming soon | Do not build a production prompt or integration contract |
| Benchmark omits harness | Do not cite it as a coding-agent comparison |
| Architecture is undisclosed | Describe inputs, outputs, and controls only |

## Verification Checklist

- [ ] Current official page visited for every changing access or pricing claim
- [ ] Local catalog claim includes client version and checked date
- [ ] User observations say “observed” or “reported”
- [ ] Ultra, Ultracode, and API effort remain separate
- [ ] Preview and unavailable products are not presented as shipping defaults
- [ ] Benchmark model, effort, fallback, and harness stay together
