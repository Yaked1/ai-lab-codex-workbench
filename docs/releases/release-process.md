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
- [ ] Source-inspired prompting content has a source map, original wording, anti-slop review, and no copied prompt dumps.
- [ ] Automation pages still describe candidate/source preparation only; they do not imply unattended publication of AI-written guides.

## Source-Inspired Release Review

Before a release that includes new prompting curriculum, Prompting OS pages, automation loops, or template packs, reviewers should check the source-to-release path:

```text
source inventory -> pattern extraction -> original synthesis -> anti-slop pass -> local checks -> diff review -> changelog -> release notes -> package manifest
```

The release package may include original synthesis and source maps. It must not include raw downloaded ZIPs, copied prompt dumps, local archive paths, leaked system prompts, private files, or generated guide content that skipped human review.

## Known Constraints

This release process packages a public documentation and prompt-template workbench. It is not an installer, library package, deployment image, model artifact, or registry-published package.

## Step-By-Step Runbook

This section is the exact sequence a maintainer runs, in order, to cut a
release. Every command matches the real scripts in this repository; nothing
here is aspirational. This repository never auto-publishes a release — every
step below is run manually, locally, by a human, before anything reaches
GitHub.

### Step 1: Confirm a clean starting point

```powershell
git status
git switch main
git pull --ff-only origin main
```

`git status` should show a clean tree before you branch. If it does not,
stop and resolve the local changes first; do not build a release on top of
uncommitted work.

### Step 2: Run local checks

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

All three must pass before you build a package. `safe_autofix.py --check` is
read-only here; if it reports fixable issues, run
`python scripts/safe_autofix.py --write` separately, review the diff, then
re-run the check.

### Step 3: Build the release package

```powershell
python scripts/build_release_package.py --version v0.1.0
```

Replace `v0.1.0` with the real version you are cutting. This writes:

```text
dist/ai-agent-coding-workbench-<version>.zip
dist/package-manifest-<version>.json
```

`scripts/build_release_package.py` builds this from a fixed allowlist
(`README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`,
`LICENSE`, plus the `data/`, `docs/`, `prompts/`, `scripts/`, `tests/`
directories and the `.github/workflows/` and `.github/codex/prompts/`
subdirectories), and it excludes caches, virtual environments, existing
archives, `.env` files, secret- or private-named files, and any file over
5 MB. The ZIP uses a fixed internal timestamp so rebuilding it from the same
source tree is deterministic.

If you are also shipping the focused Prompting OS package:

```powershell
python scripts/create_prompting_os_package.py --version v1
```

This writes `release/packages/prompting-os-v1.zip` and
`release/packages/prompting-os-v1-manifest.json` by default. Use
`--output-dir` to redirect output to a scratch location for a dry run
without touching the real `release/packages/` directory.

### Step 4: Inspect the manifest

Open the manifest and read it, do not just trust that the build succeeded:

```powershell
Get-Content .\dist\package-manifest-v0.1.0.json -TotalCount 80
(Get-Content .\dist\package-manifest-v0.1.0.json -Raw | ConvertFrom-Json).files.Count
(Get-Content .\dist\package-manifest-v0.1.0.json -Raw | ConvertFrom-Json).archive
```

Confirm:

- `files` paths are repository-relative (forward slashes, no drive letters,
  no machine-specific home directory).
- No entry mentions `.env`, a secret- or private-prefixed filename, or a
  path under `dist/`, `build/`, `logs/`, or `outputs/`.
- The `archive.sha256` field is present and non-empty.

### Step 5: Verify the archive hash

Confirm the ZIP on disk actually matches the hash recorded in its own
manifest, so you know the manifest was generated from the same build:

```powershell
$manifest = Get-Content .\dist\package-manifest-v0.1.0.json -Raw | ConvertFrom-Json
$actualHash = (Get-FileHash .\dist\ai-agent-coding-workbench-v0.1.0.zip -Algorithm SHA256).Hash
$manifestHash = $manifest.archive.sha256.ToUpper()
if ($actualHash -eq $manifestHash) { "MATCH" } else { "MISMATCH: rebuild before releasing" }
```

A mismatch means the ZIP was modified, re-zipped, or hand-edited after the
manifest was written. Do not release in that state; re-run Step 3 from a
clean tree and re-verify.

You can also spot-check the archive contents directly:

```powershell
Expand-Archive .\dist\ai-agent-coding-workbench-v0.1.0.zip .\dist\inspect-v0.1.0 -Force
Get-ChildItem .\dist\inspect-v0.1.0
Get-ChildItem .\dist\inspect-v0.1.0\docs\site\index.html
Remove-Item .\dist\inspect-v0.1.0 -Recurse -Force
```

### Step 6: Draft release notes from the template

Copy the template and fill in every field; do not leave placeholders that
look like an oversight:

