# Image Prompting Guide Generator Prompt

Target tool: Local Codex curator prompt

Purpose: generate public-safe image prompting and image-generation workflow
guides without running image-generation models in GitHub Actions.

Required sections to preserve or add:

- Autoregressive image models.
- Diffusion models.
- Hybrid systems.
- Browser/API image models.
- Local image generation tools.
- Quantized/local-friendly setups.
- Heavy GPU setups.
- Prompt templates.
- Text rendering guidance.
- Style control.
- Marketing/product shots.
- Character consistency.
- 3D asset reference prompting.
- Negative prompting where relevant.
- Local hardware warning tables.

Hardware realism:

- On entry-level hardware without a capable GPU, prefer browser/API workflows
  and lightweight local experiments.
- Do not recommend heavy diffusion models, training, fine-tuning, vLLM, SGLang,
  or heavy GPU workflows as beginner defaults.
- Separate browser/API, lightweight local, advanced local GPU, and cloud
  workflows.

Safety:

- Do not run image-generation models in GitHub Actions.
- Do not include private images, private prompts, or private account links.
- Include failure modes, evaluation checklists, source links, and license/source
  status.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `.github/codex/prompts/image-prompting-guide-generator.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `image prompting guide generator` state what decision, workflow, or reusable behavior it supports?
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
