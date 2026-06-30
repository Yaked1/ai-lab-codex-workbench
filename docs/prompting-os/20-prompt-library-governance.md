# Prompt Library Governance

A prompt library is a product surface. If prompts are reused, shared, packaged,
or taught, they need governance: naming, ownership, source status, review,
testing, deprecation, and release discipline.

## Prompt Asset Types

| Type | Example | Governance need |
| --- | --- | --- |
| One-off prompt | A single docs request. | Low, but keep safety. |
| Work-order template | Coding-agent docs update. | Inputs, scope, checks. |
| Skill prompt | Reusable tool or agent skill. | Trigger, procedure, failure behavior. |
| RAG prompt | Source-grounded answerer. | Source ledger and injection defense. |
| Structured prompt | JSON extraction. | Schema validation. |
| Image prompt | Visual generation or revision. | Visual rubric. |
| System prompt | Durable behavior instructions. | Highest review and safety. |

## Required Metadata

```yaml
id:
title:
version:
owner:
target_tool:
purpose:
inputs:
outputs:
safety_boundaries:
verification:
failure_cases:
source_status:
last_reviewed:
```

The metadata can be written in YAML, tables, or prose. What matters is that a
reviewer can answer: what is this prompt for, how is it used, and how is it
checked?

## Source Status Labels

| Label | Meaning |
| --- | --- |
| Original | Written for this repository. |
| Source-inspired | Structure learned from public sources, text is original. |
| Official-doc-grounded | Behavior depends on official docs. |
| Experimental | Not yet reliable. |
| Deprecated | Kept for history or migration only. |
| Blocked | Unsafe, private, or unsuitable for public release. |

## Review Workflow

1. Confirm prompt purpose.
2. Confirm target tool.
3. Check inputs and outputs.
4. Check safety boundaries.
5. Check source status.
6. Run or simulate normal, edge, and abuse cases.
7. Score with rubric.
8. Update version or changelog.
9. Package only if public-safe.

## Library Folder Structure

```text
prompts/
  codex/
  claude-code/
  cursor/
  github-copilot/
docs/prompting-os/templates/
docs/prompting-os/evals/
```

Keep prompts near the tool or workflow they serve. Avoid one giant file of
unlabeled prompts.

## Review Roles

| Role | Responsibility |
| --- | --- |
| Author | Writes the prompt and examples. |
| Reviewer | Checks scope, safety, and usefulness. |
| Source reviewer | Confirms attribution and source status. |
| Maintainer | Decides whether it belongs in the package. |
| User | Reports failures and unclear instructions. |

For small projects, one person may hold multiple roles. The roles still help
make the review complete.

## Change Control

Prompt changes should state:

- What behavior changed.
- Why it changed.
- Which cases were tested.
- Whether output format changed.
- Whether safety behavior changed.
- Whether downstream users must migrate.

Change note template:

```markdown
Prompt:
Version:
Change:
Reason:
Cases run:
Risks:
Migration:
```

## Package Inclusion Criteria

A prompt belongs in a package when:

- It serves a repeated workflow.
- It can be understood without private context.
- It has clear inputs and outputs.
- It has safety boundaries.
- It has verification steps.
- It has failure cases.
- It is not copied from unsafe sources.

A prompt should stay local or experimental when:

- It depends on private files.
- It depends on one person's memory.
- It has not been tested.
- It contains current product claims that were not verified.
- It overlaps heavily with an existing prompt.

## Governance Metrics

Track lightweight metrics:

- Prompt count by target tool.
- Prompts with owners.
- Prompts with failure cases.
- Prompts with verification steps.
- Deprecated prompts.
- Prompts with source status.
- Prompts changed since last release.

Metrics should guide review, not become vanity numbers. A library with fewer
well-reviewed prompts is better than a large library full of anonymous prompt
text.

## Governance Review Questions

- Does this prompt solve a repeated problem?
- Is it different from existing prompts?
- Can a new user fill the inputs correctly?
- Does it name what not to do?
- Does it protect private data?
- Does it avoid leak-derived content?
- Can it be tested or reviewed?
- Is it clear who should maintain it?

If the answer to any of these is no, the prompt can still exist as a draft, but
it should not be packaged as a reusable asset yet.

## Deprecation Policy

Deprecate when:

- Product behavior changed.
- Output schema changed.
- Safety boundary is outdated.
- Better prompt replaces it.
- Source status is unclear.

Deprecation note:

```text
Deprecated: [date]
Reason:
Replacement:
Migration:
```

## Public Release Gate

- [ ] Prompt is original or source-inspired.
- [ ] No private data.
- [ ] No leaked prompt text.
- [ ] Inputs are documented.
- [ ] Output is checkable.
- [ ] Failure behavior exists.
- [ ] Evaluation or review case exists.
- [ ] Source status is clear.
- [ ] Changelog updated if user-visible.

## Final Rule

A prompt library without governance is just a text pile. Governance turns prompt
text into reusable infrastructure.
