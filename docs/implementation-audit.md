# Implementation audit — 2026-10-09

**Scope:** GitHub connector inspection of default branch and known paths; not a complete recursive tree or live infrastructure audit. **Status:** preliminary evidence-based inventory.

## Confirmed in repository
- `README.md`: two-radar architecture, Daily Curator, Weekly Analyst, optional bounded Jev, reliability gate and cadence design.
- `schemas/candidate.schema.json`, `schemas/intel.schema.json`: JSON Schema 2020-12 contracts with provenance/score fields; `schemas/item.schema.json` is legacy.
- `prompts/practitioner-radar.md`, `prompts/daily-curator.md`, `prompts/weekly-analyst.md`: agent instructions, not executable jobs.
- `config/sources.yaml`, `config/interests.yaml`: source categories and personalized scoring.
- `docs/engineering-standards.md`: operational and Eval policy; explicitly does not claim deployment.
- Draft PR #2 proposes product vision, roadmap, release gates and Claude Code instructions.

## Not confirmed
- Running API connectors for sources, schedulers, production deployment or persisted runtime metrics.
- CI workflow or automated tests (checked `.github/workflows/ci.yml` and `.github/workflows/hourly.yml`; neither found).
- Python/Node project manifests (checked `pyproject.toml` and `package.json`; neither found).
- End-to-end real-source execution, backups/restores, alerts, cost caps or reproducible Eval fixtures.

**Important:** missing at a checked path does not prove absence elsewhere. No execution logs, GitHub Actions runs, hosting provider configuration or complete recursive file tree were inspected. Do not equate design documents with operational readiness.

## Risks and gaps
1. No verified executable path from discovery through schema-validated candidate persistence and checkpoint commit.
2. No verified Curator implementation with independent primary-source verification and accepted-intel persistence.
3. No demonstrated negative-path tests for inaccessible X content, duplicate claims, retries and partial writes.
4. No verified scheduler, concurrency guard, spend cap or failure notification.
5. No verified restore drill or operational rollback.
6. Schema shape alone does not enforce the semantic reliability gate or evidence strength; these require explicit application checks.

## Implementation order and exit criteria
### A. Inventory and baseline
- Obtain a complete tree and inspect actual entrypoints, sample data, runtime configs, GitHub Actions and hosting resources.
- Select runtime and source APIs; document authentication, quotas and budget.
- Define a small versioned Eval corpus, including invalid and adversarial source cases.
- **Exit:** reproducible local setup and baseline checks with evidence.

### B. One vertical slice
- Implement one Frontier source adapter with bounded fetch, normalized provenance, schema validation, atomic/idempotent queue write and safe checkpoint.
- Implement a minimal Curator that clusters candidates, checks primary evidence, applies the reliability gate and writes canonical intel plus a briefing.
- **Exit:** real-source run with logged run ID, accepted/rejected/unresolved examples, replay safety and a failing-source recovery test.

### C. Coverage and cadence
- Add Practitioner Radar; schedule two hourly radars and daily curation with locks, retries, cost ceilings and alerts.
- **Exit:** observed scheduled runs and recorded quality/cost metrics, not just green deployment logs.

### D. Knowledge and synthesis
- Persist corrections, topic relationships and dynamic watches; implement weekly synthesis.
- Pilot Jev or retrieval only after measurable improvement.

## Safety and release rules
Use separate PRs for implementation, tests and infrastructure when practical. Never put secrets in repo. Require review for destructive actions and production deployments. Report unknown as unknown, not passed. Follow `docs/engineering-standards.md` and `docs/release-readiness.md`.
