# Repository Audit Remediation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` or `superpowers:executing-plans` to
> implement this plan task by task. Every behavior change follows red, green,
> refactor. Every task receives an independent review before the next task.

**Goal:** Apply every actionable repository-audit recommendation while keeping
the workbench public-safe, Windows-first, beginner-friendly, source-backed, and
fully verified.

**Architecture:** Safety fixes are implemented as small behavior contracts in
the existing scripts and workflows. Documentation cleanup is deterministic:
shared policy moves to one source, repeated generated blocks are removed, and
tests measure useful structure rather than byte volume. GitHub settings and ref
deletions are recorded separately because repository files cannot prove those
external actions occurred.

**Tech stack:** Python 3 standard library, PowerShell 7, Git, GitHub Actions,
Markdown, HTML, CSS, and `unittest`. No new dependency or lock-file change.

## Global Constraints

- Work on `codex/apply-repository-audit-fixes`, not `main`.
- Preserve unrelated work and never bypass hooks.
- Every bug fix gets a regression test that fails for the original behavior.
- Use first-party sources for changing model facts.
- Current Fable fact: included promotional access ends July 19, 2026 at
  11:59:59 PM PT; the Claude Code 50% weekly-limit increase ends at the same
  time. Source: `https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access`.
- July 7 and July 12 Fable dates are superseded historical observations, not
  current claims.
- No destructive ref deletion, force push, release publication, or GitHub
  settings change without a separately verified owner action.
- A release artifact must be derived from committed Git-tree blobs, record the
  exact source commit, refuse every output collision, and match its
  documentation.
- Generic review policy must not be copied into executable prompts.
- Stars and forks remain outcome metrics, never promises.

---

### Task 1: Decouple the active plan and reconcile Fable claims

**Files:**
- Modify: `tests/test_model_media.py`
- Modify: `tests/test_model_prompting_guides.py`
- Replace: `docs/PLANS/current.md`
- Modify: `README.md`
- Modify: `docs/guides/current-models-and-interfaces.md`
- Modify: `docs/research/current-model-claim-ledger-2026-07-11.md`
- Modify: `docs/PLANS/frontier-model-essay-notes.md`
- Modify: `docs/PLANS/model-prompting-guide-notes.md`
- Modify: `docs/research/video-research-pack-2026-07-11.md`
- Modify: `docs/guides/frontier-models-and-multimodal-systems-2026.md`
- Modify: `docs/guides/model-prompting/claude-fable-5-prompting.md`
- Modify: `docs/guides/model-prompting/sources-and-observations.md`

**Contract:** `docs/PLANS/current.md` is an operational plan, not a permanent
media fixture. Every current Fable access claim uses July 19 and records the
official Help Center source and checked date. July 7 and July 12 remain in
dated research only when labeled superseded and linked to the July 19 update.

- [x] Add `test_current_plan_is_not_a_reader_facing_media_fixture`; first run
  must fail because `current.md` remains in the fixed media path set.
- [x] Change the media test to use stable named reader documents only.
- [x] Replace the global substring assertion with bounded tests for the current
  Fable availability section, evidence row, and superseded-history notes.
- [x] Run the focused tests and observe the expected Fable failure.
- [x] Update every current-facing claim and label all four dated historical
  surfaces as superseded without rewriting unrelated checked dates.
- [x] Run `python -m unittest tests.test_model_media tests.test_model_prompting_guides`.

### Task 2: Make the local PowerShell gate fail closed

**Files:**
- Modify: `scripts/local_check.ps1`
- Create: `tests/test_local_check.py`

**Contract:** each child command is executed through one helper; the first
nonzero child exit stops the script and becomes the script exit code; the
success message appears only after all commands succeed.

- [x] Add a subprocess test with a temporary `python.cmd` shim that fails the
  first invocation; verify the test fails because the script exits zero.
- [x] Add a success-path shim test that records all expected invocations.
- [x] Implement `Invoke-CheckedCommand` with argument arrays and
  `$LASTEXITCODE` propagation.
- [x] Run `python -m unittest tests.test_local_check` on Windows.

### Task 3: Validate the exact staged index in the maintainer

**Files:**
- Modify: `scripts/github_repo_maintainer.ps1`
- Modify: `tests/test_local_autopilot.py` or create
  `tests/test_github_repo_maintainer.py` when runtime isolation is clearer.

