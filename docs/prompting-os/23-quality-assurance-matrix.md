# Quality Assurance Matrix

This matrix connects repository artifacts to checks. Use it to decide what
verification is required for each change.

## Artifact Matrix

| Artifact | Quality question | Verification |
| --- | --- | --- |
| README | Does it expose required routes, links, commands, and safety guidance? | Named-section tests, live-link review, executable commands, health check. |
| Prompting OS modules | Do they teach procedures, examples, failures, and verification? | Bounded behavior/evidence tests and package parity. |
| Prompt templates | Are inputs, scope, checks, and failure behavior present? | Prompt docs tests and manual review. |
| Scripts | Do they behave deterministically? | Unit tests and focused command. |
| Static site | Does it work offline? | Local link and asset review. |
| Release package | Does it include correct files and hashes? | Build and inspect manifest. |
| Source docs | Are sources safe and attributed? | Source-policy review. |
| Automation | Is it bounded and no paid LLM default? | Workflow tests and policy review. |

## QA Levels

| Level | Use when | Checks |
| --- | --- | --- |
| Light | One-doc typo. | Diff review. |
| Standard | User-visible docs. | Health, autofix check, tests. |
| Package | ZIP source changed. | Standard plus package build and manifest. |
| Script | Python/PowerShell changed. | Standard plus focused unit/manual test. |
| Policy | Safety/source rules changed. | Standard plus public-safety scan. |

## QA Decision Flow

```text
Did package source change?
  yes -> build package and inspect manifest

Did scripts change?
  yes -> run focused tests

Did public docs change?
  yes -> run health checks and public-safety scan

Did source claims change?
  yes -> verify source authority

Did prompt templates change?
  yes -> review inputs, scope, verification, failure behavior
```

## Evidence Types

- Command output.
- Unit test results.
- Package manifest.
- File-size metrics.
- Source links.
- Diff review.
- Static site inspection.
- Changelog entry.

## Artifact-Specific Gates

### README

- Complete table of contents.
- Links to Prompting OS, guides, templates, checks, source policy.
- Public-safety section.
- Maintainer workflow.

README evidence:

- Table of contents includes major workflows.
- Prompting OS modules are linked.
- Validation commands are visible.
- Source policy is visible.
- Public-safety rules are visible.

### Prompting OS Package

- Required modules.
- Named core artifacts and reader routes.
- Worked example, failure case, and verification command.
- Manifest paths are relative.
- Generated ZIP ignored.

Package evidence:

- Manifest hash.
- Required modules list.
- Source, manifest, and archive path parity.

### Prompt Templates

- Target tool.
- Purpose.
- Inputs.
- Scope.
- Safety.
- Verification.
- Failure behavior.
- Final report.

### Automation

- No paid LLM default in GitHub Actions.
- Generated-file allowlists.
- Manual release publishing.
- No secret requirements for scheduled workflows.

## QA Review Questions

- Does the evidence match the user request?
- Does a test cover the actual requirement?
- Did we verify the generated artifact, not only source files?
- Did we update indexes and navigation?
- Did we update changelog?
- Are there private paths or secret-like strings?
- Are current product claims sourced?
- Is the final state staged if requested?

## QA Failure Examples

### False Broad Completion

A package test confirms that a ZIP builds, but no one checks its source commit,
required paths, hashes, or path parity. The fix is to assert those contracts.

### README Drift

The repository grows many guides while the README remains a short landing page.
The fix is to treat README as a public manual with sections for workflow,
Prompting OS, safety, validation, automation, and maintenance.

### Source Policy Gap

A guide mentions leak-derived repositories without explaining structural-only
use. The fix is to link source policy and state that leaked contents are not
copied or treated as current truth.

### Check Mismatch

Only unit tests run after a package-source change. The fix is to build the
package and inspect the generated manifest.

## Minimum Evidence Table

| Claim | Minimum evidence |
| --- | --- |
| README routes readers | Named headings, links, commands, and review. |
| Package is complete | Required paths, source commit, hashes, and path parity. |
| Public safety is preserved | Secret/path scan and source-policy review. |
| Scripts still work | Unit tests and focused command output. |
| Generated artifact is correct | Manifest hash and archive listing. |
| Current external fact is accurate | Official source checked on a concrete date. |

## QA Record

```markdown
Change:
QA level:
Commands:
Results:
Manifest evidence:
Public-safety review:
Remaining risk:
```

## Completion Gate

Do not mark a task complete until:

- Requested artifacts exist.
- Required checks ran.
- Evidence covers the scope.
- Known failures are reported.
- Changes are staged when requested.

## QA Anti-Patterns

- Passing tests but ignoring package manifest.
- Reviewing README without checking links.
- Claiming source-grounded accuracy without checking citations.
- Treating volume as quality instead of testing behavior and evidence.
- Treating a model summary as evidence.
- Running a narrow check and claiming broad completion.

## Final Rule

Quality assurance is matching evidence to claims. A narrow check cannot prove a
broad claim.
