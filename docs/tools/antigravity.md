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

## What Antigravity Is Good At Vs. Not

Treated conservatively here because the product surface changes quickly. What
generalizes across agent-first, planning-forward tools like this:

Good at:

- Producing a structured plan artifact before any file touches disk, which
  gives you an explicit approval gate.
- Bounded, low-risk documentation or cleanup tasks where the plan is easy to
  audit line by line.
- Comparing multiple proposed approaches before committing to one.

Not good at (or not yet verified as good at):

- Tasks where you need guaranteed parity with a specific IDE or terminal
  workflow — verify current surface support before relying on it.
- Multi-agent coordination without a single clear file-ownership owner; two
  agents editing overlapping scope is a common way agent-first tools produce
  unreviewable diffs.
- Anything where you cannot yet verify the permission model. Treat it as
  "plan-first only" until you have confirmed current write behavior in
  official docs.

## Beginner Friendliness

Medium. Agent-first workflows can help learners see structured work, but they can also make it harder to identify which agent changed which file. Beginners should begin with planning and documentation tasks.

## Using This Repository's Workflow With Antigravity

- Prompt template: [prompts/antigravity/agent-task.md](../../prompts/antigravity/agent-task.md).
- Local rules: point Antigravity at this repository's `AGENTS.md` explicitly
  in your planning prompt. Verify in current official docs whether Antigravity
  has its own dedicated rules-file convention (an agent-config or workspace
  file) separate from `AGENTS.md`; if so, mirror the same scope and safety
  content there rather than maintaining two diverging rule sets.
- Because this tool is plan-first, treat every plan artifact as a draft PR
  description: it should name files, scope, and risks before anyone approves
  edits.

## Task Intake Worksheet

Before starting, write the task down in a form that can survive a plan review.

| Intake item | What to capture |
| --- | --- |
| Outcome | One sentence describing the exact change or plan you want. |
| Mode | `Plan only`, `plan then edit`, or `single approved edit`. Use plan-only for unfamiliar product behavior. |
| Files | Exact file paths or non-overlapping file groups for each agent/task. |
| Approval gate | Who approves the plan before edits and what "approved" means. |
| Verification | Local commands, PR checks, or manual review steps that prove the result. |
| Product assumptions | Anything about Antigravity's current UI, permissions, artifacts, models, or pricing that must be checked in official docs. |
| Cost exposure | Whether the run may consume paid model usage, hosted-agent minutes, or workspace quota. |

If the intake cannot name files and verification steps, keep the session in
planning mode until the scope is clear.

## Context Selection Rules

Agent-first tools can gather more context than a beginner expects. Keep
context explicit:

- Attach or reference `AGENTS.md` first so the repository's public-safety and
  no-dependency boundaries are visible before planning.
- Give the agent exact target files, not broad repository descriptions.
- Include directly related docs or templates only when they are needed for
  consistency. Do not include private notes, local transcripts, browser data,
  archives, screenshots, or account-specific output.
- For multi-agent work, assign non-overlapping file ownership before any
  implementation step. One file should have one owner.
- Require the plan artifact to list every intended file change and every
  verification command before edits begin.
- Treat unverified product behavior as a note in the plan, not as a fact in
  public docs.

## Beginner Workflow Guidance

For a first Antigravity task in this repository, use the tool as a planner:

1. Ask for a plan for one docs page.
2. Require the plan to list files, risks, and checks.
3. Review the plan like a PR description.
4. Approve only a single, focused implementation step.
5. Compare the final diff against the approved plan.
6. Run this repository's local checks outside the agent if needed.

This makes the agent's reasoning visible before it writes files and gives the
human maintainer a clear stop point if the plan drifts.

## Example Workflow: Task Intake To PR

1. **Task intake.** Write one sentence naming the docs file and the outcome
   you want.
2. **Scoped prompt.** Use
   [prompts/antigravity/agent-task.md](../../prompts/antigravity/agent-task.md)
   and require a plan artifact as the first output, with no edits yet.
