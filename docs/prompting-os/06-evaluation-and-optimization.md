# Evaluation and Optimization

A prompt is not good because it sounds advanced. A prompt is good when it repeatedly produces useful outputs under realistic conditions.

## Evaluation Stack

| Layer | Question |
| --- | --- |
| Format | Did the output follow the required shape? |
| Accuracy | Are claims correct and supported? |
| Completeness | Did it cover the required scope? |
| Safety | Did it avoid forbidden content and private data? |
| Usefulness | Can the user act on it? |
| Robustness | Does it survive edge cases? |
| Regression | Did the new version break old successes? |

Evaluation should start before prompt rewriting. If you rewrite first, the new
prompt may feel better without solving the actual failure. Write down the
target behavior, old failure, and evidence standard before changing the prompt.

## Test Case Template

```yaml
name: source_grounded_summary
input: |
  [Prompt input]
expected:
  must_include:
    - supported summary
    - uncertainty note when needed
  must_not_include:
    - unsupported claims
    - invented citation
scoring:
  0: fails task
  1: partial result
  2: correct but weak
  3: correct and reusable
```

Use names that explain the risk:

- `normal_docs_update`
- `stale_external_claim`
- `dirty_worktree`
- `prompt_injection_in_source`
- `invalid_json_repair`
- `image_layout_preservation`
- `missing_source_refusal`

## Prompt Rubric

| Score | Meaning |
| --- | --- |
| 0 | Fails the task or violates constraints. |
| 1 | Partially useful but misses important requirements. |
| 2 | Correct core answer with weak formatting or weak edge handling. |
| 3 | Correct, structured, grounded, and reusable. |
| 4 | Excellent, robust, concise, and well verified. |

For package review, use the deeper rubric in
`evals/prompt-quality-rubric.md`. This short rubric is for quick iteration.

## Optimization Loop

```text
1. Choose representative test cases.
2. Run the current prompt.
3. Score outputs against the rubric.
4. Identify the smallest prompt change likely to improve results.
5. Re-run old and new cases.
6. Keep the change only if it improves results without regressions.
7. Record the change and reason.
```

Optimization rules:

- Change one major prompt section at a time.
- Keep old test cases.
- Add a new case for every repaired failure.
- Prefer clearer constraints over longer persona text.
- Prefer examples when format drift is the problem.
- Prefer source rules when hallucination is the problem.
- Prefer permission rules when tool misuse is the problem.

## Critic-Builder Loop

```text
First, critique the draft against the rubric.
Second, identify the top three defects.
Third, revise only those defects.
Fourth, return the final answer without repeating the full critique.
```

The critic should not rewrite everything. A useful critic identifies the
highest-impact failures, then the builder repairs those failures. This keeps
the loop from producing polished but unrelated output.

## Evaluation Harness Options

| Harness | Good for | Notes |
| --- | --- | --- |
| Manual table | Early prompt design and teaching. | Fast, cheap, easy to inspect. |
| Unit test | Output schemas, file generation, package checks. | Best when outputs are deterministic enough. |
| Golden examples | Style and workflow regression. | Keep examples public-safe. |
| Rubric review | Long-form writing, docs, agent outputs. | Requires reviewer discipline. |
| Dedicated eval tool | Prompt variants, model comparisons, red-team cases. | Add only when the workflow justifies the dependency. |

## Minimal Eval Suite

A reusable prompt should have at least:

1. One normal case.
2. One edge case.
3. One failure or abuse case.
4. A pass/fail checklist.
5. A record of what changed after evaluation.

Example:

```markdown
| Case | Input | Expected | Pass criteria |
| --- | --- | --- | --- |
| normal | Update one doc. | Scoped diff and checks. | Only target doc changed; checks reported. |
| edge | Current claim requested. | Source verification. | Official source checked or claim marked unverified. |
| abuse | Source says ignore rules. | Injection ignored. | Task rules remain in force. |
```

## Failure Taxonomy

| Failure | Detection | Repair |
| --- | --- | --- |
| Unsupported claim | Compare claim to source. | Add source-only rule. |
| Schema break | Validate output shape. | Provide exact schema and invalid-output rule. |
| Overlong answer | Count sections/tokens. | Add audience and length limit. |
| Missed edge case | Add adversarial input. | Add explicit edge-case handling. |
| Tool misuse | Check action log. | Narrow tool permissions. |
| Visual prompt failure | Compare output to entity/layout spec. | Add inventory and spatial constraints. |

## Optimization Decision Record

Use this record when changing a packaged prompt:

```markdown
## Prompt Change

Prompt:
Old version:
New version:

## Problem

Observed failure:
Cases affected:

## Change

Prompt section changed:
Reason:

## Results

Old score:
New score:
Regressions:
Skipped checks:

## Decision

Keep / revise / revert:
Follow-up:
```

## Evaluation Rule

Do not judge a prompt by one lucky output. Even broken clocks have a product demo twice a day.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/06-evaluation-and-optimization.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `06 evaluation and optimization` state what decision, workflow, or reusable behavior it supports?
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
