#!/usr/bin/env python3
"""知识库体检脚本（LLM Wiki Lint）。

用法：
    python scripts/wiki_lint.py
    python scripts/wiki_lint.py --root "E:\\code\\webchat"

退出码：存在错误时返回 1，否则返回 0。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)
LINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")
CODE_RE = re.compile(r"```.*?```", re.S)
LOG_LINE_RE = re.compile(r"^## \[(\d{4}-\d{2}-\d{2})\] (\S+) \| (\S.*)$")

REQUIRED_FIELDS = ("title", "type", "status", "sources", "created", "updated")
VALID_TYPES = {"source", "concept", "entity", "topic", "comparison"}
VALID_STATUS = {"草稿", "进行中", "稳定", "待核实", "有冲突", "已过时", "已归档"}
SPECIAL_FILES = {"index.md", "log.md"}


def parse_frontmatter(text: str):
    match = FM_RE.match(text)
    if not match:
        return None, text
    data = {}
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, _, value = stripped.partition(":")
        data[key.strip()] = value.strip()
    return data, text[match.end():]


def parse_list(value: str):
    value = (value or "").strip()
    if not value:
        return []
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
        return [item.strip().strip('"').strip("'") for item in value.split(",") if item.strip()]
    return [value.strip().strip('"').strip("'")]


def main() -> int:
    parser = argparse.ArgumentParser(description="知识库结构体检")
    parser.add_argument("--root", default=None, help="知识库根目录，默认取脚本的上级目录")
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    wiki_dir = root / "wiki"
    if not wiki_dir.is_dir():
        print(f"[错误] 找不到 wiki 目录：{wiki_dir}")
        return 1

    wiki_files = sorted(wiki_dir.rglob("*.md"))
    if not wiki_files:
        print(f"[错误] {wiki_dir} 下没有 markdown 文件")
        return 1

    by_rel_path = {}
    by_stem: dict[str, list[str]] = {}
    for path in wiki_files:
        rel = path.relative_to(root).as_posix()
        key = rel[:-3] if rel.endswith(".md") else rel
        by_rel_path[key] = path
        by_stem.setdefault(path.stem, []).append(key)

    def resolve(target: str):
        clean = target.strip().split("|")[0].split("#")[0].strip().strip("/")
        if not clean:
            return None
        base = clean[:-3] if clean.endswith(".md") else clean
        for candidate in (base, f"wiki/{base}"):
            if candidate in by_rel_path:
                return candidate
        raw_candidate = root / (clean if clean.endswith(".md") else f"{clean}.md")
        if raw_candidate.is_file():
            return f"@{clean}"
        stem = Path(base).name
        hits = by_stem.get(stem, [])
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1:
            return f"?{stem}"
        return None

    errors: list[str] = []
    warnings: list[str] = []
    inbound: dict[str, set[str]] = {key: set() for key in by_rel_path}
    titles: dict[str, list[str]] = {}

    for path in wiki_files:
        rel = path.relative_to(root).as_posix()
        key = rel[:-3]
        text = path.read_text(encoding="utf-8", errors="replace")
        front, body = parse_frontmatter(text)

        if path.name not in SPECIAL_FILES:
            if front is None:
                errors.append(f"{rel}：缺少 frontmatter")
            else:
                for field in REQUIRED_FIELDS:
                    if field not in front:
                        errors.append(f"{rel}：frontmatter 缺少字段 {field}")
                page_type = front.get("type", "").strip()
                if page_type and page_type not in VALID_TYPES:
                    errors.append(f"{rel}：type 取值不合法（{page_type}）")
                status = front.get("status", "").strip()
                if status and status not in VALID_STATUS:
                    errors.append(f"{rel}：status 取值不合法（{status}）")
                title = front.get("title", "").strip()
                if title:
                    titles.setdefault(title, []).append(rel)
                source_items = parse_list(front.get("sources", ""))
                if not source_items:
                    warnings.append(f"{rel}：sources 为空，确认是否确实没有来源")
                for item in source_items:
                    if not (root / item).exists():
                        errors.append(f"{rel}：sources 指向的文件不存在 - {item}")

        for link in LINK_RE.findall(CODE_RE.sub("", body)):
            target = link.strip()
            if not target:
                continue
            resolved = resolve(target)
            if resolved is None:
                errors.append(f"{rel}：链接无法解析 - [[{target}]]")
            elif resolved.startswith("?"):
                warnings.append(f"{rel}：链接名称不唯一 - [[{target}]]")
            elif not resolved.startswith("@"):
                inbound.setdefault(resolved, set()).add(key)

    for title, rels in sorted(titles.items()):
        if len(rels) > 1:
            errors.append(f"标题重复（{title}）：{', '.join(rels)}")

    for key in by_rel_path:
        if f"{Path(key).name}.md" in SPECIAL_FILES:
            continue
        if not inbound.get(key):
            warnings.append(f"{key}.md：没有任何页面链接到它（孤页）")

    log_path = wiki_dir / "log.md"
    if log_path.is_file():
        entries = 0
        for line in log_path.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("## "):
                entries += 1
                if not LOG_LINE_RE.match(line):
                    warnings.append(f"wiki/log.md：日志条目格式不规范 - {line[:60]}")
        if entries == 0:
            warnings.append("wiki/log.md：还没有日志条目")

    print(f"知识库体检：{root}")
    print(f"页面数：{len(by_rel_path)}")
    print()
    if errors:
        print(f"[错误] {len(errors)} 项")
        for item in errors:
            print(f"  - {item}")
        print()
    if warnings:
        print(f"[警告] {len(warnings)} 项")
        for item in warnings:
            print(f"  - {item}")
        print()
    if not errors and not warnings:
        print("未发现问题。")
    print("结果：" + ("有错误，需要处理" if errors else "通过，仅有警告" if warnings else "通过"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
