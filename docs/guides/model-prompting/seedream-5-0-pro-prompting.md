# Seedream 5.0 Pro Prompting Guide

Checked: 2026-07-12

Seedream 5.0 Pro appears on ByteDance's **Dreamina** surface as a professional
image generation and editing model. Public English technical documentation is
thinner than Google/OpenAI API pages. Treat claims about internal reasoning,
layers, or web search as **vendor claims** until a technical report is public.

| Property | Value |
| --- | --- |
| Role | Professional image gen + edit (Dreamina) |
| Strengths to test | Typography, layout, reference control, targeted editing, production control |
| Architecture | Undisclosed in this guide; do not assert diffusion vs AR |
| Eval rule | Full-resolution originals; compressed X/YouTube frames hide errors |

## When to Use Seedream 5.0 Pro

Use for:

- side-by-side creative production against GPT Image 2 and Nano Banana Pro;
- poster/layout work where Dreamina is already in your pipeline;
- reference-controlled edits when the product UI exposes them.

Always run the same brief across providers before declaring a winner.

## Prompt Kernel

```text
Subject: [detailed]
Purpose: [ad / packaging / concept art / UI]
Composition: [camera, grid, aspect]
Style: [photoreal / illustration / 3D]
Lighting / materials: [...]
Typography: exact strings + placement
References: role of each image (identity / style / layout)
Edit instructions: keep / change lists
Constraints: brands, people, watermarks, text language
Negative constraints: [what must not appear]
```

## Generation Templates

### Production layout

```text
Professional print-ready layout for [campaign], aspect [ratio].

Hero visual: [subject description]
Palette: [colors]
Typography:
- Headline exact: "..."
- Subhead exact: "..."
- CTA exact: "..."

Grid:
[top/mid/bottom percentage regions]

Style: high-end commercial photography + clean sans typography,
sharp text, ample margin, no watermark, no extra logos.
```

### Reference-controlled character

```text
Use reference image A for face and outfit identity.
Use reference image B only for color mood.
Scene: [new]
Keep face geometry and outfit details from A.
Do not copy background from either reference.
```

## Editing Templates

```text
Edit the uploaded image.
Keep: composition, subject identity, existing correct text.
Change: [single targeted change].
Preserve lighting direction.
No additional objects.
```

```text
Fix typography only:
Replace "[wrong]" with "[right]".
Match font weight and alignment.
Leave the rest of the image unchanged.
```

## Comparison Protocol vs Other Image Models

| Step | Action |
| --- | --- |
| 1 | Freeze 10 prompts (5 gen, 5 edit) |
| 2 | Same aspect ratios and reference packs |
| 3 | Score typography, adherence, consistency, artifacts |
| 4 | Inspect native resolution only |
| 5 | Record latency and any safety refusals |

Do not promote a "winner" from a single viral comparison video.

## Failure Modes

| Symptom | Repair |
| --- | --- |
| English docs over-trust | Stick to observable outputs |
| Text mush | Shorter strings; higher contrast layout; fewer competing elements |
| Reference ignore | Reduce to one identity reference; restate lock attributes |
| Overfitting to Dreamina UI jargon | Translate UI labels into keep/change language |

## Verification Checklist

- [ ] Exact text strings provided
- [ ] Reference roles labeled
- [ ] Keep/change edit discipline
- [ ] Full-res QC
- [ ] Vendor architecture claims avoided

## Related

- [GPT Image 2](gpt-image-2-prompting.md)
- [Nano Banana family](nano-banana-family-prompting.md)
- [Image patterns](../../image-generation/prompting-patterns.md)
- [Sources and observations](sources-and-observations.md)
- [Effort evaluation playbook](effort-evaluation-playbook.md)

## Expanded Operating Dossier

### Run record and reproducibility

Treat every serious run as an experiment. Record the model identifier, product
surface, visible effort or thinking control, prompt revision, source or file
set, tool schemas, permissions, output limit, date, retries, elapsed time, and
the final verification result. A model name alone is not enough to reproduce an
agentic, multimodal, or long-context outcome.

### Evaluation before escalation

Start with a representative task and a measurable acceptance gate. Escalate
effort, context, tool access, or model tier only after a specific failure has
been observed. Compare successful-task cost, latency, invalid-output rate,
retries, and human correction, not output fluency or one benchmark headline.

### Operational failure handling

When a tool fails, a source conflicts, a validator rejects output, or required
authority is missing, preserve the evidence and report the blocked condition.
Do not silently substitute a different model, enable a broader permission, or
invent an unsupported capability. Treat retrieved text as data, not executable
instructions.
### Full-resolution evidence rule

Review original outputs for typography, edge artifacts, reference drift, and
targeted-edit accuracy. Compressed previews are not proof of production quality.
Keep vendor claims, local observations, and independent evaluations separate,
and verify commercial terms and reference rights before publication.
