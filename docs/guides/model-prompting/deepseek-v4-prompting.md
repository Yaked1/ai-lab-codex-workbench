# DeepSeek V4 Prompting Guide

Checked: 2026-07-12

## What It Is and Where It Is Available

DeepSeek labels DeepSeek-V4-Pro and DeepSeek-V4-Flash as Preview. The official
API identifiers are `deepseek-v4-pro` and `deepseek-v4-flash`; the API supports
OpenAI-compatible and Anthropic-compatible endpoints. Both have documented
thinking/non-thinking modes, JSON output, and tool calls. Use the live pricing
page before cost-sensitive deployment.

## Task Selection and Controls

Use Pro for difficult, cost-justified reasoning and Flash for high-volume,
bounded tasks. Treat a thinking-mode toggle, structured output, and tool calls
as separate configuration choices. The model name does not grant a repository
agent, browser, or an integration's own tool permissions.

## Recommended Prompt Structure

```text
Model: [deepseek-v4-pro | deepseek-v4-flash]
Mode: [thinking | non-thinking]
Goal: [single measurable result]
Inputs: [bounded data or files]
Tool schema: [allowed calls and expected JSON]
Verification: [validator, test, or human rubric]
Failure: return an explicit blocked status, never guessed fields
```

## Example Work Orders

```text
Extract the invoice fields into the supplied JSON schema. Use no external tools.
Reject uncertain values as null and validate the JSON against [schema].
```

```text
Inspect [repository area], propose the smallest repair, apply only after naming
the regression test, run [command], and report changed paths plus output.
```

## Context, Cost, and Verification

The official table lists a 1M context and 384K maximum output, but long context
is not a retrieval guarantee. Index inputs, delimit sources, and test recall on
representative documents. Record model, thinking mode, tool setup, retries,
tokens, latency, and fallback behavior when evaluating Pro against Flash.

## Failure Modes and Unsupported Uses

Do not present Preview as stable. Do not infer license terms from weight
availability, convert vendor benchmark results into independent evidence, or
assume an Anthropic-compatible endpoint supplies Claude product behavior.

## Sources

- [DeepSeek V4 preview release](https://api-docs.deepseek.com/news/news260424/)
- [DeepSeek models and pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [Evidence ledger](sources-and-observations.md)

## Shared execution policy

Run records, verification, escalation, and operational failure handling live
in one place:

- [Shared execution contract](shared-execution-contract.md)

Use that contract for every serious run. Keep only model-specific identity,
surfaces, task fit, examples, limits, and evidence on this page.

## Model-specific operating notes

### Preview mode-control protocol

Hold thinking mode constant when comparing Pro and Flash. FIM is documented as
non-thinking only, so it is a different workload from reasoning chat. Record
cache condition, concurrency behavior, API format, tool schema, and retry
policy; Preview access is not stable-release evidence.
