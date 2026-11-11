"""Check title research against immutable local source material."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "wiki/comparisons/近期对标标题结构与取材方法.md"


class TitleResearchTest(unittest.TestCase):
    def test_all_titles_match_raw_and_linked_deconstruction(self):
        text = PAGE.read_text(encoding="utf-8")
        paths = json.loads(re.search(r"^sources: (.+)$", text, re.M)[1])
        rows = re.findall(r"^\| ([^|]+)：《(.+)》 \| [^|]+ \| (.+) \|$", text, re.M)
        self.assertEqual(len(paths), 32)
        self.assertEqual(len(set(paths)), 32)
        self.assertEqual(len(rows), 32)
        self.assertEqual(len({row[0] for row in rows}), 8)
        linked = 0
        for path, (account, title, evidence) in zip(paths, rows):
            with self.subTest(title=title):
                raw = (ROOT / path).read_text(encoding="utf-8")
                self.assertEqual(json.loads(re.search(r"^title: (.+)$", raw, re.M)[1]), title)
                self.assertEqual(json.loads(re.search(r"^account: (.+)$", raw, re.M)[1]), account)
                link = re.search(r"\[\[(sources/[^]]+)\]\]", evidence)
                if link:
                    linked += 1
                    source = (ROOT / "wiki" / (link[1] + ".md")).read_text(encoding="utf-8")
                    self.assertIn(path, source)
                else:
                    self.assertIn(path, evidence)
        self.assertEqual(linked, 31)


if __name__ == "__main__":
    unittest.main()
