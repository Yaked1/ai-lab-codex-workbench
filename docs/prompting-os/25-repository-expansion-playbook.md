# Repository Expansion Playbook

This playbook turns a broad "make the repository more comprehensive" request
into reviewable work. It is designed for documentation-heavy public
repositories where the risk is not only broken code, but also private data,
unsupported claims, low-value filler, and untestable documentation promises.

The playbook assumes conservative repository work: inspect first, preserve
user changes, make focused batches, run checks, and report what was not
verified.

## Expansion Is Not Filler

A comprehensive file earns its length. It should help a real reader make a
decision, run a workflow, recover from failure, or review a claim.

Good expansion adds:

- Purpose and audience.
- Beginner path and advanced path.
- Concrete commands or templates.
- Examples with inputs and expected outputs.
- Failure modes and recovery steps.
- Public-safety boundaries.
- Verification commands.
- Links to adjacent docs.
- Maintainer notes for future updates.

Bad expansion adds:

- Repeated adjectives.
- Unsupported product claims.
- Long copied lists from unclear sources.
- Generic "best practices" without checks.
- Screenshots or binary material that cannot be audited.
- Private paths or local environment details.
- Release promises that tests do not enforce.

## File Audit Tiers

Not every file needs the same treatment. Use tiers to keep expansion focused.

| Tier | File type | Expansion target | Verification |
| --- | --- | --- | --- |
| Tier 1 | Root README, package README, major guide index | Manual with navigation, workflows, package notes, safety, checks, and maintainer guidance. | Named headings, link checks, commands, reviewer scan. |
| Tier 2 | Major guide page | Overview, beginner path, advanced path, examples, failure modes, checklist, related docs. | Content tests for required headings and secret scan. |
| Tier 3 | Prompt template | Target tool, purpose, full prompt, short prompt, inputs, included scope, excluded scope, safety, verification, success criteria, report, failure cases. | Template-section tests. |
| Tier 4 | Script | Clear behavior, conservative defaults, public-safe outputs, deterministic tests where practical. | Unit tests and command checks. |
| Tier 5 | Static HTML | Offline-safe content, no remote assets, useful workflow content, matching repository docs. | Static scan for remote URLs/scripts and manual browser open if visual changes matter. |
| Tier 6 | Data/config | Comments or adjacent docs explaining purpose, update path, and safety restrictions. | Schema or fixture tests where useful. |
| Tier 7 | Generated or temporary output | Usually do not commit; document generation command instead. | Git status and ignored-output review. |

## Expansion Workflow

Use this loop for each focused batch.

1. Scope the batch.
   Name the files, audience, and acceptance evidence. Avoid mixing unrelated
   tool docs, README work, package tests, and workflow YAML unless the request
   explicitly spans them.

2. Inspect existing content.
   Read the file, adjacent index, tests, package builder, and changelog before
   editing. Do not assume a file is thin because its name is short.

3. Identify durable gaps.
   Look for missing reader paths, missing examples, missing failure modes,
   missing safety boundaries, missing verification, and broken links.

4. Draft original content.
   Use sources for structure. Write new text for this repository and this
   audience.

5. Add tests or gates.
   Encode the promised behavior, evidence identity, or artifact parity.

6. Update navigation.
   Add links from the README, package README, guide index, release docs, or
   changelog as appropriate.

7. Run checks.
   Use the strongest realistic verification for the touched area.

8. Review public safety.
   Search for secrets, private paths, token-looking strings, unsupported
   current claims, and copied private content.

9. Stage only after checks pass when the task requires staging.

## Repository-Wide Audit Checklist

Use this checklist when the request says "every meaningful file."

| Area | Questions |
| --- | --- |
| Root files | Does README explain purpose, audience, folder map, workflows, safety, validation, package, maintenance, and contribution path? |
| Agent rules | Are AGENTS instructions concise, local, public-safe, and aligned with the repository's actual checks? |
| Guides | Does each guide include concepts, procedures, examples, failure modes, checklist, and where-to-next links? |
| Tool docs | Does each tool doc say when to use it, when not to use it, risks, verification, and official-doc boundaries? |
| Prompt templates | Are all required sections present and operational? |
| Prompting OS | Does the focused package preserve required procedures, examples, failures, verification, and parity? |
| Automation docs | Are inputs, outputs, allowed files, forbidden behavior, rollback, dry run, and failure modes clear? |
| Release docs | Can a maintainer build, inspect, and review the full release and focused package? |
| Static site | Does it work offline without remote scripts, fonts, trackers, analytics, or CDNs? |
| Scripts | Do scripts default to safe behavior and have tests where practical? |
| Tests | Do tests enforce meaningful promises rather than only file existence? |
| Changelog | Are user-visible changes recorded without overclaiming? |

## Expansion Patterns

### Manual Pattern

Use this pattern for README, package README, and major guide pages.

```text
Title
Purpose
Audience
What this file covers
What this file does not cover
Beginner path
Advanced path
Workflow
Examples
Failure modes
Checklist
Verification
Related docs
Maintainer notes
```

### Work Order Pattern

Use this pattern for prompt templates and agent tasks.

```text
Target tool:
Purpose:
Full prompt:
Short version:
Inputs to fill:
Included scope:
Excluded scope:
Safety boundaries:
Verification steps:
Success criteria:
Final report format:
Failure cases:
```

### Automation Pattern

