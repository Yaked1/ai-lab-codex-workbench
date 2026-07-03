# Claude Code Skills

Source status: official-doc anchored. Verify current setup in the official
Claude Code skills documentation before teaching exact install or
distribution steps: <https://code.claude.com/docs/en/skills>

## What It Is

Claude Code skills are reusable instruction bundles that extend Claude Code
for specialized tasks. A skill can describe procedures, expected files,
resources, and scripts that Claude should load when the skill is relevant.

Claude Code also supports **custom slash commands**: Markdown files placed
under `.claude/commands/` that define a reusable prompt you can invoke with
`/command-name`. This repository already uses that pattern for local
curation work -- for example, a maintainer can define `/goal` in
`.claude/commands/goal.md` to paste in the latest curator prompt without
retyping it every session.

It is important to keep these two concepts separate:

| Concept | Native to Claude Code? | What it is |
| --- | --- | --- |
| Skill (`SKILL.md` bundle) | Yes | An instruction/resource/script bundle Claude loads when its trigger matches. |
| Custom slash command (`.claude/commands/*.md`) | The *mechanism* is native; the *command* is not | A user-authored Markdown file that becomes a `/name` shortcut. Claude Code does not ship a `/goal` command out of the box -- you write it. |

Do not describe `/goal` (or any other `.claude/commands/` file this
repository uses) as a built-in Claude Code feature. It is a custom command a
maintainer authored, using a mechanism Claude Code provides.

## What To Verify In Official Docs

Claude Code behavior can change, so public docs should verify current details
before publishing exact instructions. Treat these as official-doc verification
items:

- Current skill folder locations and packaging rules.
- Required or optional metadata fields in `SKILL.md`.
- How skills are discovered, enabled, shared, or disabled.
- Current custom command behavior and argument handling.
- Platform-specific path examples.
- Any account, plan, or product-availability claim.

If those details were not checked during the current PR, keep the wording
conceptual and point readers to the official Claude Code docs instead of
publishing exact setup claims.

## Role Boundaries

| Role | Claude Code skill may do | Human maintainer must do |
| --- | --- | --- |
| Read-only reviewer | Inspect public docs, produce findings, and identify verification gaps. | Decide whether edits are needed. |
| Write-capable helper | Edit files named in the task after reading repo instructions. | Review the diff, run or verify checks, approve the PR. |
| Custom command | Save a reusable prompt body for a specific user-invoked action. | Keep the command content public-safe and update it when repo rules change. |
| Script-assisted skill | Run a documented helper script when the user and skill allow it. | Audit the script, dependencies, inputs, and outputs before reuse. |

Do not give a skill authority to approve its own output, bypass review, merge,
push, read secrets, or widen scope. A skill is a procedure; it is not a
maintainer.

## Beginner Friendliness

Medium. Skills are useful after a learner understands normal Claude Code
use, Git branches, and review. Beginners should start with one read-only
docs skill before adding scripts or write-capable workflows. Custom slash
commands are a good next step after that, since they are just a single
Markdown file with no bundled scripts to audit.

## Installation

Use the official Claude Code skills documentation as the source of truth.

Placeholder until verified for a target environment:

```powershell
# Placeholder only. Verify the current official Claude Code skill path first.
New-Item -ItemType Directory -Path .\skills\example-skill -Force
New-Item -ItemType File -Path .\skills\example-skill\SKILL.md -Force
```

Do not publish exact global install commands unless they are checked against
official docs in the same PR.

## Required Files And Folder Shape

Typical skill bundles include:

```text
example-skill/
  SKILL.md
  references/
  scripts/
  assets/
```

Only `SKILL.md` should be mandatory for the simplest public example. Add
scripts only when they are necessary and safe to run.

Custom slash commands are simpler -- one file per command:

```text
.claude/commands/
  goal.md
  review-docs.md
```

## Minimal Skill Anatomy

For a public-safe Claude Code skill, start with a `SKILL.md` that has these
sections before adding references or scripts:

```markdown
# Skill Name

Trigger:
Use when...

Do not use when:
- The task touches secrets, credentials, or private files.
- The scope is unclear.

Purpose:
One short paragraph explaining the repeated task.

Inputs required:
- Files or topic.
- Audience.
- Allowed scope.

Procedure:
1. Read repository instructions.
2. Inspect target files.
3. Confirm scope.
4. Do the smallest safe action.
5. Verify and report.

Verification:
- Commands to run or manual evidence to collect.

Final report:
- Files read.
- Files changed.
- Commands run.
- Checks passed/failed.
- Claims needing official-doc verification.
```

