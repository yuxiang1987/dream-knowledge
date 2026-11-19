"""Render three independent creative directions for the same seven WorkBuddy settings."""
from importlib.util import module_from_spec, spec_from_file_location
from math import cos, radians, sin
from pathlib import Path

OUT = Path(__file__).resolve().parent
BASE = OUT.parent / 'mengge-workbuddy-seven-settings'
SPEC = spec_from_file_location('seven_settings', BASE / 'build.py')
s = module_from_spec(SPEC)
SPEC.loader.exec_module(s)
from build import INK, WHITE, avatar, dot, group, lettering, path, rect

DUR = 8.4
TIMES = tuple(1.48 + .71 * i for i in range(7))
LABELS = ('存储路径', '自定义指令', '回复风格', '人设记忆', '记忆进化', '窗口模型', '数据导入')
ACTIONS = ('安放文件', '写下规则', '切换语气', '记住偏好', '沉淀流程', '调节档位', '接入数据')
PALETTE = ('#2059c6', '#6c3dcc', '#a03475', '#a34822', '#007a75', '#3e56ad', '#35782c')
PAPERS = ('#dceaff', '#e9e2ff', '#fce1ee', '#ffe3d0', '#d1f2e9', '#dfe6ff', '#e1f1d6')
EASE_OUT = '.16 .7 .22 1'


def track(attr, frames, kind=None, curve=EASE_OUT):
    return s.anim(attr, frames, kind=kind, curve=curve)


def window(index):
    start = TIMES[index]
    frames = [(start - .17, 0), (start + .10, 1)]
    if index < 6:
        frames += [(start + .46, 1), (start + .54, 0)]
    return track('opacity', frames)


def place(art, x, y, scale=1):
    return group(art, transform=f'translate({x} {y}) scale({scale})')


def icon(index, ink, size=1, x=0, y=0):
    return place(s.STOPS[index][2](ink, TIMES[index]), x, y, size)


def ellipse(cx, cy, rx, ry, stroke, width=1, fill='none', dash=''):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{width}"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>')


def opener(color, accent, x=245, y=98):
    text = lettering(x, y, '程序员梦哥', 29, color) + lettering(x-4, y+76, '分享 AI、少踩坑', 64, accent)
    timing = track('opacity', [(.81, 1), (1.31, 0), (7.66, 0), (8.21, 1)])
    offset = track('transform', [(.80, '0 0'), (1.29, '0 -11'), (7.67, '0 8'), (8.22, '0 0')], 'translate')
    return group(timing + offset + text, ident='brand')


def stage(body):
    return group(s.fade(1.05, 1.43, 7.06, 7.68) + body, ident='scene', opacity=0)


def dark_orbit():
    bg = rect(0, 0, 1000, 292, 0, '#0b1530')
    bg += path('M0 250H1000M182 34V257', '#233b60', 2) + path('M30 29h96M30 260h71', '#365484', 2)
    actor = place(avatar(), 13, 35, .87)
    ring = ellipse(763, 145, 168, 102, '#375683', 2) + ellipse(763, 145, 148, 82, '#243e67', 1, dash='4 8')
    ring += ellipse(763, 145, 118, 64, '#1c345b', 1)
    ring += path('M575 145h376M763 27v235', '#28466a', 1.5) + dot(763, 145, 7, '#73c4ff')
    angles = (-154, -107, -59, -13, 39, 93, 146)
    sweep = track('transform', [(1.15, -173), *zip(TIMES, angles), (6.77, 172)], 'rotate', curve='0 0 1 1')
    cursor = group(sweep + path('M0 0H168', '#48a2e0', 2) + dot(168, 0, 12, '#1e4377')
                   + dot(168, 0, 6, '#8ef7ff'), ident='sweep')
    # Rotate in a circular coordinate system, then project to an ellipse.
    ring += group(cursor, transform='translate(763 145) scale(1 .607143)')
    for i, a in enumerate(angles):
        x, y = 763+168*cos(radians(a)), 145+102*sin(radians(a))
        hit = track('opacity', [(TIMES[i]-.08, 0), (TIMES[i]+.15, 1)])
        ring += dot(round(x,2), round(y,2), 5, '#526f9f')
        ring += group(hit + dot(round(x,2), round(y,2), 5.5, '#a1e7ff'), ident=f'node-{i}', opacity=0)
    hub = ellipse(261, 139, 56, 56, '#42689e', 2, '#14294a') + ellipse(261, 139, 65, 65, '#305687', 2, dash='5 9')
    views = []
    for i, (label, t) in enumerate(zip(LABELS, TIMES)):
        kick = track('transform', [(t-.17, '-12 0'), (t+.11, '2 0'), (t+.28, '0 0')], 'translate')
        live = icon(i, '#8ceaff', 1.14, 261, 139)
        live += group(kick + lettering(340, 153, label, 46, '#eff8ff'))
        live += lettering(342, 189, f'0{i+1} / 07', 24, '#88b6e4', False)
        views.append(group(window(i) + live, ident=f'feature-{i}', opacity=0))
    return bg + actor + opener('#a8bde0', '#e9f7ff') + stage(ring + hub + ''.join(views))


