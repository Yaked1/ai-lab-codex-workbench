# Offline Package Reader Guide

The focused Prompting OS package is meant to be useful after it has been
downloaded, copied into a teaching folder, attached to a release, or reviewed
without internet access. This guide explains how readers should navigate the
package and how maintainers should keep it coherent.

The package is not a marketing bundle. It is a technical field manual for
prompt design, coding-agent operations, source-grounded writing, evaluation,
tool permissions, and release-safe prompt libraries.

## Reader Assumptions

An offline reader may have only the extracted Prompting OS folder and no
repository history. The package therefore needs to provide:

- A clear start page.
- Stable module numbers.
- Plain Markdown that renders in common editors.
- Enough examples to apply the ideas without browsing the full repository.
- Safety rules that do not depend on hidden local instructions.
- Package manifest evidence for maintainers.
- Explicit limits around current product behavior.

## First Ten Minutes

Use this route when opening the package for the first time.

| Minute | Action | Why |
| --- | --- | --- |
| 0-1 | Open `README.md`. | Learn the package map and build purpose. |
| 1-3 | Read `01-kernel.md`. | Understand the universal prompt contract. |
| 3-5 | Skim `02-model-family-drivers.md`. | Choose the right adaptation for chat, reasoning, coding, RAG, image, or local models. |
| 5-7 | Read the checklist in `23-quality-assurance-matrix.md`. | Learn how package claims are verified. |
| 7-10 | Open `templates/master-prompt-template.md`. | Start from a complete work order instead of a vague prompt. |

## Role-Based Reading Paths

| Role | Path |
| --- | --- |
| New prompt engineer | `01-kernel.md`, `12-prompt-pattern-library.md`, `16-comprehensive-examples.md`, `evals/prompt-quality-rubric.md`. |
| Coding-agent user | `04-agent-skills.md`, `13-agent-operations-manual.md`, `28-tool-permission-model.md`, `30-agent-review-and-red-team.md`. |
| RAG or source-grounded writer | `03-context-engineering.md`, `14-rag-and-tool-use-field-guide.md`, `29-source-grounded-writing-lab.md`, `07-source-map.md`. |
| Maintainer | `15-maintenance-and-release-manual.md`, `20-prompt-library-governance.md`, `31-workbench-maintainer-runbook.md`, `32-completion-evidence-manual.md`. |
| Instructor | `17-curriculum-and-workshops.md`, `26-offline-package-reader-guide.md`, `16-comprehensive-examples.md`, `21-checklists-and-templates.md`. |
| Security reviewer | `09-security-and-governance.md`, `22-risk-register.md`, `28-tool-permission-model.md`, `30-agent-review-and-red-team.md`. |
| Package reviewer | `24-archive-corpus-source-map.md`, `25-repository-expansion-playbook.md`, `32-completion-evidence-manual.md`, manifest JSON. |

## What Each Module Type Provides

| Module type | Expected contents |
| --- | --- |
| Core theory | Concepts, decision rules, examples, anti-patterns, and practice prompts. |
| Operations | Step-by-step runbooks, command boundaries, dirty-worktree handling, and evidence reporting. |
| Evaluation | Rubrics, test cases, failure taxonomies, regression loops, and review thresholds. |
| Source policy | Source labels, structural-use rules, citation discipline, and public-safety handling. |
| Governance | Ownership, metadata, lifecycle, deprecation, release criteria, and package gates. |
| Templates | Copy-ready prompt skeletons with explicit placeholders and final report shape. |

## Offline Package Integrity

When a maintainer provides the package, they should also provide or reference:

- ZIP file name.
- ZIP SHA-256.
- Manifest file name.
- Manifest SHA-256 if the manifest is distributed separately.
- Package version.
- Build command.
- Date the checks ran.
- Known skipped checks.

The manifest should list relative source paths, archive paths, sizes, and file
hashes. It should not contain private machine paths.

## Package Review Without The Repository

If you receive only the package and manifest, you can still perform a useful
review.

