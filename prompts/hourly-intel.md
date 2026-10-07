# Frontier Radar

> Filename retained for compatibility.

## Mission
Every hour, discover meaningful changes in AI itself. Precision is more important than filling the queue.

## Read first
- `config/interests.yaml`
- `config/sources.yaml`
- `config/watchlist.yaml`
- `state/frontier.json`
- relevant items in `state/watch.json`

## Sources
Prefer official docs/announcements, maintainer releases, papers and research-lab publications. Use strong technical reporting when primary evidence is unavailable. Social posts are leads, not evidence of truth.

## Scope
Models, agents/SDKs, coding systems, multimodal systems, inference/local LLMs, major tooling, research, pricing/access/deployment and meaningful industry changes.

## Process
1. Use `state/frontier.json:last_run_at` with a small overlap.
2. Search recent changes plus persistent/dynamic watches.
3. Group URLs describing the same underlying claim/event.
4. Resolve the strongest evidence.
5. Deduplicate against both queues, accepted intel, recent dailies and topics.
6. Score retained candidates using `config/interests.yaml`.
7. Append to `queue/frontier/YYYY-MM-DD.jsonl` using `schemas/candidate.schema.json`.
8. Advance the checkpoint only after successful writes.

Generally queue when importance >= 7, novelty >= 8, actionability >= 8, or personal_value >= 8. Low-reliability high-value leads must remain `needs_verification`.

Do not write directly to accepted intel, daily, or topics.

Jev, if available, may classify relevance/duplicate/route/value/verification priority only.

Return a short Japanese run summary.
