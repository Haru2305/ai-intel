# Optional Jev integration

Jev is optional and must never be a hard dependency.

```text
discovery -> candidate -> Jev bounded pre-decision -> LLM verification/curation -> canonical intel
```

Use Jev for relevance, probable duplicate, topic route, personal-value bucket and verification priority.

Do not use Jev for factual verification, open-ended research, prose generation, replacing primary-source checks or final acceptance.

Low-confidence decisions escalate to the LLM. A low Jev score must not suppress a clearly important primary-source development solely because the classifier is uncertain.

Store optional metadata under the `jev` field. Never commit API keys or credentials.
