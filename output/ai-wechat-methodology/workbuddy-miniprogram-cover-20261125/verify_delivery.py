"""Check deliverable dimensions, typography safety and unchanged source."""
import hashlib
from PIL import Image, ImageDraw, ImageFont
from build_cover import HERE, ROOT, cover

with Image.open(HERE / "cover-v2.png") as image:
    assert image.size == (900, 383)
    assert image.format == "PNG" and image.mode == "RGB"
    assert image.getbbox() == (0, 0, 900, 383)

draw = ImageDraw.Draw(Image.new("RGB", (900, 383)))
font = ImageFont.truetype(cover.find_font(True), 48)
lines = cover.wrap(draw, "不用敲一行代码\n做微信小程序", font, 405)
assert lines == ["不用敲一行代码", "做微信小程序"]
for line, y in zip(lines, [112, 174]):
    left, top, right, bottom = draw.textbbox((48, y), line, font=font, stroke_width=1)
    assert left >= 45 and right <= 450 and top >= 20 and bottom <= 363
subtitle_font = ImageFont.truetype(cover.find_font(False), 20)
assert draw.textbbox((48, 240), "WorkBuddy · 从原型到手机真能用", font=subtitle_font)[2] <= 450

source = ROOT / "raw/article/程序员梦哥/WorkBuddy + huashu skill 手搓健身小程序（附提示词）.md"
assert hashlib.sha256(source.read_bytes()).hexdigest() == "5a910ddebd0866c25209046a37dfb1e0f3cf3b21e7873b9c95f528163af7c496"
print("PASS: 900x383 RGB PNG, complete two-line title, typography safety, unchanged article")
