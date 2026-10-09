import datetime as dt
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from aiintel.frontier import candidate, run, validate_candidate

NOW = dt.datetime(2026, 10, 9, 8, 0, tzinfo=dt.timezone.utc)


def release(id=12):
    return {"id": id, "tag_name": "v1.2.3", "name": "Release v1.2.3",
            "published_at": "2026-10-09T07:00:00Z",
            "html_url": "https://github.com/openai/codex/releases/tag/v1.2.3",
            "body": "Release notes", "draft": False, "prerelease": False}


class FrontierTests(unittest.TestCase):
    def test_valid_candidate(self):
        item = candidate("openai/codex", release(), "2026-10-09T08:00:00Z")
        validate_candidate(item)
        self.assertEqual(item["status"], "needs_verification")

    def test_replay_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fetch = lambda repo: [release()]
            first = run(root, ("openai/codex",), fetch, NOW)
            second = run(root, ("openai/codex",), fetch, NOW)
            self.assertEqual(first["queued"], 1)
            self.assertEqual(second["queued"], 0)
            self.assertEqual(len((root / "queue/frontier/2026-10-09.jsonl").read_text().splitlines()), 1)

    def test_source_failure_does_not_advance_checkpoint(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def fail(repo):
                if repo == "bad/repo":
                    raise RuntimeError("simulated failure")
                return [release()]
            with self.assertRaises(RuntimeError):
                run(root, ("openai/codex", "bad/repo"), fail, NOW)
            self.assertFalse((root / "state/frontier-github.json").exists())
            self.assertFalse((root / "queue/frontier/2026-10-09.jsonl").exists())

    def test_malformed_release_blocks_checkpoint(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                run(Path(tmp), ("openai/codex",), lambda _: [{**release(), "html_url": "invalid"}], NOW)
            self.assertFalse((Path(tmp) / "state/frontier-github.json").exists())

    def test_old_and_draft_filtered(self):
        with tempfile.TemporaryDirectory() as tmp:
            old = {**release(1), "published_at": "2020-01-01T00:00:00Z"}
            draft = {**release(2), "draft": True}
            result = run(Path(tmp), ("openai/codex",), lambda _: [old, draft], NOW)
            self.assertEqual(result["queued"], 0)


if __name__ == "__main__":
    unittest.main()
