# MCP Servers

## What It Is

Model Context Protocol, usually shortened to MCP, is a protocol for connecting AI applications to external tools, data, prompts, and workflows. MCP can make agents more useful, but it also expands what an agent can see and do.

In this repository, MCP is an advanced topic. The recommended beginner path is read-only servers connected to public docs or a test repository.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| Read-only documentation lookup | Strong | Best first MCP use. |
| Local test-repo filesystem context | Strong | Avoid private folders. |
| Reusable prompts/tools | Medium | Keep permission boundaries clear. |
| Controlled service integration | Medium | Use least privilege. |
| Write-capable automation | Advanced | Requires review and audit logs. |
| Private account integration | High risk | Avoid until permissions are understood. |

## What MCP Is Good At Vs. Not

Good at:

- Standardizing how an agent reaches external tools and data instead of
  every client inventing its own integration format. This makes read-only
  documentation, search, or filesystem servers easy to reuse across
  different AI tools.
- Giving you a visible seam to inspect: a well-behaved MCP client shows which
  server and which tool call produced a result, which is more auditable than
  a model silently "knowing" something.
- Composable, least-privilege setups when servers are chosen deliberately:
  one read-only docs server, one scoped filesystem server, reviewed
  independently.

Not good at:

- Being safe by default. MCP is a capability-expansion mechanism; a
  write-capable server connected without review is one of the highest-risk
  configurations in this entire guide.
- Hiding trust boundaries from the user. Every server you add is a new piece
  of code (and often a new network endpoint or credential) that the agent
  can call on your behalf; the protocol does not make that code trustworthy.
- First-time AI-agent users. MCP assumes you already understand what it
  means to let an agent read files and run commands; adding a third-party
  server on top of that is not a good place to start.

## Beginner Friendliness

Low to medium. MCP is easier after a learner has used at least one coding agent safely without extra tools. The hard part is not the protocol name; it is understanding trust boundaries.

## Using This Repository's Workflow With MCP

MCP is not a single agent tool with its own task-intake template in this
repository; there is no `prompts/mcp/agent-task.md`. Treat MCP as a
cross-cutting protocol topic that layers on top of whichever coding agent you
are already using (Codex, Claude Code, Cursor, Windsurf, Aider, OpenCode, or
Kilo Code):

- Start from that tool's own prompt template in `prompts/<tool>/`, then add
  an explicit MCP section listing the exact server(s) connected, the tools
  each server exposes, and whether each is read-only or write-capable.
- Always restate this repo's `AGENTS.md` boundaries in the same prompt,
  since an MCP server does not automatically inherit repository-specific
  safety rules.
- Prefer connecting exactly one read-only server for a first experiment
  (public docs or a test-repo filesystem server) rather than combining
  multiple servers in the same session.

## Task Intake Worksheet

| Intake item | What to decide |
| --- | --- |
| Goal | One sentence naming the intended result, not "explore what MCP can do." |
| Server(s) | Exact server name, source, and version/commit connected this session. |
| Tools exposed | List every tool the server exposes, not just the ones you plan to call. |
| Read vs. write | Confirm explicitly whether the server can write, and where. |
| Credentials | Where the server's credentials are stored and how scoped they are. |
| Data exposed | What files, folders, or services the server can reach. |
| Out of scope | Private folders, secrets, other MCP servers not needed for this task. |
| Verification | Local checks plus a manual review of every tool call made. |

If you cannot list every tool a server exposes before starting, do not
connect it yet.

## Example Workflow: Task Intake To PR

1. **Task intake.** Name the one server you are adding, confirm it is
   read-only, and write the one-sentence outcome.
2. **Scoped prompt.** Combine your coding agent's own template (for example
   [prompts/codex/docs-update.goal.md](../../prompts/codex/docs-update.goal.md)
   or [prompts/claude-code/review-docs.goal.md](../../prompts/claude-code/review-docs.goal.md))
   with an explicit MCP section naming the server and its tools.
3. **Agent work.** Let the agent call only the tools you named; treat any
   tool call to an un-named tool as a stop-and-ask event.
4. **Local checks.**

   ```powershell
   python scripts/repo_health_check.py
   python scripts/safe_autofix.py --check
   python -m unittest discover -s tests
   ```

5. **Diff review.** Run `git diff` and separately review the log of MCP tool
   calls made during the session, if the client exposes one.
6. **PR.** Push the branch and open a PR that names the MCP server(s) used
   alongside the usual files-changed and checks-run summary.

