"""从已下载快照生成便于Agent阅读的派生正文；不改动raw文件。"""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/ai-wechat-methodology"


class ReadableHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.hidden += 1
        if self.hidden:
            return
        if tag in ("p", "div", "section", "article", "blockquote", "tr"):
            self.parts.append("\n\n")
        elif re.fullmatch(r"h[1-6]", tag):
            self.parts.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "img":
            url = attrs.get("data-src") or attrs.get("src") or ""
            if url.startswith(("https://", "http://", "//")):
                alt = (attrs.get("alt") or "原文图片").replace("[", "").replace("]", "")
                self.parts.append(f"\n\n![{alt}]({url})\n\n")
        elif tag == "a":
            url = attrs.get("href") or ""
            safe = url if url.startswith(("https://", "http://")) else ""
            self.links.append(safe)
            if safe:
                self.parts.append("[")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)
            return
        if self.hidden:
            return
        if tag == "a" and self.links:
            url = self.links.pop()
            if url:
                self.parts.append(f"]({url})")
        elif tag in ("p", "div", "section", "article", "blockquote", "tr") or re.fullmatch(r"h[1-6]", tag):
            self.parts.append("\n\n")
        elif tag in ("td", "th"):
            self.parts.append(" | ")

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)

    def text(self):
        text = "".join(self.parts).replace("\xa0", " ").replace("\u200b", "")
        text = re.sub(r"[ \t]+\n", "\n", text)
        return re.sub(r"\n{3,}", "\n\n", text).strip()


def readable(body):
    if not re.search(r"</?(?:p|div|section|span|img|article)\b", body, re.I):
        return body.strip()
    parser = ReadableHTML()
    parser.feed(body)
    parser.close()
    return parser.text()


def main():
    manifest = json.loads((OUT / "路人甲TM最新60篇下载清单.json").read_text(encoding="utf-8"))
    if not manifest["complete"] or len(manifest["articles"]) != 60:
        raise ValueError("只为完整60篇批次生成可读版目录")
    folder = OUT / "路人甲TM最新60篇可读版"
    folder.mkdir(parents=True, exist_ok=True)
    index = ["# 路人甲TM最新60篇文章目录", "",
             f"采集时间：{manifest['acquired_at']}。按公众号文章栏目最新顺序归档，共60篇。", "",
             "可读版从原始正文提取文字与图片链接，便于Agent阅读；排版、交互和嵌入视频以原始快照及公开链接为准。图片仅保留链接，未下载媒体文件。", "",
             "这些文章已归档，尚未逐篇编译成知识页；原有23篇产品和类型台账保持原覆盖范围。本批不自动确认每篇的实际付费方。", "",
             "| 序号 | 发布时间 | 文章 | 原始快照 |", "| --- | --- | --- | --- |"]
    for i, entry in enumerate(manifest["articles"], 1):
        raw = ROOT / entry["raw_path"]
        text = raw.read_text(encoding="utf-8-sig")
        body = text.split("\n---\n", 1)[1] if text.startswith("---\n") else text
        content = readable(body)
        path = folder / f"{i:02d}-{raw.name}"
        path.write_text(f"# {entry['title']}\n\n作者：路人甲TM\n\n发布时间：{entry.get('published') or '未提供'}\n\n"
                        f"原文：{entry['url']}\n\n原始快照：`{entry['raw_path']}`\n\n"
                        "---\n\n" + content + "\n", encoding="utf-8")
        label = entry["title"].replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")
        link = quote(path.relative_to(OUT).as_posix(), safe="/")
        raw_link = quote("../../" + entry["raw_path"], safe="/")
        index.append(f"| {i} | {entry.get('published') or '未提供'} | [{label}]({link}) | [原文快照]({raw_link}) |")
    (OUT / "路人甲TM最新60篇文章目录.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print("已生成60篇可读版与文章目录；raw原始文件未改动。")


if __name__ == "__main__":
    main()
