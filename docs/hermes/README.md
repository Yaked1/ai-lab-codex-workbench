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
- Installation: <https://hermes-agent.nousresearch.com/docs/getting-started/installation>
- Configuration: <https://hermes-agent.nousresearch.com/docs/user-guide/configuration>
- Memory: <https://hermes-agent.nousresearch.com/docs/user-guide/features/memory>
- Cron: <https://hermes-agent.nousresearch.com/docs/user-guide/features/cron>

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
