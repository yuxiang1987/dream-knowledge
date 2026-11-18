"""核对三处补充、继承的图文和与原稿的边界。"""
from pathlib import Path
import re

folder = Path(__file__).resolve().parent
base = folder.parent / 'workbuddy-light-edit-20261118/WorkBuddy设置-微调稿.md'
original = base.read_text(encoding='utf-8')
draft = (folder / 'WorkBuddy设置-补充优化稿.md').read_text(encoding='utf-8')

fence = r'^\x60{3}自定义指令[^\n]*\n[\s\S]*?^\x60{3}$'
assert re.findall(fence, draft, re.M) == re.findall(fence, original, re.M)
image = r'!\[\]\(<([^>]+)>\)'
images = re.findall(image, draft)
assert len(images) == 12 and images == re.findall(image, original)
assert all((folder / path).is_file() for path in images)
assert draft.split('## 写在最后', 1)[1] == original.split('## 写在最后', 1)[1]
for first, example, next_heading in [
    ('## 自定义指令', '整理报价表', '## 回复风格'),
    ('## 记忆与进化', '拿做周报举个例子', '## 窗口设置'),
    ('## 窗口设置', '375 像素宽度', '## 数据导入'),
]:
    assert draft.index(first) < draft.index(example) < draft.index(next_heading)
print('三处补充、原提示词、12 张原图和结尾核对通过')
