# ai-intel

Personal AI intelligence knowledge base.

The goal of this repository is not to archive every AI news item. It is to continuously collect, evaluate, deduplicate, and curate high-value information so that changes in AI capabilities, tools, research, and usage patterns remain easy to track over time.

## Pipeline

```text
Web / X / GitHub / Reddit / official sources
                    |
                    v
             Hourly Intel
      collect -> verify -> score
          -> deduplicate
                    |
                    v
               inbox/
          data/accepted/
                    |
          +---------+---------+
          |                   |
          v                   v
    Daily Curator        Weekly Analyst
          |                   |
          v                   v
       daily/              weekly/
          |
          v
       topics/
```

## Principles

1. Prefer primary sources over reposts and commentary.
2. Optimize for signal, not volume.
3. Distinguish facts from claims and speculation.
4. Compare new information against existing knowledge before accepting it.
5. Preserve meaningful changes over time rather than repeatedly storing the same tip.
6. Keep raw machine-readable records separate from human-readable summaries.

## Evaluation

Each candidate item is scored from 0–10 on:

- **importance** — impact on AI capabilities, usage, or the industry
- **novelty** — how much genuinely new information it adds
- **reliability** — quality of evidence and source provenance
- **actionability** — usefulness for understanding or using AI

Default acceptance rule:

- `importance >= 7`, or
- `novelty >= 8`, or
- `actionability >= 8`

Items with `reliability <= 3` should normally be marked `needs_verification` rather than accepted.

## Repository structure

```text
ai-intel/
├── README.md
├── prompts/
│   ├── hourly-intel.md
│   ├── daily-curator.md
│   └── weekly-analyst.md
├── schemas/
│   └── item.schema.json
├── inbox/
├── daily/
├── weekly/
├── topics/
│   ├── models.md
│   ├── agents.md
│   ├── coding.md
│   ├── prompting.md
│   ├── local-llm.md
│   ├── research.md
│   ├── tools.md
│   └── ai-industry.md
└── data/
    ├── raw/
    └── accepted/
```

## Operating cadence

- **Hourly Intel:** every hour
- **Daily Curator:** once per day
- **Weekly Analyst:** once per week

The repository itself is the durable memory layer. Workers and models should be replaceable without losing accumulated knowledge.
