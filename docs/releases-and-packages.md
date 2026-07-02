# Releases And Packages

This guide explains how this repository prepares versioned releases and downloadable packages for general users.

The project is a documentation, prompt-template, and workflow workbench. Its package is therefore a release bundle: a zip file containing the top-level project docs, guides, prompts, scripts, tests, and GitHub workflow files. It is not an installable npm, PyPI, NuGet, container, or GitHub Packages registry package by default.

## Release Goals

Use releases to give users a stable snapshot they can download, teach from, audit, or adapt.

| Goal | What it means |
| --- | --- |
| Stable snapshot | A versioned artifact is available even as `main` continues changing. |
| Offline reuse | Users can open Markdown and static HTML docs without a live website. |
| Teaching support | Instructors can point learners to one release instead of a moving branch. |
| Reviewable package | The zip is built after repository checks pass. |
| Public safety | Release contents avoid secrets, private links, private paths, and generated junk. |

## Versioning

Use simple semantic version tags:

```text
vMAJOR.MINOR.PATCH
```

Examples:

| Version | Use when |
| --- | --- |
| `v0.1.0` | First public workbench release. |
| `v0.2.0` | New guide families, templates, or release/package behavior. |
| `v0.2.1` | Small corrections, link fixes, or documentation clarifications. |
| `v1.0.0` | Stable public teaching release with clear maintenance expectations. |

Pre-releases may use labels such as:

```text
v0.3.0-beta.1
```

## Package Contents

The release package is built by:

```powershell
python scripts/build_release_package.py --version v0.1.0
```

The package includes:

- `README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `AGENTS.md`.
- Markdown guides under `docs/`.
- Offline static HTML pages under `docs/site/`.
- Prompt templates under `prompts/`.
- Standard-library scripts under `scripts/`.
- Unit tests under `tests/`.
- GitHub workflow files under `.github/workflows/`.
- A generated JSON manifest next to the zip in `dist/`.

The package excludes:

- `.git/`
- `dist/`
- `build/`
- `logs/`
- `outputs/`
- virtual environments and caches
- existing archives
- temporary, backup, and log files

## Local Package Build

From the repository root:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
python scripts/build_release_package.py --version v0.1.0
```

Expected output:

```text
Built dist/ai-agent-coding-workbench-v0.1.0.zip
Wrote dist/package-manifest-v0.1.0.json
```

The `dist/` folder is ignored by Git so local package artifacts do not get committed accidentally.

## Focused Prompting OS Package

The main workbench package includes the whole repository snapshot. The focused Prompting OS package includes only `docs/prompting-os/` so readers can download the consolidated prompting framework without the full repository.

Build it from the repository root:

```powershell
python scripts/create_prompting_os_package.py --version v1
```

Default outputs:

```text
release/packages/prompting-os-v1.zip
release/packages/prompting-os-v1-manifest.json
```

For validation-only runs, prefer a temporary ignored output directory:

```powershell
python scripts/create_prompting_os_package.py --version v1 --output-dir .\dist\prompting-os
```

The focused package builder is deterministic, writes a JSON manifest with file hashes, excludes caches, archives, private-looking files, `.env` files, and oversized files, and keeps manifest paths relative to the repository root.

The focused package is not meant to be a thin README wrapper. It should contain
long-form technical files that are useful offline: a prompt kernel, model-family
drivers, context engineering, agent/skill patterns, image prompting, evaluation
and optimization, source mapping, production prompt architecture, security and
governance, an evaluation cookbook, a comprehensiveness benchmark, prompt
patterns, agent operations, RAG/tool-use guidance, maintenance guidance, worked
examples, workshop material, troubleshooting, model adaptation, library
governance, checklists, risk registers, QA matrices, archive source mapping,
repository expansion playbooks, offline reader guidance, evaluation datasets,
tool permission models, source-grounded writing labs, red-team review,
maintainer runbooks, completion-evidence manuals, prompt-library indexing,
static-site/release documentation, workshop assessments, metrics guidance,
failure-mode catalogs, a master template, and a rubric.

