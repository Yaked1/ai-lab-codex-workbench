# Hermes Agent Vs Codex Vs Claude Code

This is a workflow-tool comparison, not a model comparison. It does not rank
underlying model quality, benchmarks, or pricing; it compares how each tool
behaves as an agent workflow surface inside this repository's safety rules.
See [docs/tools/comparison-matrix.md](../tools/comparison-matrix.md) for the
full multi-tool matrix this page extends, and [docs/tools/codex.md](../tools/codex.md)
for the fuller Codex-specific reference this page stays consistent with.

| Tool | Best fit in this repo | Review stance |
| --- | --- | --- |
| Hermes Agent | Public research organization, persistent local workflows, skills, memory, and automations after careful setup. | Treat as a powerful local/private agent. Keep memory and provider config out of Git. |
| Codex | Repository edits, checks, prompt-driven changes, and PR preparation. | Use branch, checks, review, and merge. Manual curator only. |
| Claude Code | Codebase explanation, skill-based workflows, documentation review, and multi-file agent work. | Verify current skill/setup behavior in official docs. |

## Strengths And Weaknesses Side By Side

| Dimension | Hermes Agent | Codex | Claude Code |
| --- | --- | --- | --- |
| Strength | Persistent memory and skills across many small personal tasks; scheduled/cron-style automations for private workflows. | Git-first editing loop tuned to branch, check, PR, review, merge; strong at goal-style multi-step repo tasks. | Strong multi-file codebase understanding, review, and critique; good second-opinion partner to Codex. |
| Weakness | Persistent state (memory, provider config, logs) is the opposite of the clean, stateless diff a public repo edit needs; not Git-first. | Vague prompts can produce overly broad diffs; still needs a human to verify the summary against the real `git diff`. | Verify current skill/subagent/setup behavior in official docs before teaching it; not designed as the repo's primary automation publisher either. |
| Best-fit task in this repo | Organizing public research candidates, drafting a private outline, personal scheduled reminders. | Editing one docs file or script, running the three local checks, preparing a PR. | Reviewing a diff or doc for clarity/safety issues without editing; explaining an unfamiliar part of the repo. |
| Weak-fit task in this repo | Any task whose output must become a reviewable, committed diff. | Broad "fix anything" requests with no named scope; unattended production operations. | Being treated as the tool that publishes generated content automatically. |
| Safety posture | Highest persistent-state risk: memory, OAuth, logs, and provider keys accumulate locally and must never enter Git. | Command execution and file edits mean diffs can drift outside scope if the prompt is vague; mitigated by branch/PR/checks discipline. | Lower persistent-state risk day to day, but skill and project-context behavior should still be verified before broad trust. |
| Windows suitability | Verify current desktop/CLI Windows support in official Hermes Agent docs; treat as medium until checked. | Good; this repo's PowerShell-first workflow (`git status`, the three check scripts) is the reference path. | Good; verify current Windows setup steps in official docs before teaching exact commands. |

## Key Differences

| Dimension | Hermes Agent | Codex | Claude Code |
| --- | --- | --- | --- |
| Normal shape | Ongoing agent workspace with tools, memory, skills, and automations. | Git-first coding agent workflow. | Coding agent workflow with skills and project context. |
| Public repo risk | Private memory, OAuth, logs, provider keys, scheduled automations. | Overbroad diffs, command execution, direct pushes if misconfigured. | Overbroad diffs, private project context, unverified skill behavior. |
| Best first task | Read a public candidate report and draft a local outline. | Improve one docs page and run checks. | Review one guide without editing. |
| Publishing rule | Never push directly to `main`. | Branch, PR, checks, review, merge. | Branch, PR, checks, review, merge. |

## When To Use Hermes Agent

- You want persistent local organization.
- You want agent memory for private personal workflows.
- You want scheduled local reminders or reviewed automations.
- You are comfortable separating private agent state from public repository docs.

## When To Use Codex

- You want repo-local edits.
- You need tests or checks run.
- You want a reviewed PR generated from a manual workflow.
- You want clear final reporting tied to changed files.

## When To Use Claude Code

- You want a codebase explanation or docs review.
- You are using Claude Code skills.
- You want a different coding-agent surface for comparison.

## Public Safety Rule

All three tools can produce useful drafts. None of them should publish public
guide content without human review.

## Decision Matrix

| Task | Prefer | Why |
| --- | --- | --- |
| Edit repository docs and run tests | Codex | Git-first workflow, diff review, local commands, final report. |
| Read-only documentation review | Claude Code or Codex | Strong fit for findings-first review and project context. |
| Organize recurring public research sources locally | Hermes Agent | Persistent workspace can help with source queues when private state is separated. |
| Create reusable skill workflow | Claude Code or Codex | Skill/instruction bundles are reviewable when kept public-safe. |
| Scheduled local reminder or personal workflow | Hermes Agent | Better fit for persistent local automations; keep private state out of Git. |
| Publish public release | None directly | Human maintainer should trigger release after checks and manifest review. |

## Comparison Boundaries

This page does not rank model quality. It compares workflow surfaces and public
repository risk. Model names, pricing, context windows, and platform support
change often and must be verified in official docs before procurement or
production decisions.

## Review Questions

- Does the task need persistent private memory? If yes, do not publish that
  state.
- Does the task need repository edits and tests? Use a Git-first agent flow.
- Does the task need a read-only review? Keep the tool in review mode.
- Does the task create public docs? Require source status, checks, and human
  review.
- Does the task involve provider credentials? Keep credentials out of Git and
  examples.

## Failure Modes

| Failure | Example | Repair |
| --- | --- | --- |
| Tool comparison becomes model comparison | Claims about Hermes model benchmarks appear. | Remove; this folder is Hermes Agent only. |
| Private memory is treated as public evidence | A guide cites local personal notes. | Replace with public sources or omit. |
| Agent pushes directly to `main` | Automation bypasses PR review. | Require branch, checks, PR, and human approval. |
| Setup claim goes stale | Install command changes upstream. | Mark for official-doc verification or update after checking. |
