# Prompt Metrics And Telemetry

Prompt systems need measurement, but the measurement should fit the risk and
privacy profile of the repository. This module describes lightweight metrics
for prompt libraries, coding-agent workflows, RAG answers, documentation
packages, and release artifacts.

Telemetry in this context does not mean collecting private user data. For this
public workbench, prefer local, aggregate, reviewable evidence: file counts,
test results, manifest metrics, rubric scores, source labels, and failure
counts.

## Measurement Principles

| Principle | Meaning |
| --- | --- |
| Measure behavior | Track whether prompts produce required outputs, not whether they sound confident. |
| Avoid private data | Do not collect prompts, source text, paths, or account details unless explicitly public and intended. |
| Keep metrics reviewable | Prefer manifest fields, tests, and small CSV/Markdown summaries over opaque dashboards. |
| Track regressions | A metric is most useful when it catches a change from previously accepted behavior. |
| Separate quality from volume | More files, tokens, or examples do not prove better quality without review gates. |

## Core Metrics

| Metric | Use | Evidence source |
| --- | --- | --- |
| Prompt-template section coverage | Ensures reusable prompts remain operational. | Tests over `prompts/**`. |
| Package inventory counts | Describes an artifact; does not grade quality. | Manifest. |
| Source/manifest/archive parity | Detects missing, extra, or renamed package paths. | Git tree, manifest, and ZIP listing. |
| Required module presence | Prevents accidental package omissions. | Health check and package tests. |
| Secret/private-path matches | Public-safety guard. | Health check and targeted search. |
| Unit test pass/fail | Regression guard. | `python -m unittest discover -s tests`. |
| Package hash | Release artifact identity. | Manifest and file hash. |
| Source-status coverage | Prevents source laundering. | Source ledgers and review notes. |

## Prompt Quality Metrics

For prompt templates:

- Required section count.
- Number of explicit inputs.
- Presence of included and excluded scope.
- Presence of safety boundaries.
- Presence of verification commands or checks.
- Presence of final report format.
- Presence of failure cases.
- Number of evaluation examples.
- Last reviewed date.

Do not measure prompt quality by length alone. A long prompt can still be
unsafe, vague, or impossible to verify.

## Agent Workflow Metrics

For coding-agent tasks:

| Metric | Why |
| --- | --- |
| Files inspected before edit | Shows context discipline. |
| Files changed | Indicates scope. |
| Tests run | Shows verification effort. |
| Checks failed | Shows remaining risk. |
| Commands requiring approval | Shows operational risk. |
| Public-safety scan result | Protects repository hygiene. |
| Unverified items | Prevents overclaiming. |
| Time or iteration count | Helps identify hard-to-maintain workflows. |

These metrics can live in final reports or PR descriptions rather than a
central database.

## RAG Metrics

For source-grounded answers:

- Number of sources.
- Source status distribution.
- Unsupported claims removed.
- Claims marked unverified.
- Citation mismatches found.
- Prompt-injection snippets ignored.
- Official-doc checks performed.

RAG metrics should never reward citing more sources if the sources are weak.
The goal is claim support, not citation volume.

## Package Metrics

Package metrics are mandatory for focused package changes.

```text
Markdown files:
Markdown bytes:
Shortest Markdown:
ZIP files:
ZIP size:
ZIP SHA-256:
Manifest path:
Required modules present:
Excluded file rules:
```

These metrics are easy to derive and hard to fake when reviewers inspect the
manifest.

## Privacy Boundaries

Do not collect:

- Full user prompts from private work.
- Private source text.
- Absolute local paths.
- Account identifiers.
- API keys, tokens, cookies, or credentials.
- Browser profile contents.
- Hidden system prompts.
- Private test outputs.

Safe to collect:

- Public file paths relative to repository root.
- File sizes.
- Hashes of release artifacts.
- Test names and pass/fail results.
- Source status labels.
- Manual rubric scores.
- Counts of missing required sections.

## Metrics Review

Ask:

- Does this metric map to a real quality or safety promise?
- Could this metric expose private data?
- Can a reviewer reproduce it locally?
- Can it fail when the repository regresses?
- Does it encourage harmful behavior, such as adding filler to meet a byte
  floor?

If a metric creates bad incentives, pair it with a human review gate.

## Completion Checklist

- [ ] Metrics are tied to explicit repository promises.
- [ ] Metrics avoid private user data.
- [ ] Package metrics include count, byte, shortest file, and hash evidence.
- [ ] Prompt metrics include required-section coverage.
- [ ] RAG metrics include source status and unsupported-claim handling.
- [ ] Final reports include unverified items, not only success metrics.
