# Kilo Code

## What It Is

Kilo Code is an open-source AI coding agent positioned across IDE, CLI, and cloud-oriented workflows depending on current configuration. In this repository it is a comparison tool for agent modes, provider choices, planning, and small documentation or bug-fix tasks.

Verify current docs for installation, provider support, model access, cloud behavior, and pricing exposure.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| IDE-based planning | Strong | Good first mode for beginners. |
| Small docs task | Strong | Keep edits reviewable. |
| CLI experiment | Medium | Requires shell comfort. |
| Provider comparison | Medium | Track cost and credentials. |
| Codebase refactor | Medium | Require a plan and tests. |
| Sensitive repo work | Weak at first | Review permissions first. |

## Beginner Friendliness

Medium. IDE mode is usually easier than CLI mode. Start with planning or documentation tasks before allowing broad code edits.

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| IDE | Planning and visible edits. | Best first path if supported. |
| CLI | Terminal-first workflows. | Use after Git and shell basics. |
| Cloud/hybrid | If current docs support it. | Confirm repo access and permissions. |
| Provider-flexible | When comparing models or APIs. | Keep credentials out of the repo. |

## Windows Suitability

Good if the selected IDE extension or CLI path supports the current Windows setup. Verify current install guidance before teaching.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Lightweight for docs and small scripts. |
| API/account | Provider-dependent; verify current requirements. |
| Docker | Not needed for this repo unless current docs require it for a selected mode. |
| WSL | Not needed for basic work unless selected setup requires it. |
| GPU | Not needed for API-backed tasks. |

## Best First Task

Use planning mode for one small docs issue, then manually decide whether to apply the proposed change.

## Prompt Template

```text
Target tool: Kilo Code

Task:
Plan a small update to [file].

Instructions:
- Read AGENTS.md.
- Start in planning mode.
- List the exact files to change.
- Do not edit until the plan is approved.
- Keep provider and pricing claims out of the docs unless verified.

Validation after edits:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

Final report:
- Plan or summary
- Files changed
- Checks run
- Remaining risks
```

## Safety Risks

- Provider setup can be confusing.
- Credentials may be stored incorrectly.
- Cost or rate-limit behavior depends on provider and plan.
- Agent modes may have different permission levels.
- Large diffs can be accepted too quickly.

## Review Checklist

- [ ] Was the selected mode documented?
- [ ] Were provider credentials kept out of Git?
- [ ] Was a plan reviewed before edits?
- [ ] Did edits stay inside the task scope?
- [ ] Were checks run?
- [ ] Were product claims kept conservative?

## When To Avoid It

Avoid Kilo Code for:

- First tasks where setup is not verified.
- Secret-heavy projects.
- Broad refactors without tests.
- Public docs that need exact product claims but have not been checked.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Cursor | You want a more common IDE-agent starting point. |
| Codex | You want local Git-first execution and checks. |
| OpenCode | You want another open-source agent comparison. |
| Aider | You want explicit-file terminal editing. |

## Verification Notes

Verify current product name, install paths, supported modes, provider setup, permission controls, Windows support, limits, and pricing exposure.

## Claims To Verify In Official Docs

- Current installation instructions.
- IDE, CLI, cloud, and hybrid support.
- Provider and model setup.
- Permission controls.
- Windows support.
- Pricing, limits, and rate behavior.

Official docs:

- <https://kilo.ai/docs>
