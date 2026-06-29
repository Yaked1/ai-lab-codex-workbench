# Research Source Policy

The research loop has three separate stages:

1. A cheap daily scout that collects public candidate metadata.
2. A cheap curator prompt prep workflow that prepares a ready-to-copy local
   Codex prompt.
3. A local/manual Codex session run by the maintainer through Codex CLI or the
   Codex app using ChatGPT sign-in.

The scout and prompt prep jobs are inbox tools. They are not publishers and do
not call model providers.

## Daily Scout Rules

- Runs on schedule and `workflow_dispatch`.
- Does not call Codex.
- Does not require an OpenAI API key.
- Does not make paid LLM calls.
- Does not call model providers.
- Reads `data/research/sources.yml`.
- Writes `data/research/candidates.json`.
- Writes daily reports under `docs/research/inbox/YYYY-MM-DD.md`.
- May open or update one GitHub issue pointing to the latest candidates.
- Must not modify core guides automatically.
- Must not create releases or publish packages.
- Must not download large files or copy full external source content.

## Curator Prompt Prep Rules

- Runs only on `workflow_dispatch`.
- Does not require an OpenAI API key.
- Does not call Codex.
- Does not call paid LLMs.
- Does not call model providers.
- Reads candidate reports and source policies.
- Supports `scope`, `dry_run`, and `max_sources` inputs.
- Writes `docs/research/curated/curator-prompt-YYYY-MM-DD.md`.
- May open or update one issue telling the maintainer to run the prompt locally
  in Codex when usage is available.
- Must not create a PR with AI-written guide content.
- Must not push directly to `main` except for generated research prompt/report
  files when repository policy allows it.
- Runs repository validation before committing generated prompt files.

## Local Codex Curation Rules

The maintainer runs Codex locally using ChatGPT sign-in, not an API key:

```powershell
git switch main
git pull --ff-only origin main
git switch -c codex/curate-research-guides
codex
```

Then paste the generated prompt from:

```text
docs/research/curated/curator-prompt-YYYY-MM-DD.md
```

After Codex edits locally:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests

git add .
git commit -m "Curate research guide updates"
git push -u origin codex/curate-research-guides
gh pr create --title "Curate research guide updates" --body "Curates public-safe research guide updates from the scout report."
gh pr checks --watch
```

No cloud Codex GitHub Action is used.

## Candidate Metadata

Candidate records should store only:

- Source ID, name, category, and URL.
- Source status and official/community/unofficial label.
- License hints.
- Safety notes.
- Short summaries or page/repository metadata.
- HTTP or GitHub metadata from bounded public checks.
- Blocklist status and reasons.
- Deterministic score and quality label.

Do not store full prompt dumps, full docs, private data, or long copied excerpts.

## Starter Categories

`data/research/sources.yml` keeps editable starter categories:

- `official_docs`
- `agent_frameworks`
- `claude_code_skills`
- `codex_guides`
- `mcp_tools`
- `prompt_engineering`
- `prompt_auditing`
- `image_prompting`
- `local_image_generation`
- `public_research_repositories`
- `hermes_agent`
- `unofficial_pattern_sources`

Hermes Agent subtopics are source tags, not separate model categories:

- `agent_framework`
- `skills`
- `memory`
- `automations`
- `provider_configuration`
- `public_repo_safety`

Do not add Hermes language model categories.

## Blocklist Behavior

The scout should block or flag sources that look like secret dumps, credential
leaks, malware guides, prompt-leaking collections, exfiltration kits, or private
raw-file mirrors. A blocked source may stay in the candidate JSON for audit
visibility, but it must receive a zero score and must not become guide content.

## Manual Review Checklist

- [ ] Prefer official docs over community summaries.
- [ ] Verify install commands in official docs.
- [ ] Respect source licenses.
- [ ] Label unofficial or leak-derived sources.
- [ ] Avoid publishing leaked prompts or private content.
- [ ] Include failure modes and verification steps in generated guides.
- [ ] Keep Hermes Agent coverage limited to Nous Research Hermes Agent workflows.
- [ ] Keep image-generation guidance realistic for entry-level hardware.
