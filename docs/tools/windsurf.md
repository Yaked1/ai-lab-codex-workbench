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

## What Windsurf Is Good At Vs. Not

Good at:

- Editor-first explanation and small visible edits, since the agent (often
  called Cascade in current product docs) proposes changes inline where you
  can read them next to the surrounding file.
- Multi-file planning when you explicitly ask for a plan before edits; the
  IDE surface makes it easy to review a numbered plan against the files it
  names.
- Comparison learning: because the workflow resembles other IDE-agent tools,
  it is a useful second data point once you already know Cursor or a similar
  editor-based agent.

Not good at:

- Terminal-only, scriptable, or CI-reproducible workflows. Windsurf is
  IDE-first; if you need a headless or automatable step, use Codex CLI or
  Aider instead.
- Guaranteeing a diff was actually read line by line. A polished inline diff
  view can create false confidence that review happened when it did not.
- Sessions where product naming or feature availability from an older
  tutorial is assumed to still be correct. This product area has changed
  ownership and documentation location before; always re-verify.

## Beginner Friendliness

High for users who prefer an editor over a terminal. Beginners still need to review diffs, run checks, and avoid accepting broad generated edits.

## Using This Repository's Workflow With Windsurf

- Prompt template: [prompts/windsurf/agent-task.md](../../prompts/windsurf/agent-task.md).
  It already encodes the "explain first, plan, wait for approval, then edit"
  pattern this repo expects.
- Local rules: attach or restate `AGENTS.md` at the start of the session so
  the agent inherits this repo's safety boundaries and check commands.
  Verify whether the current product version supports an automatic
  repo-instructions file before assuming it reads `AGENTS.md` on its own.
- Keep the workspace scoped to this repository folder only; do not open a
  parent folder that also contains unrelated private projects, since IDE
  indexing can pull in more context than intended.

## Task Intake Worksheet

| Intake item | What to decide |
| --- | --- |
| Goal | One sentence naming the intended result, not just "improve this." |
| Files | Exact files to open or reference in the chat. |
| Mode | Explain/plan first for anything beyond a tiny edit; direct edit only after the plan is approved. |
| Context | `AGENTS.md`, the target file, and directly related tests or templates. |
| Out of scope | Files, folders, generated artifacts, workflow YAML, dependencies, and private data that must not change. |
| Verification | Commands to run in a terminal plus manual diff review inside the editor. |
| Cost/plan risk | Any account, plan, or feature behavior that depends on the current product tier. |

For beginner work, the best task is "explain this folder, propose one small
change, then wait." That sequence separates learning from editing.

## Example Workflow: Task Intake To PR

1. **Task intake.** Pick one file and one outcome ("clarify the setup note
   in `docs/tools/windsurf.md`").
2. **Scoped prompt.** Use
   [prompts/windsurf/agent-task.md](../../prompts/windsurf/agent-task.md),
   naming `AGENTS.md` and the target file explicitly.
3. **Agent work.** Ask for an explanation and a short plan before any edit is
   applied; wait for your own approval before letting Cascade write to disk.
4. **Local checks.** Run in a separate terminal if the IDE terminal is
   unavailable or unclear:

   ```powershell
   python scripts/repo_health_check.py
   python scripts/safe_autofix.py --check
   python -m unittest discover -s tests
   ```

5. **Diff review.** Read the inline diff view line by line before accepting
   any hunk, then confirm with `git diff` outside the editor.
6. **PR.** Push the branch and open a PR; treat "accept" in the editor as a
   draft step, not a substitute for PR review.

## Troubleshooting

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Agent edits files you never mentioned | Codebase indexing pulled in "related" files without being asked. | Restrict scope explicitly in the prompt; reject unrelated hunks in the diff view. |
| Chat seems to lose earlier instructions | Context window filled with long chat history or large attached files. | Start a fresh chat for a new task instead of extending one indefinitely. |
| Extension or agent panel doesn't activate | Editor needs a restart after install/update, or the feature is gated behind a setting/account tier. | Restart the editor and check current settings/docs for the feature flag. |
| Indexed codebase search returns stale results | Index has not refreshed after a large external change (e.g. `git pull`). | Trigger a re-index per current docs, or restart the editor. |
| Large multi-file diff appears after a single small request | Agent expanded scope beyond the plan, or the plan step was skipped. | Reject the diff, ask for a narrower plan, and require an explicit approval step before re-running. |
| Setup steps from an old tutorial don't match the current UI | Product naming, ownership, or docs location changed since the tutorial was written. | Re-verify against current official docs before teaching or repeating the steps. |

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

## Permissions And Defaults

By default, an IDE agent surface like Windsurf's can read and propose edits
across any file it can see in the open workspace. Scope it down by:

- Opening only this repository's folder, not a parent directory containing
  other private projects.
- Requiring an explanation-and-plan step before accepting any multi-file
  change.
- Reviewing every hunk in the diff view individually rather than accepting
  the whole change at once.
- Treating account/plan-gated features as unverified until checked in
  current official docs.

## Permission, Cost, And Data Guardrails

| Risk | Practical control |
| --- | --- |
| Workspace overexposure | Open the repository folder only; keep parent folders with private projects closed. |
| Broad agent edits | Require a plan and accept hunks manually for multi-file changes. |
| Premium or metered usage | Verify current plan, model, and feature-gating behavior before a workshop or long run. |
| Unreviewed terminal commands | Read commands before approval; run repository checks yourself when uncertain. |
| Stale tutorial assumptions | Confirm the current product name, docs location, and feature set before teaching. |

Public-facing docs should avoid exact claims about Windsurf pricing, plan
tiers, model routing, or feature availability unless verified in current
official docs.

## When To Prefer This Over The Others

Prefer Windsurf when you want an IDE-first loop with visible inline diffs and
you are comparing it against another editor-based agent like Cursor. Prefer
Cursor instead if you want the more broadly documented IDE-agent starting
point with clearer rules-file conventions. Prefer Aider or Codex CLI when you
need a terminal-only, scriptable workflow. Prefer Claude Code when you want a
read-only second-opinion review outside the editing surface entirely.

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
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **tool guide** surface. During broad
maintenance, reviewers should treat `docs/tools/windsurf.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `windsurf` state what decision, workflow, or reusable behavior it supports?
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