3. **Agent work (plan phase).** Review the plan: does it name every file it
   intends to touch? Does it call out risks?
4. **Human approval gate.** Only after you approve the plan does the agent
   proceed to edits. Treat this as non-optional, not a formality.
5. **Local checks.**

   ```powershell
   python scripts/repo_health_check.py
   python scripts/safe_autofix.py --check
   python -m unittest discover -s tests
   ```

6. **Diff review.** Confirm the actual diff matches the approved plan; agent
   summaries can drift from what was actually written.
7. **PR.** Open a PR that includes the plan artifact alongside the diff so
   reviewers can compare intent to result.

## Troubleshooting

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Agent edits files not listed in its own plan | Plan and execution phases drifted, or scope crept mid-task. | Reject the diff, regenerate a tighter plan, and re-approve before continuing. |
| Two agent runs touch the same file differently | No single owner was assigned for that file/scope. | Restart with one agent per file or module; merge manually if both runs have value. |
| Generated plan is vague ("update docs") | Prompt lacked a concrete file and outcome. | Rewrite the prompt with the exact file path and one measurable outcome. |
| Unsure what permissions the session actually has | Product surface and permission model are still evolving. | Verify current permission docs before granting write access; default to plan-only. |
| Artifact looks final but was never checked against local tests | Planning artifacts are not test output. | Always run the three local checks yourself before treating a task as done. |

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

## Permissions And Defaults

Treat the permission model as unverified until you check current official
docs. As a safe default: assume the agent can read the whole workspace it is
pointed at, require plan approval before any write, and never grant it access
to a repository containing secrets until you have confirmed exactly what it
can execute and where output artifacts are stored.

## Permission, Cost, And Data Guardrails

| Risk | Practical control |
| --- | --- |
| Unknown write permissions | Start in plan-only mode and approve writes explicitly after reading the plan. |
| Multi-agent overlap | Assign file ownership before implementation; stop if two agents touch the same file. |
| Hosted execution cost | Verify billing, quotas, and model routing before long or repeated runs. |
| Artifact leakage | Keep plans, logs, and generated reports free of secrets, private links, and machine-specific paths. |
| Product drift | Recheck official docs before publishing setup instructions or exact UI steps. |
| False confidence | Treat generated artifacts as proposals until local checks and human diff review confirm them. |

When writing public material, prefer "verify in official docs" notes for
availability, pricing, supported platforms, and permission behavior. Do not
turn a single observed session into a general product guarantee.

## When To Prefer Antigravity Over Other Tools In This Guide

Prefer Antigravity when you specifically want a plan-first artifact you can
review before any code changes, or when comparing multiple agent-proposed
approaches to the same problem is valuable. Prefer Codex or Claude Code
instead when you want a workflow with well-established, verified permission
semantics and this repo's existing branch/check/PR loop.

## Safety Risks

- Parallel or coordinated agents can drift into overlapping files.
- Generated artifacts can be mistaken for verified results.
- Permissions may be broader than expected.
- Product docs and behavior may change quickly.

## Review Checklist

- [ ] Is the product behavior verified against current docs?
- [ ] Did the agent create a plan before editing?
- [ ] Are file ownership and scope clear?
- [ ] Does the plan name exact files and verification commands?
- [ ] Are paid usage, hosted execution, or quota risks understood?
- [ ] Were generated artifacts reviewed by a human?
- [ ] Were local checks run after edits?
- [ ] Are uncertain claims marked for verification?

## Final Report Expectations

The final report should let a reviewer compare intent to result:

- Link or summarize the approved plan artifact.
- List exact files changed and any file ownership assignments used.
- State whether implementation stayed inside the approved plan.
- List checks run, where they ran, and pass/fail results.
- Mark Antigravity-specific behavior that still needs official-doc
  verification.
- Include remaining risks such as plan drift, skipped checks, or overlapping
  agent output.

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
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **tool guide** surface. During broad
maintenance, reviewers should treat `docs/tools/antigravity.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `antigravity` state what decision, workflow, or reusable behavior it supports?
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
