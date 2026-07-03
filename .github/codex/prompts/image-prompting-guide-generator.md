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
