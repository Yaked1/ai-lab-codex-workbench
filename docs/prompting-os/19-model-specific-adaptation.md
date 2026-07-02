# Model-Specific Adaptation

Prompting OS is model-family oriented, not model-worship oriented. Different
models and tools reward different prompt shapes, but the kernel remains stable:
goal, context, constraints, method, format, verification, and failure behavior.

This module explains how to adapt without depending on brittle product claims.

## Adaptation Principles

1. Start with the universal kernel.
2. Choose the driver family.
3. Add tool-specific constraints only when needed.
4. Keep fast-changing behavior in official-doc references.
5. Do not hard-code pricing, model access, or product defaults unless verified.
6. Record what was tested.

## Chat Models

Best for:

- Explanation.
- Summarization.
- Drafting.
- Rewriting.
- Brainstorming.
- Tutoring.

Prompt emphasis:

- Audience.
- Tone.
- Output shape.
- Depth.
- Examples.
- Uncertainty behavior.

Failure mode:

- Confident generic prose.

Repair:

- Add concrete audience, examples, and pass/fail criteria.

## Reasoning Models

Best for:

- Complex analysis.
- Debugging.
- Planning.
- Math.
- Tradeoff evaluation.
- Architecture review.

Prompt emphasis:

- Exact problem.
- Constraints.
- Definitions.
- Edge cases.
- Verification.
- Concise rationale.

Do not ask for hidden scratchpad. Ask for assumptions, checks, conclusions, and
what would change the answer.

## Coding Agents

Best for:

- Repository edits.
- Tests.
- Diffs.
- Package builds.
- Script repair.
- Documentation updates tied to files.

Prompt emphasis:

- Current branch/worktree.
- Files to read.
- Allowed edits.
- Forbidden edits.
- Checks.
- Staging/commit instructions.
- Final report.

Failure mode:

- Agent does broad unrelated work.

Repair:

- Tight file scope and explicit forbidden actions.

## RAG Systems

Best for:

- Source-grounded answers.
- Policy lookup.
- Documentation Q&A.
- Research synthesis.

Prompt emphasis:

- Source ledger.
- Citation rules.
- Missing-info behavior.
- Conflict handling.
- Prompt-injection defense.

Failure mode:

- Weak source becomes confident answer.

Repair:

- Label source authority and require claim-source mapping.

## Structured Output Systems

Best for:

- Extraction.
- Classification.
- Routing.
- Manifests.
- Data transformation.

Prompt emphasis:

- Schema.
- Enums.
- Required fields.
- Empty and null behavior.
- Invalid-output repair.

Failure mode:

- Extra prose breaks parsers.

Repair:

- "Return valid JSON only" plus schema validation.

## Image Models

Best for:

- Visual concepts.
- Product shots.
- Diagrams.
- Storyboards.
- UI assets.
- Edits and revisions.

Prompt emphasis:

- Subject inventory.
- Composition.
- Spatial relations.
- Style.
- Lighting.
- Constraints.
- Revision criteria.

Failure mode:

- Looks good but violates layout.

Repair:

- Define checkable visual requirements.

## Small Or Local Models

Best for:

- Narrow extraction.
- Local drafts.
- Offline experiments.
- Low-risk transformations.

Prompt emphasis:

- Short context.
- One task.
- Clear schema.
- Few examples.
- Simple language.

Failure mode:

- Long instruction loss.

Repair:

- Split into multiple steps.

## Adaptation Record

```yaml
task:
driver_family:
tool_or_model:
date_checked:
official_docs_checked:
prompt_changes:
verification:
known_limitations:
```

## Product Claim Discipline

Model-specific prompts often drift into unsupported product claims. Avoid
hard-coding:

- Exact model availability.
- Exact pricing.
- Account tier behavior.
- UI labels.
- Default settings.
- Rate limits.
- Regional availability.
- Hidden system behavior.

If a prompt depends on current product behavior, add:

```text
Verify this in official docs before relying on it. If official docs are not
available, mark the behavior unverified.
```

## Migration Between Models

When moving a prompt from one model or tool to another:

1. Keep the kernel unchanged.
2. Remove tool-specific assumptions.
3. Re-select the driver.
4. Re-test format behavior.
5. Re-test safety boundaries.
6. Re-test missing-information behavior.
7. Record known differences.

Migration table:

| From | To | Watch for |
| --- | --- | --- |
| Chat model | Coding agent | Need file scope and checks. |
| Coding agent | Chat model | Remove file-write assumptions. |
| RAG | Chat model | Remove source-only claims or provide sources. |
| Chat model | Structured output | Add schema and invalid-output rules. |
| Image prompt | Text prompt | Convert visual criteria to prose criteria. |

## Adaptation Checklist

- [ ] Kernel still has goal, context, scope, format, verification.
- [ ] Driver family is correct.
- [ ] Tool-specific assumptions are explicit.
- [ ] Current product behavior is verified or marked unverified.
- [ ] Output format was tested.
- [ ] Safety behavior was tested.
- [ ] Old cases were re-run.
- [ ] Known limitations are recorded.

## Adaptation Failure Cases

| Failure | Example | Repair |
| --- | --- | --- |
| Tool assumption leak | Chat prompt tells model to edit files. | Remove file-write procedure or switch to coding-agent driver. |
| Source rule missing | RAG prompt moved to chat model invents facts. | Provide sources or remove source-grounded claims. |
| Schema weakness | Structured prompt works in one model but emits prose in another. | Add strict JSON-only rule and validation. |
| Context overload | Small model ignores late constraints. | Split task and shorten context. |
| Visual drift | Image prompt copied from text prompt has no layout. | Add subject inventory and spatial relations. |

## Driver Test Pack

When adapting a prompt, test at least:

1. Happy path.
2. Missing information.
3. Format constraint.
4. Safety boundary.
5. Tool boundary, if tools exist.

Record the result in the adaptation record. If one driver cannot satisfy the
task reliably, choose a different driver instead of adding more prose.

## Final Rule

Adapt prompts to model families, but do not let model-specific folklore replace
verification.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/19-model-specific-adaptation.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `19 model specific adaptation` state what decision, workflow, or reusable behavior it supports?
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
