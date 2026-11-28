"""Render this article's cover with the cover skill's base compositor."""
from pathlib import Path
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FONT = "C:/Windows/Fonts/msyhbd.ttc"
REGULAR = "C:/Windows/Fonts/msyh.ttc"
TEXT = [
    ("WorkBuddy × animate Skill", (50, 83), 19, REGULAR, "#E5DDD4"),
    ("7 种风格", (47, 118), 58, FONT, "#FFF7EF"),
    ("科普动画", (47, 190), 58, FONT, "#FFBA71"),
]

if __name__ == "__main__":
    subprocess.run([
        sys.executable,
        str(ROOT / ".agents/skills/gzh-webchat-cover/scripts/compose_cover.py"),
        "--background", str(HERE / "background.png"),
        "--output", str(HERE / "cover.png"),
        "--title", "", "--overlay", "0.15",
    ], check=True)
    cover = Image.open(HERE / "cover.png").convert("RGB")
    draw = ImageDraw.Draw(cover)
    for text, position, size, font, color in TEXT:
        draw.text(position, text, font=ImageFont.truetype(font, size), fill=color)
    cover.save(HERE / "cover.png")
    cover.resize((360, 153), Image.Resampling.LANCZOS).save(HERE / "thumbnail.png")
