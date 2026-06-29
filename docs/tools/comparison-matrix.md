# AI Coding Tool Comparison Matrix

This matrix is a beginner-oriented comparison for safe AI coding workflows. Tool capabilities, pricing, plan limits, authentication flows, and platform support change quickly. Verify official documentation before publishing workshop material or making a purchasing decision.

## Quick Comparison

| Tool | Primary use | Beginner friendliness | Windows suitability | Local, cloud, IDE, CLI, or hybrid | Main risks | Best first task |
| --- | --- | --- | --- | --- | --- | --- |
| OpenAI Codex | Local repo editing, test-running, docs updates, PR prep. | Medium. | Good with PowerShell and Git. | CLI, IDE, web, hybrid. | Broad file edits, command execution, stale assumptions. | Improve a README sentence and run checks. |
| Claude Code | Codebase analysis, docs review, multi-file agent work. | Medium. | Good; verify current installer and shell guidance. | CLI, IDE, desktop, web, hybrid. | Scope creep, permissions, costs, changing surfaces. | Review one doc and propose edits. |
| Cursor | IDE agent planning, code edits, chat, rules, MCP. | High for VS Code-style users. | Good. | IDE, CLI, hybrid. | Large accepted diffs, weak review, hidden context gaps. | Ask for a plan before edits. |
| Google Antigravity | Agent-first project orchestration and artifacts. | Medium. | Verify current support. | IDE, CLI, cloud/hybrid. | Preview behavior, parallel-agent drift, unclear permissions. | Produce a plan artifact for a docs issue. |
| GitHub Copilot / Copilot coding agent | IDE assistance, GitHub cloud agent work, PRs. | High for suggestions; medium for autonomous work. | Good through supported IDEs and GitHub. | IDE, cloud, hybrid. | Generated PRs without review, plan/account differences. | Let it draft a tiny docs PR. |
| OpenCode | Open-source terminal, desktop, or IDE agent workflows. | Medium. | Verify current Windows install path. | CLI, desktop, IDE, hybrid. | Provider setup, command permissions, model costs. | Ask for a read-only repo overview. |
| Kilo Code | Open-source agent across IDE, CLI, and cloud-style surfaces. | Medium. | Good where the selected surface is supported. | IDE, CLI, cloud, hybrid. | Provider setup, cost, tool permissions. | Use planning mode on a small issue. |
| Aider | Terminal pair programming with explicit repo files. | Medium. | Good with Python and Git. | CLI, local/hybrid. | Editing too many files, automatic commits if enabled. | Edit one specified Markdown file. |
| Windsurf | IDE-based agentic coding assistance. | High for editor-first learners. | Good if current desktop product supports the setup. | IDE, hybrid. | Product branding changes, large diffs, extension trust. | Ask for a folder explanation. |
| MCP servers | Connect agents to tools, data, prompts, and workflows. | Low to medium. | Good for lightweight local servers. | Protocol, local/cloud server, hybrid. | Tool injection, secrets exposure, unsafe write tools. | Add a read-only docs or filesystem server in a test repo. |

## How to Choose

Choose by task shape, not by hype:

- Use a CLI agent when you want a Git-first, terminal-first workflow.
- Use an IDE agent when you want visible file context, inline diffs, and editor review.
- Use a cloud agent when local hardware is weak or the work should happen in GitHub-hosted infrastructure.
- Use MCP only after you understand the permissions and data exposure of every connected server.
- Use skills, rules, or prompt templates when the same workflow repeats often.
- Use hooks only when the hook is deterministic, auditable, and easy to disable.

## Safety Defaults

- Start read-only whenever the tool supports it.
- Ask for a plan before edits.
- Limit the file scope.
- Run local checks before committing.
- Review every generated diff.
- Never paste secrets into prompts.
- Do not connect agents to private services through MCP until you understand the server permissions.

## Official Docs to Verify

- OpenAI Codex: <https://developers.openai.com/codex/cli>
- Claude Code: <https://docs.anthropic.com/en/docs/claude-code/overview>
- Cursor: <https://cursor.com/docs>
- Google Antigravity: <https://antigravity.google/docs>
- GitHub Copilot coding agent: <https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent>
- OpenCode: <https://opencode.ai/docs/>
- Kilo Code: <https://kilo.ai/docs>
- Aider: <https://aider.chat/docs/>
- MCP: <https://modelcontextprotocol.io/docs/getting-started/intro>
- Windsurf / Devin Desktop Cascade: <https://docs.windsurf.com/windsurf/cascade>
