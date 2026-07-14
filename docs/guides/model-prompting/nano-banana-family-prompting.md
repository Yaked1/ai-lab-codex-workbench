# Nano Banana Family Prompting Guide

Checked: 2026-07-12

Google's consumer names map to Gemini image model IDs. **Nano Banana 2 is not
Gemini 3 Pro Image.** Nano Banana Pro **is** Gemini 3 Pro Image.

| Product name | Model ID | Role |
| --- | --- | --- |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | Fastest/cheapest; high-volume drafts |
| Nano Banana 2 | `gemini-3.1-flash-image` | General balance: quality, speed, 4K, editing |
| Nano Banana Pro | `gemini-3-pro-image` | Highest control, world knowledge, localization, professional use |
| Original Nano Banana (legacy) | `gemini-2.5-flash-image` | Google recommends replacing |

Thinking and search grounding (where documented) change latency, cost, and
outputs. Record them in every test log.

## Which Model to Pick

| Need | Model | Prompt emphasis |
| --- | --- | --- |
| Brainstorm 50 variants fast | 2 Lite | Short subject + style; few references |
| Default production stills / edits | Nano Banana 2 | Full kernel; up to 4K; moderate refs |
| Complex layouts, localization, max control | Nano Banana Pro | Exact text, layout grid, cultural/locale notes |
| Many sequential edit steps | 2 or Pro | Lite is not optimized for long edit chains |

## Shared Prompt Kernel

```text
Subject: ...
Purpose: ...
Composition / aspect: ...
Style / lighting: ...
Exact on-image text: "..."
Locale / language of text: ...
References: [how to use each attached image]
Constraints: no watermarks, no unlicensed brands, ...
Resolution target: [e.g. 1K/2K/4K if offered]
Thinking: on/off (if available)
Search grounding: on/off (if available) — only when current facts are required
```

## Nano Banana 2 Lite

**Vendor positioning:** iteration, brainstorming, high-volume; ~four-second
generation target in launch material. **Not optimized** for many reference
images or long sequential editing.

```text
Model: Nano Banana 2 Lite

Quick concept board for [product].
Style: [3 adjectives]
Background: simple
No fine print, no tiny UI text, no multi-panel complexity.
Generate a bold single-subject composition, aspect [ratio].
```

**Anti-pattern:** 6 reference images + 4 sequential edits + dense typography.

## Nano Banana 2 (Gemini 3.1 Flash Image)

**General-purpose path:** fast generation, search-grounded current knowledge
(when enabled), text rendering, subject consistency, editing, references, up
to 4K.

```text
Model: Nano Banana 2

Create a 4K marketing image of [subject].
Composition: [rule of thirds / centered / wide]
Lighting: [setup]
On-image text (exact): "[headline]"
Secondary text: "[sub]"
Keep subject consistent with reference image 1 (identity lock).
Use search grounding only if you need a current public landmark appearance;
otherwise rely on the prompt alone.
No logos other than the fictional mark described as [description].
```

### Editing with 2

```text
Edit image:
Keep: identity, pose, camera
Change: background to [new], color of [object] to [color]
Do not change face geometry or clothing logos.
```

## Nano Banana Pro (Gemini 3 Pro Image)

**Professional control path:** world knowledge, localization, typography,
complex layouts, production control. Compare to Banana 2 on the same brief.

```text
Model: Nano Banana Pro

Professional poster for [campaign] in [locale].
Language of all text: [language]
Headline (exact): "..."
Subhead (exact): "..."
Legal line (exact, small): "..."

Layout grid:
- Top 20%: headline
- Middle 55%: hero visual of [subject]
- Bottom 25%: subhead + CTA "[cta]" + legal

Visual requirements:
- High legibility at print and mobile crop
- Cultural appropriateness for [market]
- Color palette: [hex or named]
- No real celebrity likeness

References:
- Image A: product packshot (geometry lock)
- Image B: mood only (do not copy composition)
```

### Localization prompt pattern

```text
Same layout as the attached English master.
Replace text with the following [language] strings exactly:
Title: "..."
CTA: "..."
Keep visual hierarchy, spacing, and brand colors identical.
Do not translate logos that must remain in English: [list].
```

## Thinking and Search Controls

| Control | When to enable | Prompt note |
| --- | --- | --- |
| Thinking | Complex layouts, multi-constraint scenes | Still specify layout explicitly |
| Search grounding | Current public knowledge (events, places) | "Ground only for X; do not invent private data" |

Always log:

```text
model_id, thinking, search, resolution, reference_count, latency, notes
```

## Side-by-Side Eval Protocol

Use identical prompts, aspect ratios, references, and human rubric across Lite,
2, Pro, GPT Image 2, and Seedream:

1. Prompt adherence
2. Typography
3. Reference consistency
4. Layout complexity success
5. Latency / cost
6. Editability over 3 sequential revisions

## Failure Modes

| Symptom | Likely model mismatch | Repair |
| --- | --- | --- |
| Soft tiny text | Lite or weak prompt | Pro + exact strings + simpler layout |
| Reference collapse | Too many refs on Lite | Fewer refs; move to 2/Pro |
| Wrong locale text | Missing exact strings | Provide final copy, not "translate creatively" |
| Stale landmark | Search off | Enable grounding only for that element |
| Pro overkill cost | Simple hero shot | Banana 2 or Lite |

## Verification Checklist

- [ ] Correct model ID selected (Pro vs 2 vs Lite)
- [ ] Thinking/search settings logged when used
- [ ] Exact localized strings provided for text-heavy work
- [ ] Lite not used for long multi-reference edit chains
- [ ] Side-by-side eval uses full-resolution outputs

## Related

- [GPT Image 2](gpt-image-2-prompting.md)
- [Seedream 5.0 Pro](seedream-5-0-pro-prompting.md)
- [Image patterns](../../image-generation/prompting-patterns.md)
- [Surface map](surface-and-effort-map.md)
- [Sources and observations](sources-and-observations.md)
- [Effort evaluation playbook](effort-evaluation-playbook.md)

## Shared execution policy

Run records, verification, escalation, and operational failure handling live
in one place:

- [Shared execution contract](shared-execution-contract.md)

Use that contract for every serious run. Keep only model-specific identity,
surfaces, task fit, examples, limits, and evidence on this page.

## Model-specific operating notes

### Family comparison protocol

Compare Lite, general-purpose, and Pro paths using the same references, aspect
ratio, required text, grounding configuration, thinking setting, and review
rubric. Select by the output contract, not the family label. Record any enabled
search or thinking feature because it changes cost and latency.
