"""Compare three caption treatments on the same WorkBuddy seven-station animation."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parent
BASE = OUT.parent / 'mengge-workbuddy-seven-settings'
SPEC = spec_from_file_location('seven_settings', BASE / 'build.py')
seven = module_from_spec(SPEC)
SPEC.loader.exec_module(seven)

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
LABELS = ('存储路径', '自定义指令', '回复风格', '人设记忆', '记忆进化', '窗口模型', '数据导入')
COLORS = {'ink': '#405977', 'accent': '#1754bf'}


def lettering(label, x, y, size, color, max_width=105):
    width = len(label) * size
    scale = min(1, max_width / width)
    art = seven.lettering(-width / 2, 0, label, size, color)
    return seven.group(art, transform=f'translate({x} {y}) scale({scale:.6f} 1)')


def fixed(index, label, x, t):
    base = lettering(label, x, 202, 25, COLORS['ink'])
    hot = lettering(label, x, 202, 25, COLORS['accent'])
    dim = seven.anim('opacity', [(t - .08, 1), (t + .16, 0)])
    tint = seven.anim('opacity', [(t - .08, 0), (t + .16, 1)])
    return (seven.group(dim + base, ident=f'plain-{index}')
            + seven.group(tint + hot, ident=f'word-{index}', opacity=0))


def focus(index, label, _x, t):
    start = t - .16
    end = t + .54
    if index == len(LABELS) - 1:
        vis = seven.anim('opacity', [(start, 0), (t + .045, 1)])
    else:
        vis = seven.fade(start, t + .045, end - .11, end)
    drift = seven.anim('transform', [(start, '0 7'), (t + .10, '0 0')], kind='translate')
    text = lettering(label, 582, 204, 39, COLORS['accent'], max_width=320)
    return seven.group(vis + drift + text, ident=f'word-{index}', opacity=0)


def accumulate(index, label, x, t):
    arrive = seven.anim('opacity', [(t - .09, 0), (t + .17, 1)])
    drift = seven.anim('transform', [(t - .09, '0 7'), (t + .17, '0 -1'), (t + .29, '0 0')], kind='translate')
    text = lettering(label, x, 202, 25, COLORS['accent'])
    return seven.group(arrive + drift + text, ident=f'word-{index}', opacity=0)


VARIANTS = (
    ('a', '01 · 标签常驻', '七项名称同时可见，光点到站时对应文字变蓝。', fixed),
    ('b', '02 · 大字聚焦', '画面下方每次只出现当前一项，字更大，视线不用左右找。', focus),
    ('c', '03 · 逐站留名', '光点走到哪，名称才从图标下冒出来；已经出现的名称留在原位。', accumulate),
)


def render(base, code, title, draw):
    tree = ET.fromstring(base)
    scene = tree.find(f'.//{{{NS}}}g[@id="scene"]')
    labels = ''.join(draw(i, label, 252 + i * 110, 1.86 + i * .69) for i, label in enumerate(LABELS))
    patch = ET.fromstring(f'<g xmlns="{NS}">{labels}</g>')
    scene.append(patch)
    tree.set('aria-label', f'WorkBuddy 七项设置，{title}')
    # The comparison page embeds all three SVGs in one document.
    for node in tree.iter():
        if node.get('id'):
            node.set('id', f'{code}-{node.get("id")}')
    return ET.tostring(tree, encoding='unicode') + '\n'


def main():
    base = (BASE / 'intro.svg').read_text(encoding='utf-8')
    cards = []
    for code, title, desc, draw in VARIANTS:
        art = render(base, code, title, draw)
        (OUT / f'{code}.svg').write_text(art, encoding='utf-8')
        cards.append(f'<article><h2>{title}</h2>{art}<p>{desc}</p><a href="{code}.svg" download>下载 SVG</a></article>')
    template = (seven.PREVIOUS / 'preview.template.html').read_text(encoding='utf-8')
    template = template.replace('程序员梦哥 · WorkBuddy 片头三案', 'WorkBuddy 七项设置 · 短标签三案')
    template = template.replace('6.4', '8.4').replace('1.45', '2.12').replace('2.75', '4.12').replace('4.35', '6.32')
    template = template.replace('定格：转场', '定格：第一项').replace('定格：动作', '定格：第四项').replace('定格：结果', '定格：第七项')
    (OUT / 'preview.html').write_text(template.replace('<!-- samples -->', '\n'.join(cards)), encoding='utf-8')


if __name__ == '__main__':
    main()
