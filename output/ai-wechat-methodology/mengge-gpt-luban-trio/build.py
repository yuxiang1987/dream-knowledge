"""Three loopable openers cut from the archived Luban article art, no generated claims."""
from base64 import b64encode
from importlib.util import module_from_spec, spec_from_file_location
from io import BytesIO
from math import cos, radians, sin
from pathlib import Path

from PIL import Image

OUT = Path(__file__).resolve().parent
ASSETS = OUT.parents[2] / 'raw/article/程序员梦哥/assets/我用GPT Image 2.6 手搓了一套鲁班皮肤'
PREVIOUS = OUT.parent / 'mengge-workbuddy-creative-trio'
SPEC = spec_from_file_location('creative_trio', PREVIOUS / 'build.py')
creative = module_from_spec(SPEC)
SPEC.loader.exec_module(creative)
from build import WHITE, dot, group, lettering, path, rect

DUR = 8.4
CYAN = '#7feaff'
NAVY = '#0a234b'
CORAL = '#bb5624'


def still(name, box=None, frame=0, max_size=(600, 420)):
    with Image.open(ASSETS / name) as im:
        im.seek(frame)
        art = im.convert('RGB')
    if box:
        art = art.crop(box)
    art.thumbnail(max_size, Image.Resampling.LANCZOS)
    data = BytesIO()
    art.save(data, 'JPEG', quality=88, optimize=True)
    return 'data:image/jpeg;base64,' + b64encode(data.getvalue()).decode('ascii')


def image(data, x, y, w, h, clip=None):
    restriction = f' clip-path="url(#{clip})"' if clip else ''
    return (f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{data}" '
            f'preserveAspectRatio="xMidYMid slice"{restriction}/>')


def motion(frames):
    return creative.track('transform', frames, 'translate')


def visibility(start, visible, hold=7.0, gone=7.75):
    return creative.s.fade(start, visible, hold, gone)


def identity(bg, label, product, color):
    brand = lettering(57, 63, '程序员梦哥', 24, color) + rect(56, 77, 47, 4, 2, color)
    stage = lettering(54, 157, label, 62, bg) + lettering(57, 218, product, 31, color, False)
    return brand + group(visibility(.55, 1.26) + motion([(.54, '-13 0'), (1.24, '0 0')]) + stage, opacity=0)


def splash():
    # An iris and a path trace turn the water ripple into the portrait frame.
    hero = still('file-20261113221404779.png', (18, 49, 1008, 1024), max_size=(490, 490))
    mask = 'dive-window'
    aperture = (f'<defs><clipPath id="{mask}"><circle cx="756" cy="148" r="0" id="iris">'
                + creative.track('r', [(1.34, 0), (1.86, 47), (2.73, 118), (3.04, 106), (7.10, 106), (7.86, 0)])
                + '</circle></clipPath></defs>')
    bg = rect(0, 0, 1000, 312, 0, '#071a3c')
    bg += path('M0 248Q185 187 319 243T641 249T1000 219V312H0Z', 'none', fill='#0d3158')
    bg += path('M0 280Q168 222 330 269T640 273T1000 249', '#1a5074', 2)
    bg += identity('#e9f9ff', '深海换装', 'GPT Image 2.6', CYAN)
    blob = (dot(0, 0, 20, '#10395f') + dot(0, 0, 11, CYAN) + dot(-3, -3, 4, WHITE)
            + creative.track('opacity', [(.78, 0), (1.03, 1), (1.64, 1), (1.90, 0)]))
    blob = group(motion([(.73, '756 -26'), (1.52, '756 149'), (1.85, '756 148')]) + blob)
    art = group(motion([(1.42, '0 42'), (2.58, '0 -5'), (3.08, '0 0')]) + image(hero, 630, 22, 251, 252), ident='hero')
    portal = group(art, opacity=None)
    portal = f'<g clip-path="url(#{mask})">{portal}</g>'
    halo = '<circle cx="756" cy="148" r="114" fill="none" stroke="#72e5ff" stroke-width="3" opacity="0">'
    halo += visibility(1.92, 2.78) + creative.track('stroke-dasharray', [(1.88, '0 730'), (3.02, '730 730')]) + '</circle>'
    ring = '<ellipse cx="756" cy="148" rx="122" ry="115" fill="none" stroke="#588fae" opacity="0">'
    ring += visibility(2.12, 3.02) + '</ellipse>'
    spray = []
    for i in range(12):
        a = radians(17 + 29*i)
        t = 2.14 + (i%4)*.035
        x, y = 756 + cos(a)*81, 148 + sin(a)*81
        dx, dy = cos(a)*(41+i%3*17), sin(a)*(37+i%3*14)
        spray.append(group(creative.s.fade(t, t+.14, t+.25, t+.90)
                           + motion([(t,'0 0'), (t+.85,f'{dx:.2f} {dy:.2f}')])
                           + dot(round(x,2), round(y,2), 3+i%4, CYAN), opacity=0))
    return bg + aperture + portal + ring + halo + ''.join(spray) + blob


