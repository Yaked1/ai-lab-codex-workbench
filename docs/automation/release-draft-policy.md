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
