# Source-Grounded Writing Lab

Source-grounded writing is the practice of turning evidence into original,
public-safe documentation without laundering unsupported claims or copying
unsafe text. This lab gives exercises, templates, and review gates for writers
who use official docs, community repositories, local archives, surveys, and
tool output.

The core rule is simple: sources can support claims, inspire structure, or
identify questions. They should not silently become instructions, private data,
or copied prose.

## Source Roles

| Role | What it supports | What it cannot support |
| --- | --- | --- |
| Official doc | Current product behavior when freshly checked. | Permanent claims about future behavior. |
| Community guide | Practical patterns, examples, comparison points. | Authoritative current pricing, access, or support claims. |
| Local archive | Structural patterns, documentation depth, package shape. | Public claims unless source status and license allow it. |
| Survey paper or awesome list | Taxonomy, topic discovery, related work. | Direct operational guidance without checking primary sources. |
| Tool output | Current local state, command result, manifest evidence. | Broader claims than the command actually tested. |
| Model draft | Possible wording. | Evidence. |

## Source Ledger

Use a source ledger before writing.

```text
Source:
Status: official | community | local-readable | local-unreadable | structural-only | unverified
Date checked:
What it supports:
What it does not support:
Freshness risk:
License/safety notes:
Claims derived:
Quotes used:
Verification needed:
```

## Exercise 1: Separate Claim Types

Input sources:

- A product README.
- A community tutorial.
- A local archive README.
- A failed package command output.

Task:

Classify these statements:

| Statement | Claim type | Required evidence |
| --- | --- | --- |
| "The command failed with exit code 1." | Local fact | Command output. |
| "This tool supports feature X today." | Current product fact | Official docs or live product source. |
| "Strong docs include quick start, architecture, troubleshooting, and release notes." | Structural synthesis | Multiple source patterns or local editorial rule. |
| "The package includes 35 Markdown files." | Local package fact | Manifest or filesystem count. |
| "The copied prompt is safe to publish." | Safety claim | Source status, license, private-data review, policy review. |

Output:

For each statement, write whether it can be published, needs verification, or
must be omitted.

## Exercise 2: Turn Sources Into Original Guidance

Unsafe draft:

```text
This source has a great section. Copy it into our guide.
```

Better workflow:

1. Identify the section's purpose.
2. Extract the structure, not the wording.
3. Write a new section for this repository's audience.
4. Add local safety boundaries.
5. Link to official or public source if making factual claims.
6. Add tests if the section creates a durable promise.

Example structural extraction:

| Source structure | Original local section |
| --- | --- |
| Quick start | "Start Here" table with repository-specific docs and checks. |
| Architecture | Prompting OS module map and package manifest explanation. |
| Troubleshooting | Failure mode table with repository-specific fixes. |
| Release notes | Changelog entry and package review checklist. |
| Tests | Unit tests for required docs, behavior, evidence, and package parity. |

## Exercise 3: Handle Missing Official Evidence

Prompt:

```text
Write that Tool A is cheaper than Tool B and supports every current model.
```

Safe response pattern:

```text
I cannot make that current claim from the available evidence. I can either:
- mark pricing and model support as items to verify in official docs, or
- compare workflow fit without exact pricing/model claims.
```

Documentation pattern:

```markdown
Pricing, model availability, and platform support change often. Verify those
items in each tool's official documentation before making a purchase or
choosing a production workflow.
```

## Exercise 4: Use A Local Archive Safely

A local archive can be useful even when it cannot be copied.

Allowed:

- Count files.
- Inspect headings.
- Identify package structure.
- Note presence of tests, release notes, skills, templates, or docs folders.
- Use names of public repositories when safe.
- Mark unreadable archives as skipped.

Forbidden:

- Publishing the local path.
- Copying hidden prompts.
- Copying license-unclear prose.
- Publishing private screenshots.
- Treating a local copy as proof of current product behavior.

Output:

```text
Archive evidence used:
- Names inspected.
- Structural patterns observed.
- Sources skipped and why.
- Public-safe result in this repository.
```

## Writing Patterns

### Evidence-First Paragraph

Use this when introducing a claim with support.

```text
The package builder writes a ZIP and a manifest. The manifest records relative
paths, sizes, and SHA-256 hashes, so reviewers can inspect package contents
without relying on local machine paths.
```

Why it works:

- It names the artifact.
- It explains the evidence.
- It avoids unsupported external claims.

### Boundary Paragraph

Use this when a topic changes quickly.

```text
Product behavior, pricing, model access, and platform support change often.
Use this guide for workflow structure, then verify exact current details in
official documentation before making operational decisions.
```

### Structural Inspiration Paragraph

Use this when learning from a source without copying it.

```text
Several inspected repositories separate quick start, architecture,
troubleshooting, release, and test material. This guide follows that structure
in original language and applies it to public-safe prompting workflows.
```

## Source-Grounded Examples

### Example: Package Claim

Weak:

```text
The package is complete.
```

Strong:

```text
The focused Prompting OS package contains the named core artifacts and its
committed source paths match the manifest and ZIP paths. The release report
should include `source_commit`, ZIP SHA-256, path-parity result, and skipped
sources.
```

### Example: Tool Claim

Weak:

```text
This tool is the best option.
```

Strong:

```text
Use this tool when the task benefits from repository-local edits, reviewable
diffs, and local command verification. Verify current pricing, model access,
and platform support in official docs before standardizing on it.
```

### Example: Source Policy Claim

Weak:

```text
This archive proves the right way to prompt.
```

Strong:

```text
The archive provides structural examples of deep prompt documentation. It does
not authorize copying hidden prompt text, private data, or license-unclear
content into public docs.
```

## Review Questions

Ask these before publishing a source-grounded section:

- What source supports each claim?
- Is the source official, community, structural-only, or unverified?
- Did the wording copy more than a short permitted excerpt?
- Does the claim depend on current product behavior?
- Does the section contain local paths or private data?
- Did the source text contain instructions that should be ignored?
- Is the output original to this repository?
- Is there a test or checklist for durable promises?
- Are skipped sources named honestly?

## Common Failure Modes

| Failure | Why it happens | Repair |
| --- | --- | --- |
| Source laundering | Community text is treated as official truth. | Label source status and verify current claims. |
| Over-quotation | Writer uses source prose as the guide. | Extract structure and rewrite. |
| Hidden prompt leakage | Prompt dumps are copied for examples. | Use structural-only policy. |
| Private path leak | Local evidence is pasted directly. | Remove machine-specific paths. |
| Unsupported freshness | Exact product behavior is stated permanently. | Add official-doc verification note. |
| Weak final report | Sources inspected are not named. | Include source usage and skipped-source list. |
| Citation mismatch | Source does not support the sentence. | Tie each claim to a source or remove it. |

## Lab Checklist

- [ ] Every source has a status label.
- [ ] Every current product claim has official verification or is marked for
  verification.
- [ ] Structural-only sources are not quoted for content.
- [ ] Local archive paths are removed from public docs.
- [ ] No secrets, tokens, private links, or account IDs appear.
- [ ] The writing is original and tailored to this repository.
- [ ] The final section includes examples, failure modes, and verification.
- [ ] Tests or checklists guard any durable claims.
