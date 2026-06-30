# Diffusion Models

Diffusion models generate images through iterative denoising. They are powerful,
but local workflows often require large model files, VRAM, disk space, and
careful license review.

## Beginner Fit

Browser/API diffusion tools can be beginner friendly. Local diffusion stacks are
advanced and assume a capable GPU.

## Workflow Types

| Type | Fit | Notes |
| --- | --- | --- |
| Browser/API | Best beginner default | No local GPU setup; verify pricing and terms. |
| Lightweight local experiment | Limited | Small models or CPU paths can be slow but educational. |
| Advanced local GPU | Advanced | Requires VRAM, disk, model licenses, and troubleshooting. |
| Cloud GPU | Advanced | Good for heavy runs; watch cost and data policy. |

## Negative Prompting

Negative prompts are useful in some diffusion systems, but behavior varies by
tool. Keep them specific and public-safe:

```text
Negative prompt: distorted text, extra fingers, private logos, watermarks,
personal data, unsafe content, low-resolution artifacts
```

## Entry-Level Hardware Warning

On entry-level hardware without a capable GPU, do not make heavy diffusion
workflows the beginner default. Prefer browser/API tools or cloud runs.

## Failure Modes

- Out-of-memory errors.
- Very slow CPU generation.
- Missing model files.
- License mismatch between model, LoRA, checkpoint, or workflow.
- Unsafe prompts or private reference images.

## Verification Checklist

- [ ] Model and workflow licenses are checked.
- [ ] Hardware requirements are stated.
- [ ] Beginner alternatives are listed.
- [ ] No GitHub Action runs the model.
- [ ] No private images or prompts are committed.

## Prompt Anatomy For Diffusion

Diffusion prompts are usually stronger when they separate visual intent from
cleanup instructions.

```text
Subject: [main object, scene, or character].
Composition: [camera angle], [framing], [background], [aspect ratio].
Visual details: [materials], [colors], [lighting], [texture].
Style constraints: [photorealistic, editorial, 3D render, diagrammatic].
Safety constraints: no private logos, no private people, no personal data.
Negative prompt, if supported: [specific artifacts to avoid].
Review: check hands, text, brand drift, background details, and license status.
```

Avoid extremely long negative prompts that become superstition. If an artifact
keeps appearing, revise the positive prompt and inspect whether the selected
model or workflow is the real cause.

## Local Workflow Review

Before publishing local diffusion instructions, record:

| Item | Why it matters |
| --- | --- |
| Tool name and source | Prevents unofficial download links from becoming the install path. |
| Model/checkpoint source | Model files may have separate licenses and safety restrictions. |
| VRAM and disk assumptions | Readers need to know whether the workflow is realistic. |
| Python/Node requirements | Version mismatch is a common setup failure. |
| Output storage | Generated archives can become large or private. |
| CI boundary | The repository should validate docs, not run the model. |

## Beginner-Friendly Alternative

When a guide describes a local diffusion workflow, include a low-risk fallback:

```text
If you only want to learn prompt structure, use a browser/API image tool first.
Practice subject, composition, lighting, style constraints, and review. Move to
local diffusion only after you understand model licenses, hardware limits, and
where generated files will live.
```

## Troubleshooting Table

| Problem | Likely cause | Safe response |
| --- | --- | --- |
| Out of memory | Resolution, batch size, or model is too large. | Lower resolution/batch, use a smaller model, or switch to hosted/cloud. |
| Slow CPU fallback | GPU acceleration is missing or unsupported. | Do not present CPU generation as a beginner default. |
| Bad text in image | Diffusion system may not render exact text reliably. | Keep text short or add manual typography after generation. |
| Unwanted brand-like marks | Model learned visual artifacts or prompt is too vague. | Add public-safe constraints and reject outputs with invented logos. |
| License uncertainty | Model, LoRA, or workflow source is unclear. | Do not publish setup as recommended until license is reviewed. |
