"""检查微调稿的提示词、原图、七项顺序和补写的结尾。"""
from pathlib import Path
import re

folder = Path(__file__).resolve().parent
root = folder.parents[1]
source = root / "raw/article/程序员梦哥/WorkBuddy 做好这几个设置，让WorkBuddy越来越懂你.md"
original = source.read_text(encoding="utf-8")
draft = (folder / "WorkBuddy设置-微调稿.md").read_text(encoding="utf-8")

prompt = r"^\x60{3}自定义指令[^\n]*\n[\s\S]*?^\x60{3}$"
original_prompts = re.findall(prompt, original, re.M)
assert len(original_prompts) == 1
assert re.findall(prompt, draft, re.M) == original_prompts, "自定义指令发生变化"
images = re.findall(r"!\[\]\(<([^>]+)>\)", draft)
assert [Path(path).name for path in images] == re.findall(r"!\[\[([^\]]+)\]\]", original)
assert all((folder / path).is_file() for path in images), "图片链接失效"
headings = re.findall(r"^## (.+)", re.sub(prompt, "", draft, flags=re.M), re.M)
assert len(headings) == 8 and headings[-1] == "写在最后"
assert draft.split("## 写在最后", 1)[-1].strip()
assert draft.count("我是梦哥，十年程序员，爱折腾 AI。") == 1
print(f"七项设置、结尾、原提示词及 {len(images)} 张原图链接均通过检查")
