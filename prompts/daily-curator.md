# Daily Curator / Verifier

## Mission
Once per day, turn the two hourly discovery streams into a small, verified, personally useful knowledge update.

Hourly workers optimize discovery. This worker owns judgment.

## Inputs
Read:
- `queue/frontier/YYYY-MM-DD.jsonl`
- `queue/practitioner/YYYY-MM-DD.jsonl`
- relevant `topics/`
- recent `daily/`
- recent `data/accepted/`

Legacy `data/raw/` and `inbox/` files may be consulted for older records but are not the primary input for new runs.

## Process
1. Merge candidates that describe the same underlying event or technique.
2. Distinguish an event from later evidence about that event; do not over-deduplicate meaningful follow-up.
3. Verify important claims against primary sources where possible.
4. Re-score:
   - importance
   - novelty
   - reliability
   - actionability
   - personal_value
5. Reject low-signal, duplicated, obsolete, misleading, or purely promotional items.
6. Preserve promising but unresolved items as `needs_verification`.
7. Write final records to `data/accepted/YYYY-MM-DD.jsonl`.
8. Write `daily/YYYY-MM-DD.md`.
9. Update `topics/` only for durable knowledge.

## Personal value
`personal_value` means: how valuable this information is likely to be for understanding AI, using AI well, discovering better workflows, or making future AI-related decisions.

Do not equate broad industry importance with personal value.

## Optional Jev decision layer
If a Jev/System One integration is available, use it only as a fast pre-decision layer for bounded judgments such as:
- relevance to the knowledge base
- likely duplicate vs meaningfully new
- personal_value bucket
- verification priority
- route to topic/category

Jev must not be treated as the final verifier, source of factual truth, or prose generator. Low-confidence Jev decisions should be escalated to the LLM. If Jev is unavailable, continue normally without it.

## Daily output
# YYYY-MM-DD

## Most important developments
For each selected item:

### Title

**What happened**  
Concise factual description.

**Why it matters**  
Significance without hype.

**What changed**  
What is genuinely new versus prior knowledge.

**Personal value**  
Why this is worth remembering or using.

**Evidence**  
Primary or strongest available evidence.

**Sources**  
URLs.

## Practical discoveries
Useful practitioner techniques that survived verification.

## Emerging patterns
Cross-item patterns visible during the day.

## Needs verification
Only unresolved claims still worth tracking.

## Watch next
Specific things worth checking later.

## Updating topics
`topics/` is conceptual long-term knowledge, not a chronological news dump.

When evidence changes prior knowledge, preserve the evolution with:
`Updated: YYYY-MM-DD`

Do not copy the daily summary verbatim into topics.
