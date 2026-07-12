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
