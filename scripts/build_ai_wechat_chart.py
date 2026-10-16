"""生成供人速览的经营路径图，保留SVG/PDF并从PDF渲染PNG进行验收。"""
from pathlib import Path
import json
import shutil
import subprocess
from xml.sax.saxutils import escape

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/ai-wechat-methodology"
PDF = ROOT / "output/pdf/AI垂类公众号经营全流程.pdf"
WIDTH, HEIGHT = 1200, 2200
STEPS = [
    ("定位人群", "明确读者任务，也明确品牌为何需要这些人", "定位卡：人群、问题、产品、合作价值"),
    ("选题与案例", "从热点或痛点找角度，选一个能亲自验证的任务", "选题卡：问题、场景、观察标准、证据计划"),
    ("实测与写作", "人做实测和判断，AI辅助整理、结构与编辑", "内容样板：真实成果、过程、限制、证据包"),
    ("发布与分发", "记录自然与付费来源，小额测试受众是否匹配", "效果记录：同窗口反馈、关注、投入"),
    ("询价与获客", "承接客户主动询价，也可带着样板联系品牌", "客户台账：需求、阶段、下一次动作"),
    ("报价与成交", "明确范围、推广、改稿、验收和付款再确认合作", "合作约定：交付清楚、成本可承受"),
    ("交付与回款", "按约实测、审稿、发布、报告、验收并收款", "完成记录：交付物、验收、实际到账"),
    ("复盘与复购", "看客户与读者反馈，算清成本，提出下一次场景", "可复用资产：案例、客户需求、下一轮选题"),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    PDF.parent.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(TTFont("YaHei", "C:/Windows/Fonts/msyh.ttc", subfontIndex=0))
    pdfmetrics.registerFont(TTFont("YaHeiBold", "C:/Windows/Fonts/msyhbd.ttc", subfontIndex=0))
    canvas = Canvas(str(PDF), pagesize=(WIDTH / 2, HEIGHT / 2), pageCompression=1)
    canvas.setTitle("AI垂类公众号经营全流程")
    canvas.setAuthor("程序员拾梦 / 综合整理")
    canvas.scale(0.5, 0.5)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
           '<title>AI垂类公众号经营全流程</title>',
           '<desc>八个环节，从定位、选题、实测写作到分发、获客、成交、交付与复购，复盘反馈返回选题。</desc>']
    labels = []

    def color(value):
        canvas.setFillColor(value)
        canvas.setStrokeColor(value)

    def rect(x, y, w, h, fill, radius=0, stroke=None, line_width=1):
        canvas.setFillColor(fill)
        canvas.setStrokeColor(stroke or fill)
        canvas.setLineWidth(line_width)
        canvas.roundRect(x, HEIGHT - y - h, w, h, radius,
                         fill=1, stroke=int(stroke is not None))
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke or fill}" stroke-width="{line_width}"/>')

    def text(x, y, value, size=26, fill="#405368", bold=False, max_width=None):
        font = "YaHeiBold" if bold else "YaHei"
        measured = pdfmetrics.stringWidth(value, font, size)
        assert measured <= (max_width if max_width is not None else WIDTH - x - 45), value
        assert y + size <= HEIGHT - 20, value
        labels.append({"text": value, "x": x, "y": y, "width": measured, "size": size})
        canvas.setFillColor(fill)
        canvas.setFont(font, size)
        canvas.drawString(x, HEIGHT - y - size * 0.9, value)
        svg.append(f'<text x="{x}" y="{y + size * 0.9}" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{fill}">{escape(value)}</text>')

    def line(points, fill="#9AABBB", width=3, arrow=False):
        canvas.setStrokeColor(fill)
        canvas.setLineWidth(width)
        path = canvas.beginPath()
        path.moveTo(points[0][0], HEIGHT - points[0][1])
        for x, y in points[1:]:
            path.lineTo(x, HEIGHT - y)
        canvas.drawPath(path)
        svg.append(f'<polyline points="{" ".join(f"{x},{y}" for x, y in points)}" fill="none" stroke="{fill}" stroke-width="{width}" stroke-linejoin="round"/>')
        if arrow:
            x, y = points[-1]
            prev_x, prev_y = points[-2]
            if x == prev_x:
                triangle = [(x, y), (x - 7, y - 11), (x + 7, y - 11)]
            elif x < prev_x:
                triangle = [(x, y), (x + 11, y - 7), (x + 11, y + 7)]
            else:
                triangle = [(x, y), (x - 11, y - 7), (x - 11, y + 7)]
            p = canvas.beginPath()
            p.moveTo(triangle[0][0], HEIGHT - triangle[0][1])
            for xx, yy in triangle[1:]:
                p.lineTo(xx, HEIGHT - yy)
            p.close()
            canvas.setFillColor(fill)
            canvas.drawPath(p, fill=1, stroke=0)
            svg.append(f'<polygon points="{" ".join(f"{xx},{yy}" for xx, yy in triangle)}" fill="{fill}"/>')

    rect(0, 0, WIDTH, HEIGHT, "#F4F7FA")
    rect(76, 58, 140, 6, "#215FC2", radius=3)
    text(76, 92, "AI垂类公众号经营全流程", 48, "#18334D", True)
    text(78, 158, "路人甲的实操思路 × 易洋的经营框架", 27)
    for x, title, fill, ink in [(76, "选题与内容", "#E6EEFC", "#215FC2"),
                               (330, "分发与商务", "#E3F3EE", "#20755E"),
                               (584, "交付与复购", "#FCEDD9", "#9C6020")]:
        rect(x, 211, 226, 37, fill, 12)
        text(x + 37, 214, title, 22, ink, True)

    for index, (title, action, result) in enumerate(STEPS):
        y = 282 + index * 194
        fill, accent = (("#EAF1FD", "#215FC2") if index < 3 else
                        ("#E8F5F0", "#20755E") if index < 6 else
                        ("#FDF0DF", "#9C6020"))
        rect(76, y, 988, 164, "#FFFFFF", 22, "#D9E2EC", 1.4)
        rect(98, y + 25, 62, 62, fill, 19)
        text(113, y + 36, f"{index + 1:02d}", 29, accent, True, 50)
        text(184, y + 22, title, 35, "#18334D", True, 820)
        text(184, y + 78, action, 26, "#405368", max_width=830)
        text(184, y + 118, result, 23, accent, max_width=830)
        if index < len(STEPS) - 1:
            line([(570, y + 170), (570, y + 187)], arrow=True)

    # Feedback goes from stage 8 back to stage 2, outside the main reading path.
    line([(1066, 1722), (1127, 1722), (1127, 558), (1068, 558)], "#6A869F", 3, True)
    rect(1101, 1028, 52, 173, "#F4F7FA", 14)
    for index, char in enumerate("反馈回流"):
        text(1113, 1040 + 35 * index, char, 24, "#6A869F", max_width=30)

    rect(76, 1870, 988, 130, "#E8EDF3", 18)
    text(105, 1890, "每轮都检查", 26, "#18334D", True)
    text(105, 1935, "读者是否匹配  ·  是否实际到账  ·  扣成本后能否继续", 26, max_width=930)
    text(80, 2035, "内容生产与商务沟通可并行；复盘结果进入下一轮选题。", 25)
    text(80, 2080, "当前实践：7篇已发布，客户主动询价；成交与回款待验证。", 24)
    text(80, 2130, "综合整理 · 2026-10-16 · 历史经验不构成收益承诺", 21, "#6A7E92")
    svg.append("</svg>")
    (OUT / "AI垂类公众号经营全流程.svg").write_text("\n".join(svg), encoding="utf-8")
    canvas.showPage()
    canvas.save()
    (OUT / "chart-layout.json").write_text(
        json.dumps({"width": WIDTH, "height": HEIGHT, "labels": labels}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    renderer = shutil.which("pdftoppm")
    if not renderer:
        raise RuntimeError("缺少PDF渲染器pdftoppm，不能跳过视觉验收")
    subprocess.run([renderer, "-scale-to-x", str(WIDTH), "-scale-to-y", str(HEIGHT),
                    "-singlefile", "-png", str(PDF), str(OUT / "AI垂类公众号经营全流程")], check=True)
    print(f"已生成 {PDF.name}、SVG及从PDF渲染的PNG")


if __name__ == "__main__":
    main()
