"""检查优化稿引用的本地原图、原提示词和七节结构。"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DRAFT = Path(__file__).with_name("WorkBuddy设置-初稿优化版.md")
SOURCE = ROOT / "raw/article/程序员梦哥/WorkBuddy 做好这几个设置，让WorkBuddy越来越懂你.md"
PROMPT = re.compile(r"^\x60{3}自定义指令[^\n]*\n[\s\S]*?^\x60{3}$", re.M)

draft = DRAFT.read_text(encoding="utf-8")
source = SOURCE.read_text(encoding="utf-8-sig")
before = re.findall(PROMPT, source)
assert len(before) == 1 and re.findall(PROMPT, draft) == before, "原提示词发生变化"

images = re.findall(r"!\[[^\]]+\]\(<([^>]+)>\)", draft)
assert [Path(ref).name for ref in images] == re.findall(r"!\[\[(.*?)\]\]", source), "原图或顺序发生变化"
for ref in images:
    with (DRAFT.parent / ref).open("rb") as image:
        assert image.read(8) == b"\x89PNG\r\n\x1a\n", ref

assert re.findall(r"^## (0[1-7]) ", draft, re.M) == [f"{i:02}" for i in range(1, 8)]
assert draft.rstrip().endswith("## 写在最后")
assert "零成本" not in draft and "云端记忆" not in draft
print(f"七节顺序、原提示词、{len(images)} 张原图与待写结尾检查通过")
