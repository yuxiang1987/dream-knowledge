"""Article-specific origami animation, using the installed SVG intro kit."""
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location(
    "intro_kit", ROOT / ".agents/skills/gzh-svg-intro/scripts/build_svg_intro.py")
kit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kit)
FE = kit.FontEngine()
INK, BLUE, MUTED, LIME = "#1E293B", "#1E6FFF", "#8291A5", "#C6F24E"


def text(s, x, y, size=20, color=INK, bold=True):
    return FE.text(s, size, x, y, color, bold)


def times(seconds):
    return ";".join(f"{s / 8:.5f}" for s in seconds)


def attr(name, values, seconds, ease="0.45 0 0.55 1"):
    return kit.smil_attr(name, values, times(seconds), ease)


def move(kind, values, seconds, ease="0.23 1 0.32 1"):
    return kit.smil_transform(kind, values, times(seconds), ease)


def visible(start, end, fade=.15):
    return kit.smil_opacity("0;0;1;1;0;0", times([0, start, start+fade, end-fade, end, 8]))


def group(content, transform="", animation="", name=""):
    return f'<g{f" id={chr(34)}{name}{chr(34)}" if name else ""}{f" transform={chr(34)}{transform}{chr(34)}" if transform else ""}>{animation}{content}</g>'


def rect(x, y, w, h, fill, stroke="none", radius=6, width=1.5, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}">{extra}</rect>'


