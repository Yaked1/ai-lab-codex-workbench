# Release Draft Policy

`monthly-release-draft.yml` prepares a release checklist issue. It does not publish a GitHub Release automatically.

## What The Workflow Does

The monthly release draft workflow:

- Runs on `workflow_dispatch`.
- May also run monthly on a conservative schedule.
- Uses no model-provider API keys.
- Does not run Codex.
- Runs repository health checks, safe autofix check, and unit tests.
- Runs a release package smoke build with a test version.
- Removes generated `dist/` files after the smoke build unless `keep_dist=true`.
- Opens or updates an issue titled `Monthly release draft`.

The issue includes:

- Current date
- Latest commit
- Suggested version placeholder
- Maintainer commands for a manual release
- Check result summary

## Why Releases Are Not Published Automatically

This repository is public-facing documentation and prompt guidance. A release can package stale claims, missing changelog notes, or guide content that still needs review. The workflow drafts the checklist, but a maintainer decides when to publish.

## Manual Release Commands

From PowerShell, after reviewing the draft issue and choosing a real version:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
python scripts/build_release_package.py --version v0.1.2
gh workflow run release-package.yml -f version=v0.1.2 -f prerelease=false
gh run list --workflow release-package.yml
gh release view v0.1.2 --web
```

Do not commit generated `dist/` files.

## Inputs And Outputs

| Item | Meaning |
| --- | --- |
| Trigger | Manual `workflow_dispatch` or conservative schedule. |
| Version placeholder | Draft issue suggests a version but does not choose it for the maintainer. |
| `keep_dist` | Optional debug setting for retaining local package output during the workflow run. |
| Checks | Repository health, safe autofix check, unit tests, and package smoke build. |
| Output | A GitHub issue that summarizes release-readiness tasks. |
| Non-output | No GitHub Release, no tag, no package publication, no direct push to `main`. |

## Maintainer Review Steps

Before acting on a release draft issue:

1. Read the changelog and confirm the user-visible changes are complete.
2. Run the local checks from a clean worktree.
3. Build the full package with the selected version.
4. Build the focused Prompting OS package if Prompting OS changed.
5. Inspect both manifests if both packages are built.
6. Search public docs for secrets, private paths, and unsupported current
   claims.
7. Decide whether the release should be stable or prerelease.
8. Trigger the manual release workflow only after review.

## Refusal Cases

The draft issue should not be treated as release approval when:

- The changelog has placeholder text.
- Repository checks failed.
- Package smoke build failed.
- The focused Prompting OS package no longer meets its floor.
- New docs include exact product claims that need official verification.
- Generated archives or manifests are accidentally staged.
- Public-safety review has not run.

## Evidence To Copy Into Release Notes

Use evidence, not marketing language:

```text
Checks:
- repo health:
- safe autofix:
- unit tests:
- full package:
- focused Prompting OS package:

Package evidence:
- archive name:
- archive SHA-256:
- manifest path:
- known limitations:
```

## Failure Modes

| Failure | Likely cause | Response |
| --- | --- | --- |
| Draft issue is stale | Workflow ran before latest docs/tests changed. | Rerun the draft workflow after checks pass. |
| Smoke package fails | Missing required file or generated output issue. | Fix the package builder or required-file list before release. |
| `gh workflow run` fails | GitHub CLI auth or repository remote issue. | Run `gh auth status` and `gh repo view`. |
| Release notes overclaim | Draft text was treated as final copy. | Rewrite with concrete changes, checks, and limitations. |
| Generated `dist/` files remain | Debug option or interrupted cleanup. | Remove generated output unless explicitly intended. |
