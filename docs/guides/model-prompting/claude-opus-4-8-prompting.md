# Claude Opus 4.8 Prompting Guide

Checked: 2026-07-12

Opus 4.8 is a strong Claude model in its own right and the **documented
fallback** for specified Fable 5 safeguards. Use it as a stable Claude baseline
when you need to avoid Fable's model-routing layer or when Fable is not the
right cost/access choice after the official July 19, 2026 11:59:59 PM PT Fable
access extension ends; confirm current Anthropic terms before relying on the
date.

| Property | Value |
| --- | --- |
| Role | High-end Claude coding, analysis, professional artifacts |
| API efforts | `low`, `medium`, `high`, `xhigh`, `max` |
| Base API price (dated) | $5 / $25 per 1M input/output (half Fable's base rates) |
| Context | 1M with standard pricing rule (dated) |
| Independent note | Opus 4.8 Max ~55.7 Intelligence; 73 Coding Agent Index **in Claude Code** |
| Anthropic effort advice | `xhigh` coding/agentic start; `high` most demanding work; `max` only if evals show headroom |

## Effort Labels by Surface

The web `Extra` label below is a dated interface observation. Anthropic's API
documentation calls the value `xhigh`.

| Surface | Efforts | Notes |
| --- | --- | --- |
| Claude web chat | Low, Medium, High, Extra, Max | Same web set as Fable |
| Claude Code CLI 2.1.170+ | Low, Medium, High, Extra High, Max | Multi-agent / Ultracode-style workflows where product allows |
| Claude Desktop App with Code | Same as CLI | Same effort modes as Fable on Code surfaces |
| API | `low`–`max` | Configure explicitly; measure |

## When to Choose Opus vs Fable

| Prefer Opus 4.8 | Prefer Fable 5 |
| --- | --- |
| Cleaner model identity for evals | Stronger dated AA-Briefcase / broad index signals |
| Lower base API token price | Accept higher price for judgment-heavy long work |
| Avoid safeguard fallback ambiguity | Willing to log fallback notices |
| Solid Claude Code baseline | Ultracode multi-agent on Mythos-class stack |

Coding-agent numbers include harness behavior (system prompt, tools,
permissions). Do not treat Claude Code scores as bare API scores.

Opus 4.8 uses adaptive thinking when the API request enables it. Unlike Fable,
an Opus request without a thinking field can run without thinking. At `xhigh`
or `max`, Anthropic recommends a large output budget; its current prompting
guide suggests starting around 64K tokens and tuning from evaluation results.

## Effort Mode Playbooks

### Low

```text
Model: Claude Opus 4.8 | Effort: Low

Goal:
Make the smallest correct change to [file] for [behavior].

Constraints:
- No drive-by refactors
- Match existing style
- One check: [command]
```

### Medium

```text
Model: Claude Opus 4.8 | Effort: Medium

Goal:
[feature or analysis]

Context:
[files / brief]

Acceptance:
[tests or rubric]

Report format:
summary, changes, evidence, risks
```

### High

**Best fit:** most demanding non-coding-specialist work; solid default for docs,
finance-style analysis, and multi-step tasks.

```text
Model: Claude Opus 4.8 | Effort: High

Goal:
Produce [professional artifact] from [sources].

Quality bar:
- Citation accuracy over fluency
- Flag missing data
- Separate facts vs inferences
- Editable structure (headings, tables)

Verification:
[checklist: numbers trace, contradictions, actionability]
```

### Extra (web) / Extra High / xhigh

**Best fit:** coding and agentic starting point recommended by Anthropic.

```text
Model: Claude Opus 4.8 | Effort: Extra High / xhigh

You are a coding agent in [repo].

Read: AGENTS.md / CLAUDE.md, then [targets]

Task: [work order]
Scope fence: include [...]; exclude [...]

Method:
inspect -> implement -> test -> report

Mandatory checks:
[commands]

If tests fail, fix in scope only. If failures are unrelated, report and stop.
```

### Max

```text
Model: Claude Opus 4.8 | Effort: Max

Use only if a High/xhigh run failed a measurable bar:
Previous attempt: [summary + failing evidence]
New attempt must improve: [metric]

Required:
full decision record, test matrix, residual risks
```

### Multi-agent / Ultracode-style (Code surfaces)

Same discipline as Fable Ultracode: exclusive ownership, frozen interfaces,
one synthesizer, one final test pass. Opus does not magically fix bad
contracts.

```text
Parallel agents on Opus 4.8 / xhigh:

A implementer [paths]
B tester [tests]
C reviewer read-only

Shared schema freeze: [file]
Final merge + suite: [commands]
```

## API Adaptive-Thinking Pattern

```text
model: claude-opus-4-8
thinking: adaptive
effort: xhigh
max_tokens: [large tested budget; start near 64K for long agentic work]

Task contract:
- Objective: [one result]
- Tools: [schemas and permissions]
- Scope: [include / exclude]
- Verification: [tests or evidence rubric]
- Stop conditions: [approval, missing data, unsafe action]
```

If low or medium is selected, keep the task narrow and explicit. Opus follows
those lower effort limits strictly and may not explore beyond the requested
scope. If Max overthinks, compare it against xhigh on the same frozen task set.

## Document and Spreadsheet Work

Judge model choice on:

- citation accuracy;
- spreadsheet/document operation correctness;
- analytical quality;
- correction cost;

not prose fluency alone.

```text
Goal:
Build [memo / model / table] for [decision].

Rules:
- Every number cites a cell, file, or URL
- No silent unit conversions
- List open questions
- Provide an executive recommendation last, not first
```

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Fluent but uncited | Force claim→source map |
| Overbuilt solution | Lower effort; add "smallest change" |
| Agent edits outside scope | Hard exclude list + stop condition |
| Confused with Fable scores | Keep harness and fallback labels |

## Verification Checklist

- [ ] Effort chosen per Anthropic coding guidance when coding
- [ ] Web Extra vs Code Extra High mapped correctly
- [ ] Eval harness named (API vs Claude Code)
- [ ] Scope fence + checks present
- [ ] Max reserved for proven headroom

## Related

- [Fable 5 prompting](claude-fable-5-prompting.md)
- [Fable vs Sol](../fable-vs-sol.md)
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
### Opus-specific baseline discipline

Use Opus when a cleaner Claude-family baseline is needed. Keep the harness,
tools, repository state, prompt, and review rule fixed when comparing it with
Fable or another product. A polished document is incomplete until its claims,
calculations, and cited sources are checked.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** Claude Opus 4.8; API family identifier must be copied from the current Anthropic catalog for the chosen snapshot.
- **Release / availability:** Current baseline Claude flagship path in this dated pack and the required comparison when Fable access or credits are unavailable.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** closed architecture; exact current snapshot alias until catalog lookup; plan-specific web picker and quotas.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Claude web dated labels are Low, Medium, High, Extra, Max. Claude Code/Desktop Code use Extra High for xhigh. API uses low, medium, high, xhigh, max. Multi-agent permission is a harness property.

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

Claude Code provides repository and terminal tools subject to permissions. Web and API tool sets differ. Adaptive thinking must be enabled explicitly when required; a request without a thinking field may run without thinking.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Dated base API price is $5/$25 per million input/output tokens. Anthropic recommends xhigh for coding/agents and high for other hard work; xhigh/max need adequate max_tokens.

Use Opus as the dated baseline for Fable comparisons. Do not mix web Extra, API xhigh, and multi-agent Code results. Retain task set, prompt hash, context, and output budget.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Hard coding, analysis, documents, spreadsheets, and agentic work when Fable cost or availability is unsuitable.

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
Verification: domain tests, source accuracy, output-budget completion, scope audit, latency, and correction time.
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
| Domain validator and acceptance result | 35 | domain tests, source accuracy, output-budget completion, scope audit, latency, and correction time |
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

- assuming thinking is active when omitted, truncating xhigh/max through an inadequate output budget, or comparing different harnesses as bare models.
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
