# Image Prompting Engine

Image prompting is visual specification. The goal is to describe what should be visible, how it should be arranged, and how success should be checked.

## Universal Image Prompt Fields

| Field | Purpose |
| --- | --- |
| Subject | Main object, person, creature, scene, interface, or symbol. |
| Composition | Framing, camera angle, perspective, foreground, middle ground, background. |
| Spatial relations | Exact placement: left, right, above, behind, separated, centered. |
| Medium | Photograph, cinematic still, oil painting, ink drawing, 3D render, product shot. |
| Lighting | Source, direction, contrast, color temperature, atmosphere. |
| Materials | Texture, surface, fabric, metal, glass, stone, water, paper. |
| Style | Genre, era, realism level, art direction. |
| Constraints | Object count, anatomy, text rules, visual artifacts to avoid. |
| Use case | Poster, concept art, UI asset, 3D reference, storyboard, product mockup. |

Image prompts are specifications for visual output. They should make the
desired image inspectable: a reviewer should be able to compare the output to
the subject list, layout, lighting, style, and constraints.

## Diffusion Driver

Diffusion models usually respond strongly to visual descriptors, style anchors, reference images, masks, and control signals.

```text
Subject:
[Main visual content]

Scene:
[Environment and composition]

Style:
[Medium, genre, visual quality]

Lighting:
[Light source, mood, color, contrast]

Camera:
[Lens, distance, perspective, depth of field]

Details:
[Materials, textures, small features]

Avoid:
[Unwanted artifacts, wrong anatomy, unwanted text, watermark, distortion]

Controls:
[Aspect ratio, seed, steps, guidance, reference image, mask, pose/depth/layout control if supported]
```

### Diffusion Rules

- Put the main subject early.
- Separate content from style.
- Use avoidance terms sparingly.
- Use references or controls for strict layout.
- Change one variable per iteration.
- Save seeds and settings.
- Avoid adjective soup.

Diffusion systems often respond strongly to style, medium, and aesthetic
phrasing, but they can struggle with exact counts, spatial logic, and text.
Use diffusion prompts when visual texture and style matter more than strict
symbolic layout.

Diffusion review questions:

- Are the main subject and style clear?
- Are negative constraints specific and limited?
- Are reference images described by role?
- Are exact counts avoided unless the model supports them?
- Is text rendering avoided or isolated when unreliable?

## Autoregressive Image Driver

Autoregressive image systems benefit from ordered structure, global layout, entity inventory, and explicit spatial constraints.

```text
Goal:
Generate [image type] for [use case].

Global layout:
[Overall composition before details.]

Entity inventory:
- Entity 1: [appearance, position, role]
- Entity 2: [appearance, position, role]

Spatial constraints:
[Exact relationships and counts.]

Rendering priorities:
[What must be coherent first.]

Style and finish:
[Medium, lighting, palette, texture.]

Avoid:
[Visual artifacts or unwanted elements.]
```

### Autoregressive Rules

- State layout before style.
- Count entities explicitly.
- Define relationships between objects.
- Prioritize constraints.
- Keep the visual plan concise.
- Avoid late contradictions.

Autoregressive image systems often follow ordered layout descriptions better
than tag piles. Put the most important spatial commitments early.

Layout pattern:

```text
Canvas:
- aspect ratio:
- viewpoint:
- foreground:
- midground:
- background:

Entities:
- entity 1:
- entity 2:
- entity 3:

Relationships:
- entity 1 is left of entity 2
- entity 3 is behind entity 1
```

Avoid overloading the prompt with twenty equally important constraints. If
everything is critical, nothing is prioritized.

## Reasoning-Integrated Image Driver

Use this when the model can plan before generating.

```text
Before generating, internally plan the composition, spatial relationships, lighting, materials, and visual constraints. Do not show the reasoning. Render only the final image.
```

If visible planning is useful:

```text
Use this concise visual plan:
1. Subject
2. Layout
3. Lighting
4. Materials
5. Constraints
Then generate the image from that plan.
```

Use a reasoning-integrated flow when the user gives messy requirements:

- A product mockup with conflicting layout requests.
- A scene with many entities.
- A brand-safe image with strict exclusions.
- A diagram that must explain a process.
- A revision task where the failure must be diagnosed.

The reasoning step should produce a clean final prompt, not a long explanation
embedded into the image prompt.

## Image Revision Driver

```text
Revise the provided image.

Keep stable:
- [Identity, pose, layout, lighting, background, object]

Adjust:
- [Specific target]

Keep unchanged:
- [Protected elements]

Output style:
- [Realistic/cartoon/product/etc.]

Quality check:
- The revised part should match perspective, lighting, scale, and texture.
```

Revision prompts need preservation rules. Name what should stay fixed:

- Subject identity.
- Pose.
- Camera angle.
- Background.
- Color palette.
- Text content.
- Brand marks when allowed.
- Aspect ratio.

Then name the change. "Make it better" is not a revision request. "Increase
contrast on the foreground subject while preserving the background and crop" is
a revision request.

## Image Prompt Failure Modes

| Failure | Cause | Fix |
| --- | --- | --- |
| Wrong count | Object count hidden in prose | Use entity inventory. |
| Bad layout | Style described but geometry vague | Add global composition and spatial relations. |
| Odd anatomy | Too many competing pose/style instructions | Prioritize anatomy and simplify. |
| Text artifacts | Model weak at typography | Ask for no visible text or use post-processing. |
| Overstyled output | Style overwhelms subject | Separate content from style and reduce adjectives. |
| Weak revision | Stable/adjust boundaries unclear | Use explicit keep-stable and adjust blocks. |

## Quality Rubric

| Dimension | Pass question |
| --- | --- |
| Subject | Are all required entities present and recognizable? |
| Layout | Are spatial relationships correct enough for the task? |
| Style | Does the output match the requested medium and finish? |
| Lighting | Does lighting support the composition? |
| Constraints | Are forbidden elements absent? |
| Text | If text was requested, is it legible and correct? |
| Safety | Does the prompt avoid private data and disallowed content? |
| Revision | Did the change preserve protected elements? |

## Prompt Debugging Table

| Symptom | Likely issue | Prompt repair |
| --- | --- | --- |
| Main subject missing | Subject buried after style details. | Move subject inventory to the top. |
| Wrong count | Count too complex or low model reliability. | Simplify scene or split into fewer entities. |
| Wrong layout | Spatial relations vague. | Use foreground/midground/background and left/right relationships. |
| Style inconsistent | Multiple style references compete. | Choose one style anchor. |
| Text garbled | Model weak at text rendering. | Avoid text or request simple large text only. |
| Revision changes too much | Preservation rules missing. | Add "do not change" list. |

## Package Guidance

Packaged image prompts should include:

- A reusable field list.
- At least one diffusion pattern.
- At least one autoregressive layout pattern.
- Revision criteria.
- Failure modes.
- Safety reminders.
- Clear distinction between visual style and factual claims.

## Master Image Prompt

```text
Create [image type] of [subject] for [use case].

Composition:
[Camera, framing, spatial layout, foreground/background.]

Entity inventory:
- [Entity]: [appearance, position, count]

Visual details:
[Materials, textures, lighting, atmosphere, color palette.]

Model-family instruction:
[Diffusion: style/avoidance/control settings]
[Autoregressive: layout/entity/spatial priority]
[Reasoning-integrated: internally plan before rendering]

Constraints:
[Artifacts to avoid, text rules, safety limits.]

Quality check:
[What must be coherent in the final image.]
```
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/05-image-prompting-engine.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `05 image prompting engine` state what decision, workflow, or reusable behavior it supports?
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
