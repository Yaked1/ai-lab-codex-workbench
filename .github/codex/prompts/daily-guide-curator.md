# Local Codex Research Curator

You are running locally in Codex CLI or the Codex app after the maintainer copied
a prompt prepared by the no-API-key `Curator Prompt Prep` workflow. GitHub
Actions did not call Codex, use an OpenAI API key, or call a model provider.

First read:

- `docs/publication-policy.md`
- `docs/research/source-policy.md`
- `data/research/candidates.json`
- the newest files in `docs/research/inbox/`

Then select only the highest-quality public-safe sources within the configured
scope and maximum source count. Use the specialized prompt files below as
requirements, not as optional style advice:

- `.github/codex/prompts/source-safety-review.md`
- `.github/codex/prompts/skill-guide-generator.md` for `skills`, `prompt-guides`, or `all`
- `.github/codex/prompts/image-prompting-guide-generator.md` for `image-guides`, `model-guides`, or `all`
- `.github/codex/prompts/hermes-agent-guide-generator.md` for `hermes-agent` or `all`

Edit only Markdown guide files, prompt guide files, and research curation files
that are directly related to the configured scope. Keep the diff focused.

Required behavior:

- Do not publish polished docs directly to `main`.
- Do not add GitHub Actions that call Codex or paid LLM providers.
- Do not create releases or packages.
- Do not add dependencies.
- Do not run heavy image-generation models.
- Do not copy full external documents, prompt dumps, or leaked prompts.
- Do not include secrets, tokens, private paths, private emails, private
  memories, private chats, OAuth files, browser session data, or private logs.
- Mark unverified install commands as placeholders.
- Prefer Windows PowerShell examples where practical.
- Include failure modes, verification steps, source links, and license/source
  status in generated guides.
- Keep Hermes Agent coverage limited to Nous Research Hermes Agent as an
  agent/workflow tool. Exclude Hermes language model coverage.

When done, leave normal workspace edits for the workflow to validate and turn
into a patch artifact or pull request.
