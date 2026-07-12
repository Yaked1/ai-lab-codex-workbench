# Claude Sonnet 5 Prompting Guide

Checked: 2026-07-12

## What It Is and Where It Is Available

Claude Sonnet 5 is Anthropic's released Sonnet-class model. Anthropic's
2026-06-30 launch post lists Claude plans, Claude Code, and the Claude Platform;
the API identifier is `claude-sonnet-5`. Introductory API pricing is $2/$10 per
million input/output tokens through 2026-08-31, then $3/$15. Confirm the live
surface and price before a production purchase.

## Appropriate Tasks and Controls

Use it for normal knowledge work, scoped coding, tool-using workflows, and
cost-sensitive agent trials. The checked launch source describes variable effort
but does not establish a complete effort menu for every product surface. Do not
invent an effort value, tool permission, context limit, or computer-use feature:
read the current product or API documentation for the surface being used.

## Recommended Prompt Structure

```text
Goal: [observable deliverable]
Context: [sources, repository, or data]
Allowed tools: [names and boundaries]
Constraints: [cost cap, files to avoid, safety rules]
Verification: [test, source check, or acceptance rubric]
Stop: [missing authority, ambiguous requirement, or failed check]
```

For long context, supply a source map and ask the model to identify conflicts
before synthesis. For an agent, describe the actual tools, permissions, and
recovery rule instead of assuming browser or terminal access from the model name.

## Example Work Orders

```text
Task: Reconcile these three policy drafts into one decision memo.
Rules: Cite each factual claim to its supplied source; list conflicts; do not
invent policy. Verification: a reviewer can trace every recommendation.
```

```text
Task: Fix the failing test in [path]. Inspect before editing, change only files
needed for the regression, run [command], and report the exact result.
```

## Cost, Verification, and Failure Modes

Keep the context relevant, start with a small acceptance test, and measure total
cost including retries and tool calls. Do not use Sonnet 5 as evidence that it
replaces Claude Fable 5 or Opus 4.8; compare matched tasks. If tools are absent,
sources conflict, or a product control is not documented, stop and report that
boundary instead of simulating the capability.

## Unsupported or Inappropriate Uses

Do not claim a fixed context window, a universal effort menu, unrestricted web
search, computer control, or safe autonomous action without surface-specific
official documentation. Do not use an unsupported model control in API examples.

## Sources

- [Anthropic launch: Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)
- [Main research snapshot](../frontier-models-and-multimodal-systems-2026.md)
- [Evidence ledger](sources-and-observations.md)

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
### Sonnet-specific surface boundary

The launch describes agentic tool use, but each client controls which tools are
actually present. Do not infer a fixed effort menu, browser permission, terminal,
or context limit from the model name. Check the selected Claude surface and
record the actual controls used in the run.
