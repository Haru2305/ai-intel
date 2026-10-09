# Release readiness gates

**Status:** policy/checklist, not automated enforcement. Record PASS / FAIL / N/A and evidence for each applicable check. A checklist response without test evidence is not a PASS.

## P0: required for relevant deployments
- [ ] No secrets in Git, client bundles, logs or artifacts; rotate any credential ever exposed.
- [ ] Least-privilege service identities, CI permissions and protected production credentials.
- [ ] Validate external inputs and structured outputs server-side; treat retrieved content as untrusted against prompt injection.
- [ ] Apply auth and authorization on every protected endpoint and enforce tenant/data isolation if multi-user.
- [ ] Bound API spending, concurrency, retries, rate limits and token consumption; alert on budget anomalies.
- [ ] Ensure stable deduplication, idempotent writes and checkpoint advancement only after validated persistence.
- [ ] Fail closed on provenance/verification failures; prevent error output from leaking stack traces or sensitive content.
- [ ] Prove a safe rollback path; require approval for destructive migrations or production changes.

## P1: operational reliability
- [ ] Structured run/error tracking, actionable alerts and redacted diagnostic data.
- [ ] Backups, retention rules and a tested restore for durable state.
- [ ] CI tests, negative-path Evals, dependency/security checks and documented limitations.
- [ ] Validate representative performance and resource usage; investigate slow paths with measurements.
- [ ] Test recovery from API timeout, rate limit, malformed input, partial write and duplicate delivery.
- [ ] Observe post-release runs and define rollback triggers.

## Conditional public-product checks (N/A until applicable)
- [ ] Friendly 404/500 pages, accessible responsive UI and representative low-end Android testing.
- [ ] Metadata and Open Graph previews.
- [ ] Privacy policy, terms and contact/support channel appropriate to the product.
- [ ] Privacy-aware analytics and user journey monitoring.
- [ ] End-to-end signup, payment, password reset and email deliverability tests where those features exist.

## Review evidence
For each gate record: status, relevant scope, command or manual procedure, observed result, reviewer and date. CI is authoritative for machine-checkable gates; hooks are convenience checks, not a security boundary. Do not mark missing tests as passed.
