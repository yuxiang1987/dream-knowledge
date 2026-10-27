"""用 MiniMax 视觉模型标注对标封面（结构化，便于统计）。

用法：python describe_covers.py
输入：E:/tmp/cover-corpus 下的 jpg；输出：同目录 covers-vision.json
只做客观字段标注（主体、文字位置、logo、明暗），不做效果判断。
"""
import concurrent.futures
import json
import pathlib
import re
import subprocess
import sys

CORPUS = pathlib.Path("E:/tmp/cover-corpus")
OUT = pathlib.Path(__file__).resolve().parent / "covers-vision.json"
PROMPT = (
    "请只按下面四行回答，不要额外解释：\n"
    "主体类型：<产品界面截图/人物场景/图形海报/实拍照片/3D渲染/拼贴混排/其他>\n"
    "画面文字：<有/无>；<有则写位置：左/中/右/上/下，以及文字行数>\n"
    "文字内容：<逐字写出看到的主要文字，最多两行；没有写“无”>\n"
    "品牌与产品：品牌名文字<有/无>；logo<有/无>；产品界面<有/无>\n"
    "视觉风格：<深色/浅色>，主色<2到3个颜色词>，画面元素数量<简洁/中等/密集>"
)


def describe(path: pathlib.Path) -> dict:
    mmx = next((p for p in (pathlib.Path("C:/Users/Administrator/AppData/Roaming/npm/mmx.cmd"),
                             pathlib.Path("C:/Users/Administrator/AppData/Roaming/npm/mmx")) if p.exists()),
                pathlib.Path("mmx"))
    try:
        proc = subprocess.run(
            [str(mmx), "vision", "describe", "--image", str(path), "--prompt", PROMPT,
             "--output", "json", "--quiet"],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        payload = json.loads(proc.stdout or "{}")
        text = payload.get("content") or ""
        if not text:
            return {"file": path.name, "error": (proc.stderr or proc.stdout)[:200]}
        fields = {}
        for line in text.splitlines():
            if "：" in line:
                key, _, value = line.partition("：")
                fields[key.strip()] = value.strip()
        return {"file": path.name, "raw": text, "fields": fields}
    except Exception as error:  # noqa: BLE001 - 记录失败原因，不中断整批
        return {"file": path.name, "error": f"{type(error).__name__}: {error}"}


def main() -> int:
    files = sorted(CORPUS.glob("*.jpg"))
    if not files:
        print("没有找到封面图片")
        return 1
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for item in pool.map(describe, files):
            results.append(item)
            print(f"{len(results)}/{len(files)} {item['file']} {'ERR' if 'error' in item else 'ok'}",
                  flush=True)
    OUT.write_text(json.dumps({"count": len(results),
                               "ok": sum(1 for r in results if "fields" in r),
                               "items": results}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"完成：{OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
