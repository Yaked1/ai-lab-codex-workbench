# Publication Policy

This repository is public educational material. Published guides must be useful,
attributed, reproducible, and safe for a general audience.

## Core Rules

- Do not republish leaked system prompts verbatim.
- Do not publish private, proprietary, or copyrighted prompt dumps.
- Do not publish secrets, tokens, private paths, private emails, private
  memories, private conversations, OAuth files, browser session data, or logs
  that may contain credentials.
- Prefer official documentation when available.
- Clearly label unofficial, community, leaked, inferred, or unverified sources.
- Respect source licenses and attribution requirements.
- Avoid bypass, exfiltration, prompt leakage, malware, credential theft, abuse,
  jailbreak, or evasion content.
- Do not mirror leaked prompt repositories.
- Do not build guides that encourage prompt leaking or jailbreaks.
- Do not recommend heavy local models or heavy image-generation stacks as
  beginner defaults.

## Leak-Derived Or Unofficial Prompt Sources

Repositories such as `asgeirtj/system_prompts_leaks` may be used only for:

- Pattern extraction.
- Structural comparison.
- Public-safe summaries.
- Short attributed excerpts only when legally safe and necessary.
- Links to source pages.

They must not be used to copy, mirror, or normalize leaked prompts into this
repository.

## Source Labels

Use one of these labels in curated docs:

| Label | Meaning |
| --- | --- |
| Official documentation | Published by the tool or project maintainer. |
| Official repository | Source repository controlled by the project maintainer. |
| Community repository | Public user/community project; verify license and maintenance. |
| Unofficial source | Not controlled by the vendor or maintainer. |
| Leak-derived source | Use only for structural pattern extraction and public-safe summaries. |
| Inferred | Reasoned from public behavior; do not present as confirmed fact. |
| Unverified | Needs official confirmation before exact commands or claims are published. |

## Image Generation Guidance

Separate image-generation workflows into:

- Browser/API tools for beginners.
- Lightweight local tools for small experiments.
- Advanced local GPU workflows.
- Cloud GPU or managed workflows.

On entry-level hardware without a capable GPU, prefer browser/API image
generation or lightweight local experiments.
Avoid heavy diffusion models, local training, fine-tuning, vLLM, SGLang, and
large GPU workflows as beginner defaults.

## Automation Boundary

The daily scout may collect candidate metadata and write inbox reports. It must
not call Codex, require OpenAI API keys, publish polished guides, create
releases, call model providers, or run image-generation models.

The curator prompt prep workflow may prepare a ready-to-copy local Codex prompt
only when manually triggered. Actual Codex writing happens locally through Codex
CLI or the Codex app, followed by branch, pull request, checks, and human review.

## Generated Publication Boundary

Generated research publication is limited to these paths:

- `data/research/candidates.json`
- `docs/research/inbox/*.md`
- `docs/research/curated/curator-prompt-*.md`

The daily scout, curator prompt prep, and repository autopilot workflows never
write the default branch. When allowed generated changes exist, each workflow
creates the same-repository branch
`autopilot/generated-${{ github.run_id }}-${{ github.run_attempt }}` from the
default branch, commits as the GitHub Actions bot, pushes that branch, and
opens a new pull request for human review. Including `github.run_attempt`
prevents a rerun from colliding with the first attempt's branch. Repository
maintainers review generated PRs before merge.

Candidate metadata and curator prompts are automation outputs. Curated guide
content remains a human-reviewed contribution and is not published by those
workflows. The workflows do not delete remote branches. After a generated PR is
merged or closed, branch retirement is a separately configured owner setting or
a maintainer action; this policy does not claim that either is active.

