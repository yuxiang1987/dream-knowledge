"""编译人工逐篇记录与已有拆解，生成60篇研究台账；原始资料始终只读。"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote

from benchmark_research_notes import FIELDS, NEW, REUSED_QUESTIONS, SUPPORTING

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/ai-wechat-methodology"
DATE = "2026-10-16"
TOPIC = "路人甲TM文章经营全景"
SOURCE_MARK = "## 最新归档批次的关联"

# 归属限文章自述；主产品是研究对象，不等同已核实付款方。
META = {
    "特斯拉Roadster": ("汽车/资讯对象", "特斯拉；非默认AI方向"),
    "WorkBuddy": ("桌面Agent", "腾讯（文章语境）"),
    "OiiOii": ("视频创作平台", "品牌明确，公司与签约主体待核"),
    "Vidu": ("视频模型/产品线", "生数科技（实时角色篇自述）"),
    "腾讯乐享": ("企业知识治理平台", "腾讯（文章命名）"),
    "Space Bunny Alpha": ("匿名模型", "未知；不采纳身世猜测"),
    "Hy Image3.5 preview": ("图像模型", "腾讯（文章语境）"),
    "元宝": ("图像模型使用端/应用", "腾讯产品语境，实际签约主体待核"),
    "QwenNote A2": ("录音与Agent硬件", "千问办公产品线（文章语境）"),
    "千问办公": ("办公Agent与服务", "千问产品线（文章语境）"),
    "美图设计室": ("设计营销平台", "美图（文章命名）"),
    "Marvis": ("电脑管家Agent", "腾讯（文章标题）"),
    "MVLAND": ("音乐视频创作平台", "品牌明确，公司与签约主体待核"),
    "Jev": ("快速分类/决策模型", "TypeSafe AI（文章自述）"),
    "元脑AI Work一体机": ("企业模型与Agent管理软硬件", "文章未明确签约主体，不由品牌补造"),
    "豆包工作": ("办公Agent/工作模式", "豆包产品线（材料名称，需核产品边界）"),
    "Hy4 preview": ("模型", "腾讯（文章标题）"),
    "MiniMax Design": ("视频项目Agent平台", "MiniMax（文章命名）"),
    "RunningHub": ("视频工作流平台", "品牌明确；rhTV为文中使用模块"),
    "Seedance": ("视频模型家族", "材料含2.0、2.0 Fast与2.5，签约主体未知"),
    "MiniMax H3": ("视频模型", "MiniMax（材料命名，版本未独立核实）"),
    "Wan3.0": ("视频模型", "阿里（文章标题，版本未独立核实）"),
    "EvoX": ("多Agent协作平台", "创业团队（文章自述，具体主体未给）"),
    "Kimi": ("模型及Agent应用", "月之暗面（横评文章自述）"),
    "Vivix": ("实时角色/故事模型产品线", "Vivix（文章自述），A1和W1分工"),
    "巨日禄": ("短剧制作与转绘平台", "品牌明确，公司与签约主体待核"),
    "WeaveFox": ("网页应用创作平台", "品牌明确；赛事角色不等于合同主体"),
    "MonkeyCode": ("开源Coding与托管使用端", "项目品牌明确；开源项目和托管服务需区分"),
}


def canonical(title):
    return re.sub(r"\W", "", title).lower()


def display(name):
    return name.replace("（材料命名）", "")


def plain(text):
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def front(title, kind, raw_paths, status="稳定", created=DATE):
    return ["---", f"title: {title}", f"type: {kind}", "tags: [公众号, 路人甲TM, 选题, 商务研究]",
            f"status: {status}", f"sources: [{', '.join(raw_paths)}]", f"created: {created}",
            f"updated: {DATE}", "---", "", f"# {title}", ""]


def old_observations():
    text = (ROOT / "wiki/topics/路人甲TM文章写法拆解.md").read_text(encoding="utf-8")
    result = {}
    for line in text.splitlines():
        if line.startswith("| [[sources/"):
            cells = [s.strip() for s in line.split("|")[1:-1]]
            name = re.search(r"\[\[sources/([^\]]+)\]\]", cells[0]).group(1)
            result[name] = {"title_pattern": cells[2], "hook": cells[3], "structure": cells[4], "ending": cells[5]}
    return result


def new_source(record):
    raw = record["raw_path"]
    status = "有冲突" if record["archive_rank"] in (8, 55) else "稳定"
    lines = front(Path(record["source_page"]).stem, "source", [raw], status)
    note_text = " ".join(str(record[k]) for k in ("cases", "structure", "method", "boundary", "business", "own_idea"))
    glossary = {"Agent": "能调用工具推进任务的AI", "Skill": "可复用的做事方法与操作说明",
                "Harness": "模型运行时的工具和执行环境", "Prompt": "交给AI的输入指令",
                "HTML": "可在浏览器打开的网页文件", "Shot": "项目中的单个镜头节点",
                "Timeline": "剪辑时间线", "VI": "品牌视觉规范", "API": "软件之间的调用接口",
                "Token": "模型处理文字等信息的计量单位", "Gene": "原文平台保存的可复用任务经验"}
    terms = [f"{key}指{value}" for key, value in glossary.items()
             if re.search(r"(?<![A-Za-z])" + re.escape(key) + r"(?![A-Za-z])", note_text, re.I)]
    lines += [f"来源：`{raw}`。标题「{record['title']}」，发布时间 {record['published']}。",
              "", "本页分析文字中的选题与写法。图片、动图和视频未逐一观看，作者声称的测试结果不是本知识库重新实测；产品版本、榜单、价格与商业成绩没有在本轮独立核实。", "",
              *((["术语：" + "；".join(terms) + "。", ""]) if terms else []),
              "## 它讲什么", "", record["question"], "",
              f"主研究对象：{'、'.join(record['primary_products'])}；方向：{record['direction']}；主类型：{record['primary_type']}。主类型是整理者按文章目的归类，不是原作者逐篇自标。", "",
              "## 案例与推进", "", record["cases"], "", record["structure"], "",
              "## 标题、开头与可迁移写法", "", f"标题采用：{record['title_pattern']}。", "",
              record["hook"], "", record["method"], "",
              "## 证据锚点与边界", "", f"正文定位短句：「{record['anchor']}」。此句可以回到原文检索，不用它单独证明整篇所有结论。", "",
              record["boundary"], "",
              "## 产品与商务线索", "", record["business"], "",
              f"关联的模型、使用端或工具：{'、'.join(record['supporting_products']) or '本条未另行登记'}。这是角色说明，不是已知合作名单。", "",
              "作者在分享中自述账号内容100%商单，作为账号级依据保留；该说法有口述时点，不能据此推定本篇合同、实际付款方、金额或当前预算。本轮未采集评论，不把作者提及读者意见等同完整评论需求调查。", "",
              "## 对自己可执行的迁移", "", record["own_idea"], "",
              "这是待执行案例策划，尚未亲测。先核可用版本、账号权限、素材使用条件和预算，再让用户实操并留证；不移植作者的亲友故事或测试结果。", "",
              "## 与其他页面的关系", "", f"- [[topics/{TOPIC}]]", "- [[topics/AI公众号产品选题与客户地图]]",
              "- [[topics/AI写作案例库]]", "- [[topics/证据与边界库]]"]
    return "\n".join(lines) + "\n"


def main():
    manifest = json.loads((OUT / "路人甲TM最新60篇下载清单.json").read_text(encoding="utf-8"))
    old = json.loads((OUT / "路人甲TM文章产品台账.json").read_text(encoding="utf-8"))
    previous = {canonical(r["title"]): r for r in old["articles"]}
    old_products = {p["id"]: p for p in old["products"]}
    table = old_observations()
    records = []
    assert len(manifest["articles"]) == 60 and manifest["complete"]
    for n, article in enumerate(manifest["articles"], 1):
        readable_path = next((OUT / "路人甲TM最新60篇可读版").glob(f"{n:02d}-*.md"))
        body = plain(readable_path.read_text(encoding="utf-8").split("\n---\n", 1)[1])
        record = {"id": f"LRJ60-{n:02d}", "archive_rank": n, "title": article["title"],
                  "published": article["published"], "raw_path": article["raw_path"],
                  "public_url": article["url"], "raw_sha256": digest(ROOT / article["raw_path"]),
                  "readable_path": readable_path.relative_to(ROOT).as_posix(),
                  "sponsor": None, "current_budget": None, "contact": None,
                  "media_reviewed": False, "comments_collected": False}
        reused = previous.get(canonical(article["title"]))
        if reused:
            assert n in REUSED_QUESTIONS, n
            observations = table[Path(reused["source_page"]).stem]
            question, own_idea = REUSED_QUESTIONS[n]
            method = observations["structure"] + "；结尾：" + observations["ending"]
            paragraph = next(s.strip().lstrip("# ") for s in body.split("\n\n") if len(s.strip()) >= 12)
            record.update({"review_mode": "复用已有单篇拆解并核对新快照对应", "source_page": reused["source_page"],
                "previous_raw_path": reused["raw_path"], "previous_raw_sha256": reused["raw_sha256"],
                "previous_record_id": reused["id"],
                "primary_products": [display(old_products[p]["name"]) for p in reused["primary_product_ids"]],
                "supporting_products": [], "direction": reused["direction"].replace("AI视频相关素材", "图像设计"),
                "primary_type": reused["primary_type"], "secondary_tags": reused["secondary_tags"],
                "question": question, "hook": observations["hook"], "title_pattern": observations["title_pattern"],
                "cases": reused["case"], "structure": observations["structure"], "method": method,
                "boundary": "沿用已有单篇拆解的具体边界；媒体未重看，宣传数字未独核。详见单篇正文。",
                "anchor": paragraph.split("。", 1)[0][:55], "own_idea": own_idea,
                "business": "账号级商单自述保留；单篇付费方及当前预算未核，原拆解中的推广观察仍按历史语境使用。"})
        else:
            assert n in NEW, (n, article["title"])
            note = dict(zip(FIELDS, NEW[n], strict=True))
            assert note["anchor"] in body, (n, note["anchor"])
            record.update({k: v for k, v in note.items() if k not in ("page", "products")})
            record.update({"source_page": f"wiki/sources/{note['page']}.md", "primary_products": note["products"],
                           "supporting_products": SUPPORTING.get(n, []), "review_mode": "新样本文字阅读与原文锚点核验",
                           "secondary_tags": [], "title_pattern": title_pattern(article["title"])})
        records.append(record)

    for r in records:
        path = ROOT / r["source_page"]
        if r["archive_rank"] in NEW:
            path.write_text(new_source(r), encoding="utf-8")
        else:
            text = path.read_text(encoding="utf-8")
            front_text, body = text[4:].split("\n---\n", 1)
            lines = front_text.splitlines()
            for i, line in enumerate(lines):
                if line.startswith("sources: [") and r["raw_path"] not in line:
                    lines[i] = line[:-1] + ", " + r["raw_path"] + "]"
                elif line.startswith("updated:"):
                    lines[i] = f"updated: {DATE}"
            body = body.split(SOURCE_MARK, 1)[0].rstrip()
            body += (f"\n\n{SOURCE_MARK}\n\n2026-10-16按标题与账号核对到最新60篇批次的同篇快照：`{r['raw_path']}`。"
                     f"原有拆解及其历史证据保留；统一研究记录 {r['id']} 见 [[topics/{TOPIC}]]。本次未重新观看媒体，不把原作者测试改写为自己的实测。\n")
            path.write_text("---\n" + "\n".join(lines) + "\n---\n" + body, encoding="utf-8")

    products = make_products(records, old)
    stats = {"articles": len(records), "new_sources": len(NEW), "reused_sources": len(REUSED_QUESTIONS),
             "primary_product_count": sum(bool(p["primary_article_ids"]) for p in products),
             "all_research_objects": len(products),
             "types": dict(Counter(r["primary_type"] for r in records)),
             "directions": dict(Counter(r["direction"] for r in records))}
    data = {"schema_version": 1, "updated": DATE, "coverage": "最新60篇时间窗口，含22篇既有分析与38篇新增；不是作者全部历史",
            "account_claim": old["account_claim"],
            "classification": "主类型按文章目的作互斥统计；副标签可交叉。整活为表现标签，不是整合。",
            "scope": "全文文字研究与既有拆解复用；未逐一核看图像视频、未采评论、未验证单篇付款和现行产品信息",
            "stats": stats, "products": products, "articles": records}
    (OUT / "路人甲TM六十篇拆解台账.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / f"wiki/topics/{TOPIC}.md").write_text(overview(data), encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False))


def title_pattern(title):
    # 仅识别可直接看见的词法，不把词法当传播效果证明。
    parts = []
    if "？" in title or "?" in title:
        parts.append("问题或悬念")
    if any(k in title for k in ("我", "实测", "试")):
        parts.append("作者动作或测试")
    if any(k in title for k in ("教程", "手把手", "看完")):
        parts.append("行动与学习承诺")
    if any(k in title for k in ("终于", "最新", "新功能", "更新")):
        parts.append("时效变化")
    return "＋".join(parts) if parts else "对象＋结果或判断"


def make_products(records, old):
    historical = {display(p["name"]): p for p in old["products"]}
    names = sorted({n for r in records for n in r["primary_products"] + r["supporting_products"]})
    products = []
    for i, name in enumerate(names, 1):
        main = [r for r in records if name in r["primary_products"]]
        related = [r for r in records if name in r["supporting_products"]]
        old_meta = historical.get(name)
        level, brand = META.get(name, (old_meta["level"], old_meta["brand_in_material"]) if old_meta
                               else ("关联模型、工具或渠道", "文章中共现；当前主体未核"))
        products.append({"id": f"PRODUCT-{i:03d}", "name": name, "level": level, "brand_in_material": brand,
                         "directions": sorted({r["direction"] for r in main}),
                         "primary_article_ids": [r["id"] for r in main],
                         "supporting_article_ids": [r["id"] for r in related],
                         "types": sorted({r["primary_type"] for r in main}),
                         "reader_questions": list(dict.fromkeys(r["question"] for r in main)),
                         "task_proposals": list(dict.fromkeys(r["own_idea"] for r in main)),
                         "actual_sponsor": None, "current_budget": None, "verified_contact": None,
                         "verification": "历史内容研究线索；实际商务角色、现行版本、权限与入口待核"})
    return products


def overview(data):
    records, stats = data["articles"], data["stats"]
    lines = front(TOPIC, "topic", [r["raw_path"] for r in records], "进行中")
    lines += ["## 这次完成了什么", "",
        "覆盖账号文章栏目2026-07-22至2026-10-16的最新60篇，22篇复用已有单篇拆解，38篇新建source页。原来23篇中的Qwen-Image-3.0文章不在这60篇窗口里，仍保留，不能把23与60相加说成83篇独立文章；两批合起来是61篇标题可对应的独立样本。", "",
        "新样本逐篇读文字，再校验短句锚点；复用项保留原分析并关联新快照。未逐一观看图片和视频、未重新运行产品，没有完整评论区、阅读反馈、合同或回款数据。以下统计是内容样本分布，不是流量、投放额、市场份额或本账号接单概率。", "",
        "AI Agent（能调用工具推进任务的AI系统）与Coding（用AI开发和修改应用）存在交叉，本表按文章主问题归一个方向；生图、设计单列为交叉能力，不据此扩展账号默认范围。Harness指模型干活的工具与执行环境；CTA指文中引导读者下一步行动的入口。", "",
        "给人快速查看：[选题与客户速查表](../../output/ai-wechat-methodology/路人甲TM选题与客户速查表.md)。给Agent检索的完整记录在文末。", "",
        "## 对选题最有用的结论", "",
        "**产品名只解决去哪里找素材，读者问题和自己的证据才形成选题。** 同一WorkBuddy在多个更新、任务和使用者场景反复出现，说明可沿产品做系列，不需要每篇另找一个新工具。频繁出现仅证明本窗口覆盖多，不证明续约、预算、独家关系或哪个题型更能成交。", "",
        "**按问题延伸比换案例名更有价值。** 资料库回答多人协作，远程连接回答离开电脑，文件浏览器回答单文件操作，企微接入回答资料搬运。每次产品功能变化要落到一个新的阻碍；只改人物和商品而没有新的观察点，不足以构成自己的测评。", "",
        "**内容可围绕一个项目扩成不同证据。** 品牌资产可以做设计一致性和借势营销，短片可以做机位控制、镜头返修与出海。已有项目降低准备成本，但一个成功结果不能当成多次独立验证。不是所有文章都要全面、深难或横评。", "",
        "**模型和使用端要分层找客户。** Flova、LibTV、RunningHub借模型发布组织工作流卖点；标题里有Seedance、H3或Wan，不等于这篇付费方就是模型厂商。平台主推、模型依赖、参考品牌、活动组织方都应分列。", "",
        "**可学任务组织，不继承所有宣传承诺。** Vivix仍排队、Astra演示汇总未亲测；视频中的UI不是可运行应用；做出片不是广告有效，也不是创作者已经获得合作。", "",
        "## 样本分布", "",
        "主类型是整理者按主要目的编码，每篇恰计一次；实测通常落在实战，整活可以跨类型。观点/资讯并未消失，不能把作者分享中的偏好写成其账号绝无此类文章。", "",
        "| 主类型 | 篇数 |", "| --- | ---: |"]
    lines += [f"| {k} | {v} |" for k, v in stats["types"].items()]
    lines += ["", "| 主方向 | 篇数 |", "| --- | ---: |"]
    lines += [f"| {k} | {v} |" for k, v in stats["directions"].items()]
    lines += ["", f"主研究产品/对象共{stats['primary_product_count']}项，含具体工具未明确的占位项与邻接资讯对象，并非这些数量的已核实AI品牌；含仅作依赖或渠道的关联项共{stats['all_research_objects']}项。仅登记与研究问题相关的对象，不穷尽素材中每个品牌或模型。一个多产品横评可关联多对象，所以产品关联次数不能当文章篇数。", "",
              "## 产品、问题与客户研究地图", "",
              "以下按主研究文章数排序。模型名称、品牌归属和版本仅按历史材料；主对象也可能只是比较对象或资讯对象。无论是否有明确CTA，实际付款方、当前预算与联系人一律未知。", "",
              "| 产品/对象 | 层级 | 材料里的归属 | 主研究篇数 | 方向 | 来源 |", "| --- | --- | --- | ---: | --- | --- |"]
    by_id = {r["id"]: r for r in records}
    for p in sorted(data["products"], key=lambda p: (-len(p["primary_article_ids"]), p["name"])):
        if not p["primary_article_ids"]:
            continue
        refs = "、".join(f"[[sources/{Path(by_id[i]['source_page']).stem}|{i}]]" for i in p["primary_article_ids"])
        lines.append(f"| {p['name']} | {p['level']} | {p['brand_in_material']} | {len(p['primary_article_ids'])} | {'、'.join(p['directions'])} | {refs} |")
    lines += ["", "## 六类文章怎么对应案例", "",
        "| 类型 | 核心交付 | 样本入口 | 自己开始前要补的证据 |", "| --- | --- | --- | --- |",
        "| 实战型 | 具体成果、观察细节和取舍 | Vidu六场景、Miora品牌、WeaveFox游戏 | 自己真实操作、修改和失败，不复述作者的成功 |",
        "| 解决问题型 | 一个障碍怎样被解决、何时仍不能解决 | 企微材料、资料库同步、镜头局部返修 | 修改前后的对照，条件与未解决的问题 |",
        "| 教程型 | 从起点到目标的可复现路径 | 入门、做小程序、MonkeyCode、Seko新手 | 当前入口、必要权限、关键步骤与退出条件 |",
        "| 整合型 | 有依据的资源/案例组织 | DSH插件、Jev案例、Astra公开演示 | 自试、第三方展示和待测分层，资源可用性 |",
        "| 观点型 | 从现象到判断的证据链 | 美图转型、豆包爱学 | 一手事实、替代解释和无法确定部分 |",
        "| 资讯型 | 变化、出处与影响 | Vivix、特斯拉 | 可用性与亲测身份，技术及价格核验 |", "",
        "## 60篇逐篇入口", "",
        "每条记录均含问题、案例、结构、可迁移方法、边界、产品角色与自己的待测方向。复用22篇可进入原source看更详细过程，38篇新增source独立保存分析。", "",
        "| 编号 | 日期 | 拆解 | 主产品 | 主类型 | 处理方式 |", "| --- | --- | --- | --- | --- | --- |"]
    for r in records:
        name = Path(r["source_page"]).stem
        label = "新增" if r["archive_rank"] in NEW else "复用"
        lines.append(f"| {r['id']} | {r['published'][:10]} | [[sources/{name}]] | {'、'.join(r['primary_products'])} | {r['primary_type']} | {label} |")
    lines += ["", "## 值得复用的系列关系", "",
        "- **WorkBuddy从能做走向能继续用**：LRJ60-33入门、48协作、44远程、06单文件、02企微、05小程序分别回答不同阶段的问题；这是编辑研究路径，不断言作者按这个顺序规划过内容漏斗。",
        "- **视频模型→平台流程→局部控制**：H3首测53与LibTV使用55、Seedance在Flova50和LibTV51、后续Skill22说明同一能力可写不同问题；同底模的多平台出现不等于可直接证明谁更好。",
        "- **存量素材延长价值**：updream43、Seko26、巨日禄57分别研究预演和版本转绘，不能凭题材相似声称所有文章复用了同一片子。",
        "- **完整品牌→持续运营**：Miora58聚焦基础品牌资产，美图设计室12聚焦热点与持续视觉。品牌均为虚构，不将它们记成真实付费客户。", "",
        "## 不要照搬的证据问题", "",
        "| 样本 | 原文两侧信息 | 处理方式 |", "| --- | --- | --- |",
        "| LRJ60-08 | Space Bunny三题20、15、41分钟，加总76分钟；汇总写80分钟 | 保留两侧，标有冲突，不替作者改原文 |",
        "| LRJ60-16 | 开头说实时对战、联机；后文收紧为单人玩加实时榜 | 自己的标题按已测试范围写，不承诺多人同步对撞 |",
        "| LRJ60-37 | 0.6元/秒、2.9折与最低0.10元/秒同时出现 | 0.6×0.29=0.174；最低档条件未明，不把它们当同一计价条件 |",
        "| LRJ60-39 | 标题三款热门模型，正文因排队主测两款 | 按实际覆盖两款解读，不生成完整三方胜负表 |",
        "| LRJ60-55 | 同片132对243积分，结尾说不到一半 | 实际约54.3%，保留成本口径冲突，活动最低价另算 |",
        "| LRJ60-56、27 | 排队/尚未亲测，但有大量效果描述 | 归为资讯或公开演示整合，不记作者已完成全部测试 |",
        "| LRJ60-53、35 | 游戏界面视频看似有鼠标或按钮 | 视频宣发不等于可运行游戏；与Qoder/MonkeyCode应用案例分开 |", "",
        "## 程序员拾梦的候选选题工作台", "",
        "以下是基于现有文章与案例经验的策划提案，全部待实操，不是已完成测试。先做最贴近已有素材的一项；账号没有现成的权限或材料就跳过，优先级按准备条件选，不按对标标题声量决定。", "",
        "| 可选问题 | 复用材料 | 最小任务与完成条件 | 何时适合作商务样板 |", "| --- | --- | --- | --- |",
        "| 七篇文章如何变成可信选题周报 | 自己7篇原稿及后台快照 | 查清主题、素材、已做/未做和来源，故意放一条旧口径检查溯源 | 有具体读者问题与可复现的资料治理案例后 |",
        "| 自己做的工具别人能否继续用 | 已有小工具或小程序项目 | 一个真实数据操作、可访问链接、一次同链接更新；区分试用与正式发布 | 同类Coding产品无需先做一整套长文 |",
        "| 一个项目离开电脑还能接着改吗 | 已有项目与两个设备 | 只改指定文件，记录开机、断联、权限与回滚条件 | 展示远程续接的适用条件及真实失误 |",
        "| 选题看板能否双人协作 | 当前选题表 | 两人同时改、跨端核对、撤销访问各做一次 | 能讲清协作和数据保存，不止网页截图 |",
        "| 群里碎资料能否找到且不乱发 | 获准使用的脱敏项目群 | 准备已知材料清单，核漏项、冲突日期和发送前确认；没有群权限就不选 | 适合有真实办公场景的连接器案例 |",
        "| 强视频模型用起来究竟贵在哪 | 自有或获准短片和参考图 | 只选一个平台、两个镜头，记全部失败、返修与人工时间；先确认实际价格 | 有制作账和可对照局部修复结果 |",
        "| 小模型能否辅助筛选题 | 人工先标注的选题样本 | 只测分类/评分，保留误选与漏选，不让它自动写稿和联系客户 | 证明具体分工价值，不用快判断冒充深度策划 |",
        "| 旧片换语种是否仍讲同个故事 | 自己的短片与目标语言核对人 | 一个短片段，核角色关系、台词、节奏和目标读者反馈 | 有本地化证据再写，不以出片当出海成功 |", "",
        "## 从产品线索到商业闭环的执行规则", "",
        "1. 从地图选一个符合定位、能拿到权限的主产品，列它在对标文章中已经回答的问题。",
        "2. 选自己的读者仍有、自己材料能验证的一个问题。没有真实评论就使用待验证假设，不能编读者痛点。",
        "3. 设计最小案例，规定输入、保留项、观察点和停止条件。先做出新证据，不必每篇更难或更长。",
        "4. 出一份样板提案：我服务什么读者、准备验证什么、有哪些已完成同类作品。没有同产品已发稿也可以先沟通，原账号已有主动询价。",
        "5. 联系前另核产品主体、当前需求和公开商务入口。地图只提供依据，不自动联系任何人，不保证对标投过就会投我们。",
        "6. 将确认合作、交付、验收、到账分别留痕。曝光、询价与提报都不记作回款；自然/加热流量分开，按全成本复盘。", "",
        "## 供Agent检索", "",
        "机器可读入口：[六十篇拆解台账](../../output/ai-wechat-methodology/路人甲TM六十篇拆解台账.json)。含60条文章记录、正文锚点、raw哈希、产品与使用端角色、来源页、分类、案例、迁移提案，以及明确为空的预算和联系人字段。", "",
        "提问示例：某产品写过哪些问题？哪些是亲测，哪些只是演示？想测局部修改有哪些任务原型？与自己的已有文章重合在哪里？回答必须追溯文章编号与source，不用产品频次估算预算。", "",
        "## 相关页面", "", "- [[topics/AI公众号产品选题与客户地图]]", "- [[topics/路人甲TM文章写法拆解]]",
        "- [[topics/AI公众号商单商业闭环]]", "- [[topics/AI写作案例库]]", "- [[topics/公众号商单实施复盘]]"]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
