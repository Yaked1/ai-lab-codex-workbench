# Prompt Guides

Prompt guides are reusable prompts with enough context, safety boundaries, and
evaluation steps for another person to audit them.

## How A Prompt Guide Differs From An Executable Skill

A prompt guide and a skill both encode "how to do this recurring task well,"
but they differ in who executes the procedure and how much the tool
enforces it:

| Aspect | Prompt guide | Executable skill (native skill bundle, `.goal.md`, or MCP tool) |
| --- | --- | --- |
| What it is | A Markdown template a human reads, fills in, and pastes into a chat or CLI session. | A bundle or file the agent tool loads by trigger/description, or a live tool it can call. |
| Who decides when to use it | The human, every time, by choosing to copy it in. | The tool's own matching logic (skill description) or the model's own decision to call a tool. |
| Enforcement | None automatic -- if the human forgets a step, nothing stops the run. | Partial -- a skill's procedure still relies on the model following it, but scope/forbidden-file lists can be checked in review; an MCP tool's schema constrains what arguments are even possible. |
| Update mechanism | Edit the Markdown file; no packaging step. | May require specific folder structure, metadata fields, or a running server process. |
| Best for | Occasional tasks, tasks where the human should read and adapt wording each time, or tools with no native skill system. | Frequent tasks where a consistent, auditable procedure matters and the tool can load it automatically. |
| Example in this repo | [prompts/codex/docs-update.goal.md](../../prompts/codex/docs-update.goal.md) used as a manually-pasted template. | A Claude Code `SKILL.md` bundle (see [claude-code.md](claude-code.md)) or a live MCP tool call (see [mcp.md](mcp.md)). |

### When To Use Which

Use a **prompt guide** when:

- The task is occasional, not something run many times a week.
- A person should read the prompt, adjust the inputs, and decide whether it
  still applies before running it -- for example because the topic or
  audience changes each time.
- The target tool has no native skill/goal mechanism (a browser-based
  chat model, an image model, or any tool without `SKILL.md`/`AGENTS.md`
  support).
- Current product behavior is changing quickly enough that baking it into
  an auto-loaded skill risks going stale silently.

Use an **executable skill** (native `SKILL.md`, this repo's `.goal.md`
convention, or a custom slash command) when:

- The same task recurs often enough that retyping the prompt is real
  friction.
- The tool has a real loading/trigger mechanism worth using.
- The procedure benefits from bundled references or scripts.
- You want the scope/forbidden-file list to live in one canonical file that
  every invocation reuses, rather than being retyped and potentially
  drifting.

In this repo, the actual prompt guides live under
[prompts/](../../prompts/) as `.md` templates (for example
[prompts/codex/docs-update.goal.md](../../prompts/codex/docs-update.goal.md),
[prompts/codex/fix-bug.goal.md](../../prompts/codex/fix-bug.goal.md),
[prompts/codex/implement-feature.goal.md](../../prompts/codex/implement-feature.goal.md),
[prompts/codex/repository-cleanup.goal.md](../../prompts/codex/repository-cleanup.goal.md),
and [prompts/codex/review-pr.goal.md](../../prompts/codex/review-pr.goal.md)),
plus the curriculum guides under
[docs/guides/](../../docs/guides/) and the deeper
[docs/prompting-os/](../../docs/prompting-os/) module set (for example
[docs/prompting-os/04-agent-skills.md](../../docs/prompting-os/04-agent-skills.md),
which documents the "agent work order" pattern these prompt guides follow).
Every one of those `.goal.md` files is a prompt guide in the sense used on
this page: a human pastes it in, fills in the bracketed inputs, and runs it
-- there is no automatic loading step.

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

## Worked Example: Reading A Real Prompt Guide In This Repo

[prompts/codex/fix-bug.goal.md](../../prompts/codex/fix-bug.goal.md) is a
concrete example of the template above filled in for a real task family.
Opening it shows the same shape this page describes:

- `## Target Tool` names OpenAI Codex CLI or goal-mode-style agents.
- `## Inputs To Fill` lists placeholders such as `{bug_description}` and
  `{repro_steps}` a person fills in before pasting the prompt.
- `## Full Prompt` contains the complete, ready-to-paste instruction block,
  including mandatory first steps (`git status`, read `AGENTS.md`, read the
  affected files) and a `## Final Report Format` the model must fill out.
- `## Failure Cases` and `## Verification Steps` give the reader a way to
  judge whether a run actually worked, instead of trusting a bare "done."

