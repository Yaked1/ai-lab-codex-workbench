# Image Prompting Patterns

Use these patterns as starting points. Always respect tool policies, licenses,
private data boundaries, and source attribution. This guide focuses on
worked, copy-paste prompt examples across subject, composition, style,
lighting, materials, and constraints. For plan-then-generate workflows
(layout-first prompts, reason-then-generate, critique-then-revise), see
[Reasoning-integrated image generation](reasoning-integrated-image-generation.md)
instead.

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

Treat every field as required, not optional. A prompt missing composition or
constraints is the single most common cause of a vague, unusable first draft.

## Worked Examples By Dimension

Each example below isolates one dimension so you can see what a
specification-grade phrase looks like for that dimension, then mix and match
across a real prompt.

| Dimension | Weak | Strong |
| --- | --- | --- |
| Subject | "a coffee mug." | A matte ceramic coffee mug, cylindrical with a slightly flared rim, plain surface with no logo, standing upright, empty (no liquid or steam). |
| Subject | "a person working." | A fictional adult in business-casual clothing, seated at a desk, typing on a laptop, face partially turned away from camera, no visible identifying tattoos, jewelry, or badges. |
| Composition | "nice angle." | Three-quarter view from slightly above eye level, subject centered in the left third of the frame, shallow depth of field with background softly blurred, 4:5 portrait aspect ratio. |
| Composition | "wide shot." | Wide establishing shot, camera at hip height, horizon line at the lower third, subject small within the frame to emphasize scale, 16:9 landscape aspect ratio. |
| Style | "make it look nice." | Clean vector-style illustration, flat color fills, minimal gradients, 2px consistent line weight, limited palette of three colors plus white background. |
| Style | "realistic." | Photorealistic editorial photography style, natural color grading, slight film grain, sharp focus on the subject, comparable to a magazine product feature rather than a snapshot. |
| Lighting | "good lighting." | Soft studio lighting from a large diffused softbox positioned upper-left, gentle fill light from the right to reduce harsh shadows, no visible light source in frame, neutral white balance. |
| Lighting | "dramatic." | Single hard rim light from behind the subject, deep shadow across the front of the face and body, low ambient fill, high contrast between lit edge and shadowed mass. |
| Materials | "metal object." | Brushed aluminum surface with visible fine linear grain, subtle cool reflections, no fingerprints or smudges, matte edges where the surface has been machined. |
| Materials | "fabric." | Heavyweight woven cotton canvas, visible thread texture at close range, matte finish with no sheen, slight natural creasing consistent with folded storage. |
| Constraints | "keep it safe." | No real brand logos or trademarked marks, no real person's likeness, no readable text other than the specified label, no watermark or signature, no private account interfaces, no medical or legal claims. |

## Marketing Or Product Shots

```text
Studio product shot of [product], three-quarter view, neutral background,
softbox lighting, realistic materials, crisp edges, no brand marks unless
provided and licensed, no extra labels.
```

## Character Consistency

```text
Character reference sheet for [character description].
Show front, side, and three-quarter views, same pose scale in each panel.
Keep clothing, colors, face shape, and accessories consistent across panels.
No real person likeness unless permission is explicit.
```

## 3D Asset Reference Prompting

```text
Create a 3D asset reference for [object].
Orthographic front, side, and top views, consistent scale across all three.
Show simple material callouts as plain text and a scale-reference cue.
Avoid decorative background clutter and readable text beyond the callouts.
```

## Style Control

- Name visual constraints rather than private artist imitation.
- Use public-safe descriptors such as lighting, medium, era, camera, material,
  and layout.
- Avoid copying living artists' signature styles unless the tool policy and
  source rights allow it.

## Before -> After: A Full Revision Walkthrough

This walkthrough shows the gap between a vague prompt and a
specification-grade one, and why each addition earns its place.

**Before (vague):**

```text
A cool robot in a city.
```

Why this fails: no composition, no lighting, no material description, no
aspect ratio, no constraints, and no definition of "cool." Every one of
those gaps gets filled by the model guessing, which means two runs of this
same prompt can produce wildly different, unrepeatable results.

**Revision pass 1** adds subject specificity and purpose: a fictional small
maintenance robot, boxy body, two articulated arms, one circular optical
sensor, no real brand marks — built for a documentation blog post about
municipal infrastructure robots, set on a quiet city street at dusk.

**Revision pass 2** adds composition and lighting: three-quarter view,
robot centered in the lower half of the frame, street receding into the
background, 16:9 aspect ratio; warm streetlamp light from upper-right, cool
blue ambient dusk light, soft reflections on wet pavement.

**Revision pass 3** adds materials and style: matte gray-blue painted metal
body with faint scuff marks, no rust, glass lens with a subtle streetlamp
reflection; photorealistic render, shallow depth of field, no lens flare or
motion blur.

