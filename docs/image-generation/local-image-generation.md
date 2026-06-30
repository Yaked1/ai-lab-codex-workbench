# Local Image Generation

Local image generation is useful for learning and privacy-sensitive experiments,
but it is easy to over-recommend heavy GPU setups to beginners.

## Local Workflow Levels

| Level | Example fit | Beginner guidance |
| --- | --- | --- |
| Lightweight local | Small experiments, prompt syntax practice | Accept slow output and limited quality. |
| Advanced local GPU | Diffusion UIs, node workflows, batch generation | Use only with enough VRAM and license review. |
| Local training/fine-tuning | Custom models, LoRAs, datasets | Not a beginner default. Use cloud or dedicated hardware. |

## Setup Guidance

Use each tool's official repository and docs. If commands are not verified in
the current PR, mark them as placeholders:

```powershell
# Placeholder only. Verify official tool docs first.
git clone <official-tool-repository-url>
cd <tool-folder>
<official-install-command>
```

## Public-Safe Notes

- Do not commit model files, checkpoints, LoRAs, or generated image archives.
- Do not commit private reference images.
- Do not include private prompt histories.
- Keep `.env` and API keys out of Git.
- Document model licenses separately from UI/tool licenses.

## Failure Modes

- GPU driver mismatch.
- Python or Node version mismatch.
- VRAM too small for the selected model.
- Missing model weights.
- Long install time on entry-level hardware.

## Safer Alternatives

- Browser/API image tools.
- Cloud notebooks with clear cost limits.
- Small public sample prompts without local generation.
- Static guide validation in GitHub Actions instead of generation.

## Local Setup Boundary

Local image generation should be documented as an advanced path unless the
setup has been verified on ordinary hardware. A guide should not imply that a
reader can download any model, run any UI, and get reliable results on an
entry-level laptop.

Before adding a local setup command, verify:

- The official repository or release page.
- The supported operating systems.
- Required Python, Node, driver, or runtime versions.
- Expected VRAM, RAM, and disk space.
- Model-file license and redistribution limits.
- Whether generated outputs can be used publicly.
- How to remove large generated files from the repository.

## Local Project Hygiene

Keep local generation artifacts outside the repository unless a public-safe
asset is intentionally committed.

Recommended local folders:

```text
image-work/
  prompts/
  outputs/
  rejected/
  notes/
```

Do not commit:

- Checkpoints.
- LoRAs.
- Embeddings.
- Generated batches.
- Private reference images.
- Prompt histories containing private text.
- Tool caches.

## Beginner Exercise Without Running Models

A beginner can still learn image prompting without local generation.

1. Pick a public-safe use case such as a documentation banner or product draft.
2. Write subject, composition, lighting, style, output, and safety constraints.
3. Add a review checklist.
4. Compare the prompt against `prompting-patterns.md`.
5. Mark the actual generation tool as "browser/API or official docs to verify."

This keeps the lesson focused on prompt quality, not driver installation.

## Failure Recovery

| Failure | Recovery |
| --- | --- |
| Install takes too long | Stop and use browser/API workflow for the learning task. |
| Model file is missing | Do not search random mirrors; use official source or skip. |
| GPU is unsupported | Lower expectations, use hosted workflow, or choose CPU-friendly experiments only. |
| Output contains private reference data | Delete local output and do not commit it. |
| License is unclear | Treat result as non-publishable until reviewed. |
