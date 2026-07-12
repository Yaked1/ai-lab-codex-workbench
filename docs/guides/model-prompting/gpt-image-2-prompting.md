# GPT Image 2 Prompting Guide

Checked: 2026-07-12

GPT Image 2 is OpenAI's **flagship image generation and editing model** with
text and image input, image output, flexible sizes, and high-fidelity reference
inputs. Product docs emphasize typography, prompt adherence, precise editing,
and reference consistency. Internal architecture claims (for example "fully
autoregressive reasoning-integrated image model") are **unconfirmed** in the
checked OpenAI docs; prompt for outputs, not for hidden mechanisms.

| Property | Value |
| --- | --- |
| Role | State-of-the-art OpenAI image gen + edit |
| Surfaces | Images API, ChatGPT image tools |
| Inputs | Text, images (references / edit bases) |
| Evaluate | Full-resolution outputs, not compressed social frames |

## Universal Image Prompt Kernel

```text
Subject: [what, how many, exact attributes]
Scene: [place, time, weather, background]
Composition: [camera, framing, focal length feel, aspect ratio]
Style: [medium, finish, color grade]
Lighting: [key, fill, contrast]
Text (if any): [exact string, font style, placement]
References: [what must stay consistent]
Constraints: [no logos, no real people, no watermarks, safety]
Edit ops (if editing): [keep X, change Y only]
Output: [size/aspect, count]
```

## Generation Templates

### Product / marketing

```text
Studio product photograph of [product description], three-quarter view,
seamless light-gray background, softbox key from upper left, gentle fill,
crisp materials, no brand logos unless supplied, no extra labels,
commercial catalog quality, aspect ratio [ratio].
```

### UI / diagram (typography-critical)

```text
Clean UI mockup of [screen purpose].
Layout:
- Header: "[exact title]"
- Primary button: "[exact label]"
- Three cards titled "[A]", "[B]", "[C]"
Style: modern minimal, high contrast text, consistent 8px spacing rhythm,
no lorem typos, no watermark, desktop 16:9.
Text must be sharp and correctly spelled.
```

### Character consistency with references

```text
Using the attached reference image(s) as identity lock:
Generate [scene] with the same character face, hair, outfit colors, and
body proportions. Do not invent a new character. Keep the logo on the
jacket identical. Environment may change to [new scene].
```

## Editing Templates

### Surgical edit

```text
Edit the attached image.
Keep: composition, camera angle, subject identity, lighting direction.
Change only: [single change].
Do not alter text that already exists unless listed.
Do not add new objects.
```

### Text repair

```text
In the attached image, replace the misspelled headline with exactly:
"[correct text]"
Match existing font weight, color, and alignment as closely as possible.
Leave all other pixels unchanged.
```

### Layout expansion

```text
Extend the canvas to [aspect] by continuing the background consistently.
Do not crop the subject. Do not introduce new focal objects.
```

## Prompting by Quality Goal

| Goal | Add to prompt |
| --- | --- |
| Typography | Exact strings, placement, "no typos", "sharp text" |
| Reference fidelity | "identity lock", list invariant attributes |
| Editing precision | Keep/change lists; forbid extras |
| Style control | Medium, lighting, materials; avoid living-artist imitation unless rights allow |
| Safety / commercial | No real brands, no real private people, no watermarks |

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Wrong text spelling | Quote exact string; reduce other instructions |
| Identity drift | Fewer scene changes; restate invariants; attach clearer refs |
| Over-creative edit | "Change only X"; negative constraints |
| Looks good in thumbnail, fails print | Inspect full resolution; check edges and small type |
| Architecture debates in prompts | Irrelevant; prompt for measurable visual outputs |

## Evaluation Rubric

Score each output 1-5 on:

1. Prompt adherence
2. Typography accuracy
3. Reference consistency
4. Edit precision (if editing)
5. Artifacts / edges
6. Commercial safety compliance

Use the same prompts and aspect ratios across providers when comparing to Nano
Banana, Seedream, or Muse Image.

## Verification Checklist

- [ ] Exact text strings quoted when typography matters
- [ ] Keep/change lists present for edits
- [ ] References have identity vs style roles
- [ ] Full-resolution QC completed
- [ ] Safety/commercial constraints present

## Related

- [Image prompting patterns](../../image-generation/prompting-patterns.md)
- [Nano Banana family](nano-banana-family-prompting.md)
- [Seedream 5.0 Pro](seedream-5-0-pro-prompting.md)
- [Surface map](surface-and-effort-map.md)
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
### Image generation versus editing

Evaluate generation and editing separately. For edits, inspect preservation of
unmentioned regions, localized change, reference consistency, and drift across
multiple revisions. Keep full-resolution source and output images; do not infer
undisclosed architecture from interface behavior.
