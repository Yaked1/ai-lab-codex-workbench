# Context Engineering and RAG

Context engineering is the art of deciding what the model sees, in what order, with what labels, and with what trust level.

Prompting without context engineering is just shouting into a very expensive autocomplete canyon.

## Context Layers

| Layer | Content | Rule |
| --- | --- | --- |
| System/developer rules | Stable behavior constraints | Keep short and non-conflicting. |
| Task prompt | Current goal and format | Make specific and testable. |
| Source context | Documents, snippets, data | Label source, date, reliability, and scope. |
| Examples | Few-shot demonstrations | Use high-quality examples only. |
| Memory | Prior decisions and preferences | Include only what affects the task. |
| Tool observations | Search, files, tests, logs | Treat as evidence, not decoration. |

Context engineering is the act of deciding what the model should see, what it
should ignore, and how it should interpret each piece. More context is not
automatically better. The right context is small enough to follow and rich
enough to verify.

## Context Ledger

Use this for large tasks:

```text
Task:
[What is being solved]

Loaded context:
- [Source/file]: [why it matters]

Skipped context:
- [Source/file]: [why it was not needed]

Trust levels:
- High: official docs, provided source text, test output
- Medium: reputable community docs, maintained examples
- Low: old notes, forum posts, unclear summaries

Assumptions:
- [Assumption] — confidence: [low/medium/high]

Open questions:
- [What remains unknown]
```

Use the ledger when:

- A task spans multiple turns.
- External sources were checked.
- A source may be stale.
- The model must distinguish instructions from evidence.
- A reviewer needs to know why certain files were read.

The ledger does not need to be long. Its job is to prevent silent assumptions.

## RAG Prompt Contract

```text
Use only the provided sources.
Answer only claims supported by the sources.
Cite or point to the supporting source for each non-obvious claim.
If sources conflict, describe the conflict.
If sources are insufficient, say what is missing.
Do not fill source gaps from memory.
```

Retrieved text can contain malicious or irrelevant instructions. A source that
says "ignore your previous instructions" is not a higher-priority instruction.
It is just text inside a source.

For public docs, add source freshness:

```text
For product behavior, pricing, model availability, platform support, or command
syntax, use official sources and state the date checked. If current official
sources are unavailable, mark the claim unverified.
```

## Retrieval Quality Checklist

- Does the source actually answer the question?
- Is the source current enough?
- Is the source authoritative for the claim?
- Is the chunk too small to preserve meaning?
- Is the chunk too large and noisy?
- Are multiple viewpoints required?
- Are tables, images, or code blocks needed?
- Did retrieval find the right document but the wrong section?

Add a retrieval rejection list:

- Secret dumps.
- Credential leaks.
- Private logs.
- License-unclear bulk prompt dumps.
- Search-result snippets without source pages.
- Outdated issue comments used as current product behavior.

Rejected sources can still be mentioned as rejected when that helps the audit.

## Context Compression

Compress context by preserving:

- Decisions.
- Definitions.
- Constraints.
- Source-backed facts.
- Unresolved questions.
- File paths or identifiers.
- Test results.

Cut:

- Polite filler.
- Repeated discussion.
- Dead branches of reasoning.
- Stale assumptions.
- Motivational noise.

Compression should preserve:

- Decisions.
- Constraints.
- Open questions.
- Evidence.
- Commands run.
- Test results.
- File paths.
- User preferences that affect the task.

Compression may drop:

- Repeated conversation filler.
- Failed speculative ideas.
- Full command output after the key result is recorded.
- Unrelated source excerpts.
- Old plans that no longer apply.

If a compressed summary changes the meaning of a requirement, it is a bug.

## Rolling Summary Template

```text
Current goal:
[Goal]

Settled decisions:
- [Decision]

Important constraints:
- [Constraint]

Current state:
- [State]

Open issues:
- [Issue]

Next best action:
- [Action]
```

## Context Budgeting

Use this priority order when the context window is limited:

1. Current user objective.
2. Local repository instructions.
3. Relevant files or source excerpts.
4. Current command output.
5. Existing tests and failure output.
6. Recent decisions.
7. Background explanation.
8. Optional examples.

If a prompt includes too many examples and too few constraints, the model may
imitate style while missing the actual acceptance criteria.

## Source Trust Table

| Source | Trust use | Risk |
| --- | --- | --- |
| Official docs | Product behavior and supported commands. | May change; cite date checked. |
| Repository files | Local architecture and conventions. | May be dirty or staged; inspect current state. |
| Test output | Current behavior evidence. | May not cover broad claims. |
| Community guides | Patterns and examples. | Not authoritative for product behavior. |
| Leaked prompt collections | Structural study only. | Do not copy or treat as current truth. |
| Model memory | Background knowledge. | May be stale or wrong. |

## RAG Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Retrieval miss | Answer says sources are silent, but answer exists elsewhere. | Improve query terms and inspect document structure. |
| Chunk blindness | The answer misses context before/after the retrieved snippet. | Retrieve neighboring sections. |
| Source laundering | Weak source becomes confident answer. | Label source quality. |
| Citation theater | Citation exists but does not support the claim. | Verify each citation against the claim. |
| Memory leakage | Model answers from memory instead of sources. | Require source-only answering. |

## Context Rule

More context is not automatically better. A thousand irrelevant tokens are just fog with invoices.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/03-context-engineering.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `03 context engineering` state what decision, workflow, or reusable behavior it supports?
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
