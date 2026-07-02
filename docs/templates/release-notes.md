# Release Notes Template

Use this template for GitHub Releases.

This repository never auto-publishes a release. Every release is built and
reviewed locally by a maintainer before a GitHub Release is created, and the
release workflow itself only runs on manual `workflow_dispatch`. These notes
are the human-readable record of that manual, reviewed process. See
[docs/releases/release-process.md](../releases/release-process.md) for the
full runbook this template supports.

## How To Use This Template

1. Copy the sections below into the GitHub Release description, or draft them
   as a Markdown file under `docs/releases/<version>.md` first and paste from
   there.
2. Fill in every field. Use `N/A` for anything genuinely not applicable, and
   `not run` for a check you skipped, rather than leaving a blank that looks
   like an oversight.
3. Do not write exact external pricing, plan availability, or model-access
   claims as settled fact. Mark them under **Claims Needing Official-Doc
   Verification** instead.
4. Never paste secrets, tokens, private file paths, internal URLs, or
   account-specific screenshots into a release note. This document ships to
   the public the moment the release is published.

## Release

- Version:
- Tag:
- Date:
- Release type:
- Maintainer:

Field notes: **Release type** is one of `major`, `minor`, `patch`, or
`pre-release` (for tags like `v0.3.0-beta.1`). Match it to the semantic
version, not to how big the diff felt.

## Summary

-

## Audience

- Primary reader:
- Maintainer impact:
- Beginner impact:
- Reviewer impact:

## User-Facing Changes

-

## Maintainer-Facing Changes

-

## Package Contents

- [ ] README and top-level project docs
- [ ] Markdown guides under `docs/`
- [ ] Offline static HTML under `docs/site/`
- [ ] Prompt templates under `prompts/`
- [ ] Examples under `examples/`
- [ ] Standard-library scripts under `scripts/`
- [ ] Unit tests under `tests/`
- [ ] GitHub workflows under `.github/workflows/`
- [ ] `package-manifest-VERSION.json`

## Verification

- [ ] `python scripts/repo_health_check.py`
- [ ] `python scripts/safe_autofix.py --check`
- [ ] `python -m unittest discover -s tests`
- [ ] `python scripts/build_release_package.py --version VERSION`
- [ ] Package contents reviewed
- [ ] JSON package manifest reviewed

## Known Limitations

-

## Claims Needing Official-Doc Verification

-

Use this section for anything that may drift after release, such as tool
availability, model access, hosted-product pricing, platform support, CLI
flags, installer behavior, or provider-specific authentication flows. If a
release note contains a specific dollar amount, a specific rate limit, or a
named model as "currently available," and that fact was not checked against
official documentation the same day, it belongs here instead of in the
Summary or Highlights sections.

## Public-Safety Review

- [ ] No secrets or token-like values
- [ ] No private links
- [ ] No private machine paths
- [ ] No personal account data
- [ ] No unreviewed generated artifacts

## Upgrade Notes

-

## Reviewer Notes

- [ ] The release text does not overstate automation safety.
- [ ] Any exact external-tool behavior is either verified or marked for
  official-doc verification.
- [ ] Breaking changes or changed defaults are called out clearly.
- [ ] Any package metric in the release notes matches the generated manifest.
- [ ] The final release text names known limitations instead of hiding them.

## Verification Evidence To Include

Use short factual evidence. Do not paste noisy logs.

| Evidence | Value |
| --- | --- |
| Repository health | `passed` / `failed` / `not run` |
| Safe autofix check | `passed` / `failed` / `not run` |
| Unit tests | test count and result |
| Full package ZIP | path and SHA-256 |
| Full package manifest | path and review status |
| Focused Prompting OS ZIP | path and SHA-256, if built |
| Focused Prompting OS metrics | Markdown files, Markdown bytes, shortest Markdown file |
| Public-safety scan | result and safe-placeholder notes |

## Release Notes Writing Rules

- Keep the summary factual.
- Name who benefits.
- Name verification commands.
- Name limitations.
- Do not claim a check passed unless it ran.
- Do not mention private local paths, private branches, account URLs, or
  machine-specific screenshots.
- Mark product behavior, pricing, model access, platform support, and setup
  details as official-doc verification items when not freshly checked.

## Example Summary

```text
This release expands the public Prompting OS package, tightens package-depth
tests, and adds prompt-template completeness checks. The focused package now
contains [N] Markdown files and [N] Markdown bytes. Repository health, safe
autofix check, unit tests, and package build were run before release.
```

## Worked Example: Filled Release Notes Entry

This is a hypothetical patch release for a documentation fix, filled in end to
end so the structure is easy to copy.

```markdown
## Release

- Version: v0.1.1
- Tag: v0.1.1
- Date: 2026-07-01
- Release type: patch
- Maintainer: repository maintainer

## Summary

- Corrects a broken internal link in the Codex start guide and clarifies the
  safe-autofix scope in docs/codex/03-safe-autofix-policy.md. No behavior or
  package-content changes.

## Audience

- Primary reader: existing users of the v0.1.0 release.
- Maintainer impact: none, docs-only patch.
- Beginner impact: fixes a dead link that beginners were hitting.
- Reviewer impact: small diff, single-session review.

## User-Facing Changes

- Fixed a broken relative link in docs/codex/00-start-here.md.
- Clarified that safe autofix never reorders imports or reformats code.

## Verification

- [x] python scripts/repo_health_check.py
- [x] python scripts/safe_autofix.py --check
- [x] python -m unittest discover -s tests
- [x] python scripts/build_release_package.py --version v0.1.1
- [x] Package contents reviewed
- [x] JSON package manifest reviewed

## Known Limitations

- Same known limitations as v0.1.0; this is a documentation-only correction.

## Claims Needing Official-Doc Verification

- None added in this release.
```

## What Must Never Appear In Release Notes

- Secrets, API keys, tokens, or anything that looks like a credential.
- Private local file paths (for example, a machine-specific home directory).
- Internal or account-specific URLs, including private repository links.
- Unverified exact pricing, rate limits, or "currently available" claims
  about external model providers or tools.
- Screenshots or logs that could contain any of the above.
- Claims that a check passed when it was not actually run for this release.

## Asset Review

- [ ] GitHub Release title matches the tag.
- [ ] ZIP asset opens locally.
- [ ] Manifest asset opens locally.
- [ ] Manifest uses relative paths.
- [ ] Archive SHA-256 is recorded.
- [ ] Generated `dist/` output is not committed unless explicitly intended.
- [ ] Known limitations are included.

## Failure Cases To Mention When Relevant

| Case | Suggested note |
| --- | --- |
| Check was not run | Say `not run` and explain why. |
| Check failed for unrelated reason | Name the failing command and the suspected unrelated area. |
| Package build was skipped | Do not publish package metrics. |
| External docs were not refreshed | Mark the claim as needing official-doc verification. |
| Known issue remains | Put it under Known Limitations with a concrete workaround or next step. |

## Final Release Checklist

- [ ] Release branch or PR reviewed.
- [ ] Changelog entry matches the release notes.
- [ ] Package command used the intended version string.
- [ ] Manifest and ZIP are attached to the release.
- [ ] No private local paths, account IDs, tokens, or generated logs are present.
- [ ] Post-release tag and asset links were checked in the browser.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/templates/release-notes.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `release notes` state what decision, workflow, or reusable behavior it supports?
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
