# GLM-5.2 Prompting Guide

Checked: 2026-07-12

## What It Is and Where It Is Available

Z.ai introduced GLM-5.2 on 2026-06-16 as an open-source, MIT-licensed
long-horizon model with published weights and a 1M-token context claim. The
reviewed first-party source identifies `GLM-5.2` for Coding Plan and describes
Z.ai and ZCode access. It documents High and Max thinking choices on its coding
surfaces; it does not establish a current API price or maximum-output limit.

## Appropriate Tasks and Effort

Use GLM-5.2 for long-horizon coding and analysis only when the task has a real
state record, a limited tool boundary, and repeated verification. Use High for
ordinary difficult work and reserve Max for measured headroom. Do not infer a
web-search, system-instruction, or computer-control capability from a coding UI.

## Recommended Prompt Structure

```text
Goal: [end state, not a vague exploration]
Context map: [files, source roles, known failures]
Allowed actions: [tools, paths, budget]
Milestones: [observable checkpoints]
Verification: [tests, diff review, source ledger]
Failure behavior: preserve state and report the blocked milestone
```

## Example Work Order

```text
Repair the failing integration in [paths]. First produce a dependency map, then
make the smallest change, run [tests], and report each milestone and any failed
assumption. Stop before network, deployment, or destructive actions.
```

## Context, Verification, and Cost

Long context needs a navigable source map and checkpoints. Measure success,
correction burden, latency, tokens, effort, and tool configuration, not a vendor
benchmark in isolation. Check current product limits and pricing before use.

## Failure Modes and Unsupported Uses

Do not treat the 1M context claim as proof of useful recall. Do not cite Z.ai
benchmark charts as independent results or assume a public weight automatically
makes every deployment safe, cheap, or compatible with an agent harness.

## Sources

- [Z.ai: GLM-5.2](https://z.ai/blog/glm-5.2)
- [ZCode Agent documentation](https://zcode.z.ai/en/docs/agents)
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
### Long-horizon state discipline

Use a source map, milestones, and compact evidence-linked state instead of
replaying raw transcripts. A 1M-token context is capacity, not a guarantee of
useful retrieval. Treat vendor benchmark results as vendor claims and report
High/Max comparisons with the same task, tools, and completion definition.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** GLM-5.2; use the exact Coding Plan, API, or checkpoint identifier shown by the selected Zhipu surface.
- **Release / availability:** Current first-party-described coding and open-model path in this dated pack. Host, checkpoint, and plan access are separate claims.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** plan-specific current price and quota unless checked; any topology field absent from the model config; production reliability of a third-party quantization.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Coding Plan, first-party API, or a named self-hosted runtime. Record High/Max labels only on surfaces that expose them. A quantized local runtime is a different harness from the hosted plan.

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

Coding harness tools and permissions must be enumerated. For self-hosting, record runtime, quantization, tensor parallelism, context configuration, tool parser, and chat template.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Use first-party configuration for parameters, layers, expert topology, attention, context, checkpoint precision, and recommended runtime. Record memory and throughput on the actual hardware; do not convert theoretical size into measured VRAM.

Attach coding scores to the named GLM checkpoint, effort, tool harness, and evaluator. For local quantization, run a separate quality and throughput comparison because quantization changes the system under test.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Long-horizon coding, agent loops, open-model experiments, and deployments that need control over weights or serving.

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
Verification: repository tests, long-run state retention, tool parsing, peak memory, tokens per second, and quantized-versus-reference quality.
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
| Domain validator and acceptance result | 35 | repository tests, long-run state retention, tool parsing, peak memory, tokens per second, and quantized-versus-reference quality |
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

- treating hosted and self-hosted results as identical, omitting quantization/runtime, inferring VRAM from parameter count alone, or reporting tests not run.
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
