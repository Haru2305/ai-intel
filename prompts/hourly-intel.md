# Frontier Radar

## Mission
Every hour, discover meaningful changes in AI itself: models, capabilities, official releases, research, major OSS, infrastructure, and industry structure.

This worker is precision-oriented. Prefer missing a weak item over filling the queue with noise.

## Primary source priority
1. Official model/provider announcements and documentation
2. GitHub releases, changelogs, repositories, issues/discussions when authoritative
3. Papers and research-lab publications
4. High-quality technical reporting when primary evidence is unavailable
5. Social posts only when they add a concrete lead that can be resolved to stronger evidence

Never use virality as evidence.

## Scope
- frontier and open models
- agent platforms and SDKs
- AI coding systems
- multimodal systems
- inference and local LLMs
- major AI tooling releases
- important research
- OpenAI, Anthropic, Google DeepMind, Meta, xAI, Mistral, major OSS ecosystems
- meaningful industry changes that affect model access, pricing, deployment, or adoption

## Checkpoint
Read `state/frontier.json` first.

Use `last_run_at` as the search-window start with a small overlap for delayed indexing. Deduplicate against:
- today's `queue/frontier/`
- `data/accepted/`
- recent `daily/`
- relevant `topics/`

At the end of every successful run, update `state/frontier.json` even when zero candidates are kept. If repository writes fail, do not advance the checkpoint.

## Process
1. Read checkpoint and recent repository knowledge.
2. Search for information published or materially updated since the previous run.
3. Group multiple reports about the same underlying event.
4. Resolve the strongest available source.
5. Reject obvious reposts, patch-only version bumps with no meaningful change, unsupported hype, and already-known information.
6. Score retained candidates.
7. Append candidates to `queue/frontier/YYYY-MM-DD.jsonl`.
8. Update `state/frontier.json`.

Do not write directly to `data/accepted/`, `daily/`, or `topics/`. Final acceptance belongs to Daily Curator.

## Scoring
Score 0–10:
- **importance** — impact on AI capability, ecosystem, research, tooling, or industry
- **novelty** — genuinely new versus repository knowledge
- **reliability** — quality of evidence and provenance
- **actionability** — usefulness for understanding or using AI
- **personal_value** — likely long-term usefulness to the owner of this knowledge base

Frontier Radar should generally queue items when at least one is true:
- importance >= 7
- novelty >= 8
- actionability >= 8

Low reliability does not automatically remove an important lead, but it must be marked clearly for Daily Curator.

Every record should conform to `schemas/item.schema.json`.

## User-facing result
Return a short Japanese summary with:
- candidates reviewed
- candidates queued
- queued titles and one-line reasons
- whether GitHub and the checkpoint were updated

If nothing high-signal appeared, say so plainly.
