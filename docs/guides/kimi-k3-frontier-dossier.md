# Kimi K3 Frontier Dossier

Checked: 2026-07-17

Kimi K3 is Moonshot AI's current frontier-model release. This page records only
claims that can be traced to Moonshot's official announcement and product
surfaces on the checked date. It does not convert announcement language into
undisclosed architecture facts, and it treats the announced open-source date as
a future event until weights and a license are actually published.

## Release card

| Release field | Evidence-conscious record |
| --- | --- |
| Developer | Moonshot AI |
| Announcement date | July 16, 2026 |
| Release state | Hosted product and API release; open-source publication announced for July 27, 2026 but not yet verified |
| Intended role | Frontier reasoning, coding, agentic work, research, and long-context tasks |
| Architecture disclosure | Moonshot's announcement describes a 2.8T-parameter model; dense-versus-MoE topology and active-parameter count remain unverified in the checked public materials |
| Weights and license | Not yet published on the checked date; do not label the model open-weight until the announced release occurs and the files and license are inspected |
| Pricing | Verify against Moonshot's current API pricing page at the time of use; this dossier does not freeze a number without a stable first-party pricing record |
| Primary source | Moonshot AI's official Kimi K3 announcement and current product/API documentation |

## Launch story

Moonshot presents Kimi K3 as a new flagship intended to compete in difficult
reasoning, software engineering, research, and agent workflows. The announcement
emphasizes capability and scale, but a release post is not a substitute for a
model card, checkpoint configuration, tokenizer files, or an independently
reproduced evaluation. The 2.8T figure is therefore recorded as a vendor-stated
total-parameter claim, not as proof of a particular routing design.

## Capabilities and product behavior

Evaluate Kimi K3 as a complete system: exact model identifier, API or product
surface, reasoning mode, context supplied, tools, permissions, retries, and
fallback behavior. Coding results obtained in a hosted agent harness should not
be relabeled as bare-model API results. Likewise, a long context window is
capacity, not evidence that the model retrieved the correct evidence from a
large packet.

Kimi K3 is a plausible candidate for:

- repository-scale coding and repair tasks with executable validation;
- source-grounded research with a claim ledger;
- long-context synthesis where omissions and contradictions are measured;
- agent workflows with explicit tool schemas and approval boundaries;
- matched cost-quality comparisons against other frontier systems.

## Benchmarks, results, and what they establish

Treat every launch benchmark as a vendor claim unless the benchmark maintainer
or an independent evaluator publishes the exact model, effort, harness, tools,
time limit, and scoring method. Do not average incomparable rows across chat,
API, coding-agent, browsing, and tool-use systems. For repository work, prefer a
frozen task set and report accepted tasks, first-pass success, retries, wall
time, token or credit cost, and human correction.

A useful comparison record is:

```text
Model and returned identifier:
Surface and client version:
Reasoning or effort mode:
Tools and permission boundary:
Task-set revision and hashes:
Validator command:
Accepted tasks / total:
Retries and fallback events:
Provider cost and wall time:
Human correction minutes:
```

## Deployment and evaluation consequences

Before production use, verify the current API identifier, context and output
limits, rate limits, pricing, data-handling terms, regional availability, and
tool-call behavior from Moonshot's live documentation. Pin client versions where
possible and log provider responses that identify the model actually used.

When the announced open-source release occurs, perform a separate checkpoint
audit covering:

1. repository owner and immutable revision;
2. license and acceptable-use terms;
3. configuration-declared total and active parameters;
4. dense or mixture-of-experts topology;
5. tokenizer and context configuration;
6. weight formats, shard sizes, and checksums;
7. supported inference runtimes and required hardware;
8. quantizations and whether they are first-party or community supplied.

## Limits, unknowns, and misleading shortcuts to avoid

The checked evidence does not establish whether Kimi K3 is dense or MoE, how
many parameters are active per token, its layer count, expert count, attention
topology, training-token total, serving precision, or the exact license of the
future weights. A promised open-source date is not the same as published,
inspectable weights. Do not fill those fields from rumors, screenshots, model
names, or analogy with earlier Kimi releases.

## Practical verdict

Kimi K3 belongs in the frontier-model evaluation set now as a hosted system, but
its architecture row must remain explicitly incomplete until Moonshot publishes
inspectable technical artifacts. Use it where its measured task success justifies
its cost and latency, and re-audit the dossier after July 27, 2026 or whenever
Moonshot changes the model, pricing, or access surface.

## Verification

```powershell
python -m unittest tests.test_kimi_k3_frontier
python -m unittest tests.test_frontier_model_dossiers
```

Failure means the dossier is missing its dated evidence boundary, announced
open-source status, operational evaluation contract, or explicit unknowns.
