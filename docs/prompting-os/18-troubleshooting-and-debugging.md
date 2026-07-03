# Troubleshooting And Debugging

Prompt failures should be debugged with evidence, not vibes. This module gives
a practical diagnosis path for prompts, agents, RAG systems, structured output,
image prompts, and packages.

## Debugging Loop

```text
observe -> classify -> isolate -> repair -> rerun -> record
```

Do not rewrite the whole prompt first. Identify the smallest failed contract:
goal, context, scope, format, verification, safety, or model-driver choice.

## Failure Classifier

| Symptom | Likely class | First check |
| --- | --- | --- |
| Output answers wrong question | Goal ambiguity | Is the deliverable explicit? |
| Output is plausible but unsupported | Grounding failure | Are sources required and cited? |
| Output shape changes | Format failure | Is the schema exact? |
| Agent edits unrelated files | Scope failure | Are allowed paths named? |
| Agent skips tests | Verification failure | Are commands required? |
| Source instructions override task | Prompt injection | Is source text evidence only? |
| JSON cannot parse | Structured-output failure | Are Markdown and comments forbidden? |
| Image has wrong layout | Visual-spec failure | Are spatial relationships listed? |
| Package is too thin | Maintenance failure | Are depth gates tested? |

## Minimal Reproduction

For prompt bugs, create a minimal reproduction:

```text
Prompt version:
Input:
Expected:
Actual:
Source/context used:
Model/tool:
Checks:
Failure class:
Smallest suspected cause:
```

Keep reproductions public-safe. Do not include secrets, private documents, or
leaked prompts.

## Repair Strategies

| Failure | Repair |
| --- | --- |
| Vague answer | Add audience, deliverable, and output sections. |
| Overlong answer | Add section budget and priority order. |
| Missing detail | Add required checklist and examples. |
| Unsupported claims | Add source-only rule and missing-info behavior. |
| Hallucinated citations | Require claim-source table. |
| Scope creep | Add include/exclude path list. |
| Tool misuse | Add permission ladder and approval gates. |
| Fragile format | Add schema, valid example, invalid example. |
| Poor revision | Add preserve/change blocks. |

## Prompt Diff Review

When a prompt changes, review the diff:

- Did a constraint disappear?
- Did output format change?
- Did safety language weaken?
- Did the source policy change?
- Did verification become optional?
- Did failure behavior become vague?
- Did the prompt become longer without becoming clearer?

Prompt diffs should be reviewed like code diffs.

## Agent Debugging

Agent failures require command and file evidence.

Collect:

- `git status --short --branch`
- `git diff --stat`
- Relevant test output.
- Changed files.
- Final report.

Ask:

- Did the agent read instructions?
- Did it inspect target files?
- Did it preserve unrelated work?
- Did it run checks?
- Did it claim more than the evidence supports?

## RAG Debugging

RAG failures often come from retrieval, not generation.

Check:

- Query terms.
- Source authority.
- Source date.
- Chunk boundaries.
- Missing neighboring context.
- Citation support.
- Conflicting sources.
- Prompt-injection text.

Repair:

- Retrieve better sections.
- Add source ledger.
- Add conflict handling.
- Require missing-info output.

## Image Prompt Debugging

Image prompt failures should be mapped to visual requirements.

| Symptom | Repair |
| --- | --- |
| Wrong subject | Put subject inventory first. |
| Wrong count | Simplify entities and count explicitly. |
| Wrong position | Add foreground/midground/background and left/right relations. |
| Overstyled | Reduce style anchors. |
| Text artifacts | Avoid text or make it simple and large. |
| Revision drift | Add protected elements. |

## Package Debugging

For package issues:

```powershell
python scripts/create_prompting_os_package.py --version v1 --output-dir .\.tmp\prompting-os-package-check
```

Inspect:

- ZIP exists.
- Manifest exists.
- Required files are included.
- Excluded files are absent.
- Hashes exist.
- Markdown byte count meets threshold.
- Paths are relative.

## Regression Debugging

Prompt regressions are often subtle. The new prompt may sound better while
breaking an older use case.

Regression questions:

- What old case used to pass?
- What changed in the prompt?
- Did a constraint move lower in the prompt?
- Did an example change the style too much?
- Did a new safety rule block a valid old task?
- Did the output schema change?
- Did a tool permission become ambiguous?

Regression repair:

1. Restore the old case as a test.
2. Identify the exact prompt section that changed behavior.
3. Add a narrower instruction instead of a broad rewrite.
4. Re-run old and new cases.
5. Record the tradeoff.

## Debugging Metrics

Track:

- Failure class.
- Prompt version.
- Case name.
- Score before repair.
- Score after repair.
- Commands or checks rerun.
- Remaining risk.

Metrics are useful only when paired with examples. A score without a case does
not explain what failed.

## Debugging Record

```markdown
## Debug Record

Failure:
Evidence:
Class:
Root cause:
Repair:
Checks rerun:
Result:
Regression risk:
Follow-up:
```

## Final Rule

If you cannot name the failure class, do not rewrite the prompt yet. First make
the failure observable.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/18-troubleshooting-and-debugging.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `18 troubleshooting and debugging` state what decision, workflow, or reusable behavior it supports?
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
