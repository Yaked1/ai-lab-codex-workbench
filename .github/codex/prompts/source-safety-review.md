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
