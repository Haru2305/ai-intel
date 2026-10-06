# ai-intel

Personal AI intelligence knowledge base.

The goal is not to archive every AI news item. The system separates fast discovery from slower judgment so that useful weak signals can be captured without letting noise pollute the long-term knowledge base.

## Architecture

```text
                    HOURLY DISCOVERY

   Official / GitHub / Research           X / Reddit / HN / Blogs
              |                                      |
              v                                      v
      Frontier Radar                         Practitioner Radar
      precision-oriented                     recall-oriented
              |                                      |
              v                                      v
    queue/frontier/                         queue/practitioner/
              \                                      /
               \                                    /
                +-------------+----------------------+
                              |
                              v
                    Daily Curator / Verifier
                 dedupe / verify / personal value
                              |
                    +---------+---------+
                    |         |         |
                    v         v         v
              data/accepted  daily/   topics/
                              |
                              v
                       Weekly Analyst
```

## Why two hourly radars?

### Frontier Radar
Asks: **What changed in AI itself?**

Focus:
- official releases
- model/provider docs
- GitHub releases and changelogs
- research
- major OSS
- meaningful industry changes

It is precision-oriented and prefers primary evidence.

### Practitioner Radar
Asks: **What are people discovering by actually using AI?**

Focus:
- X
- Reddit / Hacker News
- GitHub issues/discussions and small projects
- technical blogs
- real workflows, experiments, failure modes, and useful tricks

It is recall-oriented and may keep promising unverified signals for later review.

Approximate search emphasis:
- 50% broad practitioner/community discovery
- 30% watchlist
- 20% wildcard discovery

## Daily Curator

Hourly workers do **discovery**, not final acceptance.

Daily Curator:
1. merges duplicates without deleting meaningful follow-up evidence
2. verifies important claims against primary sources
3. re-scores candidates
4. evaluates personal value
5. writes final accepted records
6. updates daily summaries and durable topic knowledge

This keeps the hourly pipeline fast while making the long-term knowledge base clean.

## Evaluation

Candidates are scored 0–10 on:

- **importance** — impact on AI capabilities, tooling, research, or industry
- **novelty** — genuinely new information versus repository knowledge
- **reliability** — evidence quality and provenance
- **actionability** — usefulness for understanding or using AI
- **personal_value** — likely usefulness for the owner of this knowledge base

A broad industry announcement can be important but low personal value. A small workflow trick can be modestly important but very high personal value.

## Optional Jev decision layer

Jev is optional and must never be a hard dependency.

When available, use it as a fast pre-decision layer for bounded judgments such as:
- relevance
- duplicate likelihood
- topic routing
- personal-value bucket
- verification priority

The generative LLM still performs research, verification, synthesis, and prose generation. See `docs/jev-integration.md`.

## Repository structure

```text
ai-intel/
├── README.md
├── prompts/
│   ├── hourly-intel.md          # Frontier Radar
│   ├── practitioner-radar.md
│   ├── daily-curator.md
│   └── weekly-analyst.md
├── schemas/
│   └── item.schema.json
├── state/
│   ├── frontier.json
│   └── practitioner.json
├── queue/
│   ├── frontier/
│   └── practitioner/
├── data/
│   ├── raw/                     # legacy/bootstrap records
│   └── accepted/
├── daily/
├── weekly/
├── topics/
└── docs/
    └── jev-integration.md
```

## Operating cadence

- **Frontier Radar:** every hour
- **Practitioner Radar:** every hour
- **Daily Curator / Verifier:** once per day
- **Weekly Analyst:** once per week

The repository is the durable memory layer. Individual models and workers should remain replaceable.
