# Prompt Library Indexing

A prompt library becomes useful only when readers can find the right prompt,
understand when to use it, and trust that it has been reviewed. This module
defines an indexing model for prompt assets, prompt packs, examples, rubrics,
and release packages.

The indexing model is designed for public repositories. It avoids private
metadata, secret-bearing examples, hidden system prompts, and claims that
cannot be verified.

## Index Goals

| Goal | Why it matters |
| --- | --- |
| Discovery | Readers can find prompts by task, tool, model family, risk level, and required inputs. |
| Review | Maintainers can see source status, safety boundaries, and verification expectations. |
| Packaging | Release builders can include the right assets and exclude private or generated files. |
| Deprecation | Old prompts can be replaced without silently breaking links. |
| Teaching | Instructors can assemble exercises from prompts, examples, and evaluation cases. |

## Prompt Asset Metadata

Every reusable prompt should have metadata, even if it is written in Markdown
rather than a structured database.

```text
Title:
Target tool:
Model family:
Task family:
Audience:
Inputs:
Outputs:
Included scope:
Excluded scope:
Risk level:
Source status:
Verification:
Owner:
Version:
Last reviewed:
Package inclusion:
```

## Task Family Taxonomy

Use task families to make prompts discoverable.

| Family | Examples |
| --- | --- |
| Documentation | README expansion, guide writing, changelog, release notes, source-policy updates. |
| Coding | Bug fix, feature implementation, refactor, test addition, script repair. |
| Review | PR review, docs review, source review, package review, security review. |
| Research | Source discovery, citation verification, literature map, official-doc check. |
| RAG | Source-grounded answer, source ledger, retrieval evaluation, contradiction handling. |
| Agent operations | Long-running goal, dirty worktree handling, staging, package build, final report. |
| Image prompting | Product shot, UI mockup, illustration, revision, style guide. |
| Evaluation | Rubric design, dataset case, regression test, prompt audit. |
| Release | Package build, manifest inspection, public-safety scan, release checklist. |

## Risk Levels

| Level | Description | Examples |
| --- | --- | --- |
| Low | Read-only or docs-only with no current claims. | Rewrite a checklist, summarize a local guide. |
| Medium | Edits public docs, prompt templates, or tests. | Expand README, update prompt template sections. |
| High | Tool use, package builds, workflow changes, current product claims. | Build release package, edit automation docs, verify external behavior. |
| Critical | Destructive commands, secret access, publishing, account actions. | Force push, delete files, publish release, read credentials. |

Prompts with high or critical risk should include explicit ask-first and
forbidden-action sections.

## Index File Shape

An index can be a Markdown table when the library is small.

| Prompt | Task family | Target tool | Risk | Verification |
| --- | --- | --- | --- | --- |
| `prompts/codex/docs-update.goal.md` | Documentation | Codex | Medium | Health check, docs tests, diff check. |
| `prompts/codex/fix-bug.goal.md` | Coding | Codex | Medium | Reproduction or focused test, unit tests. |
| `prompts/codex/review-pr.goal.md` | Review | Codex | Low | Findings-first review with file references. |

For larger libraries, keep the Markdown index as the public reader surface and
generate machine-readable summaries only when necessary.

## Search Fields

Index entries should support these searches:

- "I need a prompt for a docs update."
- "I need a prompt that can run tests."
- "I need a read-only review prompt."
- "I need a prompt that handles RAG sources."
- "I need a prompt safe for public repositories."
- "I need a prompt for package manifest review."
- "I need a prompt with final report requirements."

## Prompt Example Registry

Examples should be indexed separately from templates. A template is reusable;
an example is a concrete scenario.

| Example type | Required fields |
| --- | --- |
| Normal case | Input, filled prompt, expected output, verification. |
| Failure case | Input, expected refusal or missing-info behavior, risk. |
| Regression case | Old failure, fixed behavior, test or review gate. |
| Source case | Sources, source statuses, supported claims, omitted claims. |
| Package case | Build command, manifest evidence, metrics, hash. |

## Versioning

Use simple version labels for prompt assets:

| Change | Version action |
| --- | --- |
| Clarify wording only | Patch note or no version if internal. |
| Add required section | Minor version. |
| Change allowed actions or output schema | Minor or major version depending on compatibility. |
| Remove input or change semantics | Major version or deprecate old prompt. |
| Fix safety issue | Patch plus changelog and review note. |

In Markdown-only libraries, version can be a visible metadata line and a
changelog entry.

## Deprecation

Do not silently delete reusable prompts. Deprecate first unless the prompt is
unsafe.

Deprecation note:

```text
Deprecated:
- Reason:
- Replacement:
- Migration notes:
- Last package version expected:
```

Immediate removal is acceptable when a prompt leaks secrets, encourages unsafe
behavior, contains copied private material, or points to a harmful workflow.

## Package Inclusion

Use package labels:

| Label | Meaning |
| --- | --- |
| `include` | Ships in release package. |
| `include-docs-only` | Ships as documentation but not as an executable prompt. |
| `exclude-private` | Must not ship. |
| `exclude-generated` | Generated output, not source material. |
| `exclude-unsafe` | Unsafe or deprecated for safety reasons. |
| `review-needed` | Do not package until reviewed. |

## Index Maintenance Workflow

1. Add or update the prompt.
2. Check required sections.
3. Add or update evaluation case.
4. Update prompt index.
5. Update package inclusion label.
6. Update changelog if user-visible.
7. Run prompt-template tests.
8. Run public-safety scan.

## Public-Safety Fields

Every index should make safety visible.

| Field | Purpose |
| --- | --- |
| Source status | Prevents source laundering. |
| Risk level | Tells users when a prompt can touch files, tools, or accounts. |
| Forbidden actions | Prevents accidental destructive operations. |
| Current-claim warning | Tells users to verify product behavior. |
| Final report | Forces evidence rather than confidence. |

## Index Quality Checklist

- [ ] Every prompt appears in an index.
- [ ] Every index entry has target tool and task family.
- [ ] Risk level is visible.
- [ ] Package inclusion is visible.
- [ ] Deprecated prompts point to replacements.
- [ ] Current product claims are marked for official verification.
- [ ] Private prompts or local-only prompts are not indexed for public package
  inclusion.
- [ ] Tests enforce required sections.

## Common Index Failures

| Failure | Impact | Repair |
| --- | --- | --- |
| Prompt exists but is not indexed | Readers cannot find it. | Add index entry and package label. |
| Index says low risk but prompt can write files | Users underestimate danger. | Raise risk and add permission block. |
| Deprecated prompt has no replacement | Users keep copying old workflow. | Add migration note. |
| Prompt has no verification | Final reports become vague. | Add verification and success criteria. |
| Package includes review-needed prompt | Unsafe artifact ships. | Exclude until reviewed. |

## Maintainer Final Gate

Before release:

- [ ] Prompt index matches actual files.
- [ ] Prompt-template tests pass.
- [ ] Package builder includes only intended prompt assets.
- [ ] Changelog names major prompt-library changes.
- [ ] Public-safety scan covers prompts and examples.
- [ ] Deprecated prompt links still resolve.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/33-prompt-library-indexing.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `33 prompt library indexing` state what decision, workflow, or reusable behavior it supports?
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
