"""Build a word-light, seven-stop WorkBuddy opener (Pillow, fonttools, Microsoft YaHei)."""
from pathlib import Path
from random import Random
import sys

OUT = Path(__file__).resolve().parent
PREVIOUS = OUT.parent / 'mengge-workbuddy-svg-trio'
sys.path.insert(0, str(PREVIOUS))
from build import BLUE, CYAN, EASE, MID, WHITE, avatar, dot, group, lettering, path, rect, tween

DUR = 8.4
START = 207
END = 961
Y = 161
TRACK = '#c4d8f2'
SKY = '#eaf3ff'
GLOW = '#ffd85d'


def anim(attr, frames, *, kind=None, curve=EASE):
    return tween(attr, [(0, frames[0][1]), *frames, (DUR, frames[-1][1])], kind=kind, dur=DUR, curve=curve)


def fade(start, full, hold, gone):
    return anim('opacity', [(start, 0), (full, 1), (hold, 1), (gone, 0)])


def shift(art, t, initial, settle='0 -3'):
    return group(anim('transform', [(t, initial), (t + .27, settle), (t + .45, '0 0')], kind='translate') + art)


def turn(art, t, initial, settle):
    return group(anim('transform', [(t, initial), (t + .30, settle), (t + .48, 0)], kind='rotate') + art)


def scale(art, t):
    return group(anim('transform', [(t, '.56 .56'), (t + .27, '1.12 1.12'), (t + .45, '1 1')], kind='scale') + art)


def star(color):
    return path('M0-12Q2-2 12 0Q2 2 0 12Q-2 2-12 0Q-2-2 0-12Z', color, 2, color)


def folder(c, t):
    base = path('M-34-3v-12h23l7 6h35v25h-65Z', c, 3.5, WHITE)
    arrow = path('M-3 3h20m-6-6 6 6-6 6', c, 3.5)
    return shift(base + arrow, t, '-10 8', '3 -3')


def instruction(c, t):
    paper = rect(-13, -25, 26, 50, 5, WHITE, c) + path('M-6-11H6M-6 0H6M-6 11H4', c)
    left = shift(path('M-21-15h-8v30h8', c, 3.5), t, '-10 0', '2 0')
    right = shift(path('M21-15h8v30h-8', c, 3.5), t, '10 0', '-2 0')
    return paper + left + right


def reply(c, t):
    bubble = path('M-30-19h60v33H-6l-10 10V14h-14Z', c, 3.5, WHITE)
    guide = path('M-17-8h30', c, 4)
    line = path('M0 0h31', c, 3.7)
    shrink = anim('transform', [(t, '1 1'), (t + .27, '.4 1'), (t + .44, '.56 1')], kind='scale')
    return bubble + guide + group(shrink + line, transform='translate(-17 4)')


def persona(c, t):
    head = dot(-8, -10, 12, c) + path('M-30 19Q-29 4-8 4T15 19', c, 3.7)
    badge = dot(20, 12, 13, WHITE) + path('M14 12l5 5 8-10', c, 3.6)
    return head + shift(badge, t, '9 -18', '-2 3')


def evolve(c, t):
    arrows = path('M-23-3a23 23 0 0 1 40-13m-2-8 5 11-12 1M23 3a23 23 0 0 1-40 13m2 8-5-11 12-1', c, 3.4)
    return turn(arrows, t, -65, 12) + scale(star(c), t + .10)


def model(c, t):
    window = rect(-32, -23, 64, 46, 8, WHITE, c)
    dial = path('M-17 9a17 17 0 0 1 34 0', c, 3.3)
    needle = path('M0 0V-15', c, 4)
    return window + dial + group(turn(needle, t, -66, 21) + dot(0, 0, 3, c), transform='translate(0 10)')


def import_data(c, t):
    pocket = path('M-27 2v19h54V2M-27 10h16l4 5H7l4-5h16', c, 3.6, WHITE)
    arrow = path('M0-23V3m-10-8L0 5 10-5', c, 4)
    return pocket + shift(arrow, t, '0 -14', '0 4')


STOPS = (
    ('storage', '存储路径', folder), ('instruction', '自定义指令', instruction),
    ('reply', '回复风格', reply), ('persona', '人设和长期记忆', persona),
    ('evolve', '记忆与进化', evolve), ('model', '窗口和模型', model),
    ('import', '数据导入', import_data),
)


