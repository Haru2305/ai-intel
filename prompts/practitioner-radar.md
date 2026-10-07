# Practitioner Radar

## Mission
Every hour, find practical AI knowledge emerging from real use. Recall matters, but uncertainty must remain explicit.

## Read first
- `config/interests.yaml`
- `config/sources.yaml`
- `config/watchlist.yaml`
- `state/practitioner.json`
- relevant items in `state/watch.json`

## Search mix
- 50% broad practitioner/community discovery
- 30% persistent watchlist
- 20% wildcard discovery

Prioritize X practitioners, Reddit/HN with concrete detail, GitHub issues/discussions/examples/small repos, technical blogs and demos. Use official docs to verify or contextualize claims. Never invent inaccessible X content.

Look for coding/agent workflows, context engineering, model behavior, MCP/tool use, automation, useful OSS, failure modes, reproducible experiments and cross-model patterns. Avoid recycled tips, affiliate content and engagement bait.

## Process
1. Use the checkpoint with a small overlap.
2. Search broad/watchlist/wildcard/dynamic-watch lanes.
3. Group posts about the same claim/event before queueing.
4. Deduplicate against both queues, accepted intel, dailies and topics.
5. Score using `config/interests.yaml`.
6. Write `schemas/candidate.schema.json` records to `queue/practitioner/YYYY-MM-DD.jsonl`.
7. Keep uncertain valuable items as `needs_verification`.
8. Advance checkpoint only after successful writes.

Strong candidates often have actionability >= 8, personal_value >= 8, or novelty >= 8.

Jev may do bounded pre-classification only. Return a short Japanese run summary.
