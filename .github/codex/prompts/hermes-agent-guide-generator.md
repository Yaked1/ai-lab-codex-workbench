# Hermes Agent Guide Generator Prompt

Target tool: Local Codex curator prompt

Purpose: generate public-safe documentation about Nous Research Hermes Agent as
an agent/workflow tool.

Scope allowed:

- What Hermes Agent is.
- What Hermes Agent is used for.
- Difference between Hermes Agent and normal chatbots.
- Difference between Hermes Agent, Codex, and Claude Code as agent/workflow
  tools.
- Provider configuration.
- Skills.
- Memory.
- Automations.
- Public research and documentation workflows.
- Prompt guide, skill guide, and agent workflow organization.
- Public-repository safety, privacy risks, dry runs, and reviewed PRs.
- Installation and setup only when verified from official Hermes Agent docs.

Scope forbidden:

- Hermes language models.
- Hermes 3, Hermes 4, or Hermes 4.3.
- GGUF files.
- Ollama Hermes model downloads.
- vLLM or SGLang model serving.
- Model benchmarks.
- Model parameter counts.
- Model quantization.
- Model cards.
- Local model running.

Public safety requirements:

- Do not include provider API keys.
- Use placeholders such as `$env:PROVIDER_API_KEY = "replace-with-your-key"`.
- Tell users not to commit `.env`, local memory files, tokens, OAuth files,
  logs, private conversations, or browser session data.
- Never allow Hermes Agent to push directly to `main`.
- Prefer branch, pull request, checks, review, and merge.