These workflows create pull requests with `GITHUB_TOKEN`. Under GitHub's
[token event rules](https://docs.github.com/en/actions/concepts/security/github_token),
an opened, synchronized, or reopened pull request created with that token does
create `pull_request` workflow runs in an approval-required state. Someone with
write access must approve those runs. The documented exception does not include
`pull_request_target`, so the safe-generated automerge workflow still requires
a separately authorized trusted invocation, such as its guarded manual
dispatch. Maintainers must verify that required checks actually completed
before merge. If PR creation fails after the branch push, the per-attempt branch
remains for inspection; an owner setting or maintainer action must retire it.
The workflow does not delete that ref automatically.

Each write-capable job has a checked-in guard that accepts manual dispatch only
from the default branch. A selected ref can contain a modified workflow, so the
guard is not an authorization boundary by itself. Owner-side workflow execution
protections must restrict manual dispatch to trusted maintainers, and those
maintainers must select the default branch.

When Repository Autopilot runs with `create_pr=false`, it completes generation
and validation but does not publish or push an orphan branch.

## Attribution Requirements

Every guide that is materially informed by external material should make the
source status clear. A short source note is enough for most docs, but deeper
guides should include a source ledger or reference section. The goal is to make
the origin of ideas auditable without copying private, leaked, or copyrighted
material into the repository.

Use this minimum standard:

- Official docs: link to the relevant page and note that behavior may change.
- Official repositories: link to the repository and verify the license.
- Community repositories: link to the source, verify the license, and avoid
  overstating maintenance status.
- Archive corpus material: use it for structure and coverage ideas, then write
  original guidance in this repository's voice.
- Leak-derived sources: do not mirror or normalize the prompt text.

## Pre-Publication Review

Before merging public-facing content, reviewers should confirm:

- No token-like strings, private paths, private account IDs, or private logs are
  present.
- External claims are either evergreen or marked for official-doc verification.
- Source/license status is documented where source material shaped the guide.
- Automation remains bounded, preview-first, and human-reviewed.
- Beginner recommendations do not assume heavy GPU, local training, or complex
  provider setup by default.
- The content teaches safe workflow habits instead of bypassing review.

## Incident Response

If private or unsafe material is found after publication:

1. Stop expanding the affected content.
2. Remove the unsafe material in the smallest possible follow-up change.
3. Rotate exposed credentials if any real secret or auth material appeared.
4. Review commit history and release assets for the same material.
5. Add a changelog or release note when users need to understand the correction.

Do not replace an incident response with vague wording. Name the class of issue
and the corrective action while avoiding repetition of the sensitive material.

## Pre-Publish Checklist, Deepened

The checklist in Pre-Publication Review above is the minimum bar. This section
expands each item with why it exists and a concrete, fast way to verify it, so
a reviewer with five minutes can actually check the box instead of assuming it.

### No token-like strings, private paths, private account IDs, or private logs

**Why:** a single leaked token or machine path in a public repository can be
scraped within minutes of merge. Public repos are indexed continuously; there
is no quiet grace period to fix it after the fact. Private paths and account
IDs are lower severity than a live token but still leak information about a
person's machine, employer, or account structure that they did not choose to
publish.

**Quick verification:**

```powershell
git diff --staged | Select-String -Pattern "sk-|ghp_|AKIA|api[_-]?key|password\s*=|Bearer\s"
git diff --staged | Select-String -Pattern "C:\\Users\\[A-Za-z0-9_.-]+"
```

Treat any hit as a stop-and-check, not a false-positive to wave through. A
placeholder like `C:\Users\example\project` is fine; a real Windows or WSL
username pulled from an actual command output is not.

### External claims are either evergreen or marked for official-doc verification

**Why:** pricing, rate limits, model availability, and plan tiers change on
a schedule this repository does not control. A specific dollar figure or
"currently supports X" statement written today can be false within weeks,
and a beginner reader has no way to know the guide is stale.

**Quick verification:** search the changed files for digits next to currency
symbols, the words "currently," "now supports," "as of today," or a bare
model name presented as available without a link. Anything matching should
either be rewritten as a general workflow description or moved under a
"verify in official docs" note.

```powershell
git diff --staged | Select-String -Pattern "\$\d|currently (supports|available)|as of today"
```

### Source/license status is documented where source material shaped the guide

**Why:** without a source note, a reader (or a future maintainer) cannot tell
whether a section is original guidance or adapted from someone else's
material, and cannot check whether that material's license permits the reuse.
This is also what makes the leak-derived structural-only rule enforceable:
if the source isn't named, nobody can audit whether the boundary was respected.

**Quick verification:** for any section that references an external
repository, paper, or prompt collection, confirm a link and a label
(official / community / academic / leak-derived) appear nearby, using the
labels defined in this document's Source Labels table.

### Automation remains bounded, preview-first, and human-reviewed

**Why:** this repository's core safety promise is that nothing publishes
itself. If a doc implies a workflow runs unattended end-to-end — scout finds
something, an LLM writes it up, and it merges without a human — that doc is
teaching an unsafe pattern even if no code in this repo actually does that.

**Quick verification:** read every sentence describing an automated job and
confirm it stops at "opens an issue," "writes a candidate file," or "prepares
a local prompt," never at "publishes," "merges," or "creates a release."
Cross-check against `AGENTS.md`'s Research Automation Rules, which is the
source of truth for what automation may and may not do.

### Beginner recommendations do not assume heavy GPU, local training, or complex provider setup by default

**Why:** the audience for this repository includes people on laptops without
a discrete GPU. A guide that defaults to "spin up vLLM" or "fine-tune a 7B
model locally" as step one silently excludes most of the intended audience
and sets an unrealistic baseline expectation.

**Quick verification:** for any beginner-facing section, confirm the first
recommended path is a browser/API tool or a lightweight local option, with
heavier GPU workflows introduced later and clearly labeled as optional/advanced.

### The content teaches safe workflow habits instead of bypassing review

**Why:** this is the meta-check. A guide can pass every other item and still
fail this one if its overall shape teaches a reader to skip branches, skip
review, or treat a human-in-the-loop step as optional friction to route
around.

**Quick verification:** read the guide's command sequence end to end and
confirm it still includes branch creation, local checks, and a pull request
step. If a shortcut path is documented, confirm it is explicitly labeled as
a deliberate exception with a stated reason, not presented as the default.

## Worked Example: A Document That Would Fail Review

Consider a hypothetical draft guide titled "Fast-track: publishing a
prompting guide in one command." It contains this passage:

> Run `python scripts/generate_guide.py --topic prompting --auto-merge` and
> the scout will pull the top 10 sources, have Codex draft the guide, and
> push it straight to `main`. This costs about $0.02 per guide on the
> current GPT-5.5 API pricing and takes under a minute. No need to open a
> PR for small guides like this.

This fails review on at least four independent grounds, any one of which
would be enough to block it:

1. **Automation boundary violation.** It describes an auto-merge path that
   writes AI-generated guide content directly to `main` with no human
   review step. This directly contradicts the Automation Boundary section
   above and the Research Automation Rules in `AGENTS.md`, which require
   local Codex curation followed by branch, PR, checks, and human review.
2. **Unverified exact pricing claim.** "$0.02 per guide on the current
   GPT-5.5 API pricing" is a specific dollar figure tied to a fast-changing
   provider price sheet. It is exactly the kind of claim that belongs under
   "Claims Needing Official-Doc Verification," not stated as settled fact.
3. **Implies API-key LLM usage in an automated path.** The passage implies
   an unattended script is calling a paid model API. This repository's rule
   set forbids adding API-key LLM execution to automation; any model calls
   must go through a local, human-driven Codex or Claude Code session.
4. **Discourages the reviewable-diff workflow.** "No need to open a PR for
   small guides like this" actively undermines the branch/PR/review
   practice this repository exists to teach. Even if the other three issues
   were fixed, this line alone would need to be removed.

A corrected version would describe the real workflow: the scout writes
candidate metadata, the curator prep step manually prepares a local prompt,
a maintainer runs that prompt through a local Codex or Claude Code session,
and the result goes through a normal branch, pull request, checks, and
review cycle before merge — with any pricing claim linked and marked for
official-doc verification instead of stated as a fixed number.
