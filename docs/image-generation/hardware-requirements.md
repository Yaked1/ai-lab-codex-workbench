# Image Generation Hardware Requirements

Hardware requirements vary by model, resolution, batch size, precision, and
tooling. Treat exact requirements as official-doc verification items.

## Practical Table

| Hardware | Realistic use | Avoid |
| --- | --- | --- |
| Browser or API only (no local GPU) | Hosted browser/API tools; prompt writing practice. | Any local model download or local generation. |
| Entry laptop: integrated or low-end discrete GPU, about 2 GB VRAM or less | Browser/API tools; lightweight local experiments; prompt writing practice. | Heavy diffusion, training, fine-tuning, vLLM, SGLang, large local serving. |
| 16 GB RAM, 4-6 GB VRAM | Some small local workflows at low resolution. | Large checkpoints, batch runs, training, high-resolution generation. |
| 32 GB RAM, 8-12 GB VRAM | More practical local diffusion and node workflows. | Assuming every model fits; license-blind downloads. |
| Cloud GPU or server GPU | Advanced generation, batch jobs, experiments. | Unbounded spend, private data uploads without policy review. |

## Beginner Recommendation

For public workshops or beginner docs, start with browser/API tools. Move to
local workflows only after learners understand model licenses, GPU memory,
storage, and safety boundaries.

## GitHub Actions Boundary

GitHub Actions may validate Markdown, run Python tests, and build release
packages. They must not run heavy GPU image generation, download model weights,
or train/fine-tune models.

## Checklist

- [ ] Does the guide state hardware assumptions?
- [ ] Does it separate API, lightweight local, advanced local, and cloud paths?
- [ ] Does it warn entry-level hardware users?
- [ ] Does it avoid local training as a beginner default?
- [ ] Does it tell readers to verify current tool requirements?

## Recommendation Language

Use careful language because hardware requirements change by model and tool.

Preferred:

```text
For beginner readers, prefer browser/API workflows. Local generation becomes
practical only when the user has enough VRAM, disk, driver support, and time to
debug the selected tool. Verify exact requirements in the tool's official docs.
```

Avoid:

```text
Any laptop can run this model.
```

Also avoid exact performance promises unless measured in the current setup and
documented with model, resolution, batch size, precision, driver, and hardware.

## Cost And Privacy Tradeoffs

| Path | Cost risk | Privacy risk | Best fit |
| --- | --- | --- | --- |
| Browser/API | Subscription or usage fees. | Prompts/images may be processed by provider. | Beginners, workshops, quick drafts. |
| Lightweight local | Time and storage. | Data stays local if no external calls occur. | Learning prompt structure and small experiments. |
| Advanced local GPU | Hardware cost, disk, power, maintenance. | Local control, but outputs and model licenses still matter. | Advanced users with verified setup. |
| Cloud GPU | Usage fees can grow quickly. | Private data may leave local machine. | Batch jobs or experiments with clear budget and policy. |

## Hardware Disclosure Template

When publishing a local workflow, include:

```text
Tested on:
- Operating system:
- CPU/RAM:
- GPU/VRAM:
- Driver/runtime:
- Tool version:
- Model/checkpoint:
- Resolution and batch size:
- Approximate generation time:
- Known failures:
```

If those fields are not known, do not present the workflow as verified.

## CI And Repository Boundary

This repository's CI should stay lightweight:

- Markdown checks.
- Standard-library Python tests.
- Package manifest creation.
- Static safety checks.

It should not:

- Download model weights.
- Run GPU jobs.
- Generate images.
- Train or fine-tune models.
- Upload private prompt or image data.
