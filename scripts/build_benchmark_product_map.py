"""将现有路人甲文章整理成可追溯的产品、题型、案例与商务研究台账。"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/ai-wechat-methodology"
DATE = "2026-10-16"

# 归属只登记文章中的历史线索，不宣称已核实当前商务主体。
PRODUCTS = [
    ("workbuddy", "WorkBuddy", ["AI Agent", "Coding"], "应用/Agent", "腾讯（材料语境）", "新手上手、文件任务、小程序", "已有3篇自主作品"),
    ("baidu_dazi", "百度搭子", ["AI Agent"], "办公Agent", "百度（材料名称）", "直播材料、内容工作流、数据报告", "暂无同产品已发布样本"),
    ("buzz", "Buzz", ["AI Agent", "Coding"], "多Agent协作平台", "Block（原文自述，当前主体待核）", "共享上下文、角色分工、交接", "暂无同产品已发布样本"),
    ("deepseek_harness", "DeepSeek Harness / DSH", ["AI Agent", "Coding"], "Harness与插件生态", "DeepSeek（材料语境）", "同模型换外壳、插件与执行约束", "暂无同产品已发布样本"),
    ("qoder", "Qoder", ["Coding", "AI Agent"], "开发工具/产品线", "阿里（原文标题）", "照片、草图、音频转应用", "暂无同产品已发布样本"),
    ("gpt6_astra", "GPT-6 Astra（材料命名）", ["Coding", "AI Agent"], "模型及使用端", "OpenAI（材料语境，命名/版本未独立核实）", "空间、程序、电脑操作与成本", "已有湖景房与游戏实测；另有替补选题"),
    ("qwen38", "Qwen3.8-27B（材料命名）", ["Coding"], "模型", "阿里（原文标题）", "本地/云端部署、硬件和任务表现", "暂无同产品已发布样本"),
    ("seed_evolving", "豆包 Seed-Evolving（材料命名）", ["Coding", "AI Agent"], "模型", "豆包产品线（材料命名，商务主体待核）", "长程任务、推理与核查", "暂无同产品已发布样本"),
    ("qwen_image", "Qwen-Image-3.0（材料命名）", ["AI视频相关素材"], "图像模型", "Qwen产品线（材料语境）", "中文图像、海报、分镜", "暂无同产品已发布样本"),
    ("gpt_image", "GPT Image2.5（材料命名）", ["AI视频相关素材"], "图像模型/编辑", "OpenAI（材料语境，命名/版本未独立核实）", "草图、生图、局部编辑与前后对照", "已有1篇自主实测"),
    ("pixmax", "Pixmax", ["AI视频"], "视频制作平台", "Pixmax产品品牌；公司主体待核", "短片制作、成本和团队协作", "暂无同产品已发布样本"),
    ("wanxing", "万兴剧厂", ["AI视频"], "视频制作平台", "万兴产品线（原文命名，签约主体待核）", "剧本、分镜、资产到机甲短片", "暂无同产品已发布样本"),
    ("updream", "updream预演台", ["AI视频"], "预演/空间控制工具", "updream产品品牌；公司主体待核", "白模、机位、走位与运镜", "暂无同产品已发布样本"),
    ("libtv", "LibTV", ["AI视频"], "视频平台/Skill宿主", "LibTV产品品牌；公司主体待核", "长视频节点与连续性Skill", "暂无同产品已发布样本"),
    ("seko", "Seko", ["AI视频"], "视频Agent/转绘工具", "Seko产品品牌；公司主体待核", "存量短片本地化与剧本适配", "暂无同产品已发布样本"),
    ("miora", "Miora", ["AI Agent", "AI视频相关素材"], "设计Agent", "腾讯（原文标题）", "Logo、品牌物料、视频与界面", "暂无同产品已发布样本"),
    ("uu_remote", "UU远程", ["Coding配套工具"], "远程控制工具", "网易资深团队（原文表述，签约主体待核）", "离开电脑继续任务、移动操作", "暂无同产品已发布样本"),
    ("doubao_aixue", "豆包爱学", ["邻接样本"], "教育应用", "豆包产品线（材料命名，商务主体待核）", "诗词的地理、人物与知识联系", "非本账号默认主线"),
    ("meitu", "美图", ["邻接样本"], "公司/产品组合", "美图（原文对象）", "公司转型与产品结构分析", "非本账号默认主线"),
    ("unspecified_design", "原文未明确的AI设计/建模工具", ["AI视频相关素材"], "具体工具未明", "待核实；不得将苹果当作已确认客户", "配件概念设计与3D展示", "暂无可对应的具体产品样本"),
]

# 每项为原文唯一定位词、摘要页、主产品、主要内容方向、文章目的、表现标签、核心案例。
ARTICLES = [
    ("AI办公智能体增速第一", "百度搭子三道题文章拆解", ["baidu_dazi"], "AI Agent", "实战型", ["实测", "多案例"], "发布会材料、内容链路、财报核查"),
    ("GPT-6 Atsra终于开放", "GPT-6-Astra连测文章拆解", ["gpt6_astra"], "Coding", "实战型", ["实测", "多案例"], "五项跨能力任务与加测失败"),
    ("Qwen-Image-3.0实测", "Qwen-Image-3实测文章拆解", ["qwen_image"], "AI视频相关素材", "实战型", ["实测", "对照"], "中文图像、海报、UI和分镜"),
    ("WorkBuddy最新教程", "WorkBuddy入门教程文章拆解", ["workbuddy"], "AI Agent", "教程型", ["实战", "新手上手"], "生活工作台与PDF文件匹配"),
    ("阿里Qwen3.8-27B", "Qwen3.8-27B本地模型实测文章拆解", ["qwen38"], "Coding", "实战型", ["实测", "部署条件"], "规则、文档应用与空间算法"),
    ("开源黑马Buzz", "Buzz多Agent协作文章拆解", ["buzz"], "AI Agent", "教程型", ["实战", "解决问题", "翻车复盘"], "多Agent开发数据分析工具"),
    ("把B站干崩", "Pixmax修仙短剧文章拆解", ["pixmax"], "AI视频", "实战型", ["整活", "作品复刻", "成本"], "自有角色制作凝结元婴短片"),
    ("半夜秃袭", "GPT-Image2.5草图生图文章拆解", ["gpt_image"], "AI视频相关素材", "实战型", ["实测", "对照", "整活"], "草图、品牌物料与图像编辑"),
    ("不睡觉连肝三小时", "DeepSeek原生Harness文章拆解", ["deepseek_harness"], "Coding", "实战型", ["实测", "对照"], "固定模型改变Harness进行三组测试"),
    ("拆解爆火的天才机甲师", "天才机甲师拆解文章拆解", ["wanxing"], "AI视频", "实战型", ["教程", "整活", "第三方素材混合"], "自有机甲短片的分镜、资产、机位与组接"),
    ("豆包爱学这次", "豆包爱学诗词山河文章拆解", ["doubao_aixue"], "邻接样本", "观点型", ["产品体验", "价值判断"], "诗词与地点、诗人轨迹连接的体验"),
    ("还在靠抽卡做视频", "updream预演台文章拆解", ["updream"], "AI视频", "解决问题型", ["实测", "对照", "作品"], "白模控制静态、简单与复杂运镜"),
    ("美图，不止", "美图公司分析文章拆解", ["meitu"], "邻接样本", "观点型", ["公司分析", "无实测"], "产品组合与公司转型解释"),
    ("全新Qoder实测", "全新Qoder实测文章拆解", ["qoder"], "Coding", "实战型", ["实测", "多输入"], "照片、草图与录音转成可运行项目"),
    ("实测豆包Seed-Evolving", "豆包Seed-Evolving实测文章拆解", ["seed_evolving"], "Coding", "实战型", ["实测", "事实核查"], "知识图谱、游戏与交叉核查"),
    ("手机、电脑无缝衔接", "UU远程Vibecoding文章拆解", ["uu_remote"], "Coding配套工具", "解决问题型", ["实测", "场景"], "手机继续Coding、办公应急与游戏"),
    ("为了让AI拍完长视频", "长视频导演Skill文章拆解", ["libtv"], "AI视频", "解决问题型", ["实战", "对照", "自建Skill"], "长视频导演Skill与节点连续性对照"),
    ("我给DeepSeek Harness搭", "DSH插件市场文章拆解", ["deepseek_harness"], "AI Agent", "整合型", ["教程", "实战", "自建工具"], "插件资源整理与自建使用量面板"),
    ("我给iPhone Duo", "iPhoneDuo配件设计文章拆解", ["unspecified_design"], "AI视频相关素材", "实战型", ["整活", "概念设计", "非实物"], "手机壳、手写笔、支架概念方案与3D展示"),
    ("我让腾讯Miora", "Miora火锅店品牌全案文章拆解", ["miora"], "AI Agent", "实战型", ["整活", "完整项目", "品牌设计"], "虚构火锅店Logo、包装、海报、视频和界面"),
    ("这就是AGI", "GPT-6-Astra演示汇总文章拆解", ["gpt6_astra"], "Coding", "整合型", ["资讯", "观点", "第三方演示", "无亲测"], "公开演示汇总与拒绝轻率宣布胜负"),
    ("只用五分钟，Seko", "Seko出海转绘文章拆解", ["seko"], "AI视频", "解决问题型", ["实测", "作品", "版本对照"], "52秒自有短片的多地区版本与剧本适配"),
    ("手把手教你用WorkBuddy做微信小程序", "WorkBuddy小程序教程文章拆解", ["workbuddy"], "AI Agent", "教程型", ["实战", "解决问题"], "家庭记账试用小程序、改账单与网站转小程序"),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    raw_files = list((ROOT / "raw/article/lurenjiaTM").glob("*.md"))
    product_ids = {p[0] for p in PRODUCTS}
    records = []
    for index, (key, source, products, direction, purpose, tags, case) in enumerate(ARTICLES, 1):
        hits = [p for p in raw_files if key in p.name]
        assert len(hits) == 1, key
        raw = hits[0]
        text = raw.read_text(encoding="utf-8-sig")
        summary = ROOT / f"wiki/sources/{source}.md"
        assert summary.is_file(), summary
        assert set(products) <= product_ids
        urls = re.findall(r'^source:\s*"([^"]+)"', text, re.M)
        # 分享页中的poc_token等会话参数不作为台账资料。
        public_url = urls[0].split("?", 1)[0] if urls else None
        records.append({
            "id": f"LRJ-{index:03d}", "title": raw.stem,
            "raw_path": raw.relative_to(ROOT).as_posix(),
            "source_page": summary.relative_to(ROOT).as_posix(),
            "public_url": public_url, "primary_product_ids": products,
            "direction": direction, "primary_type": purpose,
            "secondary_tags": tags, "case": case,
            "commercial_evidence": "作者账号级100%商单自述；该篇付费主体未单核",
            "sponsor_id": None, "current_budget": None, "contact": None,
            "raw_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
        })
    assert {r["raw_path"] for r in records} == {p.relative_to(ROOT).as_posix() for p in raw_files}
    products = []
    for pid, name, directions, level, brand, tasks, own in PRODUCTS:
        products.append({
            "id": pid, "name": name, "directions": directions, "level": level,
            "brand_in_material": brand, "task_examples": tasks, "own_portfolio": own,
            "article_ids": [r["id"] for r in records if pid in r["primary_product_ids"]],
            "brand_verification": "据历史材料记录，未独立核实当前公司/商务主体",
            "official_contact": None, "budget_status": "未知",
        })
    data = {
        "updated": DATE, "coverage": "本地现有23篇；不是账号全部历史",
        "account_claim": {
            "source": "https://www.biji.com/note/share_note/7gvozqXeM4Lmb",
            "timestamp": "21:00", "claim": "作者自述自己的账号内容100%商单",
            "scope": "口述时点的账号级自述；不替代每篇付费主体与当前预算核对",
        },
        "classification_source": "录音41:44与44:00；主类型为综合归类，整活为表现标签",
        "content_types": ["实战型", "解决问题型", "整合型", "教程型", "观点型", "资讯型"],
        "products": products, "articles": records,
    }
    (OUT / "路人甲TM文章产品台账.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    raw_paths = ", ".join(r["raw_path"] for r in records)
    lines = ["---", "title: AI公众号产品选题与客户地图", "type: topic",
             "tags: [公众号, 路人甲TM, 产品池, 选题, 商务]", "status: 进行中",
             f"sources: [{raw_paths}]", f"created: {DATE}", f"updated: {DATE}", "---", "",
             "# AI公众号产品选题与客户地图", "", "## 目标与本批覆盖", "",
             "将对标文章中的产品、内容类型、案例任务和商务线索关联起来，支持选题与客户研究。本批覆盖本地现有23篇路人甲TM原文，22篇已有摘要，本次补齐1篇WorkBuddy小程序教程；不是账号全部历史。既有摘要复用，不重复新建。",
             "", "图像模型、设计工具是三个主方向的交叉能力；教育产品和公司分析保留为邻接样本，不据此扩大程序员拾梦的默认主题。产品有多个用途时允许跨方向标记，模型、应用、平台、插件和公司不混为同一层。",
             "", "## 商业依据与来源层次", "",
             "2026-10-16重新读取[路人甲分享录音](https://www.biji.com/note/share_note/7gvozqXeM4Lmb)转写。约21:00作者自述自己的内容100%商单，其他账号比例则是他的观察。这个自述应作为肯定的账号级商业依据，不能继续仅凭正文未标推广就忽略它。",
             "", "口述时点与后续文章日期不同，账号级自述不等于掌握每篇合同、实际付费方、预算和当前投放意愿。历史摘要的「具备推广特征、未单独核实付费」描述保留为当时的文本证据，与新增账号自述并列记录，不悄悄改成已知单篇客户。",
             "", "品牌归属列仅按材料记载，不宣称本轮已核实当前主体。台账中联系入口与预算未知就留空；需要联系时再核对官网、当前产品团队与商务入口，不从模型提供方、工具依赖或故事里的品牌自动推定甲方。",
             "", "## 原分享的类型与工作标签", "",
             "录音41:44提到实战型、解决问题型、整合型、教程型；44:00补充观点型与资讯型。作者当时主推实战、较少推荐观点和资讯，这是他的经验判断，不是对所有账号的永久规则。",
             "", "| 原分享类型 | 本表怎样识别 | 可交付的内容 |", "| --- | --- | --- |",
             "| 实战型 | 亲手做任务或作品，实测是其中一种 | 过程、成果、失败与适用判断 |",
             "| 解决问题型 | 围绕一个具体障碍验证办法 | 问题、调整、再次结果与限制 |",
             "| 整合型 | 本次暂归为资源、案例或工具整理；非原作者逐字定义 | 有筛选依据的清单与使用条件 |",
             "| 教程型 | 让目标读者跟着完成任务 | 起点、步骤、验收、常见问题 |",
             "| 观点型 | 解释产品或行业变化 | 证据、替代解释、判断边界 |",
             "| 资讯型 | 交代已核实的新变化 | 信息出处、变化与适用人群 |",
             "", "「整合」与「整活」是两回事。整活指有趣、反差或脑洞的任务/呈现方式，可以同时属于实战、实测、教程或解决问题。主类型用于查找，副标签用于表达形式；分类并非互斥，也不代表作者本人给每篇贴过这些标签。",
             "", "## 产品与客户研究入口", "",
             "| 产品/对象 | 方向 | 层级 | 材料中的归属线索 | 可研究任务 | 自己的样板 |",
             "| --- | --- | --- | --- | --- | --- |"]
    for p in products:
        lines.append(f'| {p["name"]} | {"、".join(p["directions"])} | {p["level"]} | {p["brand_in_material"]} | {p["task_examples"]} | {p["own_portfolio"]} |')
    lines += ["", "## 23篇文章的关联台账", "",
              "下表是材料研究目录，不是23笔已确认订单。每行对应真实原文和单篇摘要；具体产品版本、评论需求、实际付费方及当前预算仍按证据补充。",
              "", "| 编号 | 摘要入口 | 主产品/对象 | 主类型及副标签 | 核心案例 |",
              "| --- | --- | --- | --- | --- |"]
    by_id = {p["id"]: p for p in products}
    for r in records:
        source = Path(r["source_page"]).stem
        names = "、".join(by_id[pid]["name"] for pid in r["primary_product_ids"])
        lines.append(f'| {r["id"]} | [[sources/{source}]] | {names} | {r["primary_type"]}；{"、".join(r["secondary_tags"])} | {r["case"]} |')
    lines += ["", "## 用这份地图选题和找客户", "",
              "1. 先从产品池选符合读者与作者实操条件的产品；跨方向只是标签，不要求每个方向平均发文。",
              "2. 点开关联摘要和原文，记录原文回答的问题、成果、未覆盖的环节与证据。现有归档没有完整评论区，不编造评论需求。",
              "3. 将缺口转成自己的最小任务，选择主类型与副标签；无需每篇比原文更难，但需有自己的问题、表达和证据。",
              "4. 对接前补核产品官方身份、品牌与实际签约主体、当前需求和商务入口。历史产品曝光不等于当前预算。",
              "5. 用自己已完成的同类样板或具体案例计划沟通；不必为每个候选客户先免费写完长文。本文不授权自动发送消息。",
              "6. 逐条记录联系、需求、报价、对方表示将提报、确认、交付与回款的证据，不能把资料清单变成已成交记录。",
              "", "原文提到iPhone/苹果是配件设计的故事对象，不据此认定苹果付费；视频平台使用某模型，也不代表模型方是该文甲方；作者自建插件或Skill，应找清宿主产品和合作角色。",
              "", "## 维护方式", "",
              "机器可读的[文章产品台账](../../output/ai-wechat-methodology/路人甲TM文章产品台账.json)保留文章链接、原文路径、摘要、类型、案例、产品、账号级商业证据与待补字段。新增原文先检查是否重复，再创建对应摘要、补关联记录并重新生成本页；数据目录尚未提供账号全量历史，不能称为全量归档。",
              "", "## 相关页面", "",
              "- [[topics/路人甲TM文章写法拆解]]",
              "- [[topics/AI公众号商单商业闭环]]",
              "- [[topics/公众号商单实施复盘]]",
              "- [[topics/公众号文章切入点方法]]"]
    (ROOT / "wiki/topics/AI公众号产品选题与客户地图.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"已整理{len(records)}篇、{len(products)}个产品/品牌研究条目；没有登记已确认预算或私人联系信息。")


if __name__ == "__main__":
    main()
