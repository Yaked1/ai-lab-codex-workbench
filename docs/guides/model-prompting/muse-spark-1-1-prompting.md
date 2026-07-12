# Meta Muse Spark 1.1 Prompting Guide

Checked: 2026-07-12

Muse Spark 1.1 is Meta's **multimodal reasoning model** for agentic work,
computer use, coding, and multimodal understanding. It appears in Thinking mode
in Meta AI and through the Meta Model API public preview. The model name alone
does **not** grant a repository editor, browser, or computer-control harness;
the client supplies tools.

| Property | Value |
| --- | --- |
| Role | Lower-cost fast multimodal reasoning |
| Independent snapshot | ~51 Intelligence Index at xhigh; ~116 tok/s; 1M context; ~$1.25/$4.25 per 1M |
| Surfaces | Meta AI Thinking mode; Meta Model API public preview |
| Equal-score warning | Rounded Intelligence near Luna Max does not imply equal Codex coding reliability |

## When to Choose Muse Spark 1.1

Choose Muse when:

- you need multimodal understanding plus reasoning at lower cost;
- throughput matters;
- your own client provides tools (browser, computer use, code runner).

Prefer Luna/Terra/Grok/Sol when:

- you need a measured Codex coding-agent configuration;
- you need GPT-5.6 product integration (Work/Codex);
- GUI computer-use quality is unproven for your app.

## Prompting Principles

1. **Name the tools** the client actually exposes.
2. **Separate modalities** in the prompt (image facts vs text instructions).
3. **Keep one goal** per turn for agent loops.
4. **Require evidence** (screenshots, DOM snippets, file paths, command output).
5. **Do not assume** hidden computer control.

## Effort / Thinking Modes

Exact API enum names can change; independent testing has used an **xhigh-like**
deep setting. Treat Thinking vs non-Thinking (Meta AI) and API reasoning levels
as compute dials, not different model families.

| Mode band | Use | Prompt emphasis |
| --- | --- | --- |
| Fast / low thinking | Extraction, captioning, simple Q&A on clear inputs | Schema, short answers |
| Default thinking | Multistep tool use, coding with clear tests | Goal, tools, checks |
| Deep / xhigh | Ambiguous multimodal problems, multi-app computer tasks | Hypotheses, checkpoints, stop rules |

### Fast template

```text
Model: Muse Spark 1.1 | Mode: fast/low thinking

From the attached image/document, extract:
[fields]

Return JSON only matching:
[schema]

If a field is unreadable, use null and add "issues": ["..."].
```

### Agentic coding template

```text
Model: Muse Spark 1.1 | Mode: default/deep thinking

Available tools: [list exactly]
Workspace: [path or none]

Goal:
[outcome]

Constraints:
- Only use listed tools
- No invented file contents
- After each tool call, summarize observation before next action

Done when:
[tests or acceptance]

Final report:
actions taken, artifacts, verification, residual uncertainty
```

### Computer-use template

```text
Model: Muse Spark 1.1 | Computer-use client

Task:
Complete [UI workflow] in [app].

Start state:
[URL or screen description]

Rules:
- Prefer accessibility labels over brittle coordinates when available
- Confirm destructive clicks
- After each step: observe screenshot -> decide -> act
- Stop if login, CAPTCHA, or payment is required

Success screenshot criteria:
[what must be visible]
```

### Multimodal analysis template

```text
You will receive [images/pdfs/audio transcript].

Questions:
1. ...
2. ...

Answer format:
- Observation (what is visible/said)
- Inference (what you conclude)
- Confidence
- Missing evidence

Do not invent text that is not legible.
```

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Invents UI state | Require screenshot observation before action |
| Treats model as full IDE | Attach or name real tools |
| Overlong chain | Cap steps; checkpoint every N actions |
| Compared unfairly to Luna Max coding | Run same harness, same tests |

## Verification Checklist

- [ ] Tools actually available to the client
- [ ] Thinking depth matched to ambiguity
- [ ] Multimodal answers separate observation vs inference
- [ ] Computer-use stop conditions for login/payment
- [ ] Local eval if used for production coding

## Related

- [Luna](gpt-5-6-luna-prompting.md) for cheaper GPT coding volume
- [Gemini 3.5 Flash](gemini-3-5-flash-prompting.md) for Google tool stack
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
### Muse multimodal evaluation

Separate visual grounding, planning, tool-call validity, and completed task
quality. A correct-looking answer can still point to the wrong image region or
request an invalid action. The host application, not the model name, determines
desktop, browser, and repository permission.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** Meta Muse Spark 1.1 through Meta AI or Meta Model API preview as documented.
- **Release / availability:** Public-preview and consumer availability are surface dependent. Keep dated preview behavior separate from production guarantees.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** stable API terms, exact consumer picker, closed architecture, and whether independent price/context snapshots remain current.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Meta AI Thinking mode or Meta Model API preview. Independent xhigh tests describe one configuration but do not establish a universal consumer picker.

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

Record client-provided function, coding, computer-use, image, or search tools and their permissions. Multimodal inputs must retain file type, resolution, ordering, and preprocessing.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

The guide records an independent snapshot near 1M context, about 116 tokens/s, and roughly $1.25/$4.25, but these are not first-party permanent guarantees. Recheck the official API before budgeting.

Independent index results must keep effort, endpoint, date, latency, and tool setup. Run local multimodal and agent tests because a single aggregate score cannot establish tool reliability.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Multimodal reasoning, coding, computer use, and Meta ecosystem experiments where preview status is acceptable.

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
Verification: grounded multimodal answers, tool-call correctness, visual evidence references, latency, and preview stability.
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
| Domain validator and acceptance result | 35 | grounded multimodal answers, tool-call correctness, visual evidence references, latency, and preview stability |
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

- presenting an independent snapshot as official, claiming xhigh on a surface that does not show it, or omitting multimodal preprocessing.
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
