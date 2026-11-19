"""Build the WorkBuddy switchyard sample. Uses Pillow, fonttools and Microsoft YaHei."""
from pathlib import Path
import sys

OUT = Path(__file__).resolve().parent
PREVIOUS = OUT.parent / 'mengge-workbuddy-svg-trio'
sys.path.insert(0, str(PREVIOUS))
from build import (BLUE, DURATION, EASE, LINE, MID, PALE, WHITE, alpha, dot, group,
                   lettering, move, num, path, rect, svg, tween)

TRACK = '#a8bdd7'
LIVE = '#1565eb'
SOFT = '#dcecff'
ROUTE = 'M230 112H574C630 112 652 167 714 167H896'


def motion(route, stops):
    times = ';'.join(num(t / DURATION) for t, _ in stops)
    points = ';'.join(str(p) for _, p in stops)
    curves = ';'.join([EASE] * (len(stops) - 1))
    return (f'<animateMotion path="{route}" dur="{DURATION}s" repeatCount="indefinite" '
            f'calcMode="spline" keyTimes="{times}" keyPoints="{points}" keySplines="{curves}"/>')


def rail(d, color, width=4):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'


def tray(label, subtitle, accent, background):
    return (rect(0, -49, 166, 66, 13, background, LINE)
            + lettering(13, -20, label, 32, accent)
            + lettering(13, 5, subtitle, 24, MID, False)
            + path('M116-10v15h34v-15', accent, 2.5))


def folder(accent, fill):
    return path('M-15-10v-6h12l4 5h16v22h-32Z', accent, 2.7, fill)


def scene():
    # One actual SVG path: the underline grows a horizontal segment, then its tip bends into the new rail.
    underline = 'M230 112L448 112C448 112 448 112 448 112L448 112'
    extended = 'M230 112L574 112C626 112 663 112 714 112L741 112'
    switched = 'M230 112L574 112C630 112 652 167 714 167L896 167'
    geometry = tween('d', [(0, underline), (1.79, underline), (2.48, extended), (2.70, extended),
                            (3.23, switched), (DURATION, switched)])
    track = f'<path id="rail" d="{underline}" fill="none" stroke="{TRACK}" stroke-width="5" stroke-linecap="round">{geometry}</path>'
    old_line = group(alpha(2.31, 2.62, 5.38, 5.73) + rail('M574 112H806Q826 112 838 95H896', TRACK), opacity=0)
    active_line = (f'<path id="active-line" d="{ROUTE}" fill="none" stroke="{LIVE}" stroke-width="4" '
                   'stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100">'
                   + tween('stroke-dashoffset', [(0, 100), (3.17, 100), (3.77, 0), (DURATION, 0)]) + '</path>')
    label = group(tween('opacity', [(0, 1), (2.54, 1), (3.28, .58), (DURATION, .58)])
                  + move(2.55, 3.22, '0 0', '0 -11') + lettering(226, 91, '默认工作空间', 40))
    old = group(alpha(1.56, 2.17, 5.36, 5.72) + tray('C 盘', '旧任务', MID, '#f5f8fb')
                + group(folder(MID, '#e5edf6'), transform='translate(133 -12)', ident='old-folder'),
                transform='translate(763 86)', opacity=0)
    bounce = move(4.67, 4.82, '0 0', settle='0 4')
    new = group(alpha(2.71, 3.38, 5.35, 5.72) + bounce + tray('D 盘', '新任务', BLUE, PALE),
                ident='d-tray', transform='translate(763 170)', opacity=0)
    turn = tween('transform', [(0, 0), (2.58, 0), (2.71, -8), (2.95, 35), (3.13, 27), (DURATION, 27)], kind='rotate')
    lever = group(alpha(2.19, 2.53, 5.38, 5.72) + dot(0, 0, 9, WHITE)
                  + group(turn + path('M0 0h41', BLUE, 5) + dot(41, 0, 6, LIVE), ident='lever') + dot(0, 0, 5, BLUE),
                  transform='translate(574 112)', opacity=0)
    # First leg ends at the pivot; the same light waits for the turn and continues down the branch.
    light = group(alpha(1.66, 1.85, 3.85, 4.19) + motion(ROUTE, [(0, 0), (1.81, 0), (2.58, .498),
                   (3.13, .498), (3.86, 1), (DURATION, 1)]) + dot(0, 0, 15, SOFT) + dot(0, 0, 7, LIVE),
                  ident='route-light', opacity=0)
    cargo = group(alpha(3.55, 3.77, 5.35, 5.72) + motion(ROUTE, [(0, 0), (3.54, 0), (3.90, .32),
                  (4.51, .91), (4.70, 1), (DURATION, 1)]) + folder(BLUE, '#bfe0ff'), ident='cargo', opacity=0)
    pulse = (f'<circle cx="896" cy="164" r="17" fill="none" stroke="{LIVE}" stroke-width="2" opacity="0">'
             + alpha(4.66, 4.78, 4.82, 5.19)
             + tween('r', [(0, 17), (4.71, 17), (5.18, 40), (DURATION, 40)]) + '</circle>')
    return old_line + track + active_line + label + old + new + lever + light + cargo + pulse


def main():
    artwork = svg('switch', '路径改道', '蓝点沿下划线到达道岔，轨道弯向 D 盘；新任务改道，C 盘旧任务不搬。', BLUE, scene)
    (OUT / 'intro.svg').write_text(artwork, encoding='utf-8')
    template = (PREVIOUS / 'preview.template.html').read_text(encoding='utf-8')
    template = template.replace('程序员梦哥 · WorkBuddy 片头三案', '程序员梦哥 · WorkBuddy 路径改道')
    template = template.replace('<main class="samples">', '<main class="samples" style="max-width:770px">')
    template = template.replace('同步重播', '从头重播').replace('对比播放控制', '播放控制')
    template = template.replace('data-frame="1.45">定格：转场', 'data-frame="2.6">定格：触发')
    template = template.replace('data-frame="2.75">定格：动作', 'data-frame="3.28">定格：改道')
    template = template.replace('4.35', '4.95')
    card = f'<article>{artwork}<p>改的是新任务的默认工作空间，不是旧数据的存放位置。</p><a href="intro.svg" download>下载 SVG</a></article>'
    (OUT / 'preview.html').write_text(template.replace('<!-- samples -->', card), encoding='utf-8')


if __name__ == '__main__':
    main()
