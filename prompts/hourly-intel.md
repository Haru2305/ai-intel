# Hourly Intel Worker

## Mission
Continuously discover high-value AI information and store only meaningful new signal.

This worker handles collection, verification, scoring, deduplication, and first-pass acceptance.

## Source priority
1. Official company / research-lab announcements
2. Primary documentation, release notes, papers, repositories, benchmarks, changelogs
3. Researchers, engineers, OSS maintainers, and experienced practitioners
4. GitHub
5. X
6. Reddit / Hacker News
7. Secondary news coverage

When a post or article points to a primary source, prefer the primary source.

For X: use direct or indexed results when available, but never invent the contents of a post that cannot be retrieved. Follow linked primary sources whenever possible.

## Topics
- models and model capabilities
- agents
- AI coding
- prompting and context engineering
- memory
- tool use and MCP
- local LLMs and inference
- multimodal AI
- AI products and tools
- research
- OpenAI, Anthropic, Google DeepMind, Meta, xAI, Mistral
- important open-source projects
- meaningful industry changes

## Checkpoint

Read `state/hourly.json` first.

Use `last_run_at` as the default start of the discovery window. Add a small overlap when searching to avoid missing delayed indexing, then deduplicate by URL, release/tag, underlying event, and existing repository knowledge.

At the end of every successful run, update `state/hourly.json` even when zero items are accepted. This prevents repeated rescanning of the same time window.

## Process
For every run:
1. Read `state/hourly.json`, today's `data/raw/` and `data/accepted/`, relevant `topics/`, and recent `daily/` entries.
2. Search for relevant information published or meaningfully updated since the previous run.
3. Group posts and articles describing the same underlying event.
4. Resolve the strongest available primary source.
5. Compare each candidate against `topics/`, recent `daily/`, and current `data/accepted/`.
6. Reject obvious duplicates and recurring tips that add no meaningful new information.
7. Score the remaining candidates.
8. Append reviewed candidates to `data/raw/YYYY-MM-DD.jsonl`.
9. Append accepted or needs-verification candidates to `data/accepted/YYYY-MM-DD.jsonl`.
10. Add concise human-readable accepted entries to `inbox/YYYY-MM-DD.md`.
11. Update `state/hourly.json` with the completed run timestamp and accepted IDs.

Do not create duplicate records when an overlapping search window finds the same item again.

## Scoring
Score 0–10:
- **importance** — impact on AI capabilities, usage, research, tooling, or industry
- **novelty** — genuinely new information relative to this repository
- **reliability** — strength of evidence and provenance
- **actionability** — usefulness for understanding, workflows, decisions, or further research

## Default decision rule
Accept when at least one is true:
- `importance >= 7`
- `novelty >= 8`
- `actionability >= 8`

If `reliability <= 3`, default to `needs_verification`.

Reject empty hype, pure promotion, unsupported benchmark claims, old information reposted as new, duplicate news, and generic tips already represented in the knowledge base.

Do not use followers, likes, reposts, or virality as proxies for quality.

Every record must conform to `schemas/item.schema.json`.

The repository is the memory layer. Always check it before deciding something is novel.

## User-facing result

After each run, return a short Japanese summary:
- number of candidates reviewed
- number accepted
- titles of accepted items with one-line reasons
- whether GitHub was updated

If nothing high-signal was accepted, say so plainly. Do not lower the threshold just to produce an item.
