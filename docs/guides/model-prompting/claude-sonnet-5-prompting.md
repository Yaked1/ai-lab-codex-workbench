# Claude Sonnet 5 Prompting Guide

Checked: 2026-07-12

## What It Is and Where It Is Available

Claude Sonnet 5 is Anthropic's released Sonnet-class model. Anthropic's
2026-06-30 launch post lists Claude plans, Claude Code, and the Claude Platform;
the API identifier is `claude-sonnet-5`. Introductory API pricing is $2/$10 per
million input/output tokens through 2026-08-31, then $3/$15. Confirm the live
surface and price before a production purchase.

## Appropriate Tasks and Controls

Use it for normal knowledge work, scoped coding, tool-using workflows, and
cost-sensitive agent trials. The checked launch source describes variable effort
but does not establish a complete effort menu for every product surface. Do not
invent an effort value, tool permission, context limit, or computer-use feature:
read the current product or API documentation for the surface being used.

## Recommended Prompt Structure

```text
Goal: [observable deliverable]
Context: [sources, repository, or data]
Allowed tools: [names and boundaries]
Constraints: [cost cap, files to avoid, safety rules]
Verification: [test, source check, or acceptance rubric]
Stop: [missing authority, ambiguous requirement, or failed check]
```

For long context, supply a source map and ask the model to identify conflicts
before synthesis. For an agent, describe the actual tools, permissions, and
recovery rule instead of assuming browser or terminal access from the model name.

## Example Work Orders

```text
Task: Reconcile these three policy drafts into one decision memo.
Rules: Cite each factual claim to its supplied source; list conflicts; do not
invent policy. Verification: a reviewer can trace every recommendation.
```

```text
Task: Fix the failing test in [path]. Inspect before editing, change only files
needed for the regression, run [command], and report the exact result.
```

## Cost, Verification, and Failure Modes

Keep the context relevant, start with a small acceptance test, and measure total
cost including retries and tool calls. Do not use Sonnet 5 as evidence that it
replaces Claude Fable 5 or Opus 4.8; compare matched tasks. If tools are absent,
sources conflict, or a product control is not documented, stop and report that
boundary instead of simulating the capability.

## Unsupported or Inappropriate Uses

Do not claim a fixed context window, a universal effort menu, unrestricted web
search, computer control, or safe autonomous action without surface-specific
official documentation. Do not use an unsupported model control in API examples.

## Sources

- [Anthropic launch: Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)
- [Main research snapshot](../frontier-models-and-multimodal-systems-2026.md)
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
### Sonnet-specific surface boundary

The launch describes agentic tool use, but each client controls which tools are
actually present. Do not infer a fixed effort menu, browser permission, terminal,
or context limit from the model name. Check the selected Claude surface and
record the actual controls used in the run.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** Claude Sonnet 5; API `claude-sonnet-5` in the cited release material.
- **Release / availability:** Current agentic Claude tier in this dated pack. Introductory API pricing ends 2026-08-31, so price-sensitive routing must recheck after that date.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** closed architecture; unverified web effort menu and plan quota; post-introductory price changes after the stated schedule.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Use the API or the exact Claude product picker that names Sonnet 5. Do not infer Fable/Opus effort menus, Ultracode access, or plan quotas without a Sonnet-specific picker or help page.

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

Repository, terminal, web, and function tools come from Claude Code or the client. Record whether adaptive thinking and multi-agent permission are actually available.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Cited introductory API price is $2/$10 per million input/output tokens through 2026-08-31, then $3/$15. Recheck context, output, cache, and batch terms in the live model page.

Treat release scores as vendor evidence. Compare Sonnet with Terra, Opus, or Fable on the same harness, prompt, tool permissions, acceptance tests, and correction budget.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Cost-aware coding agents, repeated repository work, structured analysis, and production traffic that does not need the top Claude tier.

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
Verification: tests, tool success, source accuracy, first-pass rate, successful-task price, and correction time.
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
| Domain validator and acceptance result | 35 | tests, tool success, source accuracy, first-pass rate, successful-task price, and correction time |
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

- copying a Fable effort menu onto Sonnet, retaining expired introductory pricing, or omitting the active harness from a comparison.
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
