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
