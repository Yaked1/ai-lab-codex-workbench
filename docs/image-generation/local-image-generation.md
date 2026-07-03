# Local Image Generation

Local image generation is useful for learning and privacy-sensitive experiments,
but it is easy to over-recommend heavy GPU setups to beginners. The default
path for this repository, and for any beginner-facing guide built from it, is
browser/API-first. Local generation is an optional, advanced tier that a
reader opts into only after understanding the tradeoffs on this page.

## Local Workflow Levels

| Level | Example fit | Beginner guidance |
| --- | --- | --- |
| Lightweight local | Small experiments, prompt syntax practice | Accept slow output and limited quality. |
| Advanced local GPU | Diffusion UIs, node workflows, batch generation | Use only with enough VRAM and license review. |
| Local training/fine-tuning | Custom models, LoRAs, datasets | Not a beginner default. Use cloud or dedicated hardware. |

None of these levels should be the first thing a beginner tries. See
[Hardware requirements](hardware-requirements.md) for the generic tier
language (browser/API tier, entry consumer GPU tier, advanced GPU tier,
cloud/rented GPU tier) used throughout this decision.

## Safety And Setup Checklist

Work through this list, in order, before running any local image-generation
tool. Stop and go back to a browser/API workflow if any item fails.

1. **Disk space.** Diffusion checkpoints commonly run from roughly one to
   several gigabytes each, and a working install (tool, dependencies, model
   files, generated outputs) can multiply that quickly. Confirm free disk
   space before downloading anything, and again before adding a second model
   or LoRA.
2. **Model license review.** Read the model's license and model card before
   downloading. Licenses differ on commercial use, redistribution, output
   ownership, and required attribution. A tool's own license (the UI or
   runtime) is separate from the model file's license — review both.
3. **Source verification.** Download model files only from the official
   repository or a source the model card explicitly names. Do not use random
   mirrors, forum links, or unofficial "faster download" hosts.
4. **Isolate and never commit downloaded model files.** Keep model weights,
   checkpoints, LoRAs, and embeddings in a folder that is never staged into
   Git, separate from source code and docs. Model files do not belong in
   version control: they are large, frequently license-encumbered, and bloat
   every future clone. See the concrete repo pattern below.
5. **Runtime and driver check.** Confirm the tool's stated Python/Node
   version and GPU driver requirements before installing. A version mismatch
   is one of the most common local setup failures (see the troubleshooting
   table below).
6. **Privacy check.** If generating from a reference image, confirm you have
   the right to use it and that the tool does not upload it somewhere
   unexpected. Some "local" UIs still phone home for updates, telemetry, or
   model downloads even though the generation itself runs locally.
7. **Output review plan.** Decide, before generating anything, where outputs
   will live and how you will review them for private data, license issues,
   or unsafe content before sharing or publishing.

### This Repo's Own Pattern, As A Concrete Example

This repository does not host or run image models, but it already treats
"never commit large or generated binaries" as a first-class rule, and that
pattern is worth copying into any local image-generation workspace:

- [`.gitignore`](../../.gitignore) excludes build artifacts, caches, archives
  (`*.zip`, `*.7z`, `*.tar`, `*.tar.gz`), logs, and generated `outputs/`
  directories so they can never be staged by accident.
- [`scripts/repo_health_check.py`](../../scripts/repo_health_check.py) prints
  a warning (its `check_large_files` check) for any tracked file over 5 MB —
  it does not fail the build, but it is a signal worth acting on, since that
  size class is exactly where model checkpoints, safetensors files, GGUF
  files, and generated image batches land.
- [`scripts/safe_autofix.py`](../../scripts/safe_autofix.py) only touches a
  fixed allowlist of text extensions (`.md`, `.txt`, `.py`, `.ps1`, `.yml`,
  `.yaml`, `.json`, `.toml`, plus `.gitignore`/`.editorconfig`), so it never
  reaches into a binary model file even by accident.

Apply the same idea in your own local workspace: add explicit `.gitignore`
entries for model-file extensions such as `*.safetensors`, `*.ckpt`, `*.pt`,
`*.gguf`, and `*.onnx` in any project where you download weights, so a
`git add .` cannot silently stage a multi-gigabyte checkpoint. Verify the
current file formats used by your chosen tool in its official docs, since
new formats appear over time.

## When Local Isn't Worth It Yet

Local generation is frequently the wrong first step. Prefer a browser/API
workflow instead when any of these are true:

- You are still learning prompt structure (subject, composition, lighting,
  style, constraints). Local setup friction has nothing to do with prompt
  quality and will only slow that learning down.
- You are on entry consumer GPU tier hardware, or unsure what GPU you have.
  Expect long installs, slow CPU fallback, and frequent out-of-memory errors.
- You need a single image for a document, mockup, or one-off task. The setup
  cost is not worth it for a single output.
- You have not yet reviewed the target model's license.
- You need results today. Local installs routinely take longer than expected
  the first time, especially with driver or dependency mismatches.
- You are teaching a workshop or writing beginner material. Keep the taught
  default at browser/API tier and mention local setups only as an optional,
  clearly labeled advanced appendix.

