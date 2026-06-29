# Image Prompting Patterns

Use these patterns as starting points. Always respect tool policies, licenses,
private data boundaries, and source attribution.

## Base Prompt Template

```text
Subject: [main object or scene].
Purpose: [marketing, documentation, UI mockup, character reference, product shot].
Composition: [camera angle], [framing], [background].
Lighting: [soft studio, daylight, dramatic rim light].
Style: [realistic, editorial, 3D render, clean vector-like illustration].
Constraints: no private logos, no private people, no watermarks, no unsafe content.
Output: [aspect ratio], [resolution if supported], [file type if supported].
```

## Text Rendering

```text
Create a clean poster with exactly this text: "[short text]".
Use large readable letters, high contrast, simple background.
Do not add extra words, misspellings, signatures, or watermarks.
```

Keep text short. If exact text is critical, plan manual review and correction.

## Marketing Or Product Shots

```text
Studio product shot of [product], three-quarter view, neutral background,
softbox lighting, realistic materials, crisp edges, no brand marks unless
provided and licensed, no extra labels.
```

## Character Consistency

```text
Character reference sheet for [character description].
Show front, side, and three-quarter views.
Keep clothing, colors, face shape, and accessories consistent.
No real person likeness unless permission is explicit.
```

## 3D Asset Reference Prompting

```text
Create a 3D asset reference for [object].
Orthographic front, side, and top views.
Show simple material callouts and scale cues.
Avoid decorative background clutter.
```

## Style Control

- Name visual constraints rather than private artist imitation.
- Use public-safe descriptors such as lighting, medium, era, camera, material,
  and layout.
- Avoid copying living artists' signature styles unless the tool policy and
  source rights allow it.

## Negative Prompting

Use only where the tool supports it:

```text
Negative prompt: extra text, watermark, private logo, unsafe content, distorted
hands, unreadable labels, low-quality artifacts
```

## Evaluation Checklist

- [ ] Does the output match the subject and purpose?
- [ ] Are private data and private likenesses absent?
- [ ] Is text readable and exact?
- [ ] Are licenses and source status documented?
- [ ] Is the hardware/API requirement clear?
