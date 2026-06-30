# Prompt Quality Rubric

Use this rubric to review prompt files before they become reusable assets or
ship in a package. It is intentionally practical: a prompt is good when it
produces useful, reviewable behavior under realistic conditions.

## Score Summary

| Score | Meaning | Ship? |
| ---: | --- | --- |
| 0 | Fails the task, violates constraints, or is unsafe. | No. |
| 1 | Has a task but lacks scope, format, or safety boundaries. | No. |
| 2 | Works for a simple happy path but fails edge cases. | Only as a draft. |
| 3 | Clear goal, relevant context, explicit scope, and usable format. | Yes for low-risk use. |
| 4 | Adds verification, failure behavior, source discipline, and reviewability. | Yes for reusable prompts. |
| 5 | Tested, versioned, source-aware, safe, concise, and resilient to misuse. | Yes for packaged prompts. |

## Dimensions

Score each dimension from 0 to 5.

| Dimension | 0 | 3 | 5 |
| --- | --- | --- | --- |
| Goal | No clear deliverable. | Specific output and audience. | Output, audience, use case, and success criteria are all explicit. |
| Context | Missing or noisy. | Relevant facts included. | Context is layered, trusted, current where needed, and separated from instructions. |
| Scope | Unbounded. | Include/exclude rules present. | Scope names files/actions/topics, forbidden work, and escalation behavior. |
| Format | Vague prose. | Output shape stated. | Output is schema-like, examples exist, and malformed output is detectable. |
| Verification | None or "check it." | Manual or command check listed. | Checks, rubrics, cases, and failure reporting are explicit. |
| Safety | No privacy or tool boundary. | Basic private-data warning. | Secrets, prompt injection, permissions, destructive actions, and source trust are handled. |
| Robustness | Works once. | Handles common missing-info cases. | Includes edge cases, abuse cases, and regression expectations. |
| Maintainability | Anonymous text. | Named prompt with purpose. | Version, owner, source status, changelog, and test path are present. |

## Pass Thresholds

| Use case | Minimum |
| --- | --- |
| One-off personal brainstorming | 2, if no private data or tools are involved. |
| Public documentation prompt | 3, with source and safety checks. |
| Coding-agent work order | 4, because file writes and tests are involved. |
| RAG or source-grounded answerer | 4, because unsupported claims are likely. |
| Tool-using or automation prompt | 4, with explicit permissions. |
| Packaged reusable prompt | 5 or a documented 4 with known limitations. |

## Review Procedure

1. Read the prompt without the author's explanation.
2. Identify the deliverable, audience, scope, format, and checks.
3. Classify the target driver: chat, reasoning, coding-agent, RAG, image,
   structured-output, or tool-agent.
4. Score each dimension.
5. Run or mentally simulate one normal case.
6. Run or mentally simulate one edge case.
7. Run or mentally simulate one abuse case if tools, sources, or private data
   are involved.
8. Record the weakest dimension and the smallest useful fix.

## Required Evidence

A prompt review should cite at least one of these:

- Output from a command or script.
- A rendered or parsed artifact.
- A source citation.
- A schema validation result.
- A human review table.
- A before/after comparison.
- A package manifest.
- A test fixture.

Do not accept "the model said it looks good" as evidence.

## Common Defects

| Defect | Symptom | Repair |
| --- | --- | --- |
| Persona-only prompt | Long role text, no deliverable. | Add goal, context, scope, output, and verification. |
| Scope leak | Model changes unrelated topics or files. | Add include/exclude lists and forbidden actions. |
| Source blur | Model mixes source facts and inference. | Add source ledger and inference labels. |
| Format drift | Output shape changes between runs. | Add exact schema or examples. |
| Safety gap | Prompt allows secrets or broad tools. | Add permission profile and blocked actions. |
| Evaluation gap | Prompt has no test cases. | Add golden, edge, and abuse cases. |
| Maintenance gap | No owner or version. | Add metadata and changelog rule. |

## Example Review Table

```markdown
| Dimension | Score | Evidence | Fix |
| --- | ---: | --- | --- |
| Goal | 4 | Deliverable and audience are explicit. | Add success metric. |
| Context | 3 | Relevant files named. | Separate trusted and untrusted context. |
| Scope | 5 | Include/exclude paths listed. | None. |
| Format | 4 | Final report format exists. | Add JSON schema if automated. |
| Verification | 3 | Commands listed. | Add failure behavior for skipped checks. |
| Safety | 4 | Secrets and destructive actions blocked. | Add prompt-injection rule. |
| Robustness | 2 | No edge cases. | Add stale-source and dirty-tree cases. |
| Maintainability | 3 | Prompt has a name. | Add version and owner. |
```

## Red Flags

- The prompt asks for "best" without a scoring function.
- The prompt asks for current product behavior without requiring verification.
- The prompt asks an agent to edit files without file boundaries.
- The prompt grants tools without approval gates.
- The prompt uses leaked or proprietary text as reusable content.
- The prompt includes real or realistic-looking credentials.
- The prompt has no way to report uncertainty.
- The prompt cannot be reviewed without trusting model confidence.

## Package Gate

Before a prompt or guide ships in the Prompting OS ZIP:

- [ ] It is original or source-inspired, not copied from prompt dumps.
- [ ] It has enough technical detail to teach a workflow.
- [ ] It includes examples, failure modes, or review questions.
- [ ] It links or points to source policy when external sources matter.
- [ ] It avoids private paths, secrets, and hidden vendor prompts.
- [ ] It can be checked by a human or script.
- [ ] It ends with a clear rule, checklist, or next action.

Length is not the score, but extremely short files rarely satisfy this package
gate. A packaged file should usually teach a complete concept, not only name it.
