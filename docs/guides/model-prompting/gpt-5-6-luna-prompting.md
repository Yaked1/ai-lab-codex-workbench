# GPT-5.6 Luna Prompting Guide

Checked: 2026-07-12

Luna is the **fastest and least expensive GPT-5.6 tier**. It wins on high-volume
extraction, classification, bounded edits, and subagent steps with a clear
correctness test. Raising Luna's effort does **not** turn it into Sol.

| Property | Value |
| --- | --- |
| Role | Fastest / cheapest GPT-5.6 tier |
| API ID | `gpt-5.6-luna` |
| Base API price (dated) | $1 / $6 per 1M input/output |
| Local Codex default | Medium |
| Ultra | **Not** in local Codex Luna menu |
| Independent note | Luna Max ~51 Intelligence, 75 Coding Agent Index (dated) |

## When to Choose Luna

Choose Luna when:

- volume and latency dominate;
- the output is schema-checked or unit-tested;
- you need many parallel subagents doing small jobs;
- the repository pattern is already known.

Do not choose Luna when:

- architecture is ambiguous;
- sources conflict and judgment is the product;
- a wrong answer is expensive and hard to catch automatically.

## Effort Menus by Surface

| Surface | Efforts | Notes |
| --- | --- | --- |
| Codex CLI 0.144.0+ | Low, Medium, High, Extra High, Max | 0.144.0 minimum; no local Luna Ultra |
| New ChatGPT Desktop App | **Light**, Medium, High, Extra High, Max | Dated observation; Light = Low; no Ultra |
| ChatGPT Work web | Through Max observed; Work Ultra depends on plan/product | Do not infer Luna Ultra from the local Codex menu |
| Standard Chat | Not selectable | Sol only |
| API | `none`–`max` | Measure latency vs accuracy |

## Effort Mode Playbooks

### Light / Low

**Best fit:** speed-sensitive classification, metadata extraction, repeated
small transforms, cheap subagent tasks.

```text
Model: GPT-5.6 Luna | Effort: Light/Low

Task type: classification | extraction | transform

Input:
"""
[content]
"""

Output schema (JSON only):
{
  "label": "enum:A|B|C",
  "confidence": 0.0,
  "evidence_span": "short quote"
}

Rules:
- If unsure, label "unknown" and confidence <= 0.4
- No prose outside JSON
- Do not invent fields
```

### Medium (fast daily driver)

**Best fit:** small feature in a known pattern, source-packet summary, test
updates when templates exist.

```text
Model: GPT-5.6 Luna | Effort: Medium

Goal:
Implement [small change] matching existing pattern in [example file].

Read:
- [example]
- [target]

Do:
- Mirror style and APIs from the example
- Update tests if present
- Run: [command]

Do not:
- Invent new abstractions
- Touch unrelated modules
```

### High

**Best fit:** several steps or tool use still under a tight output contract.

```text
Model: GPT-5.6 Luna | Effort: High

Goal:
[multi-step but bounded]

Steps:
1. ...
2. ...
3. ...

Edge cases:
- [case] -> [expected]
- [case] -> [expected]

Output contract:
[schema or file list]

Verify:
[command]
Stop after one repair loop if still failing; report raw errors.
```

### Extra High / xhigh

**Best fit:** more search or verification needed without paying Sol rates.

```text
Model: GPT-5.6 Luna | Effort: Extra High

Goal:
[task needing broader search]

Search budget:
- Max files to open: [N]
- Prefer grep/path hints: [patterns]

Still required:
- Tight final schema/diff
- No architecture redesign

If the problem needs design judgment, stop and recommend Terra/Sol.
```

### Max

**Best fit:** highest Luna single-agent effort for hard-but-cheap work.

```text
Model: GPT-5.6 Luna | Effort: Max

Goal:
[harder bounded task]

Provide:
- Evidence of inspection
- Minimal patch
- Full check output

Escalation rule:
If after Max the acceptance tests still fail for judgment reasons (not missing
data), escalate to Terra High+ or Sol with the same tests and failure log.
```

## Subagent Pattern

Luna shines as a worker under a stronger orchestrator (Sol/Terra Ultra, Claude
Ultracode, or your own multi-agent loop).

```text
Orchestrator assigns Luna worker:

Worker goal: extract all public endpoints from [file] into JSON list.
Worker must not edit files.
Worker returns only JSON array of {method, path, handler}.
Orchestrator validates schema then continues.
```

## Failure Modes

| Symptom | Repair |
| --- | --- |
| JSON with commentary | "JSON only" + schema validation retry |
| Confident wrong class | Require unknown bucket + evidence span |
| Silent scope creep | Cap files; forbid new abstractions |
| Max still fails design tasks | Escalate tier, keep tests |
| Using Luna Ultra in docs | Invalid; Luna has no Ultra in local catalog |

## Verification Checklist

- [ ] Output is machine-checkable
- [ ] Effort not Max by default
- [ ] Desktop Light = Low understood
- [ ] Escalation criteria written
- [ ] No Ultra assumed for Luna

## Related

- [Terra](gpt-5-6-terra-prompting.md)
- [Sol](gpt-5-6-sol-prompting.md)
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
### Luna-specific batch discipline

Use Luna with schemas, gold samples, deterministic validators, and explicit
null handling. Sample failures before scaling a batch. Do not launch parallel
workers against shared mutable files; use independent shards and a separate
integration reviewer instead.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** GPT-5.6 Luna; API `gpt-5.6-luna`.
- **Release / availability:** Current fast GPT-5.6 tier on the checked date; Work, Codex, and API availability is plan and rollout dependent.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** closed architecture; account-specific picker; the point where Luna retries cost more than a first-pass Terra run.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Desktop uses Light, Medium, High, Extra High, Max. CLI uses Low, Medium, High, Extra High, Max. The checked Luna catalog has no Ultra. API supports none through max.

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

Use bounded repository, search, file, or API tools supplied by the harness. Keep batches independent and validators deterministic; do not grant broad write access only to compensate for a fast model tier.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Dated API envelope: 1.05M context, 128K output, $1/$6 per million input/output tokens and $0.10 cached input.

Vendor results: Agents Last Exam 50.3, GDPval-AA v2 1591.8, management consulting 35.4, Big Finance 36, AA Intelligence 51.2. Near-Terra aggregate results do not erase the larger finance gap or local failure cases.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Extraction, classification, mechanical edits, fast drafts, subagent research slices, and high-volume jobs with deterministic checks.

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
Verification: schema validation, exact-match fixtures, scoped diff, retry rate, throughput, and human correction.
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
| Domain validator and acceptance result | 35 | schema validation, exact-match fixtures, scoped diff, retry rate, throughput, and human correction |
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

- claiming Luna Ultra, using it for an unbounded high-stakes change without review, or ignoring aggregate retry cost.
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
