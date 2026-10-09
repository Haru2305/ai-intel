# AIIntel implementation roadmap

This roadmap distinguishes **design** from **verified deployment**. Do not check off milestones without linked evidence.

## Phase 0 — repository contract
- [ ] Audit existing schemas, prompts, queues, topic records and source configs for consistency.
- [ ] Select scheduler, storage, deployment boundaries and per-run budget.
- [ ] Create a small labeled Eval fixture set including unverifiable X posts and duplicate claims.
- [ ] Establish secret handling, protected branches and baseline CI.

## Phase 1 — minimum reliable vertical slice
- [ ] Run one Frontier Radar discovery cycle using real source integrations.
- [ ] Validate and persist candidates; capture provenance and checkpoints.
- [ ] Run Daily Curator verification, deduplication and reliability gate.
- [ ] Produce an evidence-backed daily briefing from accepted intel.
- [ ] Exercise timeout, rate-limit, partial-write and replay recovery.

## Phase 2 — two-radar coverage
- [ ] Add Practitioner Radar with independent discovery objectives.
- [ ] Schedule both radars hourly with concurrency and spend limits.
- [ ] Compare recall, precision, duplicates and cost per useful accepted item.
- [ ] Add structured run monitoring and alerts.

## Phase 3 — durable intelligence
- [ ] Maintain topic histories, corrections, watches and feedback signals.
- [ ] Produce Weekly Analyst synthesis and track evolving claims.
- [ ] Measure usefulness and false-acceptance rates against baselines.

## Phase 4 — measured extensions
- [ ] Pilot Jev only for bounded routing and measure misses/cost.
- [ ] Consider semantic retrieval only if keyword/metadata retrieval fails labeled tests.
- [ ] Consider new workers only after observed coverage gaps.
- [ ] Consider richer notifications/UI after the intelligence pipeline is trustworthy.

## Decision gate
For each proposed extension document: problem, evidence of baseline deficiency, alternative approaches, projected cost, acceptance metric, rollback and owner.
