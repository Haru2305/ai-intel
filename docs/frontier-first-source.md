# First real-source Frontier adapter

This is an **implementation**, not proof of a successful production run. It reads the public GitHub Releases API for `anthropics/claude-code` and `openai/codex`, producing **unverified discovery candidates**. It does not scrape X, accept canonical intel, run an LLM or send notifications.

## Run locally

Python 3.11+ (standard library only):

```bash
PYTHONPATH=src python -m aiintel.frontier --root .
python -m unittest discover -s tests -v
```

Optionally set `GITHUB_TOKEN` for authenticated API access (do not commit the token). Override repositories with repeatable `--repo owner/repo` flags. Output is written to `queue/frontier/YYYY-MM-DD.jsonl` and `state/frontier-github.json`. Review output before committing; use a disposable `--root` directory for experiments.

## Guarantees and limitations
- Bounded retries on transient GitHub API errors; non-transient errors fail the run.
- Stable IDs, daily-file deduplication, temporary-file replacement and checkpoint after successful queue persistence.
- Partial source failures abort the batch without advancing the checkpoint.
- 1-day checkpoint overlap; initial lookback is 7 days; only first 30 releases per repo are retrieved. **High-volume repositories can lose older releases:** add pagination before scaling.
- No cross-day/global deduplication yet; a release within the overlap can appear in multiple daily queue files. Daily Curator must deduplicate by underlying claim/event.
- No concurrent-run lock or durable transaction across queue/checkpoint. Run one instance at a time; replay safely after failures.
- Minimal built-in validation is not a substitute for full JSON Schema validation or independent factual verification.
- GitHub release metadata is a discovery signal; all outputs remain `needs_verification`, regardless of publisher.
- No scheduler, CI, metrics backend, secret provisioning or production deployment is configured here.

## Next milestones
Add full JSON Schema validation and global deduplication; source pagination; concurrency protection; a testable Curator; CI and controlled scheduling after Eval baselines and cost budgets are agreed.
