# Windsurf

## What It Is

Windsurf is an IDE-based AI coding environment associated with agentic assistant workflows. Product naming, ownership, and documentation locations have changed over time, so this repository keeps Windsurf guidance conservative and points learners to current vendor documentation before setup.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| Editor-first code explanation | Strong | Good for visual learners. |
| Small docs update | Strong | Review visible diffs before accepting. |
| Multi-file planning | Medium | Require a plan before edits. |
| Comparing IDE agents | Strong | Useful alongside Cursor and Copilot. |
| Large implementation | Medium | Keep PR scope narrow. |
| Exact product tutorial | Verify first | Product docs may drift. |

## Beginner Friendliness

High for users who prefer an editor over a terminal. Beginners still need to review diffs, run checks, and avoid accepting broad generated edits.

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| IDE | Primary path. | Best first mode if current product supports it. |
| Hybrid | IDE work plus GitHub PR review. | Keep branch and CI workflow explicit. |
| Cloud/account | If supported by current product. | Verify privacy and plan behavior. |

## Windows Suitability

Good if the current desktop product supports the target Windows setup. Verify installer, account, and workspace guidance before teaching.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Suitable for lightweight docs and small code tasks. |
| API/account | Verify current account and plan requirements. |
| Docker | Not needed for this repo. |
| WSL | Not needed for basic docs and scripts. |
| GPU | Not needed. |

## Best First Task

Ask the assistant to explain one folder, identify one small documentation improvement, and wait for human approval before editing.

## Prompt Template

```text
Target tool: Windsurf

Task:
Explain the [folder] folder and propose one small documentation improvement.

Instructions:
- Read AGENTS.md.
- Do not edit until the plan is approved.
- Keep changes inside this repository.
- Do not modify workflow YAML.
- Do not add dependencies.
- Keep external tool claims conservative.

Validation after edits:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

Final report:
- Files inspected
- Files changed
- Checks run
- Claims to verify
```

## Safety Risks

- Older tutorials may not match the current product.
- IDE-generated diffs can be broad.
- Extension and account policies can affect file access.
- Learners may assume editor approval equals code review.

## Review Checklist

- [ ] Is current product documentation verified?
- [ ] Did the agent explain files before editing?
- [ ] Was the proposed diff reviewed?
- [ ] Were local checks run?
- [ ] Did the task avoid private files and secrets?
- [ ] Are uncertain claims marked for verification?

## When To Avoid It

Avoid Windsurf for:

- Exact setup handouts that have not been checked against current docs.
- Broad refactors without tests.
- Repositories with sensitive files where IDE indexing policy is unclear.
- Tasks where terminal-only reproducibility is required.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Cursor | You want another IDE-agent workflow. |
| GitHub Copilot | You want GitHub-native issue and PR flow. |
| Codex | You want the repo's Git-first reference workflow. |
| Claude Code | You want review without editor-specific behavior. |

## Verification Notes

Verify current product name, documentation location, installer, account requirements, IDE behavior, privacy settings, plan limits, and model behavior.

## Claims To Verify In Official Docs

- Current documentation URL and product naming.
- Supported operating systems.
- Account and plan requirements.
- Agent and chat behavior.
- File indexing and privacy controls.
- Pricing, limits, and model access.

Official docs:

- <https://docs.windsurf.com/windsurf/cascade>
