# Task Spec

Use this template before asking Codex or another AI coding agent to work.

Copy the sections that matter into an issue, PR description, or agent goal. For a tiny typo fix, this may be too much. For any multi-file, agent-assisted, public-facing, or workflow-sensitive task, use the full template.

The goal of a task spec is to remove ambiguity before an agent starts editing.
An agent that is not told what is out of scope will happily "improve" files
nobody asked it to touch. An agent that is not given verification commands
will report success without running anything. This template exists so the
requester, not the agent, makes those calls up front.

## How To Use This Template

1. Fill in **Objective**, **Included Scope**, and **Excluded Scope** at a
   minimum. These three sections alone prevent most scope creep.
2. Add **Background**, **User Story**, and the readiness checklist for
   anything larger than a one-file fix.
3. Always keep **Local Checks** and **Success Criteria** in the spec, even for
   small tasks, so the agent knows what "done" means without guessing.
4. Paste the finished spec into the PR description, an issue, or directly as
   the prompt/goal given to the agent.

## Task Title

```text
[Short public-safe title]
```

## Objective

```text
[One clear outcome. Avoid vague requests such as "improve everything."]
```

A good objective names a file or a small set of files, a concrete deliverable,
and how a reviewer will know it is met. "Improve the docs" is not testable.
"Expand docs/codex/04-review-checklist.md with a PR review sequence and
public-safety checks" is testable: a reviewer can open the file and check.

## Owner And Review

- Requester:
- Implementer or agent:
- Reviewer:
- Target branch:
- Expected PR size:
- Deadline, if any:

## Background

- Why this change is needed:
- Who benefits:
- Relevant issue or discussion:
- Tool intended for the task:
- Current limitation or pain point:
- Previous related work:

## User Story

```text
As a [learner/contributor/maintainer/instructor],
I want [specific improvement],
so that [observable benefit].
```

## Readiness Checklist

- [ ] The objective is specific.
- [ ] The included scope is listed.
- [ ] The excluded scope is listed.
- [ ] Success criteria are testable.
- [ ] Required checks are listed.
- [ ] Public-safety risks are identified.
- [ ] Fast-changing external claims are marked for official-doc verification.

## Files The Agent Should Inspect First

- `AGENTS.md`
- `README.md`
- `[add relevant docs, scripts, or tests]`

Listing files here saves an entire exploration pass. An agent that is told
exactly which files ground the task can skip guessing at repository layout and
go straight to reading the right context.

## Current Behavior Or Current Content

```text
[Describe what exists now. Link or name the relevant section, script behavior, prompt template, or workflow.]
```

## Desired Behavior Or Desired Content

```text
[Describe the target state in enough detail that a reviewer can tell whether it was achieved.]
```

## Included Scope

- [ ] `[file or folder]`
- [ ] `[specific behavior or section]`
- [ ] `[tests, docs, prompts, or changelog entry if needed]`

Included scope should be specific enough that `git diff --stat` after the
task can be checked line by line against this list. If a file appears in the
diff that is not in this list, that is a scope violation, not a bonus.

## Excluded Scope

- [ ] Do not edit secrets or `.env` files.
- [ ] Do not install dependencies without approval.
- [ ] Do not delete files.
- [ ] Do not change unrelated folders.
- [ ] Do not modify workflow YAML unless explicitly requested.
- [ ] Do not add exact pricing, model, or platform claims without official-doc verification.
- [ ] Do not rewrite unrelated guides or templates.
- [ ] Do not add generated assets, screenshots, or binaries unless explicitly requested.

## Success Criteria

- [ ] The requested change is complete.
- [ ] The diff is focused.
- [ ] Beginner-facing docs are clear.
- [ ] Advanced users can audit the reasoning, safety boundaries, and verification path.
- [ ] Public-safety rules still hold.
- [ ] External claims are conservative or explicitly marked for official-doc verification.
- [ ] Internal links still point to real files or headings.
- [ ] Checks pass or failures are honestly reported.
- [ ] Final response lists files changed, commands run, checks run, and remaining risks.

## Acceptance Tests Or Review Evidence

| Requirement | Evidence to inspect |
| --- | --- |
| `[requirement]` | `[file section, command output, test result, rendered page, or PR review note]` |
| `[requirement]` | `[evidence]` |

