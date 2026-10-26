"""Validate the multi-agent evaluation page: provenance, resolvable links, and discoverability."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "wiki/comparisons/公众号流水线多Agent化改造评估.md"
INDEX = ROOT / "wiki/index.md"
PIPELINE_TOPIC = ROOT / "wiki/topics/公众号Skill流水线设计.md"
LINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")
FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)


def parse_frontmatter(text: str) -> dict:
    match = FM_RE.match(text)
    if not match:
        return {}
    data = {}
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, _, value = stripped.partition(":")
        data[key.strip()] = value.strip()
    return data


def parse_sources(value: str) -> list:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    return [item.strip().strip('"').strip("'") for item in value.split(",") if item.strip()]


class MultiAgentEvaluationTest(unittest.TestCase):
    def setUp(self):
        self.assertTrue(PAGE.is_file(), "评估页缺失")
        self.text = PAGE.read_text(encoding="utf-8-sig")
        self.front = parse_frontmatter(self.text)

    def test_frontmatter_and_provenance(self):
        self.assertEqual(self.front.get("type"), "comparison")
        for field in ("title", "status", "sources", "created", "updated"):
            self.assertIn(field, self.front)
        sources = parse_sources(self.front["sources"])
        self.assertTrue(sources, "评估页必须登记来源")
        for source in sources:
            with self.subTest(source=source):
                self.assertTrue(source.startswith("raw/"))
                self.assertTrue((ROOT / source).is_file(), f"来源不存在：{source}")

    def test_internal_links_resolve(self):
        for link in LINK_RE.findall(self.text):
            target = link.split("|")[0].split("#")[0].strip()
            if not target or target.startswith("raw/"):
                continue
            with self.subTest(link=target):
                candidates = [ROOT / "wiki" / f"{target}.md", ROOT / f"{target}.md"]
                self.assertTrue(any(c.is_file() for c in candidates), f"链接无法解析：{target}")

    def test_reachable_from_index_and_pipeline_topic(self):
        """The page must be discoverable from the index and from the pipeline design page."""
        page_key = "comparisons/公众号流水线多Agent化改造评估"
        for source in (INDEX, PIPELINE_TOPIC):
            with self.subTest(source=source.name):
                links = {link.split("|")[0].strip() for link in LINK_RE.findall(source.read_text(encoding="utf-8-sig"))}
                self.assertIn(page_key, links, f"{source.name} 未链接评估页")

    def test_does_not_claim_verified_cost_benefit(self):
        """Coordination cost and benefit are unmeasured; the page must not present them as settled."""
        body = self.text.split("---", 2)[-1]
        forbidden = ["成本降低", "提速", "效率提升", "已验证多Agent更优", "实测证明多Agent"]
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, body, f"评估页不得出现未经测量的收益断言：{phrase}")


if __name__ == "__main__":
    unittest.main()
