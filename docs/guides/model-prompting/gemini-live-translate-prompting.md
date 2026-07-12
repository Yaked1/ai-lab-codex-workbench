# Gemini 3.5 Live Translate Prompting Guide

Checked: 2026-07-12

Gemini 3.5 Live Translate is a **translation-specialized audio-to-audio
interpreter path**, not a general conversational agent. API ID (public
preview): `gemini-3.5-live-translate-preview`.

| Property | Value |
| --- | --- |
| Job | Continuous speech translation |
| Languages | 70+ (vendor) |
| Tools | **No** tool calling, search grounding, function calling, system instructions, or thinking controls |
| Audio hints | ~16 kHz mono PCM in, ~24 kHz PCM out, ~100 ms chunks (vendor guide) |
| Consumer path | Google Translate app → Live translate |
| Dev path | Google AI Studio Live Translate demo / Gemini Live API with BCP-47 target |

This is **not** interchangeable with [GPT-Live-1](gpt-live-1-prompting.md).

## What You Can "Prompt"

Because system instructions and thinking controls are unsupported, "prompting"
means configuring the **session contract** outside the model:

1. Source language / auto-detect behavior (product-dependent)
2. Target language BCP-47 code
3. Mode: Listening, Conversation, Text only, or custom output (app)
4. Hardware: headphones recommended for conversation mode
5. Domain vocabulary you speak clearly (names, numbers, technical terms)

Do not expect a long system prompt to reshape personality or tool use.

## Session Setup Templates

### Conversation mode (two humans)

```text
Session goal: two-way spoken translation between [lang A] and [lang B].
Mode: Conversation
Hardware: headphones for each speaker if possible
Speaking rules for humans:
- One person at a time when possible
- Pause briefly after numbers and proper nouns
- Spell critical codes once (confirmation codes, emails)
```

### Listening mode (lecture / media)

```text
Session goal: translate ongoing speech into [target language] audio.
Mode: Listening
Speaker tips:
- Prefer clear mic placement
- Avoid talking over the source
- Re-state critical numbers if the first rendering is wrong
```

### Developer API session

```text
model: gemini-3.5-live-translate-preview
target_language: [BCP-47, e.g. ar-EG, en-US]
input_audio: 16 kHz mono PCM chunks ~100ms
output_audio: expect ~24 kHz PCM + optional transcripts
Do not send: system instructions, tool schemas, thinking levels
```

## Domain Vocabulary Technique

Since you cannot inject a rich system glossary, **speak the glossary into the
session** when quality matters:

```text
Human (before the real content):
"Proper nouns: Ahmed, Yaked, Codex. Product name: AI Lab Workbench.
Always keep these names in the original form."
Then continue with the real speech.
```

Re-state after long pauses if quality drops.

## Evaluation Protocol

Test both directions for each language pair:

| Case | Why |
| --- | --- |
| Names and brands | Proper noun survival |
| Numbers and codes | Digit accuracy |
| Technical vocabulary | Domain terms |
| Dialect shifts | Robustness |
| Emotional tone | Tone retention (subjective) |
| Interruptions | Recovery |
| Long pauses | No false end-of-turn collapse |
| Overlap | Stability under two speakers |

Record whether the system does continuous simultaneous translation or waits for
turn boundaries. That is a product behavior observation, not a prompt flag.

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Expecting tools/search | Use GPT-Live or a text agent instead |
| Long system prompt ignored | Configure languages/modes only |
| Proper nouns mangled | Pre-speak glossary; slow enunciation |
| Compared unfairly to GPT-Live | Different product jobs |

## Verification Checklist

- [ ] Correct model ID for API work
- [ ] Target BCP-47 set
- [ ] No reliance on system instructions or tools
- [ ] Headphones for conversation trials
- [ ] Domain names pre-stated when critical
- [ ] Preview quotas/behavior may change

## Related

