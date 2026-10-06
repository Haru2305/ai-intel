# Daily Curator

## Mission
Turn one day of accepted AI intelligence into a compact, durable summary and update the long-term knowledge base.

Do not produce a news dump.

## Inputs
Read:
- `data/accepted/YYYY-MM-DD.jsonl`
- `inbox/YYYY-MM-DD.md`
- relevant `topics/`
- recent `daily/` entries when needed

## Process
1. Merge records about the same underlying development.
2. Prefer primary evidence.
3. Remove weak duplicates or items that became clearly irrelevant.
4. Rank developments by actual significance.
5. Write `daily/YYYY-MM-DD.md`.
6. Update `topics/` only when information has durable value.

## Daily format
# YYYY-MM-DD

## Most important developments

### Title
**What happened**  
Concise factual description.

**Why it matters**  
Significance without hype.

**What changed**  
What is genuinely new versus prior knowledge.

**Evidence**  
Primary or strongest available evidence.

**Sources**  
URLs.

## Emerging patterns
Cross-item patterns visible during the day.

## Needs verification
Only claims still worth tracking.

## Watch next
Specific unresolved developments worth checking later.

## Updating topics
`topics/` is a knowledge base, not a chronological news archive.

Integrate information conceptually. When new evidence changes prior knowledge, preserve the evolution with:

`Updated: YYYY-MM-DD`

Do not copy the daily summary verbatim into topics.
