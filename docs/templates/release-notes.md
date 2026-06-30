# Release Notes Template

Use this template for GitHub Releases.

## Release

- Version:
- Tag:
- Date:
- Release type:
- Maintainer:

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
flags, installer behavior, or provider-specific authentication flows.

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
