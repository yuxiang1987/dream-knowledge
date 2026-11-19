"""Build standalone SVGs and their inline preview. Requires Pillow + fonttools, Windows Microsoft YaHei."""
from collections import defaultdict
from functools import lru_cache
from html import escape
from pathlib import Path
from random import Random
import os

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from PIL import Image

OUT = Path(__file__).resolve().parent
SPRITE = OUT.parent / '程序员拾梦闯关片头五案-v1' / 'sprite-idle.png'
DURATION = 6.4
INK = '#172f4e'
MID = '#506885'
BLUE = '#2460d6'
CYAN = '#007e85'
PALE = '#edf5ff'
LINE = '#c5d8ee'
WHITE = '#fff'
EASE = '.42 0 .24 1'
OUTWARD = '.17 .68 .3 1'


def num(n):
    return f'{n:.6f}'.rstrip('0').rstrip('.') or '0'


def tween(attr, frames, *, kind=None, dur=DURATION, curve=EASE):
    assert frames[0][0] == 0 and frames[-1][0] == dur
    tag = 'animateTransform' if kind else 'animate'
    kind_attr = f' type="{kind}"' if kind else ''
    times = ';'.join(num(t / dur) for t, _ in frames)
    values = ';'.join(str(v) for _, v in frames)
    splines = ';'.join([curve] * (len(frames) - 1))
    return (f'<{tag} attributeName="{attr}"{kind_attr} dur="{dur}s" repeatCount="indefinite" '
            f'calcMode="spline" keyTimes="{times}" values="{values}" keySplines="{splines}"/>')


def alpha(start, stable, hold, end):
    return tween('opacity', [(0, 0), (start, 0), (stable, 1), (hold, 1), (end, 0), (DURATION, 0)])


def move(start, stable, initial, final='0 0', *, settle=None):
    frames = [(0, initial), (start, initial), (stable, final if settle is None else settle)]
    if settle is not None:
        frames.append((stable + .24, final))
    return tween('transform', frames + [(DURATION, final)], kind='translate', curve=OUTWARD)

def group(content, *, transform='', ident='', opacity=None):
    if transform:
        return f'<g transform="{transform}">{group(content, ident=ident, opacity=opacity)}</g>'
    attrs = f' id="{ident}"' if ident else ''
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    return f'<g{attrs}>{content}</g>'


