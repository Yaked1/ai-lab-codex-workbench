# Current Plan: Precision Model Prompting Guide Expansion

## Goal

Expand every guide in `docs/guides/model-prompting/` into a precise operating
manual. A reader must be able to identify the exact model, release state,
subscription plan, product surface, client or API harness, effort or thinking
mode, tool set, permission boundary, prompt contract, validation method, and
failure path before running a task.

The guide pack must separate three kinds of statements:

1. current vendor-documented product facts;
2. dated local or account observations;
3. recommendations that require evaluation on the reader's workload.

![GPT-5.6 effort controls by product surface](../assets/model-guides/gpt-5-6-effort-surfaces.svg)

[![Watch a hands-on test of GPT-5.6 Sol, Terra, and Luna](https://i.ytimg.com/vi/xDXX2M5DrO0/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-5-6-family-test)

*Third-party workflow context. Official documentation remains the authority
for model access, effort menus, versions, and prices.*

## Scope

- All GPT-5.6 Sol, Terra, and Luna guides.
- All Claude Fable, Opus, and Sonnet guides.
- Grok, Gemini, Muse, DeepSeek, GLM, Mistral, live-audio, image, video,
  translation, open-model, media, and robotics guides.
- The pack index, surface and effort map, evidence ledger, and effort
  evaluation playbook.
- Regression tests that prevent future guides from collapsing into short
  product summaries.

## Per-Guide Acceptance Contract

Every model or system guide must include:

- exact public model name and API model identifier when one is documented;
- dated release, preview, promotional, or availability state;
- plan and organization-policy boundary for consumer products;
- exact surface and harness, including client version when it changes access;
- visible effort label and underlying API value, without treating them as
  interchangeable when the product does not;
- tool availability, required setup, permission boundary, and forbidden
  actions;
- context, output, latency, quota, pricing, or billing facts when published;
- architecture and benchmark context only when supported, with vendor and
  independent results clearly separated;
- model-specific task fit, weak fits, and routing thresholds;
- a production prompt containing objective, context, constraints, output
  contract, verification, stop conditions, and retry or escalation rules;
- a weighted evaluation rubric, auto-fail conditions, failure protocol, and
  reproducible run record;
- explicit unknowns for undisclosed architecture, unverified pickers, absent
  prices, unavailable products, and plan-dependent rollouts.

## Shared-Guide Acceptance Contract

- The index routes by task, model, surface, and evidence need.
- The surface map records ChatGPT Chat, Work web, Desktop Work, Desktop Codex,
  Codex CLI, API, Claude, Grok, Gemini, live, image, video, and specialist
  surfaces without merging their controls.
- GPT-5.6 Sol coverage records the checked Codex CLI version, current stable and
  alpha package versions, Chat plan matrix, Work and Codex effort menus,
  Desktop Light versus CLI Low wording, API effort values, and Ultra versus Sol
  Pro semantics.
- The evidence ledger maps volatile claims to a source, evidence tier, checked
  date, scope, and recheck trigger.
- The evaluation playbook defines frozen prompts, repeated trials, weighted
  rubrics, confidence reporting, successful-task cost, orchestration cost, and
  promotion or rollback rules.

## Verification Gates

- [x] Every indexed file exists and ends with a newline.
- [x] Every model guide contains the precision contract headings and fields.
- [x] Every model guide is at least 1,000 words, while grouped or flagship
  guides may be longer when their surface count requires it.
- [x] Model-specific boundaries remain intact, including Luna without Ultra,
  Sol Pro as a separate model path, Fable's dated promotion, Muse Video as
  unavailable, and translation-only limitations.
- [x] Source links and volatile claims pass the repository's documentation
  checks.
- [x] Unit tests, repository health check, safe autofix check, and diff check
  pass.
- [x] The final diff is reviewed, committed, and pushed to the established
  remote without force.

## Phases

- [x] Audit all guide files, existing tests, surface tables, and source rules.
- [x] Verify the current GPT-5.6 Sol product, API, CLI, plan, and effort facts.
- [x] Add shared precision standards and claim-level evidence rules.
- [x] Expand every model and system guide with its exact operating contract.
- [x] Add structural and content regression tests.
- [x] Run all repository checks and review the final diff.
- [x] Commit and push the accepted change set.

## Decisions

- Use exact dated facts where first-party sources or the local catalog support
  them. Do not infer an effort menu from another surface.
- Treat model, effort, harness, tools, and permissions as one run identity.
- Treat Ultra and Ultracode as orchestration modes, not API reasoning values.
- Treat Sol Pro as a separate highest-quality Chat path, not a renamed effort.
- Keep vendor benchmark charts labeled as vendor results and require local
  workload evaluation before routing decisions.
- Never invent architecture, pricing, plan access, or availability for systems
  whose owners have not published it.

## Current Evidence Snapshot

- Installed Codex CLI: `0.144.0`.
- Current npm stable checked on 2026-07-12: `0.144.1`.
- Current npm alpha checked on 2026-07-12: `0.145.0-alpha.4`.
- Local Codex catalog: Sol and Terra expose Low through Ultra; Luna exposes Low
  through Max and no Ultra.
- Official ChatGPT help: Plus Chat exposes Sol Medium and High; Pro, Business,
  and Enterprise expose Medium, High, Extra High, and the separate Sol Pro
  path.
- Official launch: Work Ultra is documented for Pro and Enterprise; Codex Ultra
  for Plus and higher. A Business Work Ultra picker remains a dated workspace
  observation, not a universal plan promise.

## Status

The guide expansion, regression gates, final review, commit, and push are
complete.
