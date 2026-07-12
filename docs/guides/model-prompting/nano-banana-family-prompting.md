# Nano Banana Family Prompting Guide

Checked: 2026-07-12

Google's consumer names map to Gemini image model IDs. **Nano Banana 2 is not
Gemini 3 Pro Image.** Nano Banana Pro **is** Gemini 3 Pro Image.

| Product name | Model ID | Role |
| --- | --- | --- |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | Fastest/cheapest; high-volume drafts |
| Nano Banana 2 | `gemini-3.1-flash-image` | General balance: quality, speed, 4K, editing |
| Nano Banana Pro | `gemini-3-pro-image` | Highest control, world knowledge, localization, professional use |
| Original Nano Banana (legacy) | `gemini-2.5-flash-image` | Google recommends replacing |

Thinking and search grounding (where documented) change latency, cost, and
outputs. Record them in every test log.

## Which Model to Pick

| Need | Model | Prompt emphasis |
| --- | --- | --- |
| Brainstorm 50 variants fast | 2 Lite | Short subject + style; few references |
| Default production stills / edits | Nano Banana 2 | Full kernel; up to 4K; moderate refs |
| Complex layouts, localization, max control | Nano Banana Pro | Exact text, layout grid, cultural/locale notes |
| Many sequential edit steps | 2 or Pro | Lite is not optimized for long edit chains |

## Shared Prompt Kernel

```text
Subject: ...
Purpose: ...
Composition / aspect: ...
Style / lighting: ...
Exact on-image text: "..."
Locale / language of text: ...
References: [how to use each attached image]
Constraints: no watermarks, no unlicensed brands, ...
Resolution target: [e.g. 1K/2K/4K if offered]
Thinking: on/off (if available)
Search grounding: on/off (if available) — only when current facts are required
```

## Nano Banana 2 Lite

**Vendor positioning:** iteration, brainstorming, high-volume; ~four-second
generation target in launch material. **Not optimized** for many reference
images or long sequential editing.

```text
Model: Nano Banana 2 Lite

Quick concept board for [product].
Style: [3 adjectives]
Background: simple
No fine print, no tiny UI text, no multi-panel complexity.
Generate a bold single-subject composition, aspect [ratio].
```

**Anti-pattern:** 6 reference images + 4 sequential edits + dense typography.

## Nano Banana 2 (Gemini 3.1 Flash Image)

**General-purpose path:** fast generation, search-grounded current knowledge
(when enabled), text rendering, subject consistency, editing, references, up
to 4K.

```text
Model: Nano Banana 2

Create a 4K marketing image of [subject].
Composition: [rule of thirds / centered / wide]
Lighting: [setup]
On-image text (exact): "[headline]"
Secondary text: "[sub]"
Keep subject consistent with reference image 1 (identity lock).
Use search grounding only if you need a current public landmark appearance;
otherwise rely on the prompt alone.
No logos other than the fictional mark described as [description].
```

### Editing with 2

```text
Edit image:
Keep: identity, pose, camera
Change: background to [new], color of [object] to [color]
Do not change face geometry or clothing logos.
```

## Nano Banana Pro (Gemini 3 Pro Image)

**Professional control path:** world knowledge, localization, typography,
complex layouts, production control. Compare to Banana 2 on the same brief.

```text
Model: Nano Banana Pro

Professional poster for [campaign] in [locale].
Language of all text: [language]
Headline (exact): "..."
Subhead (exact): "..."
Legal line (exact, small): "..."

Layout grid:
- Top 20%: headline
- Middle 55%: hero visual of [subject]
- Bottom 25%: subhead + CTA "[cta]" + legal

Visual requirements:
- High legibility at print and mobile crop
- Cultural appropriateness for [market]
- Color palette: [hex or named]
- No real celebrity likeness

References:
- Image A: product packshot (geometry lock)
- Image B: mood only (do not copy composition)
```

### Localization prompt pattern

```text
Same layout as the attached English master.
Replace text with the following [language] strings exactly:
Title: "..."
CTA: "..."
Keep visual hierarchy, spacing, and brand colors identical.
Do not translate logos that must remain in English: [list].
```

## Thinking and Search Controls

| Control | When to enable | Prompt note |
| --- | --- | --- |
| Thinking | Complex layouts, multi-constraint scenes | Still specify layout explicitly |
| Search grounding | Current public knowledge (events, places) | "Ground only for X; do not invent private data" |

Always log:

```text
model_id, thinking, search, resolution, reference_count, latency, notes
```

## Side-by-Side Eval Protocol

Use identical prompts, aspect ratios, references, and human rubric across Lite,
2, Pro, GPT Image 2, and Seedream:

1. Prompt adherence
2. Typography
3. Reference consistency
4. Layout complexity success
5. Latency / cost
6. Editability over 3 sequential revisions

## Failure Modes

| Symptom | Likely model mismatch | Repair |
| --- | --- | --- |
| Soft tiny text | Lite or weak prompt | Pro + exact strings + simpler layout |
| Reference collapse | Too many refs on Lite | Fewer refs; move to 2/Pro |
| Wrong locale text | Missing exact strings | Provide final copy, not "translate creatively" |
| Stale landmark | Search off | Enable grounding only for that element |
| Pro overkill cost | Simple hero shot | Banana 2 or Lite |

## Verification Checklist

- [ ] Correct model ID selected (Pro vs 2 vs Lite)
- [ ] Thinking/search settings logged when used
- [ ] Exact localized strings provided for text-heavy work
- [ ] Lite not used for long multi-reference edit chains
- [ ] Side-by-side eval uses full-resolution outputs

## Related

- [GPT Image 2](gpt-image-2-prompting.md)
- [Seedream 5.0 Pro](seedream-5-0-pro-prompting.md)
- [Image patterns](../../image-generation/prompting-patterns.md)
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
### Family comparison protocol

Compare Lite, general-purpose, and Pro paths using the same references, aspect
ratio, required text, grounding configuration, thinking setting, and review
rubric. Select by the output contract, not the family label. Record any enabled
search or thinking feature because it changes cost and latency.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** Nano Banana 2 Lite `gemini-3.1-flash-lite-image`, Nano Banana 2 `gemini-3.1-flash-image`, Nano Banana Pro `gemini-3-pro-image`; legacy original `gemini-2.5-flash-image`.
- **Release / availability:** Current family mapping in Google's dated image documentation; legacy original is not the recommended default.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** account picker and region rollout; current rates and option parity until API check; closed generator architecture.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Gemini API or a Gemini product picker that exposes the product name. Select the exact ID because Pro, 2, Lite, and legacy have different quality, speed, and cost envelopes.

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

Record references, masks, search grounding, thinking controls if documented, aspect ratio, resolution, output format, and edit history. Search grounding must cite current sources for factual graphics.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Use the per-model page for 4K support, image input limits, thinking/search behavior, rate limit, and price. Product names do not establish identical API options.

Run the same prompt/reference set across Pro, 2, and Lite. Score original outputs for adherence, text, identity, edit locality, factual grounding, latency, and successful-image cost.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Lite for drafts and volume, 2 for general balance and editing, Pro for highest control, localization, knowledge, and professional compositions.

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
Verification: original-image rubric, OCR, reference similarity, factual source check, edit locality, latency, and cost per accepted image.
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
| Domain validator and acceptance result | 35 | original-image rubric, OCR, reference similarity, factual source check, edit locality, latency, and cost per accepted image |
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

- calling Nano Banana 2 the same as Pro, using the legacy ID by accident, trusting generated text without OCR, or accepting unsupported factual imagery.
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
