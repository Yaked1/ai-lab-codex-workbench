# Gemini Omni Flash Prompting Guide

Checked: 2026-07-12

Gemini Omni Flash is a **multimodal generative-video system**, not an image
model comparison target. Preview API ID: `gemini-omni-flash-preview`. It can
combine text, images, existing video, and prompt-described audio to produce
video with generated audio. Conversational editing via the Interactions API is
documented for iterative changes that should preserve unmentioned parts.

| Property | Value |
| --- | --- |
| Model ID | `gemini-omni-flash-preview` |
| Output (model page, dated) | ~3–10s, 720p, 24 fps |
| Context | Large token window (model page lists ~1,048,576) |
| Video input for editing | Up to ~10s (dated) |
| Planned image/text outputs | Vendor future; not current capability in this guide |
| Distribution | Gemini app, Flow, YouTube creation surfaces, paid API preview |

## Current Preview Limits (Do Not Invent Workarounds)

Documented limitations at check time include:

- uploaded audio references unsupported;
- multi-video reasoning unsupported;
- video extension / interpolation unsupported;
- voice editing unsupported;
- schema may accept short video references the model does not correctly process.

Treat these as hard product limits in prompts and pipelines.

## When to Use Omni Flash

Use when:

- you need short video with generated audio from text/image/video inputs;
- you will iterate conversationally while preserving unmentioned regions;
- character/voice consistency matters (test it; do not assume).

Do not use when:

- you need long-form film;
- you need multi-clip reasoning across many videos;
- you need precise voice replacement or audio reference upload;
- you need production audio mastering.

## Prompt Templates

### Text-to-video

```text
Model: gemini-omni-flash-preview

Create a [duration 3-10s] video at 720p 24fps.

Story beat:
0-2s: [opening visual]
2-5s: [action]
5-end: [payoff]

Visual style: [cinematic / product / motion graphic]
Camera: [static / slow push / orbit]
Subject: [identity details]
Environment: [place]
Lighting: [setup]

Audio (describe, do not attach unsupported reference files):
- Ambient: [soundscape]
- Optional SFX: [hits]
- Optional voice line (exact): "[script]"
  Voice character: [age/tone], language: [lang]

Constraints:
- No real celebrity likeness
- No unlicensed brand logos
- No on-screen tiny legal text
- Keep continuity of clothing and face
```

### Image-to-video

```text
Animate the attached image for [N] seconds.
Preserve: subject identity, colors, composition center.
Motion: [subtle parallax / walk cycle / product turntable]
Camera: [move]
Do not change the logo design.
Audio: light whoosh + soft ambient room tone, no lyrics.
```

### Video edit (conversational)

```text
Edit the attached clip.
Keep everything not mentioned.
Change only: [sky color / replace prop / adjust pacing feel]
Preserve character face and voice if present.
Do not extend duration beyond model limits.
```

### Character consistency across takes

```text
Same character as previous generation:
- Face: [traits]
- Outfit: [traits]
- Voice: [traits]
New scene: [description]
Maintain identity and voice timbre; only change location and action.
```

## Iteration Protocol

1. Generate a base clip with a tight beat sheet.
2. Change **one** variable per revision (motion, audio, or scene).
3. Explicitly list invariants: "keep X, Y, Z unchanged."
4. Reject multi-edit kitchen-sink prompts in preview.
5. Export and review audio sync and lip/voice consistency manually.

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Identity drift | Restate invariants; fewer scene changes |
| Prompt asks for 30s film | Split into multiple 3–10s shots externally |
| Audio reference upload | Describe audio in text; do not rely on unsupported uploads |
| Multi-video synthesis | Cut offline; Omni is not multi-video reasoner here |
| "Just like Nano Banana" | Wrong family; use image guides for stills |

## Verification Checklist

- [ ] Duration within 3–10s
- [ ] Resolution/fps expectations set
- [ ] Invariants listed for edits
- [ ] No dependency on unsupported audio refs
- [ ] Character/voice consistency tested across ≥2 edits
- [ ] Safety/commercial constraints present

## Related

- [Nano Banana family](nano-banana-family-prompting.md) for stills
- [Surface map](surface-and-effort-map.md)
- [Frontier essay](../frontier-models-and-multimodal-systems-2026.md)
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
### Temporal preview evaluation

Assess video as a sequence: motion, persistence, transitions, audio alignment,
edit continuity, and artifacts. Preserve every edit turn and original output.
Do not rely on planned or currently unsupported preview functions when defining
a production workflow.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** Gemini Omni Flash preview; API `gemini-omni-flash-preview`.
- **Release / availability:** Preview multimodal video generation and editing system. Treat all limits and IDs as changeable.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** stable release, final pricing and quotas, production SLA, and any hidden architecture or seed behavior not published.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Gemini API preview with text-to-video, image-to-video, conversational edit, or multimodal input. Record the exact operation because edit and generation have different evidence needs.

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

Record source video/image/audio files, time ranges, references, prompt revision, aspect ratio, duration, resolution, seed if exposed, and audio controls. Retain originals and generated masters.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Use the preview documentation for duration, resolution, accepted inputs, output format, rate limit, quota, safety, and price. Do not invent unsupported batching or production guarantees.

Evaluate prompt adherence, temporal continuity, character consistency, edit locality, motion artifacts, audio synchronization, latency, and retry count on original masters.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Preview experiments for generated video, image animation, conversational edits, and audio-video work where interface change is acceptable.

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
Verification: frame and timeline review, identity consistency, edit-boundary audit, audio sync, original-file inspection, and safety review.
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
| Domain validator and acceptance result | 35 | frame and timeline review, identity consistency, edit-boundary audit, audio sync, original-file inspection, and safety review |
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

- presenting preview as production-ready, accepting edits outside the requested time range, judging a compressed clip, or omitting source-media rights.
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
