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
