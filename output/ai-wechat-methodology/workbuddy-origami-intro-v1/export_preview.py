"""Local browser raster export of this SVG's actual animated attribute values."""
from http.server import SimpleHTTPRequestHandler, HTTPServer
from io import BytesIO
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
FRAMES = {}

RENDER_JS = r'''
<button id="export" onclick="renderFrames()">生成 GIF 预览</button><p id="status">等待生成</p>
<script>
function freezeSVG(svg) {
  const clone = svg.cloneNode(true);
  const sources = [svg, ...svg.querySelectorAll('*')];
  const targets = [clone, ...clone.querySelectorAll('*')];
  sources.forEach((el, i) => {
    const animated = [...el.children].filter(n => ['animate','animateTransform'].includes(n.localName));
    const css = getComputedStyle(el);
    for (const anim of animated) {
      const attr = anim.getAttribute('attributeName');
      if (attr === 'transform') {
        const list = el.transform.animVal;
        let matrix = new DOMMatrix();
        for (let j=0; j<list.numberOfItems; j++) matrix = matrix.multiply(list.getItem(j).matrix);
        targets[i].setAttribute(attr, `matrix(${matrix.a} ${matrix.b} ${matrix.c} ${matrix.d} ${matrix.e} ${matrix.f})`);
      } else if (attr === 'd') {
        const d = css.getPropertyValue('d');
        targets[i].setAttribute('d', d.replace(/^path\(["']?/, '').replace(/["']?\)$/, ''));
      } else if (['fill','stroke','opacity','stroke-dashoffset'].includes(attr)) {
        targets[i].setAttribute(attr, css.getPropertyValue(attr));
      } else if (el[attr] && el[attr].animVal && typeof el[attr].animVal.value === 'number') {
        targets[i].setAttribute(attr, el[attr].animVal.value);
      } else throw Error('Unsupported animated attribute: '+attr);
    }
  });
  clone.querySelectorAll('animate, animateTransform').forEach(n => n.remove());
  clone.setAttribute('width', '1246'); clone.setAttribute('height', '220');
  clone.removeAttribute('style');
  return new XMLSerializer().serializeToString(clone);
}
async function renderFrames() {
  const button = document.getElementById('export'); button.disabled = true;
  const status = document.getElementById('status');
  try {
    const svg = document.querySelector('svg'); svg.pauseAnimations();
    const canvas = document.createElement('canvas'); canvas.width=1246; canvas.height=220;
    const ctx = canvas.getContext('2d');
    for (let i=0; i<160; i++) {
      svg.setCurrentTime(i/20);
      await new Promise(requestAnimationFrame);
      const frozen = freezeSVG(svg);
      const url = URL.createObjectURL(new Blob([frozen], {type:'image/svg+xml'}));
      const image = new Image(); image.src=url; await image.decode();
      ctx.fillStyle='white'; ctx.fillRect(0,0,1246,220); ctx.drawImage(image,0,0);
      URL.revokeObjectURL(url);
      const blob = await new Promise(resolve=>canvas.toBlob(resolve,'image/png'));
      const res = await fetch('/frame/'+i,{method:'POST',body:blob});
      if (!res.ok) throw Error(await res.text());
      status.textContent = '正在生成 '+(i+1)+'/160 帧';
    }
    const response = await fetch('/finish',{method:'POST'});
    if (!response.ok) throw Error(await response.text());
    status.textContent = await response.text();
  } catch (error) {status.textContent = '生成失败：'+error.message; button.disabled=false;}
}
</script>'''


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(HERE), **kwargs)

    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path != "/render.html":
            return super().do_GET()
        svg = (HERE / "intro.svg").read_text(encoding="utf-8")
        body = ('<!doctype html><html lang="zh"><meta charset="utf-8"><title>折纸手机动图导出</title>'
                '<body style="margin:20px;font-family:Microsoft YaHei;background:white">'+svg+RENDER_JS).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path.startswith("/frame/"):
            index = int(self.path.removeprefix("/frame/"))
            assert 0 <= index < 160
            png = self.rfile.read(int(self.headers["Content-Length"]))
            FRAMES[index] = Image.open(BytesIO(png)).convert("RGB")
            if index in [10, 44, 67, 89, 112, 133]:
                FRAMES[index].save(HERE / f"frame-{index/20:.2f}s.png")
            self.send_response(200)
            self.end_headers()
        elif self.path == "/finish":
            assert len(FRAMES) == 160
            frames = [FRAMES[i] for i in range(160)]
            # Sample the entire story so red, sage, lime and brand colors all survive GIF indexing.
            samples = Image.new("RGB", (312, 55*16))
            for i in range(16):
                samples.paste(frames[i*10].resize((312, 55)), (0, i*55))
            palette = samples.quantize(colors=256)
            colors = palette.getpalette()
            for i in range(0, len(colors), 3):
                if min(colors[i:i+3]) >= 248:
                    colors[i:i+3] = [255, 255, 255]
            colors[-3:] = [255, 255, 255]
            palette.putpalette(colors)
            indexed = [im.quantize(palette=palette, dither=Image.Dither.NONE) for im in frames]
            indexed[0].save(HERE / "intro.gif", save_all=True, append_images=indexed[1:], duration=50,
                            loop=0, optimize=False, disposal=2)
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("已生成 intro.gif：160 帧，8 秒循环".encode())
            print("GIF exported: 160 frames, 8 seconds", flush=True)
        else:
            self.send_error(404)


if __name__ == "__main__":
    print("Open http://127.0.0.1:8769/render.html for raster export", flush=True)
    HTTPServer(("127.0.0.1", 8769), Handler).serve_forever()
