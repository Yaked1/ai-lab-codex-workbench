# Skills Package

This folder packages this repository's guides, tool docs, and prompt
templates into 100+ installable **skill bundles** that an AI coding-agent
harness can load or stage for manual use. It is additive: nothing in
[docs/](../docs/) or
[prompts/](../prompts/) moved or changed shape because of this folder. Every
skill here is a thin, actionable wrapper that points back at the deep guide
it packages -- the guides stay the single source of truth, and skills stay
short enough to actually read before running.

See [docs/skills/README.md](../docs/skills/README.md) first if you have not
already -- it explains what "skill" means (and does not mean) per tool, and
this folder is the concrete implementation of the rubric that guide
describes in the abstract. The catalog includes a few hand-authored workflow
skills plus generated wrappers for the repository's public docs and prompt
templates, so agents can reach for the right source guide quickly without
copying the source text into every task.

## Quick Install

```powershell
git clone https://github.com/Yaked1/ai-lab-codex-workbench.git
cd ai-lab-codex-workbench
python scripts/install_skill.py --list
python scripts/install_skill.py --skill use-codex-safely --harness codex-cli
python scripts/install_skill.py --skill use-codex-safely --harness claude-code-cli
```

PowerShell users can use the native script instead of the Python one:

```powershell
.\scripts\install_skill.ps1 -List
.\scripts\install_skill.ps1 -Skill use-codex-safely -Harness codex-cli
.\scripts\install_skill.ps1 -Skill use-codex-safely -Harness claude-code-cli
```

Install every skill at once:

```powershell
.\scripts\install_skill.ps1 -All -Harness codex-cli
.\scripts\install_skill.ps1 -All -Harness claude-code-cli
.\scripts\install_skill.ps1 -All -Harness hermes -Scope user
```

No clone available yet, or scripting on a machine without the repo? Download
just the installer first, **read it**, then run it -- never pipe a remote
script straight into a shell:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Yaked1/ai-lab-codex-workbench/main/scripts/install_skill.ps1" -OutFile install_skill.ps1
notepad install_skill.ps1   # read it before running it
.\install_skill.ps1 -Skill use-codex-safely -Harness codex-cli
```

The installer then fetches only the specific skill's files over plain HTTPS
(`Invoke-WebRequest` / `urllib.request`, both already part of Windows
PowerShell and the Python standard library -- no new dependency is added).
See [Installer Behavior](#installer-behavior) below for exactly what each
`-Harness` value does, because it is not the same for every tool.

## Why This Exists

Reading a 10-15KB guide before every task does not scale. A skill is the
same knowledge compressed into a trigger, a scope, an ordered procedure, and
a verification list -- short enough for an agent (or a human) to hold in
working memory, with a link back to the full guide for anything that needs
more depth. [docs/skills/README.md](../docs/skills/README.md) already
defines the quality bar (Skill Anatomy Checklist, Quality Bar, Review
Rubric); this folder applies that bar across the repository's current public
docs and prompt templates.

## Skill Bundle Shape

Every skill is a folder under `skills/` containing at least one file:

```text
skills/<slug>/
  SKILL.md          # required
  references/       # optional -- longer supporting material, rare
  scripts/          # optional -- helper scripts, rare, stdlib only
```

`<slug>` is lower-kebab-case and doubles as the skill's install name.

### `SKILL.md` Frontmatter

```yaml
---
name: <slug>
description: <one sentence: when an agent should reach for this skill>
category: <tools | prompts | codex-workflow | hermes | image-generation | guides | meta>
source:
  - <repo-relative path to the deep guide(s) this skill packages>
