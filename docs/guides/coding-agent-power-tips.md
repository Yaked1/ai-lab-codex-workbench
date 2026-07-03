# Coding Agent Power Tips

Tool-specific tricks for getting more out of popular AI coding agents. Pair this
with the tool-agnostic [Prompting AI coding agents](prompting-ai-coding-agents.md)
guide: the techniques there are the load-bearing skills; the features below only
amplify them.

> Feature names, flags, and defaults change often. Everything here is a pointer
> to confirm in official docs, not a fixed promise. Official links are collected
> in [prompting-references.md](prompting-references.md) and on each tool page
> under [docs/tools/](../tools/). This guide states no pricing, plan, or model
> claims on purpose.

## Cross-Agent Habits (Learn These First)

These habits matter more than any single feature:

1. **Write a memory/rules file.** Every serious agent reads a persistent
   instructions file (`AGENTS.md`, `CLAUDE.md`, project rules). Putting your
   conventions, commands, and "never do" lines there beats repeating them in
   every prompt.
2. **Plan before acting on anything non-trivial.** Ask for a plan, review it,
   approve it. The plan is the cheapest place to fix a wrong approach.
3. **Keep approvals tight by default.** Start every tool in its most restrictive
   permission mode. Loosen only for trusted repos and specific workflows.
4. **Make it verify.** Ask the agent to run tests and checks and paste output.
   Never accept "done" without evidence.
5. **Start fresh per task.** A clean context window beats a long, polluted one.
6. **Use sub-agents / parallel runs for independent work.** Delegating scoped
   investigations keeps your main context clean and lets independent units run
   at once.
7. **Connect tools through MCP carefully.** The Model Context Protocol lets
   agents reach external tools and data. Start read-only, in a test repo, before
   granting write access or private-data access.

## Claude Code

Official docs: <https://docs.anthropic.com/en/docs/claude-code/overview>

| Capability | What it does | How to use it well |
| --- | --- | --- |
| `CLAUDE.md` memory | Project/personal instructions read each session. | Keep it short and high-signal. If Claude already does something right, delete the rule. Convert repeated fix-ups into hooks. |
| Custom slash commands | Markdown files in `.claude/commands/` become `/command`. | Save reusable workflows as commands. For example, a `.claude/commands/goal.md` file lets you run `/goal` to pin a task for the session. Personal commands live in `~/.claude/commands`. These are commands you define, not built-ins. |
| Plan mode | Plan before editing. | Use it for any multi-file or risky change; approve the plan, then let it execute. |
| Extended thinking | Ask it to "think" for harder problems. | Documented budgets escalate roughly `think` < `think hard` < `think harder` < `ultrathink`. Use more for architecture and tricky bugs, less for mechanical edits. |
| Subagents | Delegate scoped investigations or parallel work. | Send exploration to a subagent so it does not consume your main context. |
| Agent Skills | Packaged, reusable capabilities and instructions. | Use skills for repeatable domain tasks instead of re-prompting from scratch. |
| MCP | Connect external tools and data sources. | Add read-only servers first; review what each server can do before write access. |
| Hooks | Run your own commands on agent events. | Enforce rules deterministically (formatting, checks) instead of asking each time. |
| `/clear` and fresh sessions | Reset context. | Clear between unrelated tasks to avoid context drift. |
| Headless / print mode | Run non-interactively for scripts and CI. | Good for batch jobs and pipelines once a prompt is trusted. |

Power moves:

- Turn your most-repeated instruction into a `CLAUDE.md` line or a hook, not a
  sentence you retype.
- Build a small library of custom slash commands for your common loops.
- Use a subagent to investigate a bug while the main session keeps building.

## OpenAI Codex

Official docs: <https://developers.openai.com/codex/cli> and
<https://developers.openai.com/codex/learn/best-practices>

| Capability | What it does | How to use it well |
| --- | --- | --- |
| `AGENTS.md` | Durable instructions Codex reads before work. | Layer global guidance (in the Codex home dir) with per-repo `AGENTS.md`. Codex reads `AGENTS.override.md` first if present. |
| Approval modes | Control how much runs without confirmation. | Start in read-only/consultative mode; it browses and proposes a plan. Reserve full access for trusted repos and tasks. |
| CLI, IDE, and cloud surfaces | Run locally, in an editor, or remotely. | Match the surface to the task; keep branch state and PR output reviewable wherever it runs. |
| Verify loop | Ask it to test and check its own work. | Tell it what "good" looks like via the prompt or `AGENTS.md`: write tests, run checks, confirm, then review. |
| MCP and subagents | Extend tools; delegate scoped work. | Same caution as any agent: tight permissions, read-only first. |

