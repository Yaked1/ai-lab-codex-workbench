# Archive Corpus Source Map

This module records how a local archive corpus was used as a structural
benchmark for this Prompting OS package. It intentionally avoids local machine
paths, private notes, copied prompt dumps, and long excerpts from third-party
repositories. The goal is to preserve the useful lessons: repository shape,
documentation depth, package organization, safety gates, and verification
habits.

The corpus was treated as evidence, not as authority. A repository can be
useful as a model of organization while still being unsuitable for content
reuse because of license ambiguity, stale product claims, private material, or
leak-derived prompt text.

## Inspection Contract

Every source inspection should answer five questions before any repository
content is changed.

| Question | Evidence to collect | Use in this repository |
| --- | --- | --- |
| What kind of project is it? | README headings, directory names, package files, docs folders, tests. | Decide whether it teaches docs depth, prompt libraries, agent operations, tooling, or package practice. |
| Is it public-safe? | License file, public README, absence of private data, absence of leaked hidden prompts. | Use directly only when source status is acceptable; otherwise use structural lessons only. |
| What is the durable pattern? | Tables of contents, examples, checklists, failure modes, manifests, rubrics. | Rebuild the pattern in original language for this workbench. |
| What must not be copied? | Secrets, local paths, private links, hidden prompts, account-specific screenshots, license-unclear bulk text. | Exclude from docs and tests. |
| How will reuse be verified? | Public-safety scan, package manifest, tests, changelog, source-policy note. | Keep the result reviewable and reproducible. |

## Top-Level Archive Inventory

The local archive contained twenty-five top-level files with `.zip` names and
two directories for extracted material. Direct ZIP inspection was attempted for
each archive. Some files had local ZIP headers but could not be read through
the standard ZIP central directory reader; those were not used for direct text
inspection in this pass.

| Archive name | Direct ZIP read | Safe use in this package |
| --- | --- | --- |
| `agent-coworker-main.zip` | Readable | Agent workbench shape, multiple interfaces, skill folders, desktop/app docs, tests. |
| `aws-samples-amazon-bedrock-samples.zip` | Central directory unreadable in local scan | Structural mention only unless recovered separately. |
| `aws-samples-generative-ai-use-cases.zip` | Central directory unreadable in local scan | Structural mention only unless recovered separately. |
| `aws-samples-sample-building-intelligent-multimodal-applications-with-Nova.zip` | Central directory unreadable in local scan | Structural mention only unless recovered separately. |
| `Azure-Samples-visionary-lab.zip` | Central directory unreadable in local scan | Structural mention only unless recovered separately. |
| `chromex-main.zip` | Readable | Browser bridge architecture, runtime boundary notes, release management, extension safety patterns. |
| `CL4R1T4S-main.zip` | Readable | Small repository shape and README taxonomy. |
| `claude-mem-9.0.12.zip` | Readable | Memory architecture docs, worker service notes, hook docs, viewer docs, multilingual documentation shape. |
| `claw-code-main.zip` | Readable | Porting-status documentation, parity checkpoints, repository layout, test scaffolding. |
| `git-time-explorer-main.zip` | Readable | Small tool README and license practice. |
| `gjtjx-awesome-structued-prompts.zip` | Readable | Prompt collection organization and index style, used structurally only. |
| `GoogleCloudPlatform-generative-ai.zip` | Central directory unreadable in local scan | Structural mention only unless recovered separately. |
| `JindongGu-Awesome-Prompting-on-Vision-Language-Model.zip` | Readable | Vision-language prompt survey organization, used structurally. |
| `langgptai-Awesome-Multimodal-Prompts.zip` | Central directory unreadable in local scan | Structural mention only unless recovered separately. |
| `microsoft-Build25-LAB324.zip` | Central directory unreadable in local scan | Structural mention only unless recovered separately. |
| `microsoft-generative-ai-for-beginners.zip` | Central directory unreadable in local scan | Structural mention only unless recovered separately. |
| `nidhinjs-prompt-master.zip` | Readable | Prompt template sectioning and small template-library shape. |
| `openai-openai-cookbook.zip` | Central directory unreadable in local scan | Structural mention only unless recovered separately; product behavior must be verified in official docs before claims. |
| `page-agent-main.zip` | Readable | Browser page-agent package structure, quick starts, use-case framing. |
| `Prompt-Engineering-Guide-main.zip` | Readable | Large guide architecture, nested indexes, conceptual breadth, reference taxonomy. |
| `promptslab-Awesome-Prompt-Engineering.zip` | Readable | Awesome-list organization and source aggregation patterns. |
| `rsmdt-multimodal-mcp.zip` | Readable | MCP and multimodal tool boundary patterns. |
| `stop-slop-main.zip` | Readable | Anti-slop criteria and small opinionated guide shape. |
| `superpowers-main.zip` | Readable | Skill library docs, test README, release notes, skill packaging. |
| `YingqingHe-Awesome-LLMs-meet-Multimodal-Generation.zip` | Readable | Multimodal generation survey structure, used structurally. |

