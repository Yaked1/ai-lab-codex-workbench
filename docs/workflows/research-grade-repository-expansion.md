# Research-Grade Repository Expansion

Use this workflow when a maintainer asks for a broad documentation, prompt,
skill, or policy expansion and wants the result to be comprehensive rather than
cosmetic. It is designed for public AI-agent workbench repositories where the
goal is not more words for their own sake, but better explanations, stronger
evidence, clearer review paths, and safer reuse.

The short rule is:

```text
Expand breadth only when navigation improves, and expand depth only when the
new material gives reviewers stronger evidence, clearer decisions, or safer
execution.
```

This guide deliberately rejects the vague instruction "make everything better."
Research-grade work needs a scope, an evidence model, quality bars, validation
commands, and staging discipline. Without those, a large agent-generated diff
is hard to review and easy to trust for the wrong reasons.

## What Research-Grade Means Here

Research-grade does not mean academic prose, hidden reasoning, or an
unreviewable wall of citations. In this repository it means each expanded
artifact has enough structure and evidence that another maintainer can audit
it without asking the original author what they meant.

| Quality | Practical meaning |
| --- | --- |
| Clear problem statement | The file explains what decision or workflow it supports. |
| Defined audience | Beginner, maintainer, reviewer, instructor, tool builder, or source curator is named. |
| Source discipline | Fast-changing product claims are verified or explicitly marked for verification. |
| Operational detail | The reader gets commands, checklists, examples, decision criteria, or review steps. |
| Failure analysis | The file names common mistakes and how to recover from them. |
| Evidence path | The file says what command, diff, manifest, package metric, or review artifact proves completion. |
| Safety boundary | The file says what not to do, especially around secrets, private data, automation, and external tools. |
| Navigation | The file links to the next guide, template, prompt, script, or test that completes the workflow. |

A research-grade expansion should therefore add useful sections such as:

- terminology and assumptions;
- scope and non-goals;
- role-specific workflows;
- decision tables;
- examples and counterexamples;
- verification commands;
- review checklists;
- failure modes;
- source and safety notes;
- final-report templates;
- changelog guidance.

It should not add:

- repeated introductory prose already covered elsewhere;
- exact product pricing or model availability without official-doc
  verification;
- private paths, local account details, screenshots, logs, or secrets;
- copied vendor marketing language;
- copied leaked prompt text;
- broad claims that no local check can verify;
- generated artifacts that do not belong in Git.

## Expansion Scope Model

Broad repository work should be split by artifact class. Each class has a
different job and should not be expanded in the same style.

| Artifact class | Primary job | Good expansion | Bad expansion |
| --- | --- | --- | --- |
| Root README | Orient a new reader and route them to deeper docs. | Add decision paths, repository map, validation, and safety context. | Duplicate every guide inline. |
| `AGENTS.md` | Tell agents how to behave in this repo. | Add rules, boundaries, and references agents must follow. | Add long tutorials that bloat every agent session. |
| Workflow docs | Teach repeatable action. | Add gates, command sequences, evidence, and recovery paths. | Add abstract philosophy with no commands or checks. |
| Tool guides | Explain how and when to use a tool safely. | Add setup boundaries, task fit, risks, and official-doc verification notes. | Freeze fast-changing product behavior as permanent truth. |
| Prompt templates | Act as executable work orders. | Add inputs, scope, exclusions, checks, report format, and failure behavior. | Add motivational text the agent cannot act on. |
| Skills | Package a focused behavior for an agent runtime. | Add trigger conditions, source files, boundaries, verification, and reporting. | Hide broad repo instructions inside one skill. |
| Scripts | Provide deterministic local automation. | Add dry-run modes, clear output, tests, and safety constraints. | Add networked LLM calls or destructive side effects. |
| Tests | Preserve promises the repo makes. | Assert required files, section coverage, package floors, and safety rules. | Test wording so tightly that useful edits become painful. |
| Changelog | Record user-visible changes. | Summarize concrete additions and behavior changes. | Claim sweeping quality improvements without evidence. |

When the request says "every file," translate it into one of two safer forms:

1. Every major repository surface should have a research-grade expansion path.
2. Every file touched by this task should become materially more comprehensive.

Do not silently edit hundreds of files just to satisfy a literal reading if the
result will be impossible to review.

## Intake Checklist

Before editing, write down the answers to these questions in the task prompt,
issue, or final report:

- What repository areas are in scope?
- What repository areas are out of scope?
- Is this a documentation-only task, a prompt-template task, a script task, or
  a mixed task?
- Which files must be inspected before editing?
- Which checks must pass?
- Should generated packages be built?
- Should all resulting changes be staged?
- Are there any existing local changes to preserve?
- Are current product claims involved?
- Is source research required, or is this an internal documentation expansion?
- What would make the diff too large to review?

If the task cannot answer those questions, perform an audit first and propose a
bounded expansion plan.

## Evidence Levels

Use evidence labels so the reader knows what kind of support a claim has.

