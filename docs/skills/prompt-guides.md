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
