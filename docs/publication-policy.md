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
