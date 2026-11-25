"""Use the cover skill compositor with an explicit editorial line break."""
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location(
    "compose_cover", ROOT / ".agents/skills/gzh-webchat-cover/scripts/compose_cover.py"
)
cover = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cover)
wrap = cover.wrap
cover.wrap = lambda draw, text, font, width: [
    line for paragraph in text.split("\n")
    for line in wrap(draw, paragraph, font, width)
]

if __name__ == "__main__":
    sys.argv = [str(__file__), "--background", str(HERE / "background.png"),
                "--output", str(HERE / "cover-v2.png"),
                "--title", "不用敲一行代码\n做微信小程序",
                "--subtitle", "WorkBuddy · 从原型到手机真能用",
                "--accent", "#C6F24E", "--overlay", "0.15"]
    cover.main()
