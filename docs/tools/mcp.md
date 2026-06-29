# MCP Servers

Model Context Protocol, usually shortened to MCP, is an open protocol for connecting AI applications to external tools, data, prompts, and workflows. MCP can be useful, but it also expands what an agent can see and do.

## Best For

- Read-only documentation lookup.
- Local filesystem context in a test repository.
- Connecting agents to controlled tools.
- Reusing prompts or workflows across tools.
- Teaching permission boundaries.

## Beginner Fit

Low to medium. MCP is easier to understand after a learner has used at least one coding agent safely without extra tools.

## Windows Fit

Good for lightweight local servers and simple tool integrations. Avoid sensitive services and write-capable servers in beginner setups.

## Surface

Protocol plus local or cloud servers, usually connected to an AI tool that supports MCP.

## Main Risks

- Exposing secrets or private files through a server.
- Installing untrusted MCP servers.
- Letting a tool run write operations without review.
- Prompt or tool injection through connected data.
- Confusing server trust with model trust.

## Best First Task

Connect a read-only documentation or filesystem server to a test repository. Ask the agent to summarize files, not edit them.

## Safe MCP Rules

- Prefer read-only servers for learning.
- Avoid private accounts, browser data, and credentials.
- Review the server source and permissions.
- Use a test repository first.
- Disable the server when it is not needed.

## Official Docs

- <https://modelcontextprotocol.io/docs/getting-started/intro>
