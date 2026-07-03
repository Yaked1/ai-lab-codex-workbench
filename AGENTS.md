# AGENTS.md

This file gives Codex and other AI coding agents the local rules for this repository. Read it before editing anything.

## Project Purpose

This is a public, beginner-friendly AI coding-agent and prompting guide. It teaches safe repository work with Codex, Claude Code, and comparable tools: task intake, branch creation, prompt design, local checks, pull requests, review, controlled merge, rollback, changelog updates, and public-repository hygiene.

## Repository Profile

- Lightweight documentation, prompts, scripts, and templates.
- Windows and PowerShell friendly by default.
- Python standard library preferred.
- GitHub Actions used for validation and conservative automation.
- No heavy runtime dependencies.
- Avoid Docker, WSL, local model hosting, GPU-heavy tasks, and large dependency trees unless the user explicitly asks.

## Required Operating Rules

1. Run `git status` before making changes.
2. Inspect relevant files before editing.
3. Keep diffs small, focused, and tied to the requested task.
4. Do not edit unrelated files.
5. Do not delete files unless the user explicitly requests deletion.
6. Do not edit `.env`, `.env.*`, credentials, browser profiles, private documents, or secrets.
7. Do not add dependencies without explicit approval.
8. Do not run destructive commands.
9. Prefer Windows PowerShell commands in docs and final instructions.
10. Use conservative language for fast-changing external tools.
11. Mark product behavior, pricing, platform support, and model availability as items to verify in official docs.
12. Report anything you did not verify.

## Documentation Quality Rules

- Write for beginners first, but include enough detail for advanced users to audit the workflow.
- Prefer practical tables, checklists, command examples, prompt examples, and failure modes.
- Do not invent exact pricing, private model details, release claims, or unsupported features.
- Do not include secrets, personal data, private links, private repository URLs, or machine-specific private paths.
- For Codex references, keep guidance aligned with official concepts such as `AGENTS.md`, configuration, skills, subagents, local/IDE/web/cloud workflows, permissions, and reviewable goal-style work.
- For non-Codex tools, keep claims conservative and direct readers to official documentation.
- Link to deeper docs instead of making this file bloated.
- For broad "make the repository more comprehensive" tasks, use
  [docs/workflows/research-grade-repository-expansion.md](docs/workflows/research-grade-repository-expansion.md)
  as the quality bar: every touched file should gain purpose, scope,
  operational detail, verification, safety boundaries, navigation, or failure
  handling. Do not pad files just to make them longer.

## Static HTML Documentation Rules

- Static HTML docs in `docs/site/` must work offline by opening the file in a browser.
- Use plain HTML and CSS only. Do not add external JavaScript, analytics, trackers, CDNs, remote fonts, or framework assets.
- Keep styles and assets local to the repository and public-safe.
- Prefer relative links to repository docs and prompt templates.
- Do not include private links, account-specific URLs, personal data, private paths, screenshots, or secrets.
- Keep pages useful: include real workflow guidance, checklists, tables, command blocks, and safety notes.

## Safe Edit Boundaries

Safe by default:

- Markdown docs.
- Static HTML/CSS docs that are offline-safe and public-safe.
- Prompt templates.
- Standard-library Python scripts already present in the repo.
- Tests for existing scripts.
- GitHub Actions only when the task explicitly involves automation.

Avoid unless explicitly requested:

- Workflow YAML changes.
- Dependency installation.
- Package manager lock files.
- Broad rewrites across unrelated docs.
- Large generated artifacts.
- Binary files, images, archives, and model files.

## Broad Expansion Protocol

When the requested task is a broad repository expansion, do not start by
editing every Markdown file. Start by turning the request into a reviewable
artifact plan:

1. Inspect `git status --short --branch` and preserve any unrelated local work.
2. Identify the major repository surfaces involved: README, workflow docs,
   prompt templates, skills, scripts, tests, safety policy, release/package
   docs, and changelog.
3. Pick the smallest set of files that covers those surfaces and can still be
   reviewed in one PR.
4. Add depth where it changes reader behavior: commands, decision tables,
   review evidence, failure modes, and safety boundaries.
5. Add maintenance hooks for new core docs: README links, health-check required
   files, tests for durable headings, and changelog entries.
6. Run repository checks and `git diff --check` before staging.

For broad work, "comprehensive" means useful, evidenced, navigable, and safe.
It does not mean every file must be longer.

## Local Checks

Run these after relevant changes:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

If a check fails:

- Fix the smallest likely cause when it is related to your change.
- Rerun the focused failing check.
- If the failure is unrelated to the requested task, report it clearly instead of rewriting the project.

