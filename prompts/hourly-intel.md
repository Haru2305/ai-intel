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
- OpenAI, Anthropic, Google DeepMind, Meta, xAI
- important open-source projects
- meaningful industry changes

## Process
For every run:
1. Search for relevant information published or meaningfully updated since the previous run.
2. Group posts and articles describing the same underlying event.
3. Resolve the strongest available primary source.
4. Compare each candidate against `topics/`, recent `daily/`, and current `data/accepted/`.
5. Reject obvious duplicates and recurring tips that add no meaningful new information.
6. Score the remaining candidates.
7. Store all reviewed candidates in `data/raw/YYYY-MM-DD.jsonl`.
8. Store accepted or needs-verification candidates in `data/accepted/YYYY-MM-DD.jsonl`.
9. Add concise human-readable entries to `inbox/YYYY-MM-DD.md`.

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
