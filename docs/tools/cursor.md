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

## What Cursor Is Good At Vs. Not

Good at:

- Fast, visible-diff editing inside an IDE you likely already know if you
  come from VS Code.
- Codebase chat and explanation before you commit to an edit.
- Project rules that keep every new chat aligned with repo conventions
  without retyping them.
- MCP experiments where you want to see tool calls happen inside the editor.

Not good at:

- Terminal-only reproducibility. If your workflow needs to be scriptable and
  headless (CI, batch jobs), Cursor's IDE-first model is the wrong shape;
  reach for Codex CLI or Aider instead.
- Guaranteeing a diff was actually read. An IDE making a change look tidy is
  not the same as a human having reviewed it — this is Cursor's single
  biggest beginner trap.
- Very large refactors in one pass. Multi-file agent edits are easiest to
  review when scoped to a handful of files at a time.

## Beginner Friendliness

High for users familiar with VS Code-style editors. The main beginner risk is accepting a generated multi-file diff without reading it. Use Cursor as an assistant, not as an automatic merge button.

## Using This Repository's Workflow With Cursor

- Prompt template: [prompts/cursor/agent-task.md](../../prompts/cursor/agent-task.md).
- Local rules: Cursor's own convention for repo-specific rules is commonly
  referred to as project rules (historically `.cursorrules`, more recently a
  `.cursor/rules` directory with individual rule files). Verify the current
  exact filename and format in official docs, since this has changed between
  product versions. Whichever form is current, mirror the scope and safety
  content already in this repo's `AGENTS.md` so Cursor chats start aligned
  without you repeating it every session.
- Use `@`-context to attach `AGENTS.md` and the specific target file directly
  in the chat rather than trusting the agent to find them via indexing.

## Task Intake Worksheet

Cursor is easiest to use safely when the task is written before the chat
starts.

| Intake item | What to decide |
| --- | --- |
| Goal | One sentence that names the intended result, not just "improve this." |
| Files | Exact files to attach with `@` or open in the editor. |
| Mode | Ask/plan mode first for anything beyond a tiny edit; agent mode only after the plan is clear. |
| Context | `AGENTS.md`, the target file, and directly related tests or templates. |
| Out of scope | Files, folders, generated artifacts, workflow YAML, dependencies, and private data that must not change. |
| Verification | Commands to run in the terminal and any manual UI or diff review required. |
| Cost/plan risk | Any model, usage limit, premium request, extension, or MCP server behavior that depends on the current account plan. |

For beginner work, the best task is "explain this file, propose one small
change, then wait." That sequence separates learning from editing.

## Context Selection Rules

Cursor's workspace index and `@`-context are useful, but they can also pull a
task wider than intended.

- Attach `AGENTS.md` and the target file explicitly before asking for edits.
- Use `@` references for the smallest complete context instead of relying only
  on broad codebase search.
- Start a fresh chat for each unrelated task so old instructions and file
  attachments do not carry over.
- Do not attach secrets, `.env` files, private notes, logs with account data,
  browser profiles, generated archives, or screenshots containing private
  information.
- If Cursor proposes a change to an unmentioned file, require a short reason
  and approve the scope expansion before accepting the hunk.
- For MCP experiments, list the server tools the chat may use and prefer
  read-only servers until permissions are understood.

## Beginner Workflow Guidance

Use this pattern for a first Cursor agent run:

1. Open only the repository folder, not a parent folder containing unrelated
   private projects.
2. Ask Cursor to explain the target file and identify the smallest useful
   edit.
3. Ask for a plan before applying changes.
4. Accept or reject each hunk in the diff view deliberately.
5. Run local checks in PowerShell or Cursor's terminal.
6. Review `git diff` outside the chat before committing.

The IDE makes generated edits feel polished. Do not let that replace line by
line review.

## Example Workflow: Task Intake To PR

