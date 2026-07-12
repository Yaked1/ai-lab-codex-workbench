# DeepSeek V4 Prompting Guide

Checked: 2026-07-12

## What It Is and Where It Is Available

DeepSeek labels DeepSeek-V4-Pro and DeepSeek-V4-Flash as Preview. The official
API identifiers are `deepseek-v4-pro` and `deepseek-v4-flash`; the API supports
OpenAI-compatible and Anthropic-compatible endpoints. Both have documented
thinking/non-thinking modes, JSON output, and tool calls. Use the live pricing
page before cost-sensitive deployment.

## Task Selection and Controls

Use Pro for difficult, cost-justified reasoning and Flash for high-volume,
bounded tasks. Treat a thinking-mode toggle, structured output, and tool calls
as separate configuration choices. The model name does not grant a repository
agent, browser, or an integration's own tool permissions.

## Recommended Prompt Structure

```text
Model: [deepseek-v4-pro | deepseek-v4-flash]
Mode: [thinking | non-thinking]
Goal: [single measurable result]
Inputs: [bounded data or files]
Tool schema: [allowed calls and expected JSON]
Verification: [validator, test, or human rubric]
Failure: return an explicit blocked status, never guessed fields
```

## Example Work Orders

```text
Extract the invoice fields into the supplied JSON schema. Use no external tools.
Reject uncertain values as null and validate the JSON against [schema].
```

```text
Inspect [repository area], propose the smallest repair, apply only after naming
the regression test, run [command], and report changed paths plus output.
```

## Context, Cost, and Verification

The official table lists a 1M context and 384K maximum output, but long context
is not a retrieval guarantee. Index inputs, delimit sources, and test recall on
representative documents. Record model, thinking mode, tool setup, retries,
tokens, latency, and fallback behavior when evaluating Pro against Flash.

## Failure Modes and Unsupported Uses

Do not present Preview as stable. Do not infer license terms from weight
availability, convert vendor benchmark results into independent evidence, or
assume an Anthropic-compatible endpoint supplies Claude product behavior.

## Sources

- [DeepSeek V4 preview release](https://api-docs.deepseek.com/news/news260424/)
- [DeepSeek models and pricing](https://api-docs.deepseek.com/quick_start/pricing/)
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
### Preview mode-control protocol

Hold thinking mode constant when comparing Pro and Flash. FIM is documented as
non-thinking only, so it is a different workload from reasoning chat. Record
cache condition, concurrency behavior, API format, tool schema, and retry
policy; Preview access is not stable-release evidence.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** DeepSeek V4 Pro `deepseek-v4-pro` and DeepSeek V4 Flash `deepseek-v4-flash`.
- **Release / availability:** Preview/current API paths described in the cited sources. Treat model behavior, quotas, and identifiers as preview-sensitive.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** stable release date, unchanged preview identifiers, exact current prices unless live-checked, and any undisclosed architecture field.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

DeepSeek API or an explicitly named host. Pro and Flash are separate model selections. Any thinking control must be taken from the selected endpoint schema rather than copied from GPT or Claude labels.

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

The application owns function schemas, retrieval, repository tools, and permissions. Open-weight or hosted status must be recorded separately; API availability does not prove downloadable weights.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Use the live provider page for context, output, cache, and price. Record both prompt and completion usage, retries, and any preview rate limit. Do not infer topology or quantization from the product name.

Keep published V4-Pro and V4-Flash results separate and retain sampling, tools, and evaluator. Test coding with repository harness checks and structured tasks with schema validity.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Cost-aware coding, structured generation, tool calling, and preview evaluation where the team accepts possible API changes.

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
Verification: schema validity, deterministic tests, tool-call correctness, preview stability, latency, and successful-task cost.
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
| Domain validator and acceptance result | 35 | schema validity, deterministic tests, tool-call correctness, preview stability, latency, and successful-task cost |
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

- merging Pro and Flash results, presenting preview behavior as stable, claiming open weights from API access, or inventing an effort mapping.
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
