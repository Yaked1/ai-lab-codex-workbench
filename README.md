# AI Prompting and Coding Agent Workbench

A practical public guide for using AI assistants, coding agents, prompt templates, reusable skills, and image-generation prompts while keeping work reviewable, scoped, and safe to publish.

This repository gives you a simple operating system for AI-assisted work:

```text
clear task -> bounded context -> scoped agent work -> local checks -> diff review -> pull request -> human approval
```

It is not a prompt dump, a model-access service, a benchmark leaderboard, or a shortcut around product limits. It is a workflow and documentation workbench for making AI help useful, inspectable, and safe enough to publish.

## Use This Repository When You Want To

- Write better prompts for coding agents, research agents, document agents, and image models.
- Use Codex, Claude Code, or similar tools with clear task scope and review gates.
- Create reusable `AGENTS.md` instructions, goal prompts, skill files, and checklists.
- Keep public repositories free of secrets, private paths, leaked prompts, and unverifiable claims.
- Package documentation and prompt systems into reviewable release bundles.
- Teach beginners a safe path while still giving advanced users enough structure to audit the work.

## Start Here

| If you want to... | Open this first |
| --- | --- |
| Understand the repository rules | [AGENTS.md](AGENTS.md) |
| Start using Codex on this repo | [docs/codex/00-start-here.md](docs/codex/00-start-here.md) |
| Run a complete agent task | [docs/workflows/agent-task-lifecycle.md](docs/workflows/agent-task-lifecycle.md) |
| Pick a ready-to-use prompt | [prompts/codex/](prompts/codex/) |
| Learn prompt engineering deeply | [docs/guides/comprehensive-prompt-engineering-guide.md](docs/guides/comprehensive-prompt-engineering-guide.md) |
| Learn prompt engineering patterns | [docs/guides/prompt-engineering-playbook.md](docs/guides/prompt-engineering-playbook.md) |
| Learn agentic coding workflows | [docs/guides/agentic-coding-playbook.md](docs/guides/agentic-coding-playbook.md) |
| Compare AI coding tools | [docs/tools/comparison-matrix.md](docs/tools/comparison-matrix.md) |
| Work with image-generation prompts | [docs/image-generation/README.md](docs/image-generation/README.md) |
| Use the Prompting OS package | [docs/prompting-os/README.md](docs/prompting-os/README.md) |
| Review public-safety rules | [docs/workflows/public-repo-safety.md](docs/workflows/public-repo-safety.md) |

## Fast Path

For a normal documentation or prompt update:

1. Read [AGENTS.md](AGENTS.md).
2. Choose one target file or one narrow task.
3. Use a prompt template from [prompts/codex/](prompts/codex/).
4. Keep the agent inside the requested scope.
5. Run the validation commands.
6. Review the diff yourself.
7. Update [CHANGELOG.md](CHANGELOG.md) for user-visible changes.
8. Open a pull request instead of trusting an agent summary. Summaries are not evidence; diffs, checks, and source alignment are evidence.

## What Is Included

| Area | What it provides | Entry point |
| --- | --- | --- |
| Codex workflow docs | Start guide, goal workflow, branch/PR flow, safe autofix policy, review checklist, and roadmap. | [docs/codex/00-start-here.md](docs/codex/00-start-here.md) |
| Prompting And Agent Mastery | Comprehensive prompt engineering, prompt anatomy, context engineering, prompt audits, prompt compression, agent prompts, source-grounded prompting, evaluation, image prompting, and source-inspired curriculum. | [docs/guides/comprehensive-prompt-engineering-guide.md](docs/guides/comprehensive-prompt-engineering-guide.md) |
| Prompting guides | Prompt anatomy, context engineering, prompt audits, prompt compression, agent prompts, and source-inspired curriculum. | [docs/guides/README.md](docs/guides/README.md) |
| Tool guides | Practical notes for Codex, Claude Code, Cursor, Copilot, Aider, Windsurf, OpenCode, Kilo Code, MCP, and related tools. | [docs/tools/comparison-matrix.md](docs/tools/comparison-matrix.md) |
| Skills documentation | Claude Code skills, Codex skills, MCP tool-use systems, and reusable prompt-guide patterns. | [docs/skills/README.md](docs/skills/README.md) |
| Prompt templates | Goal-style work orders for documentation updates, repository cleanup, feature work, bug fixes, and PR review. | [prompts/codex/docs-update.goal.md](prompts/codex/docs-update.goal.md) |
| Image-generation docs | Diffusion prompting, autoregressive image prompting, local/cloud tradeoffs, hardware tiers, and prompt patterns. | [docs/image-generation/README.md](docs/image-generation/README.md) |
| Prompting OS | A modular framework for prompt kernels, model-family drivers, context engineering, skills, image prompting, and evaluation. | [docs/prompting-os/README.md](docs/prompting-os/README.md) |
| Automation docs | Local checks, research scout workflow, release packaging, release drafts, and strict automerge boundaries. | [docs/automation/repository-autopilot.md](docs/automation/repository-autopilot.md) |
| Hermes Agent docs | Nous Research Hermes Agent setup, provider configuration, prompting, skills, memory, automations, and troubleshooting. | [docs/hermes/README.md](docs/hermes/README.md) |
| Offline site | Plain HTML/CSS pages that can be opened locally without trackers, CDNs, analytics, or external assets. | [docs/site/index.html](docs/site/index.html) |
| Release packaging | Deterministic public release ZIPs and manifests for selected documentation and prompt assets. | [docs/releases-and-packages.md](docs/releases-and-packages.md) |