## Approved Safe Commands

Generally safe inside this repository:

```powershell
git status
git diff
git branch
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python scripts/safe_autofix.py --write
python -m unittest discover -s tests
```

Use caution and ask before:

```powershell
pip install ...
npm install ...
gh repo delete ...
git clean -fd
Remove-Item -Recurse -Force ...
```

Never run commands that format disks, delete broad directories, expose secrets, force-push shared history, or modify system-wide settings.

## Branch, Commit, and PR Rules

- Use branches named `agent/<short-task-name>`.
- Keep one branch focused on one task.
- Commit messages should be concise and factual.
- Never claim tests passed unless they were actually run.
- Every PR should include what changed, why it changed, commands run, checks run, screenshots only for visual changes, and known limitations.

## Prompt Template Rules

Prompt templates in [prompts/](prompts/) should include:

- Target tool.
- Purpose.
- Full prompt.
- Short version.
- Inputs to fill.
- Success criteria.
- Safety boundaries.
- Verification steps.
- Final report format.
- Failure cases.

## Research Automation Rules

- Do not run expensive LLM workflows automatically.
- The daily research scout must stay cheap, public-safe, and free of Codex or OpenAI API key usage.
- Repository Autopilot may only automate generated research files: `data/research/candidates.json`, `docs/research/inbox/*.md`, and `docs/research/curated/curator-prompt-*.md`.
- Safe automerge must reject content, code, workflow, policy, script, test, Hermes Agent, image-generation, skills, README, AGENTS, or changelog changes.
- Local AI curation remains manual through a local agent (Codex via ChatGPT sign-in, or Claude Code), local branch work, pull request checks, and human review.
- Never add API-key LLM execution to GitHub Actions.
- Never auto-publish releases.
- Scheduled workflows must not add `OPENAI_API_KEY` requirements.
- GitHub Actions must not run Codex directly through the OpenAI Codex Action or any paid LLM provider.
- The curator prompt prep workflow must stay cheap, run only when manually triggered, and prepare a local Codex prompt instead of writing AI-generated guide content.
- Guide writing must happen locally through a local agent (Codex CLI or the Codex app using ChatGPT sign-in, or Claude Code), followed by branch, pull request, checks, review, and merge.
- Never push curated guide content directly to `main`.
- Do not mirror leaked prompts or publish leaked system prompts verbatim.
- Do not publish private data, private memories, private conversations, private logs, private paths, OAuth files, or secrets.
- Do not recommend heavy local image-generation models, local training, vLLM, SGLang, or GPU-heavy workflows as beginner defaults.
- Hermes Agent docs must cover only Nous Research Hermes Agent as an agent/workflow tool and must exclude Hermes language model, model-card, benchmark, quantization, GGUF, Ollama, vLLM, and SGLang coverage.
- All generated guides must include failure modes, source references, source/license status, and verification steps.

## Public Repository Hygiene

Before finalizing public-facing docs:

- Confirm no secrets or token-like examples are present.
- Confirm no private links, private account IDs, or private file paths are present.
- Keep external tool claims evergreen where possible.
- Add "verify in official docs" notes for fast-changing tool behavior.
- Update [CHANGELOG.md](CHANGELOG.md) for user-visible documentation or workflow changes.

## Deeper References

- Project overview: [README.md](README.md)
- Contribution workflow: [CONTRIBUTING.md](CONTRIBUTING.md)
- Security policy: [SECURITY.md](SECURITY.md)
- Agent lifecycle: [docs/workflows/agent-task-lifecycle.md](docs/workflows/agent-task-lifecycle.md)
- Research-grade expansion: [docs/workflows/research-grade-repository-expansion.md](docs/workflows/research-grade-repository-expansion.md)
- Public repo safety: [docs/workflows/public-repo-safety.md](docs/workflows/public-repo-safety.md)
- Tool comparison: [docs/tools/comparison-matrix.md](docs/tools/comparison-matrix.md)
- Codex start guide: [docs/codex/00-start-here.md](docs/codex/00-start-here.md)

## Definition of Done

A task is done only when:

- The requested change is complete.
- The diff is minimal and reviewable.
- Relevant checks were run.
- Failing checks are fixed or honestly reported.
- Public-safety constraints are preserved.
- The final response includes changed files, commands run, checks run, and remaining risks.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **top-level repository policy document** surface. During broad
maintenance, reviewers should treat `AGENTS.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `AGENTS` state what decision, workflow, or reusable behavior it supports?
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
