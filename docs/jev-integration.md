# Optional Jev integration

Jev is optional. The pipeline must continue to work when Jev is unavailable.

## Best role

Use Jev as a cheap, fast decision layer before expensive LLM verification.

Good bounded decisions:
- Is this candidate relevant to the knowledge base?
- Is this probably a duplicate?
- Which topic should receive it?
- How high is personal value?
- How urgently should this claim be verified?

## Do not use Jev for
- factual verification by itself
- open-ended research
- prose summaries
- replacing primary-source checks
- final acceptance when confidence is low

## Escalation

A practical pattern:

```text
candidate
   |
   v
Jev: relevance / route / priority / personal-value estimate
   |
   +-- low confidence --> LLM review
   |
   +-- high confidence, low relevance --> discard or low-priority queue
   |
   +-- high confidence, high relevance --> LLM verification
```

Store optional decision metadata under the `jev` field in `schemas/item.schema.json`.

Never commit API keys or credentials to this repository. Use environment secrets in the runtime that eventually calls the API.
