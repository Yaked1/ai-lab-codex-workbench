# GPT-5.6 Terra Prompting Guide

Checked: 2026-07-12

Terra is OpenAI's **balanced GPT-5.6 tier**: daily repository work, documents,
analysis, and tool-heavy tasks when Sol's price is not justified. Artificial
Analysis measured Terra Max at 55 Intelligence Index and 77 Coding Agent Index
in Codex (dated snapshot).

| Property | Value |
| --- | --- |
| Role | Balanced intelligence and cost |
| API ID | `gpt-5.6-terra` |
| Base API price (dated) | $2.50 / $15 per 1M input/output |
| Local Codex default effort | Medium |
| Ultra | Available in Codex / eligible Work (not Plus web Work Ultra) |
| Companions | [Sol](gpt-5-6-sol-prompting.md), [Luna](gpt-5-6-luna-prompting.md), [Surface map](surface-and-effort-map.md) |

## When to Choose Terra

Choose Terra when:

- you do daily multi-file coding with clear acceptance criteria;
- cost matters more than the last few coding-index points;
- Free/Go Codex users receive Terra as their GPT-5.6 path;
- you want Ultra-style multi-area work at lower token rates than Sol.

Escalate to Sol when architecture, ambiguous science, or high-risk synthesis
keeps failing Terra Max with good prompts.

Demote to Luna when the work is high-volume extraction, classification, or
bounded subagent steps with a simple correctness test.

## Effort Menus by Surface

| Surface | Efforts | Notes |
| --- | --- | --- |
| Codex CLI 0.144.0+ | Low, Medium, High, Extra High, Max, Ultra | 0.144.0 minimum; local default Medium |
| New ChatGPT Desktop App | **Light**, Medium, High, Extra High, Max, Ultra | Dated observation; Light = Low |
| ChatGPT Work web Plus | Through Max observed | No Ultra in the supplied observation |
| ChatGPT Work web Pro/Enterprise | Through Max + Ultra | Official Ultra eligibility; exact lower labels can vary |
| ChatGPT Work web Business | Ultra observed on the user's workspace | Observation, not universal official eligibility |
| Standard Chat | Not selectable | Sol only in ordinary chat |
| API | `none`–`max` | No `ultra` reasoning value |

## Effort Mode Playbooks

### Light / Low

**Best fit:** deterministic repository edits, structured data cleanup, drafting
from a supplied outline.

```text
Model: GPT-5.6 Terra | Effort: Light/Low

Goal:
Apply the exact transformation: [describe].

Inputs:
- [file or table]
- Outline/schema: [paste or path]

Rules:
- Preserve fields not mentioned.
- No creative rewriting.
- Output only [format].

Check:
- [schema validate / unit test / diff stat]
If check fails, fix once then stop with error details.
```

### Medium (strongest cost-aware default)

**Best fit:** daily coding, test updates, document synthesis, tool use with
clear acceptance criteria.

```text
Model: GPT-5.6 Terra | Effort: Medium

Goal:
[Feature or doc outcome]

Read first:
- [convention files]
- [target modules]

Include: [paths]
Exclude: [paths]

Acceptance:
- [test command] passes
- Diff stays in scope
- Report: files, commands, risks

Do not:
- Expand style/refactors
- Touch lockfiles or CI unless asked
```

### High

**Best fit:** Medium found the area but did not close the issue; multi-file
debugging.

```text
Model: GPT-5.6 Terra | Effort: High

Problem:
[bug with repro steps]

Already known:
- Failing command: [cmd + output]
- Suspected files: [list]
- Medium attempt result: [summary]

Required:
1. Confirm root cause with evidence
2. Minimal fix
3. Regression test
4. Re-run failing command and adjacent suite

If root cause is outside suspected files, list callers before editing.
```

### Extra High / xhigh

**Best fit:** broad but bounded engineering: many callers, more hypotheses,
more verification surfaces.

```text
Model: GPT-5.6 Terra | Effort: Extra High

Goal:
[Bounded multi-surface engineering task]

Progress checkpoints:
After each major step, report: files inspected, hypotheses live, next action.

Guardrails:
- Max investigation time/steps: [N]
- No unrelated cleanup
- Prefer existing patterns in repo

Verification matrix:
| Surface | Command | Expected |
| --- | --- | --- |
| unit | ... | pass |
| integration | ... | pass |
| docs | link/check | pass |
```

