# Skills Package

This folder packages this repository's guides, tool docs, and prompt
templates into a small v1 starter pack of installable **skill bundles** that
an AI coding-agent harness can load or stage for manual use. It is additive:
nothing in [docs/](../docs/) or
[prompts/](../prompts/) moved or changed shape because of this folder. Every
skill here is a thin, actionable wrapper that points back at the deep guide
it packages -- the guides stay the single source of truth, and skills stay
short enough to actually read before running.

See [docs/skills/README.md](../docs/skills/README.md) first if you have not
already -- it explains what "skill" means (and does not mean) per tool, and
this folder is the concrete implementation of the rubric that guide
describes in the abstract. This starter pack is intentionally modest: it
ships the safe Codex workflow, a bounded goal-runner pattern, and the two
meta-skills needed to create or install future bundles.

## Quick Install

```powershell
git clone https://github.com/Yaked1/ai-lab-codex-workbench.git
cd ai-lab-codex-workbench
python scripts/install_skill.py --list
python scripts/install_skill.py --skill use-codex-safely --harness claude-code
```

PowerShell users can use the native script instead of the Python one:

```powershell
.\scripts\install_skill.ps1 -List
.\scripts\install_skill.ps1 -Skill use-codex-safely -Harness claude-code
```

Install every skill at once:

```powershell
.\scripts\install_skill.ps1 -All -Harness claude-code
```

No clone available yet, or scripting on a machine without the repo? Download
just the installer first, **read it**, then run it -- never pipe a remote
script straight into a shell:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Yaked1/ai-lab-codex-workbench/main/scripts/install_skill.ps1" -OutFile install_skill.ps1
notepad install_skill.ps1   # read it before running it
.\install_skill.ps1 -Skill use-codex-safely -Harness claude-code
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
Rubric); this folder is where that bar is applied first to a starter set
that can grow through reviewed, tested additions.

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
| `claude-code` | Copies `skills/<slug>/` to `.claude/skills/<slug>/` (project scope, default) or `~/.claude/skills/<slug>/` with `-Scope user`. | Claude Code has a documented native `SKILL.md` bundle format that loads from these paths. |
| `codex` | Copies `skills/<slug>/` to `.codex/skills/<slug>/` and prints a caveat. | Per [docs/skills/codex.md](../docs/skills/codex.md), Codex's exact skill-discovery path is not verified in official docs as of this writing. The file is staged either way; if auto-discovery does not pick it up on your Codex surface, paste `SKILL.md`'s body into your session directly -- that always works, the same way this repo's own `.goal.md` prompts are pasted in. |
| `cursor`, `windsurf`, `aider`, `antigravity`, `github-copilot`, `opencode`, `kilo-code`, `mcp` | Copies the skill body (frontmatter stripped) to `.agent-skills/<harness>/<slug>.md` and prints where that tool's own custom-instructions/rules mechanism currently lives, per `docs/tools/<harness>.md`. | These tools have no native skill-loading mechanism today -- see the "What Counts As A Skill In Each Tool" table in [docs/skills/README.md](../docs/skills/README.md). Staging a plain file and telling you exactly where to paste it is honest; claiming an auto-install path that does not exist would not be. |

The installer never overwrites an existing target without `-Force`, never
deletes anything outside the target skill folder, and never pipes a remote
script into a shell for you to execute -- it only fetches plain Markdown/JSON
files when you are not already inside a clone.

## Full Skill Index

See [skills/INDEX.md](INDEX.md) for the complete v1 starter list of every
skill in this folder with its one-line description, category, and source
guide.

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
