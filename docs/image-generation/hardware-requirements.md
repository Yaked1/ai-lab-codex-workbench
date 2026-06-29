# Image Generation Hardware Requirements

Hardware requirements vary by model, resolution, batch size, precision, and
tooling. Treat exact requirements as official-doc verification items.

## Practical Table

| Hardware | Realistic use | Avoid |
| --- | --- | --- |
| 8 GB RAM, low-end NVIDIA MX-class GPU, about 2 GB VRAM | Browser/API tools; lightweight local experiments; prompt writing practice. | Heavy diffusion, training, fine-tuning, vLLM, SGLang, large local serving. |
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
- [ ] Does it warn weak-laptop users?
- [ ] Does it avoid local training as a beginner default?
- [ ] Does it tell readers to verify current tool requirements?