### Max

**Best fit:** deepest Terra attempt when Sol price is hard to justify but the
task still needs maximum single-agent Terra compute.

```text
Model: GPT-5.6 Terra | Effort: Max

Goal:
[Hard task still inside Terra envelope]

Deliver:
1. Diagnosis with evidence
2. Implementation or decision
3. Full verification matrix results
4. Why Sol is not required (or why next step should escalate to Sol)

Cost discipline:
- Cache stable prompt prefixes when using API
- Avoid re-reading the whole monorepo; name entry points
```

### Ultra

**Interpretation:** parallel orchestration using Terra agents, not “Terra
beyond Max.” Attractive for multi-area work against stable contracts; parallel
duplication can erase Terra's price advantage.

```text
Model: GPT-5.6 Terra | Effort: Ultra

Project:
[outcome]

Streams (exclusive ownership):
A. Code: [paths]
B. Tests: [paths]
C. Docs: [paths]
D. Reviewer: read-only findings

Contracts:
- Shared types/API: [paths] — only stream A may change after freeze
- Integration test is truth

Synthesizer:
Merge without duplicate logic; run full suite once; report cost-relevant notes
(streams that thrash should be sequentialized next time).
```

## Recommended Routing Table

| Task class | Start | Escalate |
| --- | --- | --- |
| Format / rename / schema map | Light/Low | Medium |
| Feature with tests | Medium | High |
| Bug with partial repro | High | Extra High |
| Cross-module design in one service | Extra High | Max |
| Multi-package parallel work | Ultra | Sol Ultra if judgment fails |
| Ambiguous architecture | Sol High+ | Sol Max |

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Cheap but incomplete | Raise effort; add acceptance tests |
| Ultra thrash | Sequential High/Max with clearer ownership |
| Terra Max still wrong architecture | Move to Sol, keep the same prompt and tests |
| Over-prompted Low task | Shorten prompt; remove analysis requests |

## Verification Checklist

- [ ] Terra chosen for cost/capability fit
- [ ] Effort started at Medium unless task is trivial or known-hard
- [ ] Desktop Light treated as Low
- [ ] Ultra only for independent streams
- [ ] Escalation path to Sol documented if Max fails

## Related

- [Sol prompting](gpt-5-6-sol-prompting.md)
- [Luna prompting](gpt-5-6-luna-prompting.md)
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
### Terra-specific work shaping

Terra is strongest when the task is broad but bounded. Name paths, non-goals,
dependencies, acceptance tests, and stop conditions. Split deterministic work
into scripts and tests; reserve higher effort for a measured ambiguity or
cross-file dependency rather than routine formatting.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** GPT-5.6 Terra; API `gpt-5.6-terra`.
- **Release / availability:** Current balanced GPT-5.6 tier on the checked date; available in Work, Codex, and API rather than ordinary Chat selection.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** closed architecture; exact picker and Ultra eligibility on an uninspected account; workload-specific break-even against Sol or Luna.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Work/Desktop/Codex expose Light or Low, Medium, High, Extra High, Max, and Ultra where eligible. CLI uses Low rather than Light. API supports none, low, medium, high, xhigh, and max; ultra is orchestration.

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

Same configured Work/Codex/API tool families as Sol, but actual tool access comes from the harness, workspace policy, sandbox, and caller schema rather than the model name.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Dated API envelope: 1.05M context, 128K output, $2.50/$15 per million input/output tokens and $0.25 cached input.

Vendor results: Agents Last Exam 50.4, GDPval-AA v2 1593.0, management consulting 37.2, Big Finance 51, AA Intelligence 55.0. Terra is close to Sol on some suites, so successful-task cost is the routing metric.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Default repository work, iterative documents, broad analysis, and agent tasks that need more headroom than Luna without Sol's price.

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
Verification: tests, schema or artifact checks, diff scope, tool trace, successful-task cost, and human correction.
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
| Domain validator and acceptance result | 35 | tests, schema or artifact checks, diff scope, tool trace, successful-task cost, and human correction |
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

- presenting Terra as ordinary Chat selection, treating Ultra as API effort, or routing from average benchmark score without task-level evidence.
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