Only add `references/` when the skill needs stable public guidance, and only
add `scripts/` when a simple prompt cannot do the job safely. Scripts should
use existing project patterns and avoid new dependencies unless explicitly
approved.

## Worked Example: Writing A Custom Command

This example creates a `/review-docs` command that asks Claude Code to
review a named doc for the same things this repository's skill docs already
check for: clarity, safety boundaries, and unverified claims.

1. Create the folder if it does not exist yet:

   ```powershell
   New-Item -ItemType Directory -Path .\.claude\commands -Force
   ```

2. Create `.claude\commands\review-docs.md` with this content:

   ```markdown
   ---
   description: Review a public doc for clarity, safety, and unverified claims
   ---

   Read AGENTS.md first.

   Then read the file the user names in $ARGUMENTS.

   Review it for:
   - Beginner clarity.
   - Missing safety boundaries.
   - Unsupported or fast-changing product claims that need an
     official-doc verification note.
   - Private paths, private links, or token-looking examples.

   Do not edit the file unless the user explicitly asks.

   Report findings ordered by severity, then list files reviewed and any
   claims that still need verification.
   ```

3. Invoke it in a Claude Code session:

   ```text
   /review-docs docs/skills/mcp.md
   ```

4. Review Claude's response like any other output -- it is a prompt shortcut,
   not an automated pipeline. If the command should also run repository
   checks, add those exact commands into the Markdown body (for example
   `python scripts/repo_health_check.py`) so Claude runs them as part of
   following the instructions, not by inventing its own.

This is the same pattern as `/goal` in this repository: a plain-text prompt
saved once, invoked by name, editable like any other file, and safe to
version-control because it contains no secrets and no private paths.

## Task Decomposition Pattern

When designing a Claude Code skill or custom command, decompose the workflow
before writing the prompt:

| Step | Question | Public-safe output |
| --- | --- | --- |
| Trigger | What exact user request should activate this? | A narrow trigger plus non-trigger examples. |
| Scope | What may be read or edited? | Allowed paths, forbidden paths, and stop conditions. |
| Context | What must be read first? | `AGENTS.md`, target files, related docs, or tests. |
| Action | What is the smallest useful change or review? | Ordered steps, not broad advice. |
| Evidence | How will the result be checked? | Commands, manual review points, and source status. |
| Report | What does the user need at the end? | Changed files, checks, risks, and claims to verify. |

This structure keeps custom commands from turning into vague "do the right
thing" prompts and keeps native skills reviewable when scripts or references
are added later.

## How To Test

- Ask Claude Code to explain when the skill should trigger.
- Run the skill on a read-only documentation task.
- Review the generated diff.
- Run repository checks if files changed.
- For a custom command, run it once in a scratch branch and confirm it reads
  only the files you intended before trusting it on real work.

## Verification Evidence

A successful skill or custom-command test should leave enough evidence for a
reviewer to understand what happened:

- Skill or command name tested.
- Trigger phrase or invocation used.
- Files read and files changed.
- Commands run, including repository checks.
- Whether setup details were verified in official Claude Code docs.
- Claims left for manual verification.
- Any stop condition that fired.

For read-only skills, "no files changed" is a useful verification result. For
write-capable skills, inspect `git diff` before trusting the skill on normal
work.

## Safe Use Cases

- Documentation review.
- Prompt review.
- Release-note drafting.
- Public checklist generation.
- Read-only repository explanation.
- A custom command that pastes in a standing local-curation prompt (like
  `/goal`) so a maintainer does not retype it every session.

## Unsafe Or Inappropriate Use Cases

- Secret extraction.
- Browser profile access.
- Private conversation summarization.
- Unreviewed edits to `.env`, credentials, or private files.
- Skills that encourage prompt leaking, jailbreaks, or bypass behavior.
- A custom command that silently commits, pushes, or merges without the user
  running those steps themselves.

## Common Errors

