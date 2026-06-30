# Workbench Maintainer Runbook

This runbook is for maintainers who keep the AI prompting and coding-agent
workbench useful, safe, and release-ready. It focuses on recurring operations:
intake, docs expansion, prompt-template updates, package checks, source-policy
reviews, and final evidence reports.

Maintainers should prefer small, reviewable changes. Broad expansion is allowed
when requested, but it should still be broken into evidence-backed batches.

## Maintainer Responsibilities

| Responsibility | What good looks like |
| --- | --- |
| Preserve repository safety | No secrets, private paths, leaked prompts, or unsupported current claims. |
| Keep docs navigable | README, indexes, guide pages, and package README link to each other. |
| Keep prompts operational | Templates include inputs, scope, safety, verification, and final reports. |
| Keep package useful | Prompting OS package remains substantial and offline-readable. |
| Keep checks meaningful | Tests enforce promises readers depend on. |
| Keep releases reviewable | ZIPs and manifests can be inspected with hashes and relative paths. |
| Keep changelog factual | User-visible changes are recorded without overclaiming. |

## Standard Maintenance Loop

1. Intake.
   Identify task, audience, files, source needs, and acceptance evidence.

2. Inspect.
   Read local instructions, status, relevant docs, tests, and scripts.

3. Plan.
   Choose a focused batch. Name what will not be touched.

4. Edit.
   Use repository conventions. Avoid unrelated refactors.

5. Verify.
   Run relevant checks. Build package if package content changed.

6. Review.
   Inspect diff, package manifest, public-safety search, and changelog.

7. Stage.
   Stage explicit paths only when requested or required by the task.

8. Report.
   Include changed files, commands, results, package metrics, and risks.

## Daily Or Per-Task Checks

Use these for ordinary docs or prompt-template work.

```powershell
git status --short --branch
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
```

When package content changed:

```powershell
python scripts/create_prompting_os_package.py --version v1 --output-dir .\.tmp\prompting-os-package-check
Get-Content .\.tmp\prompting-os-package-check\prompting-os-v1-manifest.json -TotalCount 120
```

## Monthly Review

Run a broader review before a release or workshop.

| Area | Review |
| --- | --- |
| README | Still explains purpose, audience, start path, workflows, safety, validation, package, and maintenance. |
| Prompting OS | File count, byte count, shortest file size, required modules, package manifest. |
| Prompt templates | Required sections present and examples still match repository checks. |
| Tool docs | Fast-changing claims are conservative or marked for official verification. |
| Automation docs | Allowed files, forbidden files, dry-run/apply behavior, rollback, and failure modes are clear. |
| Static site | Offline-safe, no remote scripts, no trackers, no remote fonts. |
| Changelog | Unreleased entries are factual and not duplicated excessively. |
| Tests | Tests fail for meaningful regressions and do not encode stale weak floors. |

## Prompt Template Maintenance

When updating prompt templates:

- Keep the target tool explicit.
- Keep purpose short and operational.
- Keep full prompt complete enough to paste into the target tool.
- Keep short version useful for quick tasks.
- Keep inputs to fill as a table or list.
- Name included scope and excluded scope.
- Include safety boundaries.
- Include verification steps.
- Include success criteria.
- Include final report format.
- Include failure cases.

Review prompt changes with at least one normal case and one failure case.

## Prompting OS Package Maintenance

The package should stay substantial. Maintain these expectations:

- At least 35 Markdown files.
- At least 300 KB of Markdown payload.
- Required numbered modules are present.
- Master template and rubric remain non-trivial.
- Short modules are intentional indexes, schemas, or visual companions.
- Package manifest uses relative paths.
- Exclusions protect caches, archives, private-looking files, `.env` files,
  and oversized files.

When adding modules:

- Use stable numbering.
- Update `docs/prompting-os/README.md`.
- Update package tests.
- Update repository health required files if the module is mandatory.
- Update root README if the reading path changes.
- Update release docs if package review changes.
- Update changelog.

## Source Policy Maintenance

Source rules protect the public repository.

| Source type | Maintenance rule |
| --- | --- |
| Official docs | Verify current claims before exact statements. |
| Community projects | Use for patterns and examples; avoid treating as official. |
| Local archives | Remove local paths; use structural lessons unless content is clearly safe. |
| Leak-derived material | Structural-only; never publish hidden prompts. |
| Private notes | Do not publish. |
| Generated drafts | Review as drafts, not evidence. |

## Release Maintenance

Before release:

1. Finish changelog.
2. Run health checks.
3. Run safe autofix check.
4. Run all tests.
5. Build full workbench package if releasing the repository snapshot.
6. Build focused Prompting OS package if Prompting OS changed.
7. Inspect manifests.
8. Record hashes.
9. Search for private paths and secret patterns.
10. Prepare release notes with known limitations.

Do not auto-publish releases. Keep release publication manual and reviewable.

## Triage Rules

| Situation | Response |
| --- | --- |
| A check fails in touched area | Fix the smallest likely cause and rerun focused check. |
| A check fails outside scope | Report clearly; do not rewrite unrelated areas unless asked. |
| Source is unreadable | Mark skipped; do not infer content. |
| User asks for latest product behavior | Verify official source before answering or editing. |
| Worktree is dirty | Preserve existing changes; stage explicit paths only. |
| Generated artifacts appear | Confirm ignored or intentionally tracked. |
| Dependency seems useful | Ask before adding. |
| Destructive command seems faster | Do not use without explicit request and approval. |

## Maintainer Notes For Broad Goals

Broad goals can produce broad diffs. Keep them reviewable by grouping the work:

- Archive/source inspection.
- README expansion.
- Prompting OS modules.
- Prompt templates.
- Tool/workflow docs.
- Static site.
- Tests and package gates.
- Public-safety review.

Report each group separately in the final summary.

## Evidence Log

Keep a compact evidence log in the final response or PR description.

```text
Evidence:
- Read AGENTS.md.
- Ran git status.
- Inspected archive inventory.
- Added Prompting OS modules 24-32.
- Updated README and package index.
- Ran health check, safe autofix check, unit tests, package builder, diff check.
- Manifest: markdown files, markdown bytes, shortest markdown, ZIP SHA-256.
- Public-safety scan: private paths and secret patterns.
```

## Runbook Failure Modes

| Failure | Repair |
| --- | --- |
| Changelog drift | Collapse duplicate entries and keep newest wording factual. |
| Package floor too low | Raise tests to match documented target. |
| README too long but not useful | Add navigation, tables, and workflows instead of prose blocks. |
| Source map exposes private path | Replace with archive names and sanitized labels. |
| Tests pass but package not inspected | Open manifest and compute metrics. |
| Broad staging includes unrelated files | Reset staging only for own paths if safe, then stage explicit paths. |
| Official-claim drift | Mark claim for verification or browse official docs. |

## Completion Checklist

- [ ] Local rules were read.
- [ ] Worktree status was inspected.
- [ ] Files changed match the task.
- [ ] Navigation and indexes are updated.
- [ ] Changelog is updated.
- [ ] Tests match documented promises.
- [ ] Package manifest is inspected when package changed.
- [ ] Public-safety searches pass.
- [ ] Final report names skipped checks and skipped sources.