def path(d, fill="none", stroke=INK, width=2, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round">{extra}</path>'


def circle(x, y, r, fill, stroke="none", width=1.5, extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}">{extra}</circle>'


def captions():
    parts = [text("WorkBuddy", 274, 59, 26), text("× huashu-design", 275, 82, 13, MUTED, False)]
    for start, end, lines in [
        (1.80, 2.70, ["说出一个想法", "做个健身小程序"]),
        (2.66, 3.98, ["三套原型展开", "挑中喜欢的那套"]),
        (3.94, 5.40, ["让设计稿", "折成一部手机"]),
        (5.36, 7.26, ["不用敲一行代码", "让小程序动起来"]),
    ]:
        words = text(lines[0], 274, 125, 27) + text(lines[1], 274, 161, 27, BLUE)
        parts.append(group(words, animation=visible(start, end, .09)))
    parts.append(path("M275 182 H315", stroke=BLUE, width=3))
    return "".join(parts)


def request_note():
    paper = path("M-114 -58 H91 L114 -35 V58 H-114 Z", "#F8FBFF", "#A9C6EE", 2)
    paper += path("M91 -58 V-35 H114", "#E1EDFF", "#A9C6EE", 1.5)
    paper += text("我想做个", -88, -10, 25) + text("健身小程序", -88, 25, 25, BLUE)
    paper += path("M-89 42 H-28", stroke="#A9C6EE", width=2)
    paper = group(paper, animation=move("rotate", "-9; -9; 2; 0; 0", [0, 1.82, 2.05, 2.25, 8]))
    paper = group(paper, animation=move("scale", ".65;.65;1.06;1;1", [0, 1.8, 2.03, 2.19, 8]))
    return group(paper, "translate(826 111)", visible(1.80, 2.76, .18), "request-note")


def prototype(label, surface, accent, ink, index):
    # Each page has its own composition, not just a recolored rectangle.
    page = rect(-49, -65, 98, 130, surface, "#CFD8E5", 5)
    page += text(label, -38, -45, 11, ink)
    if index == 0:
        page += rect(-37, -32, 74, 30, accent, radius=0)
        page += text("MOVE", -31, -11, 16, "#FFFFFF")
        for y in (10, 30):
            page += path(f"M-35 {y} H34", stroke="#222B34", width=1)
            page += rect(-35, y+6, 29, 5, "#CAD0D8", radius=0)
        page += rect(-36, 49, 72, 7, accent, radius=0)
    else:
        page += circle(0, -7, 23, "none", accent, 5)
        page += path("M-18 24 H18 M-24 34 H24", stroke=ink, width=2)
        page += rect(-34, 45, 68, 11, accent, radius=5)
    return page


def fan_pages():
    pages = []
    for i, (label, bg, accent, ink, dest, tilt) in enumerate([
        ("A · 网格", "#FFFFFF", "#EE6257", INK, -131, -9),
        ("B · 留白", "#F0F3E9", "#90A891", "#4B6253", 0, 0),
        ("C · 能量", "#191D23", LIME, "#F2F5E8", 131, 9),
    ]):
        content = prototype(label, bg, accent, ink, i)
        if i == 2:
            outline = rect(-54, -70, 108, 140, "none", BLUE, 8, 2.5)
            content += group(outline + circle(44, -59, 10, BLUE) + path("M39 -59 l4 4 7 -8", stroke="#FFFFFF", width=2), animation=visible(3.30, 4.04, .12))
        content = group(content, animation=move("rotate", f"0;0;{tilt};{tilt};0;0", [0, 2.44, 2.90, 3.65, 4.04, 8]))
        content = group(content, animation=move("translate", f"0 0;0 0;{dest} 0;{dest} 0;0 0;0 0", [0, 2.44, 2.92, 3.60, 4.05, 8]))
        pages.append(group(content, animation=visible(2.44, 4.10, .16)))
    # Small pencil check travels to the chosen C sheet.
    pointer = path("M0 0 L2 23 L8 16 L15 27 L21 23 L14 13 L25 11 Z", "#FFFFFF", BLUE, 1.5)
    pointer = group(pointer, animation=move("translate", "1032 167;1032 167;984 134;972 139;984 134;984 134", [0, 2.95, 3.28, 3.36, 3.47, 8]))
    pages.append(group(pointer, animation=visible(2.98, 3.70)))
    pages.append(group(text("选方案 C", -45, 96, 16, BLUE), "translate(957 110)", visible(3.30, 3.84, .10)))
    # Paper fan is centered; the pointer already uses absolute coordinates.
    return group("".join(pages[:-2]), "translate(826 108)", name="three-prototypes") + "".join(pages[-2:])


def fold_phone():
    # The selected page is the same central surface throughout folding and activation.
    phone = rect(-65, -80, 130, 160, "#F4F8FF", "#8CAAD3", 5, 2, extra=
                 attr("fill", "#F4F8FF;#F4F8FF;#15181D;#15181D", [0, 4.60, 5.03, 8]) +
                 attr("stroke", "#8CAAD3;#8CAAD3;#253349;#253349", [0, 4.60, 5.03, 8]) +
                 attr("rx", "5;5;19;19", [0, 4.60, 5.03, 8]))
    left = "M-65 -80 L-117 -50 L-117 50 L-65 80 Z"
    left_fold = "M-65 -80 L-65 -50 L-65 50 L-65 80 Z"
    right = "M65 -80 L117 -50 L117 50 L65 80 Z"
    right_fold = "M65 -80 L65 -50 L65 50 L65 80 Z"
    flaps = path(left, "#DCE9FC", "#9DBBE2", 1.5, attr("d", f"{left};{left};{left_fold};{left_fold}", [0, 4.13, 4.62, 8]))
    flaps += path(right, "#ECF3FF", "#9DBBE2", 1.5, attr("d", f"{right};{right};{right_fold};{right_fold}", [0, 4.27, 4.76, 8]))
    top = "M-65 -80 L0 -102 L65 -80 L0 -60 Z"
    top_fold = "M-65 -80 L0 -80 L65 -80 L0 -80 Z"
    flaps += path(top, "#FFFFFF", "#9DBBE2", 1.5, attr("d", f"{top};{top};{top_fold};{top_fold}", [0, 4.46, 4.94, 8]))
    phone += group(flaps, animation=visible(3.88, 5.03, .10))
    creases = path("M-65 -80 V80 M65 -80 V80", stroke="#82A7D7", width=1)
    phone += group(creases, animation=visible(3.90, 4.96, .12))
    blueprint = text("方案 C", -25, -50, 14, "#58759A")
    blueprint += circle(0, -8, 31, "none", "#98B2D3", 3)
    blueprint += path("M-39 34 H-17 M-6 34 H11 M23 34 H39", stroke="#98B2D3", width=2)
    blueprint += rect(-47, 47, 94, 19, "none", "#98B2D3", 5, 1)
    phone += group(blueprint, animation=visible(3.88, 4.95, .13))
    # A narrow edge and speaker make the paper visibly become a device.
    details = rect(-20, -73, 40, 4, "#54616F", radius=2)
    details += path("M-70 -35 V-12 M70 -23 V0", stroke=INK, width=2.5)
    details += rect(-15, 72, 30, 3, "#6B7786", radius=2)
    phone += group(details, animation=visible(4.86, 7.40))
    screen = text("梦动健身", -38, -51, 14, "#F1F5ED")
    screen += circle(0, -8, 31, "none", "#363E37", 7)
    screen += '<g transform="rotate(-90 0 -8)"><circle id="energy-ring" cx="0" cy="-8" r="31" fill="none" stroke="#C6F24E" stroke-width="7" stroke-linecap="round" stroke-dasharray="195" stroke-dashoffset="195">' + attr("stroke-dashoffset", "195;195;42;42", [0, 5.62, 6.58, 8]) + '</circle></g>'
    screen += text("动起来", -21, -4, 14, "#F1F5ED")
    screen += path("M-40 35 H-20 M-8 35 H10 M22 35 H40", stroke="#85937B", width=2)
    button = rect(-47, 47, 94, 19, LIME, radius=7) + text("开始运动", -23, 60, 11, "#192219")
    screen += kit.scale_around(0, 56, "1;1;.90;1.05;1;1", times([0, 5.48, 5.60, 5.73, 5.88, 8]), button)
    phone += group(screen, animation=visible(4.78, 7.45))
    phone = group(phone, animation=move("rotate", "9;9;-3;0;0", [0, 3.90, 4.45, 5.03, 8]))
    phone = group(phone, animation=move("translate", "131 0;131 0;0 0;0 0", [0, 3.88, 4.18, 8]))
    shadow = '<ellipse cx="0" cy="92" rx="77" ry="5" fill="#DCE5F0"/>'
    return group(shadow + phone, "translate(826 111)", visible(3.88, 7.40, .12), "origami-phone")


def tap_and_run():
    # The finger arrives before the button press, then retracts.
    hand = path("M0 0 C-3 -5 -3 -15 1 -15 C5 -15 5 -11 6 -7 L10 9 L13 5 C15 2 18 4 19 7 L24 20 Q26 25 20 30 L7 35 Q2 36 -1 31 L-10 19 Q-13 14 -8 13 L0 20 Z", "#FFF1E1", "#253349", 1.7)
    hand = group(hand, animation=move("translate", "931 205;931 205;834 171;834 166;856 190;931 205;931 205", [0, 5.03, 5.45, 5.60, 5.83, 6.13, 8]))
    ripple = circle(826, 167, 8, "none", BLUE, 2, attr("r", "8;8;30;30", [0, 5.60, 5.98, 8]))
    ripple = group(ripple, animation=visible(5.59, 6.03, .08))
    # Running is a symbolic continuation of tapping the fitness app.
    runner = circle(0, -39, 9, "#EBC5A4")
    runner += path("M-7 -46 Q0 -54 8 -45", stroke=INK, width=5)
    runner += path("M0 -27 L-9 1", stroke=BLUE, width=17)
    for limb, base, vals in [
        ("M-2 -21 L-17 -10 L-28 -20", (-2, -21), "-14;25;-14"),
        ("M-2 -21 L14 -25 L24 -13", (-2, -21), "20;-25;20"),
        ("M-8 0 L-22 17 L-39 14", (-8, 0), "-16;27;-16"),
        ("M-8 0 L9 16 L5 32", (-8, 0), "24;-22;24"),
    ]:
        part = path(limb, stroke=INK if base[1] == 0 else "#EBC5A4", width=6)
        runner += kit.rotate_around(*base, vals, "0;.5;1", part, dur=".64s")
    runner = group(runner, animation=move("translate", "0 0;0 -3;0 0", [0, 4, 8]))
    runner = group(runner, animation=move("translate", "-130 0;-130 0;0 0;0 0", [0, 5.76, 6.34, 8]))
    runner = group(runner, "translate(1050 127)", visible(5.76, 7.40), "runner")
    track = path("M983 172 H1118", stroke="#DCE6F3", width=2)
    marks = path("M980 105 H1002 M970 122 H996 M982 139 H1000", stroke="#91B9F2", width=2)
    labels = text("手机真能用", 983, 194, 19, BLUE)
    labels += text("健身小程序 · 动起来", 967, 61, 15, MUTED, False)
    finish = kit.check_badge(1120, 142, 13, .79)
    return group(hand, animation=visible(5.03, 6.16)) + ripple + group(track+marks+labels+runner+finish, animation=visible(5.76, 7.40), name="activation")


def build():
    stage = kit.wrap_stage(captions() + request_note() + fan_pages() + fold_phone() + tap_and_run())
    aria = ("程序员梦哥，分享AI少踩坑；像素文字变成粒子；WorkBuddy 接收健身小程序想法，"
            "需求纸展开成三套原型，选中青柠色方案C；纸张两侧与顶部依次折合变成手机；"
            "手指按下开始运动后能量环增长，跑步小人从手机方向跑出，最后弹出对勾与手机真能用。")
    svg = kit.assemble_svg(stage, aria)
    info = kit.save_intro_bundle(svg, HERE / "intro.svg", HERE / "preview.html",
        title="WorkBuddy · 把想法折成小程序",
        stops=[(.5,"品牌"),(2.2,"需求纸"),(3.35,"三套原型"),(4.45,"折成手机"),(5.60,"手指点击"),(6.65,"动起来")])
    preview = (HERE / "preview.html").read_text(encoding="utf-8")
    preview = preview.replace("1246×220 · 8s 循环 · 纯内嵌 SVG + SMIL（零 &lt;text&gt;、零 &lt;image&gt;、零 &lt;script&gt;、零 &lt;defs&gt;）",
                              "8 秒循环 · 需求纸展开 → 三套原型 → 折成手机 → 点击动起来")
    preview = preview.replace("正常循环播放", "从头播放").replace("s.unpauseAnimations(); document.getElementById('msg')", "s.setCurrentTime(0); s.unpauseAnimations(); document.getElementById('msg')")
    (HERE / "preview.html").write_text(preview, encoding="utf-8")
    (HERE / "intro.wechat.html").write_text(f'<section style="width:100%;margin:0 0 18px;line-height:0">{svg}</section>', encoding="utf-8")
    (HERE / "storyboard.json").write_text(json.dumps({
        "title": "把想法折成小程序", "duration": 8,
        "article": "raw/article/程序员梦哥/WorkBuddy + huashu skill 手搓健身小程序（附提示词）.md",
        "beats": [[1.8,2.76,"需求纸条"],[2.44,4.10,"三套原型与选择C"],[3.88,5.03,"纸张折成手机"],[5.03,5.60,"手指按下按钮"],[5.62,7.04,"能量环增长与跑步角色"]],
        "wechat_live_verified": False,
    }, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(info, ensure_ascii=False))


if __name__ == "__main__":
    build()