## Troubleshooting

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Server won't start | Missing dependency, wrong transport/config, or a port/path conflict on the host machine. | Check the server's own logs and current official docs for its exact startup requirements; do not loosen permissions to "make it work." |
| Permission scope is broader than the task needs | Server was configured with default or all-tools access instead of a scoped subset. | Reconfigure to expose only the tools the task requires, or choose a server that supports scoped/read-only configuration. |
| Server exposes unintended write access | A tool that looks read-only (e.g. "update index") actually mutates state, or a write tool was enabled by default. | Read each tool's declared description and schema before first use; disable or decline any tool whose write behavior is not confirmed. |
| Unclear where credentials are stored | Server or client stores tokens in a config file, keychain, or environment variable without clear documentation. | Verify the current storage location in official docs; keep credentials out of the Git repository regardless of where the client stores them locally. |
| Tool-name collisions across servers | Two connected servers expose a tool with the same or a confusingly similar name. | Disconnect one server, or confirm with the client which tool actually gets called before approving any action. |
| Agent uses a tool you didn't expect for the task | Model chose an available tool without being asked, because it was in scope. | Narrow the connected servers to only what the task needs; treat unexpected tool use as a signal to reduce scope, not just re-prompt. |

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| Local server | Safe for test repos and public docs. | Prefer read-only. |
| Cloud server | Useful for hosted tools. | Verify data exposure. |
| IDE/agent integration | Depends on the AI tool. | Read both server and client docs. |
| Hybrid | Local repo plus external service. | Use least privilege. |

## Windows Suitability

Good for lightweight local servers and simple tool integrations. Avoid sensitive services, write-capable servers, browser data, and private folders in beginner setups.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Lightweight for simple local servers. |
| API/account | Depends on the server; use least privilege. |
| Docker | Some servers may offer Docker, but do not require it for this repo by default. |
| WSL | Not required for the learning path here unless a selected server requires it. |
| GPU | Not needed. |

## Best First Task

Connect a read-only documentation or filesystem server to a test repository. Ask the agent to summarize files, not edit them.

## Prompt/Task Template

```text
Target tool: MCP-capable coding agent

Task:
Use the configured read-only MCP server to summarize the public docs in this repository.

Boundaries:
- Use read-only tools only.
- Do not access private folders.
- Do not request secrets.
- Do not run write operations.
- Do not install new servers.

Success criteria:
- Summary names the files inspected.
- No files are modified.
- Any missing permissions are reported.

Final report:
- MCP server used
- Tools called
- Files or resources read
- Data not accessed
- Risks and next steps
```

## Permissions And Defaults

MCP has no single default permission model; each server and each client
implementation decides what it exposes and how it is authorized. Scope it
down by:

- Treating every server as write-capable until you have confirmed otherwise
  by reading its tool list and descriptions.
- Connecting one server at a time for a new task instead of a standing set
  of servers "just in case."
- Storing credentials the way current official docs recommend, never inside
  this repository.
- Disconnecting or disabling a server the moment the task that needed it is
  done.

## Permission, Cost, And Data Guardrails

| Risk | Practical control |
| --- | --- |
| Exposing secrets or private files through a server | Use least-privilege credentials; exclude private folders from any filesystem server's root. |
| Installing untrusted servers | Prefer well-known, inspectable servers; read the source or tool schema before connecting. |
| Tool injection through connected data | Treat content returned by a server (web pages, files, issues) as untrusted input, not instructions. |
| Write tools changing state without review | Require explicit approval before any write-capable tool call; log or screenshot the call. |
| Confusing server trust with model trust | Remember that a trustworthy model calling an untrustworthy server is still a risk; vet both. |
| Logging sensitive content through the server or client | Check what the client logs by default; avoid passing secrets through tool arguments. |

## When To Prefer This Over The Others

Prefer adding MCP when the task genuinely needs external data or a tool the
base coding agent cannot reach on its own (a live docs search, a scoped
filesystem outside the repo, a ticketing system) and you can name every tool
exposed before starting. Prefer skipping MCP and using the coding agent's
built-in repo context alone when the task is fully answerable from files
already in this repository. Prefer a read-only GitHub PR review workflow
instead of a write-capable MCP server whenever the goal is just review, not
automation.

## Safety Risks

- Exposing secrets or private files through a server.
- Installing untrusted servers.
- Tool injection through connected data.
- Write tools changing state without review.
- Confusing server trust with model trust.
- Logging sensitive content through the server or client.

## Review Checklist

- [ ] Is the server from a trusted source?
- [ ] Is the server read-only for first use?
- [ ] Are private folders excluded?
- [ ] Are credentials scoped and stored outside Git?
- [ ] Are tool calls visible or logged?
- [ ] Is the server disabled when not needed?

## When To Avoid It

Avoid MCP for:

- First AI-agent tasks.
- Secret-heavy repositories.
- Private services without least-privilege tokens.
- Write-capable automation without audit logs.
- Servers you cannot inspect or trust.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Built-in repo context | You only need the current files. |
| Official docs in browser | You only need to read public docs. |
| Local scripts | You need deterministic repository checks. |
| Read-only GitHub PR review | You need review without service integration. |

## Verification Notes

Verify MCP specification version, client support, server permissions, transport/security guidance, authentication behavior, and current best practices in official docs.

## Claims To Verify In Official Docs

- Current protocol overview and terminology.
- Supported transports and authentication guidance.
- Client support for your chosen AI tool.
- Server permission and security recommendations.
- Tool, prompt, and resource behavior.
- Logging and data exposure risks.

Official docs:

- <https://modelcontextprotocol.io/docs/getting-started/intro>
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **tool guide** surface. During broad
maintenance, reviewers should treat `docs/tools/mcp.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `mcp` state what decision, workflow, or reusable behavior it supports?
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
