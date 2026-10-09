"""First real-source Frontier Radar: public GitHub releases, stdlib only.

This is discovery, NOT verification. Every output remains a candidate.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import random
import sys
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

UTC = dt.timezone.utc
DEFAULT_REPOS = ("anthropics/claude-code", "openai/codex")
CATEGORIES = {"models", "agents", "coding", "prompting", "local-llm", "research", "tools", "ai-industry"}


def utcnow():
    return dt.datetime.now(UTC)


def parse_time(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)


def iso(value):
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


def atomic_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=".tmp-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as out:
            json.dump(value, out, ensure_ascii=False, indent=2)
            out.write("\n")
            out.flush()
            os.fsync(out.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def fetch_releases(repo, token=None, attempts=3):
    owner, name = repo.split("/")
    url = f"https://api.github.com/repos/{quote(owner)}/{quote(name)}/releases?per_page=30"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "ai-intel-frontier/0.1",
               "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for attempt in range(attempts):
        try:
            with urlopen(Request(url, headers=headers), timeout=15) as response:
                payload = json.load(response)
            if not isinstance(payload, list):
                raise ValueError("GitHub API did not return a release list")
            return payload
        except HTTPError as error:
            # Authentication and validation errors are not transient. Respect rate limits.
            retry = error.code in (429, 500, 502, 503, 504) or (
                error.code == 403 and error.headers.get("X-RateLimit-Remaining") == "0")
            if not retry or attempt == attempts - 1:
                raise RuntimeError(f"GitHub API error {error.code} for {repo}") from None
        except (URLError, TimeoutError) as error:
            if attempt == attempts - 1:
                raise RuntimeError(f"Network failure for {repo}: {type(error).__name__}") from None
        if attempt < attempts - 1:
            time.sleep(min(2 ** attempt + random.random(), 5))
    raise RuntimeError("unreachable")


def candidate(repo, release, collected_at):
    published = release.get("published_at")
    url = release.get("html_url")
    tag = release.get("tag_name")
    if not (isinstance(published, str) and isinstance(url, str) and url.startswith("https://github.com/")
            and isinstance(tag, str) and tag):
        raise ValueError("release missing publication time, canonical URL or tag")
    parse_time(published)
    identity = f"github-release:{repo}:{release['id']}"
    digest = hashlib.sha256(identity.encode()).hexdigest()[:20]
    body = release.get("body") or ""
    title = release.get("name") or tag
    return {
        "id": f"frontier-{digest}", "collected_at": collected_at, "published_at": published,
        "lane": "frontier", "source": f"GitHub releases: {repo}",
        "url": url, "primary_source_url": url, "title": str(title)[:300],
        "summary": str(body).strip()[:1200] or f"Official release {tag} in {repo}.",
        "original_claim": f"{repo} published release {tag}.",
        "category": ["coding", "tools"], "importance": 5, "novelty": 5,
        "reliability": 5, "actionability": 5, "personal_value": 7,
        "confidence": "medium", "status": "needs_verification",
        "verification_status": "unverified",
        "tags": ["github-release", repo],
    }


def validate_candidate(item):
    # Required contract checks; full JSON Schema validation is an independent CI task.
    required = {"id", "collected_at", "lane", "source", "url", "title", "summary", "category",
                "importance", "novelty", "reliability", "actionability", "personal_value",
                "confidence", "status"}
    if not required.issubset(item):
        raise ValueError(f"candidate missing {sorted(required - item.keys())}")
    if item["lane"] != "frontier" or item["status"] not in ("queued", "needs_verification"):
        raise ValueError("invalid lane or status")
    if not item["category"] or not set(item["category"]).issubset(CATEGORIES):
        raise ValueError("invalid categories")
    if any(type(item[key]) is not int or not 0 <= item[key] <= 10 for key in
           ("importance", "novelty", "reliability", "actionability", "personal_value")):
        raise ValueError("invalid scores")
    for key in ("collected_at", "published_at"):
        parse_time(item[key])
    if not item["url"].startswith("https://"):
        raise ValueError("invalid URL")


def load_json(path, fallback):
    if not path.exists():
        return fallback
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def run(root, repos=DEFAULT_REPOS, fetcher=fetch_releases, now=None):
    """Collect a batch atomically per daily queue file; checkpoint only after persistence.

    Raises on any source failure, preserving the previous checkpoint. A persisted
    queue may already contain results, so replays must deduplicate stable IDs.
    """
    now = now or utcnow()
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    stamp = iso(now)
    checkpoint_path = root / "state" / "frontier-github.json"
    previous = load_json(checkpoint_path, {"repos": {}})
    if not isinstance(previous, dict) or not isinstance(previous.get("repos"), dict):
        raise ValueError("invalid checkpoint format")
    cutoff_default = now - dt.timedelta(days=7)
    additions = []
    next_state = dict(previous["repos"])
    for repo in repos:
        last = previous["repos"].get(repo)
        cutoff = max(cutoff_default, parse_time(last) - dt.timedelta(days=1)) if last else cutoff_default
        releases = fetcher(repo)
        newest = parse_time(last) if last else cutoff_default
        for release in releases:
            if release.get("draft") or release.get("prerelease"):
                continue
            published = release.get("published_at")
            if not published:
                continue
            timestamp = parse_time(published)
            if timestamp > now + dt.timedelta(minutes=5):
                raise ValueError("release timestamp is unexpectedly in the future")
            if timestamp > newest:
                newest = timestamp
            if timestamp < cutoff:
                continue
            item = candidate(repo, release, stamp)
            validate_candidate(item)
            additions.append(item)
        next_state[repo] = iso(newest)

    queue_path = root / "queue" / "frontier" / f"{now.date().isoformat()}.jsonl"
    existing = []
    if queue_path.exists():
        with queue_path.open(encoding="utf-8") as stream:
            for line in stream:
                if line.strip():
                    existing.append(json.loads(line))
    ids = {item["id"] for item in existing}
    unique = [item for item in additions if item["id"] not in ids and not ids.add(item["id"])]
    if unique:
        queue_path.parent.mkdir(parents=True, exist_ok=True)
        fd, temp = tempfile.mkstemp(prefix=".queue-", dir=queue_path.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as out:
                for item in existing + unique:
                    out.write(json.dumps(item, ensure_ascii=False) + "\n")
                out.flush()
                os.fsync(out.fileno())
            os.replace(temp, queue_path)
        finally:
            if os.path.exists(temp):
                os.unlink(temp)
    atomic_json(checkpoint_path, {"repos": next_state, "last_success_at": stamp})
    return {"sources_succeeded": len(repos), "candidates_seen": len(additions),
            "queued": len(unique), "duplicates": len(additions) - len(unique),
            "checkpoint": str(checkpoint_path), "queue": str(queue_path)}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Collect public GitHub releases as unverified Frontier candidates")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--repo", action="append", dest="repos", help="owner/repo (repeatable)")
    args = parser.parse_args(argv)
    repos = tuple(args.repos) if args.repos else DEFAULT_REPOS
    if any(len(repo.split("/")) != 2 or not all(repo.split("/")) for repo in repos):
        parser.error("each --repo must be owner/repo")
    try:
        result = run(args.root, repos=repos)
    except Exception as error:
        print(json.dumps({"status": "failed", "error": str(error)}), file=sys.stderr)
        return 1
    print(json.dumps({"status": "success", **result}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
