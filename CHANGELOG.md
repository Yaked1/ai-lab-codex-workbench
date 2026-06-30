# Changelog

## Unreleased

Fixed:

- Fixed a crash in `scripts/local_autopilot.ps1` where `-Mode local-codex` and `-Mode full-safe` failed with "You cannot call a method on a null-valued expression". The branch lookup called `.Trim()` on the null result of `git branch --list` when the target branch did not exist yet. Branch existence is now null-safe, the helper uses a single `-Branch` parameter (the unused `$BranchName` is gone), and the same null-safe guard was applied to the workflow-run lookup.

Changed:

- Added `docs/guides/comprehensive-prompt-engineering-guide.md`, a release-bundled curriculum covering prompt anatomy, context engineering, reusable prompt functions, task patterns, agentic prompting, coding agents, tool-use safety, RAG, reasoning, evaluation, prompt security, compression, image prompting, repository prompt management, templates, and review rubrics.
- Reworked the README into a sharper public landing page with a direct start-here table, fast path, core workflow, validation commands, prompt-template guide, safety rules, repository map, and linked archive/source-audit references instead of an inline archive manifest.
- Reworked the README into a public landing page with a clearer start-here path, repository map, validation commands, prompt-template usage, Codex/Claude Code navigation, and explicit public-safety non-goals.
- Added a `docs/guides/README.md` navigation page and expanded the Codex prompt templates into more operational work orders with included/excluded scope, safety boundaries, verification steps, final report formats, and failure cases.
- Added a source-inspired prompting curriculum and connected README, guide navigation, Prompting OS source maps, automation docs, release review guidance, and offline-site navigation to the public-safe source-to-release loop.
- Reworked the README into a standalone prompting and agent-skill playbook focused on prompting concepts, Claude Code skills, Codex operating instructions, tool-use safety, prompt evaluation, prompt compression, and autoregressive/diffusion image-generation prompting.
- De-personalized public-facing docs: the README, offline site, image-generation guides, publication policy, source policy, and prompt templates no longer reference a specific personal laptop (exact RAM, GPU model, or VRAM) and instead use generic hardware tiers (browser/API, entry GPU, advanced GPU, cloud). Audience framing moved from "student-friendly" to "beginner-friendly" for general public users.
- Made `local-codex` and `local-claude` default their branch (`codex/curate-research-guides` and `claude/curate-research-guides`) so they run without a `-Branch` argument, fast-forward `main` with `--ff-only` when possible (warn and continue when the branch has diverged), and keep refusing dirty trees, PR merges, force-pushes, and branch deletes.
- Made `repo_health_check.py` and `safe_autofix.py` skip local scratch, editor, and agent-tool state directories (`.tmp`, `.idea`, `.vscode`, `.omc`) and added them to `.gitignore` so local tooling does not break the standard validation.

Added:

