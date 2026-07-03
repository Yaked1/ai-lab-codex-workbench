# Source Safety Review Prompt

Target tool: Local Codex curator prompt

Purpose: decide whether a candidate source can inform public repository
documentation without leaking private or copyrighted material.

Review every source for:

- Official status: official docs, official repository, community repository,
  unofficial source, leak-derived source, inferred source, or unverified source.
- License/source status: summarize the license hint and verify before adapting
  examples.
- Publication risk: leaked prompts, proprietary dumps, private files, secrets,
  private chats, malware, bypass, credential theft, exfiltration, jailbreak
  instructions, or copyrighted bulk content.
- Quote limits: prefer paraphrase and source links. Use short attributed
  excerpts only when legally safe and necessary.
- Public usefulness: beginner value, Windows friendliness, failure modes,
  evaluation guidance, and public-safe use cases.

Output requirements:

- Use source links.
- Label unofficial, community, leaked, inferred, or unverified sources.
- Reject any source that would require mirroring leaked prompt repositories.
- Reject any source that encourages prompt leaking or jailbreaks.
- Prefer official documentation when it exists.
- Keep source notes concise enough for a PR reviewer to audit.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `.github/codex/prompts/source-safety-review.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `source safety review` state what decision, workflow, or reusable behavior it supports?
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
