# Current Mistral Models Prompting Guide

Checked: 2026-07-12

## What These Models Are and Where They Are Available

Mistral Medium 3.5 and Small 4 are generalist multimodal models. OCR 4 is a
document-intelligence service, Voxtral TTS generates speech, Leanstral 1.5 is a
Lean 4 proof-engineering Labs model, and Robostral Navigate is an announced
embodied-navigation system. Do not treat this as one interchangeable family.
Current official identifiers include `mistral-medium-3-5`,
`mistral-small-2603`, `mistral-ocr-4-0`, `voxtral-mini-tts-2603`, and
`labs-leanstral-1-5`. Robostral has no public identifier in the sources reviewed.

## Task Selection and Controls

| System | Use for | Verify with |
| --- | --- | --- |
| Medium 3.5 / Small 4 | Coding, structured work, agent tasks | Same repository, tools, tests, and correction budget |
| OCR 4 | Document extraction and layout | Field accuracy, tables, boxes, language coverage, human correction |
| Voxtral TTS | Narration and speech agents | Intelligibility, latency, pronunciation, consent and rights checks |
| Leanstral 1.5 | Lean 4 proof work | Compiled proofs and reproducible project tests |
| Robostral Navigate | Research planning only | Simulation, hardware validation, and safety review |

## Recommended Prompt Structures

```text
Generalist goal: [deliverable]
Context: [bounded sources or repository]
Tools: [explicit schemas and permission boundary]
Verification: [tests, schema, or review]
Failure: report uncertainty and preserve unrelated files
```

```text
OCR task: Extract [fields] from [document set]. Return [schema] with page,
bounding-box, and confidence fields where the API provides them. Flag unclear
values. Validate the result against [ground truth sample].
```

```text
Lean task: Prove [theorem] in [Lean project]. Use only listed imports. The proof
is complete only when [command] compiles it; report any unresolved goals.
```

```text
TTS task: Read the supplied original script in [language], at [pace] with
[pronunciation notes]. Do not imitate a real person without consent. Review
proper nouns and numbers from the generated audio.
```

## Context, Cost, and Failure Modes

Use Mistral's current pricing page for deployment costs. OCR pages, speech
characters, and token work have different units. A model card listing function
calling or agents does not grant an arbitrary application's tools. Keep personal
documents and voice samples within documented privacy and consent rules.

Robostral is not production guidance: its public announcement does not establish
API access, weights, hardware, pricing, or safety terms. Never translate
high-level navigation output directly into low-level robot control without a
separate safety-critical controller and physical validation.

## Unsupported or Inappropriate Uses

Do not rank OCR, TTS, Lean proofs, or robotics with general chat scores. Do not
claim unverified handwriting, watermarking, language, deployment, or physical
robot support. Do not use copyrighted lyrics as TTS examples.

## Sources

- [Mistral model overview](https://docs.mistral.ai/models/overview)
- [Mistral pricing](https://mistral.ai/pricing/api/)
- [Mistral latest news](https://mistral.ai/news/)
- [Evidence ledger](sources-and-observations.md)

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
### Specialist evaluation boundaries

OCR needs ground-truth extraction and correction metrics; TTS needs
intelligibility, latency, consent, and rights checks; Leanstral needs compiled
proofs; robotics needs simulation and supervised physical validation. Do not use
a general chat score as a substitute for one of these domain-specific gates.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** Family guide: `mistral-medium-3-5`, `mistral-small-2603`, `mistral-ocr-4-0`, `voxtral-mini-tts-2603`, `labs-leanstral-1-5`; Robostral has no public identifier in the reviewed sources.
- **Release / availability:** Mixed stable, dated, labs, and announced systems. Select one exact member before using this contract.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** Robostral public identifier and production access; any current field not present on the selected member's official page.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Mistral API, documented open-weight runtime, Lean toolchain, OCR endpoint, TTS endpoint, or supervised robotics environment. Never treat the family name as one harness.

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

Generalist function tools, OCR file ingestion, TTS voice controls, Lean compiler, and robotics actions have different schemas and permissions. Enable only the domain tools required for the selected member.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Look up per-model context, output, price, license, weight precision, and hardware guidance. Record audio duration, document page limits, or compiler/runtime version for specialists.

Use OCR error rate for OCR, intelligibility and latency for TTS, compiler acceptance for Lean, simulation and safety gates for robotics, and task success for generalists. Do not average them into one family score.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Choose the narrowest Mistral member matching general reasoning, smaller deployment, OCR, TTS, formal proof, or robotics.

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
Verification: member-specific ground truth: tests, OCR CER/WER, listening rubric, Lean compiler, or supervised simulation safety checks.
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
| Domain validator and acceptance result | 35 | member-specific ground truth: tests, OCR CER/WER, listening rubric, Lean compiler, or supervised simulation safety checks |
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

- using the wrong family member, grading a specialist with prose quality, presenting Robostral as a current public API, or skipping license and rights checks.
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