**Contract:** automated commit mode begins with an empty index, scans cached
blob bytes, rejects oversized content, and proves the final staged path set
equals the approved path set.

- [x] Add a temporary-repository test where a forbidden file is pre-staged;
  verify commit mode refuses it.
- [x] Add a staged/worktree mismatch test and an oversized-file test.
- [x] Implement clean-index enforcement and cached-blob scanning with
  `git show :<path>`.
- [x] Compare approved and staged paths immediately before commit.
- [x] Run the focused maintainer tests in PowerShell and Python.

### Task 4: Move generated-file validation to trusted base code

**Files:**
- Modify: `.github/workflows/automerge-safe-generated.yml`
- Modify: `docs/automation/safe-automerge-policy.md`
- Modify: `tests/test_research_discovery.py`

**Contract:** a PR cannot replace the path validator that judges that PR. The
write-capable merge step consumes a read-only validation result and executes no
PR-controlled script.

- [x] Add structural tests that reject execution of the checker from the PR
  checkout and reject write permission in the validation job.
- [x] Verify those tests fail on the current workflow.
- [x] Fetch base-owned checker content into a separate trusted directory or run
  a pinned base-ref checkout before the PR checkout.
- [x] Split validation and merge into jobs with the least permissions needed.
- [x] Update the policy diagram and run focused tests.

### Task 5: Harden workflow inputs and generated-content publication

**Files:**
- Modify: `.github/workflows/autofix.yml`
- Modify: `.github/workflows/monthly-release-draft.yml`
- Modify: `.github/workflows/daily-research-scout.yml`
- Modify: `.github/workflows/curator-prompt-prep.yml`
- Modify: `.github/workflows/repo-autopilot.yml`
- Modify: `docs/publication-policy.md`
- Modify: `docs/automation/repository-autopilot.md`
- Modify: `tests/test_research_discovery.py`

**Contract:** dispatch inputs enter shell only through quoted environment
variables. Generated research uses a reviewable per-run branch/PR path rather
than direct default-branch pushes or a permanent merge-heavy branch.

- [x] Add tests that reject `${{ inputs.* }}` inside `run:` bodies.
- [x] Add tests that reject direct default-branch `git push` in scout/curator
  workflows.
- [x] Move inputs to `env:` and use shell variables.
- [x] Route generated files through per-run `autopilot/generated-<run_id>`
  branches and PR creation.
- [x] Document allowed paths, owner, review, and retirement rules.

### Task 6: Make release packages commit-exact, bounded, and collision-safe

**Files:**
- Modify: `scripts/build_release_package.py`
- Modify: `scripts/create_prompting_os_package.py`
- Modify: `tests/test_build_release_package.py`
- Modify: `tests/test_prompting_os_package.py`
- Modify: `docs/releases-and-packages.md`
- Modify: `docs/releases/release-process.md`
- Modify: `docs/releases/v0.1.0.md`

**Interfaces:**
- `source_commit(root: Path) -> str`
- `committed_package_paths(root: Path, commit: str) -> list[str]`
- `committed_blob(root: Path, commit: str, relative: str) -> bytes`

**Contract:** the main bundle includes the documented committed surfaces,
including `skills/` and `examples/`; reads bytes from the recorded Git tree
rather than the mutable worktree; records `source_commit`; and refuses every
same-version overwrite while preserving existing bytes.

- [x] Add untracked-file, dirty-worktree-byte, source-commit, scope-parity,
  symlink, and collision tests; observe failures.
- [x] Replace recursive working-tree discovery with `git ls-tree` path
  enumeration and `git show <commit>:<path>` blob reads.
- [x] Treat Git symlink entries as non-packageable data rather than
  dereferencing their worktree targets.
- [x] Make both builders fail before writing when either output already exists.
- [x] Make docs and manifests describe the same surface.
- [x] Test-build and test-extract both packages in temporary directories.

### Task 7: Make bootstrap review candidates before staging

**Files:**
- Modify: `scripts/bootstrap_github_repo.ps1`
- Create: `tests/test_bootstrap_github_repo.py`

**Contract:** bootstrap lists candidate paths, performs health and secret
checks, requires apply confirmation, stages only approved files, and reports
hook/commit failure distinctly from an empty commit.

- [x] Add tests for dirty candidate display, secret rejection, hook failure,
  empty commit, and apply gating.