The unit tests check both package mechanics and minimum source depth so the ZIP
remains substantial enough to study without returning to the repository. The
focused package should retain at least 35 Markdown files and at least 300 KB of
Markdown payload. If those floors fail, add useful examples, failure modes,
review questions, source-policy notes, or verification steps rather than
padding text.

## Manual GitHub Release Workflow

The repository includes `.github/workflows/release-package.yml`.

The workflow is manual on purpose:

1. A maintainer triggers **Release Package** from GitHub Actions.
2. The maintainer enters a version such as `v0.2.0`.
3. The workflow runs repository health, safe autofix check, and unit tests.
4. The workflow builds `dist/ai-agent-coding-workbench-VERSION.zip`.
5. The workflow writes `dist/package-manifest-VERSION.json`.
6. The workflow creates a GitHub Release with the zip and manifest attached.
7. A maintainer reviews the release assets and keeps the package reversible through normal GitHub release controls.

Manual `workflow_dispatch` keeps a human in the loop. Do not auto-publish release artifacts on every push.
Keep release workflow names unique so GitHub Actions and GitHub CLI commands identify the intended workflow clearly.

## Release Checklist

Before publishing a release:

- [ ] `CHANGELOG.md` has a clear entry for the release.
- [ ] `README.md` still describes the current public user experience.
- [ ] `python scripts/repo_health_check.py` passes.
- [ ] `python scripts/safe_autofix.py --check` passes.
- [ ] `python -m unittest discover -s tests` passes.
- [ ] `python scripts/build_release_package.py --version VERSION` builds a zip and JSON manifest.
- [ ] The generated JSON manifest looks reasonable.
- [ ] The focused Prompting OS package contains substantial technical Markdown files, not only short notes.
- [ ] The focused Prompting OS package has at least 35 Markdown files and 300 KB of Markdown payload.
- [ ] The focused Prompting OS package manifest has been inspected for file count, Markdown bytes, shortest Markdown file, relative paths, and ZIP SHA-256.
- [ ] No secrets, private links, private paths, or account-specific data are present.
- [ ] External tool claims are conservative or marked for official-doc verification.
- [ ] The release title, notes, tag, attached zip, and attached manifest are correct.

## Package Review Checklist

After building the zip:

- [ ] Open the zip and confirm `README.md` is present at the package root.
- [ ] Confirm `docs/site/index.html` is included for offline browsing.
- [ ] Confirm `prompts/` is included.
- [ ] Confirm `.github/workflows/` is included.
- [ ] Confirm `dist/`, `logs/`, caches, and virtual environments are not included.
- [ ] Confirm `package-manifest-VERSION.json` is present in `dist/`.

PowerShell example:

```powershell
Expand-Archive .\dist\ai-agent-coding-workbench-v0.1.0.zip .\dist\inspect-v0.1.0
Get-ChildItem .\dist\inspect-v0.1.0
Get-Content .\dist\package-manifest-v0.1.0.json -TotalCount 80
```

## GitHub Packages

This repository does not publish a registry package by default because its primary artifact is documentation and prompt templates.

If maintainers later want GitHub Packages, decide first:

- What package ecosystem is appropriate.
- What users would install.
- Whether the package adds value beyond the release zip.
- How credentials and package permissions will be managed.
- How publishing will stay manual, reviewable, and reversible.

Do not add registry publishing until the package has a clear user need.

## Release Notes

Use [docs/templates/release-notes.md](templates/release-notes.md) for manual releases. Keep release notes factual:

- What changed.
- Who benefits.
- How to verify the package.
- Known limitations.
- Claims that need official-doc verification.

Do not paste private data, logs, tokens, personal paths, or account-specific URLs into release notes.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/releases-and-packages.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `releases and packages` state what decision, workflow, or reusable behavior it supports?
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
