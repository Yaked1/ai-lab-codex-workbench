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
