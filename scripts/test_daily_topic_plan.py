"""核对个人工具状态、明日计划与模拟材料；不填造产品实测结果。"""
import json
import hashlib
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/ai-wechat-methodology"
PACK = OUT / "豆包电脑版明日选题包"


class DailyTopicPlanTest(unittest.TestCase):
    def test_doubao_is_available_by_user_report_without_invented_entitlements(self):
        pool = json.loads((OUT / "程序员拾梦可用工具池.json").read_text(encoding="utf-8"))
        product = next(p for p in pool["products"] if p["name"] == "豆包电脑版")
        self.assertEqual(product["membership_duration_user_reported"], "一个月")
        for key in ("membership_tier", "expires_at", "quota", "actual_sponsor"):
            self.assertIsNone(product[key])
        self.assertFalse(product["task_mode_verified"])
        self.assertFalse(product["public_offer_verified"])
        self.assertEqual(product["historical_article_ids"], ["LRJ60-24", "LRJ60-42", "LRJ60-52"])
        self.assertFalse(pool["availability"]["automatic_publication_authorized"])
        self.assertEqual(pool["availability"]["target_publish_date"], "2026-10-17")

    def test_historical_dataset_is_not_recounted_as_new_sponsorship(self):
        historical = json.loads((OUT / "路人甲TM六十篇拆解台账.json").read_text(encoding="utf-8"))
        self.assertEqual(len(historical["articles"]), 60)
        p = next(p for p in historical["products"] if p["name"] == "豆包工作")
        self.assertEqual(len(p["primary_article_ids"]), 3)
        chart = (OUT / "路人甲TM选题与客户速查表.md").read_text(encoding="utf-8")
        for text in ("豆包电脑版", "3篇", "映射待实操核对", "不改变60篇历史统计"):
            self.assertIn(text, chart)

    def test_simulated_materials_have_consistent_attendance_and_budget(self):
        text = (PACK / "模拟资料/报名与预算.md").read_text(encoding="utf-8")
        rows = re.findall(r"\| P\d+ \| ([^|]+) \|", text)
        self.assertEqual(len(rows), 12)
        self.assertEqual(sum(s.strip() == "确认参加" for s in rows), 8)
        self.assertEqual(sum(s.strip() == "候补" for s in rows), 2)
        self.assertEqual(sum(s.strip() == "已取消" for s in rows), 2)
        costs = re.findall(r"\| ([^|]+) \| (\d+) \| (\d+) \| (\d+) \| ([^|]+) \|", text)
        self.assertEqual(len(costs), 4)
        for _, quantity, price, subtotal, _ in costs:
            self.assertEqual(int(quantity) * int(price), int(subtotal))
        total = sum(int(r[3]) for r in costs)
        self.assertEqual(total, 860)
        self.assertEqual(total - 120, 740)
        for p in (PACK / "模拟资料").glob("*.md"):
            self.assertIn("模拟", p.read_text(encoding="utf-8"))
        answer = (PACK / "核对参考.md").read_text(encoding="utf-8")
        for expected in ("740", "860", "140", "260", "15:00—18:00", "安禾", "已付金额都是0"):
            self.assertIn(expected, answer)

    def test_task_prompts_do_not_feed_reference_answers_or_fake_performance(self):
        text = (PACK / "给豆包的提示词.md").read_text(encoding="utf-8")
        first = text.split("## 第一段", 1)[1].split("## 第二段", 1)[0]
        self.assertNotIn("740", first)
        self.assertNotIn("860", first)
        for expected in ("不要上传", "模拟数据", "不要修改上传的源文件", "不要对外发布", "实际看到"):
            self.assertIn(expected, text)
        record = (PACK / "实测记录.md").read_text(encoding="utf-8")
        self.assertIn("状态：待实操", record)
        self.assertGreater(record.count("待填写"), 15)

    def test_plan_files_timing_and_publication_ownership_are_clear(self):
        plan = (PACK / "选题与实操安排.md").read_text(encoding="utf-8")
        for expected in ("target_publish_date: 2026-10-17", "21:00 Asia/Shanghai", "待实操",
                         "今晚", "明天上午", "作者人工", "不是产品速度承诺", "不创建自动任务"):
            self.assertIn(expected, plan)
        for filename in ("模拟资料/活动原计划.md", "模拟资料/报名与预算.md", "模拟资料/群聊补充.md",
                         "给豆包的提示词.md", "核对参考.md", "实测记录.md"):
            self.assertTrue((PACK / filename).is_file())

    def test_knowledge_entries_and_counts_are_linked(self):
        index = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
        for link in ("[[entities/豆包电脑版]]", "[[topics/公众号每日选题决策]]"):
            self.assertIn(link, index)
        count = sum(p.name not in ("index.md", "log.md") for p in (ROOT / "wiki").rglob("*.md"))
        self.assertEqual(int(re.search(r"知识页：(\d+) 页", index).group(1)), count)
        product = (ROOT / "wiki/entities/豆包电脑版.md").read_text(encoding="utf-8")
        self.assertIn("历史", product)
        self.assertIn("不凭名称直接判断", product)
        self.assertIn("用户在2026-10-16确认", product)

    def test_user_rejection_demotes_old_plan_without_inventing_new_results(self):
        decision = (ROOT / "wiki/topics/公众号每日选题决策.md").read_text(encoding="utf-8")
        plan = (PACK / "选题与实操安排.md").read_text(encoding="utf-8")
        self.assertIn("具体题目尚未确认，均未实操", decision)
        self.assertIn("不继续作为明日主推", decision)
        self.assertIn("本方案已降为备选", plan)
        self.assertIn("没有核实各平台2026双11档期", decision)
        self.assertIn("https://www.doubao.com/legal/DoubaoAgentModeNotice", decision)
        target = PACK / "../../../wiki/topics/公众号每日选题决策.md"
        self.assertTrue(target.resolve().is_file())
        for name in ("消费者：", "商家：", "互动作品："):
            self.assertIn(name, decision)
        self.assertIn("待填写", (PACK / "实测记录.md").read_text(encoding="utf-8"))

    def test_double11_plan_preserves_supplied_sources_and_resolves_local_links(self):
        sources = {
            "raw/article/管三/没花一分钱！一张实拍图，「豆包工作」帮我做出主图、详情页和3条带货视频.md":
                "58a0db0743c9b08dbac656956f2b23a4a460303e5834e5edf52231b80c8e89bd",
            "raw/article/lurenjiaTM/实测OiiOii最新Skill，这套电商组合堪称双十一王炸！.md":
                "87a1a719f3db6a4a45b51d8ee05e92990bdac3b9467445366668424453febeff",
            "raw/article/lurenjiaTM/真正的双11来了！天猫预售居然免定金！.md":
                "3e85ce75877576f08d4eb30b535f886663aa8ddce5289bb16c1dac367f235c14",
        }
        plan_path = OUT / "豆包双11商品素材实操方案.md"
        text = plan_path.read_text(encoding="utf-8")
        for path, expected in sources.items():
            # Windows编辑器及Git可能转换换行，仍严格验证原文内容。
            body = (ROOT / path).read_bytes().replace(b"\r\n", b"\n")
            self.assertEqual(hashlib.sha256(body).hexdigest(), expected)
            self.assertIn("../../" + path, text)
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if not target.startswith(("https://", "http://")):
                self.assertTrue((plan_path.parent / target).resolve().is_file(), target)

    def test_product_video_is_recorded_while_presenter_video_remains_pending(self):
        decision = (ROOT / "wiki/topics/公众号每日选题决策.md").read_text(encoding="utf-8")
        current = decision.split("## 2026-10-17确认方向", 1)[1].split("## 旧候选", 1)[0]
        self.assertIn("产品宣传视频已生成两轮并收到饱满版MP4，人物带货视频待实操", current)
        self.assertIn("不是用户的实测记录", current)
        product = (ROOT / "wiki/entities/豆包电脑版.md").read_text(encoding="utf-8")
        self.assertIn("## 当前研究问题（2026-10-17）", product)
        self.assertNotIn("当前商品待选", product)
        plan = (OUT / "豆包双11商品素材实操方案.md").read_text(encoding="utf-8")
        self.assertIn("待实操", plan)
        self.assertIn("未观看链接视频", plan)
        self.assertIn("本轮实际执行的键盘图片提示词", plan)
        rows = re.findall(r"\| (带货视频) \| ([^|]+) \| ([^|]+) \|", plan)
        self.assertEqual(len(rows), 1)
        for _, status, result in rows:
            self.assertIn(status.strip(), ("待确认", "待实操"))
            self.assertEqual(result.strip(), "待填写")

    def test_selected_keyboard_input_is_archived_without_claiming_generated_output(self):
        photo = OUT / "豆包双11键盘素材/键盘原始实拍.jpg"
        self.assertEqual(hashlib.sha256(photo.read_bytes()).hexdigest(),
                         "3a876561840f202776841051cacd903b1df46d6b6c09bf063dcf51b53053820b")
        plan = (OUT / "豆包双11商品素材实操方案.md").read_text(encoding="utf-8")
        self.assertIn("不是豆包生成结果", plan)
        self.assertIn("商品已选，图片及视频入口已见", plan)
        first_prompt = plan.split("本轮实际执行的键盘图片提示词", 1)[1].split("## 首轮真实结果", 1)[0]
        self.assertNotIn("【粘贴", first_prompt)
        self.assertIn("保持商品外观一致", first_prompt)
        self.assertIn("不要编造", first_prompt)
        self.assertIn("不将其描述为该键盘的真实声音", plan)

    def test_keyboard_image_request_is_brief_and_keeps_requested_deliverables(self):
        plan = (OUT / "豆包双11商品素材实操方案.md").read_text(encoding="utf-8")
        prompt = plan.split("本轮实际执行的键盘图片提示词", 1)[1].split("## 首轮真实结果", 1)[0]
        body = re.search(r"```text\n(.*?)\n```", prompt, re.DOTALL).group(1)
        for deliverable in ("商品标题", "1张主图", "详情页文案", "6屏详情图"):
            self.assertIn(deliverable, body)
        self.assertLess(len(body), 240)
        self.assertNotRegex(body, r"详情第\d屏|我是一个淘宝卖家")
        self.assertIn("没有提供的规格、功能和优惠信息不要编造", body)
        self.assertNotIn("请制作以下3张图", prompt)
        decision = (ROOT / "wiki/topics/公众号每日选题决策.md").read_text(encoding="utf-8")
        self.assertIn("1张主图＋6屏详情图，共7张独立图片", decision)

    def test_image_runs_have_six_evidence_files_and_no_invented_cost_or_video(self):
        evidence_dir = OUT / "豆包双11键盘素材"
        record_path = evidence_dir / "首轮商品图实测记录.md"
        record = record_path.read_text(encoding="utf-8")
        screenshots = re.findall(r"!\[[^]]*\]\(([^)]+\.png)\)", record)
        self.assertEqual(len(set(screenshots)), 6)
        for filename in screenshots:
            self.assertTrue((evidence_dir / filename).read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))
        for expected in ("创意设计", "4分18秒", "3.77%", "右下角", "右上角",
                         "金属旋钮", "未取得7张独立原尺寸图片", "现金费用", "均待实操"):
            self.assertIn(expected, record)
        plan = (OUT / "豆包双11商品素材实操方案.md").read_text(encoding="utf-8")
        self.assertIn("| 商品图 | 已执行，原尺寸细节待核 |", plan)
        self.assertIn("商品外观以原始实拍图为准", plan)

    def test_proportion_feedback_and_accepted_repair_preserve_observation_limits(self):
        record = (OUT / "豆包双11键盘素材/首轮商品图实测记录.md").read_text(encoding="utf-8")
        self.assertIn("好像不对，细看显得太宽了", record)
        self.assertIn("主图不计入", record)
        self.assertIn("未测量原尺寸成品", record)
        self.assertIn("用户随后实际发送", record)
        self.assertIn("只修改这两张，其他图片不要改", record)
        self.assertIn("1分3秒", record)
        self.assertIn("1.08%", record)
        self.assertIn("这版修改好了", record)
        self.assertIn("未取得前后所有独立文件进行比较", record)
        for path in (OUT / "豆包双11商品素材实操方案.md",
                     ROOT / "wiki/topics/公众号每日选题决策.md"):
            text = path.read_text(encoding="utf-8")
            self.assertIn("返修已执行", text)
            self.assertNotIn("返修待执行", text)

    def test_video_file_is_preserved_and_inspection_scope_is_explicit(self):
        folder = OUT / "豆包双11键盘素材"
        video = folder / "产品宣传视频-饱满版.mp4"
        self.assertEqual(hashlib.sha256(video.read_bytes()).hexdigest(),
                         "4544ebe1e47436c91267f24a1cae9b5080044fb3ec2dfceba2c58e6cbd8bb200")
        meta = json.loads((folder / "宣传视频媒体信息.json").read_text(encoding="utf-8"))
        self.assertEqual((meta["width"], meta["height"]), (720, 1280))
        self.assertAlmostEqual(meta["duration_seconds"], 15.071995, places=5)
        self.assertEqual(len(meta["sampled_frame_times"]), 17)
        record_path = folder / "产品宣传视频实测记录.md"
        record = record_path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", record):
            self.assertTrue((folder / target).resolve().is_file(), target)
        for observation in ("4分29秒", "3分59秒", "104.14%", "104.17%",
                            "未独立试听", "画面太空了", "品牌附近字母有变形", "人物出镜带货视频仍待执行"):
            self.assertIn(observation, record)
        plan = (OUT / "豆包双11商品素材实操方案.md").read_text(encoding="utf-8")
        self.assertIn("| 产品宣传视频 | 已生成及重做，继续修改中 |", plan)
        self.assertIn("不要编造使用经历、规格和优惠", plan)

    def test_new_text_and_voice_revision_is_proposed_without_claiming_execution(self):
        record = (OUT / "豆包双11键盘素材/产品宣传视频实测记录.md").read_text(encoding="utf-8")
        section = record.split("## 开头字幕与旁白修改建议（待执行）", 1)[1].split("## 下一步", 1)[0]
        self.assertIn("尚未收到用户实际发送截图或第三轮成片", section)
        prompt = re.search(r"```text\n(.*?)\n```", section, re.DOTALL).group(1)
        self.assertLess(len(prompt), 200)
        self.assertIn("开头字幕改成「让桌面亮起来」", prompt)
        self.assertIn("不要念品牌名，也不要加品牌字幕", prompt)
        self.assertIn("其他镜头和音乐保持不变", prompt)
        self.assertNotIn("98", prompt)
        self.assertNotIn("AULA", prompt)


if __name__ == "__main__":
    unittest.main()
