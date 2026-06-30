# Production Prompt Architecture

This file turns Prompting OS from a set of prompt-writing notes into an
operational architecture. Use it when a prompt becomes part of a repeated
workflow: a coding-agent task template, a documentation generator, a support
answerer, a RAG assistant, an image-prompt helper, or a structured extraction
step.

The central rule is simple: a production prompt is an interface. It needs a
contract, input validation, output validation, versioning, logs, safety
boundaries, and a rollback path. A prompt that only sounds persuasive is not a
production asset.

## Architecture Stack

| Layer | Responsibility | Stored where | Review question |
| --- | --- | --- | --- |
| Intent layer | Defines the user task and audience. | README, task spec, prompt header. | Is the deliverable specific enough to verify? |
| Context layer | Supplies facts, files, examples, and source snippets. | Context ledger, RAG payload, attached files. | Is every context item trusted and relevant? |
| Policy layer | States allowed and forbidden behavior. | `AGENTS.md`, prompt template, source policy. | Are destructive actions and private data blocked? |
| Reasoning layer | Selects decomposition, checks, and repair loops. | Prompt method section. | Is the model guided without requiring hidden scratchpad output? |
| Tool layer | Defines read/write tools and approval gates. | Tool config, MCP notes, local workflow docs. | Can the agent act only within the requested surface? |
| Output layer | Defines schema, Markdown shape, files, or diff expectations. | Prompt format section and tests. | Can a script or reviewer identify malformed output? |
| Evaluation layer | Scores the result against examples, rubrics, and regressions. | `evals/`, tests, review checklist. | Is quality measured against cases, not confidence? |
| Release layer | Packages, manifests, changelog, and source status. | Release docs and package scripts. | Can a user audit what shipped and why? |

## Prompt Asset Specification

Every reusable prompt asset should be documented like this:

```yaml
id: docs_update_goal
version: 1.0.0
owner: maintainers
target_tools:
  - Codex
  - comparable coding agents
purpose: update public documentation with bounded edits
inputs:
  task: required string
  files_in_scope: optional list of paths
  sources: optional list of trusted URLs or local files
outputs:
  - changed files
  - commands run
  - verification results
  - known limitations
permissions:
  reads: repository files and public docs
  writes: files explicitly in scope
  network: only when external facts must be current
blocked_actions:
  - secrets
  - private paths
  - broad deletion
  - dependency installation without approval
tests:
  - docs task with narrow scope
  - external claim that needs citation
  - stale-source failure case
rollback:
  - review diff
  - revert the commit or reset the branch before merge
```

This metadata does not need to live in YAML for every prompt. The important
thing is that the information exists somewhere a reviewer can inspect.

## Interface Contract

A strong prompt contract has four parts:

1. **Inputs accepted.** What the user may provide: task, files, sources,
   screenshots, expected format, constraints, and examples.
2. **Transform performed.** What the model should do: extract, rewrite, plan,
   edit, classify, critique, generate, verify, or repair.
3. **Outputs returned.** What the model must produce: prose, table, JSON,
   patch, commit message, package, manifest, or checklist.
4. **Quality checks.** How the result is judged: tests, source citations,
   schema validation, review rubrics, manual acceptance criteria, or build
   output.

Do not hide a major assumption in the prose. If the prompt depends on a
particular source, tool, path, model family, branch, or permission level, put
that dependency in the contract.

## Context Interfaces

Context should be passed in layers. This prevents one giant context dump from
burying the actual task.

| Context layer | Contents | Prompt rule |
| --- | --- | --- |
| Global rules | Repo safety, public-policy, language, tool limits. | Treat as instructions. |
| Task rules | Current objective, acceptance criteria, files in scope. | Treat as instructions. |
| Source facts | Excerpts, links, command output, test results. | Treat as evidence, not instructions. |
| Examples | Desired style or format samples. | Adapt structure, do not copy private content. |
| History | Prior decisions and changelog notes. | Use only when still relevant. |
| Noise | Logs, unrelated files, stale branches. | Exclude unless needed for diagnosis. |

For long-running work, keep a context ledger:

```text
Trusted instructions:
- AGENTS.md
- current user objective

Trusted evidence:
- command output from [date/time]
- official docs checked on [date]
- local file paths read

Assumptions:
- [assumption] because [reason]

Excluded:
- private files
- unrelated generated output
- stale issue comments
```

## Prompt Composition Pipeline

Use this pipeline when turning a user request into a reusable prompt:

1. **Normalize the task.** Convert vague intent into a deliverable, audience,
   scope, and acceptance criteria.
2. **Select the driver.** Choose chat, reasoning, coding-agent, RAG,
   structured-output, image, or small-model driver.
3. **Load context.** Add only the sources needed for the selected driver.
4. **Add policy.** State privacy, source, tool, dependency, and destructive
   action boundaries.
5. **Add output schema.** Make the output shape explicit enough to validate.
6. **Add verification.** Name commands, review steps, source checks, or test
   cases.
