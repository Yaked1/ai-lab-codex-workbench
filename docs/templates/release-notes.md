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

## User-Facing Changes

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

## Public-Safety Review

- [ ] No secrets or token-like values
- [ ] No private links
- [ ] No private machine paths
- [ ] No personal account data
- [ ] No unreviewed generated artifacts

## Upgrade Notes

-
