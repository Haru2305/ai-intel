---
name: release-review
description: Review AIIntel code or deployment changes against release readiness, security, operational recovery and evidence-based verification gates.
---

Read `docs/release-readiness.md` and `docs/engineering-standards.md`. Identify the changed scope and classify each applicable gate PASS, FAIL or N/A with concrete evidence. Inspect credentials exposure, least privilege, untrusted content, schema validation, provenance, retry/idempotency/checkpoints, cost ceilings, logging and rollback. Do not invent test results. End with blockers, follow-ups and the precise checks performed.
