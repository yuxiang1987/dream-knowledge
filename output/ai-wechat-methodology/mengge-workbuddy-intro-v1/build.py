"""Render the standalone WorkBuddy sample with Pillow; no layout Skill dependency."""
import math
import os
from functools import lru_cache
from pathlib import Path
from random import Random

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
SPRITE = OUT.parent / '程序员拾梦闯关片头五案-v1' / 'sprite-idle.png'
FONTS = Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts'
SIZE = (1000, 236)
STEP_MS = 50
FRAME_COUNT = 108
WHITE = (255, 255, 255)
INK = (25, 42, 70)
MUTED = (72, 97, 130)
BLUE = (34, 95, 218)
PALE = (238, 246, 255)
BORDER = (211, 226, 247)


@lru_cache
def font(size, bold):
    return ImageFont.truetype(str(FONTS / ('msyhbd.ttc' if bold else 'msyh.ttc')), size)


def ease(t, start, end):
    u = min(1, max(0, (t - start) / (end - start)))
    return u * u * (3 - 2 * u)


def mix(a, b, amount):
    return tuple(round(x + (y - x) * amount) for x, y in zip(a, b))


def text(draw, xy, message, size, fill=INK, bold=False):
    draw.text(xy, message, fill=fill, font=font(size, bold), anchor='lm')


def brand_layer():
    layer = Image.new('RGBA', SIZE)
    d = ImageDraw.Draw(layer)
    text(d, (209, 77), '程序员梦哥', 29, MUTED, True)
    text(d, (206, 140), '分享 AI、', 61, INK, True)
    text(d, (486, 140), '少踩坑', 61, BLUE, True)
    d.rounded_rectangle((210, 184, 267, 190), radius=3, fill=BLUE)
    return layer


def particle_seeds(brand):
    rng = Random(264)
    return [(x, y, brand.getpixel((x, y))[:3], rng.randint(35, 108), rng.randint(-58, 51), rng.randint(3, 8))
            for y in range(54, 196, 9) for x in range(208, 718, 9)
            if brand.getpixel((x, y))[3] > 140 and rng.random() < .48]


def scene(t):
    layer = Image.new('RGBA', SIZE)
    d = ImageDraw.Draw(layer)
    p = ease(t, 2.52, 2.84)
    text(d, (211, 52), 'WorkBuddy', 36, INK, True)
    text(d, (449, 53), '回复风格', 29, MUTED)
    d.rounded_rectangle((699, 28, 943, 77), radius=24, fill=mix(PALE, BLUE, p))
    d.ellipse((719, 44, 735, 60), fill=mix(WHITE, WHITE, p), outline=mix(MUTED, WHITE, p), width=3)
    if p > .5:
        d.ellipse((724, 49, 730, 55), fill=WHITE)
    text(d, (750, 53), '高效务实', 32, mix(BLUE, WHITE, p), True)
    d.rounded_rectangle((206, 91, 944, 202), radius=20, fill=WHITE, outline=BORDER, width=2)
    old = 1 - ease(t, 2.58, 2.84)
    if old:
        tint = mix(WHITE, MUTED, old)
        text(d, (232, 124), '有几种做法，先说一下背景…', 36, tint)
        for y, w in ((153, 375), (174, 260)):
            d.rounded_rectangle((234, y, 234 + w, y + 8), radius=4, fill=mix(WHITE, BORDER, old))
    new = ease(t, 2.85, 3.22)
    if new:
        text(d, (232, 143), '结论：先用方案 A。', 44, mix(WHITE, INK, new), True)
        d.ellipse((855, 120, 903, 168), fill=mix(WHITE, PALE, new))
        d.line(((868, 144), (878, 153), (891, 134)), fill=mix(WHITE, BLUE, new), width=5, joint='curve')
    cursor = ease(t, 2.01, 2.51) * (1 - ease(t, 2.88, 3.09))
    if cursor:
        fly = 1 - ease(t, 2.01, 2.51)
        x, y = round(838 + 88 * fly), round(60 + 40 * fly)
        pointer = ((x, y), (x, y + 31), (x + 8, y + 23), (x + 16, y + 35),
                   (x + 22, y + 31), (x + 14, y + 19), (x + 25, y + 18))
        d.polygon(pointer, fill=mix(WHITE, INK, cursor))
        d.line((*pointer, pointer[0]), fill=WHITE, width=2)
    return layer


def overlay(image, layer, strength):
    if strength <= 0:
        return
    if strength < 1:
        layer = layer.copy()
        layer.putalpha(layer.getchannel('A').point([round(i * strength) for i in range(256)]))
    image.alpha_composite(layer)


def render(t, sprite, brand, particles):
    base = Image.new('RGBA', SIZE, WHITE)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((9, 12, 991, 224), radius=30, fill=(246, 250, 255), outline=BORDER, width=2)
    d.rounded_rectangle((25, 26, 165, 210), radius=22, fill=PALE)
    d.ellipse((56, 181, 134, 197), fill=(217, 232, 253))
    bob = round(3 * math.sin(math.tau * t / 1.8))
    base.alpha_composite(sprite, (95 - sprite.width // 2, 40 + bob))
    d.line((184, 42, 184, 194), fill=BORDER, width=2)
    overlay(base, brand, (1 - ease(t, 1.16, 1.52)) + ease(t, 5.04, 5.32))
    if 1.12 < t < 1.89:
        q = ease(t, 1.12, 1.89)
        opacity = math.sin(math.pi * q)
        for x, y, color, dx, dy, size in particles:
            px, py = round(x + dx * q), round(y + dy * q)
            width = max(1, round(size * (1 - .65 * q)))
            d.rectangle((px, py, px + width, py + width), fill=mix((246, 250, 255), color, opacity))
    overlay(base, scene(t), ease(t, 1.64, 1.98) * (1 - ease(t, 4.69, 5.04)))
    return base.convert('RGB')


def main():
    with Image.open(SPRITE) as source:
        h = 145
        sprite = source.convert('RGBA').resize((round(h * source.width / source.height), h), Image.Resampling.NEAREST)
    brand = brand_layer()
    particles = particle_seeds(brand)
    frames = [render(i * STEP_MS / 1000, sprite, brand, particles).quantize(colors=128)
              for i in range(FRAME_COUNT)]
    frames[0].save(OUT / 'intro.gif', save_all=True, append_images=frames[1:], loop=0, duration=STEP_MS, optimize=True)


if __name__ == '__main__':
    main()
