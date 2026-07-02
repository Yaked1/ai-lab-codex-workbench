# Checklists And Templates

This file gathers operational checklists for prompt design, agent work, source
review, package review, and publication. Use it as a quick reference during
review.

## Prompt Design Checklist

- [ ] Goal names a deliverable.
- [ ] Audience is clear.
- [ ] Context is relevant.
- [ ] Trusted instructions are separated from evidence.
- [ ] Scope includes allowed work.
- [ ] Scope excludes forbidden work.
- [ ] Output format is explicit.
- [ ] Verification is concrete.
- [ ] Failure behavior is defined.
- [ ] Safety boundaries are present.

## Coding-Agent Checklist

- [ ] Run `git status --short --branch`.
- [ ] Read `AGENTS.md`.
- [ ] Read relevant files.
- [ ] Preserve unrelated changes.
- [ ] Edit only scoped files.
- [ ] Avoid dependency installs unless approved.
- [ ] Run checks.
- [ ] Report failures.
- [ ] Stage only if requested.

## Source Review Checklist

- [ ] Source type classified.
- [ ] Authority level clear.
- [ ] Date checked when freshness matters.
- [ ] License/source status acceptable.
- [ ] No private data.
- [ ] No leak-derived text copied.
- [ ] Claims are supported.
- [ ] Missing information is reported.

## Package Review Checklist

- [ ] Package builds.
- [ ] Manifest exists.
- [ ] Paths are relative.
- [ ] Hashes exist.
- [ ] Required files included.
- [ ] Excluded files absent.
- [ ] Markdown depth targets met.
- [ ] Generated artifacts ignored.
- [ ] Changelog updated.

## Public-Safety Checklist

- [ ] No `.env` files.
- [ ] No credentials.
- [ ] No OAuth files.
- [ ] No cookies.
- [ ] No private paths.
- [ ] No private repository links.
- [ ] No leaked prompts.
- [ ] No unsupported current product claims.
- [ ] No paid LLM workflow requirement in GitHub Actions.

## Final Report Template

```markdown
Summary:
- [what changed]

Files changed:
- [file]

Commands run:
- [command]

Results:
- [result]

Package evidence:
- [manifest or zip details]

Risks:
- [risk]

Unverified:
- [item]
```

## PR Template Additions

```markdown
## What Changed

## Why

## Files

## Verification

## Public Safety

## Package Impact

## Known Limitations
```

## Source Ledger Template

```yaml
sources:
  - id: S1
    title:
    type:
    url_or_path:
    date_checked:
    authority:
    supports:
    risks:
```

## Context Ledger Template

```markdown
## Context Ledger

Trusted instructions:
- [instruction]

Trusted evidence:
- [evidence]

Assumptions:
- [assumption]

Excluded:
- [excluded context]

Open questions:
- [question]
```

## Evaluation Table Template

```markdown
| Case | Input | Expected | Actual | Score | Notes |
| --- | --- | --- | --- | ---: | --- |
| normal |  |  |  |  |  |
| edge |  |  |  |  |  |
| abuse |  |  |  |  |  |
```

## Prompt Asset Template

```yaml
id:
version:
target_tool:
purpose:
inputs:
outputs:
scope:
forbidden:
verification:
failure_cases:
source_status:
```

## Release Checklist

- [ ] Version selected.
- [ ] Changelog updated.
- [ ] Health check passes.
- [ ] Safe autofix check passes.
- [ ] Unit tests pass.
- [ ] Package builds.
- [ ] Manifest inspected.
- [ ] Release notes drafted.
- [ ] Human review complete.

## Package Manifest Review Template

```markdown
Package:
Version:
ZIP path:
Manifest path:
File count:
Markdown files:
Markdown bytes:
Required modules present:
Excluded files absent:
SHA256:
Reviewer:
```

## Work Order Template

```markdown
## Objective

## Audience

## Files In Scope

## Files Out Of Scope

## Source Requirements

## Safety Boundaries

## Verification Commands

## Success Criteria

## Failure Behavior

## Final Report Fields
```

## Source-Grounded Answer Template

```markdown
## Answer

## Supported Claims

| Claim | Source |
| --- | --- |

## Inferences

## Missing Information

## Source Risks
```

## Prompt Regression Template

```markdown
## Regression Case

Prompt:
Old behavior:
New behavior:
Expected:
Evidence:
Severity:
Repair:
Retest:
```

## Tool Permission Template

```markdown
Allowed:
- read:
- search:
- compute:

Requires approval:
- write:
- network:
- publish:
- destructive:

Forbidden:
- secrets:
- private data:
- unrelated systems:
```

## Prompt Review Comment Template

```markdown
Finding:
Severity:
File/prompt:
Why it matters:
Suggested fix:
Verification:
```

## README Expansion Checklist

- [ ] Table of contents covers major surfaces.
- [ ] Start-here table points to beginner and maintainer paths.
- [ ] Prompting OS module map is present.
- [ ] Core workflow is explained.
- [ ] Prompt templates are linked.
- [ ] Source policy is explained.
- [ ] Validation commands are visible.
- [ ] Public-safety rules are visible.
- [ ] Package build commands are visible.
- [ ] Contributing path is visible.
- [ ] Known limitations and non-goals are visible.

## Incident Note Template

```markdown
Incident:
Affected files:
Risk:
Fix:
Checks:
Follow-up:
```

## Final Rule

Checklists are not bureaucracy when they prevent false confidence. Keep them
short enough to use and specific enough to catch real failures.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/21-checklists-and-templates.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `21 checklists and templates` state what decision, workflow, or reusable behavior it supports?
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
