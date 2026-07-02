# Codex Prompt: Repository Cleanup

## Target Tool

OpenAI Codex CLI or Codex-style coding-agent goal mode.

## Purpose

Use this prompt for conservative repository cleanup that improves consistency, navigation, or validation without changing project meaning, architecture, dependencies, or workflow behavior. This is not a refactor prompt and not a review prompt: it exists for the narrow case where files need tidying (dead links fixed, stale references removed, whitespace normalized, obviously unused files retired) with the smallest possible blast radius. If the work involves adding behavior, use `implement-feature.goal.md`. If the work involves inspecting someone else's diff, use `review-pr.goal.md`.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{cleanup_goal}` | The exact cleanup objective. | `Fix Markdown navigation and obvious broken internal references` |
| `{allowed_scope}` | Files or folders that may change. | `README.md`, `docs/guides/`, `prompts/codex/` |
| `{excluded_scope}` | Files, folders, or actions that must not change. | `.github/workflows/`, dependencies, generated archives |
| `{validation}` | Required checks. | `repo_health_check`, `safe_autofix`, `unittest` |
| `{suspected_dead_files}` | Files believed unused, to confirm before touching. | `docs/guides/old-notes.md` |

## Full Prompt

```text
/goal
Objective:
Perform this conservative repository cleanup: {cleanup_goal}

Mandatory first steps:
1. Run git status.
2. Read AGENTS.md fully.
3. Inspect {allowed_scope} before editing.
4. Identify pre-existing modified or untracked files and preserve user work.
5. For every file in {suspected_dead_files}, search the whole repository for
   references before treating it as unused: links, import-style paths,
   script arguments, README/CHANGELOG mentions, and test fixtures. Zero
   hits means a candidate; any hit means it is referenced, not dead.
6. Check CHANGELOG.md for any mention of files you plan to touch or remove.
   A file named there needs a deliberate decision, not a silent deletion.
7. If cleanup touches links, note every link target and anchor now so they
   can be re-checked after editing.

Included scope:
- {allowed_scope}
- Deterministic whitespace/final-newline cleanup when reported by safe_autofix.
- CHANGELOG.md if the cleanup is visible to readers.

Excluded scope:
- {excluded_scope}
- Do not touch anything under .github/workflows/.
- Do not add dependencies or modify package manager lock files.
- Do not delete files.
- Do not edit secrets, .env files, private links, private paths, browser profiles, credentials, or private data.
- Do not rewrite large sections just to make them sound different.
- Do not introduce exact pricing, model, benchmark, or unsupported tool claims.
- Do not touch generated or vendored directories (build output, packaged
  release artifacts, third-party bundled assets) even if they look messy.

Safety boundaries:
- Cleanup must be predictable, reviewable, and tied to the stated objective.
- Prefer safe_autofix.py for whitespace cleanup.
- Do not mix broad editorial rewrites with deterministic cleanup.
- Ask or stop if a file appears obsolete but deletion was not explicitly approved.
- Treat "looks unused" as a hypothesis until a full-repo search confirms
  zero references.
- A file read dynamically (by path string, glob, or config key) may not
  show up in a plain filename grep; check config files and file-list
  scripts before concluding a file is dead.

Verification steps:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check
- git diff --stat
- git diff
- Re-run a full-repo search for every removed or renamed path to confirm no
  remaining reference exists (docs, tests, scripts, CHANGELOG.md).

Success criteria:
- Repository meaning and behavior are preserved.
- The diff is small enough to review.
- No unrelated files change.
- Public-safety rules still hold.
- No file is deleted or renamed without a confirmed zero-reference search.
- {validation} pass or failures are honestly reported.

Final report format:
## Summary
## Git state
## Files changed
## Files considered for removal and why they were kept or removed
## Commands run
## Verification results
## Remaining risks
```

### Worked Example

```text
/goal
Objective:
Perform this conservative repository cleanup: Fix Markdown navigation and
remove one confirmed-unused draft file in docs/guides/.

Mandatory first steps:
1-4. Standard (git status, read AGENTS.md, inspect docs/guides/ and
     README.md, preserve pre-existing user work).
5. For docs/guides/draft-notes-2024.md, search the whole repository for
   references: README.md, CHANGELOG.md, other docs/guides/*.md files,
   scripts/build_release_package.py's file list, and tests/*.py.
6. Check CHANGELOG.md for any mention of draft-notes-2024.md before deciding.
7. List every internal link inside docs/guides/*.md to re-check after editing.

Included scope:
- docs/guides/*.md and README.md (link fixes only)
- docs/guides/draft-notes-2024.md (delete, only if zero references found)
- CHANGELOG.md (this cleanup is visible to readers)

Excluded scope:
- Do not touch .github/workflows/, add dependencies, or edit secrets/private
  paths/credentials.
- Do not rewrite prose in docs/guides/*.md beyond fixing broken links.
- Do not touch scripts/ or prompts/ in this task.

Safety boundaries:
- Only delete draft-notes-2024.md if a full-repo search returns zero
  references; otherwise keep it and report why.
- Keep the diff limited to link fixes plus the one candidate deletion.
- Stop and ask if CHANGELOG.md mentions the file by name.

Verification steps:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check / git diff --stat / git diff
- Full-repo search for "draft-notes-2024" before and after the change to
  confirm zero remaining references.

Success criteria:
- All internal links in docs/guides/*.md and README.md resolve to real
  files and anchors.
- draft-notes-2024.md is removed only if the search proved it unreferenced,
  and the report states the search result explicitly.
- CHANGELOG.md has one new entry if anything reader-visible changed.
- Required checks pass, or failures are reported honestly.

Final report format: same as above.
```

