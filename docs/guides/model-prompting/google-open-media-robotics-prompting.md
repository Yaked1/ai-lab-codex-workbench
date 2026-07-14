# Google Open, Media, and Robotics Prompting Guide

Checked: 2026-07-12

## What These Systems Are and Where They Are Available

Gemma 4 and DiffusionGemma are open-weight model families; Veo 3.1 Lite, Lyria
3, and Gemini Robotics-ER 1.6 are current preview API systems. Gemini 3.5 Pro
is a watchlist item only: Google says "coming soon" but the checked sources do
not expose an identifier, availability, or access instructions. No prompting
template is supplied for it.

## Task Selection and Product Boundaries

| System | Appropriate task | Boundary to keep explicit |
| --- | --- | --- |
| Gemma 4 / DiffusionGemma | Local or controlled open-weight deployment | Hardware, quantization, tuning, safety filters, and tool support are deployment choices |
| Veo 3.1 Lite Preview | High-volume video generation and editing trials | Preview limits apply; no 4K or Extension in the reviewed page |
| Lyria 3 Preview | Music clips and longer prompted songs | Respect commercial terms, artist-style policy, and audio-format checks |
| Robotics-ER 1.6 Preview | Embodied reasoning, visual/spatial planning | It returns reasoning output; physical control and safety stay in the robot stack |

## Recommended Prompt Structures

```text
Video brief: [story, subject, duration, framing, motion, audio]
References: [rights-cleared images only]
Continuity: [facts and visual elements that must persist]
Verification: inspect temporal consistency, audio sync, edits, and provenance
```

```text
Music brief: [original concept, genre descriptors, instrumentation, structure,
vocal/instrumental choice, duration]. Do not request a living artist's exact
style or provide copyrighted lyrics. Verify structure, intelligibility, and
prompt adherence in the generated audio.
```

```text
Robotics reasoning task: Given [image/video/audio] and [goal], identify objects,
spatial constraints, uncertainty, and a high-level plan. Return structured text.
Do not command actuators. Verify in simulation, then through supervised physical
tests with an independent safety controller.
```

## Thinking, Context, and Verification

Gemma 4 and DiffusionGemma document configurable thinking modes, but configure
only the control supported by the chosen runtime. The current Robotics-ER page
documents a thinking budget and tool paths; these do not mean safe autonomy.
For media, test original outputs for prompt adherence, temporal or musical
continuity, latency, cost, provenance, and rights. For robotics, record inputs,
model version, tool calls, simulation outcome, operator approval, and failures.

## Failure Modes and Unsupported Uses

Do not treat an open weight as an API version of Gemini, infer a model ID, or
claim that a preview is production-ready. The current Lyria sources conflict on
44.1 kHz versus 48 kHz output; verify the live response format. Robotics-ER
does not establish direct low-level control, safety-critical suitability, or
real-world reliability without independent hardware validation.

## Sources

- [Gemma 4 overview](https://ai.google.dev/gemma/docs/core)
- [DiffusionGemma model card](https://ai.google.dev/gemma/docs/diffusiongemma/model_card)
- [Veo 3.1 Lite Preview](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview)
- [Lyria 3 music generation](https://ai.google.dev/gemini-api/docs/music-generation)
- [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview)
- [Evidence ledger](sources-and-observations.md)

## Shared execution policy

Run records, verification, escalation, and operational failure handling live
in one place:

- [Shared execution contract](shared-execution-contract.md)

Use that contract for every serious run. Keep only model-specific identity,
surfaces, task fit, examples, limits, and evidence on this page.

## Model-specific operating notes

### Open, media, and robotics boundaries

Open weights make the builder responsible for runtime, quantization, safety, and
data controls. Preview media systems need original-output review and rights
checks. Robotics-ER produces high-level reasoning output; an independent safety
controller, simulation, operator approval, and staged trials remain mandatory.