def station(index, key, label, draw, x, t):
    tile = rect(-42, -37, 84, 74, 18, '#f5f9fe', TRACK)
    base = group(draw('#8da6c4', t))
    arm = path('M0 38V64', TRACK, 3) + dot(0, 66, 5.5, TRACK)
    hot = rect(-42, -37, 84, 74, 18, SKY, BLUE) + draw(BLUE, t)
    hot += path('M0 38V64', BLUE, 4) + dot(0, 66, 6.2, BLUE)
    active = group(anim('opacity', [(t - .07, 0), (t + .19, 1)]) + hot, ident=key, opacity=0)
    ring = (f'<circle cy="66" r="6" fill="none" stroke="{BLUE}" stroke-width="2" opacity="0">'
            + fade(t - .025, t + .09, t + .12, t + .40) + anim('r', [(t, 6), (t + .40, 21)]) + '</circle>')
    return group(f'<g aria-label="{index + 1}、{label}">' + tile + base + arm + active + ring + '</g>',
                 transform=f'translate({x} 95)')


def render():
    slogan = lettering(234, 91, '程序员梦哥', 29, MID) + lettering(230, 157, '分享 AI、', 65) + lettering(530, 157, '少踩坑', 65, BLUE)
    brand = group(anim('opacity', [(.94, 1), (1.49, 0), (7.69, 0), (8.20, 1)]) + slogan, ident='brand')
    sparks = []
    rng = Random(127)
    for i in range(19):
        x, y = rng.randrange(238, 726), rng.randrange(112, 161)
        t = 1.03 + .22 * (x - 238) / 488
        dx, dy = rng.randrange(22, 108), rng.randrange(7, 48)
        drift = anim('transform', [(t, '0 0'), (t + .53, f'{dx} {dy}')], kind='translate')
        sparks.append(group(fade(t, t + .13, t + .15, t + .51) + drift
                            + rect(x, y, 5, 5, 1, BLUE if i % 3 else CYAN), opacity=0))
    stops = [(252 + i * 110, 1.86 + i * .69) for i in range(len(STOPS))]
    motion = [(1.36, START), *((t, x) for x, t in stops), (6.63, END)]
    head = (anim('transform', [(t, f'{x} {Y}') for t, x in motion], kind='translate', curve='0 0 1 1')
            + fade(1.27, 1.56, 6.43, 6.85) + dot(0, 0, 14, '#ffefad') + dot(0, 0, 8, GLOW)
            + dot(0, 0, 3, WHITE))
    rail = (f'<line x1="{START}" x2="{START}" y1="{Y}" y2="{Y}" stroke="{BLUE}" stroke-width="4" stroke-linecap="round" id="progress">'
            + anim('x2', motion, curve='0 0 1 1') + '</line>')
    icons = ''.join(station(i, *setup, x, t) for i, (setup, (x, t)) in enumerate(zip(STOPS, stops)))
    scene = group(fade(1.22, 1.65, 7.13, 7.71) + path(f'M{START} {Y}H{END}', TRACK, 4) + rail
                  + icons + group(head, ident='light', opacity=0), ident='scene', opacity=0)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 216" width="1000" height="216" '
            'role="img" aria-label="程序员梦哥：一个光点依次启动 WorkBuddy 七项设置的图标">'
            + rect(0, 0, 1000, 216, 0, WHITE) + path('M178 38V181', '#e5edf7', 2)
            + avatar() + brand + ''.join(sparks) + scene + '</svg>\n')


def main():
    art = render()
    (OUT / 'intro.svg').write_text(art, encoding='utf-8')
    template = (PREVIOUS / 'preview.template.html').read_text(encoding='utf-8')
    template = template.replace('程序员梦哥 · WorkBuddy 片头三案', '程序员梦哥 · WorkBuddy 七项设置')
    template = template.replace('6.4', '8.4').replace('同步重播', '从头重播').replace('对比播放控制', '播放控制')
    template = template.replace('<main class="samples">', '<main class="samples" style="max-width:770px">')
    template = template.replace('2.75', '3.52').replace('4.35', '6.56')
    labels = ' → '.join(label for _, label, _ in STOPS)
    card = f'<article>{art}<details><summary>七个图标分别代表什么</summary><p>{labels}</p></details><p><a href="intro.svg" download>下载 SVG</a></p></article>'
    (OUT / 'preview.html').write_text(template.replace('<!-- samples -->', card), encoding='utf-8')


if __name__ == '__main__':
    main()
