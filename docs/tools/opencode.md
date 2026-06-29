# OpenCode

## What It Is

OpenCode is an open-source AI coding-agent project with terminal, desktop, IDE, or hybrid surfaces depending on the current release. It can be useful for learners who want to understand provider-flexible agent workflows, local command permissions, and open-source alternatives to hosted coding agents.

Verify current install commands, provider setup, platform support, and pricing exposure in official docs.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| Read-only repository overview | Strong | Safe first task. |
| Terminal-first coding session | Medium | User should understand Git and shell commands. |
| Provider comparison | Medium | Track cost and credentials carefully. |
| Open-source agent experimentation | Strong | Good for learning architecture and permissions. |
| Beginner implementation | Medium | Start with docs and tests. |
| Sensitive private repo | Weak | Understand provider and local permissions first. |

## Beginner Friendliness

Medium. OpenCode is approachable for terminal users, but beginners need clear setup boundaries: where provider credentials live, which commands can run, and how to review diffs.

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| CLI | Terminal-first work. | Good after Git basics. |
| Desktop/IDE | If current release supports it. | Verify before teaching. |
| Hybrid | Provider plus local repository workflow. | Keep credentials out of the repo. |

## Windows Suitability

Verify current Windows installation and shell support before writing a setup lesson. For this repo, first tasks should be read-only until the environment is understood.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Lightweight for docs and small script tasks. |
| API/account | Provider-dependent; verify current setup and cost exposure. |
| Docker | Do not assume it is required. |
| WSL | Do not assume it is required. |
| GPU | Not needed for normal API-backed coding-agent work. |

## Best First Task

Ask OpenCode to summarize the repository structure without editing files:

```text
Read the repository and explain its main docs, scripts, workflows, and tests.
Do not modify files.
Do not run write commands.
```

## Prompt Template

```text
Target tool: OpenCode

Mode:
Start read-only.

Task:
Explain this repository and propose one small documentation improvement.

Boundaries:
- Read AGENTS.md first.
- Do not edit files.
- Do not install dependencies.
- Do not access files outside the repository.
- Do not print environment variables.

Final report:
- Repo summary
- Suggested files to change
- Proposed checks
- Risks and assumptions
```

## Safety Risks

- Provider credentials can be misconfigured or accidentally exposed.
- Terminal agents may run commands the user did not expect.
- Cost exposure can change when switching providers.
- Windows support may differ by install method.

## Review Checklist

- [ ] Were credentials kept outside the repo?
- [ ] Did the first task start read-only?
- [ ] Was command execution limited?
- [ ] Were proposed edits scoped to specific files?
- [ ] Were local checks run after any write task?
- [ ] Are provider and pricing details marked for verification?

## When To Avoid It

Avoid OpenCode for:

- First-time users uncomfortable with terminal output.
- Repositories containing secrets before permissions are reviewed.
- Tasks requiring guaranteed vendor support.
- Public setup docs that have not been verified against current release notes.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Codex | You want the repo's reference workflow. |
| Aider | You want explicit-file terminal editing. |
| Cursor | You want IDE-first review. |
| Claude Code | You want review and explanation. |

## Verification Notes

Verify current install commands, supported surfaces, provider configuration, permission controls, Windows behavior, pricing exposure, and model/provider options.

## Claims To Verify In Official Docs

- Current installation method.
- Supported operating systems.
- CLI, desktop, and IDE support.
- Provider setup and credential storage.
- Permission model.
- Pricing exposure through providers.

Official docs:

- <https://opencode.ai/docs/>
