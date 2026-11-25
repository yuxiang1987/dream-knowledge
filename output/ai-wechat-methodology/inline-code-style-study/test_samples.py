from html.parser import HTMLParser
from pathlib import Path
from PIL import Image
class Samples(HTMLParser):
    def __init__(self):
        super().__init__()
        self.groups = []
        self.current = None
    def handle_starttag(self, tag, attrs):
        if tag == "section": self.current = []
        if tag == "p": self.groups.append(self.current)
    def handle_data(self, data):
        if self.current is not None and any(self.current is group for group in self.groups): self.current.append(data)
    def handle_endtag(self, tag):
        if tag == "section": self.current = None
root = Path(__file__).resolve().parent
for name, count in (("compare", 4), ("ten", 10)):
    parser = Samples()
    parser.feed((root / f"{name}.html").read_text(encoding="utf-8-sig"))
    assert len(parser.groups) == count and len({tuple(g) for g in parser.groups}) == 1
    image = Image.open(root / f"{name}.jpg").convert("RGB")
    assert image.width >= 650 and image.height > 300 and image.getextrema()[0][0] < 50
