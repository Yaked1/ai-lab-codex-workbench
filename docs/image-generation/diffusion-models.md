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