---
```

`source` must always point at a real, current file in this repository.
[tests/test_skills_package.py](../tests/test_skills_package.py) fails the
build if a `source` path does not exist, so a skill can never silently drift
from the guide it claims to summarize.

### `SKILL.md` Body

Every skill answers the same nine questions
[docs/skills/README.md](../docs/skills/README.md#skill-anatomy-checklist)
already defines, as these exact section headings:

```markdown
## Trigger
## Purpose
## Inputs
## Scope
## Procedure
## Verification
## Failure Cases
## Final Report
## Disable Path
```

Keep the body short -- 40 to 120 lines is normal. If a step needs more
explanation than that, link to the source guide instead of inlining it.

## Content Rules (Inherited From AGENTS.md)

Every skill in this folder follows the same rules as every other public
document in this repository -- see
[AGENTS.md](../AGENTS.md#documentation-quality-rules) for the full list.
The ones that matter most for skill content specifically:

- No invented exact pricing, plan tiers, or model-availability claims for
  fast-moving external tools. Say "verify current details in official docs."
- No secrets, private paths, private links, or machine-specific detail.
- Windows PowerShell examples for every command.
- No Docker, WSL, or GPU-heavy setup recommended as a default.
- Hermes-category skills cover only the Hermes Agent workflow tool, never
  the Hermes language-model family, benchmarks, quantization, GGUF, Ollama,
  vLLM, or SGLang.
- Every skill must end with a trailing newline.

## Installer Behavior

`scripts/install_skill.ps1` and `scripts/install_skill.py` are equivalent;
use whichever fits your shell. Both are standard-library only -- no new
dependency was added to install or run either one.

| `-Harness` value | What actually happens | Why |
| --- | --- | --- |
| `codex-cli`, `codex-desktop`, `codex` | Copies `skills/<slug>/` to `.agents/skills/<slug>/` (project scope, default) or `~/.agents/skills/<slug>/` with `-Scope user`. | OpenAI's Codex skills docs describe `.agents/skills` as the repo/user skill location and say skills are available in the Codex CLI, IDE extension, and Codex app. |
| `claude-code-cli`, `claude-code-desktop`, `claude-code` | Copies `skills/<slug>/` to `.claude/skills/<slug>/` (project scope, default) or `~/.claude/skills/<slug>/` with `-Scope user`. | Claude Code has a documented native `SKILL.md` bundle format that loads from these paths. The `claude-code-desktop` value is a convenience alias for the same Claude Code project skill folder, not a claim about the consumer Claude app. |
| `hermes` | With `-Scope user`, copies `skills/<slug>/` to `~/.hermes/skills/<slug>/SKILL.md`. With project scope, stages the same folder shape under `.agent-skills/hermes/<slug>/SKILL.md` so you can add `.agent-skills/hermes` to Hermes `skills.external_dirs`. | Hermes documents local skills under `~/.hermes/skills`, optional external skill directories, GitHub/tap installs, and direct URL installs. This repository's public `skills/<slug>/SKILL.md` files are real Hermes-compatible skill bundles, not placeholder text. |
| `cursor`, `windsurf`, `aider`, `antigravity`, `github-copilot`, `opencode`, `kilo-code`, `mcp` | Copies the skill body (frontmatter stripped) to `.agent-skills/<harness>/<slug>.md` and prints where that tool's own custom-instructions/rules mechanism currently lives, per `docs/tools/<harness>.md`. | These tools have no native skill-loading mechanism today -- see the "What Counts As A Skill In Each Tool" table in [docs/skills/README.md](../docs/skills/README.md). Staging a plain file and telling you exactly where to paste it is honest; claiming an auto-install path that does not exist would not be. |

The installer never overwrites an existing target without `-Force`, never
deletes anything outside the target skill folder, and never pipes a remote
script into a shell for you to execute -- it only fetches plain Markdown/JSON
files when you are not already inside a clone.

## Agent-Created Prompting Skills

Yes: this package includes the two meta-skills needed for an agent to create
more prompting skills and then follow a prompt it generated for itself.

- `create-a-new-skill` turns a recurring workflow, guide, or prompt template
  into one new `skills/<slug>/SKILL.md` bundle, updates `skills/INDEX.md` and
  `skills/manifest.json`, and requires the skill-package tests before it can
  be reported done.
- `self-directed-goal-runner` turns a broad task into a bounded self-prompt
  under `.tmp/self-prompts/<slug>.md`, follows one checklist step per
  iteration, and stops on ambiguity, failed verification, scope creep, or its
  iteration cap.

Use them together for self-extension: first install the catalog into the
target harness, then ask the agent to use `create-a-new-skill` for the new
prompting workflow and `self-directed-goal-runner` to write and follow the
task prompt. The new skill must still have real source files, required
sections, manifest/index entries, and passing tests. Do not publish empty
scaffolds or unverifiable tool claims.

## Full Skill Index

See [skills/INDEX.md](INDEX.md) for the complete list of every skill in this
folder with its one-line description, category, and source guide.

## Verification

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
python scripts/install_skill.py --list
```

`tests/test_skills_package.py` specifically checks: every `skills/*/SKILL.md`
has the required frontmatter and section headings, every declared `source`
path exists in the repository, and `skills/INDEX.md` lists every skill with
no orphans in either direction.

## Maintenance And Disable Path

- To retire a skill, delete its folder under `skills/` and remove its row
  from `skills/INDEX.md` and `skills/manifest.json` in the same change.
- To disable an already-installed skill without deleting the source, remove
  or rename its folder from the harness-specific install location listed in
  the table above (for example `.claude/skills/<slug>/`); the copy in this
  repository is unaffected.
- Review skill content whenever its source guide changes, whenever a tool's
  official skill-discovery behavior changes, or whenever
  `tests/test_skills_package.py` starts failing.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **installable agent skill** surface. During broad
maintenance, reviewers should treat `skills/README.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `README` state what decision, workflow, or reusable behavior it supports?
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
