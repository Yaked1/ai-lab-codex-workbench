# Image Generation Guides

This folder teaches public-safe image prompting and workflow selection. GitHub
Actions in this repository document and validate guides; they must not run
complex image-generation models.

## Guide Map

| Guide | Use it for |
| --- | --- |
| [Autoregressive image models](autoregressive-image-models.md) | Browser/API image systems that generate images token-by-token or through multimodal model stacks. |
| [Diffusion models](diffusion-models.md) | Local and cloud diffusion workflows, strengths, and warnings. |
| [Local image generation](local-image-generation.md) | Separating lightweight experiments from advanced GPU setups. |
| [Hardware requirements](hardware-requirements.md) | Realistic browser/API, CPU-only, entry GPU, advanced GPU, and cloud guidance. |
| [Prompting patterns](prompting-patterns.md) | Prompt templates for text rendering, style, product shots, characters, and 3D references. |

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