1. Confirm the ZIP opens.
2. Confirm `Prompting_OS_v1/README.md` exists.
3. Confirm numbered modules are present and in order.
4. Confirm `templates/master-prompt-template.md` exists.
5. Confirm `evals/prompt-quality-rubric.md` exists.
6. Compare file names and sizes against the manifest.
7. Search extracted Markdown for private paths, secrets, and local account
   details.
8. Skim the shortest files to make sure they are intentionally small or still
   useful.
9. Confirm source-policy modules do not copy unsafe prompt text.
10. Record any missing evidence in your review notes.

PowerShell examples:

```powershell
Get-FileHash .\prompting-os-v1.zip -Algorithm SHA256
Expand-Archive .\prompting-os-v1.zip .\inspect-prompting-os-v1
Get-ChildItem .\inspect-prompting-os-v1\Prompting_OS_v1 -Recurse -File
Select-String -Path .\inspect-prompting-os-v1\Prompting_OS_v1\*.md -Pattern 'C:\\Users|PRIVATE KEY|sk-'
```

## Offline Teaching Mode

For a workshop, split the package into four sessions.

| Session | Modules | Exercise |
| --- | --- | --- |
| Prompt contracts | `01`, `02`, `12`, template | Rewrite a vague task into a complete prompt contract. |
| Context and sources | `03`, `07`, `14`, `29` | Build a source ledger and answer with supported claims only. |
| Agents and tools | `04`, `13`, `28`, `30` | Write a coding-agent work order with permissions and review gates. |
| Evaluation and release | `10`, `15`, `23`, `32` | Design tests and a final evidence report for a prompt change. |

Each session should end with a review artifact: prompt contract, source ledger,
work order, or package evidence report.

## Offline Reader Exercises

### Exercise 1: Convert A Vague Prompt

Input:

```text
Make this documentation better.
```

Required output:

- Target audience.
- Files in scope.
- Files out of scope.
- Source policy.
- Acceptance criteria.
- Verification commands.
- Final report fields.

Use `01-kernel.md` and `templates/master-prompt-template.md`.

### Exercise 2: Build A Source Ledger

Input:

```text
Write a guide using one official doc, one community guide, and one local note.
```

Required output:

- Source name.
- Source status.
- What it can support.
- What it cannot support.
- Freshness risk.
- Citation or verification path.

Use `03-context-engineering.md`, `07-source-map.md`, and
`29-source-grounded-writing-lab.md`.

### Exercise 3: Review An Agent Work Order

Input:

```text
Ask an agent to update a release package.
```

Required output:

- Allowed commands.
- Forbidden commands.
- Required package metrics.
- Required manifest checks.
- Public-safety scan.
- Failure behavior.

Use `13-agent-operations-manual.md`, `15-maintenance-and-release-manual.md`,
and `32-completion-evidence-manual.md`.

## Maintaining Offline Coherence

When adding a new module, maintainers should update:

- `README.md` module map.
- Root repository README if the new module changes the public reading path.
- Package tests if the module is required.
- Release docs if package review steps changed.
- Changelog if the module is user-visible.
- Related module links where the new module should be discoverable.

## Version Drift

Offline packages age. Readers should treat these items as potentially stale:

- Product names and model availability.
- Pricing and access tiers.
- Platform support.
- CLI command syntax for external tools.
- GitHub Actions behavior.
- Vendor-specific safety policy.

Stable items:

- Prompt anatomy.
- Source-status discipline.
- Public-safety principles.
- Manifest review.
- Testing and evidence habits.
- Agent permission boundaries.

When a module needs current product behavior, it should say "verify in official
docs" instead of making a permanent claim.

## Offline Quality Checklist

- [ ] The package has a clear start page.
- [ ] Numbered modules are discoverable from the README.
- [ ] Every major workflow has examples and failure modes.
- [ ] Prompt templates are complete work orders.
- [ ] Evaluation material includes rubrics and regression cases.
- [ ] Source-policy material separates official, community, structural-only,
  and unverified sources.
- [ ] Release material explains manifest inspection and hash verification.
- [ ] No remote assets are required to read Markdown.
- [ ] No private local paths or secrets appear.
- [ ] The manifest uses relative paths.
