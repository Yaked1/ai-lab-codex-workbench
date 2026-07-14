# GitHub Owner Settings and Ref Retirement

This document separates repository changes that can be reviewed in Git from
owner-only settings that exist only on GitHub. A committed workflow or policy
file is evidence of intent, not evidence that the corresponding live setting is
enabled. Humanity has already produced enough checklists that certify
themselves.

## Evidence rule

Treat a live setting as verified only when an owner records one of these forms
of evidence with the date, repository, and actor:

1. a screenshot of the relevant GitHub settings page;
2. saved output from a read-only GitHub CLI or REST API query; or
3. a link to a completed GitHub Actions run, ruleset, environment, or release
   page that directly demonstrates the setting.

Do not place access tokens, private email addresses, organization secrets, or
unredacted private-repository data in the evidence record.

Suggested evidence directory for a release review:

```text
docs/releases/evidence/<version>/
```

The directory is optional. Evidence may instead live in a private maintainer
record when screenshots contain account information. Public documentation must
state `not verified` rather than implying that private evidence exists.

## Owner-only verification checklist

Record `verified`, `not configured`, `not applicable`, or `not verified` for
each item. Include a date and evidence reference.

| Area | GitHub UI path | Read-only command or API evidence | Required result |
| --- | --- | --- | --- |
| Default branch | **Settings → Branches → Default branch** | `gh repo view --json defaultBranchRef` | The intended release branch is the default branch. |
| Rulesets / branch protection | **Settings → Rules → Rulesets** and **Settings → Branches** | `gh api repos/{owner}/{repo}/rulesets` and `gh api repos/{owner}/{repo}/branches/main/protection` | Direct pushes are restricted as intended; required reviews and checks match the policy below. A 404 is evidence of absence, not success. |
| Required checks | Open the active ruleset or branch-protection rule | Inspect the rule payload and recent PR checks | Repository health, safe-autofix check, unit tests, Windows runtime gate, and change-specific package/site checks are required where available. Exact check names must match current workflow job names. |
| Workflow permissions | **Settings → Actions → General → Workflow permissions** | `gh api repos/{owner}/{repo}/actions/permissions/workflow` | Default token permission is read-only unless a specific reviewed workflow needs more; pull-request approval behavior is recorded. |
| Allowed actions | **Settings → Actions → General → Actions permissions** | `gh api repos/{owner}/{repo}/actions/permissions` | The allow policy matches the pinned actions used by this repository. |
| Fork pull-request approval | **Settings → Actions → General → Fork pull request workflows** | Record UI evidence; API coverage may vary | The approval boundary is deliberate and documented, especially for workflows with elevated events. |
| Environments | **Settings → Environments** | `gh api repos/{owner}/{repo}/environments` | Any publishing environment has the intended reviewers, branch/tag restrictions, and no undocumented secret dependency. |
| Pages | **Settings → Pages** | `gh api repos/{owner}/{repo}/pages` | Source, custom domain, HTTPS status, and deployment branch/workflow are recorded. A missing Pages site is stated plainly. |
| Discussions | **Settings → General → Features** | `gh repo view --json hasDiscussionsEnabled` | Enabled or disabled deliberately; README links must match reality. |
| Issues and templates | **Settings → General → Features**, then create-issue UI | `gh repo view --json hasIssuesEnabled` | Issues are enabled if contribution docs send users there; all committed forms render successfully. |
| Security features | **Settings → Security & analysis** | `gh api repos/{owner}/{repo}` plus the relevant security endpoints available to the owner | Dependabot, secret scanning, push protection, and private vulnerability reporting are recorded as enabled, unavailable, or intentionally disabled. |
| Tag protection / release rules | **Settings → Rules → Rulesets** | Inspect ruleset payload for tag targets | Release tags cannot be moved or deleted casually; bypass actors are explicit. |
| Repository visibility and metadata | **Settings → General** and repository **About** panel | `gh repo view --json visibility,description,homepageUrl,repositoryTopics` | Visibility, description, homepage, topics, and license presentation match the public positioning. |
| Merge methods and deletion | **Settings → General → Pull Requests** | `gh repo view --json mergeCommitAllowed,squashMergeAllowed,rebaseMergeAllowed,deleteBranchOnMerge` | Allowed merge methods and branch deletion behavior match maintainer practice. |
| Release state | Repository **Releases** page | `gh release list` and `gh release view <tag> --json ...` | Tag, target commit, notes, prerelease state, assets, and checksums are consistent. |
| Traffic and adoption | **Insights → Traffic**, **Insights → Community Standards** | Owner-visible UI evidence; public counters are insufficient | Record the review date. Never freeze volatile counts into evergreen guidance. |

