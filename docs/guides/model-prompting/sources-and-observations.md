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
- Anthropic's Fable promotional-access terms state that the promotion ends July
  19, 2026 at 11:59:59 PM PT. The linked Claude Code weekly-limits promotion
  states that its 50% increase also extends through that date. This is a dated
  promotional condition and should be rechecked before billing decisions.

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

## Expanded-Dossier Source Rules

The expanded prompting pages must not add a product fact unless the linked
primary source establishes that exact fact. When a guide gives operational
advice, it should say whether that advice is an interpretation of documented
controls or a local evaluation procedure. A model card, launch chart, or product
demo can establish a vendor claim; it does not establish an independent result.

For every serious comparison, retain a small evidence packet: source URL and
date, model identifier, product surface, effort/thinking configuration, context
and tool setup, prompt version, observed outputs, validation result, cost/latency
measurement, and human correction. Keep preview and announced systems separate
from stable production surfaces. If two official sources conflict, record both
and choose neither without a newer authoritative resolution.

## Claim-Level GPT-5.6 Ledger

| Claim | Evidence class | Scope | Checked | Recheck trigger |
| --- | --- | --- | --- | --- |
| Codex CLI minimum for GPT-5.6 is 0.144.0 | Official | Codex CLI access | 2026-07-12 | Help page or CLI release changes |
| Installed CLI is 0.144.0 | Local evidence | This Windows machine | 2026-07-12 | Local package update |
| Stable npm is 0.144.1; alpha is 0.145.0-alpha.4 | Package registry | Public npm tags | 2026-07-12 | Version-sensitive instruction |
| Sol/Terra local menu includes Low through Ultra; Luna stops at Max | Local evidence | Installed catalog and account | 2026-07-12 | Client, login, or catalog update |
| Plus Chat offers Sol Medium and High | Official | ChatGPT Chat | 2026-07-12 | Plan or picker update |
| Pro/Business/Enterprise Chat add Extra High and Sol Pro | Official | ChatGPT Chat | 2026-07-12 | Plan or picker update |
| Work Ultra is documented for Pro and Enterprise | Official | ChatGPT Work | 2026-07-12 | Help or launch page update |
| Business Work Ultra was visible | User observation | One workspace only | 2026-07-12 | Workspace policy or rollout update |
| API uses `none` through `max`, not `ultra` | Official | Responses API controls | 2026-07-12 | Model page or API schema update |
| Sol/Terra/Luna API context is 1.05M with 128K output | Official | Dated model catalog | 2026-07-12 | Model snapshot or catalog update |
| Sol/Terra/Luna list prices are $5/$30, $2.50/$15, $1/$6 | Official | Standard API million-token rates | 2026-07-12 | Pricing page update |

### Required evidence packet for any model claim

```text
Claim:
Exact model or product identifier:
Source URL and page title:
Publisher:
Publication/update date if shown:
Date checked:
Evidence class:
Surface and plan scope:
Harness and version scope:
Directly supported wording or data:
Inference, if any:
Conflict or uncertainty:
Recheck trigger:
```

Architecture, price, context, effort, plan access, benchmark, and availability
are separate claims. A model page that supports one does not automatically
support the others. A vendor score remains a vendor result until an independent
evaluator reproduces the named model, effort, tools, and harness.

### Source failure protocol

1. Preserve the URL, checked date, and failure response.
2. Look for a second first-party page from the same vendor.
3. If only cached, user-provided, or local evidence remains, narrow the claim
   and label the evidence.
4. Do not copy a price, score, ID, architecture field, or plan boundary from an
   unattributed summary.
5. Mark the field `unknown or unverified` when the exact claim cannot be
   established.
6. Recheck by trigger rather than silently retaining a stale value.
