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

## Operating Modes

Codex can be used in several practical modes. The exact product surfaces can change, so verify current setup details in official OpenAI docs before publishing instructions.

| Mode | Best for | Review habit |
| --- | --- | --- |
| Chat or planning | Understanding a task, drafting a prompt, reviewing a design. | Treat output as advice until checked against files. |
| Local repo editing | Focused docs, scripts, tests, and small features. | Inspect `git diff` and run local checks. |
| Goal-style work | Multi-step tasks that need persistence and verification. | Keep success criteria concrete and evidence-based. |
| PR review | Finding bugs, missing tests, safety issues, and documentation gaps. | Ask for findings first and verify line references. |
| Cloud or remote workflow | Work that benefits from offloading compute or keeping a laptop light. | Confirm permissions, branch state, and PR output. |

The safest beginner mode is local repo editing on a short branch with a named file scope.

## Beginner Friendliness

Medium. Codex is approachable after a learner understands:

- Git branches.
- `git diff`.
- Local checks.
- Pull requests.
- The difference between an agent summary and the real file diff.

Beginners should start with one Markdown file and one branch. Do not begin with dependency upgrades, workflow rewrites, or broad refactors.

## Task Sizing

Codex works best when the task has enough context to be useful and enough boundaries to stay reviewable.

| Task shape | Good prompt boundary |
| --- | --- |
| One docs section | Name the file, audience, required section, and checks. |
| One script bug | Provide reproduction, expected behavior, relevant test, and allowed files. |
| One prompt template | Require target tool, purpose, full prompt, short version, inputs, criteria, safety, verification, report, and failure cases. |
| One review | Make it read-only and ask for findings ordered by severity. |
| Multi-file guide update | Name every file allowed and require a changelog entry. |

Avoid prompts that say "fix anything" unless the first output is a plan and no edits are made.

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

## Repository Workflow

In this repo, a typical Codex task should look like this:

```powershell
git status
git switch -c agent/<short-task-name>
```

Then the prompt should ask Codex to:

1. Read `AGENTS.md`.
2. Inspect relevant files before editing.
3. Keep changes inside the included scope.
4. Avoid secrets, dependency installs, workflow changes, deletion, and broad cleanup unless explicitly requested.
5. Run the three local checks when edits are complete.
6. Report files changed, commands run, checks run, claims needing verification, and remaining risks.

The reviewer then checks the diff and local check evidence before opening or merging a PR.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Lightweight for docs, scripts, tests, and Git workflows. |
| API/account | Verify current account, plan, model, and authentication requirements in official docs. |
| Docker | Not needed for this repo. |
| WSL | Not needed for this repo. |
| GPU | Not needed. |

## Trust Boundaries

Codex can operate across text, code, commands, and connected tools. Keep these boundaries explicit:

| Boundary | Safe default |
| --- | --- |
| Filesystem | Work inside the repository unless a maintainer explicitly approves otherwise. |
| Secrets | Never read, print, edit, or commit secrets. |
| Network | Use official docs for current product facts; avoid private services unless approved. |
| Commands | Prefer read-only and repo-local commands. Ask before destructive or system-wide commands. |
| Automation | Generated changes should open a reviewable PR, not merge themselves. |
| External tools | Start read-only and document permissions before enabling writes. |

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

## Common Failure Patterns

| Pattern | Risk | Correction |
| --- | --- | --- |
| Vague prompt | Large, unrelated diff. | Add included and excluded scope. |
| No checks requested | Final state is unverified. | List exact local commands in the prompt. |
| Trusting summary | Missed file changes or unsupported claims. | Review `git diff` directly. |
| Exact product claims | Docs become stale. | Link to official docs and qualify the claim. |
| Workflow edits bundled into docs task | Automation risk hidden in a broad PR. | Split workflow changes into a separate reviewed task. |
| Missing changelog | User-visible docs change is harder to audit later. | Add a factual `CHANGELOG.md` entry. |

## Reviewer Questions

Ask these before accepting Codex output:

- Did the task start from a known Git state?
- Did Codex inspect the relevant files before editing?
- Are all changed files expected?
- Does the diff solve the requested problem?
- Are local checks current for this diff?
- Are public-safety rules preserved?
- Are fast-changing external claims marked for official-doc verification?
- Is rollback straightforward?

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
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **tool guide** surface. During broad
maintenance, reviewers should treat `docs/tools/codex.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `codex` state what decision, workflow, or reusable behavior it supports?
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
