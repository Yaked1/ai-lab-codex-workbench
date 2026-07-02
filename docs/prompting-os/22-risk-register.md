# Risk Register

This risk register lists recurring risks in prompt engineering and coding-agent
work. Use it during design, review, release, and incident response.

## Risk Table

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Secret exposure | Credentials or private data published. | Health checks, public-safety review, `.gitignore`. |
| Prompt injection | Source text overrides task. | Treat sources as evidence only. |
| Unsupported claims | Docs become misleading. | Official-doc verification. |
| Scope creep | Agent changes unrelated files. | Include/exclude paths. |
| False success | Agent claims unrun checks passed. | Require command output. |
| Thin package | ZIP is not useful offline. | Package-depth tests. |
| Copied leaked prompts | Legal and safety risk. | Structural-only leak policy. |
| Dependency creep | Repo gets heavier. | Approval for dependencies. |
| Stale docs | Product behavior changes. | Mark current claims for verification. |
| Weak evaluation | Prompt regressions unnoticed. | Golden, edge, and abuse cases. |

## Risk Scoring

| Score | Meaning |
| ---: | --- |
| 1 | Low impact, easy to repair. |
| 2 | Moderate impact, local repair. |
| 3 | User-visible issue. |
| 4 | Public safety or release risk. |
| 5 | Secret, destructive action, or serious misinformation. |

## High-Risk Changes

Treat these as high risk:

- Workflow YAML changes.
- Dependency additions.
- Release automation changes.
- Secret handling changes.
- Tool permission changes.
- Prompt templates used for writes.
- Source-policy changes.
- Package builder changes.

## Risk Controls

| Control | Catches |
| --- | --- |
| Required-file health check | Missing core docs or scripts. |
| Secret-pattern scan | Private keys and token-shaped strings. |
| Final-newline check | Basic text hygiene. |
| Package-depth tests | Thin ZIP regressions. |
| Manifest inspection | Missing files and unsafe paths. |
| Source policy | Unsafe external content. |
| Changelog | Untracked user-visible changes. |
| Review checklist | Human judgment gaps. |

## Risk Lifecycle

1. Identify risk.
2. Score severity.
3. Add mitigation.
4. Add verification.
5. Assign owner or review surface.
6. Reassess after changes.
7. Close only with evidence.

## Risk Review Template

```markdown
Risk:
Severity:
Trigger:
Mitigation:
Verification:
Owner:
Status:
```

## Incident Response

1. Stop publishing.
2. Identify affected files.
3. Remove unsafe content.
4. Rotate secrets if exposed.
5. Add regression check.
6. Update release notes or security notes.
7. Rebuild package.

## Example Risks

### Unsupported Model Availability Claim

Risk:
Docs claim a model is available in a tool without checking official docs.

Mitigation:
Replace exact claim with a conservative note and link official docs.

Verification:
Review source link and date checked.

### Prompt Package Too Thin

Risk:
The ZIP technically builds but does not teach enough offline.

Mitigation:
Add long technical modules and package-depth tests.

Verification:
Build package and inspect manifest byte counts.

### Leaked Prompt Copying

Risk:
Public docs copy text from leak-derived repositories.

Mitigation:
Use structural-only benchmarking and source policy.

Verification:
Manual review plus text search for known copied phrases when relevant.

### Tool Permission Overreach

Risk:
An agent with broad tool access writes to external systems or unrelated files.

Mitigation:
Use permission profiles and require approval for write, publish, and destructive
actions.

Verification:
Review tool audit and final report.

### Evaluation Blind Spot

Risk:
A prompt passes the normal case but fails missing-info or abuse cases.

Mitigation:
Require normal, edge, and abuse cases for reusable prompts.

Verification:
Review evaluation table and scores.

### Package Manifest Drift

Risk:
The package ZIP no longer matches documentation claims.

Mitigation:
Build package during review and inspect manifest.

Verification:
Record file count, Markdown bytes, required modules, and hash.

### README Under-Explains The Project

Risk:
The public README behaves like a short landing page even though the repository
contains a full prompt workbench.

Mitigation:
Maintain a comprehensive README with table of contents, workflow, Prompting OS
map, safety rules, validation commands, and maintainer guidance.

Verification:
Check README size, headings, links, and tests that enforce minimum depth.

### Thin Module Regression

Risk:
New packaged modules become short stubs that technically exist but do not teach
a complete concept.

Mitigation:
Require every packaged Markdown module to exceed a minimum useful size and to
include procedure, examples, failure modes, or review questions.

Verification:
Run package-depth tests and inspect the shortest files.

## Risk Closure Criteria

A risk is closed only when:

- Mitigation is implemented.
- Verification ran.
- Evidence is recorded.
- Remaining risk is acceptable or documented.

## Final Rule

Most prompt risks are mundane: vague scope, weak checks, stale sources, and
private data. Catch those before looking for exotic failures.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/22-risk-register.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `22 risk register` state what decision, workflow, or reusable behavior it supports?
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
