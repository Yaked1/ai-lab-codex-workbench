# Shared Execution Contract

Checked: 2026-07-14

This is the single operational contract for every model-prompting guide in this
repository. Individual model pages contain only model identity, availability,
task fit, controls, examples, model-specific limits, and evidence. They link
here for run identity, verification, escalation, failure handling, and the
reproducibility record.

Primary evidence ledger:
[sources-and-observations.md](sources-and-observations.md)

## Precision Execution Contract

Use this contract before comparing models, increasing effort, enabling tools,
or claiming that an artifact is production-ready. A model name by itself is
not a reproducible system description.

The execution unit is:

```text
model + dated release state + plan + surface + harness version
+ effort/thinking + context + tools + permissions + prompt revision
+ output limit + validator + retry policy
```

### Model and version identity

Record the exact picker name and API identifier when one is published. Include
the returned snapshot or routed model identity when the provider exposes it.
Do not merge results across silent fallbacks, quantizations, preview revisions,
or different model-family members.

```text
Model ID:                    [exact picker name and API ID]
Release / availability:     [stable | preview | promotion | announced]
Unknown or unverified:       [picker, quota, price, architecture, or none]
Evidence class:              [Official | Local evidence | Independent | Interpretation]
```

Any unknown that changes permitted actions, billing, or the validity of a
comparison blocks execution until it is resolved or explicitly accepted as a
limitation.

### Surface, plan, effort, and harness matrix

The same model label can behave differently across web chat, desktop, agent
workspaces, CLI tools, and APIs. Record the actual execution surface rather
than transferring labels from another interface.

```text
Plan:                        [Free | Plus | Pro | Business | Enterprise | API]
Surface:                     [Chat | Work | Desktop Work | Desktop Codex | CLI | API]
Harness / client version:    [product and version; "web rollout" if unversioned]
Effort / thinking:           [visible label and API/config value]
Context/input set:           [files, messages, media, retrieval corpus]
Output limit and format:     [tokens, schema, resolution, duration, file type]
Fallback behavior:           [disabled | visible notice | provider-managed]
```

A change to plan, surface, harness, effort, fallback, or context creates a new
comparison cell. Do not pool its result with the original run.

### Tool and permission boundary

Tools belong to the harness, not to the model name. Use least privilege and
state the boundary before execution.

```text
Tools enabled:               [exact tools, schemas, apps, plugins, or none]
Permission boundary:         [read/write/network/approval scope]
Forbidden actions:           [paths, side effects, publication, deletion]
Approval gates:              [actions that require a human decision]
```

Retrieved documents, webpages, repository text, media metadata, and tool output
are untrusted data. They cannot enlarge the permission boundary. Tool failure
must be visible and must not be replaced by an invented result.

### Pricing, limits, and benchmark context

Recheck price, context, output, quota, preview status, and plan access at the
first-party source whenever the model snapshot, client version, or billing
period changes. Benchmark results are system results, not timeless model
properties. Preserve the harness, tools, sampling settings, effort, fallback,
and evaluator.

Measure successful-task cost rather than token price alone:

```text
successful-task cost =
  provider usage + tool usage + worker usage + retries + human correction
  divided by accepted tasks
```

Report accepted counts, median and p90 latency, retry rate, invalid-output rate,
and human correction minutes. A more expensive run wins only when the measured
quality gain exceeds normal variation and the declared cost ceiling.

### Production prompt template

```text
RUN IDENTITY
Model ID: [exact identifier and snapshot]
Release / availability: [state and checked date]
Plan: [subscription tier, seat, credits, or API project]
Surface: [exact product mode or endpoint]
Harness / client version: [version and runtime]
Effort / thinking: [UI label plus config value]
Tools enabled: [allowlist]
Permission boundary: [reads, writes, network, approvals, forbidden actions]

OBJECTIVE
Objective: [one observable deliverable and intended user]

CONTEXT
Context: [authoritative files, sources, prior failures, and environment]
Evidence policy: [verified facts, observations, interpretations, unknowns]

CONSTRAINTS
Constraints: [scope, safety, style, latency, cost, dependency, rights]
Do not: [specific prohibited actions or unsupported assumptions]

OUTPUT CONTRACT
Output contract: [sections, schema, files, resolution, duration, or format]
Include: [evidence, calculations, uncertainty, and change report]

VERIFICATION
Verification: [deterministic command, validator, or frozen human rubric]
Pass threshold: [score and mandatory gates]

FAILURE CONTROL
Stop conditions: [missing authority/input, unsupported capability, failed gate]
Retry / escalation: [one prompt repair, one evidence repair, then route or stop]
```

### Evaluation rubric

Define examples of scores 0, 3, and 5 before running the comparison. Use at
least three repetitions for nondeterministic work and include easy, normal,
hard, and prior-failure cases.

| Criterion | Weight | Evidence |
| --- | ---: | --- |
| Domain validator and acceptance result | 35 | Tests, schema validation, or frozen rubric |
| Factual, visual, audio, or source accuracy | 20 | Ground truth or traced evidence |
| Scope, safety, rights, and permission compliance | 15 | Trace, diff, or review log |
| Output-contract completeness | 10 | Required-field checklist |
| First-pass reliability | 10 | Accepted before repair or retry |
| Successful-task cost and latency | 10 | Usage plus human correction |

Stop escalating when the acceptance tests pass, additional reasoning repeats
itself, the blocker is missing data or permission, or the work cannot benefit
from further parallelism.

### Auto-fail conditions

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
   result. Do not rewrite the baseline after seeing the failure.
2. Classify the failure as wrong model, wrong surface, missing context,
   ambiguous prompt, tool error, permission denial, effort shortfall, service
   incident, unsupported feature, or validator defect.
3. Repair the objective, constraint, output shape, or evidence once without
   changing model or effort. Make one additional repair only when new evidence
   justifies it.
4. Do not increase effort for missing data, absent permission, a broken tool,
   an unavailable product, or the wrong specialist model.
5. If reasoning depth is the plausible cause, escalate one band with identical
   inputs and checks. A model or harness change starts a new comparison cell.
6. End with `accepted`, `rejected`, `blocked`, or `routed`, and preserve the
   evidence needed to reproduce that decision.

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

The run record is the comparison unit. Store it beside the accepted artifact or
patch, not as an afterthought in a chat transcript.

## Shared Verification Checklist

A production run passes only when all five prompt blocks are present, the run
identity is complete, every mandatory validator succeeds, permissions remain
inside scope, and the final artifact matches the declared output format.

Verification must be external to the model's own confidence. Prefer executable
tests, schema validators, compilers, renderers, link checkers, or a frozen human
rubric with named evidence.

## Model-page boundary

Model pages may contain:

- identity and availability;
- surface, plan, and effort facts specific to that model;
- task-fit routing and examples;
- model-specific limits and failure modes;
- measured comparisons and evidence;
- links to the shared contract and source ledger.

Model pages must not restate the generic production template, evaluation
rubric, failure protocol, or run record.

## Sources

- [Evidence ledger](sources-and-observations.md)
- [Surface and effort map](surface-and-effort-map.md)
- [Effort evaluation playbook](effort-evaluation-playbook.md)