Replace `{owner}` and `{repo}` with the actual repository coordinates. Commands
are read-only unless GitHub itself changes an endpoint's semantics; review the
command before running it rather than treating a code fence as divine law.

## Required protection intent

The repository files establish this intended boundary:

- changes reach the default branch through reviewed pull requests;
- write-capable workflows are narrowly scoped and use trusted control files;
- required checks cannot be satisfied by a modified checker from the proposed
  branch when the workflow claims a trusted validation boundary;
- release publication remains a manual owner action;
- generated research uses a unique per-run branch and pull request;
- branch names do not grant bypass rights;
- administrator or ruleset bypass actors are few, named, and reviewed.

These bullets are not proof that GitHub enforces them. Record live evidence in
an owner review before a release claims protected-branch or protected-tag
status.

## Ref disposition ledger

The July 13, 2026 repository audit identified the following historical refs.
This table records intended disposition only. It does **not** authorize an
agent, script, or release job to delete a local or remote ref.

| Ref | Observed audit SHA | Disposition | Owner verification before action |
| --- | --- | --- | --- |
| `main` / `origin/main` / `origin/HEAD` | `6d533fd` | Keep | Confirm the current default branch and remote target; the SHA is historical, not a current-state claim. |
| `agent/finish-skill-pack-v1` and remote counterpart | `f8022b5` | Delete after verification | Confirm no open PR, no unique behavior missing from the 125-skill system, and no external release/reference dependency. |
| `agent/repo-maintenance` remote-tracking ref | `ca1e26c` | Prune stale tracking data after verification | Confirm the remote branch is absent and run a fetch/prune preview before removing only the stale tracking ref. |
| `claude/fix-deploy-public-readme-autopilot` and remote counterpart | local `2b415fa`, remote `ceaab5a` | Delete after verification | Confirm merged or patch-equivalent status, no open PR, and no attached worktree. |
| `cleanup/root-junk-health-check` | `0439dda` | Retire only after worktree inspection | List worktrees and confirm the attached worktree is clean, closed, or intentionally preserved. |
| `cleanup/strip-research-grade-expansion` and remote counterpart | `f42f62b` | Preserve as historical reference until replay is verified, then archive or delete | Confirm current-main cleanup and regression tests supersede the branch; do not merge it wholesale. |
| `cleanup/thin-front-deep-back` remote counterpart | `e84b8ed` | Delete after verification | Confirm patch-equivalent status and no live PR or dependent documentation. |
| `codex/curate-hermes-agent-guides` | `6462777` | Delete local after verification | Confirm fully merged and not attached to another worktree. |
| `codex/dry-run-hermes-agent-curation` | `8f60df7` | Delete local after verification | Confirm fully merged and not attached to another worktree. |
| `autopilot/generated-research-updates` remote counterpart | `4295bd9` | Stop reusing; retain temporarily only for audit, then retire after accepted work is preserved | Confirm every accepted generated change exists on the default branch or a reviewed PR. Future runs must use unique `autopilot/<run-id>` branches. |

### Non-destructive inspection commands

Run these before any retirement decision:

```powershell
git status --short --branch
git worktree list --porcelain
git branch --all --verbose --no-abbrev
git branch --merged main
git branch --no-merged main
git ls-remote --heads origin
gh pr list --state all --limit 200 --json number,title,state,headRefName,baseRefName,url
```

Use `git fetch --prune --dry-run origin` when supported by the installed Git
version to preview stale remote-tracking cleanup. A branch deletion is a
separate owner-approved operation and is intentionally absent from this
runbook.

## Release-readiness record

Before triggering `.github/workflows/release-package.yml`, record:

- the release tag and target commit;
- a clean committed tree used for the package build;
- local and CI verification results;
- the ZIP and manifest SHA-256 values;
- completed release notes and changelog entry;
- live default-branch, ruleset/protection, Actions-permission, environment, and
  tag-protection status, each with evidence or `not verified`;
- ref cleanup decisions, with no destructive action hidden inside release work;
- a dated review of model availability, pricing, benchmark, and platform claims
  included in the release; and
- any owner-only uncertainty that remains.

A release may proceed with a documented `not verified` item only when the owner
accepts the risk and the public notes do not falsely claim the missing control.

## Dated-claim policy

Model menus, limits, pricing, benchmarks, GitHub features, public counters, and
repository settings are volatile. For each such claim:

1. attach an `as of YYYY-MM-DD` date;
2. prefer first-party evidence for product behavior and settings;
3. distinguish official facts, vendor claims, independent measurements, and
   local observations;
4. keep unresolved conflicts explicit; and
5. re-verify before a release, purchase, deployment, or access decision.

A recent edit timestamp does not make an old claim current. It merely proves
someone touched the file, a distinction software projects repeatedly discover
at inconvenient moments.
