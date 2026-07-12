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
