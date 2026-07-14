# GLM-5.2 Prompting Guide

Checked: 2026-07-12

## What It Is and Where It Is Available

Z.ai introduced GLM-5.2 on 2026-06-16 as an open-source, MIT-licensed
long-horizon model with published weights and a 1M-token context claim. The
reviewed first-party source identifies `GLM-5.2` for Coding Plan and describes
Z.ai and ZCode access. It documents High and Max thinking choices on its coding
surfaces; it does not establish a current API price or maximum-output limit.

## Appropriate Tasks and Effort

Use GLM-5.2 for long-horizon coding and analysis only when the task has a real
state record, a limited tool boundary, and repeated verification. Use High for
ordinary difficult work and reserve Max for measured headroom. Do not infer a
web-search, system-instruction, or computer-control capability from a coding UI.

## Recommended Prompt Structure

```text
Goal: [end state, not a vague exploration]
Context map: [files, source roles, known failures]
Allowed actions: [tools, paths, budget]
Milestones: [observable checkpoints]
Verification: [tests, diff review, source ledger]
Failure behavior: preserve state and report the blocked milestone
```

## Example Work Order

```text
Repair the failing integration in [paths]. First produce a dependency map, then
make the smallest change, run [tests], and report each milestone and any failed
assumption. Stop before network, deployment, or destructive actions.
```

## Context, Verification, and Cost

Long context needs a navigable source map and checkpoints. Measure success,
correction burden, latency, tokens, effort, and tool configuration, not a vendor
benchmark in isolation. Check current product limits and pricing before use.

## Failure Modes and Unsupported Uses

Do not treat the 1M context claim as proof of useful recall. Do not cite Z.ai
benchmark charts as independent results or assume a public weight automatically
makes every deployment safe, cheap, or compatible with an agent harness.

## Sources

- [Z.ai: GLM-5.2](https://z.ai/blog/glm-5.2)
- [ZCode Agent documentation](https://zcode.z.ai/en/docs/agents)
- [Evidence ledger](sources-and-observations.md)

## Shared execution policy

Run records, verification, escalation, and operational failure handling live
in one place:

- [Shared execution contract](shared-execution-contract.md)

Use that contract for every serious run. Keep only model-specific identity,
surfaces, task fit, examples, limits, and evidence on this page.

## Model-specific operating notes

### Long-horizon state discipline

Use a source map, milestones, and compact evidence-linked state instead of
replaying raw transcripts. A 1M-token context is capacity, not a guarantee of
useful retrieval. Treat vendor benchmark results as vendor claims and report
High/Max comparisons with the same task, tools, and completion definition.
