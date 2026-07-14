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

## Shared execution policy

Run records, verification, escalation, and operational failure handling live
in one place:

- [Shared execution contract](shared-execution-contract.md)

Use that contract for every serious run. Keep only model-specific identity,
surfaces, task fit, examples, limits, and evidence on this page.

## Model-specific operating notes

### Opus-specific baseline discipline

Use Opus when a cleaner Claude-family baseline is needed. Keep the harness,
tools, repository state, prompt, and review rule fixed when comparing it with
Fable or another product. A polished document is incomplete until its claims,
calculations, and cited sources are checked.
