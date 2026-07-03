# Comprehensiveness Benchmark

This module records how Prompting OS should use large public prompt repositories
as a depth benchmark without copying their contents. It was added after
inspecting a local clone of
[`asgeirtj/system_prompts_leaks`](https://github.com/asgeirtj/system_prompts_leaks)
on 2026-06-30. That repository is leak-derived, so it is not a content source
for this workbench. It is useful only as a structural benchmark for breadth,
file size, indexing, and standalone technical organization.

The result should be clear: this repository should be comprehensive, but it
should be comprehensive by teaching original, public-safe workflows. It should
not become a mirror of hidden prompts.

## Benchmark Snapshot

The local clone was inspected by metadata, directory names, file sizes, and
README headings. Prompt contents were not imported.

| Measurement | Value |
| --- | ---: |
| Non-git files | 267 |
| Text-like files | 263 |
| Text-like payload | 8,393,214 bytes |
| Average text-like file size | 31,913 bytes |
| Largest text-like file | 549,311 bytes |
| Text-like files over 5 KB | 174 |
| Text-like files over 25 KB | 60 |
| Text-like files over 100 KB | 22 |

Category distribution by top-level folder:

| Category | Text-like files | Bytes | Average bytes | Largest file |
| --- | ---: | ---: | ---: | ---: |
| Anthropic | 101 | 5,837,671 | 57,799 | 549,311 |
| OpenAI | 87 | 1,393,197 | 16,014 | 370,668 |
| Misc | 23 | 310,945 | 13,519 | 55,403 |
| Google | 23 | 252,826 | 10,992 | 29,122 |
| xAI | 11 | 202,748 | 18,432 | 55,389 |
| Microsoft | 5 | 154,400 | 30,880 | 74,167 |
| Perplexity | 3 | 66,724 | 22,241 | 38,832 |
| Meta | 1 | 58,280 | 58,280 | 58,280 |
| Notion | 1 | 47,805 | 47,805 | 47,805 |
| Cursor | 1 | 18,435 | 18,435 | 18,435 |
| Mistral | 1 | 16,351 | 16,351 | 16,351 |
| Qwen | 1 | 6,935 | 6,935 | 6,935 |

The useful structural lesson is not "copy long leaked files." The useful
lesson is that a serious prompt repository needs many self-contained technical
documents, clear categories, current index pages, source/status metadata, and
enough depth that readers can study the artifact offline.

## What To Learn Structurally

| Benchmark trait | Safe lesson for this repo |
| --- | --- |
| Vendor/product folders | Organize by model family, workflow, or user task so readers can route quickly. |
| Long standalone files | Make each important file useful without requiring five other tabs. |
| Recently updated index | Keep README and package index connected to the actual contents. |
| Raw/diff/version groupings | Preserve version history through changelog, manifests, and package hashes. |
| Tool and policy subsections | Treat tools, permissions, safety, and failure behavior as first-class content. |
| Large technical payload | Package enough material that the ZIP is useful offline. |
| Many file-size tiers | Include quick references, medium guides, and deep technical modules. |

## What Not To Import

Do not import:

- Leaked vendor system prompts.
- Hidden tool instructions.
- Private product policy text.
- Raw prompt dumps.
- Prompt contents copied from leak-derived files.
- Machine-specific local paths.
- Claims that leaked text reflects current product behavior.

Allowed:

- Metadata about structure and size.
- Public GitHub repository link.
- High-level category observations.
- Original guidance inspired by repository organization.
- Safety notes explaining why leaked contents are not reused.

## Target Shape for This Repository

This workbench should be comprehensive across three surfaces.

### 1. Public Learning Surface

The public learning surface is the README, guides, and static site. It should
answer:

- What should a beginner read first?
- What should an advanced user use as a reference?
- Which files are prompt templates?
- Which files are workflow docs?
- Which files are source policy and publication rules?
- Which claims require official-doc verification?
- Which checks prove the repo is healthy?

The README should stay navigational, not become a giant manual. Deep content
belongs in linked guide files.

### 2. Prompting OS Package Surface

The focused ZIP should be useful offline. It should include:

- A kernel contract.
- Model-family drivers.
- Context engineering and RAG rules.
- Agent and skill patterns.
- Image prompting.
- Evaluation and optimization.
- Source map and safe synthesis rules.
- Production prompt architecture.
- Security and governance.
- Evaluation cookbook.
- Comprehensiveness benchmark.
- Master prompt template.
- Prompt quality rubric.
- Diagram or visual architecture reference.

Each important Markdown file should be long enough to teach a complete concept:
definitions, procedure, examples, failure modes, and review questions.

### 3. Maintenance Surface

The maintenance surface is tests, scripts, changelog, package manifests, and
release documentation. It should answer:

- Which files must exist?
- Which package files are included?
- Which private-looking files are excluded?
- How large and substantial is the package?
- What checks ran?
- How are generated artifacts kept out of commits?
- What changed in the public docs?

The maintenance surface prevents the repository from looking comprehensive
while quietly shipping thin or unsafe artifacts.

## Depth Targets

These are local quality targets for the focused Prompting OS package:

| Target | Reason |
| --- | --- |
| At least 14 Markdown files | Keeps the package broader than a small note bundle. |
| At least 14 Markdown files over 5 KB | Ensures each module has real technical depth. |
| At least 100 KB of Markdown source | Forces the package to contain substantial offline material. |
| Required production/security/evaluation modules | Prevents useful but shallow prompt advice. |
| Required template and rubric | Makes the package actionable, not only explanatory. |
| Deterministic ZIP and JSON manifest | Makes release artifacts auditable. |

The benchmark repository is much larger than this workbench should be. This
workbench is not trying to match an 8 MB prompt archive byte-for-byte. It is
using that archive to avoid shipping a hollow package.

## Comprehensiveness Scorecard

Use this scorecard when reviewing future additions:

| Dimension | Weak | Strong |
| --- | --- | --- |
| Breadth | One topic repeated across many pages. | Multiple task families: chat, coding, RAG, tools, image, evals, security. |
| Depth | Short definitions only. | Procedure, examples, failure modes, and verification. |
| Indexing | Files exist but readers cannot route. | README, module map, and source map point to the right places. |
| Safety | Generic disclaimer. | Concrete rules for secrets, leak-derived sources, tools, and publication. |
| Evaluation | "Looks good." | Rubrics, test cases, package-size gates, and command output. |
| Packaging | ZIP exists. | Deterministic ZIP, hashes, manifest, exclusions, and review checklist. |
| Originality | Copied prompt text. | Original synthesis from public-safe structural patterns. |

## Review Procedure

When someone says "make it more comprehensive," do this:

1. Identify the target surface: README, guides, prompt templates, package,
   tests, release docs, or static site.
2. Measure the current surface: file count, size, coverage, links, tests, and
   packaging.
3. Compare against the benchmark traits: category breadth, standalone depth,
   index quality, safety policy, and manifest evidence.
4. Add original technical content where the gap is real.
5. Add or update tests when the requirement should not regress.
6. Rebuild the package if package contents changed.
7. Run repository checks.
8. Stage the full reviewed diff if the task asks for staging.

Do not inflate files with filler just to increase byte count. Add tables,
procedures, examples, checklists, failure modes, and verification gates that
change how a reader works.

## Public-Safety Gate

Before publishing benchmark-inspired material:

- [ ] No private local path appears in public docs.
- [ ] No leaked prompt text appears in public docs.
- [ ] No hidden vendor instruction is quoted or paraphrased in detail.
- [ ] The benchmark is described as structural only.
- [ ] Fast-changing product claims are not inferred from leaked content.
- [ ] Official docs remain the authority for current behavior.
- [ ] The package manifest can prove what shipped.

## Current Package Evidence

After the expansion that added this benchmark module, the focused Prompting OS
package should be checked with:

```powershell
python scripts/create_prompting_os_package.py --version v1 --output-dir .\.tmp\prompting-os-package-check
python -m unittest discover -s tests
```

The package-depth tests require the ZIP source to remain substantial. They do
not prove every paragraph is perfect, but they do prevent the package from
collapsing back into a short README and a few thin notes.

## Final Rule

Use large prompt repositories as evidence that serious prompt work deserves
depth, organization, and maintenance. Do not use them as permission to copy
unsafe content. This repository should be lengthy because it teaches, not
because it mirrors.
