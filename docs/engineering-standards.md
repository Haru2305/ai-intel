# AIIntel engineering standards

> Status: project policy (2026-10-09). This document defines how to **build, evaluate, and operate** AIIntel; it does not claim that the runtime or monitoring listed below is already implemented.

## North star

Build a personally useful AI intelligence system, not another generic chatbot. Prefer **one reliable end-to-end workflow** over additional workers, frameworks, or demonstrations.

Respect the architecture in [README](../README.md):

- **Frontier Radar** and **Practitioner Radar** discover and queue candidates.
- **Daily Curator / Verifier** verifies, consolidates, and accepts canonical claim/event intel.
- **Weekly Analyst** synthesizes durable developments.
- **GitHub** stores durable configuration, knowledge, schemas, and audit history; it is **not** the worker execution engine.
- **Jev** is optional, limited to bounded pre-classification, and never a verifier or final acceptance authority.

## Engineering priorities (in order)

1. **Correctness and evidence.** Every accepted claim has attributable evidence; inaccessible X posts are never reconstructed from guesses. Preserve `needs_verification` for valuable unresolved leads. Apply the existing reliability gate (0–3 reject; 4–6 require caveats and support; 7–10 normal rules).
2. **Reliable writes.** Validate against `schemas/candidate.schema.json` and `schemas/intel.schema.json` before writing. Preserve the candidate/intel boundary and deduplicate by underlying claim/event, not by URL alone.
3. **Recoverable execution.** Tools and APIs are real integrations in production, not mocks. Use bounded retries with exponential backoff and jitter for transient errors; apply timeouts, rate-limit handling, and a documented fallback. Never retry an irreversible write blindly.
4. **Observability.** A failed or degraded run must be diagnosable by worker, stage, source, and run ID.
5. **Evals before scaling.** Test the accuracy of discovery, verification, deduplication, and briefing usefulness on representative labeled cases, including failures.
6. **Latency and costs.** Measure before optimizing. Add new retrieval systems, LLM calls, or workers only if they improve measured quality enough to justify their operational cost.
7. **Security.** Use least-privilege tokens and secrets outside the repository. Do not expose keys, private content, or raw sensitive payloads in logs or public artifacts.

## Required run contract

Each scheduled worker or curation job should make the following information available to the *runtime's* logs/metrics; do not assume a new GitHub schema exists for it:

| Field | Purpose |
| --- | --- |
| `run_id`, `worker`, `started_at`, `finished_at`, `status` | Identify and diagnose each run |
| `checkpoint_before`, `checkpoint_after` | Prove where scanning resumed |
| `sources_attempted`, `sources_succeeded`, `sources_failed` | Distinguish no news from failed retrieval |
| `candidates_seen`, `queued`, `duplicates`, `needs_verification` | Explain hourly output and deduplication |
| `schema_validation_failures`, `verification_failures`, `write_failures` | Identify correctness failures |
| `duration_ms`, `tool_calls`, `tokens_in`, `tokens_out`, `estimated_cost` | Measure latency, usage, and cost where available |

When a field cannot be measured, record it as **unknown**, not zero. Record stages and error categories with redacted details; do not write credentials, sensitive input, or full private tool responses into GitHub.

### Checkpoint and failure rules

- Read the previous checkpoint with a small overlap to reduce missed updates.
- Deduplicate across both queues, accepted intel, recent dailies, and topics.
- **Advance a checkpoint only after the output is validated and persisted successfully.**
- Writes should be idempotent (stable claim/event IDs or equivalent upsert/dedup safeguards).
- On a partial outage, record the affected source and failure; do not report an empty feed as a successful zero-find run.
- On retries exhausted, mark the run degraded or failed, preserve the prior checkpoint, and surface an actionable error.
- A fallback model/source must not silently weaken verification, provenance, or the reliability gate.

## Evaluation (Evals)

