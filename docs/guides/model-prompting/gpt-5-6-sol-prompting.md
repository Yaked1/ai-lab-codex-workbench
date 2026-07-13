# GPT-5.6 Sol Prompting Guide

Checked: 2026-07-12

Sol is OpenAI's **flagship GPT-5.6 tier** for the hardest professional work:
complex coding, research, science, design, and high-stakes synthesis. Effort
controls how aggressively Sol reasons and uses tools; it does not turn a vague
wish into a verified result.

| Property | Value |
| --- | --- |
| Role | Flagship GPT-5.6 tier |
| API ID | `gpt-5.6-sol` |
| Base API price (dated) | $5 / $30 per 1M input/output tokens |
| Context (API) | 1.05M input, 128K max output |
| Independent coding note | Sol Max in Codex led cited Coding Agent Index at 80 |
| Companion guides | [Terra](gpt-5-6-terra-prompting.md), [Luna](gpt-5-6-luna-prompting.md), [Surface map](surface-and-effort-map.md) |

## When to Choose Sol

Choose Sol when:

- mistakes are expensive (migrations, security-sensitive review, architecture);
- the task needs strong judgment across conflicting sources;
- you already tried Terra High/Max or Luna Max and failed acceptance checks;
- you need the best single-agent coding result cited for Codex Max.

Do **not** choose Sol when:

- the task is a pure schema transform or one-file format fix (use Luna);
- daily multi-file work with clear tests (Terra Medium/High is usually enough);
- you only want "more thinking" on a sequential task (raise effort, not always tier).

## Effort Menus by Surface

| Surface | Efforts | Notes |
| --- | --- | --- |
| Codex CLI 0.144.0+ | Low, Medium, High, Extra High, Max, Ultra | 0.144.0 minimum; local default Low; 0.144.1 latest stable when checked |
| New ChatGPT Desktop App | **Light**, Medium, High, Extra High, Max, Ultra | Dated observation; Light = Codex Low |
| ChatGPT Work web (Plus) | Low/Light through Max observed | User-observed **no Ultra** |
| ChatGPT Work web (Pro / Enterprise) | Through Max plus Ultra | Official launch eligibility; exact lower menu can vary |
| ChatGPT Work web (Business) | Ultra observed on the user's workspace | Not a universal official plan claim; admin policy may restrict |
| Standard Chat | Medium, High, Extra High; Sol Pro on Pro+ | Terra/Luna not available |
| API | `none`, `low`, `medium`, `high`, `xhigh`, `max` | `ultra` is not an API reasoning value |

## Effort Mode Playbooks

### Light / Low

**Best fit:** narrow review, one-file repair, fixed-schema extraction that still
benefits from flagship judgment.

**Prompt shape:** exact input, one output, one deterministic check.

**Main failure risk:** missing hidden dependencies outside the named files.

```text
Model: GPT-5.6 Sol | Effort: Light/Low

Goal:
Fix only [function/file] so [observable behavior].

Context:
- Read [file paths] and [related test if any].
- Prior error: [paste exact error].

Scope:
Include: [paths]
Exclude: everything else. Do not refactor, rename, or restyle.

Constraints:
- No new dependencies.
- No secrets.
- Keep the diff under ~[N] lines if possible.

Method:
1. Locate the root cause in the named files only.
2. Apply the smallest correct fix.
3. Run: [single command].

Verification:
- Paste command output.
- State changed files.

Failure:
If the fix requires files outside scope, stop and report the missing path.
```

### Medium

**Best fit:** ordinary professional work; default practical Sol choice for
eligible Chat users (first Sol reasoning level on many plans).

**Prompt shape:** goal, files/sources, constraints, acceptance tests.

**Main failure risk:** under-scoping a genuinely hard task.

```text
Model: GPT-5.6 Sol | Effort: Medium

Goal:
Deliver [feature/doc/analysis] that passes [acceptance criteria].

Context:
- Repo/project: [name]
- Read first: [AGENTS.md / README / key files]
- Known constraints: [list]

Scope:
Include: [paths]
Exclude: [paths, dependency files, CI unless asked]

Method:
1. Inspect before editing.
2. Implement the smallest complete solution.
3. Run checks.
4. Report evidence.

Verification:
- Commands: [list]
- Success looks like: [tests green / schema valid / citations present]

Output:
Changed files, commands + results, remaining risks.
```

### High

