# Codex Goal Workflow

Use a Codex goal when a task requires more than a quick answer: fixing a bug, implementing a small feature, improving several docs, reviewing a PR, or preparing a branch for merge.

The point of a goal is not to make the agent unbounded. The point is to give it a durable, explicit objective with scope, safety boundaries, verification, and a final report.

## When To Use A Goal

| Task | Goal fit | Notes |
| --- | --- | --- |
| Fix one bug | Strong | Include reproduction steps and expected behavior. |
| Add one documentation guide | Strong | Include audience and required sections. |
| Expand prompt templates | Strong | Include shared template structure. |
| Review a PR | Strong | Make it read-only unless edits are requested. |
| Refactor one script | Medium | Require tests and small diff. |
| Build an entire app | Weak | Split into design, scaffold, and feature PRs. |
| Install many tools | Avoid | Too much setup and risk for one goal. |

## Goal Design Principles

A good goal is durable enough for multi-step work but narrow enough to review.

| Principle | What it means |
| --- | --- |
| One outcome | The goal names a concrete target state. |
| Bounded scope | The goal lists files, folders, or behaviors that may change. |
| Explicit exclusions | The goal names risky areas that must not change. |
| Evidence-based completion | Success criteria can be proven by files, diffs, checks, or rendered output. |
| Reviewable diff | The expected result fits one PR or one clear review unit. |
| Honest uncertainty | External product behavior and unrun checks are reported, not guessed. |

Do not use a goal as a substitute for thinking through the task. Use it to preserve the task once the scope is clear.

## Standard Goal Shape

```text
Objective:
[One clear task.]

Context:
- Read AGENTS.md.
- Run git status.
- Inspect [files] before editing.

Included scope:
- [Allowed files/folders.]

Excluded scope:
- Do not edit .env or secrets.
- Do not delete files.
- Do not install dependencies without approval.
- Do not modify workflow YAML unless requested.
- Keep changes inside this repository.

Success criteria:
- [Criterion 1.]
- [Criterion 2.]
- Local checks pass.
- No unrelated files changed.
- Final response includes changed files and commands run.

Workflow:
1. Inspect relevant files.
2. Make a short plan.
3. Edit the smallest necessary files.
4. Run checks.
5. Fix related failures.
6. Report unverified claims and remaining risks.
```

## Scope Calibration

Use this table to decide whether a goal is the right size.

| Goal size | Example | Recommendation |
| --- | --- | --- |
| Tiny | Fix one typo or link. | A goal is optional. Direct edit may be enough. |
| Small | Improve one README section and update changelog. | Good goal. |
| Medium | Expand one guide and one related template. | Good goal if files are named. |
| Large | Improve every tool page. | Split by tool category or review surface. |
| Very large | Redesign docs, prompts, scripts, and workflows together. | Start with a planning issue and separate implementation goals. |

If a goal cannot name its success evidence, it is too vague.

## Good Goal Prompt Example

```text
Objective:
Expand docs/tools/codex.md into a practical guide for beginner Windows users.

Context:
- Read AGENTS.md.
- Inspect README.md and docs/tools/comparison-matrix.md.

Included scope:
- docs/tools/codex.md
- CHANGELOG.md if the change is user-visible.

Excluded scope:
- Do not edit workflow YAML.
- Do not add dependencies.
- Do not include exact pricing or unsupported model claims.

Success criteria:
- The guide includes what it is, best use cases, setup style, Windows suitability, safety risks, review checklist, alternatives, and official-doc verification notes.
- PowerShell examples are used where commands are needed.
- Local checks pass.

Verification:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
```

## Bad Goal Prompt Example

```text
Make this repo professional and fix anything you see.
```

Why it is weak:

- No included scope.
- No excluded scope.
- No success criteria.
- No safety boundaries.
- No verification commands.
- No definition of "professional."

## Goal State Template

For larger work, add a target-state block:

```text
Target state:
- README explains the repository purpose, audience, workflow, safety model, validation commands, and maintenance rules.
- CONTRIBUTING explains task readiness, scope control, PR expectations, docs style, and review roles.
- SECURITY explains threat model, private data rules, agent permissions, and incident response.
- CHANGELOG records user-visible documentation changes.
```

This makes completion easier to audit because each bullet can be checked against the current files.

## Goal Execution Checklist

- [ ] Start from the repository root.
- [ ] Run `git status`.
- [ ] Read `AGENTS.md`.
- [ ] Inspect relevant files before editing.
- [ ] Keep a minimal plan.
- [ ] Avoid unrelated cleanup.
- [ ] Run local checks.
- [ ] Review `git diff`.
- [ ] Update changelog when useful.
- [ ] Report remaining risks.

## Evidence Checklist

Before calling a goal complete, identify the evidence for each success criterion.

| Requirement | Strong evidence | Weak evidence |
| --- | --- | --- |
| "README improved" | Diff shows new sections that address the requested audience and workflow. | Agent says it improved the README. |
| "Checks pass" | Current command output from the required checks. | Checks passed before edits. |
| "No unrelated files changed" | `git status` and `git diff --stat` match the intended scope. | A quick glance at one file. |
| "No private data added" | Repo health check plus manual scan of changed files. | Assuming docs are safe because they are Markdown. |
| "External claims are conservative" | Claims are qualified or linked to official docs. | Exact pricing or model statements without verification. |

## Verification Commands

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

If safe autofix reports changes:

```powershell
python scripts/safe_autofix.py --write
python scripts/safe_autofix.py --check
```

Review the diff after any write command.

## Failure Modes

| Failure | Cause | Fix |
| --- | --- | --- |
| Agent edits unrelated files | Prompt scope too broad. | Re-scope and remove unrelated edits after review. |
| Checks not run | Goal did not require verification. | Add explicit commands to the prompt. |
| Tool claims are stale | Product behavior was assumed. | Reword with official-doc verification note. |
| Diff is too large | Task was not split. | Break into smaller PRs. |
| Final report is vague | Report format was not specified. | Require files changed, commands, checks, and risks. |
| Goal never finishes | Completion criteria were subjective. | Convert "better" into concrete sections, files, and checks. |
| Goal ignores latest user request | Context drift during a long session. | Re-read the current objective and inspect the latest worktree. |

## Completion Report Format

Codex should end with:

```markdown
## Summary

## Files changed

## Commands run

## Tests/checks

## Remaining risks
```

For public docs work, add:

```markdown
## Claims needing manual verification
```

## Example Completion Audit

Before accepting the final report, ask:

- Did the goal require README changes, and does `git diff` show them?
- Did it require meaningful additions to high-value docs, and are those docs named?
- Did it require public-safety constraints, and did the changed text avoid secrets and private links?
- Did it require local checks, and were the current checks run after edits?
- Did it require changelog updates, and does the changelog describe the visible change?
- Did the final report mention anything not verified?

Completion is not "the agent stopped working." Completion is when the evidence proves the requested end state.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/codex/01-codex-goal-workflow.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `01 codex goal workflow` state what decision, workflow, or reusable behavior it supports?
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
