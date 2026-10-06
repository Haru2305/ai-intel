# Practitioner Radar

## Mission
Every hour, find practical AI knowledge that is emerging from real use before it necessarily becomes official documentation.

This worker is recall-oriented. It should surface promising weak signals without pretending they are verified facts.

## Sources
Prioritize:
1. X posts from AI practitioners, researchers, engineers, OSS maintainers, and heavy users
2. Reddit and Hacker News discussions with concrete evidence or reproducible detail
3. GitHub issues, discussions, examples, small repositories, and newly emerging projects
4. Personal technical blogs and demos
5. Official docs only when needed to verify or contextualize a practitioner claim

For inaccessible X posts, never invent their contents. Use indexed snippets only as leads and follow linked primary sources when possible.

## Search budget
Approximate emphasis:
- 50% broad practitioner/community discovery
- 30% curated watchlist
- 20% wildcard discovery outside familiar people, companies, and projects

The goal of wildcard discovery is to deliberately find useful things that popularity-based search would miss.

## What to look for
- new Claude Code, Codex, Gemini, or agent workflows
- context-engineering and prompting techniques
- unexpected model behavior
- practical comparisons based on real tasks
- MCP/tool-use patterns
- automation patterns
- small but unusually useful OSS tools
- failure modes and limitations
- reproducible hacks, experiments, or configurations
- new ways people are combining AI tools

Do not prioritize generic "10 prompts" content, recycled tips, affiliate promotion, or engagement bait.

## Checkpoint
Read `state/practitioner.json` first.

If `last_run_at` is null, perform a one-time bootstrap scan of roughly the previous 24 hours. Afterwards use the checkpoint with a small overlap.

Deduplicate against:
- today's `queue/practitioner/`
- `data/accepted/`
- recent `daily/`
- relevant `topics/`

Update `state/practitioner.json` after every successful run, including zero-result runs. If repository writes fail, do not advance the checkpoint.

## Process
1. Search the discovery, watchlist, and wildcard lanes.
2. Group posts about the same underlying technique or project.
3. Preserve the original claim and strongest available evidence.
4. Score the candidate.
5. Queue useful leads in `queue/practitioner/YYYY-MM-DD.jsonl`.
6. Mark uncertain but interesting claims as `needs_verification`.
7. Update the checkpoint.

Do not write directly to `data/accepted/`, `daily/`, or `topics/`.

## Scoring
Score 0–10:
- **importance**
- **novelty**
- **reliability**
- **actionability**
- **personal_value**

Unlike Frontier Radar, a practitioner item may be queued with moderate reliability when actionability or personal_value is high. Do not silently upgrade an anecdote into a fact.

Strong practitioner candidates often have:
- actionability >= 8, or
- personal_value >= 8, or
- novelty >= 8

## User-facing result
Return a short Japanese summary with reviewed count, queued count, queued titles, confidence/verification notes, and whether GitHub was updated.
