# Model Routing

Checked: 2026-07-11

Route by task shape, evidence needs, and verification cost. Model and effort
names are not stable contracts, so check the live picker or catalog before
building a workflow around them.

## Codex and ChatGPT Work

| Route | Best fit | Escalate when |
| --- | --- | --- |
| GPT-5.6 Luna low/medium | Small edits, extraction, formatting, quick summaries. | The task spans several files or contains a judgment call. |
| GPT-5.6 Terra medium/high | Normal coding, tests, documents, and bounded research. | One honest attempt fails or the failure cost is high. |
| GPT-5.6 Sol high/xhigh | Hard debugging, architecture, synthesis, and final review. | Independent workstreams can run in parallel. |
| GPT-5.6 Sol max | Deep single-agent reasoning with full evidence. | The task genuinely benefits from delegated agents. |
| GPT-5.6 Sol or Terra ultra | Independent workstreams with clear contracts and integration checks. | Coordination cost exceeds the value of parallelism. |

The local Codex catalog checked on 2026-07-11 exposed `ultra` for Sol and Terra,
but not Luna. Product access varies by plan and rollout. API multi-agent is
separate from the API's `reasoning.effort` control.

## Claude

| Route | Best fit | Escalate when |
| --- | --- | --- |
| Fable low/medium | Bounded analysis or drafting where Fable-specific quality is worth the price. | The task needs long tool use or difficult judgment. |
| Fable high | Difficult knowledge work or coding with verification. | The task needs deeper long-horizon search. |
| Fable xhigh | Long coding and agent work with large token budgets. | The work needs maximum single-agent analysis or delegation. |
| Fable max | Deep single-agent analysis and correctness-sensitive review. | Independent agents can reduce wall-clock time. |
| Fable Ultracode in Claude Code | Delegated coding work with explicit ownership and merge tests. | The work is linear or file ownership is unclear. |

Ultracode is built on `xhigh` plus permission to run multi-agent workflows. It
is not an API effort above `max`.

## Other Routes

| Model or tool | Use for | Verification |
| --- | --- | --- |
| Gemini 3.5 Flash | High-volume extraction, classification, fast coding loops, and first-pass research. | Spot-check samples and verify every citation. |
| Gemini 3.5 Live Translate | Real-time audio translation. | Test the exact language pair, accent, noise, and device path. |
| Grok 4.5 High in Grok Build | Coding and agent work where Grok Build is the chosen harness. | Run repository tests and inspect regional/pricing availability. |
| GPT-Live-1 | Natural voice interaction and delegated spoken tasks. | Confirm current product access; API access was not confirmed on the checked date. |
| Local models | Private, offline, low-risk transforms and tagging. | Treat every material result as untrusted until checked. |

## Routing Rules

1. Use a script for deterministic parsing, arithmetic, transforms, and hashes.
2. Start at the lowest route that can meet the acceptance criteria.
3. Escalate after evidence of difficulty, not because a higher label exists.
4. Use multi-agent modes only for independent tasks with integration checks.
5. Compare models on the real task with the same prompt, tools, time, and pass
   criteria before making a durable routing rule.
6. Keep community sentiment out of routing decisions unless a local evaluation
   reproduces the concern.

See [current models and interfaces](guides/current-models-and-interfaces.md) for
availability, prices, exact effort labels, sources, and uncertainties. See
[Fable vs Sol](guides/fable-vs-sol.md) for the current evidence comparison.