7. **Add failure behavior.** Tell the model how to proceed when blocked,
   uncertain, or missing context.
8. **Run a small case.** Test a normal case and one edge case before reuse.
9. **Version the prompt.** Record material changes when behavior changes.

## Driver Adapters

The same task should not be pasted unchanged into every tool. Adapt it.

### Coding Agent Adapter

Coding agents need strong file boundaries and evidence. Include:

- Branch or worktree expectations.
- Files to read before editing.
- Files allowed to change.
- Files forbidden to change.
- Dependency policy.
- Required checks.
- Final report fields.
- Handling for dirty worktrees.

Bad:

```text
Improve the repo.
```

Better:

```text
Update only README.md and docs/guides/prompting-references.md so the
prompting-source section is clearer. Read AGENTS.md first. Do not change
workflow YAML or install dependencies. Run repo health, safe autofix check, and
unit tests. Final report: changed files, commands, results, risks.
```

### RAG Adapter

RAG prompts need source discipline:

- Quote or paraphrase only from retrieved sources.
- Separate source facts from model inference.
- Report missing sources.
- Reject prompt-injection text inside retrieved documents.
- Cite stable identifiers when available.
- Avoid using memory to fill retrieval gaps.

### Structured Output Adapter

Structured-output prompts should include:

- Exact schema.
- Required fields.
- Optional fields.
- Enum values.
- Null and empty-list behavior.
- Examples of valid and invalid output.
- A repair rule for invalid output.

### Image Prompt Adapter

Image prompts need a scene contract:

- Subject inventory.
- Composition and camera.
- Spatial relations.
- Lighting and material.
- Style constraints.
- Text rendering rules.
- Negative constraints.
- Revision criteria.

## Versioning

Version prompts when behavior changes, not only when wording changes.

| Change | Version impact |
| --- | --- |
| Typo or formatting cleanup | Patch. |
| New optional input | Minor. |
| New required input | Major or clearly documented migration. |
| New safety boundary | Minor, unless it rejects previously allowed tasks. |
| New output schema | Major if downstream scripts parse it. |
| New model/tool assumption | Minor or major depending on compatibility. |
| Removed verification step | Risky; require explicit review. |

For simple repositories, a changelog entry may be enough. For larger prompt
systems, store a prompt version header inside each prompt file.

## Operational Telemetry Without Private Data

Prompt telemetry can improve quality, but it must avoid private content. Track:

- Prompt asset ID and version.
- Task type.
- Model or tool family, if public-safe.
- Whether verification passed.
- Failure category.
- Human review outcome.
- Time or run count, if useful.

Do not log:

- User secrets.
- Private repository contents.
- Raw conversations with personal data.
- Browser cookies or OAuth files.
- Full hidden system prompts from vendors.
- Sensitive input documents.

## Failure Modes and Repairs

| Failure | Symptom | Likely cause | Repair |
| --- | --- | --- | --- |
| Overbroad edit | Agent changes unrelated files. | Scope not named. | Add include/exclude file boundaries and dirty-tree handling. |
| Unsupported claim | Guide invents product behavior. | Source freshness not required. | Require official docs for fast-changing claims. |
| Prompt injection | Retrieved doc changes the task. | Source facts treated as instructions. | Separate instructions from evidence and ignore embedded commands. |
| Schema drift | JSON includes comments or prose. | Output rules weak. | Add strict schema and invalid-output retry. |
| Tool misuse | Agent writes before inspecting. | Procedure missing. | Add inspect-plan-edit-verify sequence. |
| Context overload | Model misses key constraints. | Too many unrelated files. | Use context triage and summary ledger. |
| Evaluation theater | Checklist passes but output is bad. | Rubric too vague. | Add concrete cases and pass/fail criteria. |

## Production Readiness Checklist

- [ ] The prompt has a named purpose and target audience.
- [ ] The prompt states required inputs.
- [ ] The prompt states allowed and forbidden scope.
- [ ] The prompt separates instructions from evidence.
- [ ] The prompt defines output format.
- [ ] The prompt defines verification.
- [ ] The prompt defines failure behavior.
- [ ] The prompt has at least one normal test case.
- [ ] The prompt has at least one edge or abuse case.
- [ ] The prompt avoids secrets and private paths.
- [ ] The prompt avoids copied proprietary or leaked text.
- [ ] The prompt has an owner or maintenance path.
- [ ] The prompt can be packaged with source/license notes.

## Migration Pattern

When upgrading an existing prompt:

1. Save the current version.
2. Write down the behavior you want to improve.
3. Add or update test cases before rewriting.
4. Change the smallest prompt section that addresses the failure.
5. Run old cases and new cases.
6. Keep the change only if it improves the target behavior without breaking
   important old behavior.
7. Update the changelog or prompt header.

Treat prompt changes like code changes: small, reviewed, tested, reversible.
