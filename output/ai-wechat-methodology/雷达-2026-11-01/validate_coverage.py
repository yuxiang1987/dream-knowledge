"""Offline batch acceptance: coverage, evidence anchors, references and case ownership."""
import hashlib
import html
import json
import re
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[3]
BATCH = Path(__file__).resolve().parent

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, value):
        self.parts.append(value)

def visible(value):
    parser = Text()
    parser.feed(value)
    return re.sub(r"\s+", "", html.unescape("".join(parser.parts)))

def validate():
    fetched = json.loads((BATCH / "fetch-summary.json").read_text(encoding="utf-8"))
    expected = {r["raw_path"] for a in fetched["accounts"] for r in a["added_articles"]}
    rows = json.loads((BATCH / "coverage.json").read_text(encoding="utf-8"))
    assert len(rows) == len(expected) and {r["raw_path"] for r in rows} == expected, "Coverage gap or duplicate"
    index = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
    cards = (ROOT / "wiki/topics/AI写作案例库.md").read_text(encoding="utf-8")
    sources = {p.relative_to(ROOT).as_posix(): p.read_text(encoding="utf-8") for p in (ROOT / "wiki/sources").glob("*.md")}
    authors = {p.relative_to(ROOT).as_posix(): p.read_text(encoding="utf-8") for p in (ROOT / "wiki/topics").glob("*.md")}
    counts = {"deep": 0, "excluded": 0, "reused": 0, "case_cards": 0}
    for row in rows:
        raw = ROOT / row["raw_path"]
        assert hashlib.sha256(raw.read_bytes()).hexdigest() == row["raw_sha256"], raw
        counts[row["disposition"]] += 1
        if row["disposition"] == "excluded":
            assert row["reason"] and not row.get("source_path"), row["title"]
            assert any(row["title"] in t and row["raw_path"] in t for t in authors.values()), "Missing exclusion registration"
            continue
        path = row["source_path"]
        page = sources[path]
        assert row["raw_path"] in page.split("---", 2)[1], "Missing raw frontmatter reference"
        assert len(set(row["anchors"])) >= 2, "Insufficient distinct anchors"
        raw_text = visible(raw.read_text(encoding="utf-8"))
        for anchor in row["anchors"]:
            assert visible(anchor) in raw_text and anchor in page, (row["title"], anchor)
        target = path.removeprefix("wiki/").removesuffix(".md")
        def linked(text):
            return target in {x.split("|", 1)[0].split("#", 1)[0] for x in re.findall(r"\[\[([^\[\]]+)\]\]", text)}
        assert linked(index) and any(linked(text) for text in authors.values()), ("Missing navigation", path)
        refs = [p for p, text in sources.items() if row["raw_path"] in text.split("---", 2)[1]]
        assert refs == [path], ("Duplicate source ownership", refs)
        if row.get("case_card"):
            assert row["case_card"].strip() in cards, "Missing case card"
            assert re.search(r"^- 测试角度：[ \t]*$", row["case_card"], re.M), "Angle must remain human-owned"
            assert re.search(r"^- 步骤：[ \t]*$", row["case_card"], re.M), "Steps must remain human-owned"
            counts["case_cards"] += 1
    print(json.dumps({"covered": len(rows), **counts, "result": "PASS"}, ensure_ascii=False))
    return counts

if __name__ == "__main__":
    validate()
