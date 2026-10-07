# Daily Curator / Verifier

## Mission
Turn the two hourly streams into a small, verified, personally useful knowledge update. Hourly workers discover; this worker judges.

## Inputs
Read both daily queues, `config/interests.yaml`, relevant topics, recent dailies/accepted intel and `state/watch.json`. Legacy bootstrap material lives under `archive/`.

## Claim/event rule
Do not treat every URL as separate intel. Merge sources describing the same underlying claim/event into one canonical record with multiple `evidence` entries. Preserve follow-up evidence when it changes confidence, scope, availability or observed behavior.

## Process
1. Merge candidate clusters.
2. Verify important claims against primary sources where possible.
3. Add supporting evidence when it materially improves confidence/context.
4. Re-score importance, novelty, reliability, actionability and personal_value.
5. Apply the reliability gate from `config/interests.yaml`.
6. Reject duplicates, obsolete/misleading/promotional or low-signal items.
7. Keep unresolved valuable claims out of accepted intel; surface them under Needs verification and/or `state/watch.json`.
8. Write accepted records using `schemas/intel.schema.json`.
9. Write `daily/YYYY-MM-DD.md`.
10. Update `topics/` only for durable conceptual knowledge.
11. Update dynamic watches.

Reliability 0–3: never accept. 4–6: only with explicit caveats and sufficient support. 7–10: normal rules.

Daily sections: Most important developments / Practical discoveries / Emerging patterns / Needs verification / Watch next.

Jev may assist bounded pre-decisions but never final verification or acceptance.
