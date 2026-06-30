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

## Evaluation Checklist

- [ ] Does the image match the prompt?
- [ ] Is text readable and exact?
- [ ] Are private brands, faces, or account details absent?
- [ ] Is source/provider status documented?
- [ ] Are API key and subscription needs clear?

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
