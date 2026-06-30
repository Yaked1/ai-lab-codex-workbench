# Maintenance And Release Manual

Prompting OS is useful only if it stays maintained. A prompt package can become
misleading when product behavior changes, source links rot, prompt examples get
copied without review, or release artifacts stop matching the repository.

This manual defines how to maintain a public-safe, substantial prompt package.

## Maintenance Surfaces

| Surface | Maintained by | Evidence |
| --- | --- | --- |
| Markdown modules | Docs edits and review. | File contents, links, changelog. |
| Templates | Prompt asset review. | Inputs, outputs, safety, verification. |
| Rubrics | Evaluation review. | Score definitions and examples. |
| Package builder | Script tests. | Unit tests and manifest. |
| Release docs | Maintainer review. | Release checklist. |
| Source policy | Public-safety review. | Source map and policy docs. |
| README | Navigation and positioning. | Links and reading order. |

## Versioning

Use versioning when behavior changes:

| Change | Version impact |
| --- | --- |
| Typo fix | Patch. |
| New guide section | Patch or minor. |
| New module | Minor. |
| New package file | Minor. |
| New required output schema | Major if downstream tools parse it. |
| Removed module or prompt | Major unless clearly deprecated. |
| Safety restriction | Minor, or major if it rejects common old workflows. |

Prompt assets should include a stable ID when they become reusable. Large docs
can rely on changelog entries and package manifests.

## Package Build Procedure

From the repository root:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
python scripts/create_prompting_os_package.py --version v1 --output-dir .\.tmp\prompting-os-package-check
```

Then inspect:

```powershell
Get-Content .\.tmp\prompting-os-package-check\prompting-os-v1-manifest.json -TotalCount 80
```

Confirm:

- ZIP exists.
- Manifest exists.
- Package paths are relative.
- File hashes are present.
- Required modules are included.
- Private-looking files are excluded.
- Markdown payload meets depth targets.

## Package Depth Policy

The package should be broad and deep enough to study offline. Current tests
should enforce:

- A minimum Markdown file count.
- A minimum count of substantial Markdown files.
- A minimum total Markdown byte count.
- Required production, security, evaluation, benchmark, template, and rubric
  files.

Do not satisfy these tests with filler. Add useful technical material:

- Procedures.
- Decision tables.
- Examples.
- Failure modes.
- Checklists.
- Rubrics.
- Package evidence.
- Source-policy notes.

## Changelog Discipline

Update `CHANGELOG.md` for user-visible changes:

- New guide modules.
- Prompt template changes.
- Package behavior changes.
- Safety policy changes.
- New scripts or tests.
- Release process changes.

Good changelog entries are factual:

```text
Added a Prompting OS RAG field guide covering source ledgers, tool permission
levels, prompt-injection cases, and output templates.
```

Avoid:

```text
Made everything much better.
```

## Source Review

Before using external sources:

1. Classify the source.
2. Decide what it is authoritative for.
3. Check license/source status if content may be reused.
4. Use official docs for fast-changing product behavior.
5. Use leak-derived repos only as structural benchmarks.
6. Write original guidance.
7. Link or cite sources when useful.

## Link Review

For public docs:

- Prefer relative links for repository files.
- Prefer official docs for current product behavior.
- Avoid private account URLs.
- Avoid local machine paths.
- Keep static site links offline-safe.

## Public-Safety Review

Before a release:

- Search for private paths.
- Search for secret-looking strings.
- Search for copied prompt dumps.
- Review leak-derived source mentions.
- Confirm `.env` and generated packages are ignored.
- Confirm no generated ZIP is staged accidentally.

## Regression Review

When changing package source:

- Run package tests.
- Build package.
- Inspect manifest.
- Compare file count and Markdown payload.
- Confirm required modules.
- Confirm README/index links.
- Confirm changelog.

## Release Checklist

- [ ] Repository health check passes.
- [ ] Safe autofix check passes.
- [ ] Unit tests pass.
- [ ] Prompting OS package builds.
- [ ] Manifest looks public-safe.
- [ ] README describes current structure.
- [ ] Prompting OS index lists modules.
- [ ] Changelog has an entry.
- [ ] No secrets or private paths.
- [ ] No leak-derived prompt content.
- [ ] Generated artifacts remain ignored unless intentionally released.

## Deprecation

When a prompt, guide, or module becomes outdated:

1. Mark it deprecated.
2. Explain why.
3. Link the replacement.
4. Keep old content until users have a migration path.
5. Remove it in a later major change if needed.

Do not silently delete public docs without a note unless the content is unsafe.

## Final Rule

Maintenance is part of prompt engineering. A prompt package without tests,
source policy, release notes, and package manifests is not a durable artifact.