def rect(x, y, w, h, radius, fill, stroke='none'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'


def path(d, stroke, width=3, fill='none'):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>'


def dot(x, y, r, color):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'


@lru_cache
def font(bold):
    fonts = Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts'
    f = TTFont(fonts / ('msyhbd.ttc' if bold else 'msyh.ttc'), fontNumber=0)
    return f.getGlyphSet(), f.getBestCmap(), f['head'].unitsPerEm


@lru_cache
def glyph(char, bold):
    glyphs, cmap, _ = font(bold)
    item = glyphs[cmap[ord(char)]]
    pen = SVGPathPen(glyphs, ntos=num)
    item.draw(pen)
    return item.width, pen.getCommands()


def lettering(x, baseline, content, size, fill=INK, bold=True):
    scale = size / font(bold)[2]
    pen_x = 0
    shapes = []
    for char in content:
        width, outline = glyph(char, bold)
        if outline:
            shapes.append(f'<path transform="translate({pen_x} 0)" d="{outline}"/>')
        pen_x += width
    return (f'<g aria-label="{escape(content, quote=True)}" fill="{fill}" '
            f'transform="translate({x} {baseline}) scale({num(scale)} {num(-scale)})">{"".join(shapes)}</g>')


@lru_cache
def avatar():
    with Image.open(SPRITE) as original:
        sprite = original.convert('RGBA').resize((29, 59), Image.Resampling.LANCZOS).quantize(colors=48)
    rgba = sprite.convert('RGBA')
    fills = defaultdict(list)
    for y in range(rgba.height):
        x = 0
        while x < rgba.width:
            color = rgba.getpixel((x, y))
            end = x + 1
            while end < rgba.width and rgba.getpixel((end, y)) == color:
                end += 1
            if color[3] >= 96:
                fills[color[:3]].append(f'M{x} {y}h{end-x}v1h{x-end}Z')
            x = end
    paths = ''.join(f'<path fill="#{r:02x}{g:02x}{b:02x}" d="{"".join(parts)}"/>' for (r, g, b), parts in fills.items())
    bob = tween('transform', [(0, '0 0'), (.8, '0 -2.7'), (1.6, '0 0')], kind='translate', dur=1.6)
    return ('<ellipse cx="96" cy="194" rx="43" ry="6" fill="#e1ecfb"/>'
            + group(bob + '<g transform="scale(2.7)" shape-rendering="crispEdges">' + paths + '</g>', transform='translate(57 31)'))


def brand(color, prefix):
    slogan = (lettering(211, 89, '程序员梦哥', 29, MID) + lettering(207, 157, '分享 AI、', 65)
              + lettering(507, 157, '少踩坑', 65, color) + rect(211, 180, 54, 5, 2.5, color))
    visibility = tween('opacity', [(0, 1), (1.08, 1), (1.65, 0), (5.72, 0), (6.18, 1), (DURATION, 1)])
    rng = Random(19)
    bits = []
    for j in range(30):
        x = rng.randrange(218, 720)
        y = rng.randrange(109, 161)
        start = 1.08 + .24 * (x - 218) / 502
        end = start + rng.uniform(.34, .59)
        landing = f'{rng.randrange(34, 182)} {rng.randrange(-40, 47)}'
        bits.append(group(alpha(start, start + .13, start + .20, end) + move(start, end, '0 0', landing)
                          + rect(x, y, rng.randrange(4, 9), rng.randrange(4, 8), 1, color if j % 3 else LINE), opacity=0))
    return group(visibility + slogan, ident=f'{prefix}-brand') + ''.join(bits)


def check():
    return dot(0, 0, 20, '#e3f8f6') + path('M-8 0l6 6 11-12', CYAN, 4)


def arrival(content, start=1.42, stable=2.03, initial='-24 0', *, settle=None):
    return group(move(start, stable, initial, settle=settle) + content)


def a_scene():
    # A click compresses the choice, then the replacement reply slides into the same panel.
    header = lettering(224, 60, '回复风格', 36) + lettering(407, 60, 'WorkBuddy', 24, MID, False)
    chip_inactive = rect(0, 0, 233, 49, 24, PALE, LINE) + lettering(47, 34, '高效务实', 30, BLUE)
    chip_active = rect(0, 0, 233, 49, 24, BLUE) + lettering(47, 34, '高效务实', 30, WHITE) + dot(24, 24, 5, WHITE)
    chip_state = group(alpha(2.53, 2.78, 5.71, 5.91) + chip_active, ident='a-picked', opacity=0)
    pop = tween('transform', [(0, '1 1'), (2.47, '1 1'), (2.58, '.94 .94'), (2.76, '1.035 1.035'),
                              (2.99, '1 1'), (DURATION, '1 1')], kind='scale')
    chip = group(group(pop + group(chip_inactive + dot(24, 24, 5, LINE) + chip_state, transform='translate(-117 -24)'),
                       ident='a-chip'), transform='translate(823 53)')
    panel = rect(221, 87, 731, 107, 21, WHITE, LINE)
    old = group(tween('opacity', [(0, 1), (2.54, 1), (2.93, 0), (DURATION, 0)])
                + move(2.54, 2.93, '0 0', '0 -13') + lettering(249, 132, '有几种做法，先说背景…', 32, MID, False)
                + rect(249, 151, 308, 7, 3, LINE) + rect(249, 169, 226, 7, 3, PALE), ident='a-old')
    new = group(alpha(2.70, 3.15, 5.56, 5.89) + move(2.70, 3.18, '0 18', settle='0 -2')
                + lettering(249, 155, '结论：先用方案 A。', 46) + group(check(), transform='translate(894 141)'),
                ident='a-new', opacity=0)
    cursor = group(alpha(1.98, 2.22, 2.74, 3.04) + move(2.00, 2.53, '112 52', '0 0')
                   + path('M799 66v33l8-8 7 13 5-3-7-13h12Z', WHITE, 2, INK), opacity=0)
    return arrival(header + panel + old + new + chip + cursor)


def b_scene():
    header = lettering(214, 55, '把常用要求写进个性化', 35)
    track = path('M536 133H620', LINE, 4) + path('M611 124l9 9-9 9', LINE, 4)
    card = rect(-115, -33, 230, 65, 13, WHITE, '#90bdf3') + dot(-95, -1, 5, BLUE)
    card += lettering(-76, 11, '先给结论', 32, BLUE)
    drift = tween('transform', [(0, '0 0'), (2.30, '0 0'), (2.54, '17 -19'), (3.13, '319 0'),
                                (3.29, '326 0'), (3.49, '319 0'), (DURATION, '319 0')], kind='translate', curve=OUTWARD)
    tilt = tween('transform', [(0, 0), (2.30, 0), (2.54, -8), (3.11, 1.5), (3.47, 0), (DURATION, 0)], kind='rotate')
    card = group(drift + group(tilt + card), ident='b-card', transform='translate(445 134)')
    slot = rect(0, 0, 302, 125, 17, WHITE, LINE) + lettering(19, 32, '个性化', 26, MID)
    slot += '<rect x="17" y="45" width="268" height="70" rx="14" fill="#edf5ff" stroke="#b6cdeb" stroke-width="2" stroke-dasharray="6 5"/>'
    bounce = move(3.08, 3.23, '0 0', settle='0 4')
    slot = group(bounce + slot, transform='translate(613 76)')
    confirmed = group(alpha(3.23, 3.58, 5.55, 5.92) + move(3.23, 3.63, '0 9', settle='0 -2')
                      + check(), transform='translate(919 82)', ident='b-done', opacity=0)
    return arrival(header + track + slot + card + confirmed, initial='0 13')


def c_scene():
    header = lettering(214, 56, '长任务，留一张进度卡', 35)
    rail = path('M493 140H706', LINE, 5)
    progress = ('<path d="M493 140H706" fill="none" stroke="#007e85" stroke-width="5" stroke-linecap="round" '
                'pathLength="100" stroke-dasharray="100" stroke-dashoffset="100" id="c-line">'
                + tween('stroke-dashoffset', [(0, 100), (2.62, 100), (3.60, 0), (DURATION, 0)], curve=OUTWARD) + '</path>')
    left = rect(213, 94, 220, 91, 17, WHITE, LINE) + dot(240, 139, 6, CYAN) + lettering(261, 151, '这次做到', 32)
    right = rect(718, 94, 233, 91, 17, WHITE, LINE) + lettering(742, 151, '下次接着做', 32)
    sheet = rect(-36, -27, 72, 53, 9, '#e5f7f5', '#83c9c7') + path('M-18-8h33m-33 14h25', CYAN, 4)
    travel = tween('transform', [(0, '0 7'), (2.15, '0 7'), (2.52, '26 -16'), (3.60, '223 0'),
                                 (3.79, '229 0'), (4.02, '223 0'), (DURATION, '223 0')], kind='translate')
    ticket = group(alpha(2.03, 2.36, 3.51, 3.78) + travel + sheet, ident='c-ticket', transform='translate(492 140)', opacity=0)
    landing = group(move(3.56, 3.72, '0 0', settle='5 0') + right)
    status = group(alpha(3.63, 4.01, 5.53, 5.96) + move(3.63, 4.01, '0 10', settle='0 -2')
                   + check(), ident='c-done', transform='translate(932 96)', opacity=0)
    return arrival(header + left + rail + progress + ticket + landing + status, initial='0 13')


VARIANTS = (
    ('a', '01 · 结论先行', '选中「高效务实」，回复从讲背景切到先给结论。', BLUE, a_scene),
    ('b', '02 · 偏好入槽', '「先给结论」指令卡翻身滑入「个性化」，落槽后打勾。', BLUE, b_scene),
    ('c', '03 · 进度接力', '任务进度卡沿时间线送到下次会话，演示手动记台账的做法。', CYAN, c_scene),
)


def svg(prefix, title, desc, color, scene):
    scene_layer = group(alpha(1.42, 1.99, 5.30, 5.80) + scene(), ident=f'{prefix}-scene', opacity=0)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 216" width="1000" height="216" '
            f'role="img" aria-label="{escape(title + "：" + desc, quote=True)}">'
            + rect(0, 0, 1000, 216, 0, WHITE) + path('M178 38V181', '#e5edf7', 2)
            + avatar() + brand(color, prefix) + scene_layer + '</svg>\n')


def main():
    cards = []
    for prefix, title, desc, color, scene in VARIANTS:
        artwork = svg(prefix, title, desc, color, scene)
        (OUT / f'{prefix}.svg').write_text(artwork, encoding='utf-8')
        cards.append(f'<article><h2>{title}</h2>{artwork}<p>{desc}</p>'
                     f'<a href="{prefix}.svg" download>下载 SVG</a></article>')
    template = (OUT / 'preview.template.html').read_text(encoding='utf-8')
    (OUT / 'preview.html').write_text(template.replace('<!-- samples -->', '\n'.join(cards)), encoding='utf-8')


if __name__ == '__main__':
    main()
