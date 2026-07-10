# Skills And Prompt Guides

Skills and prompt guides are reusable instructions that help an AI agent perform a class of tasks consistently. They are useful when they stay small, local, public-safe, and easy to review.

This guide avoids exact setup claims for fast-changing tools. Verify tool-specific commands in official documentation before running or teaching them.

## Beginner Path

1. Start with a local `prompt-guides/` folder inside a practice repository.
2. Write one reusable Markdown prompt for a docs-only task.
3. Add a `SKILL.md`-style file that explains when to use the prompt.
4. Use placeholders instead of secrets.
5. Test the guide by pasting it into your agent tool.
6. Review the resulting diff and update the guide if the agent misunderstood.

Safe local folder setup:

```powershell
New-Item -ItemType Directory -Path .\prompt-guides -Force
New-Item -ItemType Directory -Path .\prompt-guides\skills -Force
New-Item -ItemType Directory -Path .\prompt-guides\templates -Force
New-Item -ItemType File -Path .\prompt-guides\README.md -Force
```

## Advanced Path

Use the advanced path when you want a repeatable library for several tools.

1. Separate prompts by task type, not by hype label.
2. Give each guide a purpose, trigger, inputs, safety boundaries, examples, verification, and final report.
3. Keep tool-specific setup notes in a "verify official docs" section.
4. Store private credentials outside Git and never inside prompt files.
5. Prefer read-only MCP or documentation connectors before write-capable tools.
6. Version prompt guides like code: small diffs, changelog notes, and review.
7. Test prompt guides on a disposable branch before recommending them to others.

## Recommended Folder Structure

```text
prompt-guides/
  README.md
  agent-tasks/
    docs-update.md
    bug-fix.md
    pr-review.md
  skills/
    docs-review/
      SKILL.md
      examples/
      templates/
  audits/
    prompt-audit.md
    public-repo-safety.md
```

This structure is generic. It does not assume a specific vendor, global config folder, or account setup.

## SKILL.md Template

```markdown
# Skill Name

## Purpose

What this skill helps with.

## Use When

- The task matches this situation.
- The repository has these files or conventions.

## Read First

- AGENTS.md
- Relevant docs or source files

## Safety Boundaries

- Do not read private folders.
- Do not edit secrets or credentials.
- Do not add dependencies without approval.
- Mark fast-changing tool behavior as "verify in official documentation."

## Steps

1. Inspect the repository state.
2. Read the relevant files.
3. Make the smallest correct change.
4. Run verification.
5. Report changed files, commands, checks, and risks.

## Examples

Add one example prompt and one expected final report.
```

## Codex Skill And Prompt Guide Workflow

Use repository prompt templates first, then move repeated patterns into a skill or local guide when the same task repeats.

Safe workflow:

1. Read the repository `AGENTS.md`.
2. Use an existing prompt template from `prompts/codex/`.
3. Run the task on a branch.
4. If the prompt works repeatedly, document it under `prompt-guides/`.
5. Verify current Codex skill, configuration, and `/goal` behavior in official documentation before teaching exact global setup.

Safe command examples:

```powershell
git status
Get-ChildItem -Path .\prompts\codex
Get-Content -Path .\prompts\codex\docs-update.goal.md
```

Do not paste API keys, tokens, or private repository URLs into prompts or commands.

## Claude Code SKILL.md-Style Workflow

Claude Code and similar tools may support skills, slash commands, or reusable instructions depending on current product behavior. Verify exact setup in official documentation before running install or configuration commands.

Safe local practice:

1. Create a repo-local `prompt-guides/skills/<skill-name>/SKILL.md`.
2. Paste the skill content into the tool as a normal prompt if skill loading is not verified.
3. Ask the tool to inspect the repo before editing.
4. Run local checks and review the diff.

Example task prompt:

```text
Use the SKILL.md-style instructions below as guidance.
Read AGENTS.md and inspect the relevant files before editing.
Do not add dependencies, secrets, private links, or workflow YAML changes.
Run the listed checks and report anything not verified.
```

## Generic Prompt Pack Clone Workflow

Use this only with public repositories you trust enough to inspect. Cloning a public prompt pack does not mean you should run its scripts.

```powershell
# Verify the repository is public and appropriate before cloning.
# Replace placeholders before use.
New-Item -ItemType Directory -Path .\vendor_imports -Force
git clone https://github.com/OWNER/PUBLIC-PROMPT-PACK.git .\vendor_imports\PUBLIC-PROMPT-PACK
Get-ChildItem -Path .\vendor_imports\PUBLIC-PROMPT-PACK
```

Review before use:

- Read the license.
- Search for install scripts.
- Search for secrets or private URLs.
- Copy only the prompts you understand.
- Keep attribution when required.

## npm And npx Placeholder Examples

These are placeholders, not recommendations for a specific package.

```powershell
# Verify this command in official docs before running.
# Replace placeholders before use.
# Do not paste secrets into commands.
npx TOOL_NAME@latest --help

# Verify this command in official docs before running.
# Avoid global installs for beginner workflows unless the tool officially recommends it.
npm view PACKAGE_NAME version
```

Do not add npm packages, lock files, or global tools to this repository unless a maintainer explicitly approves the change.

## MCP Safety Notes

MCP can connect agents to tools, data, prompts, and services. That is powerful, but it expands the trust boundary.

Start with:

- Read-only tools.
- Public docs.
- Test repositories.
- No private accounts.
- No write access.
- Clear logs of which tools were used.

Avoid at the beginner stage:

- Browser profile access.
- Cloud drive write access.
- Private repository write access.
- Payment, production, or database tools.
- Servers that can delete or overwrite files.

## Common Mistakes

| Mistake | Risk | Safer alternative |
| --- | --- | --- |
| Copying a prompt pack blindly | Hidden unsafe instructions. | Inspect every file before use. |
| Storing secrets in prompts | Public credential leak. | Use environment variables outside Git and placeholders in docs. |
| Using global setup too early | Hard to audit what the agent can see. | Start with repo-local prompt files. |
| Enabling write-capable MCP immediately | Large permission boundary. | Start read-only in a test repo. |
| Publishing exact install commands for fast-changing tools | Instructions become stale. | Say "verify in official documentation." |

## Review Checklist

- [ ] Does each guide have a clear purpose?
- [ ] Does each guide say when to use it?
- [ ] Does it list files to read first?
- [ ] Does it include safety boundaries?
- [ ] Does it avoid secrets, private links, private paths, and personal data?
- [ ] Does it avoid unverified pricing, plan, model, or platform claims?
- [ ] Does it include safe verification steps?
- [ ] Does it distinguish exact repo commands from placeholders?
- [ ] Does it say "Replace placeholders before use" where needed?
- [ ] Does it say "Do not paste secrets into commands" where needed?

## Failure Modes

| Failure mode | Signal | Recovery |
| --- | --- | --- |
| Skill applies to the wrong task | Agent uses irrelevant instructions. | Add clear "Use When" and "Do Not Use When" sections. |
| Prompt pack adds risky commands | Scripts or install commands appear. | Treat as untrusted until reviewed. |
| Tool setup command fails | Command was stale or platform-specific. | Verify official docs and update the guide conservatively. |
| MCP server exposes too much | Agent can access private data or write tools. | Disable it and restart with read-only permissions. |
| Guide becomes too long | Agent misses key constraints. | Split into focused skill files and templates. |
