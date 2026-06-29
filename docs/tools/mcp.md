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

## Beginner Friendliness

Low to medium. MCP is easier after a learner has used at least one coding agent safely without extra tools. The hard part is not the protocol name; it is understanding trust boundaries.

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