## The Core Workflow

Use this loop for almost every AI-assisted repository task:

```text
1. Intake
   Define the exact task, audience, allowed scope, excluded scope, and acceptance criteria.

2. Context
   Load only the files and instructions needed for the task. Separate facts from instructions.

3. Plan
   Ask for the smallest safe plan before edits. Large vague plans increase review risk and make failures harder to isolate.

4. Execute
   Edit only the target files. Do not add dependencies, secrets, private paths, or unrelated rewrites.

5. Verify
   Run the focused checks. If checks cannot run, report that clearly.

6. Review
   Inspect the diff, compare it against the acceptance criteria, and remove unsupported claims.

7. Publish
   Use a pull request, changelog entry, and human review before merging public-facing work.
```

## Validation Commands

Run these from PowerShell in the repository root:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

If deterministic formatting fixes are allowed for the task:

```powershell
python scripts/safe_autofix.py --write
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Then inspect the result:

```powershell
git status
git diff --stat
git diff
```

Do not claim these passed unless they actually ran. Final reports should distinguish completed checks from checks that were skipped, blocked, or failed.

### Claude Code `/goal` style workflow

If you use a `/goal` style workflow in Claude Code, define it as a user-created slash command in `.claude/commands/`; do not assume it is a built-in command in every tool. Keep the command as a reusable work order: objective, scope, safety boundaries, verification, and final report.

## Prompt Templates

Prompt templates live in [prompts/codex/](prompts/codex/). They are designed as practical work orders rather than generic advice.

Each serious prompt should define:

- Target tool.
- Purpose.
- Inputs to fill.
- Included scope.
- Excluded scope.
- Safety boundaries.
- Verification steps.
- Success criteria.
- Final report format.
- Failure behavior.

Start with these:

| Task | Template |
| --- | --- |
| Update documentation | [prompts/codex/docs-update.goal.md](prompts/codex/docs-update.goal.md) |
| Implement a feature | [prompts/codex/implement-feature.goal.md](prompts/codex/implement-feature.goal.md) |
| Fix a bug | [prompts/codex/fix-bug.goal.md](prompts/codex/fix-bug.goal.md) |
| Clean up repository docs or structure | [prompts/codex/repository-cleanup.goal.md](prompts/codex/repository-cleanup.goal.md) |
| Review a pull request | [prompts/codex/review-pr.goal.md](prompts/codex/review-pr.goal.md) |

## Public Safety Rules

Before publishing anything from this repository, check that it contains:

- No API keys, OAuth files, cookies, browser profiles, `.env` files, credentials, or secrets.
- No private repository links, private dashboards, private account IDs, private file paths, private logs, or personal data.
- No copied prompt dumps, leaked prompts, private system prompts, or license-unclear bulk imports.
- No exact claims about pricing, plan access, model availability, benchmarks, or platform support unless freshly verified in official documentation.
- No GitHub Actions workflow that calls paid LLMs, Codex, OpenAI API keys, or other model providers automatically.
- No heavy local AI stack presented as the beginner default.

Use these deeper references when in doubt:

- [Public repository safety](docs/workflows/public-repo-safety.md)
- [Publication policy](docs/publication-policy.md)
- [Security policy](SECURITY.md)
- [Research source policy](docs/research/source-policy.md)

## Repository Layout

```text
AGENTS.md                         Local rules for AI coding agents
README.md                         Public landing page
docs/codex/                       Codex start guide, goal workflow, PR flow, review, and roadmap
docs/guides/                      Comprehensive prompt engineering, agentic coding, audits, references, and Windows workflows
docs/tools/                       Tool-specific guides and comparison matrix
docs/skills/                      Claude Code, Codex, MCP, and prompt-guide skill documentation
docs/image-generation/            Diffusion, autoregressive, local/cloud, hardware, and image-prompting notes
docs/prompting-os/                Modular prompting framework, templates, evals, and source map
docs/automation/                  Research, local checks, automerge boundaries, and release draft policies
docs/hermes/                      Nous Research Hermes Agent workflow documentation
docs/site/                        Offline static documentation site
docs/releases/                    Release process and release notes
docs/templates/                   Task, merge, and release templates
prompts/codex/                    Goal-style Codex prompt templates
scripts/                          Standard-library helper, validation, research, and package scripts
tests/                            Unit tests for repository scripts and documentation checks
```

## Archive and Source Audits

The repository includes source-inspired material from public prompting, agent, and image-generation projects. Detailed archive and source information lives in linked documentation so the README can remain a navigational landing page.

Use these files for details:

- [Archive audit](docs/archive-audit.md)
- [Archive catalog](docs/archive-catalog.md)
- [Prompting references](docs/guides/prompting-references.md)
- [Prompting OS source map](docs/prompting-os/07-source-map.md)

Source-derived guidance should be rewritten into original, public-safe patterns. Do not bulk-import external text, leaked prompts, private content, or license-unclear material.

## What This Project Does Not Do

- It does not provide model accounts, API keys, subscriptions, or product access.
- It does not bypass AI product limits or plan restrictions.
- It does not publish private prompts, leaked system prompts, credentials, or private conversations.
- It does not treat AI-generated summaries as proof of correctness.
- It does not make GitHub Actions run paid LLM jobs.
- It does not claim fast-changing tool behavior is permanent.
- It does not require local model hosting, GPU-heavy infrastructure, Docker, or WSL for beginner use.

## Recommended Reading Order

For new users:

1. [AGENTS.md](AGENTS.md)
2. [docs/codex/00-start-here.md](docs/codex/00-start-here.md)
3. [docs/workflows/agent-task-lifecycle.md](docs/workflows/agent-task-lifecycle.md)
4. [docs/guides/comprehensive-prompt-engineering-guide.md](docs/guides/comprehensive-prompt-engineering-guide.md)
5. [docs/guides/prompting-ai-coding-agents.md](docs/guides/prompting-ai-coding-agents.md)
6. [docs/guides/prompt-engineering-playbook.md](docs/guides/prompt-engineering-playbook.md)
7. [docs/guides/coding-agent-power-tips.md](docs/guides/coding-agent-power-tips.md)
8. [docs/guides/prompting-references.md](docs/guides/prompting-references.md)
9. [docs/guides/source-inspired-prompting-curriculum.md](docs/guides/source-inspired-prompting-curriculum.md)
10. [docs/guides/agentic-coding-playbook.md](docs/guides/agentic-coding-playbook.md)
11. [prompts/codex/docs-update.goal.md](prompts/codex/docs-update.goal.md)

For maintainers:

1. [docs/workflows/public-repo-safety.md](docs/workflows/public-repo-safety.md)
2. [docs/publication-policy.md](docs/publication-policy.md)
3. [docs/automation/repository-autopilot.md](docs/automation/repository-autopilot.md)
4. [docs/releases-and-packages.md](docs/releases-and-packages.md)
5. [CONTRIBUTING.md](CONTRIBUTING.md)
6. [SECURITY.md](SECURITY.md)

## Contributing

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Good contributions are:

- Narrow in scope.
- Public-safe.
- Easy to review.
- Linked to a real task or reader need.
- Validated with the repository checks.
- Honest about what was not verified.

Every user-visible documentation or workflow change should include a changelog entry when useful. Pull requests should explain what changed, why it changed, what commands ran, what passed or failed, and what still needs manual verification.