Use this pattern for workflow and script docs.

```text
Intent:
Inputs:
Outputs:
Allowed files:
Forbidden files:
Dry-run behavior:
Apply behavior:
Rollback:
Logs and manifests:
Common failures:
Verification commands:
Security notes:
```

### Package Pattern

Use this pattern for release and package docs.

```text
Package purpose:
Source directory:
Build command:
Output files:
Manifest fields:
Included file types:
Excluded file types:
Review checklist:
Hash verification:
Public-safety scan:
Known limitations:
```

## Reader Path Matrix

Comprehensive repositories should support different readers without forcing
everyone through the same path.

| Reader | Needs first | Needs later | Files that should serve them |
| --- | --- | --- | --- |
| Beginner | What to open, what commands are safe, what not to touch. | How to write better prompts and interpret checks. | README, Codex start guide, workflow guide, prompt templates. |
| Maintainer | How to preserve safety and run checks. | Package review, changelog, release flow, test updates. | AGENTS, release docs, automation docs, tests. |
| Prompt engineer | Prompt anatomy, patterns, evaluation, source grounding. | Prompt library governance and regression suites. | Prompting OS, prompt guides, templates, rubric. |
| Research curator | Source status, official-doc boundaries, citation handling. | Public-safe synthesis and review reports. | Source policy, research docs, Prompting OS source modules. |
| Tool evaluator | When to use a tool, when not to, risks, verification. | Comparison and migration notes. | Tool docs, comparison matrix, agent operations manual. |
| Instructor | Reading order, workshops, exercises, release snapshot. | Assessment and package evidence. | Curriculum docs, offline site, package guide. |

## Batch Planning

Use small batches even when the goal is broad.

| Batch | Good scope | Avoid |
| --- | --- | --- |
| README batch | Root README, README tests, changelog. | Editing every guide at once. |
| Prompting OS batch | New modules, package README, package tests, package docs. | Unrelated workflow YAML. |
| Prompt template batch | `prompts/**`, template tests, guide links. | Rewriting scripts. |
| Tool-doc batch | One tool family and comparison matrix. | Product claims without official verification. |
| Static-site batch | HTML pages and CSS only. | Remote assets or new JS framework. |
| Release batch | Release docs, package builder tests, manifest inspection. | Auto-publishing or registry setup. |

## Evidence Levels

Do not use weak evidence for broad completion claims.

| Claim | Weak evidence | Strong evidence |
| --- | --- | --- |
| README routes readers | It "looks long." | Named headings, links, commands, tests, reviewer scan. |
| Package is complete | A ZIP exists. | Required paths, source commit, hashes, source/manifest/archive parity. |
| Prompt templates are operational | They mention success criteria once. | Tests verify all required sections across prompt files. |
| Public safety is preserved | No obvious secret in the edited paragraph. | Repository health check, targeted private-path search, token-pattern scan, source-policy review. |
| External claims are safe | They sound plausible. | Official docs checked or claims phrased as "verify in official docs." |
| Existing work was preserved | No merge conflict. | Git diff reviewed, unrelated files untouched, staged/unstaged state reported. |

## Expansion Anti-Patterns

| Anti-pattern | Risk | Better move |
| --- | --- | --- |
| One giant undifferentiated guide | Readers cannot navigate or audit it. | Split into indexed modules with clear purposes. |
| Source dump | Copyright and privacy risk. | Write original synthesis and link source policy. |
| Testless promise | Documentation can silently regress. | Add a small test that checks the promise. |
| Current product claim | It may become false quickly. | Use conservative wording and point to official docs. |
| Local-path evidence in public docs | Reveals private machine structure. | Report archive names and sanitized source labels. |
| Broad script rewrite | Creates unrelated risk. | Keep edits near requested behavior. |
| Generated artifacts committed by accident | Bloats repo and causes drift. | Build into ignored output directories and inspect manifest. |

## Public-Safety Review

Run this review before finalizing public-facing expansion.

- Search for private absolute paths such as personal home directories.
- Search for token-like strings and private-key blocks.
- Search for `.env` references that imply committing environment files.
- Search for exact pricing, model availability, and platform support claims.
- Confirm leak-derived material is structural-only.
- Confirm archive names do not expose private local context.
- Confirm final report separates verified, skipped, and unverified items.

## Final Report Model

Every expansion should end with a compact report.

```text
Summary:
- What changed and why.

Changed files:
- File list grouped by area.

Archive/source usage:
- Sources inspected.
- Sources skipped and why.
- Structural lessons used.

Verification:
- Commands run and results.
- Package metrics, if package changed.
- Public-safety scan results.

Remaining risks:
- Unverified external claims.
- Sources skipped.
- Checks not run.
```

## Maintainer Completion Gate

Do not mark a broad expansion complete until these are true:

- [ ] Requirements from the instruction file or issue were converted into
  concrete evidence items.
- [ ] Existing staged and unstaged changes were preserved or intentionally
  incorporated.
- [ ] New content is original, public-safe, and linked from relevant indexes.
- [ ] Tests enforce the new behavior, evidence, or parity claims.
- [ ] Package artifacts were built when package contents changed.
- [ ] Manifest evidence was inspected, not merely generated.
- [ ] Public-safety searches found no private paths or secrets.
- [ ] Final status includes changed files, commands, checks, metrics, risks,
  and skipped sources.
