# Skill Index

This starter index lists every installable skill bundle currently shipped in
`skills/`. The source of truth for installer automation is
[`manifest.json`](manifest.json); this page is the human-readable companion.

| Skill | Category | What it helps with | Source |
| --- | --- | --- | --- |
| `use-codex-safely` | tools | Start a Codex session with repo rules, scoped edits, checks, and reviewable PR flow. | `docs/tools/codex.md`, `docs/codex/00-start-here.md`, `docs/codex/01-codex-goal-workflow.md`, `AGENTS.md` |
| `self-directed-goal-runner` | meta | Convert a broad goal into a bounded checklist with stop conditions and verification. | `docs/templates/task-spec.md`, `AGENTS.md`, `docs/skills/README.md` |
| `create-a-new-skill` | meta | Author one new skill bundle from an existing guide, prompt template, or recurring workflow. | `docs/skills/README.md`, `skills/README.md`, `skills/use-codex-safely/SKILL.md` |
| `install-this-skill-pack` | meta | Install one or more skills into Claude Code, Codex, or a staged harness-specific file. | `skills/README.md`, `scripts/install_skill.ps1`, `scripts/install_skill.py` |

## Maintenance

When a skill is added or removed, update this index and
[`manifest.json`](manifest.json) in the same change. The test suite checks
that every manifest entry has a matching folder and that every listed source
path exists.
