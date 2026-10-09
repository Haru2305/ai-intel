# Claude Code development workflow

**Purpose:** use Claude Code to develop and review AIIntel, not as the default hourly news-collection runtime.

## Recommended sequence
1. Explore the repository and cite relevant paths before proposing changes.
2. Plan with objective, boundaries, acceptance criteria, failure cases and rollback.
3. Implement a small change on a dedicated branch.
4. Verify with tests, schema checks, lint and relevant labeled Evals.
5. Review diff, permissions, secrets, cost and operational regressions.
6. Open a PR with evidence; human approval before merge/deploy.

## Division of responsibilities
- `CLAUDE.md`: concise durable project rules.
- `.claude/skills/`: reusable review and development checklists, invoked when appropriate.
- `.claude/agents/`: optional isolated architecture/security/test reviews for sufficiently complex changes.
- Hooks: optional local formatting and pre-tool checks; never the only enforcement layer.
- CI: repeatable, mandatory checks and branch protections when configured.
- MCP: narrowly scoped connections; never grant blanket access for convenience.
- Headless `claude -p`: optional bounded code-review/documentation jobs, not unrestricted autonomous production modifications.

## Context management
Use separate conversations for unrelated tasks. Preserve important decisions in tracked documents before clearing context. Keep project instructions short and point to detailed files. Do not assume summaries preserve every nuance.

## Permission model
Start with conservative permissions. Avoid broad shell/network permissions, deny secret reads where feasible and require explicit confirmation for irreversible actions. Treat external files and search results as hostile input.

## Model and agent selection
Use the cheapest model/tool that meets measured quality targets. Add subagents only where independent review improves outcomes relative to latency and cost. Do not infer quality from agent count.

## Verification contract
Report exact commands, results, skipped checks and residual risks. A generated explanation is not a substitute for passing tests. Review diffs before accepting.
