# Guides

## Current model and interface guides

- [Current models, interfaces, and effort controls](current-models-and-interfaces.md)
- [Frontier models and multimodal systems in 2026](frontier-models-and-multimodal-systems-2026.md)
- [Model and effort prompting guides](model-prompting/README.md) (Sol/Terra/Luna, Fable/Opus, Grok, Muse, Gemini, Live, image/video)
- [Surface and effort map](model-prompting/surface-and-effort-map.md)
- [Effort evaluation playbook](model-prompting/effort-evaluation-playbook.md)
- [Model source and observation ledger](model-prompting/sources-and-observations.md)
- [Frontier-model video research pack](../research/video-research-pack-2026-07-11.md)
- [Claude Fable 5 Max vs GPT-5.6 Sol](fable-vs-sol.md)
- [Live audio and translation models](live-audio-and-translation.md)

This folder contains the broad learning guides that sit between the repository landing page and the tool-specific docs. Use it when you want to improve prompting, agent task design, skill design, public-safe source use, or Windows-friendly command habits before choosing a specific coding agent.

## Recommended reading order

| Step | Guide | Use it for |
| ---: | --- | --- |
| 1 | [Comprehensive Prompt Engineering Guide](comprehensive-prompt-engineering-guide.md) | Full prompt-engineering curriculum: anatomy, techniques, context, agents, tools, RAG, evals, security, compression, image prompting, repository management, and templates. |
| 2 | [Prompting AI Coding Agents](prompting-ai-coding-agents.md) | Work-order prompts, context control, verification, and anti-patterns for coding agents. |
| 3 | [Prompt Engineering Playbook](prompt-engineering-playbook.md) | General prompt anatomy, examples, and reusable prompt structure. |
| 4 | [Prompt Audit Checklist](prompt-audit-checklist.md) | Reviewing prompts for scope, safety, evidence, and output quality. |
| 5 | [Coding Agent Power Tips](coding-agent-power-tips.md) | Tool-specific habits for Codex, Claude Code, Cursor, Copilot, Aider, Windsurf, and MCP. |
| 6 | [Skills and Prompt Guides](skills-and-prompt-guides.md) | Designing reusable skills, slash-command style prompts, and prompt-guide folders. |
| 7 | [Prompting References](prompting-references.md) | Public sources to learn from without copying private or leaked prompt content. |
| 8 | [Source-Inspired Prompting Curriculum](source-inspired-prompting-curriculum.md) | How to turn public guides and archived GitHub downloads into original, tested repository content. |
| 9 | [Agentic Coding Playbook](agentic-coding-playbook.md) | End-to-end agent task lifecycle patterns. |
| 10 | [Windows Setup Commands](windows-setup-commands.md) | PowerShell-friendly setup and validation commands. |

## Related sections

- Codex goal workflow: [../codex/00-start-here.md](../codex/00-start-here.md)
- Tool comparison: [../tools/comparison-matrix.md](../tools/comparison-matrix.md)
- Skills docs: [../skills/README.md](../skills/README.md)
- Image-generation docs: [../image-generation/README.md](../image-generation/README.md)
- Public repository safety: [../workflows/public-repo-safety.md](../workflows/public-repo-safety.md)
- Source and publication policy: [../research/source-policy.md](../research/source-policy.md), [../publication-policy.md](../publication-policy.md)

## How To Use These Guides

Start with the broad guide only when you need the full mental model. If you
already have a concrete repository task, read the coding-agent guide, copy the
closest prompt template, and add the exact files, checks, and success criteria
for your task. The goal is not to produce longer prompts; the goal is to give an
agent enough bounded context to make a small, reviewable change.

For beginner workshops, pair each guide with a tiny exercise:

| Exercise | Good file type | Verification |
| --- | --- | --- |
| Improve a prompt | Markdown prompt template | Peer review against the audit checklist |
| Update a doc | Markdown guide | `python scripts/repo_health_check.py` |
| Review a workflow | GitHub Actions doc | Manual checklist, no workflow edit |
| Package docs | Release docs | Manifest spot-check |

## Maintenance Notes

When adding a new guide, make sure it has a clear home in the reading order. If
it overlaps with an existing guide, either link to the existing material or make
the difference explicit. Avoid creating parallel instructions for the same
workflow unless the new guide serves a distinct audience.

Each guide should answer:

- What task does this help with?
- What should the reader do before using an agent?
- What files or inputs does the agent need?
- What checks prove the work is complete?
- What should remain manual or human-reviewed?

## Safety notes

- Treat external prompt collections as inspiration for structure, not text to copy.
- Do not publish leaked prompts, copied prompt dumps, private conversations, or private files.
- Mark fast-changing product behavior for official-doc verification.
- Keep automation examples preview-first and human-reviewed; do not frame them as safe to run blindly.

## Review Checklist

- [ ] The guide uses public-safe examples.
- [ ] It does not include private paths, account URLs, secrets, or logs.
- [ ] It points to official docs for fast-changing behavior.
- [ ] It includes practical commands or checklists rather than vague advice.
- [ ] It fits the beginner-first tone of the repository.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/guides/README.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `README` state what decision, workflow, or reusable behavior it supports?
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
