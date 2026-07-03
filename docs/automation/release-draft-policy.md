# Release Draft Policy

`monthly-release-draft.yml` prepares a release checklist issue. It does not
publish a GitHub Release automatically. Treat every draft issue as a todo
list for a human, not as an announcement.

## What The Workflow Does

The monthly release draft workflow:

- Runs on `workflow_dispatch`.
- May also run monthly on a conservative schedule.
- Uses no model-provider API keys.
- Does not run Codex.
- Runs repository health checks, safe autofix check, and unit tests.
- Runs a release package smoke build with a test version.
- Removes generated `dist/` files after the smoke build unless
  `keep_dist=true`.
- Opens or updates an issue titled `Monthly release draft`.

The issue includes:

- Current date
- Latest commit
- Suggested version placeholder
- Maintainer commands for a manual release
- Check result summary

## What The Workflow Does Not Do

This is the section to read before assuming a green run means "shipped."
`monthly-release-draft.yml` never:

- Publishes a GitHub Release.
- Creates or pushes a Git tag.
- Pushes any commit to `main`.
- Chooses a version number for you (it only suggests a placeholder).
- Runs Codex or any paid LLM API.
- Uploads the smoke-built package anywhere permanent (the smoke `dist/`
  output is deleted unless `keep_dist=true`, and even then it stays local to
  the workflow run's artifacts, not published as a release asset).
- Bypasses branch protection or admin merge rules.

The only durable output is a GitHub issue. Everything else it touches
(package smoke build, checks) is disposable or informational.

## Beginner Mental Model

Think of the workflow as a release-readiness reminder, not a release robot.
It answers "what should a maintainer look at next?" It does not answer "is
this release approved?"

| Question | Answer |
| --- | --- |
| Did it publish anything? | No. It opens or updates a checklist issue. |
| Did it choose the final version? | No. A maintainer chooses the version. |
| Did it prove every doc claim is current? | No. It runs repository checks; humans still verify fast-changing external claims. |
| Did it upload a permanent package? | No. The smoke package is disposable unless debug output is intentionally retained. |
| Can a green draft replace PR review? | No. It is release preparation evidence, not review approval. |

If you are new to the repository, stop after reading the generated issue and
copy its checklist into your release notes draft. Do not tag or publish until
the manual review steps below are complete.

## Inputs, Decisions, And Outputs

| Stage | Who decides? | Evidence to keep | Common mistake |
| --- | --- | --- | --- |
| Trigger the draft workflow | Maintainer | Workflow run URL or run ID | Assuming scheduled output is automatically current. |
| Read the draft issue | Maintainer | Issue link and checklist status | Treating placeholders as final release text. |
| Choose version | Maintainer | Reason for major/minor/patch/prerelease | Reusing the placeholder version. |
| Run local checks | Maintainer | Command names and pass/fail results | Trusting only the workflow run. |
| Build package | Maintainer or reviewed workflow | Archive name, manifest path, SHA-256 | Committing generated `dist/` files accidentally. |
| Publish release | Maintainer | Tag, assets, release URL | Publishing before public-safety review. |

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

## Choosing A Version

The release draft issue may include a placeholder. Replace it with a real
version before building or publishing.

| Change type | Typical version decision | Examples |
| --- | --- | --- |
| Typo fixes, broken links, small wording clarifications | Patch | `v0.1.1` after `v0.1.0` |
| New guides, new templates, compatible workflow docs | Minor | `v0.2.0` after `v0.1.3` |
| Breaking repo process changes or renamed public paths | Major | `v1.0.0` after `v0.x` only when the project is ready |
| Experimental release candidate | Prerelease | `v0.2.0-beta.1` |

Do not publish exact compatibility promises, hosted-product availability,
pricing, or model access claims unless they were checked against official
docs during release preparation. Otherwise, list them as claims needing
official-doc verification in the release notes.

## Inputs And Outputs

| Item | Meaning |
| --- | --- |
| Trigger | Manual `workflow_dispatch` or conservative schedule. |
| Version placeholder | Draft issue suggests a version but does not choose it for the maintainer. |
| `keep_dist` | Optional debug setting for retaining local package output during the workflow run. |
| Checks | Repository health, safe autofix check, unit tests, and package smoke build. |
| Output | A GitHub issue that summarizes release-readiness tasks. |
| Non-output | No GitHub Release, no tag, no package publication, no direct push to `main`. |

## Manual Steps A Human Must Still Take

The draft issue is a starting point, not an approval. After it appears, a
human must:

1. Read the diff of everything since the last release and confirm the
   changelog reflects it.
2. Pick the actual version number (semantic versioning; the issue only offers
   a placeholder).
3. Decide stable vs. prerelease.
4. Run the local checks from a clean worktree, not just trust the workflow's
   run.
5. Build the real release package locally or via `release-package.yml`, with
   the chosen version.
6. Verify the built package manifest and archive hash.
7. Search the new docs and changelog for secrets, private paths, and any
   claims that need an "official docs" verification note.
8. Manually trigger `release-package.yml` (or run the local build script) --
   this step never happens automatically.
9. Manually create/publish the GitHub Release from the built artifact, or
   confirm `release-package.yml` did so as part of a reviewed, intentional
   run.
10. Close the draft issue referencing the real release once it is public.

None of these ten steps happen without a human explicitly running a command
or clicking a button.

## Public-Safety Review Before Publishing

Run this review on the final release notes, changelog, and package manifest:

| Risk | What to check | Acceptable outcome |
| --- | --- | --- |
| Secrets or tokens | Search for API-key-like strings, credentials, and copied environment values. | None present. |
| Private paths | Search for home directories, local archive paths, screenshots, and account-specific links. | None present in public files. |
| External tool claims | Look for exact pricing, model availability, CLI behavior, hosted features, and platform support. | Verified in official docs or moved to "needs verification." |
| Generated artifacts | Review `git status --short` and package output. | `dist/` is not committed unless intentionally reviewed. |
| Source/license status | Check any newly referenced public source. | License/source status is documented or the reference is removed. |

When the answer is uncertain, write conservative release notes. A release can
say "updated guidance and added verification steps" without claiming that a
third-party product works in a specific way today.

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

## Rollback And Recovery

| Problem | Recovery |
| --- | --- |
| Draft issue contains stale commit or check data | Rerun `monthly-release-draft.yml` after the latest PRs merge and checks pass. |
| Wrong version was used for a local package build | Delete the local generated package output, rebuild with the intended version, and do not publish the wrong artifact. |
| Wrong version was published as a GitHub Release | Draft a corrective release or remove the release only after following the repository's release/security policy and coordinating with maintainers. |
| Generated `dist/` files were staged | Unstage them before commit; release artifacts belong in release assets or workflow artifacts, not normal docs commits. |
| A release note overclaims third-party behavior | Edit the release notes to conservative language and add an official-doc verification item. |
| Package manifest looks wrong | Stop the release, fix the package builder or source files in a reviewed PR, then rebuild. |

For ordinary documentation mistakes discovered after release, use a follow-up
patch release. For secrets, private data, or security-sensitive publication,
follow `SECURITY.md` instead of treating it as a normal docs typo.

## Failure Modes

| Failure | Likely cause | Response |
| --- | --- | --- |
| Draft issue is stale | Workflow ran before latest docs/tests changed. | Rerun the draft workflow after checks pass. |
| Smoke package fails | Missing required file or generated output issue. | Fix the package builder or required-file list before release. |
| `gh workflow run` fails | GitHub CLI auth or repository remote issue. | Run `gh auth status` and `gh repo view`. |
| Release notes overclaim | Draft text was treated as final copy. | Rewrite with concrete changes, checks, and limitations. |
| Generated `dist/` files remain | Debug option or interrupted cleanup. | Remove generated output unless explicitly intended. |
| Someone assumes the draft issue means "already released" | Issue title/labels were skimmed, not read. | Point them to this doc's "What The Workflow Does Not Do" section. |
| Version placeholder gets used verbatim | Maintainer skipped the "pick a real version" step. | Re-tag and re-release only after coordinating with SECURITY.md guidance if the placeholder was already pushed. |