def edit_scan():
    original = still('file-20261113221404779.png')
    edited = still('鲁班鲸鱼帽局部改色结果.png', (56, 372, 536, 692), max_size=(480, 320))
    x, y, w, h = 562, 23, 386, 257
    bg = rect(0, 0, 1000, 312, 0, '#fff6ea') + path('M24 20H978V291H24Z M529 36V273', '#ead9c9', 2)
    bg += identity('#322d2b', '只改鲸鱼帽', '蓝色 → 珊瑚橙', CORAL)
    frame = '<defs><clipPath id="edit-frame"><rect x="562" y="23" width="386" height="257" rx="13"/></clipPath>'
    sweep = [(2.28, 0), (4.24, w), (7.10, w), (7.87, 0)]
    frame += ('<clipPath id="edit-wipe"><rect x="562" y="23" width="0" height="257" id="reveal">'
              + creative.track('width', sweep) + '</rect></clipPath></defs>')
    board = image(original, x, y, w, h)
    board += image(edited, x, y, w, h, 'edit-wipe')
    board = f'<g clip-path="url(#edit-frame)">{board}</g>'
    border = rect(x, y, w, h, 13, 'none', '#ccb7a6')
    scanner = path(f'M{x} 32V270', '#fff4e8', 2) + dot(x, 151, 11, '#fff7ef') + dot(x, 151, 5, '#f38b59')
    scanner = group(creative.s.fade(2.12, 2.34, 4.16, 4.43) + motion([(t, f'{xpos} 0') for t,xpos in sweep]) + scanner,
                    opacity=0)
    guide = path('M621 53h-14v14m105-14h14v14M607 111v14h14m105 0h-14', '#fff0d2', 3)
    guide = group(creative.s.fade(1.43, 1.76, 2.17, 2.58) + guide, opacity=0)
    chips = dot(74, 253, 11, '#315f9c') + path('M92 253h28m-7-5 7 5-7 5', '#af8265', 2) + dot(140, 253, 11, '#ed935b')
    return bg + frame + group(visibility(.32, 1.11) + board + border + scanner + guide + chips, ident='scene', opacity=0)


def film_reel():
    frames = (
        ('皮肤设定', still('file-20261113221404779.png')),
        ('武器拆解', still('file-20261113223104137.png')),
        ('技能动效', still('鲁班大鱼四技能.gif', frame=20)),
        ('表情包', still('file-20261113223654182.png', (26, 28, 748, 490))),
    )
    bg = rect(0, 0, 1000, 312, 0, '#152032') + rect(0, 0, 1000, 33, 0, '#081424')
    bg += rect(0, 278, 1000, 34, 0, '#081424')
    for hole in range(16, 1000, 48):
        bg += rect(hole, 10, 24, 11, 3, '#385166') + rect(hole, 289, 24, 11, 3, '#385166')
    bg += lettering(49, 77, '程序员梦哥', 23, '#9cb8cd')
    bg += lettering(47, 142, '深海造梦', 53, '#e8f8ff')
    bg += lettering(49, 191, 'GPT Image 2.6', 28, '#83cee2', False)
    box = '<defs><clipPath id="film-aperture"><rect x="333" y="42" width="634" height="226" rx="14"/></clipPath></defs>'
    slots = []
    w, gap = 337, 25
    for i, (label, photo) in enumerate(frames):
        x = 474 + (w+gap)*i
        slots.append(rect(x, 44, w, 224, 12, '#294258') + image(photo, x+6, 50, w-12, 181)
                     + lettering(x+14, 258, label, 27, '#e4f8fd'))
    stops = [(1.52, '0 0'), (2.75, '0 0'), (3.11, '-362 0'), (4.03, '-362 0'),
             (4.39, '-724 0'), (5.34, '-724 0'), (5.70, '-1086 0'), (6.60, '-1086 0'), (7.29, '-1510 0')]
    strip = '<g clip-path="url(#film-aperture)">' + group(motion(stops) + ''.join(slots), ident='reel') + '</g>'
    stripe = rect(451, 44, 383, 225, 16, 'none', '#70d8ec')
    return bg + box + group(visibility(.43, 1.18) + strip + stripe, ident='scene', opacity=0)


VARIANTS = (
    ('a','01 · 深海换装','一颗水滴撞开涟漪，涟漪撑成舷窗，原画鲁班从水下浮出。',splash),
    ('b','02 · 只改鲸鱼帽','珊瑚色扫描线扫过原图，揭示文章里的局部改色结果。',edit_scan),
    ('c','03 · 深海放映机','把皮肤设定、武器拆解、技能动效和表情包剪成一卷连续推进的胶片。',film_reel),
)


def main():
    cards = []
    for code, title, desc, scene in VARIANTS:
        art = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 312" width="1000" height="312" '
               f'role="img" aria-label="GPT Image 鲁班 · {title}">' + scene() + '</svg>\n')
        (OUT/f'{code}.svg').write_text(art, encoding='utf-8')
        cards.append(f'<article><h2>{title}</h2>{art}<p>{desc}</p><a href="{code}.svg" download>下载 SVG</a></article>')
    page = (creative.s.PREVIOUS/'preview.template.html').read_text(encoding='utf-8')
    page = page.replace('程序员梦哥 · WorkBuddy 片头三案', 'GPT Image · 鲁班皮肤片头三案')
    page = page.replace('6.4', str(DUR)).replace('1.45', '1.64').replace('2.75', '3.15').replace('4.35', '5.87')
    page = page.replace('动作示意，不是产品录屏', '复用文章原画 · 创意剪辑，不是产品录屏')
    (OUT/'preview.html').write_text(page.replace('<!-- samples -->','\n'.join(cards)), encoding='utf-8')


if __name__ == '__main__':
    main()