## Short Version

```text
Clean up {allowed_scope} for {cleanup_goal}. Run git status, read AGENTS.md, preserve existing user work, confirm any suspected-dead file has zero repo-wide references before touching it, do not delete files without that confirmation/add dependencies/change workflows/touch secrets, prefer safe_autofix for whitespace, run required checks, inspect git diff, and report files, commands, checks, and risks.
```

## Included Scope

- Files and folders named in `{allowed_scope}`.
- Obvious broken navigation or deterministic formatting issues.
- CHANGELOG.md if readers will notice the cleanup.
- Removal of a file named in `{suspected_dead_files}` only after a
  documented full-repo search shows zero references.

## Excluded Scope

- Any change under `.github/workflows/`.
- Adding dependencies or modifying package manager lock files.
- File deletion without a confirmed zero-reference search, broad
  restructuring, generated binary artifacts, and unrelated prose rewrites.
- Generated or vendored directories (build output, packaged release
  artifacts, bundled third-party assets).
- Secrets, credentials, private data, private paths, and private links.

## Safety Boundaries

- Treat untracked files as user work unless explicitly told otherwise.
- Do not use `git clean`, `git reset`, stash, rebase, or force-push.
- Do not claim cleanup is safe until the diff is inspected.
- Do not modify anything under `.github/workflows/`, ever, in this task type.
- Do not add a dependency to make a cleanup "cleaner"; if the smallest fix
  needs one, stop and ask instead.
- Do not delete a file referenced by a test, a script's file list, a config
  key, or CHANGELOG.md without calling that out explicitly and getting
  approval.

## Verification Steps

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
git diff --stat
git diff
```

If safe autofix reports formatting issues and the task allows it:

```powershell
python scripts/safe_autofix.py --write
python scripts/safe_autofix.py --check
```

Task-specific check: for every path removed or renamed, run a full-repo
text search for the old path/filename (including without its extension,
since some references are import-style or config-key style) and confirm
zero remaining hits before reporting success.

## Success Criteria

- Cleanup is scoped, reversible where practical, and preserves user data.
- No files are deleted or moved unless the task explicitly allows it and a
  full-repo reference search confirmed the file is unused.
- Manifests, logs, or reports exist when organization work affects many files.
- Checks pass or failures are reported with the changed-file list.

## Final Report Format

```markdown
## Summary
## Git state
## Files changed
## Files considered for removal and why they were kept or removed
## Commands run
## Verification results
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Cleanup becomes a rewrite | Stop and split into a documentation task. |
| Unexpected files changed | Report them and avoid staging/committing until reviewed. |
| A file seems safe to delete | Ask for explicit approval instead of deleting it. |
| Safe autofix changes many files | Review the full diff before claiming success. |
| Tests fail outside cleanup scope | Report the pre-existing or unrelated failure clearly. |
| A file that looks dead is actually referenced dynamically (config key, glob pattern, script argument, not a static link) | Widen the search to config files and scripts before deleting; if still uncertain, keep the file and report the ambiguity. |
| Cleanup removes a file a test imports or reads | Restore the file, or update the test in the same change and explain why in the report; never leave a broken test. |
| Cleanup touches a generated or vendored directory | Revert that part of the diff; regenerate from source instead of hand-editing generated output. |
| Cleanup breaks a relative link in docs (moved or renamed file, unfixed reference) | Fix every incoming link to the moved/renamed file in the same change, verified by search, not by memory. |
| Cleanup deletes something still referenced in CHANGELOG.md | Keep the file, or update the CHANGELOG entry to reflect the intentional removal, and say which choice was made and why. |

## Anti-Patterns

- Deleting a file because it "looks old" or "looks unused" without running
  a full-repo search first. A hunch is not a safe-deletion criterion.
- Bundling a prose rewrite into a cleanup task because the file was already
  open. Cleanup diffs should be boring and mechanical; save editorial
  judgment calls for a docs-update task.
- Running `safe_autofix.py --write` and committing the result without
  reading the diff. Bulk formatting changes still need a human-reviewable
  pass before they are called safe.
- Treating "no static link found" as proof of no reference. Dynamic
  references (build scripts, config file lists, test fixtures) do not show
  up in a simple text search for a Markdown link pattern.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **agent prompt template** surface. During broad
maintenance, reviewers should treat `prompts/codex/repository-cleanup.goal.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `repository cleanup.goal` state what decision, workflow, or reusable behavior it supports?
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