1. **Task intake.** Pick one file and one outcome ("clarify section X in
   `docs/tools/cursor.md`").
2. **Scoped prompt.** Use
   [prompts/cursor/agent-task.md](../../prompts/cursor/agent-task.md),
   attaching `AGENTS.md` and the target file with `@`-context.
3. **Agent work.** Ask for a short plan first (plan/ask mode) before letting
   Cursor apply edits.
4. **Local checks.** Run in Cursor's integrated terminal or your own shell:

   ```powershell
   python scripts/repo_health_check.py
   python scripts/safe_autofix.py --check
   python -m unittest discover -s tests
   ```

5. **Diff review.** Read the diff view Cursor renders inline, line by line,
   before accepting.
6. **PR.** Push the branch and open a PR; do not let editor-level "accept"
   substitute for the PR review step.

## Troubleshooting

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Agent edits files you never mentioned | Codebase indexing pulled in "related" files without being asked. | Restrict scope explicitly in the prompt; reject unrelated hunks in the diff view. |
| Chat seems to "forget" earlier instructions | Context window filled with long chat history or large attached files. | Start a fresh chat for a new task instead of extending one indefinitely. |
| Extension or agent mode doesn't activate | Editor needs a restart after install/update, or the feature is gated behind a setting. | Restart the editor and check current settings/docs for the feature flag. |
| Indexed codebase search returns stale results | Index has not refreshed after a large external change (e.g. `git pull`). | Trigger a re-index per current docs, or restart the editor. |
| MCP server exposes more than expected | Server was added with default/broad permissions. | Review the server's declared tools before connecting; prefer read-only servers first. |
| Rules file seems ignored | Wrong filename/format for the current product version. | Verify the current rules-file convention in official docs; old tutorials may reference a deprecated format. |

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

## Permissions And Defaults

By default, Cursor indexes and can read the workspace you open, and agent
mode can propose edits across any file it can see. Scope it down by opening
only the folder you intend to work in (not a parent directory containing
other private projects), reviewing diffs before accepting, and treating MCP
servers as opt-in, read-only by default.

## Permission, Cost, And Data Guardrails

| Risk | Practical control |
| --- | --- |
| Workspace overexposure | Open the repository folder only; keep parent folders with private projects closed. |
| Broad agent edits | Require a plan and accept hunks manually for multi-file changes. |
| Premium or metered usage | Verify current plan, model, request limits, and paid-feature behavior before a workshop or long run. |
| MCP data access | Review each MCP server's tools and permissions; start read-only. |
| Rules drift | Confirm the current rules-file format in official docs before teaching setup. |
| Unreviewed terminal commands | Read commands before approval and run repository checks yourself when uncertain. |

Public-facing docs should avoid exact claims about Cursor pricing, model
routing, feature availability, or extension behavior unless verified in
current official docs.

## When To Prefer Cursor Over Other Tools In This Guide

Prefer Cursor when you want an IDE-first loop with visible diffs, project
rules, and `@`-context in one place, especially if you already think in
VS Code terms. Prefer Aider or Codex CLI instead when you need a
terminal-only, scriptable workflow, or Claude Code when you want a
read-only second-opinion review outside the editing surface.

## Safety Risks

- Large diffs can look safe because they appear in an editor.
- Rules, chat history, indexed code, and MCP context can interact in confusing ways.
- MCP servers can expose more data than intended.
- Current pricing, model, and feature behavior may differ from old tutorials.

## Review Checklist

- [ ] Did Cursor explain the relevant files before editing?
- [ ] Was the plan narrow?
- [ ] Were `AGENTS.md` and the target files attached or otherwise read?
- [ ] Was the workspace limited to the intended repository?
- [ ] Were generated diffs reviewed before acceptance?
- [ ] Did the change stay inside the requested files?
- [ ] Were checks run after edits?
- [ ] Are third-party claims conservative?

## Final Report Expectations

Ask Cursor for a final report that includes:

- Exact files changed and whether any scope expansion was approved.
- The plan it followed, summarized in a few bullets.
- Commands run, including checks that could not be run inside the IDE.
- Any MCP servers, external context, or model/provider assumptions used.
- Product behavior, pricing, or platform claims that still need official-doc
  verification.
- Remaining risks for the human reviewer, especially large diffs or skipped
  tests.

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
