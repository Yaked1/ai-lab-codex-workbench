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
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `.github/codex/prompts/daily-guide-curator.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `daily guide curator` state what decision, workflow, or reusable behavior it supports?
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