Maintain a small, versioned evaluation set before changing prompts, routing, models, or ingestion logic. Include at least:

- **Important positive:** major official release with primary-source confirmation must be discovered.
- **Duplicate cluster:** multiple URLs/X posts about one event yield one canonical intel record with multiple evidence links.
- **Unverifiable social claim:** an inaccessible or unsupported post remains unresolved, never accepted as fact.
- **Misleading claim:** contradictory primary evidence triggers rejection or explicit correction.
- **Useful niche signal:** a practical workflow with high personal value is not discarded solely because generic importance is low.
- **Failure injection:** API timeout, rate limit, malformed tool output, invalid schema, repeated delivery, and partial write do not silently advance the checkpoint.

Track these separately; one blended score hides dangerous trade-offs:

| Metric | Interpretation |
| --- | --- |
| Discovery recall on labeled important items | Missed meaningful updates |
| Precision of accepted intel | Incorrect or low-signal accepted claims |
| Duplicate leakage | One underlying event appearing as multiple accepted records |
| Evidence traceability | Accepted claims with checkable, attributable support |
| Schema validity | Candidate/intel records conforming to their schemas |
| Run success / degraded / failure | Operational health, including partial source outages |
| End-to-end latency and cost per useful accepted item | Operational efficiency, not just cost per API call |

**No arbitrary pass thresholds.** Establish a baseline, record target levels for the intended use, and compare candidates against that baseline. Treat provenance failures and false factual acceptance as release blockers, even if speed or cost improves.

## Change / release checklist

Before merging changes that alter a worker, prompt, schema, source, model, or tool integration:

- [ ] State the user-visible problem, expected improvement, and rollback procedure.
- [ ] Confirm real APIs/tool-call contracts (inputs, authentication, pagination, timeouts, rate limits, response validation).
- [ ] Preserve structured output validation, evidence links, and the candidate-to-intel gate.
- [ ] Check idempotency, safe retries, fallback behavior, and checkpoint semantics.
- [ ] Run relevant Evals, including at least one negative case and one tool/source failure.
- [ ] Compare recall, precision, duplicate leakage, reliability, latency, and estimated cost against the baseline where applicable.
- [ ] Confirm run IDs, redacted errors, and metrics allow post-release diagnosis.
- [ ] Update documentation/runbook if behavior or operating procedure changed.
- [ ] Deploy with a bounded rollout, observe actual runs, and revert if acceptance or reliability regresses.

For a **docs-only** change, link checks and consistency review suffice; do not claim runtime Evals were executed.

## When to add more technology

- **More hourly workers:** only when measured misses demonstrate that Frontier + Practitioner cannot cover a meaningful objective. Do not split merely by website.
- **RAG / embeddings / vector search:** only when baseline keyword/metadata retrieval cannot recover relevant historical intel sufficiently. Prove the gain on labeled queries, including retrieval cost and maintenance.
- **Long-term agent memory:** only for a concrete repeated decision that cannot be reconstructed reliably from existing state, queues, intel, and topics.
- **Authentication:** mandatory when exposing protected accounts/data or a multi-user product; unnecessary for internal design documents.
- **Jev or other classifiers:** adopt only when pre-routing measurably reduces cost or improves prioritization without increasing missed important items. Low-confidence decisions escalate to the LLM.
- **Optimization:** profile slow stages and expensive calls before adding caching, batching, or alternative models.

## Incident loop

1. Identify the affected run(s), worker(s), source(s), and earliest failed stage.
2. Preserve redacted error context and whether the checkpoint advanced.
3. Reproduce with the smallest input that demonstrates the failure.
4. Fix the root cause; add a regression Eval with that case.
5. Replay safely from the retained checkpoint and inspect deduplication/accepted intel.
6. Record the user-visible impact and follow-up action.

The goal is not to collect every headline. It is to **reliably deliver fewer, better verified, personally useful insights**, with enough evidence and diagnostics to trust the system.
