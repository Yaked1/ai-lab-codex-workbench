# Image Generation Guides

This folder teaches public-safe image prompting and workflow selection. GitHub
Actions in this repository document and validate guides; they must not run
complex image-generation models.

Every guide in this folder assumes the same default: start browser/API-first,
treat local generation as an optional advanced tier, and verify fast-changing
product details (pricing, model names, exact hardware limits) in official
docs before publishing them anywhere.

## Guide Map

| Guide | One-line description | Use it for |
| --- | --- | --- |
| [Diffusion models](diffusion-models.md) | How denoising-based image models respond to prompts, and how that differs from chat prompting. | Understanding positive/negative prompts, weighting conventions, samplers, and img2img vs txt2img. |
| [Autoregressive image models](autoregressive-image-models.md) | How token-by-token and multimodal image systems read ordered, structured prompts. | Layout-precise images, text-in-image tasks, and iterative conversational edits. |
| [Transformer architecture](transformer-architecture.md) | How tokens, embeddings, attention, spatial encodings, multimodal conditioning, and decoding show up in image generation. | Explaining why structured prompts can help layout, text rendering, and revision workflows without overclaiming product internals. |
| [Reasoning-integrated image generation](reasoning-integrated-image-generation.md) | How planning, critique, multimodal analysis, and generation can work together in modern image workflows. | Diagram-like images, short text labels, iterative edits, and output review against a written brief. |
| [Prompting patterns](prompting-patterns.md) | A worked library of prompt templates and before/after revisions. | Copy-paste starting points for product shots, characters, posters, and 3D references. |
| [Hardware requirements](hardware-requirements.md) | Generic hardware tiers, decision table, and troubleshooting table. | Deciding whether your machine can run local generation at all, and diagnosing failures. |
| [Local image generation](local-image-generation.md) | Safety/setup checklist for running any local tool, plus when local is not worth it yet. | Beginners deciding whether to try local generation, and what to isolate if they do. |

## Decision Guide: Where Do I Start?

Answer these in order. Stop at the first row that matches you.

| Your situation | Start here |
| --- | --- |
| You have no dedicated GPU, or you are not sure what GPU you have. | [Hardware requirements](hardware-requirements.md), then [prompting-patterns.md](prompting-patterns.md). Use browser/API tools exclusively. |
| You just want to write better prompts, regardless of tool. | [Prompting patterns](prompting-patterns.md) first, then skim [diffusion-models.md](diffusion-models.md) and [autoregressive-image-models.md](autoregressive-image-models.md) to know which conventions apply to your tool. |
| You are choosing between a diffusion tool and a multimodal/autoregressive tool. | Read [diffusion-models.md](diffusion-models.md) and [autoregressive-image-models.md](autoregressive-image-models.md) back to back; the "when to prefer" sections in each cover the same decision from both sides. |
| You need to explain how modern image systems use transformers. | Read [Transformer architecture](transformer-architecture.md), then compare [Autoregressive image models](autoregressive-image-models.md) and [Diffusion models](diffusion-models.md). |
| Your task needs planning, counts, text labels, or diagram-like review. | Use [Reasoning-integrated image generation](reasoning-integrated-image-generation.md), then adapt the [Prompting patterns](prompting-patterns.md) templates. |
| You want to run something locally, "just to see." | [Local image generation](local-image-generation.md) first, specifically the "when local isn't worth it yet" section, before touching [hardware-requirements.md](hardware-requirements.md). |
| You have verified you have an advanced GPU tier and understand model licenses. | [Hardware requirements](hardware-requirements.md) decision table, then [local-image-generation.md](local-image-generation.md) setup checklist. |

If you only read one file in this folder, read `prompting-patterns.md` — the
prompt quality gap is usually larger than the tool-choice gap.

## Workflow Categories

- Browser/API tools: best beginner default.
- Lightweight local tools: small experiments only.
- Quantized/local-friendly setups: advanced experiments that must still state
  quality, speed, and compatibility tradeoffs.
- Advanced local GPU workflows: for users who understand model files, VRAM, and licenses.
- Cloud workflows: for heavy generation, batch jobs, or training.

## Model And Tool Families

