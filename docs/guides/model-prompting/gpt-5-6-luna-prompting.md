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

## Shared execution policy

Run records, verification, escalation, and operational failure handling live
in one place:

- [Shared execution contract](shared-execution-contract.md)

Use that contract for every serious run. Keep only model-specific identity,
surfaces, task fit, examples, limits, and evidence on this page.

## Model-specific operating notes

### Luna-specific batch discipline

Use Luna with schemas, gold samples, deterministic validators, and explicit
null handling. Sample failures before scaling a batch. Do not launch parallel
workers against shared mutable files; use independent shards and a separate
integration reviewer instead.
