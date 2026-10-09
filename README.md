# ai-intel

Personal AI intelligence system. The goal is not to archive every AI news item; it is to discover weak signals quickly, verify them carefully, and preserve only useful knowledge.

## V1 architecture

```text
Official / GitHub / Research       X / Reddit / HN / Blogs
            |                                |
     Frontier Radar                  Practitioner Radar
     precision-oriented              recall-oriented
            \                                /
             +------ optional Jev -----------+
                        |
                 candidate queue
                        |
               Daily Curator / Verifier
              merge / verify / judge
                        |
          +-------------+-------------+
          |             |             |
 data/accepted/       daily/        topics/
 canonical intel     briefing     durable knowledge
          |
     Weekly Analyst
```

## Core rules

1. Workers discover; Daily Curator judges.
2. Durable knowledge is a **claim/event**, not a post or URL.
3. One intel record may contain multiple evidence sources.
4. Reliability is a gate, not merely another weighted score.
5. Personal usefulness can outrank generic news importance.
6. GitHub is durable memory/config/audit history, not the execution engine.
7. Models and workers remain replaceable.

## Workers

**Frontier Radar** asks what changed in AI itself: models, official releases, research, major OSS, inference, agent infrastructure, pricing/access and meaningful industry structure.

**Practitioner Radar** asks what people are learning by actually using AI: workflows, hacks, experiments, failure modes, small OSS tools, X/Reddit/HN/GitHub discussions and practitioner blogs.

**Daily Curator / Verifier** merges candidates into claim/event units, verifies them, re-scores them, applies the reliability gate, writes canonical intel, updates the daily briefing, durable topics and dynamic watches.

**Weekly Analyst** synthesizes what materially changed across the week rather than counting mentions.

## Candidate vs Intel

- `schemas/candidate.schema.json`: hourly discovery lead; may be incomplete or unresolved.
- `schemas/intel.schema.json`: canonical claim/event that survived curation and may aggregate multiple evidence sources.
- `schemas/item.schema.json`: legacy compatibility only; do not use for new writes.

## Scoring

Scores are 0–10: importance, novelty, reliability, actionability, personal_value.

Default personal-priority weights live in `config/interests.yaml`.

Reliability gate:
- 0–3: never accepted
- 4–6: only with explicit caveats and sufficient supporting evidence
- 7–10: normal curation rules

## Jev

Jev is optional. Use it only for bounded pre-decisions such as relevance, likely duplicate, route, personal-value bucket and verification priority. It is not a verifier, researcher, prose generator or final acceptance authority.

## Repository

```text
config/       priorities, sources, persistent watchlist
prompts/      worker instructions
schemas/      candidate + canonical intel schemas
state/        checkpoints + dynamic watches
queue/        hourly candidates
data/accepted canonical intel
daily/        daily briefing
weekly/       weekly synthesis
topics/       durable conceptual knowledge
archive/      legacy/bootstrap working records
```

## Engineering & operational quality

See [Engineering standards](docs/engineering-standards.md) for the run contract, failure handling, observability, evaluation fixtures, cost/latency tracking, release checklist, and incident loop.

This is a **design and delivery policy**, not a claim that the runtime, metrics, or automated Evals are already deployed. Measure quality before adding extra hourly workers, RAG, vector search, or agent memory.

## Cadence

- Frontier Radar: hourly
- Practitioner Radar: hourly
- Daily Curator: daily
- Weekly Analyst: weekly

Do not add more hourly workers by default. Split by discovery objective, not by source; add another worker only after measured misses justify it.
