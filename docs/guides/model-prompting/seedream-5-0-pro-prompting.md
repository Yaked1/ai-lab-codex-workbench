# Seedream 5.0 Pro Prompting Guide

Checked: 2026-07-12

Seedream 5.0 Pro appears on ByteDance's **Dreamina** surface as a professional
image generation and editing model. Public English technical documentation is
thinner than Google/OpenAI API pages. Treat claims about internal reasoning,
layers, or web search as **vendor claims** until a technical report is public.

| Property | Value |
| --- | --- |
| Role | Professional image gen + edit (Dreamina) |
| Strengths to test | Typography, layout, reference control, targeted editing, production control |
| Architecture | Undisclosed in this guide; do not assert diffusion vs AR |
| Eval rule | Full-resolution originals; compressed X/YouTube frames hide errors |

## When to Use Seedream 5.0 Pro

Use for:

- side-by-side creative production against GPT Image 2 and Nano Banana Pro;
- poster/layout work where Dreamina is already in your pipeline;
- reference-controlled edits when the product UI exposes them.

Always run the same brief across providers before declaring a winner.

## Prompt Kernel

```text
Subject: [detailed]
Purpose: [ad / packaging / concept art / UI]
Composition: [camera, grid, aspect]
Style: [photoreal / illustration / 3D]
Lighting / materials: [...]
Typography: exact strings + placement
References: role of each image (identity / style / layout)
Edit instructions: keep / change lists
Constraints: brands, people, watermarks, text language
Negative constraints: [what must not appear]
```

## Generation Templates

### Production layout

```text
Professional print-ready layout for [campaign], aspect [ratio].

Hero visual: [subject description]
Palette: [colors]
Typography:
- Headline exact: "..."
- Subhead exact: "..."
- CTA exact: "..."

Grid:
[top/mid/bottom percentage regions]

Style: high-end commercial photography + clean sans typography,
sharp text, ample margin, no watermark, no extra logos.
```

### Reference-controlled character

```text
Use reference image A for face and outfit identity.
Use reference image B only for color mood.
Scene: [new]
Keep face geometry and outfit details from A.
Do not copy background from either reference.
```

## Editing Templates

```text
Edit the uploaded image.
Keep: composition, subject identity, existing correct text.
Change: [single targeted change].
Preserve lighting direction.
No additional objects.
```

```text
Fix typography only:
Replace "[wrong]" with "[right]".
Match font weight and alignment.
Leave the rest of the image unchanged.
```

## Comparison Protocol vs Other Image Models

| Step | Action |
| --- | --- |
| 1 | Freeze 10 prompts (5 gen, 5 edit) |
| 2 | Same aspect ratios and reference packs |
| 3 | Score typography, adherence, consistency, artifacts |
| 4 | Inspect native resolution only |
| 5 | Record latency and any safety refusals |

Do not promote a "winner" from a single viral comparison video.

## Failure Modes

| Symptom | Repair |
| --- | --- |
| English docs over-trust | Stick to observable outputs |
| Text mush | Shorter strings; higher contrast layout; fewer competing elements |
| Reference ignore | Reduce to one identity reference; restate lock attributes |
| Overfitting to Dreamina UI jargon | Translate UI labels into keep/change language |

## Verification Checklist

- [ ] Exact text strings provided
- [ ] Reference roles labeled
- [ ] Keep/change edit discipline
- [ ] Full-res QC
- [ ] Vendor architecture claims avoided

## Related

- [GPT Image 2](gpt-image-2-prompting.md)
- [Nano Banana family](nano-banana-family-prompting.md)
- [Image patterns](../../image-generation/prompting-patterns.md)
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
### Full-resolution evidence rule

Review original outputs for typography, edge artifacts, reference drift, and
targeted-edit accuracy. Compressed previews are not proof of production quality.
Keep vendor claims, local observations, and independent evaluations separate,
and verify commercial terms and reference rights before publication.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** Seedream 5.0 Pro in Dreamina or another ByteDance surface that explicitly names the model; no API ID is established by this guide.
- **Release / availability:** Current professional image generation/editing product claim with limited English first-party technical disclosure.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** public API ID, internal architecture, exact current credit price, and English first-party benchmark detail.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Dreamina product UI or an explicitly documented ByteDance endpoint. Record region, plan or credits, operation type, visible quality setting, and output resolution.

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

Record reference images, masks, layout controls, aspect ratio, resolution, prompt revision, and edit history. Keep the full-resolution original before social compression.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Use live product terms for credits, resolution, batch size, input limits, rights, and availability. Do not infer an API identifier, architecture, parameter count, or benchmark from marketing output.

Compare at matched resolution and references against GPT Image 2 or Nano Banana. Score adherence, identity, typography, edit locality, artifacts, latency, and credits per accepted image.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Professional compositions, high-resolution generation, controlled reference work, layout production, and iterative edits in the Dreamina workflow.

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
Verification: full-resolution rubric, OCR, reference fidelity, edit locality, credit use, rights review, and export integrity.
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
| Domain validator and acceptance result | 35 | full-resolution rubric, OCR, reference fidelity, edit locality, credit use, rights review, and export integrity |
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

- inventing technical architecture, evaluating only a preview, omitting credit or rights checks, or changing protected edit regions.
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