```powershell
Copy-Item .\docs\templates\release-notes.md .\docs\releases\v0.1.0.md -ErrorAction Stop
```

If `docs/releases/v0.1.0.md` (or the version you are cutting) already
exists, skip the copy and edit it directly instead of overwriting a
finished note. Open the new file and complete every section from
[docs/templates/release-notes.md](../templates/release-notes.md): Release,
Summary, Audience, User-Facing Changes, Maintainer-Facing Changes, Package
Contents, Verification, Known Limitations, Claims Needing Official-Doc
Verification, Public-Safety Review, Upgrade Notes, and Reviewer Notes. Use
the Verification Evidence table to record the actual pass/fail result and
the archive SHA-256 from Step 5, not a placeholder value.

The GitHub Actions release workflow (`.github/workflows/release-package.yml`)
checks for this exact file at `docs/releases/<version>.md` and refuses to
create the release if it is missing, so this step is not optional even for
a small patch release.

### Step 7: Update the changelog

Add a dated entry to `CHANGELOG.md` describing the user-visible change. The
release notes and the changelog entry should describe the same change; if
they drift, a reader comparing the two will trust neither.

### Step 8: Commit, push, and open a pull request

```powershell
git switch -c agent/release-v0.1.0
git add docs/releases/v0.1.0.md CHANGELOG.md
git commit -m "Add v0.1.0 release notes"
git push -u origin agent/release-v0.1.0
gh pr create --title "Release v0.1.0" --body "Adds release notes and changelog entry for v0.1.0."
gh pr checks --watch
```

Merge only after checks pass and a human has reviewed the diff. Do not tag
or trigger the release workflow before this merges to `main`.

### Step 9: Tag the release

After the release-notes PR is merged into `main`:

```powershell
git switch main
git pull --ff-only origin main
git tag -a v0.1.0 -m "AI Agent Coding Workbench v0.1.0"
git push origin v0.1.0
```

Tagging locally does not publish anything by itself. It only creates a
reference point; the GitHub Release is a separate, manual step next.

### Step 10: Trigger the manual release workflow

```powershell
gh workflow run release-package.yml -f version=v0.1.0 -f prerelease=false
gh run list --workflow release-package.yml
gh run view <RUN_ID> --log-failed
gh release view v0.1.0 --web
```

This workflow only runs when a maintainer triggers `workflow_dispatch` by
hand. It re-runs the health check, the safe-autofix check, and the unit
tests inside CI, rebuilds the package, and refuses to proceed if
`docs/releases/v0.1.0.md` is missing or if a release for that tag already
exists. It never runs on a schedule and never runs on a plain push.

### Step 11: Review the published release

```powershell
gh release view v0.1.0 --web
```

Confirm in the browser that the title, tag, attached ZIP, attached manifest,
and release notes body all match what you expect before telling anyone the
release is available.

## Rollback: A Bad Release Artifact Was Already Shared

If a release ZIP or manifest is found to contain something it should not
(a stale doc, a broken link, or in the worst case something that violates
the Public Repository Hygiene rules), treat it as an incident, not a quiet
edit:

1. **Do not silently re-upload a fixed ZIP under the same tag.** GitHub
   Releases are meant to be an immutable record; silently swapping assets
   erases the audit trail of what was actually downloaded.
2. **Mark the existing release clearly.** Edit the release description to
   add a visible note at the top, for example: "This release contained an
   issue; see v0.1.1 for the corrected package." Use
   `gh release edit v0.1.0 --notes-file <updated-notes-path>` or edit
   through the GitHub web UI.
3. **If the shared artifact contains a real secret or credential**, rotate
   that credential immediately, independent of anything else in this list.
   A fixed release does not undo an exposed credential.
4. **Cut a corrected patch release** following Steps 1 through 11 above
   with the next patch version (for example `v0.1.1`), and reference the
   problem plainly in that release's Summary and Known Limitations
   sections.
5. **If the artifact must be removed rather than superseded**, a maintainer
   can delete the release with `gh release delete v0.1.0 --yes` and delete
   the tag with `git push --delete origin v0.1.0`, but only after
   confirming no other reference (documentation link, changelog entry,
   external teaching material) depends on that tag still resolving. Prefer
   marking-and-superseding over deletion whenever possible, since deletion
   breaks any existing link to that release.
6. **Update `CHANGELOG.md`** with a correction entry so the historical
   record shows both the original release and the fix, rather than quietly
   rewriting history.

The guiding rule: a rollback should make the correction *more* visible than
the original mistake, not less. Quietly overwriting a shared asset trades a
small embarrassment now for a larger trust problem later, because someone
who already downloaded the bad artifact has no way to know it changed.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/releases/release-process.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `release process` state what decision, workflow, or reusable behavior it supports?
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
