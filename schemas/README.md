# Schemas

- `candidate.schema.json`: new hourly queue records.
- `intel.schema.json`: durable accepted claim/event records with one or more evidence entries.
- `item.schema.json`: legacy compatibility only.

Candidates are leads; intel records are canonical knowledge. Do not use the legacy schema for new writes.