**Best fit:** multi-step reasoning, difficult implementation, first-plausible
answer that still needs testing.

**Prompt shape:** inspect-before-edit, acceptance tests, evidence for done.

**Main failure risk:** more latency and tool use without stronger gates.

```text
Model: GPT-5.6 Sol | Effort: High

Goal:
[Hard multi-file outcome]

Context:
- Symptoms: [log / failing test / user report]
- Already tried: [what failed]
- Relevant subsystems: [list]

Method:
1. Form 2-3 hypotheses ranked by likelihood.
2. Gather evidence for/against each before large edits.
3. Implement the fix that survives the evidence.
4. Add or update tests that would have caught the bug.
5. Run the full relevant suite.

Verification:
- Primary: [command]
- Secondary: [command]
- Falsification: [what would prove the fix wrong]

Stop if:
You cannot isolate a root cause after [N] investigation steps; report evidence.
```

### Extra High / xhigh

**Best fit:** real uncertainty: cross-service failure, unfamiliar repo, hard
proof, conflicting sources.

**Prompt shape:** decision log, boundaries, checkpoints, stop conditions.

**Main failure risk:** over-analysis on routine work.

```text
Model: GPT-5.6 Sol | Effort: Extra High / xhigh

Goal:
Resolve [uncertain problem] and produce [decision or patch] with evidence.

Decision log required:
- Alternatives considered
- Evidence for/against each
- Chosen path and why
- What would change the decision

Boundaries:
- Max files touched: [N]
- Do not expand into [cleanup, renames, drive-by refactors]
- Checkpoint every [major step] with status

Evidence rules:
- Prefer command output and file citations over claims.
- Label Official / Independent / Inference.
- If sources conflict, present both and choose with criteria.

Final gate:
Independent validation step: [second test matrix / red-team checklist]
```

### Max

**Best fit:** deepest single-model effort: final architecture, hard math/science,
high-risk migration, expensive miss if wrong.

**Prompt shape:** decision, alternatives, test matrix, review gate, falsifiers.

**Main failure risk:** large token and time cost.

```text
Model: GPT-5.6 Sol | Effort: Max

Goal:
Make a final recommendation / implementation for [high-stakes work].

Must include:
1. Restated problem and non-goals
2. Alternatives with tradeoffs
3. Recommendation with falsifiers
4. Test matrix (happy path, edge, failure, rollback)
5. Reviewer checklist of evidence to inspect
6. Residual risks and monitoring

Constraints:
- [latency, cost, compatibility, safety]
- Prefer reversible steps
- No secrets in output

Done means:
All matrix rows executed or explicitly skipped with reason, and a human can
reproduce the decision from the report alone.
```

### Ultra (orchestration, not “Max+”)

**Best fit:** parallelizable projects with separable workstreams.

**Not for:** tiny bugs, tightly sequential migrations, one shared mutable file.

**How it works (Official product description):** coordinates multiple agents
(often four by default) then a primary agent synthesizes. Total tokens can rise;
weak boundaries create duplication and conflicting edits.

**Plus web Work:** no Ultra in the supplied observation. **Pro/Enterprise
Work:** official Ultra eligibility. **Business Work:** Ultra was observed by the
user but is not generalized here. **Codex Plus and higher:** official Ultra
eligibility.

```text
Model: GPT-5.6 Sol | Effort: Ultra

Overall goal:
[Project outcome]

Subtask contracts (independent streams):
1. Implementation owner: [scope A], forbidden: [B]
2. Tests owner: [test paths], must not change production code unless required
3. Docs owner: [doc paths]
4. Adversarial review owner: read-only, produce findings only

Shared contracts:
- Interfaces / schemas: [paths]
- Do not both edit: [hot files]
- Merge rule: primary synthesizer reconciles; prefer tests as truth

Synthesis criteria:
- One coherent diff
- No contradictory edits
- Full verification suite once
- Report per-stream contributions and conflicts resolved

If streams are not independent, abort Ultra and rerun at High or Max.
```

## Surface-Specific Templates

### Codex repository work order

```text
You are operating in a local repository with shell and file tools.

Repo root: [path]
Branch: [name]
Read first: AGENTS.md, [target files]

Task: [one sentence]
Include: [paths]
Exclude: [paths]
Forbidden: secrets, force-push, broad cleanup, dependency changes unless asked

Commands to run:
1. [test]
2. [lint/health]

Done only with:
- diff limited to scope
- command output pasted
- remaining risks listed
```

