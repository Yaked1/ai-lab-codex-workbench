# GPT Image 2 Prompting Guide

Checked: 2026-07-12

GPT Image 2 is OpenAI's **flagship image generation and editing model** with
text and image input, image output, flexible sizes, and high-fidelity reference
inputs. Product docs emphasize typography, prompt adherence, precise editing,
and reference consistency. Internal architecture claims (for example "fully
autoregressive reasoning-integrated image model") are **unconfirmed** in the
checked OpenAI docs; prompt for outputs, not for hidden mechanisms.

| Property | Value |
| --- | --- |
| Role | State-of-the-art OpenAI image gen + edit |
| Surfaces | Images API, ChatGPT image tools |
| Inputs | Text, images (references / edit bases) |
| Evaluate | Full-resolution outputs, not compressed social frames |

## Universal Image Prompt Kernel

```text
Subject: [what, how many, exact attributes]
Scene: [place, time, weather, background]
Composition: [camera, framing, focal length feel, aspect ratio]
Style: [medium, finish, color grade]
Lighting: [key, fill, contrast]
Text (if any): [exact string, font style, placement]
References: [what must stay consistent]
Constraints: [no logos, no real people, no watermarks, safety]
Edit ops (if editing): [keep X, change Y only]
Output: [size/aspect, count]
```

## Generation Templates

### Product / marketing

```text
Studio product photograph of [product description], three-quarter view,
seamless light-gray background, softbox key from upper left, gentle fill,
crisp materials, no brand logos unless supplied, no extra labels,
commercial catalog quality, aspect ratio [ratio].
```

### UI / diagram (typography-critical)

```text
Clean UI mockup of [screen purpose].
Layout:
- Header: "[exact title]"
- Primary button: "[exact label]"
- Three cards titled "[A]", "[B]", "[C]"
Style: modern minimal, high contrast text, consistent 8px spacing rhythm,
no lorem typos, no watermark, desktop 16:9.
Text must be sharp and correctly spelled.
```

### Character consistency with references

```text
Using the attached reference image(s) as identity lock:
Generate [scene] with the same character face, hair, outfit colors, and
body proportions. Do not invent a new character. Keep the logo on the
jacket identical. Environment may change to [new scene].
```

## Editing Templates

### Surgical edit

```text
Edit the attached image.
Keep: composition, camera angle, subject identity, lighting direction.
Change only: [single change].
Do not alter text that already exists unless listed.
Do not add new objects.
```

### Text repair

```text
In the attached image, replace the misspelled headline with exactly:
"[correct text]"
Match existing font weight, color, and alignment as closely as possible.
Leave all other pixels unchanged.
```

### Layout expansion

```text
Extend the canvas to [aspect] by continuing the background consistently.
Do not crop the subject. Do not introduce new focal objects.
```

## Prompting by Quality Goal

| Goal | Add to prompt |
| --- | --- |
| Typography | Exact strings, placement, "no typos", "sharp text" |
| Reference fidelity | "identity lock", list invariant attributes |
| Editing precision | Keep/change lists; forbid extras |
| Style control | Medium, lighting, materials; avoid living-artist imitation unless rights allow |
| Safety / commercial | No real brands, no real private people, no watermarks |

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Wrong text spelling | Quote exact string; reduce other instructions |
| Identity drift | Fewer scene changes; restate invariants; attach clearer refs |
| Over-creative edit | "Change only X"; negative constraints |
| Looks good in thumbnail, fails print | Inspect full resolution; check edges and small type |
| Architecture debates in prompts | Irrelevant; prompt for measurable visual outputs |

## Evaluation Rubric

Score each output 1-5 on:

1. Prompt adherence
2. Typography accuracy
3. Reference consistency
4. Edit precision (if editing)
5. Artifacts / edges
6. Commercial safety compliance

Use the same prompts and aspect ratios across providers when comparing to Nano
Banana, Seedream, or Muse Image.

## Verification Checklist

- [ ] Exact text strings quoted when typography matters
- [ ] Keep/change lists present for edits
- [ ] References have identity vs style roles
- [ ] Full-resolution QC completed
- [ ] Safety/commercial constraints present

## Related

- [Image prompting patterns](../../image-generation/prompting-patterns.md)
- [Nano Banana family](nano-banana-family-prompting.md)
- [Seedream 5.0 Pro](seedream-5-0-pro-prompting.md)
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
### Image generation versus editing

Evaluate generation and editing separately. For edits, inspect preservation of
unmentioned regions, localized change, reference consistency, and drift across
multiple revisions. Keep full-resolution source and output images; do not infer
undisclosed architecture from interface behavior.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** GPT Image 2 through the Images API or an OpenAI product surface that explicitly reports GPT Image 2.
- **Release / availability:** Current flagship image generation and editing path in the dated OpenAI model catalog.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** internal generator architecture; exact product-side model if the UI does not report it; current per-image rate until price-page check.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Images API, ChatGPT image tool, or a named product integration. Record whether the operation is generation, edit, variation, mask edit, or tool-mediated image creation.

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

Record reference images, masks, transparency, size, quality, format, compression, moderation path, and any search/code tool used to construct factual graphics. Do not infer hidden architecture from UI animation.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Use the model page for supported sizes, quality controls, per-image price, rate limits, input-image rules, and output formats. Retain original files and actual billed settings.

Use a fixed prompt and reference set. Score prompt adherence, composition, text accuracy, identity, edit locality, artifacts, and safety on original outputs, not thumbnails.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for High-quality generation, controlled editing, typography-aware graphics, reference-guided characters, product visuals, and iterative layout work.

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
Verification: original-resolution visual rubric, OCR for required text, pixel or mask locality for edits, reference fidelity, and rights/safety review.
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
| Domain validator and acceptance result | 35 | original-resolution visual rubric, OCR for required text, pixel or mask locality for edits, reference fidelity, and rights/safety review |
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

- claiming an undisclosed architecture, judging only a compressed preview, altering protected regions in a surgical edit, or failing required text exactly.
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
