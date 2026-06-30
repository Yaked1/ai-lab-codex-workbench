# Publication Policy

This repository is public educational material. Published guides must be useful,
attributed, reproducible, and safe for a general audience.

## Core Rules

- Do not republish leaked system prompts verbatim.
- Do not publish private, proprietary, or copyrighted prompt dumps.
- Do not publish secrets, tokens, private paths, private emails, private
  memories, private conversations, OAuth files, browser session data, or logs
  that may contain credentials.
- Prefer official documentation when available.
- Clearly label unofficial, community, leaked, inferred, or unverified sources.
- Respect source licenses and attribution requirements.
- Avoid bypass, exfiltration, prompt leakage, malware, credential theft, abuse,
  jailbreak, or evasion content.
- Do not mirror leaked prompt repositories.
- Do not build guides that encourage prompt leaking or jailbreaks.
- Do not recommend heavy local models or heavy image-generation stacks as
  beginner defaults.

## Leak-Derived Or Unofficial Prompt Sources

Repositories such as `asgeirtj/system_prompts_leaks` may be used only for:

- Pattern extraction.
- Structural comparison.
- Public-safe summaries.
- Short attributed excerpts only when legally safe and necessary.
- Links to source pages.

They must not be used to copy, mirror, or normalize leaked prompts into this
repository.

## Source Labels

Use one of these labels in curated docs:

| Label | Meaning |
| --- | --- |
| Official documentation | Published by the tool or project maintainer. |
| Official repository | Source repository controlled by the project maintainer. |
| Community repository | Public user/community project; verify license and maintenance. |
| Unofficial source | Not controlled by the vendor or maintainer. |
| Leak-derived source | Use only for structural pattern extraction and public-safe summaries. |
| Inferred | Reasoned from public behavior; do not present as confirmed fact. |
| Unverified | Needs official confirmation before exact commands or claims are published. |

## Image Generation Guidance

Separate image-generation workflows into:

- Browser/API tools for beginners.
- Lightweight local tools for small experiments.
- Advanced local GPU workflows.
- Cloud GPU or managed workflows.

On entry-level hardware without a capable GPU, prefer browser/API image
generation or lightweight local experiments.
Avoid heavy diffusion models, local training, fine-tuning, vLLM, SGLang, and
large GPU workflows as beginner defaults.

## Automation Boundary

The daily scout may collect candidate metadata and write inbox reports. It must
not call Codex, require OpenAI API keys, publish polished guides, create
releases, call model providers, or run image-generation models.

The curator prompt prep workflow may prepare a ready-to-copy local Codex prompt
only when manually triggered. Actual Codex writing happens locally through Codex
CLI or the Codex app, followed by branch, pull request, checks, and human review.

## Attribution Requirements

Every guide that is materially informed by external material should make the
source status clear. A short source note is enough for most docs, but deeper
guides should include a source ledger or reference section. The goal is to make
the origin of ideas auditable without copying private, leaked, or copyrighted
material into the repository.

Use this minimum standard:

- Official docs: link to the relevant page and note that behavior may change.
- Official repositories: link to the repository and verify the license.
- Community repositories: link to the source, verify the license, and avoid
  overstating maintenance status.
- Archive corpus material: use it for structure and coverage ideas, then write
  original guidance in this repository's voice.
- Leak-derived sources: do not mirror or normalize the prompt text.

## Pre-Publication Review

Before merging public-facing content, reviewers should confirm:

- No token-like strings, private paths, private account IDs, or private logs are
  present.
- External claims are either evergreen or marked for official-doc verification.
- Source/license status is documented where source material shaped the guide.
- Automation remains bounded, preview-first, and human-reviewed.
- Beginner recommendations do not assume heavy GPU, local training, or complex
  provider setup by default.
- The content teaches safe workflow habits instead of bypassing review.

## Incident Response

If private or unsafe material is found after publication:

1. Stop expanding the affected content.
2. Remove the unsafe material in the smallest possible follow-up change.
3. Rotate exposed credentials if any real secret or auth material appeared.
4. Review commit history and release assets for the same material.
5. Add a changelog or release note when users need to understand the correction.

Do not replace an incident response with vague wording. Name the class of issue
and the corrective action while avoiding repetition of the sensitive material.