Compare that to [prompts/codex/review-pr.goal.md](../../prompts/codex/review-pr.goal.md),
which uses the identical section structure for a different task (reviewing
a pull request instead of fixing a bug). That repetition is intentional: a
prompt guide's value comes from reusing a proven shape across many topics,
not from writing a new structure every time. When adding a new prompt guide
to this repo, copy the section headings from an existing file in
[prompts/codex/](../../prompts/codex/) rather than inventing a new outline.

## Troubleshooting Table

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Prompt guide followed inconsistently across runs | The guide leaves an ordering or scope decision implicit, so different sessions fill the gap differently. | Add explicit numbered "mandatory first steps" and named `## Included Scope` / `## Excluded Scope`, as in `docs-update.goal.md`. |
| Model invents current product behavior (pricing, limits, availability) | The guide did not explicitly forbid it or provide a conservative-wording instruction. | Add a line such as "do not invent exact pricing, plan tiers, or model availability; mark as verify in official docs" to the Full Prompt block. |
| Output contains secrets or private paths | The guide's inputs were filled with real private data instead of placeholders, or the model copied source text verbatim. | Reject the output, replace private values with placeholders, and add an explicit "no secrets/private paths" line to Safety Boundaries. |
| Guide and skill overlap, causing confusion about which to use | The same task was documented twice: once as a prompt guide, once as a native skill, with no cross-reference. | Pick one as canonical for the recurring case (usually the skill, if the tool supports it) and link to it from the prompt guide instead of duplicating instructions. |
| Verification section is ignored and the model claims success anyway | The guide's `## Evaluation Method` or `## Verification Steps` are vague ("check it works") rather than exact commands. | Replace with the exact commands this repo already uses: `python scripts/repo_health_check.py`, `python scripts/safe_autofix.py --check`, `python -m unittest discover -s tests`. |
| Guide works for one model/tool but fails for another | The guide assumes a specific tool's conventions (for example Codex's `/goal` goal mode) without noting that other tools need adaptation. | State the target tool explicitly in `## Target Tool` and add a note where the prompt needs tool-specific adjustment. |

## Revision Checklist

- [ ] Is the target tool clear?
- [ ] Are inputs and outputs explicit?
- [ ] Are safety boundaries concrete?
- [ ] Are source links and source labels included?
- [ ] Is there a failure-mode section?
- [ ] Is there a verification path?
- [ ] Would a beginner know what to do next?

## Checklist: Writing A New Prompt Guide Safely In This Repo

- [ ] Confirm a prompt guide is the right choice, not a skill -- see
      "When To Use Which" above.
- [ ] Reuse the section headings from an existing file in
      [prompts/codex/](../../prompts/codex/) so the format stays consistent
      and passes `tests/test_prompting_docs.py`'s section checks.
- [ ] Name the target tool and audience explicitly.
- [ ] List every input placeholder (for example `{topic}`, `{audience}`,
      `{allowed_scope}`) with a short description and example value.
- [ ] Write `## Included Scope` and `## Excluded Scope` with concrete file
      paths or task boundaries, not vague language.
- [ ] Add mandatory first steps: check `git status`, read `AGENTS.md`, read
      every file named in scope, before any edit.
- [ ] Add `## Safety Boundaries` forbidding secrets, `.env` files,
      credentials, private links, private paths, dependency additions, and
      unsupported/exact product claims.
- [ ] Add `## Verification Steps` with the repo's real commands (see
      Troubleshooting Table above).
- [ ] Add `## Success Criteria`, `## Final Report Format`, and
      `## Failure Cases` sections.
- [ ] Mark every fast-changing product claim (pricing, plan tiers, model
      availability, feature support) as "verify in official docs" instead
      of asserting it.
- [ ] Confirm no secrets, real tokens, or private paths appear anywhere in
      the guide, including worked examples.
- [ ] Run the local check suite after adding or editing the file:
      `python scripts/repo_health_check.py`,
      `python scripts/safe_autofix.py --check`,
      `python -m unittest discover -s tests`.

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

## Claims To Verify In Official Docs

Prompt guides age quickly whenever they name a specific tool's behavior.
Before publishing, mark the following as "verify in official docs" rather
than fact if they were not freshly checked in the current change:

- Any target tool's current CLI flags, goal-mode syntax, or invocation
  method (for example Codex's `/goal` behavior or Claude Code's slash
  command syntax).
- Context window size, token limits, or rate limits for any named model.
- Pricing, plan tier, or subscription requirements for any named tool.
- Model availability or default-model claims for any named provider.
- Whether a tool auto-runs verification commands versus requiring them to
  be pasted explicitly into the prompt.
- Any claim that a specific prompt pattern is officially recommended by a
  vendor, as opposed to a community or repo-local convention.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/skills/prompt-guides.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `prompt guides` state what decision, workflow, or reusable behavior it supports?
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
