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

## Why Diffusion Prompting Is Not Chat Prompting

A chat prompt asks a language model to reason and respond in words. A diffusion
prompt asks a denoising process to steer, step by step, toward an image that
matches a description. That difference changes how prompts should be written:

| Chat prompting | Diffusion prompting |
| --- | --- |
| Instructions can be long, conversational, and sequential ("first do X, then Y"). | The model reads the whole prompt roughly as one set of visual cues, not a sequence of instructions. |
| The model can ask clarifying questions or refuse. | The model renders its best interpretation every time; there is no clarifying turn inside a single generation. |
| Negation works directly ("do not mention the weather"). | Negation in the *positive* prompt is unreliable — describing what you don't want can still visually cue it. Use a separate negative prompt field when the tool offers one. |
| Word order mostly affects tone. | Word order and emphasis often affect how strongly a concept is rendered; early, clearly-weighted terms tend to dominate. |
| One instruction, one topic, is fine. | Competing visual instructions (two styles, two subjects, conflicting lighting) tend to blend or produce artifacts instead of resolving cleanly. |
| Follow-up messages carry full context. | Editing usually means a new generation (txt2img) or an image-conditioned pass (img2img); the model does not "remember" your last prompt unless the tool explicitly chains state. |

The practical takeaway: write diffusion prompts as a **visual specification**,
not a set of instructions to a reasoning agent. Say what should be visible, not
what should be thought about.

## Positive And Negative Prompts As A Pattern

Most diffusion tools split intent into two channels:

- **Positive prompt** — what should appear: subject, composition, lighting,
  materials, style.
- **Negative prompt** — what should be suppressed, when the tool supports a
  dedicated negative-prompt field.

Treat this as a *pattern* to expect, not a guarantee every tool implements it
the same way. Some tools fold negative terms into a single field with a
separator, some expose a distinct UI field, and some (especially many
API-first products) do not expose negative prompting at all. Verify the
current mechanism in each tool's own docs before relying on it.

```text
Positive prompt:
Subject: [main object, scene, or character].
Composition: [camera angle], [framing], [background], [aspect ratio].
Visual details: [materials], [colors], [lighting], [texture].
Style constraints: [photorealistic, editorial, 3D render, diagrammatic].
Safety constraints: no private logos, no private people, no personal data.

Negative prompt (only if the tool supports it):
[specific artifacts to avoid, e.g. distorted hands, extra limbs, watermark, text]
```

Negative prompting rules of thumb:

- Keep it specific and short. A 40-term negative prompt usually helps less
  than fixing the positive prompt.
- If an artifact keeps appearing, treat it as a signal to revise the positive
  description or reconsider the model/tool, not just to pile on negatives.
- Negative prompts are not a safety mechanism. They reduce visual artifacts;
  they do not reliably block unsafe or private content. Rely on the tool's
  actual content policy for that.

## Weighting Syntax As A Convention, Not A Standard

Many diffusion tools let you emphasize or de-emphasize a term, commonly using
some form of parentheses, numeric weights, or repetition, for example a
pattern shaped like `(term:1.3)` or `((term))` to increase emphasis. Treat
this as **a pattern that recurs across tools**, not as a universal syntax:

- The exact characters, whether weighting is supported at all, and the valid
  numeric range are tool-specific and change between product versions.
- A weighting string that works in one tool can be ignored, rendered as
  literal text, or rejected by another tool.
- Always verify the current weighting syntax in the specific tool's official
  docs before publishing an example that depends on it.

When in doubt, prefer plain, clear language ("a large red umbrella in the
foreground") over relying on emphasis syntax to fix a prompt that is
structurally vague.

## Sampler, Steps, And Guidance Scale — Concepts To Verify Per Tool

These three controls appear across many diffusion tools, but their exact
names, ranges, and defaults vary and change over time. Treat the following as
concepts to look up per tool, not fixed numbers to copy:

| Concept | What it generally controls | Why you can't hardcode a value |
| --- | --- | --- |
| Sampler / scheduler | The denoising algorithm and step pattern used to go from noise to image. | Different samplers trade speed for quality differently, and available samplers vary by tool and model. |
| Steps | How many denoising iterations run. | More steps can improve quality up to a point of diminishing (or negative) returns; the useful range depends on the sampler and model. |
| Guidance scale (sometimes called CFG scale) | How strongly the model is pushed to match the prompt versus generating freely. | Too low can ignore the prompt; too high can over-saturate or distort the image. The useful range is model-specific. |

If you are documenting a specific tool's defaults or ranges for these
settings, mark that section "verify in official docs" rather than asserting a
number that may already be outdated.

## img2img Vs txt2img Framing

- **txt2img** — the model starts from noise and is guided entirely by the text
  prompt (and any weighting/negative prompt). Use this for first drafts and
  for exploring a concept from scratch.
- **img2img** — the model starts from an existing image plus a text prompt,
  and denoises toward something that keeps some structure from the source
  image while moving toward the prompt. Use this for style transfer, targeted
  edits, or when you want to preserve composition while changing texture,
  lighting, or style.

A "denoising strength" or similar parameter usually controls how much of the
source image survives in img2img: low values stay close to the source, high
values behave closer to txt2img. Treat the exact parameter name and scale as
tool-specific; verify before documenting an exact number.

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
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **image-generation guide** surface. During broad
maintenance, reviewers should treat `docs/image-generation/diffusion-models.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `diffusion models` state what decision, workflow, or reusable behavior it supports?
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
