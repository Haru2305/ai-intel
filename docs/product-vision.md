# AIIntel product vision and decision record

**Status:** consolidated design, not a statement of deployed functionality.

## Mission
Continuously discover AI developments, distinguish evidence from speculation, connect new claims to durable knowledge and deliver a small number of personally useful, actionable insights. Optimize for signal quality and time saved, not number of posts collected.

## Coverage
- Official model releases, API capabilities, access/pricing changes, safety/limitations.
- Research papers, benchmarks, open-source repositories, inference and agent infrastructure.
- Practitioner discoveries on X, Reddit, Hacker News, GitHub and technical blogs.
- Agentic coding workflows, Claude Code/Codex, context engineering, orchestration, local models and automation.
- Weak signals and niche practical ideas, with explicit uncertainty.

## Information lifecycle
1. **Hourly discovery:** Frontier Radar prioritizes authoritative developments; Practitioner Radar prioritizes experimental usage and emerging workflows. Split by purpose, not platform.
2. **Candidate queue:** retain source URL, retrieval time, tentative claim, provenance, uncertainty, duplicate hints and routing metadata. Unavailable source content remains unresolved.
3. **Daily curation:** cluster by underlying claim/event, verify against primary evidence where possible, apply the reliability gate and personal priority score, and accept or reject with reasons.
4. **Knowledge:** persist canonical claim/event records with multiple evidence links, topic connections, updates and corrections. Git provides traceable history, not semantic memory by itself.
5. **Delivery:** concise daily briefing with why it matters, evidence, limitations, suggested experiments and watch items.
6. **Weekly synthesis:** what actually changed, trend trajectories, emerging opportunities, failed predictions and shifts in prior judgments.

## Personalization
Use `config/interests.yaml` as the source of truth for interest weights. Personal usefulness can outweigh broad press coverage but never bypasses factual verification.

## Output contract (design)
Each highlighted insight should answer: what happened; source and verification status; what changed compared with previous understanding; why it matters; practical implications; caveats; recommended next action; and whether follow-up is needed. Do not invent adoption metrics or predict certainty.

## Dynamic watchlist and feedback
Keep watches for uncertain claims, forthcoming releases, technical trends and experiments. Record explicit feedback on useful/noisy/missed items and use it to refine discovery and ranking. Maintain provenance and reversibility when updating earlier conclusions.

## Deliberate boundaries
- No autonomous installation or deployment of discovered tools.
- No trading execution, wallet management or financial decisions.
- No unverified X summaries.
- No unnecessary extra hourly agents or multi-agent chains.
- No claim that a proposed feature is already running.

## Open implementation decisions
Hosting/scheduler, storage backend, API access, notification channel, budget and quantitative Eval thresholds require evidence-based selection. Prefer a minimal end-to-end vertical slice before infrastructure expansion.
