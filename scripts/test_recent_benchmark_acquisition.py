"""Validate the recorded, user-scoped TikHub research batch without network calls."""
import hashlib
import html
import json
from pathlib import Path
import re
import unittest

from wiki_lint import parse_frontmatter, parse_list

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "output/ai-wechat-methodology/指定十账号最近30篇-2026-10-26"


def visible(text):
    return html.unescape(re.sub(r"<[^>]+>", "", text))


class RecentBenchmarkAcquisitionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.request = json.loads((BATCH / "request.json").read_text(encoding="utf-8"))
        cls.manifest = json.loads((BATCH / "manifest.json").read_text(encoding="utf-8"))

    def test_only_authorized_accounts_are_recorded(self):
        expected = self.request["accounts"]
        actual = [account["requested_name"] for account in self.manifest["accounts"]]
        self.assertCountEqual(actual, expected)
        self.assertEqual(len(actual), len(set(actual)))
        resolved = [account["username"] for account in self.manifest["accounts"]
                    if account["identity_status"] == "verified"]
        self.assertEqual(len(resolved), len(set(resolved)))

    def test_latest_selection_is_ordered_unique_and_honest(self):
        for account in self.manifest["accounts"]:
            with self.subTest(account=account["requested_name"]):
                articles = account["articles"]
                self.assertLessEqual(len(articles), self.request["per_account_limit"])
                self.assertEqual([row["rank"] for row in articles],
                                 list(range(1, len(articles) + 1)))
                ids = [row["id"] for row in articles]
                self.assertEqual(len(ids), len(set(ids)))
                times = [row["list_create_time"] for row in articles]
                self.assertEqual(times, sorted(times, reverse=True))
                if account["complete"]:
                    self.assertEqual(account["identity_status"], "verified")
                    self.assertEqual(len(articles), self.request["per_account_limit"])
                    self.assertTrue(account["list_complete"])
                    self.assertTrue(all(row["status"] == "analyzed" for row in articles))
                elif len(articles) < self.request["per_account_limit"]:
                    self.assertTrue(account.get("incomplete_reason"))

    def test_selection_matches_independent_api_pages(self):
        def article_rows(value):
            if isinstance(value, list):
                for item in value:
                    yield from article_rows(item)
            elif isinstance(value, dict):
                if "app_msg_id" in value and value.get("url"):
                    yield value
                else:
                    for item in value.values():
                        yield from article_rows(item)

        for account in self.manifest["accounts"]:
            with self.subTest(account=account["requested_name"]):
                fetched = {}
                for relative in account["list_evidence_files"]:
                    saved = json.loads((ROOT / relative).read_text(encoding="utf-8-sig"))
                    for row in article_rows(saved):
                        identity = f'{row["app_msg_id"]}:{row.get("idx", 1)}'
                        fetched.setdefault(identity, row)
                latest = sorted(fetched, key=lambda identity: int(
                    fetched[identity].get("create_time") or 0), reverse=True)
                self.assertEqual([str(row["id"]) for row in account["articles"]],
                                 latest[:self.request["per_account_limit"]])
                for row in account["articles"]:
                    self.assertEqual(row["list_create_time"],
                                     int(fetched[row["id"]]["create_time"]))

    def test_raw_provenance_and_locatable_evidence(self):
        for account in self.manifest["accounts"]:
            for row in account["articles"]:
                with self.subTest(account=account["requested_name"], article=row["id"]):
                    self.assertIn(row["status"], ("analyzed", "partial", "failed"))
                    if row["status"] == "failed":
                        self.assertTrue(row.get("error"))
                        continue
                    raw = ROOT / row["raw_path"]
                    self.assertTrue(raw.resolve().is_relative_to((ROOT / "raw/article").resolve()))
                    self.assertEqual(hashlib.sha256(raw.read_bytes()).hexdigest(), row["raw_sha256"])
                    page = ROOT / row["source_page"]
                    self.assertTrue(page.resolve().is_relative_to((ROOT / "wiki/sources").resolve()))
                    text = page.read_text(encoding="utf-8-sig")
                    front, _ = parse_frontmatter(text)
                    self.assertIsNotNone(front)
                    self.assertIn(row["raw_path"], parse_list(front["sources"]))
                    raw_text = raw.read_text(encoding="utf-8-sig")
                    if row["status"] == "analyzed":
                        self.assertGreaterEqual(len(set(anchor["text"] for anchor in row["anchors"])), 2)
                    for anchor in row["anchors"]:
                        self.assertTrue(anchor["location"])
                        self.assertIn(anchor["text"], visible(raw_text))
                        self.assertIn(anchor["text"], visible(text))

    def test_preexisting_raw_and_source_identity_are_preserved(self):
        baseline = json.loads((BATCH / "preservation-baseline.json").read_text(encoding="utf-8"))
        continuation = json.loads((BATCH / "continuation-baseline.json").read_text(encoding="utf-8"))
        for relative, expected in continuation["raw_sha256"].items():
            with self.subTest(raw=relative):
                self.assertEqual(hashlib.sha256((ROOT / relative).read_bytes()).hexdigest(), expected)
        for relative, created in baseline["source_created"].items():
            with self.subTest(source=relative):
                front, _ = parse_frontmatter((ROOT / relative).read_text(encoding="utf-8-sig"))
                self.assertEqual(front["created"], created)


if __name__ == "__main__":
    unittest.main()