# Same point topology throughout: the outline itself interpolates, instead of cutting between seven plates.
SILHOUETTES = (
    ((-112,-50),(-35,-50),(-17,-32),(111,-32),(111,71),(-112,71),(-112,44),(-112,0)),
    ((-70,-80),(33,-80),(68,-49),(68,74),(-70,74),(-70,37),(-70,0),(-70,-36)),
    ((-117,-64),(116,-64),(116,54),(12,54),(-38,83),(-37,54),(-117,54),(-117,0)),
    ((-109,-73),(63,-73),(109,-41),(109,63),(78,77),(-109,77),(-109,36),(-109,-29)),
    ((0,-90),(74,-47),(104,10),(61,68),(0,90),(-69,58),(-104,2),(-70,-54)),
    ((-126,-72),(125,-72),(125,54),(39,54),(39,83),(-39,83),(-39,54),(-126,54)),
    ((-109,-24),(-53,-24),(-33,0),(32,0),(52,-24),(109,-24),(109,70),(-109,70)),
)


def outline(points):
    return 'M' + ' L'.join(f'{x} {y}' for x, y in points) + ' Z'


def shape_shifter():
    bg = rect(0, 0, 1000, 292, 0, '#fffdf7')
    bg += path('M24 25H976V267H24Z M165 46V248 M615 45V249', '#e7dfce', 2)
    for x, y in ((34, 35), (966, 35), (34, 257), (966, 257)):
        bg += dot(x, y, 3, '#b9aa8f')
    actor = place(avatar(), 5, 53, .8)
    shapes = [outline(p) for p in SILHOUETTES]
    edges = [(1.16, shapes[0])]
    pigments = [(1.16, PAPERS[0])]
    for i, t in enumerate(TIMES[1:], 1):
        edges += [(t-.22, shapes[i-1]), (t+.11, shapes[i])]
        pigments += [(t-.22, PAPERS[i-1]), (t+.11, PAPERS[i])]
    form = (f'<path id="surface" d="{shapes[0]}" fill="{PAPERS[0]}" stroke="#6b6558" stroke-width="3" stroke-linejoin="round">'
            + track('d', edges) + track('fill', pigments) + '</path>')
    views = []
    for i, (label, t) in enumerate(zip(LABELS, TIMES)):
        tick = group(window(i) + rect(0, 0, 27, 4, 2, PALETTE[i]), opacity=0)
        active = lettering(660, 82, f'0{i+1} / 07', 27, PALETTE[i], False)
        active += lettering(657, 151, label, 57 if len(label) == 4 else 49)
        active += lettering(660, 203, ACTIONS[i], 32, PALETTE[i])
        active += place(tick, 663 + 36*i, 227)
        views.append(group(window(i) + icon(i, PALETTE[i], 1.45, 386, 139) + active,
                           ident=f'feature-{i}', opacity=0))
    foundation = ellipse(386, 234, 136, 12, '#eee7d7', 1, '#f6f0e4')
    foundation += path('M242 145h288M386 39v204', '#e5dac6', 1.5)
    body = foundation + place(form, 386, 139) + ''.join(views)
    return bg + actor + opener('#665d4e', INK) + stage(body)


