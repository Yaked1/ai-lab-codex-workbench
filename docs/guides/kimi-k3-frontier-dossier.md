# Kimi K3 Frontier Dossier

Checked: 2026-07-17

Kimi K3 is Moonshot AI's current frontier-model release. This page records only
claims traceable to Moonshot's official announcement and current product
surfaces on the checked date. Vendor benchmarks remain vendor claims unless an
independent evaluator publishes a reproducible matching configuration.

## Release card

| Release field | Evidence-conscious record |
| --- | --- |
| Developer | Moonshot AI |
| Announcement date | July 17, 2026 |
| Release state | Hosted product and API release; full model weights announced for release by July 27, 2026 and not yet inspectable on the checked date |
| Model identifier | `kimi-k3` in Moonshot's API documentation |
| Intended role | Frontier coding, long-horizon agents, knowledge work, reasoning, and native multimodal tasks |
| Architecture disclosure | 2.8T-parameter Mixture-of-Experts model using Kimi Delta Attention, Attention Residuals, and Stable LatentMoE; 16 of 896 experts active |
| Context | Up to 1 million tokens on the documented Kimi Code surface |
| Reasoning effort | `max` at launch; low and high announced for later updates |
| Weights and license | Full weights announced for release by July 27, 2026; license and final checkpoint artifacts must be inspected when published |
| API pricing | $0.30/MTok cache-hit input, $3.00/MTok cache-miss input, and $15.00/MTok output on the checked official announcement |
| Primary source | [Moonshot AI's official Kimi K3 announcement](https://www.kimi.com/blog/kimi-k3) |

## Launch story

Moonshot presents Kimi K3 as its most capable model and the first open
3T-class system. The official announcement describes native vision, a
1-million-token context window, and deployment across Kimi.com, Kimi Work,
Kimi Code, and the Kimi API. The hosted release is usable now, while the full
weights remain a future artifact until the announced July 27 publication occurs.

## Architecture and infrastructure

Moonshot discloses a 2.8-trillion-parameter sparse architecture built around:

- Kimi Delta Attention for efficient long-context attention;
- Attention Residuals for selective retrieval across model depth;
- Stable LatentMoE with 16 of 896 experts active;
- Gated MLA and additional training-stability mechanisms;
- quantization-aware training using MXFP4 weights and MXFP8 activations.

These are vendor-published architecture facts. They do not yet provide every
checkpoint-level field needed for independent deployment, such as the final
license, complete configuration files, shard inventory, checksums, exact layer
count, or verified runtime compatibility. Moonshot recommends supernode-class
configurations with 64 or more accelerators, which makes local deployment a
substantial infrastructure project rather than an ordinary workstation task.

## Capabilities and product behavior

Kimi K3 is a plausible candidate for:

- repository-scale coding and repair tasks with executable validation;
- source-grounded research with a claim ledger;
- long-context synthesis where omissions and contradictions are measured;
- multimodal coding that iterates over screenshots or visual artifacts;
- agent workflows with explicit tool schemas and approval boundaries;
- matched cost-quality comparisons against other frontier systems.

The official Kimi Code documentation exposes model ID `k3`, up to 1M context,
and max reasoning effort at launch. The announcement warns that preserved
thinking history matters: switching models mid-session or using an incompatible
harness can make output quality unstable. Start a fresh session for controlled
comparisons and record the exact harness and effort.

## Benchmarks, results, and what they establish

Moonshot publishes coding, productivity, agentic, and multimodal evaluations,
but the announcement itself explains that different rows use KimiCode, Claude
Code, Codex, Terminus, or benchmark-specific harnesses. Those results are not
bare-checkpoint scores and should not be averaged as though the harnesses were
identical.

A useful comparison record is:

```text
Model and returned identifier:
Surface and client version:
Reasoning or effort mode:
Harness and tool versions:
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

When the announced weights appear, perform a separate checkpoint audit covering:

1. repository owner and immutable revision;
2. license and acceptable-use terms;
3. configuration-declared total and active parameters;
4. layer count, expert routing, tokenizer, and context configuration;
5. weight formats, shard sizes, and checksums;
6. supported inference runtimes and minimum hardware;
7. first-party versus community quantizations;
8. parity checks against the official API using Moonshot's verifier guidance.

## Limits, unknowns, and misleading shortcuts to avoid

The checked announcement does not yet establish the final weight license,
checkpoint file layout, checksums, complete layer configuration, independent
benchmark reproduction, or practical quality of third-party inference ports.
A promised open release is not the same as published, inspectable artifacts.
The 2.8T total parameter count also does not mean 2.8T parameters are active per
token; Moonshot states that 16 of 896 experts are active.

Moonshot explicitly lists sensitivity to missing thinking history and excessive
proactiveness as limitations. Production prompts should impose clear action,
write, network, and approval boundaries rather than rewarding improvisation.

## Practical verdict

Kimi K3 belongs in the frontier-model evaluation set now as a hosted system and
as an announced open-weight model. Its disclosed sparse architecture is notable,
but deployment claims must wait for the July 27 artifacts and license. Use it
where matched task success justifies cost and latency, and re-audit this dossier
when the weights, technical report, or pricing change.

## Sources and recheck triggers

- [Kimi K3 official announcement](https://www.kimi.com/blog/kimi-k3)
- [Kimi Code model configuration](https://www.kimi.com/code/docs/en/kimi-code/models.html)
- [Kimi API Platform](https://platform.kimi.ai/)

Recheck on or after July 27, 2026, when the technical report appears, when API
pricing changes, or when Moonshot adds the announced low and high effort modes.

## Verification

```powershell
python -m unittest tests.test_kimi_k3_frontier
python -m unittest tests.test_frontier_model_dossiers
```

Failure means the dossier is missing its dated evidence boundary, architecture,
announced weight status, operational evaluation contract, or explicit unknowns.
