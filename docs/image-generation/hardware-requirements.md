# Image Generation Hardware Requirements

Hardware requirements vary by model, resolution, batch size, precision, and
tooling. Treat exact requirements as official-doc verification items.

## Generic Hardware Tiers

This guide uses generic tier names throughout instead of specific machine
specs, because exact VRAM/RAM numbers that work for one model version can be
wrong for the next one:

- **Browser/API tier** — no local GPU needed at all; generation happens on the
  provider's infrastructure.
- **Entry consumer GPU tier** — a laptop or desktop with integrated graphics or
  a low-VRAM discrete GPU. Fine for browser/API use and light local
  experiments; not a good fit for heavy local diffusion.
- **Advanced GPU tier** — a desktop-class discrete GPU with enough VRAM to run
  common local diffusion checkpoints at reasonable resolution. Users here are
  expected to understand model licenses and troubleshooting.
- **Cloud/rented GPU tier** — a rented cloud instance or server GPU used for
  batch jobs, training, or heavy generation, with an explicit budget and data
  policy.

## Practical Table

| Hardware | Realistic use | Avoid |
| --- | --- | --- |
| Browser/API tier (no local GPU) | Hosted browser/API tools; prompt writing practice. | Any local model download or local generation. |
| Entry consumer GPU tier | Browser/API tools; lightweight local experiments; prompt writing practice. | Heavy diffusion, training, fine-tuning, vLLM, SGLang, large local serving. |
| Entry consumer GPU tier, upper end | Some small local workflows at low resolution. | Large checkpoints, batch runs, training, high-resolution generation. |
| Advanced GPU tier | More practical local diffusion and node workflows. | Assuming every model fits; license-blind downloads. |
| Cloud/rented GPU tier | Advanced generation, batch jobs, experiments. | Unbounded spend, private data uploads without policy review. |

## Decision Table: Goal To Tier

Match your actual goal to a tier before picking a tool. This is the table to
use before opening any local install docs.

| Goal | Recommended tier | Realistic tradeoffs |
| --- | --- | --- |
| Learn prompt writing, no setup wanted | Browser/API tier | Usage limits or subscription cost; prompts/images may be processed by the provider. |
| Occasional drafts for docs, blog posts, mockups | Browser/API tier | Same as above; fastest path to a usable image with zero install risk. |
| Curious about local generation, has an entry laptop | Entry consumer GPU tier, lightweight local only | Slow generation, small models only, frequent out-of-memory errors if you push resolution or model size. |
| Wants repeatable local workflows, batch generation, or custom LoRAs | Advanced GPU tier | Real setup time, disk space for models, license review per model/LoRA, driver troubleshooting. |
| Needs high-volume generation or training/fine-tuning | Cloud/rented GPU tier | Real money cost that scales with usage; private data leaves the local machine unless the provider's policy is reviewed first. |
| Building a workshop or beginner curriculum | Browser/API tier as the taught default | Local tiers can be an optional "advanced" appendix, never the main path. |

## Troubleshooting Table

Generic symptom-to-cause-to-fix guidance. Exact error text and settings names
vary by tool; verify in that tool's docs.

| Symptom | Likely cause | What to try |
| --- | --- | --- |
| Out-of-memory / CUDA out of memory error | Resolution, batch size, or model size exceeds available VRAM. | Lower resolution or batch size, switch to a smaller/quantized model, close other GPU-using apps, or move to browser/API or cloud/rented GPU tier. |
| Generation is extremely slow (minutes per image on what should be fast) | Running on CPU instead of GPU, or GPU acceleration isn't being used by the tool. | Confirm the tool is actually using the GPU (check its logs/settings), confirm drivers are installed correctly, or accept that entry consumer GPU tier means CPU-speed fallback is normal and not a beginner default. |
| Tool won't detect the GPU at all | Driver mismatch, missing runtime, or unsupported GPU/OS combination for that tool. | Reinstall or update the GPU driver from the official vendor source, confirm the tool's stated supported OS/driver versions, and check the tool's own troubleshooting docs before searching random forum fixes. |
| Install fails partway through | Python/Node version mismatch, missing build tools, or insufficient disk space. | Check the tool's stated required runtime versions, verify free disk space, and avoid unofficial "fixed" installers from third-party sites. |
| Output quality is much worse than examples online | Different model/checkpoint version, wrong resolution, or missing required settings (sampler, steps, guidance scale — see [diffusion-models.md](diffusion-models.md)). | Confirm which exact model version the example used, and check the tool's docs for the settings that example relied on. |
| Generation crashes the whole system or app | VRAM exhaustion escalating to a driver crash, or a corrupted model file. | Lower resolution/batch further, re-download the model file from the official source, and update drivers before retrying. |

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
| Browser/API tier | Subscription or usage fees. | Prompts/images may be processed by provider. | Beginners, workshops, quick drafts. |
| Entry consumer GPU tier, lightweight local | Time and storage. | Data stays local if no external calls occur. | Learning prompt structure and small experiments. |
| Advanced GPU tier | Hardware cost, disk, power, maintenance. | Local control, but outputs and model licenses still matter. | Advanced users with verified setup. |
| Cloud/rented GPU tier | Usage fees can grow quickly. | Private data may leave local machine. | Batch jobs or experiments with clear budget and policy. |

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