def assembly(brand_actor=None, *, heading='七项设置'):
    bg = rect(0, 0, 1000, 292, 0, '#f0eafe')
    bg += path('M0 230L1000 171V292H0Z', 'none', fill='#e5ddfa')
    bg += rect(23, 20, 954, 249, 22, '#f8f4ff', '#d9cef1')
    coords = ((332,78),(514,78),(696,78),(878,78),(422,206),(604,206),(786,206))
    frame = path('M259 139H947M352 252H859', '#ddd1f1', 2)
    if heading:
        frame += lettering(56, 132, heading, 37, '#4c347a')
    frame += lettering(57, 171 if brand_actor is None else 221, 'WorkBuddy', 24, '#756492', False)
    scene_actor = place(avatar(), 60, 10, .42) if brand_actor is None else ''
    tiles = []
    for i, ((x,y),t) in enumerate(zip(coords,TIMES)):
        offset = (-119 if i % 2 == 0 else 112)
        landing = track('transform', [(t-.43, f'{offset} -73'), (t+.14, '0 6'), (t+.39, '0 0')], 'translate')
        tilt = track('transform', [(t-.43, -17 if i%2 == 0 else 17), (t+.14, 4 if i%2 == 0 else -4), (t+.39, 0)], 'rotate')
        opacity = track('opacity', [(t-.41, 0), (t-.07, 1)])
        tile = rect(-76, -51, 152, 108, 16, '#dbd0ee') + rect(-76,-55,152,105,16, WHITE, '#ddd3ef')
        tile += rect(-70, -49, 140, 61, 12, PAPERS[i]) + icon(i, PALETTE[i], .82, 0, -17)
        size = 27 if len(LABELS[i]) == 5 else 30
        tile += lettering(-len(LABELS[i]) * size/2, 39, LABELS[i], size, '#3d2f58')
        tiles.append(place(group(opacity + landing + group(tilt + tile), ident=f'tile-{i}', opacity=0), x, y))
    seal = group(track('opacity', [(5.90, 0), (6.21, 1)]) + path('M38 30V15h18M963 30V15h-18M38 252v16h18M963 252v16h-18', '#8f6ec4', 4), ident='lock', opacity=0)
    return (bg + (brand_actor or '') + opener('#6a5189', '#412765', 245, 105)
            + stage(frame + scene_actor + ''.join(tiles) + seal))


VARIANTS = (
    ('a', '01 · 暗夜轨道', '坐标雷达扫过七个节点，左侧像仪表读数一样切换图标和短名称。', dark_orbit),
    ('b', '02 · 一纸七变', '同一张纸的轮廓连续折成文件夹、气泡、窗口等七种道具。', shape_shifter),
    ('c', '03 · 组件着陆', '七块立体组件交错飞入、回弹归位，最终拼成一台设置面板。', assembly),
)


def main():
    cards = []
    for code, title, desc, create in VARIANTS:
        art = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 292" width="1000" height="292" '
               f'role="img" aria-label="WorkBuddy 七项设置 · {title}">' + create() + '</svg>\n')
        (OUT / f'{code}.svg').write_text(art, encoding='utf-8')
        # Inline variants have separate ID namespaces on the comparison page.
        indexed = art.replace(' id="', f' id="{code}-')
        cards.append(f'<article><h2>{title}</h2>{indexed}<p>{desc}</p><a href="{code}.svg" download>下载 SVG</a></article>')
    page = (s.PREVIOUS / 'preview.template.html').read_text(encoding='utf-8')
    page = page.replace('程序员梦哥 · WorkBuddy 片头三案', 'WorkBuddy 七项设置 · 三种动效创意')
    page = page.replace('6.4', str(DUR)).replace('1.45', '2.40').replace('2.75', '4.08').replace('4.35', '6.48')
    page = page.replace('定格：转场', '定格：前段').replace('定格：动作', '定格：中段').replace('定格：结果', '定格：收尾')
    (OUT / 'preview.html').write_text(page.replace('<!-- samples -->', '\n'.join(cards)), encoding='utf-8')


if __name__ == '__main__':
    main()