**Revision pass 4** adds constraints and a review target, producing the
final, specification-grade prompt:

```text
Subject: a fictional small maintenance robot, boxy body, two articulated
arms, single circular optical sensor, no real brand marks.
Setting: a quiet city street at dusk, wet pavement, no visible people.
Composition: three-quarter view, robot centered in the lower half of the
frame, street receding into the background, 16:9 aspect ratio.
Lighting: warm streetlamp light upper-right, cool blue ambient dusk light,
soft reflections on wet pavement.
Materials: matte gray-blue painted metal body, faint scuff marks, no rust,
glass lens with a subtle streetlamp reflection.
Style: photorealistic render, shallow depth of field, no lens flare or
motion blur.
Constraints: no real brand logos, no readable text anywhere in the frame,
no private people, no license plates, no invented storefront signage.
Review: confirm no invented brand text appears anywhere in the frame, and
that the robot's proportions match the description.
```

What changed and why it matters:

| Pass | Added | Problem it solves |
| --- | --- | --- |
| 1 | Subject specificity, purpose | Removes ambiguity about what "robot" and "cool" mean; gives the model (and the reviewer) a fixed target. |
| 2 | Composition, lighting | Fixes framing and mood instead of leaving them to chance; makes the result reproducible across runs. |
| 3 | Materials, style | Locks down surface detail and rendering approach so revisions don't drift in look. |
| 4 | Constraints, output, review | Makes the prompt checkable — a reviewer now has an explicit list of things to reject the image for, instead of a vague "looks fine" judgment. |

The lesson generalizes: a vague prompt is under-specified across composition,
material, and constraints simultaneously. Fix one dimension at a time if you
are learning, but ship the fully specified version, not the first pass.

## Negative Prompting

Use only where the tool supports it:

```text
Negative prompt: extra text, watermark, private logo, unsafe content, distorted
hands, unreadable labels, low-quality artifacts
```

### Negative-Prompt Patterns Table

Negative prompts suppress recurring artifacts; they are not a substitute for
fixing a vague positive prompt, and they are not a safety mechanism. Verify
whether your tool has a dedicated negative-prompt field at all — some
API-first tools do not expose one (see
[diffusion-models.md](diffusion-models.md)).

| Problem category | Example negative terms | Better fix in the positive prompt |
| --- | --- | --- |
| Anatomy artifacts | extra fingers, extra limbs, distorted hands, malformed face | Name pose and hand visibility explicitly, e.g. "hands relaxed at sides." |
| Unwanted text | watermark, signature, extra text, duplicated caption | State exactly what text should appear, or "no readable text in the image." |
| Brand and logo drift | brand logo, trademark symbol, storefront signage | Add "no real brand marks, generic unbranded packaging." |
| Quality artifacts | low resolution, blurry, jpeg artifacts, oversaturated | Specify style and sharpness directly, e.g. "sharp focus, natural color grading." |
| Composition drift | cropped subject, off-center, cluttered background | Specify framing and background explicitly instead of relying on negatives. |
| Unsafe or private content | private ID, QR code, license plate, real person likeness | Treat as a hard positive-prompt constraint and a rejection criterion on review, not just a negative entry. |
| Style contamination | painterly texture, cartoon style, unwanted sketch lines | State the intended style directly; competing style cues in the positive prompt usually cause this. |

Keep negative prompts specific and short — a 40-term list usually helps less
than fixing the positive prompt. If an artifact keeps appearing, revise the
positive description or reconsider the model/tool rather than piling on more
negatives. Negative prompts are not a safety mechanism: they reduce visual
artifacts, not unsafe or private content — rely on the tool's actual content
policy for that.

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

Worked example: preserve the matte ceramic mug from the Subject row above,
same pose and lighting, and change only its color from white to dark green —
do not add extra text, logos, signatures, or watermarks.

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

When a prompt uses references, record who owns it, whether it is public or
private, whether likeness/brand rights apply, whether the tool may process
it, and whether the output can be published. Do not use private screenshots,
private people, school/work documents, account pages, or proprietary product
assets in public examples.

## Failure Modes To Inspect

Extra fingers or impossible anatomy, misspelled or extra text, invented
logos/labels/signatures/watermarks, private-looking names/IDs/QR
codes/dashboards, mismatched details between revisions, background clutter
that changes meaning, and style drift away from the requested public-safe
visual language.

## Where This Fits In The Folder

See [Diffusion models](diffusion-models.md) for why prompts behave like a
visual specification rather than a conversation, [Reasoning-integrated image
generation](reasoning-integrated-image-generation.md) for layout-first and
plan-then-generate structures, and [Local image
generation](local-image-generation.md) for deciding whether a local tool is
worth trying before writing any of these prompts.
