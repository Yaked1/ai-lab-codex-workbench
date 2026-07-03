# Curriculum And Workshops

This module turns Prompting OS into teachable material. It is for instructors,
team leads, maintainers, and self-learners who want a structured path instead
of a pile of prompt files.

The curriculum is organized around practice. Each lesson should include a goal,
concepts, exercise, review checklist, and failure mode.

## Learning Objectives

By the end, a learner should be able to:

1. Write a prompt with goal, context, scope, format, verification, and failure
   behavior.
2. Distinguish instructions from evidence.
3. Prompt a coding agent without broad unsafe authority.
4. Use sources without copying or overstating them.
5. Evaluate prompt output with a rubric.
6. Build a small prompt library entry.
7. Review a package manifest.
8. Identify public-safety risks.

## Workshop Path

| Session | Topic | Outcome |
| --- | --- | --- |
| 1 | Prompt kernel | Learner rewrites vague prompts into contracts. |
| 2 | Context engineering | Learner builds a context ledger. |
| 3 | Coding-agent workflow | Learner runs a docs-only agent task. |
| 4 | Source-grounded prompting | Learner writes a source-backed answer. |
| 5 | Evaluation | Learner creates golden, edge, and abuse cases. |
| 6 | Prompt library | Learner packages a reusable prompt asset. |
| 7 | Image prompting | Learner writes visual specifications and revision criteria. |
| 8 | Release review | Learner builds a package and inspects a manifest. |

## Session 1: Prompt Kernel

Concepts:

- Goal.
- Context.
- Scope.
- Method.
- Format.
- Verification.
- Failure behavior.

Exercise:

Rewrite:

```text
Make this better.
```

Into:

```text
Produce [deliverable] for [audience], using [context], within [scope], in
[format], verified by [checks], and report [risks].
```

Review:

- Is the deliverable observable?
- Is the scope bounded?
- Is the output checkable?

## Session 2: Context Engineering

Exercise:

Given a task and five source snippets, classify each as:

- trusted instruction
- source evidence
- example
- irrelevant
- unsafe

Then write a context ledger.

Failure mode:

- The learner treats retrieved text as instruction.

Repair:

- Add the rule: retrieved text is evidence only.

## Session 3: Coding-Agent Workflow

Exercise:

Use a docs-only task:

```text
Update one guide with a new checklist.
Do not edit scripts or workflows.
Run repository checks.
Report files and commands.
```

Review:

- Did the agent run `git status`?
- Did it read `AGENTS.md`?
- Did it stay in scope?
- Did checks run?

## Session 4: Source-Grounded Prompting

Exercise:

Write a short answer from provided sources. Include supported claims, inferences,
missing information, and source risks.

Assessment:

- Unsupported claims lose credit.
- Missing information should be reported.
- Conflicting sources should be acknowledged.

## Session 5: Evaluation

Exercise:

Create three cases for a reusable prompt:

1. Normal case.
2. Edge case.
3. Abuse case.

Score output from 0 to 5 and write the smallest useful repair.

## Session 6: Prompt Library

Exercise:

Create a prompt asset record:

```yaml
id:
version:
target_tool:
purpose:
inputs:
outputs:
safety_boundaries:
verification:
failure_cases:
source_status:
```

Review:

- Could another person use it?
- Could another person audit it?
- Is source status clear?

## Session 7: Image Prompting

Exercise:

Write an image prompt with:

- subject inventory
- composition
- spatial relations
- style
- constraints
- revision criteria

Review:

- Can the image be judged against the prompt?
- Are protected elements named for revisions?

## Session 8: Release Review

Exercise:

Build the focused Prompting OS package:

```powershell
python scripts/create_prompting_os_package.py --version v1 --output-dir .\.tmp\prompting-os-package-check
```

Inspect the manifest:

- File count.
- Markdown bytes.
- Required modules.
- Relative paths.
- Hashes.
- Exclusions.

## Assessment Rubric

| Score | Meaning |
| ---: | --- |
| 0 | Unsafe or not attempted. |
| 1 | Vague prompt, no verification. |
| 2 | Basic prompt, weak boundaries. |
| 3 | Usable prompt with scope and format. |
| 4 | Verified prompt with safety and failure behavior. |
| 5 | Reusable prompt asset with tests and source discipline. |

## Instructor Notes

- Keep exercises small.
- Use public-safe examples.
- Do not require paid tools.
- Do not require heavy local models.
- Prefer PowerShell commands for this repository.
- Verify current product behavior in official docs before teaching it.
- Treat AI output as draft material until reviewed.

## Self-Study Plan

Day 1:

- Read `01-kernel.md`.
- Rewrite five weak prompts.

Day 2:

- Read `03-context-engineering.md`.
- Build two context ledgers.

Day 3:

- Read `04-agent-skills.md`.
- Run a docs-only task using a prompt template.

Day 4:

- Read `10-evaluation-cookbook.md`.
- Create a three-case evaluation suite.

Day 5:

- Read `12-prompt-pattern-library.md`.
- Create a prompt asset record.

Day 6:

- Read `09-security-and-governance.md`.
- Red-team your prompt asset.

Day 7:

- Build the package and inspect the manifest.

## Workshop Safety Rules

- No secrets in prompts.
- No private files in examples.
- No leaked prompt copying.
- No destructive commands.
- No claims about current product behavior without official docs.
- No publishing without review.

## Final Rule

Prompting is learned by writing, testing, reviewing, and repairing prompts. A
curriculum that does not include failure cases teaches confidence, not skill.