If none of those apply, and you have verified advanced GPU tier hardware,
reviewed the model license, and understand the disk and driver requirements,
local generation becomes a reasonable choice. See
[Hardware requirements](hardware-requirements.md) for the full decision table.

## Setup Guidance

Use each tool's official repository and docs. Mark unverified commands as
placeholders:

```powershell
# Placeholder only. Verify official tool docs first.
git clone <official-tool-repository-url>
cd <tool-folder>
<official-install-command>
```

## Failure Modes

- GPU driver mismatch.
- Python or Node version mismatch.
- VRAM too small for the selected model.
- Missing model weights.
- Long install time on entry-level hardware.

## Troubleshooting Table

Generic symptom-to-cause-to-fix guidance. Exact error text, menu names, and
settings vary by tool and version; verify in that tool's own docs before
treating any fix as universal.

| Problem | Likely cause | What to try |
| --- | --- | --- |
| Out-of-memory / CUDA out of memory error | Resolution, batch size, or model size exceeds available VRAM. | Lower resolution or batch size, switch to a smaller/quantized model, close other GPU-using apps, or move to browser/API or cloud/rented GPU tier. |
| Driver won't detect the GPU, or the tool falls back to CPU silently | GPU driver mismatch, missing runtime library, or an unsupported GPU/OS combination for that tool. | Update the GPU driver from the official vendor source, confirm the tool's documented supported OS/driver versions, and check its logs for which device it selected. |
| Generation is painfully slow (minutes per image where it should be seconds) | Running on CPU instead of GPU, or GPU acceleration is present but not enabled by the tool. | Confirm the tool selected the GPU, verify drivers, and otherwise accept CPU-speed generation as normal on entry consumer GPU tier hardware, not a beginner default. |
| Download finishes but the model fails to load, or the file size looks wrong | Corrupted download, interrupted transfer, or a mirror serving a different file. | Re-download from the official source only, compare size/checksum against the model card if published, and delete the partial file instead of trying to repair it. |
| Install fails partway through | Python/Node version mismatch, missing build tools, or insufficient disk space. | Check the tool's stated runtime versions, verify free disk space, and avoid unofficial "fixed" installers from third-party sites. |
| Tool starts but crashes on first generation | Incompatible model/tool version pairing, or a plugin conflict. | Confirm the model matches the tool version, disable extra plugins, and check the tool's issue tracker for the exact error. |
| Output quality is much worse than examples seen online | Different model/checkpoint version, wrong resolution, or missing settings (sampler, steps, guidance scale — see [diffusion-models.md](diffusion-models.md)). | Confirm which model version the example used and check the tool's docs for the settings it depended on. |

## Safer Alternatives

- Browser/API image tools.
- Cloud notebooks with clear cost limits.
- Small public sample prompts without local generation.
- Static guide validation in GitHub Actions instead of generation.

## Local Setup Boundary

Local image generation should be documented as an advanced path unless the
setup has been verified on ordinary hardware. A guide should not imply that a
reader can download any model, run any UI, and get reliable results on an
entry-level laptop. State hardware assumptions as generic tiers (see
[Hardware requirements](hardware-requirements.md)) rather than one exact spec
that may not match the reader's machine, and confirm whether generated
outputs can be used publicly before recommending a setup as ready to follow.

## Local Project Hygiene

Keep local generation artifacts outside the repository unless a public-safe
asset is intentionally committed. Recommended local folders:

```text
image-work/
  prompts/
  outputs/
  rejected/
  notes/
```

Do not commit, in any of these folders or elsewhere: model checkpoints,
LoRAs, embeddings, generated batches, private reference images, prompt
histories containing private text, `.env`/API keys, or tool caches. Document
model licenses separately from UI/tool licenses.

## Beginner Exercise Without Running Models

A beginner can still learn image prompting without local generation.

1. Pick a public-safe use case such as a documentation banner or product draft.
2. Write subject, composition, lighting, style, output, and safety constraints.
3. Add a review checklist.
4. Compare the prompt against `prompting-patterns.md`.
5. Mark the actual generation tool as "browser/API or official docs to verify."

This keeps the lesson focused on prompt quality, not driver installation.

## Failure Recovery

| Failure | Recovery |
| --- | --- |
| Install takes too long | Stop and use browser/API workflow for the learning task. |
| Model file is missing | Do not search random mirrors; use official source or skip. |
| GPU is unsupported | Lower expectations, use hosted workflow, or choose CPU-friendly experiments only. |
| Output contains private reference data | Delete local output and do not commit it. |
| License is unclear | Treat result as non-publishable until reviewed. |
| A model file was accidentally staged in Git | Unstage it, add its extension to `.gitignore`, and confirm `git status` is clean before committing anything else. |

## Where This Fits In The Folder

Start with [Hardware requirements](hardware-requirements.md) to confirm which
tier you are actually on. Read [Diffusion models](diffusion-models.md) for
the local-workflow concepts (samplers, steps, guidance scale, img2img) a
local tool will expose in its UI. Come back to
[prompting-patterns.md](prompting-patterns.md) once the tool is running — the
prompt quality gap matters more than the tool choice.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **image-generation guide** surface. During broad
maintenance, reviewers should treat `docs/image-generation/local-image-generation.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `local image generation` state what decision, workflow, or reusable behavior it supports?
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
