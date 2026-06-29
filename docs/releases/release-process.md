# Release Process

This repository publishes a GitHub Release ZIP asset for each public release. It does not publish to npm, PyPI, Docker Hub, GitHub Packages, or any binary package registry by default.

The first package type is a downloadable release bundle:

```text
dist/ai-agent-coding-workbench-<version>.zip
dist/package-manifest-<version>.json
```

Use release tags such as `v0.1.0`, `v0.2.0`, or `v0.2.0-beta.1`.

## What The Package Includes

The package builder uses a small allowlist. It includes:

| Path | Purpose |
| --- | --- |
| `README.md` | Project overview and quick start. |
| `AGENTS.md` | Local agent operating rules. |
| `CONTRIBUTING.md` | Contribution workflow. |
| `SECURITY.md` | Public repository safety policy. |
| `CHANGELOG.md` | User-visible change history. |
| `LICENSE` | License terms. |
| `docs/` | Markdown guides and offline HTML docs. |
| `prompts/` | Prompt templates. |
| `scripts/` | Standard-library helper scripts. |
| `tests/` | Unit tests for local scripts. |
| `.github/workflows/` | Reviewable GitHub Actions workflows. |

The package excludes `.git/`, `dist/`, Python caches, virtual environments, `node_modules/`, `.env`, `.env.*`, secret or private file names, existing archives, logs, temporary files, and large binary or model files.

## Local Verification

Run these from the repository root in PowerShell before creating a release:

```powershell
git status
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
python scripts/build_release_package.py --version v0.1.0
```

Expected release package outputs:

```text
dist/ai-agent-coding-workbench-v0.1.0.zip
dist/package-manifest-v0.1.0.json
```

Inspect the package when needed:

```powershell
Expand-Archive .\dist\ai-agent-coding-workbench-v0.1.0.zip .\dist\inspect-v0.1.0
Get-ChildItem .\dist\inspect-v0.1.0
Get-Content .\dist\package-manifest-v0.1.0.json -TotalCount 80
```

## Manual GitHub Release

The release workflow is manual. It does not run on every push.

Trigger it with GitHub CLI:

```powershell
gh workflow run release-package.yml -f version=v0.1.0 -f prerelease=false
gh run list --workflow release-package.yml
gh run view <RUN_ID> --log-failed
gh release view v0.1.0 --web
```

The workflow:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Runs `python scripts/repo_health_check.py`.
4. Runs `python scripts/safe_autofix.py --check`.
5. Runs `python -m unittest discover -s tests`.
6. Builds the ZIP and JSON manifest with `scripts/build_release_package.py`.
7. Creates a GitHub Release with `gh release create`.
8. Uploads the ZIP and JSON manifest as release assets.

The workflow uses the repository-scoped `GITHUB_TOKEN` from the workflow environment. It does not require a personal access token and does not print token values.

Keep the release automation to one workflow file with one unique workflow name. Duplicate workflow names make GitHub Actions and `gh workflow` commands harder to audit and can cause maintainers to trigger the wrong release path.

## Release Notes

Every release should have a notes file at:

```text
docs/releases/<version>.md
```

For example, the first release uses:

```text
docs/releases/v0.1.0.md
```

The workflow refuses to create a release if the matching notes file is missing.

## Safety Checklist

Before triggering a release:

- [ ] `CHANGELOG.md` includes the user-visible release changes.
- [ ] Release notes exist under `docs/releases/`.
- [ ] Local checks pass.
- [ ] The generated ZIP and manifest names match the release tag.
- [ ] The manifest does not list private files, secrets, `.env` files, caches, or generated artifacts.
- [ ] External product behavior, pricing, platform support, and model availability claims are conservative or marked for official-doc verification.
- [ ] No npm, PyPI, Docker, binary package, or GitHub Packages publishing has been added without a separate explicit decision.

## Known Constraints

This release process packages a public documentation and prompt-template workbench. It is not an installer, library package, deployment image, model artifact, or registry-published package.
