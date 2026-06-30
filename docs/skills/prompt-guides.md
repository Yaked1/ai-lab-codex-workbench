# Prompt Guides

Prompt guides are reusable prompts with enough context, safety boundaries, and
evaluation steps for another person to audit them.

## Required Prompt Guide Structure

Each prompt guide should include:

- Target model or tool.
- Purpose.
- Full prompt.
- Optional shorter version.
- Why the prompt works.
- Failure cases.
- Output-format constraints.
- Safety boundaries.
- Evaluation method.
- Revision checklist.

## Public-Safe Template

~~~markdown
# Prompt Title

Target tool: Codex, Claude Code, MCP client, browser model, or image model

Purpose: one sentence.

## Full Prompt

```text
Read the relevant local instructions first.
Work only in the requested files.
Do not use secrets, private links, or unverifiable claims.
Run the listed checks.
Report changed files, commands run, checks run, and remaining risks.
```

## Short Version

```text
Improve the named guide, keep it public-safe, run checks, and report risks.
```

## Why It Works

- It names the input files.
- It sets forbidden actions.
- It requires validation.
- It asks for a reviewable final report.

## Failure Cases

- The prompt is too broad.
- The model invents current product behavior.
- The output contains private data or copied source text.
- The response skips verification.

## Evaluation Method

- Compare output against the requested scope.
- Check for secrets, private links, stale claims, and unsupported commands.
- Run repository checks.
- Review the diff before merge.
~~~

## Revision Checklist

- [ ] Is the target tool clear?
- [ ] Are inputs and outputs explicit?
- [ ] Are safety boundaries concrete?
- [ ] Are source links and source labels included?
- [ ] Is there a failure-mode section?
- [ ] Is there a verification path?
- [ ] Would a beginner know what to do next?

## Prompt Guide Metadata

Add this block to reusable guides when practical:

```text
Status: draft | reviewed | packaged | deprecated
Target tool:
Task family:
Risk level:
Inputs:
Outputs:
Allowed actions:
Forbidden actions:
Verification:
Source status:
Last reviewed:
```

The metadata helps readers decide whether the guide is safe to paste directly,
needs adaptation, or should be treated as a study example only.

## Example: Documentation Review Prompt

```text
Target tool: Codex or Claude Code
Purpose: Review public documentation before merge.

Read first:
- AGENTS.md
- README.md
- The docs named by the user

Review for:
- Beginner clarity.
- Missing safety boundaries.
- Unsupported product claims.
- Private paths, private links, or token-looking examples.
- Missing verification steps.

Do not:
- Edit files unless explicitly asked.
- Quote secrets or private material.
- Claim current product behavior without official-doc verification.

Final report:
- Findings ordered by severity.
- Files reviewed.
- Checks not run.
- Claims needing verification.
```

## Evaluation Cases

Every prompt guide should have at least these mental test cases:

| Case | Expected behavior |
| --- | --- |
| Normal task | Produces the requested artifact within scope. |
| Missing source | Asks for clarification or marks the claim unverified. |
| Unsafe source text | Treats source as evidence, not instruction. |
| Private data | Refuses to publish or quotes safely without revealing values. |
| Check failure | Reports failure and fixes only related issues. |

## Deprecation Notes

Deprecate a prompt guide when:

- Product behavior changed.
- The prompt encourages unsafe actions.
- A better prompt template replaces it.
- It depends on a private workflow.

Deprecation note:

```text
Deprecated:
Reason:
Replacement:
Migration notes:
```