- [x] Replace `git add .` with explicit approved path arguments.
- [x] Run the focused Windows test.

### Task 8: Add Windows runtime CI and immutable action references

**Files:**
- Modify: `.github/workflows/ci.yml`
- Modify: all workflows containing `actions/checkout@v4` or
  `actions/setup-python@v5`
- Modify: `tests/test_repo_health.py`

**Contract:** CI executes PowerShell behavior on `windows-latest`; third-party
actions use verified full commit SHAs with release-version comments.

- [x] Add structural tests requiring one Windows job and 40-character action
  SHAs.
- [x] Verify current workflow tests fail.
- [x] Add the Windows gate for `local_check.ps1`, installer behavior, and
  branch-helper behavior.
- [x] Resolve current official action release tags to immutable SHAs and pin
  every use consistently.

### Task 9: Remove mechanical expansion safely

**Files:**
- Replace behavior in: `scripts/mechanical_research_expansion.py`
- Modify: `tests/test_prompting_docs.py`
- Modify: `tests/test_skills_package.py`
- Modify: `tests/test_model_prompting_guides.py`
- Remove marked generated blocks from all current tracked targets.
- Remove or rewrite: `docs/review/mechanical-research-expansion-report.md`
  and its manifest.

**Contract:** a deterministic strip operation removes complete marker pairs
from the approved target set, preserves surrounding unique content and final
newlines, and is idempotent. The strip tool may retain marker constants needed
for detection, but cannot append generic blocks again. Current live target
count is 312; the older report/manifest count of 314 must be reconciled.

- [x] Add fixture tests for Markdown, PowerShell, Python, HTML, CSS, SVG,
  malformed markers, idempotence, and unique-content preservation.
- [x] Handle the generated `.research-grade-addendum` CSS residue that sits
  outside its marker pair, using a fixture that proves unrelated CSS remains.
- [x] Verify the marker-count test fails against current main.
- [x] Convert the tool to strip/audit behavior.
- [x] Run it once on the tracked tree and inspect the deterministic diff.
- [x] Require zero complete marker pairs in the approved target set without
  rejecting the strip tool's own marker constants.

### Task 10: Replace volume gates with behavior and source contracts

**Files:**
- Modify: `tests/test_prompting_os_package.py`
- Modify: `tests/test_model_prompting_guides.py`
- Modify: `tests/test_frontier_model_dossiers.py`
- Modify: `tests/test_prompting_docs.py`

**Contract:** tests enforce required examples, verification paths, evidence
rows, known-limit sections, package parity, and failure cases. They do not use
large byte or word floors as a proxy for quality.

- [x] Write failing contract tests for one worked example, one failure case,
  one verification command, and row-level source identity.
- [x] Remove the 300 KB and per-file size requirements after the contract tests
  fail correctly.
- [x] Retain only small truncation guards where empty or cut-off output is the
  actual defect.

### Task 11: Reduce model-guide duplication and split the frontier reference

**Files:**
- Create: `docs/guides/model-prompting/shared-execution-contract.md`
- Modify: all model-specific files in `docs/guides/model-prompting/`
- Split: `docs/guides/frontier-models-and-multimodal-systems-2026.md`
- Modify: indexes, source ledgers, skills wrappers, and affected tests.

**Contract:** shared run records, verification, escalation, and failure policy
exist once. Model pages keep only model-specific identity, surfaces, task fit,
examples, limits, and evidence. The frontier overview becomes an index plus
bounded vendor/family pages; no information or source link disappears.

- [ ] Add duplicate-contract, navigation, stable-anchor, and bounded-section
  tests. Keep file-size review advisory unless a real parser limit exists.
- [ ] Create the shared contract and update links.
- [ ] Remove duplicated dossier sections from individual model pages.
- [ ] Split the frontier reference by stable subject boundary and update every
  inbound link and skill source mapping.

### Task 12: Create a real first-success path and simplify Prompting OS

**Files:**
- Modify: `README.md`
- Modify: `examples/sample-task.md`
- Create: `examples/first-reviewed-agent-task/README.md`
- Create: `examples/first-reviewed-agent-task/expected-report.md`
- Create: `docs/prompting-os/00-first-success.md`
- Modify: `docs/prompting-os/README.md`
- Modify: overlapping Codex cleanup prompts and their skill wrappers.