## Extracted Folder Findings

The extracted folder set provided the most useful direct inspection surface
because files could be searched, counted, and sampled without modifying the
archives.

| Extracted project | Structural lessons |
| --- | --- |
| `agent-coworker-main` | A serious agent workbench separates interfaces, skills, tests, desktop notes, and tool protocols. It does not rely on one README to carry every detail. |
| `chromex-main` | Browser/extension projects need runtime boundary sections, privacy defaults, development commands, release notes, and troubleshooting. |
| `claude-mem-9.0.12` | Memory and worker systems benefit from architecture notes, service route maps, hook integration docs, and explicit beta/requirements sections. |
| `claw-code-main` | Rewrite or parity projects should expose current status, repository layout, quick start, parity checkpoint, and test strategy. |
| `page-agent-main` | Page automation tools need quick integration paths, use cases, package boundaries, and contribution notes. |
| `superpowers-main` | Skill libraries should include installation paths, verification, basic workflow, skill inventory, release notes, and tests. |

## Patterns Promoted Into This Package

The source corpus encouraged this package to expand in specific ways.

| Pattern | Why it matters | Local implementation |
| --- | --- | --- |
| Multiple indexes | Readers need entry points by role and task, not one linear document. | Root README, Prompting OS README, guide README, release docs, and offline site cross-link each other. |
| Behavior-focused modules | Readers need procedures, examples, failures, and checks. | Tests preserve those bounded surfaces. |
| Tool boundary sections | Agent and browser tooling can touch files, pages, commands, and accounts. | Agent, RAG/tool, permission, and safety modules define allowed actions and verification. |
| Package manifests | Release artifacts need reviewable evidence. | The Prompting OS package writes a manifest with relative paths, sizes, and SHA-256 hashes. |
| Release notes | Users need to know why a snapshot changed. | Changelog entries describe documentation expansion, package gates, and public-safety changes. |
| Test READMEs and rubrics | Human docs still need objective gates. | Unit tests enforce named paths, behavior, evidence, parity, and prompt-template sections. |
| Public-safe source policy | Prompting repositories often mix official, community, inferred, and unsafe material. | Source status labels keep structural inspiration separate from direct claims. |
| Troubleshooting tables | Beginners recover faster when failures are named. | Guides include failure modes, checks, and repair paths. |

## Structural Use Rules

Use a source as structure when the source is useful but not safe for direct
content reuse.

Allowed structural observations:

- It has a top-level README with quick start, architecture, troubleshooting,
  and release sections.
- It keeps prompt assets separate from evaluation assets.
- It includes tests that verify package shape.
- It names runtime boundaries and permissions.
- It uses release notes and manifests.
- It marks beta, limitations, or unsupported behavior.

Forbidden structural shortcuts:

- Copying a hidden prompt or leaked instruction because it has a useful shape.
- Keeping a private local path in a public doc as proof of inspection.
- Copying license-unclear prose into a public guide.
- Treating a community repository as proof of current product behavior.
- Reusing screenshots, account URLs, private logs, or personal environment
  details.

## Source Status Labels

Use these labels in source notes, guide drafts, and prompt-library metadata.

| Label | Meaning | Reuse allowed |
| --- | --- | --- |
| Official | Vendor or project documentation controlled by the product owner. | Direct factual claims may be used with citation and date-sensitive caution. |
| Public community | Public repository, blog, or guide with ordinary public content. | Patterns and limited factual claims; verify fast-changing product behavior separately. |
| Survey or awesome list | Curated reference list or literature map. | Taxonomy and discovery only unless individual sources are checked. |
| Local archive readable | Local copy could be inspected with standard tools. | Structural use after public-safety review. |
| Local archive unreadable | Local copy could not be inspected through the standard ZIP reader. | Do not use for content; mention only as skipped evidence if needed. |
| Leak-derived or private | Hidden prompts, private logs, credentials, private paths, or leaked material. | Structural lessons only, never prompt text or private facts. |
| Unverified | Claim has not been checked against an authoritative current source. | Mark as unverified or omit. |

## Corpus-To-Workbench Translation

The archive scan produced the following translation rules.

1. A README should work as a manual.
   A strong README is not only a pitch. It tells readers where to start, what
   each folder means, how to run checks, how to avoid dangerous actions, how to
   package artifacts, and how to contribute.

2. A package should work offline.
   If a focused package is worth building, it should not require users to hunt
   through the whole repository for context. It needs its own index, examples,
   evaluation notes, safety rules, and release instructions.

3. Prompt libraries need metadata.
   A prompt without target tool, inputs, scope, safety boundaries,
   verification, and final report format is hard to reuse and harder to audit.

4. Tool docs need permission models.
   Browser agents, coding agents, MCP tools, local scripts, and release
   builders all need clear boundaries around read, write, network, account, and
   destructive actions.

5. Public docs must avoid source laundering.
   A source can inspire structure without giving permission to copy text,
   claims, data, or examples.

6. Tests should defend the documentation promise.
   Tests should fail when named modules disappear or examples, failure behavior,
   verification, source identity, or package parity drift.

## Audit Trail Template

Use this template when adding another corpus-inspired expansion.

```text
Source set:
- Names inspected:
- Source status:
- License or safety notes:
- Direct text copied:
- Structural patterns used:
- Product claims requiring official verification:
- Files changed:
- Tests updated:
- Public-safety scan:
- Remaining skipped sources:
```

## Red Flags During Source Use

Stop and reassess when any of these appear:

- The source contains hidden system prompts or private chat transcripts.
- The source includes account-specific dashboards, URLs, IDs, cookies, or
  OAuth material.
- The source contains exact product pricing, model availability, or platform
  support claims that may have changed.
- The source license is missing or unclear and the intended reuse is more than
  a structural observation.
- The source uses screenshots or binary assets that cannot be audited.
- The source includes local file paths or personal machine details.
- The source claims benchmark results without reproducible setup.
- The source encourages bypassing product limits or permissions.

## Completion Checklist

Before closing a corpus-inspired expansion:

- [ ] Every directly inspected source is named without private paths.
- [ ] Unreadable archives are listed as skipped or structural-only.
- [ ] No local archive path appears in public repository files.
- [ ] No leaked prompt text or private source text appears in the docs.
- [ ] New docs are original and tied to this workbench's audience.
- [ ] Package tests enforce the named behavior and evidence promise.
- [ ] Release docs explain how to inspect the package manifest.
- [ ] Changelog records user-visible expansion.
- [ ] Public-safety scans cover secrets, private paths, and unsupported claims.
- [ ] The final report distinguishes verified evidence from skipped sources.