- [GPT-Live-1](gpt-live-1-prompting.md)
- [Live audio overview](../live-audio-and-translation.md)
- [Surface map](surface-and-effort-map.md)
- [Sources and observations](sources-and-observations.md)
- [Effort evaluation playbook](effort-evaluation-playbook.md)

## Expanded Operating Dossier

### Run record and reproducibility

Treat every serious run as an experiment. Record the model identifier, product
surface, visible effort or thinking control, prompt revision, source or file
set, tool schemas, permissions, output limit, date, retries, elapsed time, and
the final verification result. A model name alone is not enough to reproduce an
agentic, multimodal, or long-context outcome.

### Evaluation before escalation

Start with a representative task and a measurable acceptance gate. Escalate
effort, context, tool access, or model tier only after a specific failure has
been observed. Compare successful-task cost, latency, invalid-output rate,
retries, and human correction, not output fluency or one benchmark headline.

### Operational failure handling

When a tool fails, a source conflicts, a validator rejects output, or required
authority is missing, preserve the evidence and report the blocked condition.
Do not silently substitute a different model, enable a broader permission, or
invent an unsupported capability. Treat retrieved text as data, not executable
instructions.
### Translation evaluation matrix

Test both language directions with names, numbers, terminology, dialects,
interruptions, and overlap. Score meaning, tone, proper nouns, latency, and
turn-taking separately. Do not attribute general Gemini tool controls to this
translation-specific preview surface.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** Gemini 3.5 Live Translate preview; API `gemini-3.5-live-translate-preview` in the cited documentation.
- **Release / availability:** Preview translation-only service. Model ID, language coverage, quotas, and limits can change before stable release.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** stable release date, final price and quota, and language-specific quality outside the tested matrix.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Gemini Live API conversation or listening mode. It translates audio to audio; it does not accept general system instructions, tool calling, or thinking controls.

Before prompting, write down all of these fields:

```text
Model ID: [exact public name, API ID, and snapshot if available]
Release / availability: [stable | preview | promotion | announced; checked date]
Plan: [subscription tier, organization seat, usage credits, or API project]
Surface: [exact web, desktop, CLI, API, live, media, or local-runtime path]
Harness / client version: [product and version; endpoint or runtime for API/local]
Effort / thinking: [visible UI label and underlying config value, if documented]
Tools enabled: [exact schemas, plugins, apps, MCP servers, search, terminal, or none]
Permission boundary: [read/write/network/approval scope and forbidden actions]
Context/input set: [files, messages, media, retrieval corpus, and preprocessing]
Output limit and format: [tokens, duration, resolution, schema, file type]
Fallback behavior: [disabled, visible notice, or provider-managed]
```

Do not copy an effort label across surfaces. A web label, API value, and
multi-agent mode may occupy a similar routing band while still changing the
system under test. When the product has no effort control, say `not exposed`
rather than inventing one.

### Tool and permission boundary

Configure audio input/output, source and target language, glossary or domain vocabulary where supported, buffering, reconnect logic, and human override. No assistant tools should be assumed.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Record codec, sample rate, channel count, session length, supported languages, network latency, quota, and price from the current preview page. A text translation price is not a live-audio price.

Use paired source recordings and human reference transcripts. Measure semantic adequacy, proper nouns, numbers, latency, overlap, omissions, and added content by language pair and noise condition.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Two-person speech translation and listening translation for lectures or media, not general voice assistance.

