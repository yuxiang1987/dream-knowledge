"""Build the revised assembly sample using the exact idle pose from the default intro."""
from base64 import b64encode
from importlib.util import module_from_spec, spec_from_file_location
from io import BytesIO
from pathlib import Path

from PIL import Image

OUT = Path(__file__).resolve().parent
PREVIOUS = OUT.parent / 'mengge-workbuddy-creative-trio'
SHEET = OUT.parent / '程序员梦哥像素闯关-v3' / 'action-sheet.png'
SPEC = spec_from_file_location('creative_trio', PREVIOUS / 'build.py')
creative = module_from_spec(SPEC)
SPEC.loader.exec_module(creative)


def idle_pose():
    # v8 motion.cjs uses zero-based action frame 2 for idle; v8 build.cjs crops pixels with alpha > 110.
    with Image.open(SHEET) as source:
        w, h = source.size
        tile = source.convert('RGBA').crop((w // 2, 0, 3 * w // 4, h // 4))
    bounds = tile.getchannel('A').point(lambda alpha: 255 if alpha > 110 else 0).getbbox()
    return tile.crop(bounds)


def render():
    pose = idle_pose()
    encoded = BytesIO()
    pose.save(encoded, format='PNG', optimize=True)
    data = b64encode(encoded.getvalue()).decode('ascii')
    height = 149
    width = height * pose.width / pose.height
    actor = '<ellipse cx="121" cy="194" rx="45" ry="6" fill="#e4d9f5"/>'
    actor += (f'<image id="hero" x="{121 - width/2:.2f}" y="44" width="{width:.2f}" height="{height}" '
              f'href="data:image/png;base64,{data}"/>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 292" width="1000" height="292" '
            'role="img" aria-label="程序员梦哥 WorkBuddy 组件着陆">'
            + creative.assembly(actor, heading=None) + '</svg>\n')


def main():
    art = render()
    (OUT / 'intro.svg').write_text(art, encoding='utf-8')
    template = (creative.s.PREVIOUS / 'preview.template.html').read_text(encoding='utf-8')
    template = template.replace('程序员梦哥 · WorkBuddy 片头三案', '程序员梦哥 · 组件着陆修订版')
    template = template.replace('6.4', '8.4').replace('4.35', '6.48').replace('同步重播', '从头重播')
    template = template.replace('<main class="samples">', '<main class="samples" style="max-width:770px">')
    card = f'<article>{art}<p><a href="intro.svg" download>下载 SVG</a></p></article>'
    (OUT / 'preview.html').write_text(template.replace('<!-- samples -->', card), encoding='utf-8')


if __name__ == '__main__':
    main()
