# Image Generation Guides

This folder teaches public-safe image prompting and workflow selection. GitHub
Actions in this repository document and validate guides; they must not run
complex image-generation models.

## Guide Map

| Guide | Use it for |
| --- | --- |
| [Autoregressive image models](autoregressive-image-models.md) | Browser/API image systems that generate images token-by-token or through multimodal model stacks. |
| [Diffusion models](diffusion-models.md) | Local and cloud diffusion workflows, strengths, and warnings. |
| [Local image generation](local-image-generation.md) | Separating lightweight experiments from advanced GPU setups. |
| [Hardware requirements](hardware-requirements.md) | Realistic laptop, GPU, and cloud guidance. |
| [Prompting patterns](prompting-patterns.md) | Prompt templates for text rendering, style, product shots, characters, and 3D references. |

## Workflow Categories

- Browser/API tools: best beginner default.
- Lightweight local tools: small experiments only.
- Quantized/local-friendly setups: advanced experiments that must still state
  quality, speed, and compatibility tradeoffs.
- Advanced local GPU workflows: for users who understand model files, VRAM, and licenses.
- Cloud workflows: for heavy generation, batch jobs, or training.

## Model And Tool Families

| Section | Guidance |
| --- | --- |
| Autoregressive image models | Prefer official browser/API docs unless a local setup is verified. |
| Diffusion models | Separate browser/API, lightweight local, advanced GPU, and cloud paths. |
| Hybrid systems | Treat mixed multimodal, retrieval, editing, or diffusion-plus-agent systems as advanced until the setup is verified. |
| Browser/API image models | State API key, subscription, policy, and privacy requirements. |
| Local image generation tools | Include install commands only when verified; otherwise use placeholders. |
| Quantized/local-friendly setups | Warn about quality loss, unsupported hardware, and slow CPU fallback. |
| Heavy GPU setups | Keep out of beginner defaults and document VRAM, disk, license, and cloud alternatives. |

## Weak Laptop Warning

For an 8 GB RAM Windows laptop with a low-end NVIDIA MX-class GPU and about 2 GB
VRAM:

- Prefer browser/API image generation.
- Use lightweight local experiments only.
- Avoid heavy diffusion models as beginner defaults.
- Avoid local training or fine-tuning.
- Avoid vLLM, SGLang, and heavy GPU serving workflows.
- Use cloud or server GPUs only as advanced options.
