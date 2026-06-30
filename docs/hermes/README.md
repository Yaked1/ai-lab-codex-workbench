# Hermes Agent Guides

These guides cover Nous Research Hermes Agent as an agent and workflow tool for
public research, documentation, skills, memory, provider configuration, and
automations.

Scope: Hermes Agent only. This folder does not cover Hermes language-model
families, model files, quantization, benchmarks, local model serving, or model
cards.

Official source anchors:

- Hermes Agent docs: <https://hermes-agent.nousresearch.com/docs/>
- Hermes Agent repository: <https://github.com/NousResearch/hermes-agent>
- Repository license: MIT, as listed by the official repository and docs.
- Installation: <https://hermes-agent.nousresearch.com/docs/getting-started/installation>
- Configuration: <https://hermes-agent.nousresearch.com/docs/user-guide/configuration>
- Skills: <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
- Memory: <https://hermes-agent.nousresearch.com/docs/user-guide/features/memory>
- Cron: <https://hermes-agent.nousresearch.com/docs/user-guide/features/cron>

Source status: official documentation and official repository. Link to these
sources and summarize conservatively rather than copying long examples. Verify
current commands, platform support, provider behavior, and pricing in the
official docs before teaching setup.

## Guide Map

| Guide | Use it for |
| --- | --- |
| [Hermes Agent](hermes-agent.md) | Core concept, use cases, and public-repo workflow boundaries. |
| [Local agent setup](local-agent-setup.md) | Official install commands and verification steps. |
| [Provider configuration](provider-configuration.md) | Providers, secrets, placeholders, and config safety. |
| [Skills, memory, automations](skills-memory-automations.md) | Skills, memory, scheduled work, and manual review. |
| [Prompting Hermes Agent](prompting-hermes-agent.md) | Public-safe prompts and evaluation checklists. |
| [Hermes Agent vs Codex vs Claude Code](hermes-agent-vs-codex-vs-claude-code.md) | Workflow comparison, not model comparison. |
| [Public repo safety](public-repo-safety.md) | What must not be committed or auto-published. |
| [Troubleshooting](troubleshooting.md) | Common setup, provider, memory, and automation failures. |

## Research Loop Role

The daily research scout may discover Hermes Agent updates, but it must not run
Hermes Agent automatically. Curator prompt prep may prepare a local Codex prompt,
but Hermes Agent documentation updates still happen through local/manual editing
and a reviewed pull request.

## Reader Paths

| Reader | Path |
| --- | --- |
| Beginner evaluating Hermes Agent | Read this README, then `hermes-agent.md`, then `public-repo-safety.md`. |
| Maintainer writing setup docs | Read `local-agent-setup.md`, `provider-configuration.md`, and verify official docs. |
| Prompt author | Read `prompting-hermes-agent.md` and adapt the public-safe prompt template. |
| Automation reviewer | Read `skills-memory-automations.md`, `public-repo-safety.md`, and `troubleshooting.md`. |
| Tool comparison reader | Read `hermes-agent-vs-codex-vs-claude-code.md` and avoid model comparisons. |

## Hard Scope Boundary

This folder covers Hermes Agent as a workflow tool:

- public research organization
- provider configuration safety
- skills
- memory
- scheduled work
- public repository documentation workflows

This folder does not cover:

- Hermes language model families
- model cards
- benchmark claims
- quantization
- GGUF files
- Ollama setup
- vLLM
- SGLang
- local model serving
- training or fine-tuning

If a future contribution adds model-serving material here, move it out or
reject it unless the project scope changes explicitly.

## Verification Standard

Before updating Hermes Agent docs:

- Check official docs for installation, configuration, skills, memory, and cron
  behavior.
- Use placeholders for commands not verified in the current change.
- Keep provider credentials out of examples.
- Run repository checks.
- Update changelog when the public guide changes.
- Mark pricing, provider behavior, and platform support as official-doc
  verification items.

## Public-Safe Example Boundary

Safe examples:

- Public candidate report review.
- Public source ledger creation.
- Drafting a guide outline for PR review.
- Read-only explanation of a public repository folder.

Unsafe examples:

- Using private memory as source material.
- Publishing a scheduled daily guide update automatically.
- Committing provider config.
- Copying prompt dumps.
- Reading browser sessions or OAuth state.