| Label | Meaning | Example use |
| --- | --- | --- |
| Local file | The claim comes from a repository file. | "The package builder writes a manifest" after reading the script. |
| Local command | The claim comes from a command run in this worktree. | "Unit tests passed" with the exact command listed. |
| Official source | The claim comes from vendor or project documentation. | Current installation commands or API shapes. |
| Public community source | The claim comes from a public repo, article, or discussion. | Pattern inspiration, not definitive product behavior. |
| Structural inspiration | The source can shape organization but not be copied. | Prompt collections, archives, or license-unclear examples. |
| Inference | The author concluded something from evidence. | "This failure is likely a PATH issue" after command output. |
| Unverified | The claim needs future confirmation. | Pricing, limits, model availability, marketplace behavior. |

Use official sources for fast-changing product facts. Use local files and local
commands for repository behavior. Use structural inspiration for organization
only when copying content would be unsafe or license-unclear.

## Comprehensiveness Rubric

Score each touched documentation or prompt file before closing a broad
expansion task.

| Dimension | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| Purpose | Missing. | Implied. | Stated. | Stated with audience and use case. |
| Scope | Missing. | Partial. | Included scope only. | Included and excluded scope. |
| Operational detail | None. | Concepts only. | Some commands or examples. | Commands, examples, gates, and evidence. |
| Safety | Missing. | Generic warning. | Specific risks. | Risks, forbidden actions, recovery, and review. |
| Verification | Missing. | Manual review only. | Commands listed. | Commands plus interpretation and failure handling. |
| Navigation | Isolated. | Links one file. | Links related files. | Routes readers by role or task stage. |
| Failure modes | Missing. | One or two notes. | Table or checklist. | Failure, cause, prevention, recovery, and evidence. |
| Maintainer value | Low. | Helpful once. | Reusable. | Reusable, testable, and easy to cite in PR review. |

For research-grade status, aim for:

- no dimension below 2 for a primary guide;
- at least four dimensions at 3;
- explicit explanation when a short file is intentionally short;
- tests or health checks for new required surfaces when appropriate.

## File-Class Expansion Playbooks

### README Expansion

The README should help a new reader answer:

- What is this repository?
- What problem does it solve?
- Who is it for?
- What should I read first?
- What can I run locally?
- What must I not do?
- How do I validate the repository?
- Where are the deeper manuals?

Do not turn the README into a dumping ground. When a section grows beyond
orientation, move the detailed method into `docs/` and link it.

### Workflow Guide Expansion

A workflow guide should include:

- trigger condition;
- reader role;
- prerequisites;
- step sequence;
- stop conditions;
- verification commands;
- common failures;
- final report expectations;
- related templates.

The highest-value workflow docs explain what to do when a step fails. A guide
that only lists the happy path is not research-grade.

### Prompt Template Expansion

A prompt template should be a runnable contract. Add:

- target tool;
- purpose;
- full prompt;
- short prompt;
- inputs to fill;
- included scope;
- excluded scope;
- safety boundaries;
- verification steps;
- success criteria;
- final report format;
- failure cases.

If a template is intentionally short, link to a full template and explain that
the short one is for low-risk use only.

### Skill Expansion

A skill should tell the agent:

- when to use it;
- when not to use it;
- which source files to inspect;
- which files are safe to edit;
- which commands verify the result;
- what final report shape to use.

Keep skills narrower than the whole repository. If a skill has to teach the
entire repo, it should link to `AGENTS.md`, the README, or a workflow guide
instead of embedding all of them.

### Script And Test Expansion

Script changes need stronger evidence than prose changes. Before expanding a
script:

- identify dry-run behavior;
- identify write behavior;
- identify failure behavior;
- inspect existing tests;
- add or update tests for new branches;
- keep dependencies in the standard library unless explicitly approved.

Good script documentation names the command, inputs, outputs, side effects,
exit behavior, and rollback path.

## Research-Grade Expansion Procedure

Use this sequence for a large docs or prompt pass.

### 1. Baseline

Run:

```powershell
git status --short --branch
git log --oneline -5
```

Record whether the tree is clean. If it is dirty, classify existing changes as:

- in scope;
- user work to preserve;
- generated state to ignore;
- blocker needing user input.

### 2. Inventory

List candidate files:

```powershell
rg --files README.md AGENTS.md CONTRIBUTING.md SECURITY.md docs prompts skills scripts tests
```

Then classify the candidate set:

| Class | Questions to ask |
| --- | --- |
| Existing required file | Is it already in repository health checks? |
| Navigation file | Does it link to the deeper guide? |
| Deep guide | Does it have enough operational detail? |
| Prompt template | Does it have the required sections? |
| Script/test | Does behavior change or only documentation? |
| Changelog | Does this task need a user-visible entry? |

### 3. Select Reviewable Targets

Pick targets that cover the repository surface without making the diff
unreviewable. A good broad pass might touch:

- one new deep guide;
- README navigation;
- AGENTS or CONTRIBUTING rules;
- one health check or test;
- changelog.

That is more maintainable than editing every existing Markdown file.

### 4. Draft With Evidence Tags

