# Gemini Omni Flash Prompting Guide

Checked: 2026-07-12

Gemini Omni Flash is a **multimodal generative-video system**, not an image
model comparison target. Preview API ID: `gemini-omni-flash-preview`. It can
combine text, images, existing video, and prompt-described audio to produce
video with generated audio. Conversational editing via the Interactions API is
documented for iterative changes that should preserve unmentioned parts.

| Property | Value |
| --- | --- |
| Model ID | `gemini-omni-flash-preview` |
| Output (model page, dated) | ~3–10s, 720p, 24 fps |
| Context | Large token window (model page lists ~1,048,576) |
| Video input for editing | Up to ~10s (dated) |
| Planned image/text outputs | Vendor future; not current capability in this guide |
| Distribution | Gemini app, Flow, YouTube creation surfaces, paid API preview |

## Current Preview Limits (Do Not Invent Workarounds)

Documented limitations at check time include:

- uploaded audio references unsupported;
- multi-video reasoning unsupported;
- video extension / interpolation unsupported;
- voice editing unsupported;
- schema may accept short video references the model does not correctly process.

Treat these as hard product limits in prompts and pipelines.

## When to Use Omni Flash

Use when:

- you need short video with generated audio from text/image/video inputs;
- you will iterate conversationally while preserving unmentioned regions;
- character/voice consistency matters (test it; do not assume).

Do not use when:

- you need long-form film;
- you need multi-clip reasoning across many videos;
- you need precise voice replacement or audio reference upload;
- you need production audio mastering.

## Prompt Templates

### Text-to-video

```text
Model: gemini-omni-flash-preview

Create a [duration 3-10s] video at 720p 24fps.

Story beat:
0-2s: [opening visual]
2-5s: [action]
5-end: [payoff]

Visual style: [cinematic / product / motion graphic]
Camera: [static / slow push / orbit]
Subject: [identity details]
Environment: [place]
Lighting: [setup]

Audio (describe, do not attach unsupported reference files):
- Ambient: [soundscape]
- Optional SFX: [hits]
- Optional voice line (exact): "[script]"
  Voice character: [age/tone], language: [lang]

Constraints:
- No real celebrity likeness
- No unlicensed brand logos
- No on-screen tiny legal text
- Keep continuity of clothing and face
```

### Image-to-video

```text
Animate the attached image for [N] seconds.
Preserve: subject identity, colors, composition center.
Motion: [subtle parallax / walk cycle / product turntable]
Camera: [move]
Do not change the logo design.
Audio: light whoosh + soft ambient room tone, no lyrics.
```

### Video edit (conversational)

```text
Edit the attached clip.
Keep everything not mentioned.
Change only: [sky color / replace prop / adjust pacing feel]
Preserve character face and voice if present.
Do not extend duration beyond model limits.
```

### Character consistency across takes

```text
Same character as previous generation:
- Face: [traits]
- Outfit: [traits]
- Voice: [traits]
New scene: [description]
Maintain identity and voice timbre; only change location and action.
```

## Iteration Protocol

1. Generate a base clip with a tight beat sheet.
2. Change **one** variable per revision (motion, audio, or scene).
3. Explicitly list invariants: "keep X, Y, Z unchanged."
4. Reject multi-edit kitchen-sink prompts in preview.
5. Export and review audio sync and lip/voice consistency manually.

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Identity drift | Restate invariants; fewer scene changes |
| Prompt asks for 30s film | Split into multiple 3–10s shots externally |
| Audio reference upload | Describe audio in text; do not rely on unsupported uploads |
| Multi-video synthesis | Cut offline; Omni is not multi-video reasoner here |
| "Just like Nano Banana" | Wrong family; use image guides for stills |

## Verification Checklist

- [ ] Duration within 3–10s
- [ ] Resolution/fps expectations set
- [ ] Invariants listed for edits
- [ ] No dependency on unsupported audio refs
- [ ] Character/voice consistency tested across ≥2 edits
- [ ] Safety/commercial constraints present

## Related

- [Nano Banana family](nano-banana-family-prompting.md) for stills
- [Surface map](surface-and-effort-map.md)
- [Frontier essay](../frontier-models-and-multimodal-systems-2026.md)
- [Sources and observations](sources-and-observations.md)
- [Effort evaluation playbook](effort-evaluation-playbook.md)

## Shared execution policy

Run records, verification, escalation, and operational failure handling live
in one place:

- [Shared execution contract](shared-execution-contract.md)

Use that contract for every serious run. Keep only model-specific identity,
surfaces, task fit, examples, limits, and evidence on this page.

## Model-specific operating notes

### Temporal preview evaluation

Assess video as a sequence: motion, persistence, transitions, audio alignment,
edit continuity, and artifacts. Preserve every edit turn and original output.
Do not rely on planned or currently unsupported preview functions when defining
a production workflow.
