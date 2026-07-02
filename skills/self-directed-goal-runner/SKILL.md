---
name: self-directed-goal-runner
description: Use when a human hands the agent a broad, multi-step goal and wants it pursued to completion without being re-prompted for every step. This skill generates a bounded, checklist-driven self-prompt, then follows it -- it is the "skill that makes a skill and follows it" pattern, kept safe with hard stop conditions and an iteration cap.
category: meta
source:
  - docs/templates/task-spec.md
  - AGENTS.md
  - docs/skills/README.md
---

# Self-Directed Goal Runner

## Trigger

Use this skill when a goal is broad enough that it decomposes into several
ordered steps, and the human wants the agent to keep working through them
without stopping after each one to ask "what next?" Do not use it for a
single well-scoped edit -- that needs no loop, just do it. Do not use it for
anything destructive, anything touching secrets, or anything the human has
not actually authorized at the goal level; this skill amplifies whatever
scope it is given, so an underspecified goal becomes an underspecified loop.

## Purpose

Turn one broad instruction into a self-maintained checklist the agent
follows across many turns, with an explicit definition of done, explicit
stop conditions, and a hard iteration cap -- so "follow this until complete"
never becomes "run forever" or "silently expand scope."

## Inputs

- The goal, in the human's own words.
- Any explicit scope boundaries the human already stated (files, folders,
  what must not change).
- An optional iteration cap override (default: 25) and stall-guard override
  (default: 3 consecutive iterations with no checked box).

## Scope

This skill may only create and edit its own self-prompt file under
`.tmp/self-prompts/<slug>.md` (already outside version control -- see the
repository's `.gitignore`) and the files the generated checklist explicitly
names as in scope for the underlying goal. It may never expand the
underlying goal's scope beyond what the human stated; if a step seems to
require touching an unlisted file, that step becomes a stop condition (see
Failure Cases), not silent scope creep.

## Procedure

1. **Restate the goal as a task spec.** Fill out
   [docs/templates/task-spec.md](../../docs/templates/task-spec.md)'s
   fields for this goal: objective, audience, files explicitly in scope,
   files explicitly out of scope, verification commands, and a concrete
   definition of done. If any of these cannot be filled in confidently,
   stop here and ask the human -- do not guess at scope.
2. **Write the self-prompt.** Create `.tmp/self-prompts/<slug>.md`
   containing the filled task spec plus a literal checklist of ordered,
   independently-checkable steps (`- [ ] step`), the iteration cap, the
   stall-guard count, and a running log section (empty at first).
3. **Loop, one step per iteration:**
   1. Re-read `.tmp/self-prompts/<slug>.md` in full.
   2. If every box is checked, stop -- go to Final Report.
   3. If any hard stop condition applies (see Failure Cases), stop -- go
      to Final Report and escalate to the human instead of continuing.
   4. Otherwise, do the next unchecked step, and only that step.
   5. Run the verification command relevant to that step.
   6. Check the box, append one log line (what happened, what passed),
      and increment the iteration counter recorded in the file.
   7. If the iteration counter has now reached the cap, stop -- go to
      Final Report even if boxes remain unchecked.
4. **Never let the loop outlive the file.** If `.tmp/self-prompts/<slug>.md`
   is deleted, missing, or unreadable at the start of an iteration, stop
   immediately and report that the loop's state was lost -- do not
   reconstruct it from memory and keep going.

## Verification

Run whatever the task spec's own verification section names, plus, if this
repository's conventions apply:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Every iteration must run its step's relevant check before the box is
checked -- a checked box with no verification behind it is not a completed
step, it is an unverified guess.

## Failure Cases (Hard Stop Conditions)

Stop and escalate to the human -- do not continue the loop -- when:

- The goal's scope was ambiguous at intake and could not be resolved from
  the human's own words.
- A step would touch `.env`, `.env.*`, credentials, or any file outside the
  explicitly-scoped list.
- A step would add a new dependency, edit CI/workflow YAML, force-push,
  delete a branch, or take any other destructive or hard-to-reverse action.
- A verification command fails and the cause is not obviously within the
  current step's scope to fix.
- The stall guard trips: the configured number of consecutive iterations
  (default 3) complete with no checkbox newly checked.
- The iteration cap (default 25) is reached, regardless of remaining boxes.
- The self-prompt file is missing, corrupted, or was edited by something
  other than this loop between iterations.

None of these are "pause and silently retry." Every one of them ends the
loop and produces a Final Report for a human to read.

## Final Report

Every run -- successful, escalated, or capped -- ends with:

- The self-prompt file's final checklist state (checked vs. unchecked).
- Total iterations used versus the cap.
- Which stop condition ended the loop, if any (state "completed" if all
  boxes were checked normally).
- Files actually changed, commands run, and their results.
- What still needs a human decision, if the loop stopped early.

## Disable Path

Delete `.tmp/self-prompts/<slug>.md` to end an in-progress loop immediately
-- the next iteration will find it missing and stop per the procedure
above. Removing this skill's folder from the install location (see
[skills/README.md](../README.md#installer-behavior)) prevents new loops
from starting; it does not affect any loop's already-written self-prompt
file, since that file lives outside this skill's own folder.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **installable agent skill** surface. During broad
maintenance, reviewers should treat `skills/self-directed-goal-runner/SKILL.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `self directed goal runner` state what decision, workflow, or reusable behavior it supports?
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