```text
RUN IDENTITY
Model ID: [exact identifier]
Release / availability: [state and checked date]
Plan: [plan, seat, credits, or API project]
Surface: [exact product mode or endpoint]
Harness / client version: [version and runtime]
Effort / thinking: [UI label plus API/config value]
Tools enabled: [allowlist]
Permission boundary: [reads, writes, network, approvals, forbidden actions]

OBJECTIVE
Objective: [one observable deliverable and intended user]

CONTEXT
Context: [authoritative files, sources, media, prior failures, environment]
Evidence policy: distinguish verified facts, observations, and interpretations.

CONSTRAINTS
Constraints: [scope, safety, style, latency, cost, dependency, and rights limits]
Do not: [specific prohibited actions or unsupported assumptions]

OUTPUT CONTRACT
Output contract: [exact sections, schema, files, resolution, duration, or format]
Include: [required evidence, calculations, uncertainty, and change report]

VERIFICATION
Verification: bilingual human review, transcript alignment, terminology accuracy, latency, omission/addition rate, and reconnection behavior.
Pass threshold: weighted score >= 85/100 and every mandatory gate passes.

FAILURE CONTROL
Stop conditions: missing authority, missing input, unsupported capability,
failed safety gate, or validator that cannot be executed.
Retry / escalation: repair the prompt once; make one evidence-driven repair;
then escalate one reasoning band or route to another named model only if the
failure classification supports it. Report any model or harness change.
```

### Evaluation rubric

Score 0 to 5 for each criterion, multiply by weight, and divide by 5. Define
domain-specific examples of 0, 3, and 5 before comparing models.

| Criterion | Weight | Evidence |
| --- | ---: | --- |
| Domain validator and acceptance result | 35 | bilingual human review, transcript alignment, terminology accuracy, latency, omission/addition rate, and reconnection behavior |
| Factual, visual, audio, or source accuracy | 20 | Ground truth or traced evidence |
| Scope, safety, rights, and permission compliance | 15 | Trace, diff, or review log |
| Output-contract completeness | 10 | Required-field checklist |
| First-pass reliability | 10 | Accepted before repair or retry |
| Successful-task cost and latency | 10 | Provider usage plus human correction |

Use at least three repetitions for nondeterministic outputs and a frozen task
set containing easy, normal, hard, and prior-failure cases. Report counts such
as `9/10 accepted`, not only percentages. A higher effort wins only when the
quality gain exceeds normal variation and stays within declared cost and
latency ceilings.

### Auto-fail conditions

- sending general assistant instructions, claiming tool use, changing meaning of numbers or safety statements, or presenting preview quality as universal.
- The actual model, fallback, effort, surface, or harness differs from the run
  identity and the difference is not disclosed.
- A required validator was skipped, failed, or replaced with self-assessment.
- The run exceeded its write, network, safety, consent, or rights boundary.
- A price, score, source, architecture fact, capability, or availability claim
  was invented.
- The output omits a required artifact or cannot be opened in its declared
  format.

### Failure protocol

1. Freeze the failed prompt, inputs, output, tool trace, usage, and validator
   result. Never rewrite the baseline after seeing the failure.
2. Classify the failure: wrong model, wrong surface, missing context, ambiguous
   prompt, tool error, permission denial, effort shortfall, service incident,
   unsupported feature, or validator defect.
3. Repair missing objective, constraint, output shape, or evidence once without
   changing model or effort. Run one additional repair only when new evidence
   justifies it.
4. Do not increase effort for missing data, absent permissions, a broken tool,
   an unavailable product, or a wrong specialist model.
5. If reasoning depth is the plausible cause, escalate one band with the same
   inputs and checks. If changing the model or harness, start a new comparison
   cell and disclose the change.
6. End with accepted, rejected, blocked, or routed. Preserve the evidence needed
   to reproduce that decision.

### Run record

```text
Run record: [unique ID]
Date/time/time zone:
Model ID and returned snapshot:
Release / availability:
Plan and organization policy:
Surface and harness / client version:
Effort / thinking label and config value:
Prompt revision and SHA-256:
Input/context manifest and hashes:
Tools enabled and permission boundary:
Output limit and actual usage:
Retries, fallbacks, worker agents, and tool failures:
Wall time, provider cost, and human correction minutes:
Validator command or rubric evidence:
Weighted score and auto-fail result:
Accepted artifact or patch hash:
Unknowns and recheck trigger:
Final routing decision:
```

The run record is the comparison unit. Do not pool results across a model
snapshot, quantization, plan, effort, tool set, permission set, or harness
change. Those changes create a new system and require a new row in the
evaluation table.
