"""离线核对本次研究的来源、费用算式与写作边界，不调用收费接口。"""
import json
from decimal import Decimal
from pathlib import Path

root = Path(__file__).resolve().parent
blog = json.loads((root / 'hunyuan-official-blog.json').read_text(encoding='utf-8'))
work = json.loads((root / 'workbuddy-article.json').read_text(encoding='utf-8'))
report = (root / 'README.md').read_text(encoding='utf-8')
checks = {}
checks['no_signed_media_keys'] = all(term not in (root / name).read_text(encoding='utf-8') for name in ['hunyuan-official-blog.json', 'workbuddy-article.json'] for term in ['q-ak=', 'q-signature=', 'AKID'])
checks['official_source'] = blog['lang'] == 'zh' and blog['customUrl'] == 'hy4-flash'
checks['workbuddy_source'] = work['code'] == 200 and work['account'] == '腾讯WorkBuddy' and work['published'].startswith('2026-11-16')
checks['specs_from_source'] = all(s in blog['content'] for s in ['224B', '64B', '12B', '1M', '150 tps', '50%', '1/20', '259'])
compact = ''.join(work['text'].split())
checks['free_deadline_from_source'] = '11月16日-11月30日23:59' in compact
checks['daily_limit_from_source'] = all(s in compact for s in ['每日免费额度', '消耗积分继续使用', '生成图片与视频', '按照正常规则产生积分消耗'])
checks['discount_arithmetic'] = [str(Decimal(s) * Decimal('0.5')) for s in ['0.5', '2', '0.02']] == ['0.25', '1.0', '0.010']
checks['both_deadlines_distinguished'] = all(s in report for s in ['2026-11-30 12:00:00', '2026-11-30 23:59'])
checks['benchmark_qualifiers'] = all(s in report for s in ['max档位、忙时价格', 'preview，不是Hy4正式版', '内部用户', '不能写成全面追平Claude'])
checks['unmeasured_state'] = all(s in report for s in ['作者尚未实测', '待试', '需求为策划假设', '不能写成权重已经发布'])
benchmark = json.loads((root / 'benchmark-article.json').read_text(encoding='utf-8'))
cases = (root / 'case-recommendations.md').read_text(encoding='utf-8')
checks['benchmark_identity'] = benchmark['code'] == 200 and benchmark['account'] == '刘聪NLP' and benchmark['source'].endswith('JmgWnEMgQETC03jnxmxwcg')
checks['benchmark_reading_scope'] = all(s in benchmark['text'] for s in ['密度', '凸透镜', '键盘', '反复横跳']) and '未看图片、视频、工程和账单' in cases
repo = root.parents[2]
checks['case_sources_and_anchors'] = all(anchor in (repo / 'wiki/sources' / name).read_text(encoding='utf-8') for name, anchor in [('GPT-6-Astra连测文章拆解.md', '果冻'), ('小林豆包重力实验室文章拆解.md', '三星球'), ('全新Qoder实测文章拆解.md', '真实照片')])
checks['case_status_and_acceptance'] = cases.count('### ') == 3 and cases.count('- 验收：') == 3 and cases.count('- 首轮与退出：') == 3 and '均为待实操' in cases and '推导改编' in cases
result = {'passed': all(checks.values()), 'checks': checks, 'scope': '资料与研究稿的离线一致性检查，不验证模型效果、每日额度数值或实际计费'}
(root / 'verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=True))
assert result['passed']