Write new material using explicit evidence language:

- "This repository's local validation commands are..."
- "Use official docs for current tool claims."
- "This checklist is a review artifact, not an automated scanner."
- "If the check fails, read the exact failure before editing unrelated files."

Avoid:

- "always";
- "guaranteed";
- "best";
- "latest";
- exact model or platform claims without verification;
- dramatic claims that tests cannot support.

### 5. Add Maintenance Hooks

If the new guide becomes part of the core workflow, wire it into:

- README;
- `AGENTS.md`;
- related workflow docs;
- `scripts/repo_health_check.py` required files;
- tests that assert key headings or links;
- changelog.

This keeps the expansion from becoming an orphan page.

### 6. Validate

Run:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
```

If package inputs changed, also run the relevant package builder and inspect
the manifest. If static HTML changed, inspect it for external scripts, remote
assets, and private links.

### 7. Stage Deliberately

When the user asks to stage all changes, stage after validation:

```powershell
git add README.md AGENTS.md CONTRIBUTING.md CHANGELOG.md docs scripts tests
git status --short
```

If unrelated files were already modified before the task, do not stage them
unless the user explicitly said the full worktree is the unit of work. If the
instruction is ambiguous, report the unrelated files before staging.

## Minimum Substance Bars

These bars are not absolute law, but they prevent "comprehensive" from meaning
"one extra paragraph."

| Artifact | Minimum for a primary expansion |
| --- | --- |
| New deep guide | At least 10 meaningful sections, one table, one command block, one failure-mode section, and one final-report or review checklist. |
| README change | At least one new navigation path or decision aid, not just a new sentence. |
| AGENTS change | A rule or reference that changes agent behavior. |
| CONTRIBUTING change | A contributor-visible process, checklist, or quality bar. |
| SECURITY change | A concrete threat, forbidden behavior, review gate, or incident response step. |
| Prompt template change | A new required section or clearer executable work order. |
| Test change | A durable assertion tied to a repository promise. |
| Changelog entry | A specific user-visible change. |

## Public-Safety Review For Broad Expansions

Broad expansions create public-safety risk because they often include examples,
paths, commands, source references, and tool claims. Run this review before
staging:

- Examples use placeholders, not secrets.
- Paths are repository-relative or generic.
- Commands do not print environment variables.
- External links are public and appropriate.
- Private repositories, dashboards, portals, and account IDs are absent.
- Screenshots are not added unless explicitly requested and reviewed.
- Product claims are conservative or flagged for official-doc verification.
- Local archive material is used only as structural inspiration unless its
  license and source status are public-safe.
- Generated package artifacts are ignored unless explicitly part of the task.

## Failure Modes

| Failure | Symptom | Prevention | Recovery |
| --- | --- | --- | --- |
| Scope inflation | Diff touches many unrelated guides. | Choose targets before editing. | Split the task; revert only unrelated changes after review. |
| Prose padding | Longer files do not become more useful. | Require commands, tables, examples, and failure modes. | Replace vague prose with operational sections. |
| Stale product claims | Docs name exact current support or pricing. | Use official docs or generic wording. | Reword as "verify in official docs." |
| Orphan guide | New page is not linked or checked. | Update README and health checks. | Add navigation and tests. |
| Safety regression | Examples include private-looking data. | Use placeholders and run scans. | Remove unsafe examples and rerun checks. |
| Test brittleness | Tests lock onto incidental wording. | Test headings and required promises, not full prose. | Loosen tests to durable concepts. |
| Over-staging | Unrelated local changes get staged. | Inspect `git status` before and after edits. | Unstage unrelated paths with maintainer approval. |

## Review Checklist

Before a maintainer accepts a research-grade expansion, check:

- [ ] The task scope is visible in the prompt, issue, PR, or final report.
- [ ] The diff covers each requested repository surface.
- [ ] Every touched file is materially more useful, not merely longer.
- [ ] New deep docs are linked from navigation surfaces.
- [ ] New required docs are included in health checks or tests where useful.
- [ ] Public-safety rules still hold.
- [ ] Fast-changing claims are marked for official-doc verification.
- [ ] Local checks passed or failures are reported with exact commands.
- [ ] `git diff --check` passed.
- [ ] Changelog entry is factual.
- [ ] Staged paths match the intended task.

## Final Report Template

Use this final report shape for broad repository expansion work:

```text
Summary:
- [What changed and why.]

Research-grade additions:
- [New guide, rubric, workflow, prompt template, or evidence model.]

Files changed:
- [File]: [material improvement.]

Validation:
- [command]: [result]

Safety:
- [secret/private-path scan or repository health check result]
- [external claims needing verification]

Staging:
- [staged paths or reason staging was skipped]

Remaining risks:
- [unverified claims, skipped checks, or follow-up decisions]
```

If the final report cannot fill those fields, the task is not done.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **agent workflow guide** surface. During broad
maintenance, reviewers should treat `docs/workflows/research-grade-repository-expansion.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `research grade repository expansion` state what decision, workflow, or reusable behavior it supports?
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