| Section | Guidance |
| --- | --- |
| Autoregressive image models | Prefer official browser/API docs unless a local setup is verified. |
| Diffusion models | Separate browser/API, lightweight local, advanced GPU, and cloud paths. |
| Transformer-based components | Explain tokens, embeddings, attention, spatial encodings, and multimodal conditioning as concepts, not as guaranteed internals for every product. |
| Reasoning-integrated autoregressive image systems | Use planning, entity inventories, layout checks, and revision prompts; still require manual review and official-doc verification. |
| Hybrid systems | Treat mixed multimodal, retrieval, editing, or diffusion-plus-agent systems as advanced until the setup is verified. |
| Browser/API image models | State API key, subscription, policy, and privacy requirements. |
| Local image generation tools | Include install commands only when verified; otherwise use placeholders. |
| Quantized/local-friendly setups | Warn about quality loss, unsupported hardware, and slow CPU fallback. |
| Heavy GPU setups | Keep out of beginner defaults and document VRAM, disk, license, and cloud alternatives. |

## Entry-Level Hardware Warning

On entry-level hardware without a capable GPU (integrated graphics or a low-VRAM
discrete GPU):

- Prefer browser/API image generation.
- Use lightweight local experiments only.
- Avoid heavy diffusion models as beginner defaults.
- Avoid local training or fine-tuning.
- Avoid vLLM, SGLang, and heavy GPU serving workflows.
- Use cloud or server GPUs only as advanced options.

## Decision Flow

Use this flow before recommending an image-generation workflow.

| Question | If yes | If no |
| --- | --- | --- |
| Is the user a beginner or workshop learner? | Prefer browser/API tools and prompt-pattern exercises. | Consider local or cloud only if the reader has the required setup. |
| Is exact current product behavior needed? | Verify in official docs before publishing. | Use general workflow guidance and mark details as examples. |
| Does the workflow require model weights or checkpoints? | Treat it as advanced and document license/storage risks. | Keep setup lighter and focus on prompt design. |
| Does the task involve private images, faces, products, or brand assets? | Add explicit consent, license, and privacy checks. | Still avoid invented private logos or account details. |
| Will the repo or CI run generation? | Do not do that in this public workbench. | Use static docs and tests instead. |

## Public-Safe Image Prompt Contract

Every reusable image prompt should define:

- Purpose: documentation image, product draft, UI mood reference, character
  sheet, diagram, or marketing concept.
- Subject: the object, scene, or visual idea.
- Composition: camera angle, layout, background, crop, and aspect ratio.
- Style constraints: medium, lighting, materials, rendering style, and mood.
- Text requirements: exact text, maximum length, and manual review needs.
- Source status: reference image ownership, license, and consent.
- Safety boundaries: no private people, private logos, account details,
  medical/legal claims, or unsafe content.
- Verification: what the reviewer must inspect in the output.

## Example Workflow

1. Write a short purpose statement.
2. Choose browser/API, lightweight local, advanced local, or cloud.
3. Draft the prompt with subject, composition, constraints, and output format.
4. Add negative prompt only if the tool supports it.
5. Generate one or more drafts outside the repository.
6. Inspect for text accuracy, private data, brand drift, unsafe content, and
   license issues.
7. Store only public-safe final assets if the repository explicitly needs an
   image. Otherwise keep the image out of Git and document the prompt.

## Review Questions

- Does the guide recommend a beginner-safe path first?
- Are local hardware assumptions realistic?
- Are exact product, model, pricing, and setup claims marked for official-doc
  verification?
- Are private references, faces, logos, and datasets excluded unless permission
  is explicit?
- Does the prompt specify what to inspect after generation?
- Does the repository avoid committing model files, generated archives, and
  private prompt histories?

## Where This Folder Connects

- Prompt system design: [Prompting OS image engine](../prompting-os/05-image-prompting-engine.md)
- Source and safety policy: [Publication policy](../publication-policy.md)
- Prompt audit: [Prompt audit checklist](../guides/prompt-audit-checklist.md)
- Tool comparison: [Tool comparison matrix](../tools/comparison-matrix.md)
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **image-generation guide** surface. During broad
maintenance, reviewers should treat `docs/image-generation/README.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `README` state what decision, workflow, or reusable behavior it supports?
- Are included scope, excluded scope, and unsafe actions clear enough for an
  agent or contributor to follow?
- Are examples public-safe, repository-relative, and free of private data?
- Are fast-changing product or platform claims phrased conservatively or marked
  for official-doc verification?
- Does the file point to the next artifact a reader should inspect: a command,
  template, test, manifest, package, or deeper guide?
- Could a reviewer cite this file in a PR review and know what evidence proves
  the work is complete?

Keep future edits focused on stronger evidence, clearer failure modes, better
navigation, and safer automation boundaries. Do not add length unless the new
material makes the repository easier to operate, teach, audit, or recover.
<!-- RESEARCH-GRADE-EXPANSION:END -->
