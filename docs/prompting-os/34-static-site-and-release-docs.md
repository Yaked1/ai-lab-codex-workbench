# Static Site And Release Docs

Static HTML pages and release documentation turn a repository into something
readers can use without learning the entire source tree. This module defines
how to keep static site pages offline-safe and release docs evidence-oriented.

The workbench uses plain Markdown for most content and plain HTML/CSS for the
offline site. That simplicity is a feature. It keeps the public package easy to
audit and reduces the chance of trackers, remote assets, dependency drift, or
private data entering the release.

## Static Site Rules

Static pages should work by opening the file directly in a browser.

Allowed:

- Plain HTML.
- Plain CSS.
- Relative links to repository docs.
- Local static assets that are public-safe.
- Tables, command blocks, checklists, and workflow summaries.

Forbidden:

- Remote JavaScript.
- Analytics.
- Trackers.
- CDNs.
- Remote fonts.
- Account-specific URLs.
- Private screenshots.
- Personal local paths.
- Framework build steps unless explicitly introduced and approved.

## Static Page Content Model

Each static page should answer:

| Question | Example |
| --- | --- |
| Who is this page for? | Beginners, prompt engineers, maintainers, instructors. |
| What workflow does it support? | Agent task lifecycle, prompt engineering, tools and skills. |
| What files should the reader open next? | Relative links to Markdown docs. |
| What commands are safe to run? | PowerShell checks and package builders. |
| What safety boundaries matter? | No secrets, private paths, leaked prompts, or unsupported claims. |
| How does the reader verify success? | Tests, package manifest, diff review, public-safety scan. |

## Static Site Review Checklist

- [ ] Opens from disk without a server.
- [ ] Uses relative links.
- [ ] Contains no remote scripts.
- [ ] Contains no analytics or tracking.
- [ ] Contains no remote fonts.
- [ ] Contains no private paths or account-specific URLs.
- [ ] Links point to files that exist.
- [ ] Content is useful, not decorative only.
- [ ] Commands are PowerShell-friendly when local.
- [ ] Fast-changing claims are conservative.

## Release Documentation Purpose

Release docs should let a maintainer answer:

- What package is being built?
- What source files are included?
- What files are excluded?
- What checks must pass?
- Where is the manifest?
- What hashes prove the artifact?
- What safety scan ran?
- What limitations remain?

## Release Doc Sections

Use this structure for release docs:

```text
Release purpose
Versioning
Package contents
Build commands
Manifest fields
Review checklist
Public-safety checklist
Publishing workflow
Rollback or replacement
Known limitations
```

## Full Workbench Package

The full workbench package is a repository snapshot. It should include:

- Root docs.
- Guides.
- Prompt templates.
- Scripts.
- Tests.
- Static site.
- GitHub workflow files.
- Release notes.

It should exclude:

- `.git`.
- build output.
- package output.
- logs.
- caches.
- virtual environments.
- archives.
- private-looking files.
- environment files.

## Focused Prompting OS Package

The focused package is narrower. It includes `docs/prompting-os/` and should be
deep enough to teach without the rest of the repository.

Review fields:

```text
Markdown file count:
Markdown byte count:
Shortest Markdown file:
Required numbered modules:
Template included:
Rubric included:
ZIP SHA-256:
Manifest path safety:
```

## Manifest Review

A manifest should be inspected for:

- Archive name.
- Archive SHA-256.
- File list.
- Relative source paths.
- Archive paths.
- File sizes.
- Per-file SHA-256.
- Exclusion rules.
- Absence of private local paths.

Manifest review is not optional when package contents changed. A package build
without manifest inspection proves only that the script ran.

## Release Notes Model

Release notes should be factual.

Good:

```text
Added Prompting OS modules for archive source mapping, package evidence,
tool permissions, source-grounded writing, and maintainer operations. The
focused package now enforces at least 35 Markdown files and 300 KB of Markdown
payload.
```

Bad:

```text
Now the best prompt package on the internet.
```

Release notes should include:

- What changed.
- Who benefits.
- How to verify.
- Known limitations.
- Current claims to verify in official docs.

## Static Site And Package Linkage

The static site should point readers to source docs rather than duplicating
everything.

| Page | Should link to |
| --- | --- |
| `index.html` | README, start guide, lifecycle, Prompting OS, release docs. |
| Agent workflow page | lifecycle doc, Codex guide, prompt templates, checks. |
| Prompt engineering page | comprehensive guide, Prompting OS, evaluation rubric. |
| Skills/tools page | tool comparison, skills docs, MCP docs, permission model. |

When a major Markdown module is added, decide whether the static site needs a
link. It usually does not need full duplicated content.

## Release Failure Modes

| Failure | Cause | Repair |
| --- | --- | --- |
| Package misses new module | Index or test not updated. | Add required file and package test. |
| Manifest has local path | Builder path rendering bug or manual note. | Fix manifest or remove private path. |
| Static site uses remote font | Convenience copied from web template. | Replace with system fonts. |
| Release notes overclaim | Marketing language replaced evidence. | Use package metrics and checks. |
| Generated artifacts committed | Output directory not ignored or not reviewed. | Remove from commit if generated and document build command. |
| Old links break | Module renamed without link updates. | Update README, static site, and tests. |

## Verification Commands

Use these checks after static site or release-doc changes:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
```

For focused package changes:

```powershell
python scripts/create_prompting_os_package.py --version v1 --output-dir .\.tmp\prompting-os-package-check
Get-Content .\.tmp\prompting-os-package-check\prompting-os-v1-manifest.json -TotalCount 120
```

## Completion Checklist

- [ ] Static pages work offline.
- [ ] Static pages contain no remote scripts, analytics, trackers, CDNs, or
  remote fonts.
- [ ] Release docs explain full workbench package and focused Prompting OS
  package.
- [ ] Manifest review instructions are present.
- [ ] Package metrics are included in final report when package changed.
- [ ] Changelog records user-visible package or site changes.
- [ ] Public-safety scan covers static HTML and release docs.