- Added deterministic Prompting OS package builder coverage: `scripts/create_prompting_os_package.py` now builds a versioned ZIP plus public-safe JSON manifest with fixed archive timestamps, SHA-256 hashes, cache/private/archive exclusions, configurable source/output directories, and unit tests in `tests/test_prompting_os_package.py`.
- Added Prompting OS package build documentation to `docs/prompting-os/README.md` and `docs/releases-and-packages.md`, and made repository health checks require the Prompting OS docs, packaging script, and package tests.
- Added a comprehensive prompting curriculum: `docs/guides/prompting-ai-coding-agents.md` (the craft of prompting agents), `docs/guides/coding-agent-power-tips.md` (per-agent tricks for Claude Code, Codex, Cursor, Copilot, Aider, Windsurf, and MCP), and `docs/guides/prompting-references.md` (famous public prompting repositories and vendor docs to learn from, with leaked-prompt safe-use rules). The guides ship in every release bundle.
- Added a self-contained "Prompting And Agent Mastery" section to the README, surfaced the new guides in the offline site (`docs/site/index.html`, `docs/site/prompt-engineering.html`), and added `tests/test_prompting_docs.py` covering guide existence, README linkage, agent coverage, secret-free content, and release-package inclusion.
- Corrected the `/goal` references in the README, `docs/tools/claude-code.md`, and `docs/automation/local-autopilot.md`: `/goal` is not a built-in Claude Code feature, so the guidance now describes defining a reusable custom slash command in `.claude/commands/`.
- Added a `local-claude` mode to `scripts/local_autopilot.ps1` and documented a manual Claude Code local research-curation workflow alongside Codex, including `/goal` usage, in the README, `docs/automation/local-autopilot.md`, `docs/tools/claude-code.md`, and `AGENTS.md`.
- Added `tests/test_local_autopilot.py` covering the autopilot default branch, null-safe branch handling, the `local-claude` mode, public README framing, offline site/deployment files, automation docs, and workflow safety guards (no `OPENAI_API_KEY`, no Codex action, generated-file-only automerge).
- Added a no-API-key Repository Autopilot layer with generated research PR automation, safe generated-file automerge, monthly release draft issue workflow, local PowerShell helper, status script, policy docs, and tests.
- Added the cheap `Daily Research Scout` workflow for public AI skills, prompt-guide, image-generation, MCP/tool-use, public agent workflow, and Hermes Agent candidate discovery without Codex or OpenAI API keys.
- Added the no-API-key `Curator Prompt Prep` workflow with `scope`, `dry_run`, and `max_sources` inputs to prepare local Codex prompts without calling Codex, paid LLMs, or model providers from GitHub Actions.
- Changed the curator architecture to local/manual Codex curation using Codex CLI or the Codex app with ChatGPT sign-in instead of an OpenAI API key or cloud Codex GitHub Action.
- Added public source and publication policies for official, community, unofficial, leak-derived, inferred, and unverified sources, including restrictions on leaked prompt dumps and private data.
- Added starter research source configuration, blocklist, candidates store, deterministic discovery/scoring/report scripts, and research inbox/curated folders.
- Added skills guide structure for Claude Code skills, Codex skills, MCP tool-use systems, and reusable prompt guides.
- Added image-generation guide structure for autoregressive systems, diffusion systems, local workflows, hardware requirements, prompting patterns, entry-level hardware warnings, and GitHub Actions boundaries.
- Added Hermes Agent documentation for Nous Research Hermes Agent setup, provider configuration, skills, memory, automations, prompting, troubleshooting, comparison with Codex and Claude Code, and public-repo safety.
- Updated Hermes Agent guide pages with explicit official source links, MIT license/source status, and current official-doc safety notes for setup, providers, skills, memory, and cron workflows.
- Added tests for research source parsing, candidate scoring, report generation, blocklist behavior, secret-looking string redaction, report path formatting, and scout dry-run mode.
- Reworked the README opening and quick-start path for general public users, including release-bundle guidance and clearer links for visitors, instructors, maintainers, and learners.
- Added safe autonomous release package support with `scripts/build_release_package.py`, `.github/workflows/release-package.yml`, `docs/releases/release-process.md`, `docs/releases/v0.1.0.md`, package-builder tests, and GitHub Release ZIP plus JSON manifest assets.
- Added release package files to repository health requirements and documented manual `gh workflow run release-package.yml` triggering without npm, PyPI, Docker, binary package, or GitHub Packages publishing.
- Expanded the README with repository non-goals, operating contract, decision guide, first-session workflow, end-to-end example, scenario playbooks, quality bar, troubleshooting, and maintenance model.
- Expanded `CONTRIBUTING.md` with contribution types, definition of ready, scope control, PR expectations, documentation style guidance, script/test expectations, review roles, and post-merge practices.
- Expanded `SECURITY.md` with a public-repository threat model, public-safe examples, permission levels, workflow-secrets guidance, security review checklist, incident response steps, and AI-agent risk patterns.
- Expanded Codex onboarding, goal workflow, review checklist, and tool guide docs with beginner concepts, scope calibration, evidence-based completion, trust boundaries, reviewer questions, and failure patterns.
- Expanded task, merge, and sample-task templates with readiness checks, acceptance evidence, external-claim review, rollback planning, and stronger final-report examples.
- Professional public positioning for the AI agent coding and prompting workbench.
- Expanded README sections covering audience, architecture, safety model, quick start, learning path, tool matrix, recommended workflows, limitations, and roadmap.
- Real GitHub Actions status badges for CI and Safe Autofix PR workflows.
- Stronger `AGENTS.md` guidance for safe edits, docs quality, public repo hygiene, testing, prompt templates, and conservative external claims.
- Expanded contribution and security guidance for public AI-agent collaboration.
- Comprehensive tool guide structure for Codex, Claude Code, Cursor, Antigravity, GitHub Copilot, OpenCode, Kilo Code, Aider, Windsurf, and MCP.
- Serious tool comparison matrix with beginner, practical, advanced, Windows laptop, docs, refactor, PR review, risk, and avoid-for-now rankings.
- Full workflow guidance for issue intake, branch naming, goal prompts, agent execution, local checks, CI checks, PR review, squash merge, rollback, public safety, secret scanning, and changelog updates.
- Professional reusable prompt templates with target tool, purpose, full prompt, short version, inputs, success criteria, safety boundaries, verification, final report format, and failure cases.
- Expanded Codex-specific guides for goal-style work, Git branch/PR/merge flow, safe autofix policy, review checklists, and roadmap planning.
- Offline static HTML quick-start site for AI agent workflows, prompt engineering, skills, tool setup, MCP safety, Windows commands, and public repository safety.
- Practical Markdown playbooks for prompt engineering, agentic coding, skills and prompt guides, Windows setup commands, and prompt audits.
- Static HTML documentation safety guidance covering offline assets, local CSS, no trackers, no CDNs, no analytics, no remote fonts, and no private links.

Fixed:

- Removed the duplicate release workflow path and restored package-builder tests required by repository health checks so `release-package.yml` can run without ambiguous workflow names.

## 0.1.0

Initial Codex automation workbench.

Added:

- `AGENTS.md` for agent instructions.
- GitHub Actions CI workflow.
- Manual autofix workflow.
- Manual merge workflow.
- Codex `/goal` prompt templates.
- PowerShell helper scripts.
- Python safety and formatting scripts.
- Issue and PR templates.
