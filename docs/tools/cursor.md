# Cursor

## What It Is

Cursor is an AI-focused code editor with codebase chat, agent workflows, project rules, visible diffs, and optional integrations such as MCP depending on the current product surface. It is a good fit for learners who prefer an IDE-style environment over a terminal-first agent.

Cursor product details change quickly. Verify installer, account, CLI, plan, model, and feature claims in official docs.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| Planning a small issue | Strong | Use plan mode or ask for steps before edits. |
| Explaining code in the editor | Strong | Good for beginners learning file structure. |
| Small visible edits | Strong | Review the diff before accepting. |
| Rules-based project guidance | Medium | Keep rules short and repo-specific. |
| MCP experiments | Medium | Start with read-only servers. |
| Large refactor | Medium to weak | Split into reviewable PRs. |

## Beginner Friendliness

High for users familiar with VS Code-style editors. The main beginner risk is accepting a generated multi-file diff without reading it. Use Cursor as an assistant, not as an automatic merge button.

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| IDE | Primary path for editor-based development. | Best fit for first use. |
| CLI | Useful if current docs support it for project workflows. | Verify before teaching. |
| Hybrid | IDE plus GitHub PR review. | Keep branches and checks explicit. |
| MCP | Tool/data extension path. | Start read-only. |

## Windows Suitability

Good for Windows desktop use when the current installer supports the machine. This repo's workflows stay lightweight and avoid requiring WSL or Docker.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Editor plus Git and Python checks should fit a limited laptop. |
| API/account | Verify current account, plan, model, and provider behavior. |
| Docker | Not needed for this repo. |
| WSL | Not needed for basic docs and scripts. |
| GPU | Not needed. |

## Best First Task

Ask Cursor to create a plan for improving one documentation file. Review the plan, then approve only the smallest useful edit.

## Prompt Template

```text
Target tool: Cursor

Task:
Improve one documentation section in [file].

Instructions:
- Read AGENTS.md first.
- Inspect the target file before editing.
- Propose a short plan before applying changes.
- Edit only the selected section unless I approve more.
- Keep external tool claims conservative.

Validation:
- Run or ask me to run:
  - python scripts/repo_health_check.py
  - python scripts/safe_autofix.py --check
  - python -m unittest discover -s tests

Final report:
- Files changed
- Summary
- Checks run
- Remaining risks
```

## Safety Risks

- Large diffs can look safe because they appear in an editor.
- Rules, chat history, indexed code, and MCP context can interact in confusing ways.
- MCP servers can expose more data than intended.
- Current pricing, model, and feature behavior may differ from old tutorials.

## Review Checklist

- [ ] Did Cursor explain the relevant files before editing?
- [ ] Was the plan narrow?
- [ ] Were generated diffs reviewed before acceptance?
- [ ] Did the change stay inside the requested files?
- [ ] Were checks run after edits?
- [ ] Are third-party claims conservative?

## When To Avoid It

Avoid Cursor for:

- Repositories where the IDE should not index sensitive files.
- Broad generated refactors without a review plan.
- Work where terminal-only reproducibility is required.
- MCP experiments connected to private services before permissions are understood.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Codex | You want a Git-first local agent workflow. |
| GitHub Copilot | You want in-editor suggestions or GitHub cloud agent PRs. |
| Windsurf | You want another IDE-agent comparison point. |
| Aider | You want explicit files in a terminal session. |

## Verification Notes

Verify current product names, installer behavior, CLI support, agent modes, rules format, MCP support, pricing, and model access in official docs.

## Claims To Verify In Official Docs

- Current Windows installer and supported versions.
- Current agent, plan, rules, and chat behavior.
- CLI availability and commands.
- MCP support and permission model.
- Model/provider options, limits, and pricing.

Official docs:

- <https://cursor.com/docs>