**Contract:** the first screen leads with one product promise and three routes:
run a task, learn prompting, contribute. A 5-15 minute tutorial produces one
expected report and one verification result. Prompting OS exposes 15-minute,
one-hour, and maintainer tracks. Overlapping cleanup prompts have distinct jobs
or are consolidated with redirects.

- [ ] Add navigation and example-completeness tests.
- [ ] Write the sample input, ready work order, expected output, and check.
- [ ] Update README and Prompting OS routes.
- [ ] Make `repository-cleanup.goal.md` canonical, fold in unique balanced-mode
  content, update both known inbound references, and remove the balanced file
  only after a repository-wide reference check passes.

### Task 13: Align governance and contributor surfaces

**Files:**
- Replace: `CLAUDE.md`
- Reorder: `CHANGELOG.md`
- Create: `CODE_OF_CONDUCT.md`
- Create: `SUPPORT.md`
- Create: `CITATION.cff`
- Modify: `CONTRIBUTING.md`
- Modify the existing issue-form set and create at most one focused
  good-first-issue form under `.github/ISSUE_TEMPLATE/`.
- Modify: `.github/PULL_REQUEST_TEMPLATE.md`
- Modify: branch-policy documentation.

**Contract:** `CLAUDE.md` imports `AGENTS.md`; `Unreleased` is first; community
files have clear conduct, support, and citation contracts; the total issue-form
count remains between three and five; the good-first form states file scope,
acceptance command, safety boundary, and expected review effort; documented
branch namespaces match actual automation.

- [ ] Add existence, schema, and policy-link tests.
- [ ] Add public-safe community files and issue forms.
- [ ] Document `agent/`, `codex/`, `cleanup/`, and per-run `autopilot/`
  namespaces and retirement rules.

### Task 14: Improve the static discovery surface and starter distribution

**Files:**
- Modify: `docs/site/index.html`
- Modify: `docs/site/*.css`
- Create or modify a small local search index/script under `docs/site/`.
- Create: `starter/README.md`
- Add the task template, safety rules, one evaluation, and one example under
  `starter/`.
- Modify: release builder scope, README, and site links.

**Contract:** the static site has the same three entry routes as README, local
search without external assets, current release links, and accessible labels.
`model-media.html` is explicitly labeled as a network-required media exception
while the remaining core site stays offline-capable. The starter directory is
a coherent fork/copy boundary and contains no private paths or required network
dependency.

- [ ] Add offline-asset, search-index, route, and starter-manifest tests.
- [ ] Implement local search and starter files.
- [ ] Render or parse-check the site and verify all local links.

### Task 15: Record owner-only GitHub actions and release readiness

**Files:**
- Create: `docs/maintenance/github-owner-settings.md`
- Modify: `docs/releases/release-process.md`
- Modify: `README.md`

**Contract:** the repository distinguishes completed file changes from owner
actions: branch protection, required checks, Discussions, homepage URL, social
preview upload, traffic analytics, release publication, and stale-ref deletion.
No document claims these settings are active without live proof.

- [ ] Add a checklist with exact GitHub UI/API verification evidence.
- [ ] Record stale-ref dispositions without deleting refs.
- [ ] Define release readiness and a dated snapshot policy.

### Task 16: Full review, verification, and branch finish

**Files:** all changed files.

- [ ] Run every focused test during its task and record red-green proof.
- [ ] Run `python scripts/repo_health_check.py`.
- [ ] Run `python scripts/safe_autofix.py --check`.
- [ ] Run `python -m unittest discover -s tests`.
- [ ] Run `git diff --check`.
- [ ] Test-build and test-extract release and Prompting OS packages.
- [ ] Validate Markdown links and source-ledger claim IDs.
- [ ] Request a GPT-5.6 Luna xhigh whole-branch review and fix every critical
  or important finding.
- [ ] Commit with hooks enabled.
- [ ] Present merge, PR, keep, or discard options; do not push without the
  user's selected branch-finish option.

## External Settings Boundary

The following cannot be completed by repository file edits alone:

- enable GitHub Discussions;
- set the repository homepage URL;
- upload the social preview image;
- configure branch protection and required checks;
- inspect private traffic/referrer analytics;
- delete live remote branches;
- publish the next GitHub Release.

They remain acceptance items with live evidence, not claims inferred from
documentation.
