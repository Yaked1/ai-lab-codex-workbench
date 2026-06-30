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

## Prompt Review Rubric

| Area | Strong prompt | Weak prompt |
| --- | --- | --- |
| Subject | Names the main object, scene, or character clearly. | "Make something cool." |
| Purpose | States why the image exists. | No audience or use case. |
| Composition | Gives angle, framing, background, and aspect ratio. | Leaves layout to chance. |
| Style | Uses public-safe visual descriptors. | Imitates a private/living artist or brand style. |
| Text | Keeps exact text short and reviewable. | Requests long paragraphs in-image. |
| Safety | Excludes private people, logos, account details, and unsafe content. | Allows invented private-looking details. |
| Verification | Says what the human will inspect. | Treats generation as automatically correct. |

## Revision Patterns

Preserve-and-change:

```text
Preserve: [approved subject], [composition], [background], [approved text].
Change only: [specific issue].
Do not add: extra text, logos, signatures, watermarks, private faces, account
details, or unsafe content.
```

Text correction:

```text
Revise only the text area.
Required text: "[exact short text]".
Use large high-contrast letters.
Do not add extra words, subtitles, signatures, or decorative labels.
```

Public-safe brand substitute:

```text
Use a plain unbranded product form with no real logo, no trademark-like mark,
and no private label. Focus on material, shape, lighting, and composition.
```

## Source And Reference Handling

When a prompt uses references, record:

- Who owns the reference.
- Whether it is public or private.
- Whether likeness rights or brand rights apply.
- Whether the tool is allowed to process the reference.
- Whether the generated output can be published.

Do not use private screenshots, private people, school/work documents, account
pages, or proprietary product assets in public examples.

## Failure Modes To Inspect

- Extra fingers, distorted hands, or impossible anatomy.
- Misspelled or extra text.
- Invented logos, labels, signatures, or watermarks.
- Private-looking names, IDs, QR codes, or dashboards.
- Mismatched object details between revisions.
- Background clutter that changes the meaning.
- Style drift away from the requested public-safe visual language.
