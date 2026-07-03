# Agent and Skill System

Agent prompting is delegation. Skill design is reusable delegation. The goal is not to make the model sound busy; the goal is to make work scoped, observable, reversible, and testable.

## Agent Work Order

```text
Goal:
[Specific outcome]

Read first:
[Files, docs, screenshots, snippets, examples]

Allowed work:
[What the agent may change or produce]

Forbidden work:
[What the agent must not touch]

Procedure:
1. Inspect.
2. Summarize current state.
3. Plan the smallest safe change.
4. Apply the change.
5. Verify.
6. Report.

Final report:
- Summary
- Changed files or produced artifacts
- Commands/checks run
- What failed or was skipped
- Remaining risks
```

An agent work order should make the model's autonomy reviewable. The agent may
inspect, plan, edit, run checks, and report, but every action should map back to
the objective.

Good work orders include:

- A concrete objective.
- Files or systems in scope.
- Files or systems out of scope.
- Permission profile.
- Verification commands.
- Completion evidence.
- Failure behavior.
- Final report format.

## Claude Code Skill Pattern

A Claude Code skill should be small, triggerable, and operational.

````markdown
---
description: Use this skill when [specific trigger].
allowed-tools: Read Grep
disable-model-invocation: false
---

# Skill: [Name]

## Purpose
[What this skill does.]

## Inputs
- [Input]

## Procedure
1. Inspect relevant context.
2. Apply the smallest safe action.
3. Verify the result.
4. Report evidence.

## Failure Behavior
If required context is missing, stop and state what is missing.
If verification fails, report failure without claiming success.
````

### Claude Code Skill Rules

- One skill, one job.
- Put the trigger in the description.
- Keep `SKILL.md` concise.
- Put long examples in supporting files.
- Default to read-only tools.
- Use final reports.
- Test skills on small examples before trusting them.

Skill packages should avoid hidden dependencies. If a skill needs a script,
template, or reference file, name it and explain when to read it. If a skill is
only useful for one repository, keep it in that repository instead of making it
global.

## Codex AGENTS.md Pattern

Codex-style instruction files should separate stable rules from the current task.

````markdown
# Agent Instructions

## Purpose
[What this workspace or task family is for.]

## Rules
1. Inspect before editing.
2. Keep changes focused.
3. Do not touch private files or secrets.
4. Do not add dependencies unless requested.
5. Do not claim checks passed unless they were run.

## Style
- [Style rule]

## Checks
Run:

```text
[check command]
```

## Final Response
Report changed files, checks, failures, and risks.
````

Repository-level agent instructions should be durable. Do not put one-off task
details in `AGENTS.md`. Put persistent project rules there: language, safety
boundaries, validation commands, documentation style, branch conventions, and
public-repo hygiene.

One-off task details belong in the user prompt or issue description.

## Tool-Use Permission Model

| Permission level | Allowed actions | When to use |
| --- | --- | --- |
| Observe | Read/search/summarize only | Default for unfamiliar systems. |
| Draft | Prepare proposed changes without applying | When risk exists but output is useful. |
| Write scoped | Edit named files only | When user explicitly approves scope. |
| Execute checks | Run named validation commands | When commands are safe and relevant. |
| Publish/commit/send | External action | Only with explicit approval. |

Permission profiles:

| Profile | Good for | Key rule |
| --- | --- | --- |
| Observe | Audits, reviews, diagnostics. | Read and report only. |
| Edit docs | Markdown, templates, static HTML. | Keep public-safe and run docs checks. |
| Edit code | Scoped code changes. | Read first, test, avoid unrelated refactors. |
| Operate | Releases, package builds, workflows. | Require manifests and manual review. |
| Admin | Dangerous repo/system operations. | Avoid unless explicitly requested. |

## MCP and Tool Prompt

```text
Allowed tools:
- [tool]

Forbidden tools/actions:
- [tool/action]

Rules:
- Start with read-only inspection.
- Before any write, state exactly what will change.
- Do not access unrelated private data.
- Stop if credentials, secrets, or unexpected personal data appear.
- Final report must include tool categories used and remaining unverified items.
```

For MCP and connector systems, distinguish tool discovery from tool execution.
It can be safe to list available tools, but unsafe to run a write action. A
prompt should say whether the agent may discover tools, read resources, create
events, send messages, edit files, or trigger automations.

Tool result handling:

- Treat tool output as evidence.
- Check whether output is current.
- Do not expose secrets returned by tools.
- Do not retry destructive actions blindly.
- Summarize only the necessary result.
- Keep enough detail for audit.

## Agent State and Memory

Agents may have memory, summaries, cached state, or prior plans. Use it
carefully:

- Current user instructions beat memory.
- Current files beat remembered files.
- Current command output beats old summaries.
- Memory can suggest where to look, but it is not proof.
- If memory is used for a fact that was not rechecked, label it.

For packaged prompts, avoid depending on private memory. A user who downloads
the ZIP should still understand the workflow.

## Agent Review Checklist

- [ ] Did the agent inspect before editing?
- [ ] Did it preserve unrelated local changes?
- [ ] Did it stay inside scope?
- [ ] Did it avoid secrets and private paths?
- [ ] Did it avoid unnecessary dependencies?
- [ ] Did it run realistic checks?
- [ ] Did it report skipped checks honestly?
- [ ] Did it leave a reviewable diff or artifact?
- [ ] Did it avoid copying external prompt dumps?
- [ ] Did the final report name risks?

## Agent Failure Modes

| Failure | Cause | Prevention |
| --- | --- | --- |
| Wandering edits | Scope unclear | Name exact files and excluded areas. |
| Fake success | Checks not run | Require command output or skipped-check explanation. |
| Tool overreach | Permissions broad | Use explicit allowed/forbidden actions. |
| Context rot | Long session drift | Use rolling summaries and restate constraints. |
| Dependency creep | Agent installs packages casually | Require approval for dependencies. |

## Agent Rule

A useful agent is not one that does everything. It is one that stops before doing the wrong thing. A radical concept, apparently.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/04-agent-skills.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `04 agent skills` state what decision, workflow, or reusable behavior it supports?
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