Power moves:

- Encode "always run the test suite and report results" in `AGENTS.md` so every
  task gets a verification loop for free.
- Keep approval and sandboxing tight by default; loosen per-repo only when the
  need is clear.

## Cursor

Official docs: <https://cursor.com/docs>

| Capability | How to use it well |
| --- | --- |
| Project rules | Store conventions and guardrails so every chat starts aligned. |
| `@`-context | Attach the exact files, folders, or docs the task needs; do not rely on the agent guessing. |
| Plan / ask before apply | Review proposed edits as diffs before accepting. |
| MCP | Connect controlled tools; prefer read-only in shared or private repos. |

## GitHub Copilot

Official docs: <https://docs.github.com/en/copilot>

| Capability | How to use it well |
| --- | --- |
| Custom instructions | Add repo-level instructions so suggestions and agent work match your conventions. |
| Agent / coding-agent mode | Scope issues tightly; review the generated PR like any contributor's. |
| Issue-to-PR flow | Give the issue clear acceptance criteria so the agent has a definition of done. |
| In-editor review | Treat completions as drafts, not truth; verify before commit. |

## Aider

Official docs: <https://aider.chat/docs/>

| Capability | How to use it well |
| --- | --- |
| Explicit file adds | Add only the files in scope so edits and the repo map stay focused. |
| Conventions file | Keep style and command guidance the agent reads each run. |
| Architect/edit separation | Plan the change, then apply it, for cleaner diffs. |
| Git-native commits | Review each commit; the small-commit habit keeps changes reversible. |

## Windsurf

Official docs: <https://docs.windsurf.com/windsurf/cascade>

| Capability | How to use it well |
| --- | --- |
| Codebase context | Ask for an explanation of a folder before requesting edits. |
| Multi-file edits | Keep tasks scoped; review the full diff across files. |
| Rules / memory | Store project conventions so sessions stay consistent. |

## MCP (Model Context Protocol)

Official docs: <https://modelcontextprotocol.io/docs/getting-started/intro>

MCP is how agents connect to external tools, data, and prompts. It is powerful
and therefore the highest-risk surface in this list.

Safe defaults:

- Start with a **read-only** server in a **test repo**.
- Review exactly what each server can read and do before connecting it to real
  work or private data.
- Do not connect write-capable or private-data servers until you trust them and
  understand the permission model.
- Keep secrets out of MCP configs that get committed.

See [docs/tools/mcp.md](../tools/mcp.md) and
[docs/workflows/public-repo-safety.md](../workflows/public-repo-safety.md).

## Choosing Effort And Surface

| Situation | Reach for | Avoid |
| --- | --- | --- |
| One-line or mechanical edit | Low effort, direct prompt. | Maximum reasoning, big plans. |
| Tricky bug or architecture | Plan-first, higher reasoning effort, maybe a subagent. | One-shot "just fix it." |
| Multi-file change | Decompose; plan; review diffs per phase. | One giant prompt. |
| Anything touching secrets or prod | Tight approvals; human in the loop. | Full-access modes. |
| Repeated workflow | A custom command, skill, or rules-file entry. | Retyping the same prompt. |

## Safety Reminders

- Keep agents inside the repository so private folders are not exposed.
- Never paste secrets into a prompt or commit them to a memory/rules file.
- Prefer the most restrictive permission mode that still gets the job done.
- Review every diff. Tool autonomy does not remove human review.
- Verify fast-changing feature claims in official docs before relying on them.

## Where To Go Next

- [Prompting AI coding agents](prompting-ai-coding-agents.md) — the underlying craft.
- [Prompting references](prompting-references.md) — public resources to learn from.
- [Tool guides](../tools/) — per-tool pages with conservative comparisons.
- [Comparison matrix](../tools/comparison-matrix.md) — orientation across tools.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/guides/coding-agent-power-tips.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `coding agent power tips` state what decision, workflow, or reusable behavior it supports?
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