Every row should map one testable requirement to one concrete artifact a
reviewer can open. "Docs are better" is not a requirement. "The workflow guide
has a troubleshooting table with at least four rows" is, and the evidence is
"open the file, count the rows."

## Safety Boundaries

- Keep work inside this repository.
- Do not inspect private folders.
- Do not print environment variables.
- Do not add secrets, private links, or personal data.
- Ask before destructive commands.
- Ask before dependency installation.

## External Claims

List any claims that could become stale:

- Tool setup:
- Pricing or plan availability:
- Model names:
- Platform support:
- Feature behavior:
- Official docs to verify:

If there are no external claims, write:

```text
No fast-changing external claims added.
```

## Local Checks

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Manual Review Steps

- [ ] Review `git diff --stat`.
- [ ] Review the full diff for unrelated changes.
- [ ] Search for private links, paths, credentials, and account details.
- [ ] Check Markdown tables and links where relevant.
- [ ] Open static HTML files directly in a browser if they changed.
- [ ] Confirm changelog entry is present when user-visible docs changed.

## Rollback Plan

```text
[How to revert if this change causes confusion or breaks checks. For a normal PR, "revert the squash commit" is usually enough.]
```

Rollback for a documentation-only task is almost always `git revert
<commit>`. Name it explicitly anyway. A spec that skips rollback signals the
task is either trivial (say so) or the requester has not thought about the
failure path (which is the confusion protocol's job to catch).

## Definition Of Done

A task is done, not "partially done," when every item below is true:

- [ ] The objective is fully met, not a subset of it.
- [ ] The diff only touches files in **Included Scope**.
- [ ] All **Local Checks** were run and passed, or a failure is reported
  honestly with the exact command and error.
- [ ] **Success Criteria** are all checked off with evidence, not assumed.
- [ ] Any external claim added is either evergreen or flagged for official-doc
  verification.
- [ ] The final report follows **Final Report Format** below.

If any box is unchecked, the task is `BLOCKED` or `NEEDS_CONTEXT`, not
"mostly done." State which one and why.

## Final Report Format

```markdown
## Summary

## Files changed

## Commands run

## Checks/tests

## Claims needing manual verification

## Remaining risks
```

## Example Filled Task

```markdown
## Task Title

Expand Codex review guidance

## Objective

Expand docs/codex/04-review-checklist.md with a clearer PR review sequence, public-safety checks, and examples of review comments.

## Included Scope

- [x] docs/codex/04-review-checklist.md
- [x] CHANGELOG.md if the change is user-visible

## Excluded Scope

- [x] Do not edit workflow YAML.
- [x] Do not add dependencies.
- [x] Do not change other tool pages.

## Success Criteria

- [x] The guide explains review order, risk checks, test evidence, and final decision options.
- [x] Examples are public-safe.
- [x] Local checks pass or failures are reported.

## Owner And Review

- Requester: repository maintainer
- Implementer or agent: Codex CLI (local, ChatGPT sign-in)
- Reviewer: repository maintainer
- Target branch: agent/expand-review-checklist
- Expected PR size: single file, under 150 added lines
- Deadline, if any: none

## Background

- Why this change is needed: new contributors ask the same review-order
  questions in PR comments.
- Who benefits: contributors submitting their first PR, and reviewers who
  currently repeat the same guidance.
- Relevant issue or discussion: none tracked yet.
- Tool intended for the task: Codex CLI.
- Current limitation or pain point: the review checklist file exists but has
  no worked example of what a completed review looks like.
- Previous related work: docs/codex/02-git-branch-pr-merge-workflow.md covers
  the branch and merge steps but not review depth.

## Safety Boundaries

- Keep work inside docs/codex/04-review-checklist.md and CHANGELOG.md.
- Do not touch workflow YAML.
- Do not add dependencies.
- Ask before any destructive git command.

## External Claims

```text
No fast-changing external claims added.
```

## Local Checks

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```
```

This example is deliberately small: one file, one clear objective, explicit
exclusions, and a rollback plan that is just "revert the squash commit." That
is the right amount of ceremony for a task this size. A larger, multi-file
refactor of the workflow docs would justify filling in every section above,
including the full readiness checklist and acceptance-evidence table.
