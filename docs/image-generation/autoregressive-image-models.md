# Autoregressive Image Models

Autoregressive image systems generate or refine visual output through token-like
steps in a multimodal model stack. Many current user-facing systems are accessed
through browser or API products rather than local installs.

## Beginner Fit

High when used through a browser or API. Low when self-hosting is required.

## Public-Safe Use Cases

- Marketing draft images.
- Product-shot ideation.
- Blog illustrations.
- UI mood references.
- Text rendering experiments when the provider supports it.

## Setup Guidance

Use the provider's official browser or API documentation. Do not invent install
commands. If a local setup is not verified, write:

```powershell
# Placeholder only. Verify official setup docs before publishing.
<provider-specific-setup-command>
```

## How Autoregressive Prompting Differs From Diffusion Prompting

Diffusion models denoise an entire image roughly all at once, guided by a
prompt read as a whole. Autoregressive and token-based image systems tend to
build the image (or its underlying representation) in an ordered sequence,
often as part of a broader multimodal model that also handles text. That
generation order changes what kind of prompt structure tends to work best:

| Diffusion tendency | Autoregressive/token-based tendency |
| --- | --- |
| Responds strongly to style and mood descriptors. | Responds strongly to explicit structure: ordered lists, named entities, stated positions. |
| Global composition emerges from the whole prompt at once. | Composition benefits from being stated first, before per-entity detail. |
| Exact object counts are often unreliable. | Exact counts and an explicit entity inventory tend to hold up better. |
| Text-in-image rendering is frequently weak. | Text-in-image rendering is often a relative strength, especially for short, exact strings. |
| Spatial relationships ("left of", "behind") are a common failure point. | Spatial relationships expressed as explicit statements are more likely to be honored. |
| Prompt reads well as a mood board. | Prompt reads well as an ordered specification or outline. |

## Prompting Technique: Ordered Composition

State the big picture before the details, and state details in the order you
want them prioritized. An autoregressive system that reads the prompt in
sequence tends to anchor early statements more strongly than late ones.

```text
Global layout: [what's in the frame, overall arrangement, aspect ratio].
Then, in priority order:
1. [Most important element and its position]
2. [Second most important element and its position]
3. [Supporting details, background, texture]
```

Avoid burying the composition inside a paragraph of style adjectives. If the
layout is the thing that must be correct, put it first and phrase it plainly.

## Prompting Technique: Entity Lists

Instead of describing a scene as flowing prose, list each entity that must
appear, with its own appearance, position, and role. This maps well onto how
these systems tend to process structured input, and it makes miscounts easy
to spot and fix.

```text
Entities:
- Entity 1: [appearance], [position], [role in the scene]
- Entity 2: [appearance], [position], [role in the scene]
- Entity 3: [appearance], [position], [role in the scene]

Count check: exactly [N] entities, no more, no fewer.
```

## Prompting Technique: Spatial Layout Description

Say relationships explicitly rather than implying them through composition
adjectives.

```text
Canvas:
- aspect ratio: [value]
- viewpoint: [eye-level / overhead / three-quarter / etc.]
- foreground: [what's closest to camera]
- midground: [what's in the middle distance]
- background: [what's farthest away]

Relationships:
- [entity A] is to the left of [entity B]
- [entity C] is behind [entity A]
- [entity B] is larger than [entity C]
```

## When Autoregressive/Token-Based Tends To Outperform Diffusion

Prefer this family, or at least test it against a diffusion tool, when the
task is:

- **Text-in-image accuracy matters.** Short, exact strings (a sign, a label,
  a UI mockup with real copy) are frequently rendered more reliably.
- **Layout precision matters more than painterly style.** Diagrams,
  infographics, UI wireframes, and anything with a "this must be at position
  X" requirement.
- **Exact counts matter.** "Exactly 3 icons in a row" is a common diffusion
  failure point and a relative strength here.
- **The workflow is conversational and edit-oriented.** Iterating in natural
  language ("now move the logo to the top-left") fits a multimodal chat-style
  interface well.
- **The task blends text reasoning and image output.** For example, generating
  a diagram that must also be factually consistent with surrounding text.

Prefer diffusion instead when the priority is rich painterly style, texture,
photorealism, or mood over structural precision — see
[diffusion-models.md](diffusion-models.md) for that side of the comparison.

## Prompt Pattern

```text
Create a clean product image of [object] on [background].
Composition: [camera angle], [lighting], [important details].
Text: render exactly "[short text]" if supported.
Avoid: private logos, private people, unsafe content, extra text.
Output: [aspect ratio], [style constraints].
```

## Failure Modes

- Text rendering is misspelled or distorted.
- Product details drift between revisions.
- The model invents logos or private-looking labels.
- API behavior, pricing, and model names change.
- Ordered instructions still get partially ignored on complex scenes; simplify
  and re-check the entity count and layout when this happens.

## Evaluation Checklist

- [ ] Does the image match the prompt?
- [ ] Is text readable and exact?
- [ ] Are private brands, faces, or account details absent?
- [ ] Is source/provider status documented?
- [ ] Are API key and subscription needs clear?
- [ ] Does the entity count in the output match the entity inventory in the prompt?

## When To Prefer This Family

Autoregressive or multimodal image systems are often useful when the workflow
is conversational, edit-oriented, or tied to a broader model that can reason
about text and images together.

Use them when:

- The user wants iterative revision in natural language.
- The prompt includes text layout or diagram-like constraints.
- The tool provides a browser or API path with clear privacy terms.
- The task is a public-safe draft, not a private identity or credential image.
- The team can verify exact tool behavior in official docs.

Avoid overclaiming:

- Do not promise exact typography unless the tool's current docs and output
  prove it.
- Do not assume local installation exists.
- Do not state model names, availability, or pricing as permanent facts.

## Revision Workflow

1. Generate a first draft with a compact prompt.
2. Inspect the image against the required subject, composition, text, and safety
   constraints.
3. Write a revision prompt that names what to preserve and what to change.
4. Reject outputs that invent private details, extra labels, unsafe content, or
   brand-like marks.
5. Record the final prompt and review notes if the result is used in docs.

Revision prompt:

```text
Revise the previous image.
Preserve: [subject], [camera angle], [background], [approved text].
Change: [specific issue].
Do not add: private logos, extra words, signatures, faces, account details, or
watermarks.
Review target: [what the human will inspect].
```

## Documentation Requirements

If this repository documents an autoregressive image workflow, the guide should
include:

- Official-doc verification note for provider behavior.
- Privacy and data-retention caution.
- API key or account requirement, if relevant.
- Text-rendering limitations and manual review.
- Example prompt and revision prompt.
- Failure modes and rejection criteria.

## Rejection Criteria

Reject generated outputs when:

- Text is misspelled, extra, or unreadable.
- The image includes private-looking names, IDs, QR codes, or account screens.
- A real person's likeness appears without explicit permission.
- The model invents a brand mark or copyrighted-looking label.
- The output violates the intended public repository safety boundary.
