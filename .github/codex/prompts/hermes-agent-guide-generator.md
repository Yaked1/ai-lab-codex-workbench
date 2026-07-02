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
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `.github/codex/prompts/hermes-agent-guide-generator.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `hermes agent guide generator` state what decision, workflow, or reusable behavior it supports?
- Are included scope, excluded scope, and unsafe actions clear enough for an
  agent or contributor to follow?
- Are examples public-safe, repository-relative, and free of private data?
- Are fast-changing product or platform claims phrased conservatively or marked
  for official-doc verification?
- Does the file point to the next artifact a reader should inspect: a command,
  template, test, manifest, package, or deeper guide?
- Could a reviewer cite this file in a PR review and know what evidence proves
  the work is complete?

Keep future edits focused on stronger evidence, clearer failure modes, better
navigation, and safer automation boundaries. Do not add length unless the new
material makes the repository easier to operate, teach, audit, or recover.
<!-- RESEARCH-GRADE-EXPANSION:END -->