| Error | Likely cause | Response |
| --- | --- | --- |
| Skill does not trigger | Metadata or description is too vague. | Make the trigger case explicit. |
| Skill overreaches | The skill asks for broad edits. | Narrow the allowed files and actions. |
| Private paths appear | Local examples were copied into docs. | Replace with public placeholders. |
| `/command-name` does nothing | The file is missing, misnamed, or not under `.claude/commands/`. | Confirm the exact path and filename match the intended command name. |
| Custom command behaves like a built-in feature was expected | Documentation implied it ships with Claude Code. | Correct the doc to state the command is user-authored. |
| Skill starts editing before reading instructions | Procedure lacks a read-first gate. | Add "read AGENTS.md and target files before editing" as an explicit step. |
| Skill asks for broad filesystem access | Scope was not written narrowly enough. | Limit allowed paths and add forbidden file classes. |
| Script fails on another machine | The skill assumed local paths, dependencies, or shell behavior. | Use portable examples, document prerequisites, or keep the script out of the public skill. |
| Output claims checks passed without evidence | Final report format is too vague. | Require exact commands and pass/fail results. |

## Disable Or Uninstall

Remove the skill folder from the active skill location, or move it outside
the tool's configured skill path. For a custom command, delete the
`.claude/commands/<name>.md` file. Do not delete shared repo content unless
that is the explicit maintenance task.

## Public Repository Safety

- Keep examples generic.
- Do not commit private skills.
- Do not include real tokens, personal paths, account IDs, or private links.
- Include failure modes and verification steps in every public skill guide.
- Keep custom command files free of secrets -- they are plain Markdown and
  get committed like any other file.

## Skill Design Checklist

- [ ] The skill has a narrow trigger.
- [ ] `SKILL.md` can be read without private context.
- [ ] References are public-safe.
- [ ] Scripts are optional and documented.
- [ ] The skill starts read-only when possible.
- [ ] Write-capable actions name allowed files.
- [ ] The skill avoids hidden prompts, private memories, and credentials.
- [ ] The skill final report is reviewable.
- [ ] Product behavior is official-doc verified or marked for verification.
- [ ] Custom slash commands are labeled user-authored, not built-in.
- [ ] The skill has stop conditions for unclear scope, dependency changes,
      destructive actions, private data, and failing checks.
- [ ] The disable path is documented.

## Review Rubric

| Area | Accept | Revise |
| --- | --- | --- |
| Trigger | Specific enough that a maintainer can predict when it loads. | Broad "use for all repo work" language. |
| Scope | Names allowed files/actions and forbidden files/actions. | Leaves secrets, private paths, or workflow changes implicit. |
| Source status | Official-doc details are verified or clearly marked. | Exact setup behavior is asserted without a current source. |
| Beginner path | Starts read-only and explains how to test safely. | Begins with broad write access or scripts. |
| Custom commands | Correctly described as user-authored Markdown shortcuts. | Implies `/goal` or repo-specific commands ship with Claude Code. |
| Evidence | Requires files changed, commands run, checks, and unresolved claims. | Ends with an unstructured summary. |
| Disable path | Explains how to remove or move the skill/command. | Gives no way to stop using it safely. |

## Example Read-Only Skill Brief

```markdown
# Public Docs Reviewer

Trigger:
Use when the user asks for a documentation review in this repository.

Procedure:
1. Read AGENTS.md.
2. Read README.md and requested docs.
3. Review for clarity, safety, source support, and verification.
4. Do not edit files.
5. Report findings first, ordered by severity.

Forbidden:
- Secrets.
- Private links.
- Private machine paths.
- Exact current tool claims without official-doc verification.
```

## Write-Capable Skill Gate

Before a Claude Code skill edits files:

1. It should name files in scope.
2. It should name files out of scope.
3. It should avoid dependency changes unless explicitly approved.
4. It should run or request the relevant checks.
5. It should report changed files and risks.

If those gates are missing, keep the skill read-only. The same gate applies
to a custom slash command that is allowed to edit files: name the scope in
the command's own Markdown body, since there is no separate manifest to
enforce it.

## Review Questions

- Does the skill trigger too broadly?
- Does it duplicate a normal prompt template?
- Are local examples generic and public-safe?
- Are source claims official-doc verified or conservative?
- Does the guide explain how to disable the skill?
- Does it state what to do when checks fail?
- If this is a custom slash command, does the doc correctly call it
  user-defined rather than implying it is a native Claude Code feature?
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/skills/claude-code.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `claude code` state what decision, workflow, or reusable behavior it supports?
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
