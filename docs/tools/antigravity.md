# Google Antigravity

## What It Is

Google Antigravity is treated in this repository as an agent-first development environment for planning, coordinating, and reviewing AI-assisted development work. Because it is a fast-changing product area, this guide stays conservative and avoids exact claims about releases, pricing, model access, or platform support.

Verify current official documentation before using Antigravity in a class, public guide, or setup script.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| Planning artifact | Strong | Start with a plan before edits. |
| Documentation cleanup | Strong | Good for bounded, low-risk work. |
| Comparing agent proposals | Medium | Require a human decision before implementation. |
| Coordinated agent work | Medium | Keep file ownership explicit. |
| Codebase refactor | Medium to weak | Only after a reviewed design. |
| First-time setup workshop | Verify first | Product support can change. |

## Beginner Friendliness

Medium. Agent-first workflows can help learners see structured work, but they can also make it harder to identify which agent changed which file. Beginners should begin with planning and documentation tasks.

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| IDE | If current product supports editor-based work. | Verify before teaching. |
| Cloud/web | Useful on limited hardware if supported. | Confirm permissions and repo access. |
| CLI | Use only if current docs support it. | Avoid inventing commands. |
| Hybrid | Planning in one surface, GitHub review in another. | Keep PR review as the source of truth. |

## Windows Suitability

Unknown until verified against current official docs. Prefer browser, cloud, or lightweight IDE paths on limited Windows laptops when available. Do not require Docker, WSL, or local model hosting for beginner tasks unless official docs and the task require it.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Prefer cloud/browser or lightweight IDE paths for limited laptops. |
| API/account | Verify current account, plan, model, and access requirements. |
| Docker | Do not assume it is required. Verify. |
| WSL | Do not assume it is required. Verify. |
| GPU | Not expected for basic repository docs work. |

## Best First Task

Ask Antigravity to create a plan artifact for improving one docs page. Do not permit file edits until the plan is reviewed.

## Prompt Template

```text
Target tool: Google Antigravity

Purpose:
Create a reviewed plan for a small documentation improvement.

Task:
Improve [file] so it is clearer for beginner Windows users.

Instructions:
- Read AGENTS.md.
- Produce a plan artifact first.
- List files you intend to change.
- Wait for human approval before editing.
- Do not modify workflow YAML.
- Do not add dependencies.

Success criteria:
- Plan is narrow and reviewable.
- Safety risks are listed.
- Verification steps are included.

Final report:
- Plan summary
- Proposed files
- Risks
- Claims to verify in official docs
```

## Safety Risks

- Parallel or coordinated agents can drift into overlapping files.
- Generated artifacts can be mistaken for verified results.
- Permissions may be broader than expected.
- Product docs and behavior may change quickly.

## Review Checklist

- [ ] Is the product behavior verified against current docs?
- [ ] Did the agent create a plan before editing?
- [ ] Are file ownership and scope clear?
- [ ] Were generated artifacts reviewed by a human?
- [ ] Were local checks run after edits?
- [ ] Are uncertain claims marked for verification?

## When To Avoid It

Avoid Antigravity for:

- Public setup instructions that have not been checked against current docs.
- Secret-heavy repositories.
- Beginner tasks where product access is unclear.
- Parallel agent edits without a clear review owner.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Codex | You want a known Git-first workflow in this repo. |
| Cursor | You want IDE-first planning and visible diffs. |
| GitHub Copilot coding agent | You want GitHub issue-to-PR flow. |
| Claude Code | You want review and planning without committing to this surface. |

## Verification Notes

For public material, verify every specific claim about Antigravity. This page intentionally avoids exact pricing, launch status, model, and platform claims.

## Claims To Verify In Official Docs

- Current product availability.
- Supported operating systems.
- Installer and account setup.
- IDE, cloud, CLI, and hybrid behavior.
- Agent coordination features.
- Permission model.
- Pricing, limits, and model access.

Official docs:

- <https://antigravity.google/docs>
