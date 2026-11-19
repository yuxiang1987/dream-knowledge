"""Build the storage-settings sample SVGs (Pillow + fonttools, Windows Microsoft YaHei)."""
from pathlib import Path
import sys

OUT = Path(__file__).resolve().parent
PREVIOUS = OUT.parent / 'mengge-workbuddy-svg-trio'
sys.path.insert(0, str(PREVIOUS))
from build import (BLUE, CYAN, DURATION, LINE, MID, OUTWARD, PALE, WHITE,
                   alpha, arrival, dot, group, lettering, move, path, rect, svg, tween)

ORANGE = '#a44924'
WARM = '#fff2e6'


def trace(d, color, start, end, ident):
    return (f'<path id="{ident}" d="{d}" fill="none" stroke="{color}" stroke-width="5" '
            'stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100">'
            + tween('stroke-dashoffset', [(0, 100), (start, 100), (end, 0), (DURATION, 0)], curve=OUTWARD)
            + '</path>')


def folder(color, paper):
    return path('M-25-10V-17h18l7 6h25v31h-50Z', color, 3, paper) + path('M-25-3h50', color, 2)


def disk_scan():
    heading = lettering(214, 52, 'C 盘空间，先看是谁占的', 38)
    cards = []
    for i, (name, sub) in enumerate((('安装目录', '程序本体'), ('工作空间', '任务文件'), ('后台数据', '会话与日志'))):
        x = 223 + i * 247
        surface = rect(0, 0, 224, 99, 17, PALE, LINE) + dot(24, 30, 5, BLUE)
        surface += lettering(47, 41, name, 35) + lettering(47, 75, sub, 26, MID, False)
        cards.append(arrival(surface, 1.51 + i * .10, 2.15 + i * .10, '0 19', settle='0 -2'))
        cards[-1] = group(cards[-1], transform=f'translate({x} 80)')
    focus = (rect(0, 0, 224, 99, 17, WARM, ORANGE) + dot(24, 30, 5, ORANGE)
             + lettering(47, 41, '后台数据', 35, ORANGE) + lettering(47, 75, '会话与日志', 26, ORANGE, False))
    pop = tween('transform', [(0, '1 1'), (3.32, '1 1'), (3.51, '1.034 1.07'), (3.76, '1 1'),
                              (DURATION, '1 1')], kind='scale')
    focus = group(alpha(3.31, 3.57, 5.27, 5.74) + pop + group(focus, transform='translate(-112 -49.5)'),
                  ident='a-focus', transform='translate(829 129.5)', opacity=0)
    beam = rect(-21, 0, 42, 108, 14, '#d9eaff') + rect(-2, 0, 4, 108, 2, BLUE)
    beam = group(alpha(2.16, 2.36, 3.29, 3.62) + move(2.28, 3.39, '0 0', '651 0') + beam,
                 ident='a-beam', opacity=0, transform='translate(246 76)')
    return heading + ''.join(cards) + beam + focus


def workspace():
    heading = lettering(214, 52, '改默认路径，旧任务不搬', 38)
    old = (rect(227, 78, 199, 96, 17, '#f7faff', LINE) + lettering(248, 116, 'C 盘', 35)
           + lettering(248, 152, '旧任务', 28, MID, False))
    track = path('M455 126H513Q562 126 587 154T717 157', LINE, 4)
    active = trace('M455 126H513Q562 126 587 154T717 157', BLUE, 2.58, 3.46, 'b-route')
    current = (rect(731, 103, 220, 89, 17, PALE, '#93bdf0') + lettering(748, 137, 'D 盘', 33, BLUE)
               + lettering(748, 171, '新任务', 28, MID, False))
    new_folder = folder(BLUE, '#d9ebff')
    tracked = tween('transform', [(0, '0 0'), (2.60, '0 0'), (2.78, '76 0'), (3.10, '156 28'),
                                   (3.49, '429 23'), (3.63, '434 16'), (3.88, '429 23'),
                                   (DURATION, '429 23')], kind='translate')
    new_folder = group(alpha(2.15, 2.55, 5.30, 5.80) + tracked + new_folder,
                       ident='b-folder', transform='translate(456 126)', opacity=0)
    return arrival(heading + old + track + active + current + new_folder, initial='0 12')


def verify_result():
    heading = lettering(214, 52, '搬完别急，先核对这三项', 38)
    stages = ((322, '旧任务能打开'), (587, '新任务写到哪'), (852, '空间变化多少'))
    cards = []
    for i, (x, label) in enumerate(stages):
        start = 2.42 + .49 * i
        ring = (rect(-117, -34, 234, 68, 18, '#e6f8f6', '#78c7c4')
                + lettering(-100, 11, label, 32, CYAN))
        card = (rect(-117, -34, 234, 68, 18, '#f7faff', LINE)
                + lettering(-100, 11, label, 32) + group(alpha(start, start + .27, 5.26, 5.73) + ring,
                                                         ident=f'c-item-{i}', opacity=0))
        cards.append(group(card, transform=f'translate({x} 129)'))
    rail = path('M322 182H852', LINE, 4)
    visited = trace('M322 182H852', CYAN, 2.57, 3.57, 'c-rail')
    stops = ''.join(dot(x, 182, 5, LINE) for x, _ in stages)
    lens = dot(0, 0, 16, WHITE) + '<circle r="15" fill="none" stroke="#007e85" stroke-width="4"/>' + path('M11 11l11 11', CYAN, 5)
    travel = tween('transform', [(0, '0 0'), (2.57, '0 0'), (3.02, '265 0'), (3.57, '530 0'),
                                 (3.76, '532 -3'), (4.04, '530 0'), (DURATION, '530 0')], kind='translate')
    lens = group(alpha(2.01, 2.32, 5.14, 5.66) + travel + lens, ident='c-lens', opacity=0, transform='translate(322 178)')
    return arrival(heading + rail + stops + visited + ''.join(cards) + lens, initial='-22 0')


VARIANTS = (
    ('a', '01 · 磁盘扫描', '扫描带扫过三类目录，停在「后台数据」。先找来源，不把所有数据都叫缓存。', BLUE, disk_scan),
    ('b', '02 · 新旧分流', '新任务沿新路线进 D 盘，C 盘里的旧任务原地不动。只演示修改默认工作空间。', BLUE, workspace),
    ('c', '03 · 搬后验收', '放大镜依次扫过旧任务、新任务和磁盘空间。演示检查项，不代表迁移已经成功。', CYAN, verify_result),
)


def main():
    cards = []
    for ident, title, description, color, scene in VARIANTS:
        artwork = svg(ident, title, description, color, scene)
        (OUT / f'{ident}.svg').write_text(artwork, encoding='utf-8')
        cards.append(f'<article><h2>{title}</h2>{artwork}<p>{description}</p>'
                     f'<a href="{ident}.svg" download>下载 SVG</a></article>')
    template = (PREVIOUS / 'preview.template.html').read_text(encoding='utf-8')
    preview = template.replace('程序员梦哥 · WorkBuddy 片头三案', 'WorkBuddy 存储路径 · 片头三案')
    preview = preview.replace('动作示意，不是产品录屏', '动作示意，不是产品录屏或迁移实测')
    (OUT / 'preview.html').write_text(preview.replace('<!-- samples -->', '\n'.join(cards)), encoding='utf-8')


if __name__ == '__main__':
    main()
