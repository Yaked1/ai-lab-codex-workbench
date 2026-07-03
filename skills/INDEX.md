# Skill Index

This index lists every installable skill bundle currently shipped in
`skills/`. The source of truth for installer automation is
[`manifest.json`](manifest.json); this page is the human-readable companion.

Total skills: 125.

| Skill | Category | What it helps with | Source |
| --- | --- | --- | --- |
| `use-codex-safely` | tools | Safe first-task workflow for OpenAI Codex sessions in this repository: read local rules, scope the task, run checks, open a reviewable PR. | `docs/tools/codex.md`, `docs/codex/00-start-here.md`, `docs/codex/01-codex-goal-workflow.md`, `AGENTS.md` |
| `self-directed-goal-runner` | meta | Turn a broad multi-step goal into a bounded, checklist-driven self-prompt and follow it to completion with hard stop conditions and an iteration cap. | `docs/templates/task-spec.md`, `AGENTS.md`, `docs/skills/README.md` |
| `create-a-new-skill` | meta | Author a new prompting skill bundle in this repository's skills/ package from a recurring task or an existing doc/prompt template. | `docs/skills/README.md`, `skills/README.md`, `skills/use-codex-safely/SKILL.md` |
| `install-this-skill-pack` | meta | Give the exact command to install a skill from this repository into Codex, Claude Code, Hermes, or another agent harness. | `skills/README.md`, `scripts/install_skill.ps1`, `scripts/install_skill.py` |
| `guide-archive-audit` | guides | Use the Archive Audit: GitHub_Downloads guide from docs/archive-audit.md as a bounded, public-safe workflow. | `docs/archive-audit.md` |
| `guide-archive-catalog` | guides | Use the Archived GitHub Downloads Catalog guide from docs/archive-catalog.md as a bounded, public-safe workflow. | `docs/archive-catalog.md` |
| `guide-automation-local-autopilot` | guides | Use the Local Autopilot guide from docs/automation/local-autopilot.md as a bounded, public-safe workflow. | `docs/automation/local-autopilot.md` |
| `guide-automation-release-draft-policy` | guides | Use the Release Draft Policy guide from docs/automation/release-draft-policy.md as a bounded, public-safe workflow. | `docs/automation/release-draft-policy.md` |
| `guide-automation-repository-autopilot` | guides | Use the Repository Autopilot guide from docs/automation/repository-autopilot.md as a bounded, public-safe workflow. | `docs/automation/repository-autopilot.md` |
| `guide-automation-safe-automerge-policy` | guides | Use the Safe Automerge Policy guide from docs/automation/safe-automerge-policy.md as a bounded, public-safe workflow. | `docs/automation/safe-automerge-policy.md` |
| `guide-codex-00-start-here` | codex-workflow | Use the Start Here guide from docs/codex/00-start-here.md as a bounded, public-safe workflow. | `docs/codex/00-start-here.md` |
| `guide-codex-01-codex-goal-workflow` | codex-workflow | Use the Codex Goal Workflow guide from docs/codex/01-codex-goal-workflow.md as a bounded, public-safe workflow. | `docs/codex/01-codex-goal-workflow.md` |
| `guide-codex-02-git-branch-pr-merge-workflow` | codex-workflow | Use the Git Branch, Pull Request, and Merge Workflow guide from docs/codex/02-git-branch-pr-merge-workflow.md as a bounded, public-safe workflow. | `docs/codex/02-git-branch-pr-merge-workflow.md` |
| `guide-codex-03-safe-autofix-policy` | codex-workflow | Use the Safe Autofix Policy guide from docs/codex/03-safe-autofix-policy.md as a bounded, public-safe workflow. | `docs/codex/03-safe-autofix-policy.md` |
| `guide-codex-04-review-checklist` | codex-workflow | Use the Review Checklist guide from docs/codex/04-review-checklist.md as a bounded, public-safe workflow. | `docs/codex/04-review-checklist.md` |
| `guide-codex-05-repository-roadmap` | codex-workflow | Use the Repository Roadmap guide from docs/codex/05-repository-roadmap.md as a bounded, public-safe workflow. | `docs/codex/05-repository-roadmap.md` |
| `guide-guides-readme` | guides | Use the Guides guide from docs/guides/README.md as a bounded, public-safe workflow. | `docs/guides/README.md` |
| `guide-guides-agentic-coding-playbook` | guides | Use the Agentic Coding Playbook guide from docs/guides/agentic-coding-playbook.md as a bounded, public-safe workflow. | `docs/guides/agentic-coding-playbook.md` |
| `guide-guides-coding-agent-power-tips` | guides | Use the Coding Agent Power Tips guide from docs/guides/coding-agent-power-tips.md as a bounded, public-safe workflow. | `docs/guides/coding-agent-power-tips.md` |
| `guide-guides-comprehensive-prompt-engineering-guide` | guides | Use the Comprehensive Prompt Engineering Guide guide from docs/guides/comprehensive-prompt-engineering-guide.md as a bounded, public-safe workflow. | `docs/guides/comprehensive-prompt-engineering-guide.md` |
| `guide-guides-prompt-audit-checklist` | guides | Use the Prompt Audit Checklist guide from docs/guides/prompt-audit-checklist.md as a bounded, public-safe workflow. | `docs/guides/prompt-audit-checklist.md` |
| `guide-guides-prompt-engineering-playbook` | guides | Use the Prompt Engineering Playbook guide from docs/guides/prompt-engineering-playbook.md as a bounded, public-safe workflow. | `docs/guides/prompt-engineering-playbook.md` |
| `guide-guides-prompting-ai-coding-agents` | guides | Use the Prompting AI Coding Agents guide from docs/guides/prompting-ai-coding-agents.md as a bounded, public-safe workflow. | `docs/guides/prompting-ai-coding-agents.md` |
| `guide-guides-prompting-references` | guides | Use the Prompting References guide from docs/guides/prompting-references.md as a bounded, public-safe workflow. | `docs/guides/prompting-references.md` |
| `guide-guides-skills-and-prompt-guides` | guides | Use the Skills And Prompt Guides guide from docs/guides/skills-and-prompt-guides.md as a bounded, public-safe workflow. | `docs/guides/skills-and-prompt-guides.md` |
| `guide-guides-source-inspired-prompting-curriculum` | guides | Use the Source-Inspired Prompting Curriculum guide from docs/guides/source-inspired-prompting-curriculum.md as a bounded, public-safe workflow. | `docs/guides/source-inspired-prompting-curriculum.md` |
| `guide-guides-windows-setup-commands` | guides | Use the Windows Setup Commands guide from docs/guides/windows-setup-commands.md as a bounded, public-safe workflow. | `docs/guides/windows-setup-commands.md` |
| `guide-hermes-readme` | hermes | Use the Hermes Agent Guides guide from docs/hermes/README.md as a bounded, public-safe workflow. | `docs/hermes/README.md` |
| `guide-hermes-hermes-agent-vs-codex-vs-claude-code` | hermes | Use the Hermes Agent Vs Codex Vs Claude Code guide from docs/hermes/hermes-agent-vs-codex-vs-claude-code.md as a bounded, public-safe workflow. | `docs/hermes/hermes-agent-vs-codex-vs-claude-code.md` |
| `guide-hermes-hermes-agent` | hermes | Use the Nous Research Hermes Agent guide from docs/hermes/hermes-agent.md as a bounded, public-safe workflow. | `docs/hermes/hermes-agent.md` |
| `guide-hermes-local-agent-setup` | hermes | Use the Hermes Agent Local Setup guide from docs/hermes/local-agent-setup.md as a bounded, public-safe workflow. | `docs/hermes/local-agent-setup.md` |
| `guide-hermes-prompting-hermes-agent` | hermes | Use the Prompting Hermes Agent guide from docs/hermes/prompting-hermes-agent.md as a bounded, public-safe workflow. | `docs/hermes/prompting-hermes-agent.md` |
| `guide-hermes-provider-configuration` | hermes | Use the Hermes Agent Provider Configuration guide from docs/hermes/provider-configuration.md as a bounded, public-safe workflow. | `docs/hermes/provider-configuration.md` |
| `guide-hermes-public-repo-safety` | hermes | Use the Hermes Agent Public Repository Safety guide from docs/hermes/public-repo-safety.md as a bounded, public-safe workflow. | `docs/hermes/public-repo-safety.md` |
| `guide-hermes-skills-memory-automations` | hermes | Use the Hermes Agent Skills, Memory, And Automations guide from docs/hermes/skills-memory-automations.md as a bounded, public-safe workflow. | `docs/hermes/skills-memory-automations.md` |
| `guide-hermes-troubleshooting` | hermes | Use the Hermes Agent Troubleshooting guide from docs/hermes/troubleshooting.md as a bounded, public-safe workflow. | `docs/hermes/troubleshooting.md` |
| `guide-image-generation-readme` | image-generation | Use the Image Generation Guides guide from docs/image-generation/README.md as a bounded, public-safe workflow. | `docs/image-generation/README.md` |
| `guide-image-generation-autoregressive-image-models` | image-generation | Use the Autoregressive Image Models guide from docs/image-generation/autoregressive-image-models.md as a bounded, public-safe workflow. | `docs/image-generation/autoregressive-image-models.md` |
| `guide-image-generation-diffusion-models` | image-generation | Use the Diffusion Models guide from docs/image-generation/diffusion-models.md as a bounded, public-safe workflow. | `docs/image-generation/diffusion-models.md` |
| `guide-image-generation-hardware-requirements` | image-generation | Use the Image Generation Hardware Requirements guide from docs/image-generation/hardware-requirements.md as a bounded, public-safe workflow. | `docs/image-generation/hardware-requirements.md` |
| `guide-image-generation-local-image-generation` | image-generation | Use the Local Image Generation guide from docs/image-generation/local-image-generation.md as a bounded, public-safe workflow. | `docs/image-generation/local-image-generation.md` |
| `guide-image-generation-prompting-patterns` | image-generation | Use the Image Prompting Patterns guide from docs/image-generation/prompting-patterns.md as a bounded, public-safe workflow. | `docs/image-generation/prompting-patterns.md` |
| `guide-image-generation-reasoning-integrated-image-generation` | image-generation | Use the Reasoning-Integrated Image Generation guide from docs/image-generation/reasoning-integrated-image-generation.md as a bounded, public-safe workflow. | `docs/image-generation/reasoning-integrated-image-generation.md` |
| `guide-image-generation-transformer-architecture` | image-generation | Use the Transformer Architecture In Image Generation guide from docs/image-generation/transformer-architecture.md as a bounded, public-safe workflow. | `docs/image-generation/transformer-architecture.md` |
| `guide-prompting-os-01-kernel` | guides | Use the Prompting OS Kernel guide from docs/prompting-os/01-kernel.md as a bounded, public-safe workflow. | `docs/prompting-os/01-kernel.md` |
| `guide-prompting-os-02-model-family-drivers` | guides | Use the Model Family Drivers guide from docs/prompting-os/02-model-family-drivers.md as a bounded, public-safe workflow. | `docs/prompting-os/02-model-family-drivers.md` |
| `guide-prompting-os-03-context-engineering` | guides | Use the Context Engineering and RAG guide from docs/prompting-os/03-context-engineering.md as a bounded, public-safe workflow. | `docs/prompting-os/03-context-engineering.md` |
| `guide-prompting-os-04-agent-skills` | guides | Use the Agent and Skill System guide from docs/prompting-os/04-agent-skills.md as a bounded, public-safe workflow. | `docs/prompting-os/04-agent-skills.md` |
| `guide-prompting-os-05-image-prompting-engine` | guides | Use the Image Prompting Engine guide from docs/prompting-os/05-image-prompting-engine.md as a bounded, public-safe workflow. | `docs/prompting-os/05-image-prompting-engine.md` |
| `guide-prompting-os-06-evaluation-and-optimization` | guides | Use the Evaluation and Optimization guide from docs/prompting-os/06-evaluation-and-optimization.md as a bounded, public-safe workflow. | `docs/prompting-os/06-evaluation-and-optimization.md` |
| `guide-prompting-os-07-source-map` | guides | Use the Source Map and Synthesis guide from docs/prompting-os/07-source-map.md as a bounded, public-safe workflow. | `docs/prompting-os/07-source-map.md` |
| `guide-prompting-os-08-production-prompt-architecture` | guides | Use the Production Prompt Architecture guide from docs/prompting-os/08-production-prompt-architecture.md as a bounded, public-safe workflow. | `docs/prompting-os/08-production-prompt-architecture.md` |
| `guide-prompting-os-09-security-and-governance` | guides | Use the Prompt Security and Governance guide from docs/prompting-os/09-security-and-governance.md as a bounded, public-safe workflow. | `docs/prompting-os/09-security-and-governance.md` |
| `guide-prompting-os-10-evaluation-cookbook` | guides | Use the Prompt Evaluation Cookbook guide from docs/prompting-os/10-evaluation-cookbook.md as a bounded, public-safe workflow. | `docs/prompting-os/10-evaluation-cookbook.md` |
| `guide-prompting-os-11-comprehensiveness-benchmark` | guides | Use the Comprehensiveness Benchmark guide from docs/prompting-os/11-comprehensiveness-benchmark.md as a bounded, public-safe workflow. | `docs/prompting-os/11-comprehensiveness-benchmark.md` |
| `guide-prompting-os-12-prompt-pattern-library` | guides | Use the Prompt Pattern Library guide from docs/prompting-os/12-prompt-pattern-library.md as a bounded, public-safe workflow. | `docs/prompting-os/12-prompt-pattern-library.md` |
| `guide-prompting-os-13-agent-operations-manual` | guides | Use the Agent Operations Manual guide from docs/prompting-os/13-agent-operations-manual.md as a bounded, public-safe workflow. | `docs/prompting-os/13-agent-operations-manual.md` |
| `guide-prompting-os-14-rag-and-tool-use-field-guide` | guides | Use the RAG And Tool Use Field Guide guide from docs/prompting-os/14-rag-and-tool-use-field-guide.md as a bounded, public-safe workflow. | `docs/prompting-os/14-rag-and-tool-use-field-guide.md` |
| `guide-prompting-os-15-maintenance-and-release-manual` | guides | Use the Maintenance And Release Manual guide from docs/prompting-os/15-maintenance-and-release-manual.md as a bounded, public-safe workflow. | `docs/prompting-os/15-maintenance-and-release-manual.md` |
| `guide-prompting-os-16-comprehensive-examples` | guides | Use the Comprehensive Examples guide from docs/prompting-os/16-comprehensive-examples.md as a bounded, public-safe workflow. | `docs/prompting-os/16-comprehensive-examples.md` |
| `guide-prompting-os-17-curriculum-and-workshops` | guides | Use the Curriculum And Workshops guide from docs/prompting-os/17-curriculum-and-workshops.md as a bounded, public-safe workflow. | `docs/prompting-os/17-curriculum-and-workshops.md` |
| `guide-prompting-os-18-troubleshooting-and-debugging` | guides | Use the Troubleshooting And Debugging guide from docs/prompting-os/18-troubleshooting-and-debugging.md as a bounded, public-safe workflow. | `docs/prompting-os/18-troubleshooting-and-debugging.md` |
| `guide-prompting-os-19-model-specific-adaptation` | guides | Use the Model-Specific Adaptation guide from docs/prompting-os/19-model-specific-adaptation.md as a bounded, public-safe workflow. | `docs/prompting-os/19-model-specific-adaptation.md` |
| `guide-prompting-os-20-prompt-library-governance` | guides | Use the Prompt Library Governance guide from docs/prompting-os/20-prompt-library-governance.md as a bounded, public-safe workflow. | `docs/prompting-os/20-prompt-library-governance.md` |
| `guide-prompting-os-21-checklists-and-templates` | guides | Use the Checklists And Templates guide from docs/prompting-os/21-checklists-and-templates.md as a bounded, public-safe workflow. | `docs/prompting-os/21-checklists-and-templates.md` |
| `guide-prompting-os-22-risk-register` | guides | Use the Risk Register guide from docs/prompting-os/22-risk-register.md as a bounded, public-safe workflow. | `docs/prompting-os/22-risk-register.md` |
| `guide-prompting-os-23-quality-assurance-matrix` | guides | Use the Quality Assurance Matrix guide from docs/prompting-os/23-quality-assurance-matrix.md as a bounded, public-safe workflow. | `docs/prompting-os/23-quality-assurance-matrix.md` |
| `guide-prompting-os-24-archive-corpus-source-map` | guides | Use the Archive Corpus Source Map guide from docs/prompting-os/24-archive-corpus-source-map.md as a bounded, public-safe workflow. | `docs/prompting-os/24-archive-corpus-source-map.md` |
| `guide-prompting-os-25-repository-expansion-playbook` | guides | Use the Repository Expansion Playbook guide from docs/prompting-os/25-repository-expansion-playbook.md as a bounded, public-safe workflow. | `docs/prompting-os/25-repository-expansion-playbook.md` |
| `guide-prompting-os-26-offline-package-reader-guide` | guides | Use the Offline Package Reader Guide guide from docs/prompting-os/26-offline-package-reader-guide.md as a bounded, public-safe workflow. | `docs/prompting-os/26-offline-package-reader-guide.md` |
| `guide-prompting-os-27-prompt-evaluation-datasets` | guides | Use the Prompt Evaluation Datasets guide from docs/prompting-os/27-prompt-evaluation-datasets.md as a bounded, public-safe workflow. | `docs/prompting-os/27-prompt-evaluation-datasets.md` |
| `guide-prompting-os-28-tool-permission-model` | guides | Use the Tool Permission Model guide from docs/prompting-os/28-tool-permission-model.md as a bounded, public-safe workflow. | `docs/prompting-os/28-tool-permission-model.md` |
| `guide-prompting-os-29-source-grounded-writing-lab` | guides | Use the Source-Grounded Writing Lab guide from docs/prompting-os/29-source-grounded-writing-lab.md as a bounded, public-safe workflow. | `docs/prompting-os/29-source-grounded-writing-lab.md` |
| `guide-prompting-os-30-agent-review-and-red-team` | guides | Use the Agent Review And Red Team guide from docs/prompting-os/30-agent-review-and-red-team.md as a bounded, public-safe workflow. | `docs/prompting-os/30-agent-review-and-red-team.md` |
| `guide-prompting-os-31-workbench-maintainer-runbook` | guides | Use the Workbench Maintainer Runbook guide from docs/prompting-os/31-workbench-maintainer-runbook.md as a bounded, public-safe workflow. | `docs/prompting-os/31-workbench-maintainer-runbook.md` |
| `guide-prompting-os-32-completion-evidence-manual` | guides | Use the Completion Evidence Manual guide from docs/prompting-os/32-completion-evidence-manual.md as a bounded, public-safe workflow. | `docs/prompting-os/32-completion-evidence-manual.md` |
| `guide-prompting-os-33-prompt-library-indexing` | guides | Use the Prompt Library Indexing guide from docs/prompting-os/33-prompt-library-indexing.md as a bounded, public-safe workflow. | `docs/prompting-os/33-prompt-library-indexing.md` |
| `guide-prompting-os-34-static-site-and-release-docs` | guides | Use the Static Site And Release Docs guide from docs/prompting-os/34-static-site-and-release-docs.md as a bounded, public-safe workflow. | `docs/prompting-os/34-static-site-and-release-docs.md` |
| `guide-prompting-os-35-workshop-assessment-bank` | guides | Use the Workshop Assessment Bank guide from docs/prompting-os/35-workshop-assessment-bank.md as a bounded, public-safe workflow. | `docs/prompting-os/35-workshop-assessment-bank.md` |
| `guide-prompting-os-36-prompt-metrics-and-telemetry` | guides | Use the Prompt Metrics And Telemetry guide from docs/prompting-os/36-prompt-metrics-and-telemetry.md as a bounded, public-safe workflow. | `docs/prompting-os/36-prompt-metrics-and-telemetry.md` |
| `guide-prompting-os-37-failure-mode-catalog` | guides | Use the Failure Mode Catalog guide from docs/prompting-os/37-failure-mode-catalog.md as a bounded, public-safe workflow. | `docs/prompting-os/37-failure-mode-catalog.md` |
| `guide-prompting-os-readme` | guides | Use the Prompting OS guide from docs/prompting-os/README.md as a bounded, public-safe workflow. | `docs/prompting-os/README.md` |
| `guide-prompting-os-evals-prompt-quality-rubric` | guides | Use the Prompt Quality Rubric guide from docs/prompting-os/evals/prompt-quality-rubric.md as a bounded, public-safe workflow. | `docs/prompting-os/evals/prompt-quality-rubric.md` |
| `guide-prompting-os-templates-master-prompt-template` | guides | Use the Master Prompt Template guide from docs/prompting-os/templates/master-prompt-template.md as a bounded, public-safe workflow. | `docs/prompting-os/templates/master-prompt-template.md` |
| `guide-publication-policy` | guides | Use the Publication Policy guide from docs/publication-policy.md as a bounded, public-safe workflow. | `docs/publication-policy.md` |
| `guide-releases-and-packages` | guides | Use the Releases And Packages guide from docs/releases-and-packages.md as a bounded, public-safe workflow. | `docs/releases-and-packages.md` |
| `guide-releases-release-process` | guides | Use the Release Process guide from docs/releases/release-process.md as a bounded, public-safe workflow. | `docs/releases/release-process.md` |
| `guide-releases-v0-1-0` | guides | Use the AI Agent Coding Workbench v0.1.0 guide from docs/releases/v0.1.0.md as a bounded, public-safe workflow. | `docs/releases/v0.1.0.md` |
| `guide-research-curated-curator-prompt-2026-06-29` | guides | Use the Local Codex Curator Prompt - 2026-06-29 guide from docs/research/curated/curator-prompt-2026-06-29.md as a bounded, public-safe workflow. | `docs/research/curated/curator-prompt-2026-06-29.md` |
| `guide-research-inbox-2026-06-29` | guides | Use the Daily AI Skills And Prompt Guide Candidates - 2026-06-29 guide from docs/research/inbox/2026-06-29.md as a bounded, public-safe workflow. | `docs/research/inbox/2026-06-29.md` |
| `guide-research-inbox-2026-07-01` | guides | Use the Daily AI Skills And Prompt Guide Candidates - 2026-07-01 guide from docs/research/inbox/2026-07-01.md as a bounded, public-safe workflow. | `docs/research/inbox/2026-07-01.md` |
| `guide-research-source-policy` | guides | Use the Research Source Policy guide from docs/research/source-policy.md as a bounded, public-safe workflow. | `docs/research/source-policy.md` |
| `guide-skills-readme` | guides | Use the AI Skills And Prompt Guides guide from docs/skills/README.md as a bounded, public-safe workflow. | `docs/skills/README.md` |
| `guide-skills-claude-code` | guides | Use the Claude Code Skills guide from docs/skills/claude-code.md as a bounded, public-safe workflow. | `docs/skills/claude-code.md` |
| `guide-skills-codex` | guides | Use the Codex Skills guide from docs/skills/codex.md as a bounded, public-safe workflow. | `docs/skills/codex.md` |
| `guide-skills-mcp` | guides | Use the MCP Tool-Use Systems guide from docs/skills/mcp.md as a bounded, public-safe workflow. | `docs/skills/mcp.md` |
| `guide-skills-prompt-guides` | guides | Use the Prompt Guides guide from docs/skills/prompt-guides.md as a bounded, public-safe workflow. | `docs/skills/prompt-guides.md` |
| `guide-templates-merge-report` | guides | Use the Merge Report guide from docs/templates/merge-report.md as a bounded, public-safe workflow. | `docs/templates/merge-report.md` |
| `guide-templates-release-notes` | guides | Use the Release Notes Template guide from docs/templates/release-notes.md as a bounded, public-safe workflow. | `docs/templates/release-notes.md` |
| `guide-templates-task-spec` | guides | Use the Task Spec guide from docs/templates/task-spec.md as a bounded, public-safe workflow. | `docs/templates/task-spec.md` |
| `guide-tools-aider` | tools | Use the Aider guide from docs/tools/aider.md as a bounded, public-safe workflow. | `docs/tools/aider.md` |
| `guide-tools-antigravity` | tools | Use the Google Antigravity guide from docs/tools/antigravity.md as a bounded, public-safe workflow. | `docs/tools/antigravity.md` |
| `guide-tools-claude-code` | tools | Use the Claude Code guide from docs/tools/claude-code.md as a bounded, public-safe workflow. | `docs/tools/claude-code.md` |
| `guide-tools-codex` | tools | Use the OpenAI Codex guide from docs/tools/codex.md as a bounded, public-safe workflow. | `docs/tools/codex.md` |
| `guide-tools-comparison-matrix` | tools | Use the AI Coding Tool Comparison Matrix guide from docs/tools/comparison-matrix.md as a bounded, public-safe workflow. | `docs/tools/comparison-matrix.md` |
| `guide-tools-cursor` | tools | Use the Cursor guide from docs/tools/cursor.md as a bounded, public-safe workflow. | `docs/tools/cursor.md` |
| `guide-tools-github-copilot` | tools | Use the GitHub Copilot and Copilot Coding Agent guide from docs/tools/github-copilot.md as a bounded, public-safe workflow. | `docs/tools/github-copilot.md` |
| `guide-tools-kilo-code` | tools | Use the Kilo Code guide from docs/tools/kilo-code.md as a bounded, public-safe workflow. | `docs/tools/kilo-code.md` |
| `guide-tools-mcp` | tools | Use the MCP Servers guide from docs/tools/mcp.md as a bounded, public-safe workflow. | `docs/tools/mcp.md` |
| `guide-tools-opencode` | tools | Use the OpenCode guide from docs/tools/opencode.md as a bounded, public-safe workflow. | `docs/tools/opencode.md` |
| `guide-tools-windsurf` | tools | Use the Windsurf guide from docs/tools/windsurf.md as a bounded, public-safe workflow. | `docs/tools/windsurf.md` |
| `guide-workflows-agent-task-lifecycle` | guides | Use the Agent Task Lifecycle guide from docs/workflows/agent-task-lifecycle.md as a bounded, public-safe workflow. | `docs/workflows/agent-task-lifecycle.md` |
| `guide-workflows-public-repo-safety` | guides | Use the Public Repository Safety guide from docs/workflows/public-repo-safety.md as a bounded, public-safe workflow. | `docs/workflows/public-repo-safety.md` |
| `prompt-aider-agent-task` | prompts | Adapt the Aider Agent Task Template prompt template from prompts/aider/agent-task.md with scope, safety, and verification intact. | `prompts/aider/agent-task.md` |
| `prompt-antigravity-agent-task` | prompts | Adapt the Google Antigravity Agent Task Template prompt template from prompts/antigravity/agent-task.md with scope, safety, and verification intact. | `prompts/antigravity/agent-task.md` |
| `prompt-claude-code-review-docs-goal` | prompts | Adapt the Claude Code Goal: Review Documentation prompt template from prompts/claude-code/review-docs.goal.md with scope, safety, and verification intact. | `prompts/claude-code/review-docs.goal.md` |
| `prompt-codex-docs-update-goal` | prompts | Adapt the Codex Prompt: Documentation Update prompt template from prompts/codex/docs-update.goal.md with scope, safety, and verification intact. | `prompts/codex/docs-update.goal.md` |
| `prompt-codex-fix-bug-goal` | prompts | Adapt the Codex Prompt: Fix Bug prompt template from prompts/codex/fix-bug.goal.md with scope, safety, and verification intact. | `prompts/codex/fix-bug.goal.md` |
| `prompt-codex-implement-feature-goal` | prompts | Adapt the Codex Prompt: Implement Feature prompt template from prompts/codex/implement-feature.goal.md with scope, safety, and verification intact. | `prompts/codex/implement-feature.goal.md` |
| `prompt-codex-repository-cleanup-goal` | prompts | Adapt the Codex Prompt: Repository Cleanup prompt template from prompts/codex/repository-cleanup.goal.md with scope, safety, and verification intact. | `prompts/codex/repository-cleanup.goal.md` |
| `prompt-codex-review-pr-goal` | prompts | Adapt the Codex Prompt: Review Pull Request prompt template from prompts/codex/review-pr.goal.md with scope, safety, and verification intact. | `prompts/codex/review-pr.goal.md` |
| `prompt-cursor-agent-task` | prompts | Adapt the Cursor Agent Task Template prompt template from prompts/cursor/agent-task.md with scope, safety, and verification intact. | `prompts/cursor/agent-task.md` |
| `prompt-github-copilot-agent-task` | prompts | Adapt the GitHub Copilot Agent Task Template prompt template from prompts/github-copilot/agent-task.md with scope, safety, and verification intact. | `prompts/github-copilot/agent-task.md` |
| `prompt-opencode-agent-task` | prompts | Adapt the OpenCode Agent Task Template prompt template from prompts/opencode/agent-task.md with scope, safety, and verification intact. | `prompts/opencode/agent-task.md` |
| `prompt-windsurf-agent-task` | prompts | Adapt the Windsurf Agent Task Template prompt template from prompts/windsurf/agent-task.md with scope, safety, and verification intact. | `prompts/windsurf/agent-task.md` |

## Maintenance

When a skill is added or removed, update this index and
[`manifest.json`](manifest.json) in the same change. The test suite checks
that every manifest entry has a matching folder and that every listed source
path exists.
