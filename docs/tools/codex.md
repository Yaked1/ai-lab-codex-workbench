# OpenAI Codex

## What It Is

OpenAI Codex is a coding-agent workflow for reading a repository, editing files, running commands, explaining changes, and preparing work for review. In this repository, Codex is the reference workflow because the project is built around `AGENTS.md`, goal-style prompts, branch discipline, checks, PR review, and public-safety rules.

Codex-related product surfaces and names can change. Treat installation, subscription, model, cloud, IDE, and CLI details as claims to verify in official OpenAI documentation before publishing setup instructions.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| Documentation improvement | Strong | Give exact files, audience, and structure. |
| Bug fix with tests | Strong | Ask Codex to inspect relevant tests before editing. |
| Small feature | Strong | Keep feature scope narrow and require local checks. |
| PR review | Strong | Use read-only review prompts when possible. |
| Repository cleanup | Medium | Limit to deterministic cleanup or specific docs. |
| Large architecture rewrite | Weak at first | Break into design, tests, and small implementation PRs. |

## Beginner Friendliness

Medium. Codex is approachable after a learner understands:

- Git branches.
- `git diff`.
- Local checks.
- Pull requests.
- The difference between an agent summary and the real file diff.

Beginners should start with one Markdown file and one branch. Do not begin with dependency upgrades, workflow rewrites, or broad refactors.

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| CLI | Git-first local repository work. | Good for this repo when PowerShell and Git are already familiar. |
| IDE | When visible file context and editor review matter. | Verify current official IDE guidance. |
| Web/cloud | When work should happen outside a limited laptop. | Confirm current behavior and permission model. |
| Hybrid | Local repo plus cloud or IDE assistance. | Keep the branch and PR review path clear. |

## Windows Suitability

Good for this repository's Windows PowerShell workflow. Keep commands simple:

```powershell
git status
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Avoid requiring WSL, Docker, or local model hosting for basic Codex learning tasks.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Lightweight for docs, scripts, tests, and Git workflows. |
| API/account | Verify current account, plan, model, and authentication requirements in official docs. |
| Docker | Not needed for this repo. |
| WSL | Not needed for this repo. |
| GPU | Not needed. |

## Best First Task

Ask Codex to improve one paragraph in `README.md`, then run the three local checks. The task should fit in one PR and should not modify workflow YAML.

## Prompt Template

```text
Objective:
Improve the beginner clarity of one section in README.md.

Instructions:
- Read AGENTS.md first.
- Run git status.
- Inspect README.md before editing.
- Edit only the selected section.
- Keep claims conservative.
- Do not add dependencies.

Success criteria:
- The section is clearer for a first-time user.
- No unrelated files changed.
- These checks pass:
  - python scripts/repo_health_check.py
  - python scripts/safe_autofix.py --check
  - python -m unittest discover -s tests

Final report:
- Summary
- Files changed
- Commands run
- Checks run
- Remaining risks
```

## Safety Risks

- Edits can spread outside the intended scope if the prompt is vague.
- Command execution can change files or local state.
- Summaries may omit important details from the diff.
- Product behavior may change faster than repository docs.
- Tool integrations, skills, subagents, hooks, and MCP servers can expand permissions.

## Review Checklist

- [ ] Did Codex read `AGENTS.md`?
- [ ] Is the branch focused?
- [ ] Does the diff solve the requested task?
- [ ] Were unrelated files avoided?
- [ ] Were local checks run?
- [ ] Are failures fixed or honestly reported?
- [ ] Are external claims marked for official verification?
- [ ] Is the final report consistent with the actual diff?

## When To Avoid It

Avoid Codex for:

- Tasks involving secrets or private browser profiles.
- Unbounded whole-computer cleanup requests.
- Major dependency upgrades without a tested plan.
- Broad architecture rewrites without human design review.
- Production operations where a wrong command has immediate external impact.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Cursor | You want an IDE-first review loop. |
| Claude Code | You want a second-opinion review or documentation critique. |
| GitHub Copilot coding agent | You want GitHub issue-to-PR cloud workflow. |
| Aider | You want terminal pair programming with explicit files. |
| MCP | You need controlled access to external docs or tools. |

## Verification Notes

Use official docs for current Codex installation, authentication, model access, configuration, skills, subagents, `AGENTS.md`, IDE/cloud support, permissions, and pricing. This repository intentionally avoids exact pricing and feature availability claims.

## Claims To Verify In Official Docs

- Current Codex install and authentication flow.
- Supported operating systems and shells.
- Current CLI, IDE, web, and cloud behavior.
- `AGENTS.md` loading and scope rules.
- Skills, subagents, hooks, configuration, and MCP support.
- Permission prompts and sandboxing behavior.
- Current models, limits, pricing, and availability.

Official docs:

- <https://developers.openai.com/codex/cli>
- <https://developers.openai.com/codex/guides/agents-md>
