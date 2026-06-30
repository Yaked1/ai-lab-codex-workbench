# Hermes Agent Vs Codex Vs Claude Code

This is a workflow-tool comparison, not a model comparison.

| Tool | Best fit in this repo | Review stance |
| --- | --- | --- |
| Hermes Agent | Public research organization, persistent local workflows, skills, memory, and automations after careful setup. | Treat as a powerful local/private agent. Keep memory and provider config out of Git. |
| Codex | Repository edits, checks, prompt-driven changes, and PR preparation. | Use branch, checks, review, and merge. Manual curator only. |
| Claude Code | Codebase explanation, skill-based workflows, documentation review, and multi-file agent work. | Verify current skill/setup behavior in official docs. |

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