### ChatGPT Work artifact

```text
Produce [artifact type] for [audience].

Sources: [uploads / connected files]
Trace every numeric claim to a source.
Flag conflicts instead of averaging them.
End with: recommendation, confidence, open questions.
Do not invent citations.
```

### Standard Chat (Sol Medium / High / Extra High / Pro)

```text
Answer as GPT-5.6 Sol.

Question: [precise question]
Audience: [who]
Required structure:
1. Direct answer
2. Reasoning summary (short)
3. Assumptions
4. Checks a skeptical reader should run
5. What would change the answer

If information is insufficient, say so and ask only the missing facts.
```

### API configuration sketch

```text
model: gpt-5.6-sol
reasoning.effort: high   # none|low|medium|high|xhigh|max
# ultra is not a reasoning.effort value; use multi-agent beta separately
```

Measure success, latency, output tokens, tool calls, and human correction time
on your eval set. Higher effort is not always better for structured tasks.

## Failure Modes and Repairs

| Symptom | Likely cause | Repair |
| --- | --- | --- |
| Beautiful plan, wrong code | No acceptance tests in prompt | Name exact commands and pass criteria |
| Scope explosion | Ultra or Max without boundaries | Cap files, forbid cleanup, require checkpoint |
| Missed dependency | Light/Low on multi-file bug | Raise to High and list callers/tests |
| Expensive no-op | Max/Ultra on sequential tiny task | Drop to Medium/High |
| Conflicting multi-agent edits | Ultra without ownership map | Assign exclusive file ownership |
| Hallucinated sources | Chat/Work without citation rule | Require claim→source map; flag gaps |

## Verification Checklist

- [ ] Tier is Sol for a reason (not habit)
- [ ] Effort matches uncertainty, not anxiety
- [ ] Surface labels understood (Light vs Low, Extra High vs xhigh, Ultra vs Max)
- [ ] Scope fence present
- [ ] Verification commands or citation rules present
- [ ] Ultra only if streams are independent
- [ ] Cost acceptable for Max/Ultra path

## Related

- [Surface and effort map](surface-and-effort-map.md)
- [Fable vs Sol](../fable-vs-sol.md)
- [Frontier essay](../frontier-models-and-multimodal-systems-2026.md)
- [Coding-agent prompting](../prompting-ai-coding-agents.md)
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
### Sol-specific review gate

Use Sol for decisions whose error cost justifies deeper inspection. Require a
hypothesis ledger, alternatives, falsifiers, and an adversarial review. Ultra is
orchestration, so define independent ownership and an integration test rather
than treating it as a single-model reasoning value.

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** GPT-5.6 Sol; API `gpt-5.6-sol`; Chat also exposes the separate Sol Pro path.
- **Release / availability:** Current GPT-5.6 flagship on the checked date. Codex requires 0.144.0 or later; installed 0.144.0, stable 0.144.1, alpha 0.145.0-alpha.4.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** exact rollout picker for any uninspected account; universal Business Work Ultra eligibility; closed architecture details.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

Plus Chat: Medium/High. Pro, Business, Enterprise Chat: Medium/High/Extra High/Sol Pro. Work and Desktop Work/Codex: Light or Low through Max, with Ultra only where plan policy exposes it. CLI: Low through Ultra. API: none through max, never ultra.

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

Chat attachments depend on the product. Work can use enabled Plugins/apps. Codex can inspect, edit, run commands, test, search, and use configured MCP or skills within its sandbox. API tools exist only when the caller configures them.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Dated API envelope: 1.05M context, 128K output, $5/$30 per million input/output tokens, $0.50 cached input. Long-context multipliers apply above the published threshold.

Vendor launch chart: Agents Last Exam 52.7, GDPval-AA v2 1747.8, management consulting 43.2, Big Finance 53, AA Intelligence 58.9. Retain the vendor harness and effort; run local paired tests before selecting Sol over Terra.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Hard debugging, high-stakes synthesis, architecture, long agent loops, final review, and work where Terra has failed a frozen acceptance gate.

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
Verification: repository tests or artifact-specific checks plus source traceability, scope audit, and final model identity.
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
| Domain validator and acceptance result | 35 | repository tests or artifact-specific checks plus source traceability, scope audit, and final model identity |
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

- treating Sol Pro as an effort, sending API `ultra`, omitting worker costs in Ultra, or claiming benchmark dominance without the published harness.
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
