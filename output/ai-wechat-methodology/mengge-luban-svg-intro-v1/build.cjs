/**
 * 程序员梦哥 · 《GPT Image 叒叒叒更新了，我用它手搓了一套鲁班皮肤》专属片头动画构建器
 * 技术路线：对齐摸鱼小李纯内嵌 SVG + SMIL 声明式动画架构（零 <text>、零 <image>、零 <script>、零外部依赖）
 * 同时输出同时间轴 Canvas + FFmpeg 高清 GIF 兜底版、6 张关键帧快照与交互式定格预览页 preview.html。
 */
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '../../..');
const OUT = __dirname;
const CANVAS_DIR = path.resolve(OUT, '../程序员拾梦闯关片头五案-v1');
const canvasModule = require.resolve('@napi-rs/canvas', { paths: [CANVAS_DIR] });
const { createCanvas, loadImage, GlobalFonts, convertSVGTextToPath } = require(canvasModule);

GlobalFonts.registerFromPath('C:/Windows/Fonts/msyhbd.ttc', 'MengBold');
GlobalFonts.registerFromPath('C:/Windows/Fonts/msyh.ttc', 'MengRegular');

const W = 1246;
const H = 220;
const DUR = 8; // 8.0s 主循环周期
const FPS = 20;

// ─── 工具函数：文字转纯矢量 <path>（可返回合并串，也可返回按字拆分的独立 <path> 数组） ───
function escapeXml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function textToPathList(text, font, size, x, y, fill) {
  const raw = convertSVGTextToPath(
    `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}"><text x="${x}" y="${y}" font-family="${font}" font-size="${size}" fill="${fill}">${escapeXml(text)}</text></svg>`
  ).toString();
  const matches = raw.match(/<path\b[^>]*\/?>/g) || [];
  return matches.map(p => {
    const compact = p.replace(/-?\d+\.\d{2,}/g, m => String(Math.round(Number(m) * 10) / 10));
    return compact.endsWith('/>') ? compact : compact.replace(/>$/, '/>');
  });
}
function textToPaths(text, font, size, x, y, fill) {
  return textToPathList(text, font, size, x, y, fill).join('');
}

// ─── 工具函数：将既有像素梦哥立绘 (sprite-idle.png) 提取为 100% 纯矢量像素 <path> ───
async function vectorizeMengGeSprite() {
  const spritePath = path.join(CANVAS_DIR, 'sprite-idle.png');
  const img = await loadImage(spritePath);
  // 先裁出非透明边界：原图 (254, 504)，有效像素区约 (27, 36) -> (227, 468)
  const sw = 38;
  const sh = 68;
  const tmp = createCanvas(sw, sh);
  const tctx = tmp.getContext('2d');
  tctx.imageSmoothingEnabled = false;
  tctx.drawImage(img, 24, 34, 206, 436, 0, 0, sw, sh);
  const data = tctx.getImageData(0, 0, sw, sh).data;

  // 量化颜色保证路径紧凑干净
  function quantHex(r, g, b) {
    const qr = Math.min(255, Math.round(r / 24) * 24);
    const qg = Math.min(255, Math.round(g / 24) * 24);
    const qb = Math.min(255, Math.round(b / 24) * 24);
    return (
      '#' +
      [qr, qg, qb]
        .map(v => v.toString(16).padStart(2, '0'))
        .join('')
        .toUpperCase()
    );
  }

  const headRuns = {}; // y < 44 (头+上身，参与呼吸起伏)
  const legRuns = {};  // y >= 44 (腿脚，稳立地面)

  for (let y = 0; y < sh; y++) {
    const bucket = y < 44 ? headRuns : legRuns;
    let x = 0;
    while (x < sw) {
      const idx = (y * sw + x) * 4;
      if (data[idx + 3] < 128) {
        x++;
        continue;
      }
      const color = quantHex(data[idx], data[idx + 1], data[idx + 2]);
      const x0 = x;
      while (x < sw) {
        const i2 = (y * sw + x) * 4;
        if (data[i2 + 3] < 128 || quantHex(data[i2], data[i2 + 1], data[i2 + 2]) !== color) break;
        x++;
      }
      const len = x - x0;
      if (!bucket[color]) bucket[color] = [];
      bucket[color].push(`M${x0} ${y}h${len}v1h-${len}z`);
    }
  }

  const headPaths = Object.entries(headRuns)
    .map(([c, d]) => `<path d="${d.join('')}" fill="${c}"/>`)
    .join('');
  const legPaths = Object.entries(legRuns)
    .map(([c, d]) => `<path d="${d.join('')}" fill="${c}"/>`)
    .join('');

  return { headPaths, legPaths, sw, sh };
}

// ─── SMIL 辅助构造函数 ───
function smilOpacity(values, keyTimes, dur = '8s') {
  return `<animate attributeName="opacity" values="${values}" keyTimes="${keyTimes}" dur="${dur}" repeatCount="indefinite"/>`;
}

function smilSplineTransform(type, values, keyTimes, spline = '0.22 1 0.36 1', dur = '8s') {
  const segs = keyTimes.split(';').length - 1;
  const splines = Array(segs).fill(spline).join(';');
  return `<animateTransform attributeName="transform" type="${type}" values="${values}" keyTimes="${keyTimes}" dur="${dur}" repeatCount="indefinite" calcMode="spline" keySplines="${splines}"/>`;
}

// ─── 构建纯 SVG + SMIL 源码 ───
async function buildSVG() {
  const sprite = await vectorizeMengGeSprite();

  // 1. 背景底座与左侧常驻品牌像素梦哥区
  const bgAndAvatar = `
  <defs>
    <linearGradient id="bg-card" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F7FAFF"/>
      <stop offset="55%" stop-color="#F0F7FF"/>
      <stop offset="100%" stop-color="#FFF5F9"/>
    </linearGradient>
    <linearGradient id="ocean-bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0EA5E9"/>
      <stop offset="50%" stop-color="#3B82F6"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>
    <linearGradient id="whale-blue" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <linearGradient id="whale-pink" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FF7EB3"/>
      <stop offset="100%" stop-color="#E11D48"/>
    </linearGradient>
  </defs>

  <!-- 画布外框与柔和浅底 -->
  <rect x="0" y="0" width="1246" height="220" rx="22" fill="#FFFFFF"/>
  <rect x="8" y="8" width="1230" height="204" rx="18" fill="url(#bg-card)" stroke="#DCE8F8" stroke-width="2"/>
  <!-- 顶部装饰流光条 -->
  <rect x="28" y="8" width="1190" height="4" rx="2" fill="url(#ocean-bar)" opacity="0.85"/>

  <!-- 背景装饰网格点阵 -->
  <g fill="#CBD5E1" opacity="0.45">
    <rect x="230" y="28" width="3" height="3"/><rect x="270" y="28" width="3" height="3"/><rect x="310" y="28" width="3" height="3"/>
    <rect x="1140" y="186" width="3" height="3"/><rect x="1170" y="186" width="3" height="3"/><rect x="1200" y="186" width="3" height="3"/>
  </g>

  <!-- 左侧常驻：像素梦哥角色舞台 (x: 26..206) -->
  <g id="brand-character-stage">
    <!-- 脚下发光底座 -->
    <ellipse cx="116" cy="188" rx="48" ry="10" fill="#DBEAFE">
      <animate attributeName="rx" values="48;44;48" keyTimes="0;0.5;1" dur="2.4s" repeatCount="indefinite"/>
    </ellipse>
    <!-- 像素梦哥本体：38x68 放大 2.35 倍至约 89x160，置于 (72, 26) -->
    <g transform="translate(72 26) scale(2.35)">
      ${sprite.legPaths}
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0;0 -1.1;0 0" keyTimes="0;0.5;1" dur="2.4s" repeatCount="indefinite" calcMode="spline" keySplines="0.42 0 0.58 1;0.42 0 0.58 1"/>
        ${sprite.headPaths}
        <!-- 眼镜高光闪烁 -->
        <rect x="14" y="16" width="3" height="2" fill="#FFFFFF" opacity="0.85">
          <animate attributeName="opacity" values="0.2;0.95;0.2" keyTimes="0;0.45;1" dur="3.2s" repeatCount="indefinite"/>
        </rect>
        <rect x="22" y="16" width="3" height="2" fill="#FFFFFF" opacity="0.85">
          <animate attributeName="opacity" values="0.2;0.95;0.2" keyTimes="0;0.45;1" dur="3.2s" repeatCount="indefinite"/>
        </rect>
      </g>
    </g>
    <!-- 梦哥左侧悬浮终端角标 >_ -->
    <g transform="translate(26 42)">
      <animateTransform attributeName="transform" type="translate" values="26 42;26 37;26 42" keyTimes="0;0.5;1" dur="3.0s" repeatCount="indefinite" calcMode="spline" keySplines="0.42 0 0.58 1;0.42 0 0.58 1"/>
      <rect x="0" y="0" width="38" height="26" rx="7" fill="#1E293B"/>
      <path d="M9 8L15 13L9 18" stroke="#38BDF8" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      <rect x="18" y="16" width="9" height="2.4" fill="#38BDF8">
        <animate attributeName="opacity" values="1;0.15;1" keyTimes="0;0.5;1" dur="1.1s" repeatCount="indefinite"/>
      </rect>
    </g>
    <!-- 梦哥右侧灵感小鲸鱼气泡（在进入主题阶段 1.8s~7.2s 弹出点赞） -->
    <g opacity="0">
      ${smilOpacity('0;0;1;1;0;0', '0;0.21;0.25;0.88;0.92;1')}
      <g transform="translate(154 24)">
        ${smilSplineTransform('scale', '0.2;0.2;1.15;1;1;0.2', '0;0.21;0.25;0.28;0.88;1')}
        <rect x="0" y="0" width="46" height="28" rx="10" fill="#0284C7"/>
        <path d="M8 28L14 22L18 28Z" fill="#0284C7"/>
        <!-- 迷你像素小鲸鱼图标 -->
        <path d="M12 16C12 11 17 8 24 8C30 8 34 11 35 15L40 12V19L35 17C33 20 28 21 22 21H14C12.5 21 12 19 12 16Z" fill="#E0F2FE"/>
        <circle cx="18" cy="14" r="1.5" fill="#0369A1"/>
      </g>
    </g>
    <!-- 分隔虚线 -->
    <path d="M214 28V192" stroke="#CBD5E1" stroke-width="1.5" stroke-dasharray="5 5"/>
  </g>
  `;

  // 2. 第一幕（0.0s ~ 1.76s & 7.25s ~ 8.0s）：品牌大字亮相 + 逐字向中心坍缩为像素粒子
  const brandTitleChars = textToPathList('程序员梦哥', 'MengBold', 56, 268, 102, '#0F172A');
  const brandSubChars = textToPathList('折腾 AI，分享实用玩法', 'MengBold', 33, 270, 158, '#0284C7');
  const badgeText = textToPaths('GPT Image 2.6 · 手搓鲁班皮肤篇', 'MengBold', 18, 635, 92, '#0369A1');

  // 让每个汉字在 0.14(1.12s) -> 0.22(1.76s) 向画布中心 (660, 112) 坍缩并缩小
  const charCollapseSvg = [...brandTitleChars, ...brandSubChars]
    .map((p, i) => {
      const delay = (i * 0.0035).toFixed(4);
      const t1 = (0.145 + Number(delay)).toFixed(4);
      const t2 = (0.195 + Number(delay)).toFixed(4);
      const t3 = (0.235 + Number(delay)).toFixed(4);
      const dx = Math.round(140 - (i % 7) * 28);
      const dy = Math.round((i < 5 ? 18 : -16) + ((i % 3) - 1) * 8);
      return `
      <g>
        ${smilSplineTransform(
          'translate',
          `0 0;0 0;${dx} ${dy};${dx} ${dy};0 0;0 0`,
          `0;${t1};${t3};0.90;0.955;1`,
          '0.77 0 0.175 1'
        )}
        <g opacity="1">
          ${smilOpacity(`1;1;0;0;1;1`, `0;${t1};${t2};0.915;0.96;1`)}
          ${p}
        </g>
      </g>`;
    })
    .join('');

  // 36 枚海洋/珊瑚像素方块粒子：在 1.15s~2.0s 之间从文字区炸开并汇聚到中央工作台，7.1s~7.6s 再次散开回流
  const particleColors = ['#0284C7', '#38BDF8', '#0EA5E9', '#FF6B9D', '#6366F1', '#22C55E'];
  const particles = [];
  for (let i = 0; i < 36; i++) {
    const col = i % 12;
    const row = Math.floor(i / 12);
    const sx = 280 + col * 52 + (row % 2) * 18;
    const sy = 64 + row * 42;
    const mx = sx + ((i % 5) - 2) * 34;
    const my = sy + ((i % 3) - 1) * 28;
    const tx = 580 + ((i % 7) - 3) * 42;
    const ty = 110 + ((i % 3) - 1) * 24;
    const size = 7 + (i % 3) * 3;
    const color = particleColors[i % particleColors.length];
    particles.push(`
    <g opacity="0">
      ${smilOpacity('0;0;1;1;0;0;1;0;0', '0;0.145;0.17;0.22;0.255;0.885;0.91;0.955;1')}
      <g>
        ${smilSplineTransform(
          'translate',
          `${sx} ${sy};${sx} ${sy};${mx} ${my};${tx} ${ty};${tx} ${ty};${sx} ${sy};${sx} ${sy}`,
          '0;0.145;0.19;0.25;0.89;0.95;1',
          '0.77 0 0.175 1'
        )}
        <rect x="0" y="0" width="${size}" height="${size}" rx="2" fill="${color}"/>
      </g>
    </g>`);
  }

  const act0BrandLayer = `
  <!-- 第一幕：品牌口号与标签 -->
  <g id="act0-brand-intro">
    ${charCollapseSvg}
    <!-- 右侧副胶囊标签 -->
    <g opacity="1">
      ${smilOpacity('1;1;0;0;1;1', '0;0.145;0.195;0.915;0.96;1')}
      <rect x="615" y="64" width="330" height="40" rx="20" fill="#E0F2FE" stroke="#7DD3FC" stroke-width="1.5"/>
      ${badgeText}
      <!-- 装饰像素方块簇 -->
      <rect x="975" y="72" width="14" height="14" rx="3" fill="#0284C7"/>
      <rect x="997" y="66" width="10" height="10" rx="2" fill="#38BDF8"/>
      <rect x="995" y="84" width="16" height="16" rx="3" fill="#FF6B9D"/>
      <rect x="270" y="174" width="460" height="6" rx="3" fill="url(#ocean-bar)" opacity="0.65"/>
    </g>
    <!-- 像素粒子层 -->
    <g id="transition-particles">
      ${particles.join('')}
    </g>
  </g>
  `;

  // 3. 第二幕（1.76s ~ 7.24s，即 keyTimes 0.22 ~ 0.905）：
  // 主题故事：「大肥鱼灵感卡插入 → 鲸鱼帽鲁班立绘 → 选框局部改粉帽 → 鲸鱼水炮开火炸出三张成果卡」
  const labels = {
    consoleHeader: textToPaths('GPT Image 2.6 · 鲁班皮肤手搓工坊', 'MengBold', 15, 456, 40, '#0F172A'),
    step1Tag: textToPaths('01 设定生成', 'MengBold', 12, 686, 39, '#0369A1'),
    step2Tag: textToPaths('02 局部改色', 'MengBold', 12, 778, 39, '#BE185D'),
    step3Tag: textToPaths('03 全套动效', 'MengBold', 12, 870, 39, '#15803D'),
    fishCardTitle: textToPaths('大肥鱼灵感', 'MengBold', 15, 258, 72, '#0369A1'),
    fishCardSub: textToPaths('海洋主题 CP', 'MengRegular', 12, 260, 156, '#0284C7'),
    promptText: textToPaths('Prompt: 鲸鱼帽 + 透明水舱 + 泡泡鲸鱼炮', 'MengBold', 12, 464, 192, '#334155'),
    editChipText: textToPaths('只改粉色鲸鱼帽 · 保持脸型与武器不变', 'MengBold', 12, 464, 68, '#BE185D'),
    card1Title: textToPaths('四技能攻击 GIF', 'MengBold', 14, 984, 52, '#0369A1'),
    card1Sub: textToPaths('小鲸鱼空投水弹 & 泡泡', 'MengRegular', 11, 984, 70, '#475569'),
    card2Title: textToPaths('CAD 机械拆解图', 'MengBold', 14, 984, 114, '#1E40AF'),
    card2Sub: textToPaths('外壳 / 水舱 / 鱼鳍编号对照', 'MengRegular', 11, 984, 132, '#475569'),
    card3Title: textToPaths('12 张游戏表情包', 'MengBold', 14, 984, 174, '#BE185D'),
    card3Sub: textToPaths('「这把看我的！」坏笑动图', 'MengBold', 11, 984, 192, '#E11D48'),
  };

  const act1TopicScene = `
  <!-- 第二幕：当篇主题演示舞台 (1.76s ~ 7.24s) -->
  <g id="topic-scene-root" opacity="0">
    ${smilOpacity('0;0;1;1;0;0', '0;0.215;0.255;0.875;0.91;1')}

    <!-- (A) 左侧输入卡：DeepSeek 大肥鱼灵感卡带（在 1.85s 飞入插槽并触发机身回弹） -->
    <g id="deepseek-fish-cartridge">
      ${smilSplineTransform(
        'translate',
        '-40 -30;-40 -30;0 0;6 0;0 0;0 0',
        '0;0.22;0.275;0.295;0.315;1',
        '0.22 1 0.36 1'
      )}
      <rect x="236" y="46" width="164" height="128" rx="14" fill="#FFFFFF" stroke="#38BDF8" stroke-width="2.5"/>
      <rect x="246" y="54" width="144" height="24" rx="6" fill="#E0F2FE"/>
      ${labels.fishCardTitle}
      <!-- 大肥鱼矢量卡通插画 -->
      <g transform="translate(318 114)">
        <animateTransform attributeName="transform" type="translate" values="318 114;318 109;318 114" keyTimes="0;0.5;1" dur="1.8s" repeatCount="indefinite"/>
        <!-- 鱼身 -->
        <ellipse cx="0" cy="0" rx="34" ry="20" fill="#0284C7"/>
        <path d="M-28 4C-14 16 14 16 28 3C18 19 -14 20 -28 4Z" fill="#E0F2FE"/>
        <!-- 鱼尾与背鳍 -->
        <path d="M-32 0L-46 -13L-42 0L-46 13Z" fill="#38BDF8"/>
        <path d="M-4 -19C4 -28 14 -26 16 -17Z" fill="#0369A1"/>
        <!-- 呆萌大眼与微笑 -->
        <circle cx="16" cy="-4" r="5" fill="#FFFFFF"/>
        <circle cx="18" cy="-4" r="2.5" fill="#0F172A"/>
        <path d="M12 6Q20 11 26 5" stroke="#FFFFFF" stroke-width="2" fill="none" stroke-linecap="round"/>
        <!-- 喷水小气泡 -->
        <circle cx="38" cy="-12" r="3.5" fill="#7DD3FC"/>
        <circle cx="45" cy="-20" r="2.2" fill="#BAE6FD"/>
      </g>
      ${labels.fishCardSub}
      <!-- 右侧连接插头与能量脉冲线 -->
      <rect x="400" y="98" width="26" height="22" rx="4" fill="#0284C7"/>
      <path d="M404 109H424" stroke="#7DD3FC" stroke-width="3" stroke-linecap="round"/>
    </g>

    <!-- (B) 中央主舞台：GPT Image 2.6 角色创作舱（受卡带插入 & 水炮发射产生两次关联震动回弹） -->
    <g id="image26-workbench">
      ${smilSplineTransform(
        'translate',
        '0 0;0 0;4 3;0 0;0 0;0 3;0 0;0 0;-5 0;0 0;0 0',
        '0;0.27;0.29;0.315;0.43;0.45;0.475;0.63;0.65;0.68;1',
        '0.22 1 0.36 1'
      )}
      <!-- 创作舱外框 -->
      <rect x="424" y="20" width="516" height="182" rx="16" fill="#FFFFFF" stroke="#93C5FD" stroke-width="2.5"/>
      <!-- 顶部状态栏 -->
      <rect x="426" y="22" width="512" height="26" rx="14" fill="#F1F5F9"/>
      <circle cx="442" cy="35" r="5" fill="#38BDF8"/>
      ${labels.consoleHeader}

      <!-- 三枚阶段指示灯胶囊（随剧情依次弹跳点亮） -->
      <!-- 灯 1: 01 设定生成 (2.2s 点亮) -->
      <g>
        <rect x="676" y="25" width="84" height="20" rx="10" fill="#E0F2FE" stroke="#38BDF8" stroke-width="1.2"/>
        ${labels.step1Tag}
      </g>
      <!-- 灯 2: 02 局部改色 (3.4s 弹跳高亮珊瑚粉) -->
      <g opacity="0.35">
        ${smilOpacity('0.35;0.35;1;1;0.35', '0;0.41;0.44;0.88;1')}
        <rect x="768" y="25" width="84" height="20" rx="10" fill="#FCE7F3" stroke="#F43F5E" stroke-width="1.5"/>
        ${labels.step2Tag}
      </g>
      <!-- 灯 3: 03 全套动效 (5.0s 弹跳高亮翠绿) -->
      <g opacity="0.35">
        ${smilOpacity('0.35;0.35;1;1;0.35', '0;0.62;0.65;0.88;1')}
        <rect x="860" y="25" width="72" height="20" rx="10" fill="#DCFCE7" stroke="#22C55E" stroke-width="1.5"/>
        ${labels.step3Tag}
      </g>

      <!-- 创作舱内部网格画布 -->
      <rect x="442" y="54" width="480" height="122" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>

      <!-- ══ 鲁班七号 · 海洋大肥鱼皮肤 Q版立绘 (中心坐标 x=635, y=126) ══ -->
      <g id="luban-ocean-character" opacity="0">
        ${smilOpacity('0;0;1;1;0', '0;0.27;0.31;0.88;1')}
        <g transform="translate(620 124)">
          ${smilSplineTransform('scale', '0.4;0.4;1.08;1;1', '0;0.27;0.31;0.34;1')}

          <!-- 1. 背后透明水舱背包 (含水面与浮动气泡) -->
          <rect x="-46" y="-22" width="28" height="40" rx="8" fill="#E0F2FE" stroke="#0284C7" stroke-width="2"/>
          <path d="M-44 0Q-32 -4 -20 0V14C-20 16 -22 17 -24 17H-40C-42 17 -44 16 -44 14Z" fill="#38BDF8" opacity="0.65"/>
          <circle cx="-36" cy="8" r="2.5" fill="#FFFFFF">
            <animate attributeName="cy" values="10;-8;10" dur="1.6s" repeatCount="indefinite"/>
          </circle>
          <circle cx="-28" cy="2" r="1.8" fill="#FFFFFF">
            <animate attributeName="cy" values="6;-12;6" dur="2.1s" repeatCount="indefinite"/>
          </circle>

          <!-- 2. 鲁班身体与鱼鳍战靴 -->
          <rect x="-20" y="4" width="40" height="28" rx="9" fill="#0284C7"/>
          <rect x="-12" y="6" width="24" height="22" rx="6" fill="#F8FAFC"/>
          <!-- 胸前水滴挂饰 -->
          <path d="M0 11L-5 19A5 5 0 1 0 5 19Z" fill="#38BDF8"/>
          <!-- 双腿与两侧小鱼鳍鞋 -->
          <rect x="-16" y="30" width="11" height="14" rx="4" fill="#1E3A8A"/>
          <rect x="5" y="30" width="11" height="14" rx="4" fill="#1E3A8A"/>
          <path d="M-16 36L-24 32L-22 41Z" fill="#38BDF8"/>
          <path d="M16 36L24 32L22 41Z" fill="#38BDF8"/>

          <!-- 3. 鲁班头部与标志性“欠揍坏笑” -->
          <rect x="-24" y="-30" width="48" height="36" rx="14" fill="#FDE68A" stroke="#D97706" stroke-width="1.5"/>
          <!-- 棕色刘海与耳机 -->
          <path d="M-22 -22C-14 -30 14 -30 22 -22L18 -14C8 -20 -8 -20 -18 -14Z" fill="#78350F"/>
          <rect x="-28" y="-18" width="6" height="14" rx="3" fill="#0284C7"/>
          <rect x="22" y="-18" width="6" height="14" rx="3" fill="#0284C7"/>
          <!-- 灵动大眼睛 -->
          <ellipse cx="-10" cy="-12" rx="4.2" ry="4.8" fill="#0F172A"/>
          <ellipse cx="10" cy="-12" rx="4.2" ry="4.8" fill="#0F172A"/>
          <circle cx="-11" cy="-14" r="1.5" fill="#FFFFFF"/>
          <circle cx="9" cy="-14" r="1.5" fill="#FFFFFF"/>
          <!-- 坏笑嘴角 -->
          <path d="M-9 -2Q2 6 12 -4" stroke="#B45309" stroke-width="2.4" fill="none" stroke-linecap="round"/>
          <path d="M-6 -1Q2 4 9 -3Z" fill="#FFFFFF"/>

          <!-- 4. 头顶鲸鱼帽（核心看点：3.5s 局部改色从海蓝 -> 珊瑚粉，造型不变！） -->
          <!-- (4a) 初始海蓝色鲸鱼帽 -->
          <g id="whale-hat-blue" opacity="1">
            ${smilOpacity('1;1;0;0;1', '0;0.445;0.475;0.90;1')}
            <path d="M-28 -26C-28 -48 24 -48 28 -26C14 -31 -14 -31 -28 -26Z" fill="url(#whale-blue)" stroke="#0369A1" stroke-width="1.8"/>
            <!-- 鲸鱼帽尾巴与眼睛 -->
            <path d="M26 -32L37 -41L35 -31L39 -24L27 -27Z" fill="#38BDF8"/>
            <circle cx="-12" cy="-35" r="2.6" fill="#FFFFFF"/>
            <circle cx="-12" cy="-35" r="1.3" fill="#0F172A"/>
            <!-- 帽顶喷水珠 -->
            <circle cx="-2" cy="-50" r="2.8" fill="#38BDF8">
              <animate attributeName="cy" values="-48;-56;-48" dur="1.2s" repeatCount="indefinite"/>
            </circle>
            <circle cx="5" cy="-54" r="2" fill="#7DD3FC">
              <animate attributeName="cy" values="-52;-60;-52" dur="1.2s" repeatCount="indefinite"/>
            </circle>
          </g>

          <!-- (4b) 局部编辑后的珊瑚粉鲸鱼帽（在 0.455 = 3.64s 无缝接替） -->
          <g id="whale-hat-pink" opacity="0">
            ${smilOpacity('0;0;1;1;0', '0;0.445;0.475;0.89;1')}
            <path d="M-28 -26C-28 -48 24 -48 28 -26C14 -31 -14 -31 -28 -26Z" fill="url(#whale-pink)" stroke="#BE185D" stroke-width="1.8"/>
            <path d="M26 -32L37 -41L35 -31L39 -24L27 -27Z" fill="#FDA4AF"/>
            <circle cx="-12" cy="-35" r="2.6" fill="#FFFFFF"/>
            <circle cx="-12" cy="-35" r="1.3" fill="#881337"/>
            <circle cx="-2" cy="-50" r="2.8" fill="#FB7185">
              <animate attributeName="cy" values="-48;-56;-48" dur="1.2s" repeatCount="indefinite"/>
            </circle>
            <circle cx="5" cy="-54" r="2" fill="#FDA4AF">
              <animate attributeName="cy" values="-52;-60;-52" dur="1.2s" repeatCount="indefinite"/>
            </circle>
          </g>

          <!-- 5. 手持泡泡鲸鱼水炮（在 5.05s = keyTime 0.63 后坐蓄力并发射水弹） -->
          <g id="whale-cannon">
            ${smilSplineTransform(
              'translate',
              '0 0;0 0;-7 0;2 0;0 0;0 0',
              '0;0.62;0.645;0.67;0.70;1',
              '0.22 1 0.36 1'
            )}
            <!-- 鲸鱼炮身 -->
            <rect x="16" y="-2" width="44" height="22" rx="10" fill="#0284C7" stroke="#0369A1" stroke-width="1.8"/>
            <!-- 透明水舱视窗 -->
            <rect x="26" y="2" width="18" height="12" rx="5" fill="#E0F2FE"/>
            <path d="M27 9H43V13H27Z" fill="#38BDF8"/>
            <!-- 鲸鱼炮口与尾鳍 -->
            <rect x="56" y="2" width="9" height="14" rx="3" fill="#38BDF8"/>
            <path d="M18 -2L12 -10L24 -2Z" fill="#38BDF8"/>
          </g>
        </g>
      </g>

      <!-- ══ 动作 ②：局部改色虚线选框 + 粉色扫描光条 (3.35s ~ 4.95s, keyTimes 0.415 ~ 0.615) ══ -->
      <g id="local-edit-selection" opacity="0">
        ${smilOpacity('0;0;1;1;0;0', '0;0.405;0.435;0.58;0.615;1')}
        <!-- 顶部局部改色提示条 -->
        <rect x="454" y="54" width="256" height="20" rx="6" fill="#FCE7F3" stroke="#F472B6" stroke-width="1"/>
        ${labels.editChipText}
        <!-- 锁定鲸鱼帽的虚线框 -->
        <g>
          ${smilSplineTransform('scale', '1.25;1.25;1;1', '0;0.405;0.44;1')}
          <rect x="582" y="64" width="82" height="36" rx="4" fill="#F43F5E" fill-opacity="0.10" stroke="#E11D48" stroke-width="2" stroke-dasharray="4 3"/>
          <!-- 四角控制锚点 -->
          <rect x="579" y="61" width="6" height="6" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.5"/>
          <rect x="661" y="61" width="6" height="6" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.5"/>
          <rect x="579" y="97" width="6" height="6" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.5"/>
          <rect x="661" y="97" width="6" height="6" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.5"/>
        </g>
        <!-- 色彩替换激光扫描线 -->
        <rect x="584" y="66" width="78" height="3" fill="#FB7185">
          <animate attributeName="y" values="66;66;96;96" keyTimes="0;0.43;0.485;1" dur="8s" repeatCount="indefinite"/>
        </rect>
        <!-- 蓝->粉调色板胶囊 -->
        <g transform="translate(674 68)">
          <rect x="0" y="0" width="68" height="24" rx="12" fill="#FFFFFF" stroke="#F43F5E" stroke-width="1.5"/>
          <circle cx="15" cy="12" r="7" fill="#0284C7"/>
          <path d="M27 12H39M36 8L40 12L36 16" stroke="#64748B" stroke-width="1.8" fill="none" stroke-linecap="round"/>
          <circle cx="53" cy="12" r="7" fill="#EC4899"/>
        </g>
      </g>

      <!-- ══ 动作 ③：鲸鱼水炮开火！发射小鲸鱼飞弹与泡泡束 (5.0s ~ 7.1s, keyTimes 0.625 ~ 0.885) ══ -->
      <g id="whale-cannon-projectile" opacity="0">
        ${smilOpacity('0;0;1;1;0;0', '0;0.625;0.64;0.86;0.89;1')}
        <!-- 炮口水花闪光 -->
        <circle cx="690" cy="132" r="10" fill="#7DD3FC" opacity="0.75">
          <animate attributeName="r" values="4;16;6" keyTimes="0;0.5;1" dur="0.8s" repeatCount="indefinite"/>
        </circle>
        <!-- 飞射的小鲸鱼水弹与泡泡轨迹 -->
        <g>
          ${smilSplineTransform(
            'translate',
            '690 124;690 124;865 104;865 104',
            '0;0.625;0.685;1',
            '0.22 1 0.36 1'
          )}
          <path d="M0 8C0 1 8 -4 18 -4C27 -4 32 1 34 6L42 1V14L34 10C31 15 24 16 14 16H4C1 16 0 13 0 8Z" fill="#0EA5E9" stroke="#0284C7" stroke-width="1.5"/>
          <circle cx="24" cy="4" r="2" fill="#FFFFFF"/>
          <circle cx="-12" cy="10" r="5" fill="#7DD3FC" opacity="0.8"/>
          <circle cx="-26" cy="14" r="3.5" fill="#BAE6FD" opacity="0.7"/>
        </g>
        <!-- 展开向右侧三张成果卡的三叉能量流线 -->
        <path d="M700 132C780 132 840 60 946 56" stroke="#38BDF8" stroke-width="2.5" stroke-dasharray="6 4" fill="none"/>
        <path d="M700 132C790 132 850 118 946 118" stroke="#6366F1" stroke-width="2.5" stroke-dasharray="6 4" fill="none"/>
        <path d="M700 132C780 132 840 176 946 180" stroke="#EC4899" stroke-width="2.5" stroke-dasharray="6 4" fill="none"/>
      </g>

      <!-- 底部提示词铭牌 -->
      <rect x="450" y="179" width="464" height="18" rx="5" fill="#E2E8F0"/>
      ${labels.promptText}
    </g>

    <!-- (C) 右侧交付区：三张全套皮肤成果卡（5.2s = keyTime 0.65 依次带弹性回弹展开 + 大对勾） -->
    <!-- 成果卡 1：四技能攻击动效 GIF -->
    <g id="output-card-1" opacity="0">
      ${smilOpacity('0;0;1;1;0', '0;0.635;0.665;0.88;1')}
      <g>
        ${smilSplineTransform('translate', '40 0;40 0;-4 0;0 0;0 0', '0;0.635;0.67;0.695;1')}
        <rect x="952" y="24" width="268" height="54" rx="12" fill="#FFFFFF" stroke="#38BDF8" stroke-width="2"/>
        <rect x="960" y="34" width="18" height="34" rx="6" fill="#0284C7"/>
        ${labels.card1Title}
        ${labels.card1Sub}
        <!-- GIF 徽章 -->
        <rect x="1166" y="36" width="42" height="22" rx="6" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.2"/>
        <path d="M1176 51V43H1183M1187 43V51M1192 51V43H1198" stroke="#0369A1" stroke-width="1.8" fill="none" stroke-linecap="round"/>
      </g>
    </g>

    <!-- 成果卡 2：鲸鱼炮 CAD 机械拆解图 -->
    <g id="output-card-2" opacity="0">
      ${smilOpacity('0;0;1;1;0', '0;0.655;0.685;0.88;1')}
      <g>
        ${smilSplineTransform('translate', '40 0;40 0;-4 0;0 0;0 0', '0;0.655;0.69;0.715;1')}
        <rect x="952" y="86" width="268" height="54" rx="12" fill="#FFFFFF" stroke="#6366F1" stroke-width="2"/>
        <rect x="960" y="96" width="18" height="34" rx="6" fill="#4F46E5"/>
        ${labels.card2Title}
        ${labels.card2Sub}
        <!-- 迷你爆炸拆解线框示意 -->
        <g transform="translate(1164 98)" stroke="#4F46E5" stroke-width="1.4" fill="#EEF2FF">
          <rect x="0" y="2" width="14" height="10" rx="2"/>
          <rect x="18" y="6" width="12" height="12" rx="2"/>
          <rect x="34" y="4" width="10" height="8" rx="2"/>
          <path d="M14 7H18M30 10H34" stroke-dasharray="2 2"/>
        </g>
      </g>
    </g>

    <!-- 成果卡 3：12 张游戏表情包 + 完成大对勾徽章 -->
    <g id="output-card-3" opacity="0">
      ${smilOpacity('0;0;1;1;0', '0;0.675;0.705;0.88;1')}
      <g>
        ${smilSplineTransform('translate', '40 0;40 0;-4 0;0 0;0 0', '0;0.675;0.71;0.735;1')}
        <rect x="952" y="148" width="268" height="54" rx="12" fill="#FFFFFF" stroke="#F43F5E" stroke-width="2"/>
        <rect x="960" y="158" width="18" height="34" rx="6" fill="#E11D48"/>
        ${labels.card3Title}
        ${labels.card3Sub}
        <!-- 翠绿完成大对勾弹跳盖章 -->
        <g transform="translate(1188 175)">
          ${smilSplineTransform('scale', '0;0;1.35;0.92;1;1', '0;0.69;0.725;0.745;0.765;1')}
          <circle cx="0" cy="0" r="16" fill="#22C55E"/>
          <path d="M-7 0L-2 5L8 -5" stroke="#FFFFFF" stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
      </g>
    </g>
  </g>
  `;

  const ariaLabel =
    '程序员梦哥：折腾 AI，分享实用玩法；像素文字坍缩为海洋粒子；GPT Image 2.6 手搓鲁班七号大肥鱼皮肤全流程：1. 插入大肥鱼灵感卡生成蓝色鲸鱼帽鲁班立绘；2. 虚线选框锁定帽子局部改色为珊瑚粉；3. 鲸鱼水炮开火展开四技能动效 GIF、CAD 机械拆解图与 12 张游戏表情包，弹出绿色完成对勾';

  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" preserveAspectRatio="xMidYMid meet" role="img" aria-label="${ariaLabel}" style="display:block;width:100%;height:auto;max-width:${W}px;margin:0 auto;background:transparent;">${bgAndAvatar}${act0BrandLayer}${act1TopicScene}</svg>`;
}

// ─── 同步 Canvas 渲染器：用于生成关键帧 PNG 与 GIF 兜底文件 ───
function easeInOut(u) {
  u = Math.max(0, Math.min(1, u));
  return u * u * (3 - 2 * u);
}

function easeOutBack(u) {
  u = Math.max(0, Math.min(1, u));
  const c1 = 1.70158;
  const c3 = c1 + 1;
  return 1 + c3 * Math.pow(u - 1, 3) + c1 * Math.pow(u - 1, 2);
}

async function renderCanvasFrames() {
  const spriteImg = await loadImage(path.join(CANVAS_DIR, 'sprite-idle.png'));
  const canvas = createCanvas(W, H);
  const ctx = canvas.getContext('2d');

  function drawFrame(t) {
    ctx.fillStyle = '#FFFFFF';
    ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = '#F4F8FF';
    ctx.strokeStyle = '#DCE8F8';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(8, 8, W - 16, H - 16, 18);
    ctx.fill();
    ctx.stroke();
    // 顶部彩条
    const topBar = ctx.createLinearGradient(28, 0, W - 28, 0);
    topBar.addColorStop(0, '#0EA5E9');
    topBar.addColorStop(0.5, '#3B82F6');
    topBar.addColorStop(1, '#EC4899');
    ctx.fillStyle = topBar;
    ctx.beginPath();
    ctx.roundRect(28, 8, W - 56, 4, 2);
    ctx.fill();

    // 左侧常驻像素梦哥
    const bob = Math.round(Math.sin((t / 2.4) * Math.PI * 2) * 2);
    ctx.fillStyle = '#DBEAFE';
    ctx.beginPath();
    ctx.ellipse(116, 188, 46, 9, 0, 0, Math.PI * 2);
    ctx.fill();

    ctx.save();
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(spriteImg, 24, 34, 206, 436, 72, 26 + bob, 89, 160);
    ctx.restore();

    // >_ 终端小徽章
    ctx.fillStyle = '#1E293B';
    ctx.beginPath();
    ctx.roundRect(26, 42 - bob, 38, 26, 7);
    ctx.fill();
    ctx.fillStyle = '#38BDF8';
    ctx.font = 'bold 14px MengBold';
    ctx.fillText('>_', 34, 60 - bob);
    // 竖向分隔虚线
    ctx.save();
    ctx.setLineDash([5, 5]);
    ctx.strokeStyle = '#CBD5E1';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(214, 28);
    ctx.lineTo(214, 192);
    ctx.stroke();
    ctx.restore();

    // 第一幕：品牌文字 (0 ~ 1.45s 及 7.35 ~ 8.0s)
    let brandAlpha = 0;
    let collapseP = 0;
    if (t < 1.2) {
      brandAlpha = 1;
    } else if (t < 1.75) {
      collapseP = easeInOut((t - 1.2) / 0.55);
      brandAlpha = 1 - collapseP;
    } else if (t > 7.3) {
      const rp = easeInOut((t - 7.3) / 0.65);
      brandAlpha = rp;
      collapseP = 1 - rp;
    }

    if (brandAlpha > 0.01) {
      ctx.save();
      ctx.globalAlpha = brandAlpha;
      const cx = 660;
      const cy = 112;
      const scale = 1 - collapseP * 0.65;
      ctx.translate(cx * (1 - scale), cy * (1 - scale));
      ctx.scale(scale, scale);

      ctx.fillStyle = '#0F172A';
      ctx.font = 'bold 56px MengBold';
      ctx.fillText('程序员梦哥', 268, 102);

      ctx.fillStyle = '#0284C7';
      ctx.font = 'bold 33px MengBold';
      ctx.fillText('折腾 AI，分享实用玩法', 270, 158);

      ctx.fillStyle = '#E0F2FE';
      ctx.strokeStyle = '#7DD3FC';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.roundRect(615, 64, 330, 40, 20);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = '#0369A1';
      ctx.font = 'bold 18px MengBold';
      ctx.fillText('GPT Image 2.6 · 手搓鲁班皮肤篇', 635, 91);
      ctx.restore();
    }

    // 过渡像素粒子 (1.15s ~ 2.0s 及 7.1s ~ 7.65s)
    const inBurst = t >= 1.15 && t <= 2.05;
    const outBurst = t >= 7.1 && t <= 7.65;
    if (inBurst || outBurst) {
      const u = inBurst ? easeInOut((t - 1.15) / 0.9) : 1 - easeInOut((t - 7.1) / 0.55);
      const pColors = ['#0284C7', '#38BDF8', '#0EA5E9', '#FF6B9D', '#6366F1', '#22C55E'];
      for (let i = 0; i < 36; i++) {
        const col = i % 12;
        const row = Math.floor(i / 12);
        const sx = 280 + col * 52;
        const sy = 64 + row * 42;
        const tx = 580 + ((i % 7) - 3) * 42;
        const ty = 110 + ((i % 3) - 1) * 24;
        const px = sx + (tx - sx) * u;
        const py = sy + (ty - sy) * u + Math.sin(u * Math.PI) * ((i % 2 === 0 ? 1 : -1) * 18);
        const sz = 7 + (i % 3) * 3;
        ctx.fillStyle = pColors[i % pColors.length];
        ctx.fillRect(px, py, sz, sz);
      }
    }

    // 第二幕：主题舞台 (1.76s ~ 7.25s)
    if (t >= 1.72 && t <= 7.3) {
      let sceneAlpha = 1;
      if (t < 2.05) sceneAlpha = easeInOut((t - 1.72) / 0.33);
      else if (t > 6.95) sceneAlpha = 1 - easeInOut((t - 6.95) / 0.35);

      ctx.save();
      ctx.globalAlpha = sceneAlpha;

      // (A) 左侧大肥鱼灵感卡
      const cardP = easeOutBack(Math.min(1, Math.max(0, (t - 1.8) / 0.45)));
      const cardX = 236 - (1 - cardP) * 36;
      ctx.fillStyle = '#FFFFFF';
      ctx.strokeStyle = '#38BDF8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.roundRect(cardX, 46, 164, 128, 14);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = '#E0F2FE';
      ctx.beginPath();
      ctx.roundRect(cardX + 10, 54, 144, 24, 6);
      ctx.fill();
      ctx.fillStyle = '#0369A1';
      ctx.font = 'bold 15px MengBold';
      ctx.fillText('大肥鱼灵感', cardX + 22, 72);

      // 大肥鱼简图
      ctx.fillStyle = '#0284C7';
      ctx.beginPath();
      ctx.ellipse(cardX + 82, 114, 34, 20, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#FFFFFF';
      ctx.beginPath();
      ctx.arc(cardX + 98, 110, 5, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#0F172A';
      ctx.beginPath();
      ctx.arc(cardX + 100, 110, 2.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#0284C7';
      ctx.font = '12px MengRegular';
      ctx.fillText('海洋主题 CP', cardX + 24, 156);

      // (B) 中央创作舱
      const recoilX = t >= 5.0 && t <= 5.35 ? -4 * Math.sin(((t - 5.0) / 0.35) * Math.PI) : 0;
      const recoilY = t >= 2.15 && t <= 2.45 ? 3 * Math.sin(((t - 2.15) / 0.3) * Math.PI) : 0;
      ctx.save();
      ctx.translate(recoilX, recoilY);

      ctx.fillStyle = '#FFFFFF';
      ctx.strokeStyle = '#93C5FD';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.roundRect(424, 20, 516, 182, 16);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = '#F1F5F9';
      ctx.beginPath();
      ctx.roundRect(426, 22, 512, 26, 14);
      ctx.fill();
      ctx.fillStyle = '#0F172A';
      ctx.font = 'bold 15px MengBold';
      ctx.fillText('GPT Image 2.6 · 鲁班皮肤手搓工坊', 456, 40);

      // 三枚阶段胶囊灯
      const isPinkHat = t >= 3.6;
      const isFired = t >= 5.05;
      // 01
      ctx.fillStyle = '#E0F2FE';
      ctx.beginPath();
      ctx.roundRect(676, 25, 84, 20, 10);
      ctx.fill();
      ctx.fillStyle = '#0369A1';
      ctx.font = 'bold 12px MengBold';
      ctx.fillText('01 设定生成', 686, 39);
      // 02
      ctx.save();
      ctx.globalAlpha = t >= 3.35 ? 1 : 0.35;
      ctx.fillStyle = '#FCE7F3';
      ctx.beginPath();
      ctx.roundRect(768, 25, 84, 20, 10);
      ctx.fill();
      ctx.fillStyle = '#BE185D';
      ctx.fillText('02 局部改色', 778, 39);
      ctx.restore();
      // 03
      ctx.save();
      ctx.globalAlpha = isFired ? 1 : 0.35;
      ctx.fillStyle = '#DCFCE7';
      ctx.beginPath();
      ctx.roundRect(860, 25, 72, 20, 10);
      ctx.fill();
      ctx.fillStyle = '#15803D';
      ctx.fillText('03 全套动效', 870, 39);
      ctx.restore();

      // 内部画布与鲁班角色
      ctx.fillStyle = '#F8FAFC';
      ctx.strokeStyle = '#E2E8F0';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.roundRect(442, 54, 480, 122, 10);
      ctx.fill();
      ctx.stroke();

      if (t >= 2.15) {
        const lubanScale = easeOutBack(Math.min(1, (t - 2.15) / 0.35));
        ctx.save();
        ctx.translate(620, 124);
        ctx.scale(lubanScale, lubanScale);

        // 水舱背包
        ctx.fillStyle = '#E0F2FE';
        ctx.strokeStyle = '#0284C7';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.roundRect(-46, -22, 28, 40, 8);
        ctx.fill();
        ctx.stroke();

        // 身体
        ctx.fillStyle = '#0284C7';
        ctx.beginPath();
        ctx.roundRect(-20, 4, 40, 28, 9);
        ctx.fill();

        // 脸
        ctx.fillStyle = '#FDE68A';
        ctx.strokeStyle = '#D97706';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.roundRect(-24, -30, 48, 36, 14);
        ctx.fill();
        ctx.stroke();

        // 眼睛
        ctx.fillStyle = '#0F172A';
        ctx.beginPath();
        ctx.arc(-10, -12, 4.2, 0, Math.PI * 2);
        ctx.arc(10, -12, 4.2, 0, Math.PI * 2);
        ctx.fill();

        // 鲸鱼帽（3.6s 局部由海蓝变珊瑚粉）
        ctx.fillStyle = isPinkHat ? '#EC4899' : '#0284C7';
        ctx.beginPath();
        ctx.ellipse(0, -34, 28, 12, 0, Math.PI, 0);
        ctx.fill();

        // 鲸鱼水炮
        ctx.fillStyle = '#0284C7';
        ctx.beginPath();
        ctx.roundRect(16, -2, 44, 22, 10);
        ctx.fill();
        ctx.fillStyle = '#E0F2FE';
        ctx.beginPath();
        ctx.roundRect(26, 2, 18, 12, 5);
        ctx.fill();

        ctx.restore();
      }

      // 动作 ②：局部改色选框 (3.3s ~ 4.85s)
      if (t >= 3.3 && t <= 4.85) {
        ctx.save();
        ctx.fillStyle = '#FCE7F3';
        ctx.beginPath();
        ctx.roundRect(454, 54, 256, 20, 6);
        ctx.fill();
        ctx.fillStyle = '#BE185D';
        ctx.font = 'bold 12px MengBold';
        ctx.fillText('只改粉色鲸鱼帽 · 保持脸型与武器不变', 464, 68);

        ctx.strokeStyle = '#E11D48';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 3]);
        ctx.strokeRect(582, 64, 82, 36);
        ctx.restore();
      }

      // 动作 ③：鲸鱼水炮发射水弹 (5.0s ~ 7.1s)
      if (t >= 5.0) {
        const flyP = Math.min(1, (t - 5.0) / 0.45);
        const bx = 690 + flyP * 175;
        const by = 124 - flyP * 20;
        ctx.fillStyle = '#0EA5E9';
        ctx.beginPath();
        ctx.ellipse(bx, by, 18, 9, 0, 0, Math.PI * 2);
        ctx.fill();
      }

      // 底部提示词
      ctx.fillStyle = '#E2E8F0';
      ctx.beginPath();
      ctx.roundRect(450, 179, 464, 18, 5);
      ctx.fill();
      ctx.fillStyle = '#334155';
      ctx.font = 'bold 12px MengBold';
      ctx.fillText('Prompt: 鲸鱼帽 + 透明水舱 + 泡泡鲸鱼炮', 464, 192);
      ctx.restore();

      // (C) 右侧三张成果卡 (5.1s 起依次展开)
      const cards = [
        { y: 24, stroke: '#38BDF8', bar: '#0284C7', title: '四技能攻击 GIF', sub: '小鲸鱼空投水弹 & 泡泡', t0: 5.08 },
        { y: 86, stroke: '#6366F1', bar: '#4F46E5', title: 'CAD 机械拆解图', sub: '外壳 / 水舱 / 鱼鳍编号对照', t0: 5.24 },
        { y: 148, stroke: '#F43F5E', bar: '#E11D48', title: '12 张游戏表情包', sub: '「这把看我的！」坏笑动图', t0: 5.40 },
      ];
      cards.forEach((c, idx) => {
        if (t >= c.t0) {
          const cp = easeOutBack(Math.min(1, (t - c.t0) / 0.35));
          const cx = 952 + (1 - cp) * 36;
          ctx.fillStyle = '#FFFFFF';
          ctx.strokeStyle = c.stroke;
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.roundRect(cx, c.y, 268, 54, 12);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = c.bar;
          ctx.beginPath();
          ctx.roundRect(cx + 8, c.y + 10, 18, 34, 6);
          ctx.fill();

          ctx.fillStyle = '#0F172A';
          ctx.font = 'bold 14px MengBold';
          ctx.fillText(c.title, cx + 34, c.y + 28);
          ctx.fillStyle = '#475569';
          ctx.font = '11px MengRegular';
          ctx.fillText(c.sub, cx + 34, c.y + 46);

          if (idx === 2 && t >= 5.55) {
            ctx.fillStyle = '#22C55E';
            ctx.beginPath();
            ctx.arc(cx + 236, c.y + 27, 15, 0, Math.PI * 2);
            ctx.fill();
            ctx.strokeStyle = '#FFFFFF';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(cx + 229, c.y + 27);
            ctx.lineTo(cx + 234, c.y + 32);
            ctx.lineTo(cx + 244, c.y + 22);
            ctx.stroke();
          }
        }
      });

      ctx.restore();
    }

    return canvas.toBuffer('image/png');
  }

  const frameDir = path.join(OUT, '_frames');
  fs.mkdirSync(frameDir, { recursive: true });
  const totalFrames = DUR * FPS;
  for (let i = 0; i < totalFrames; i++) {
    const t = i === totalFrames - 1 ? 0 : i / FPS;
    fs.writeFileSync(path.join(frameDir, `${String(i).padStart(4, '0')}.png`), drawFrame(t));
  }

  // 保存 6 张关键帧 PNG
  const keyframes = [
    { name: 'keyframe-0.5s-brand.png', t: 0.5 },
    { name: 'keyframe-1.6s-particles.png', t: 1.6 },
    { name: 'keyframe-2.6s-blue-luban.png', t: 2.6 },
    { name: 'keyframe-4.2s-pink-edit.png', t: 4.2 },
    { name: 'keyframe-5.3s-cannon-fire.png', t: 5.3 },
    { name: 'keyframe-6.4s-full-deliverables.png', t: 6.4 },
  ];
  for (const kf of keyframes) {
    fs.writeFileSync(path.join(OUT, kf.name), drawFrame(kf.t));
  }

  // 合成 GIF 兜底文件
  const ff = spawnSync(
    'ffmpeg',
    [
      '-y',
      '-v',
      'error',
      '-framerate',
      String(FPS),
      '-i',
      path.join(frameDir, '%04d.png'),
      '-filter_complex',
      '[0:v]split[a][b];[a]palettegen=max_colors=128:stats_mode=full[p];[b][p]paletteuse=dither=none:diff_mode=rectangle',
      '-loop',
      '0',
      path.join(OUT, 'intro.gif'),
    ],
    { encoding: 'utf8' }
  );
  if (ff.status !== 0) {
    throw new Error(`FFmpeg GIF encode failed: ${ff.stderr}`);
  }
  // 清理临时序列帧以保持工作区整洁
  fs.rmSync(frameDir, { recursive: true, force: true });
}

function buildPreviewHTML(svg) {
  return `<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>程序员梦哥 · 《手搓鲁班大肥鱼皮肤》纯 SVG+SMIL 片头动画工作台</title>
<style>
  *{box-sizing:border-box}
  body{margin:0;background:#0F172A;color:#E2E8F0;font:15px/1.75 "Microsoft YaHei",system-ui,sans-serif}
  main{max-width:1120px;margin:28px auto;padding:28px 32px;background:#1E293B;border-radius:20px;border:1px solid #334155;box-shadow:0 20px 50px rgba(0,0,0,.4)}
  h1{font-size:24px;margin:0 0 6px;color:#F8FAFC}
  h2{font-size:17px;margin:28px 0 12px;color:#38BDF8;border-left:4px solid #38BDF8;padding-left:10px}
  p.desc{color:#94A3B8;margin:0 0 18px;font-size:14px}
  .stage{background:#FFFFFF;padding:18px;border-radius:16px;box-shadow:inset 0 0 0 1px #E2E8F0}
  .toolbar{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 6px}
  button{cursor:pointer;padding:8px 14px;border-radius:10px;border:1px solid #475569;background:#0F172A;color:#E2E8F0;font:600 13px "Microsoft YaHei",sans-serif;transition:.15s}
  button:hover{background:#0284C7;border-color:#38BDF8;color:#FFFFFF}
  button.primary{background:#0284C7;border-color:#38BDF8;color:#FFFFFF}
  .grid{display:grid;grid-template-columns:1fr 395px;gap:24px;align-items:start;margin-top:16px}
  @media(max-width:920px){.grid{grid-template-columns:1fr}}
  .phone{width:375px;background:#FFFFFF;color:#1E293B;border-radius:24px;overflow:hidden;border:6px solid #334155;margin:0 auto;box-shadow:0 12px 30px rgba(0,0,0,.35)}
  .phone-bar{background:#F8FAFC;padding:10px 16px;font-size:13px;font-weight:700;color:#0F172A;border-bottom:1px solid #E2E8F0;text-align:center}
  .phone-body{padding:14px 16px 22px;font-size:15px;line-height:1.8;color:#334155}
  .phone-body h3{font-size:19px;line-height:1.45;color:#0F172A;margin:12px 0 8px}
  .phone-body .meta{font-size:12px;color:#64748B;margin-bottom:12px}
  .phone-body p{margin:10px 0}
  .phone-body mark{background:#FEF08A;padding:1px 4px;border-radius:4px}
  .spec-list{background:#0F172A;border:1px solid #334155;border-radius:14px;padding:16px 20px;font-size:13.5px;color:#CBD5E1}
  .spec-list li{margin:8px 0}
  .spec-list code{background:#1E293B;color:#38BDF8;padding:2px 6px;border-radius:5px}
  .keyframes{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:12px;margin-top:12px}
  .kf-card{background:#0F172A;border:1px solid #334155;border-radius:12px;padding:10px}
  .kf-card span{display:block;font-size:12px;color:#94A3B8;margin-bottom:6px}
  .kf-card img{width:100%;height:auto;border-radius:8px;display:block}
</style>
</head>
<body>
<main>
  <h1>程序员梦哥 · 《GPT Image 2.6 手搓鲁班皮肤》纯 SVG+SMIL 定制片头</h1>
  <p class="desc">采用对标账号「摸鱼小李」同款纯内嵌 SVG + SMIL 声明式矢量动画技术（画布 1246×220，8秒循环，零 &lt;text&gt;、零 &lt;image&gt;、零 &lt;script&gt;、零外部字体或图片依赖）。</p>

  <div class="stage" id="main-svg-stage">
    ${svg}
  </div>

  <div class="toolbar">
    <button class="primary" onclick="playAll()">▶ 连续播放 (8s 循环)</button>
    <button onclick="freezeAt(0.5)">⏸ 0.5s 品牌亮相</button>
    <button onclick="freezeAt(1.6)">⏸ 1.6s 文字坍缩粒子</button>
    <button onclick="freezeAt(2.6)">⏸ 2.6s 大肥鱼生成蓝帽鲁班</button>
    <button onclick="freezeAt(4.2)">⏸ 4.2s 选框局部改粉色鲸鱼帽</button>
    <button onclick="freezeAt(5.3)">⏸ 5.3s 鲸鱼水炮后坐开火</button>
    <button onclick="freezeAt(6.4)">⏸ 6.4s 动效/拆解/表情包三卡齐开</button>
  </div>

  <div class="grid">
    <div>
      <h2>一、五幕分镜与摸鱼小李同源技法核对</h2>
      <ul class="spec-list">
        <li><strong>纯矢量像素梦哥（零 Base64 位图）</strong>：左侧「程序员梦哥」由既有像素立绘提取为纯 <code>&lt;path&gt;</code> 像素网格，上身与眼镜高光按 <code>2.4s / 3.2s</code> 异步呼吸闪烁，与 8s 主场景错峰循环。</li>
        <li><strong>0.0s ~ 1.8s（逐字坍缩 + 36 枚海洋粒子转场）</strong>：所有中文经 <code>convertSVGTextToPath</code> 转为独立字形路径，沿三次贝塞尔曲线 <code>keySplines="0.77 0 0.175 1"</code> 向中心聚拢并交接给 36 枚蓝/粉像素块粒子。</li>
        <li><strong>1.8s ~ 3.3s（动作 ①：大肥鱼灵感注入 → 海洋鲁班设定）</strong>：左侧「DeepSeek 大肥鱼灵感卡」飞入插槽，触发工作台 <code>4px</code> 受击回弹；中央生成戴海蓝鲸鱼帽、背透明水舱、持鲸鱼水炮的鲁班七号。</li>
        <li><strong>3.3s ~ 5.0s（动作 ②：虚线选框锁定帽子 → 局部改色不崩脸）</strong>：复刻原文<em>“只改帽子颜色，其他地方别乱动”</em>——四角锚点选框精准框住头顶，扫描线扫过，蓝帽无缝变为珊瑚粉帽，脸型与武器纹丝不动。</li>
        <li><strong>5.0s ~ 7.2s（动作 ③：鲸鱼炮后坐发射 → 三张成果卡弹性展开）</strong>：鲸鱼水炮向后蓄力后坐 <code>7px</code> 并发射小鲸鱼水弹，右侧依次弹开「四技能攻击 GIF」「CAD 机械拆解图」「12 张游戏表情包」并盖上翠绿完成大对勾 <code>✓</code>。</li>
      </ul>

      <h2>二、同时间轴 GIF 兜底版与六帧快照</h2>
      <div class="stage" style="margin-bottom:14px">
        <img src="intro.gif" alt="GIF 兜底版" style="width:100%;height:auto;display:block">
      </div>
      <div class="keyframes">
        <div class="kf-card"><span>0.5s · 品牌口号亮相</span><img src="keyframe-0.5s-brand.png" alt="0.5s"></div>
        <div class="kf-card"><span>1.6s · 文字坍缩为像素粒子</span><img src="keyframe-1.6s-particles.png" alt="1.6s"></div>
        <div class="kf-card"><span>2.6s · 大肥鱼灵感生成蓝帽鲁班</span><img src="keyframe-2.6s-blue-luban.png" alt="2.6s"></div>
        <div class="kf-card"><span>4.2s · 选框锁定局部改珊瑚粉帽</span><img src="keyframe-4.2s-pink-edit.png" alt="4.2s"></div>
        <div class="kf-card"><span>5.3s · 鲸鱼水炮后坐开火</span><img src="keyframe-5.3s-cannon-fire.png" alt="5.3s"></div>
        <div class="kf-card"><span>6.4s · 三张成果卡展开+完成对勾</span><img src="keyframe-6.4s-full-deliverables.png" alt="6.4s"></div>
      </div>
    </div>

    <div>
      <h2>三、375px 手机公众号首屏真实排版预览</h2>
      <div class="phone">
        <div class="phone-bar">程序员梦哥 · 公众号预览 (375px)</div>
        <div class="phone-body">
          ${svg}
          <h3>GPT Image 叒叒叒更新了，我用它手搓了一套鲁班皮肤</h3>
          <div class="meta">程序员梦哥 · AI 视觉与实战</div>
          <p><strong>不知道诸位对游戏有没有一种情怀或者执念。</strong></p>
          <p>我平时喜欢玩《王者荣耀》，最喜欢的英雄就是<strong>鲁班七号</strong>。虽然玩得菜，但是总想给他安排一套好看的皮肤，奈何口袋比脸还干净。</p>
          <p><mark>正好，上周 OpenAI 官宣，自己的生图模型叒叒叒更新了！这次更新到了 Image 2.6。</mark></p>
          <p>那就先用 GPT Image 2.6 试试。让它设计一套海洋大肥鱼皮肤，再试局部改帽子颜色、配齐四技能攻击动效、CAD 机械拆解和 12 张表情包……</p>
        </div>
      </div>
    </div>
  </div>
</main>
<script>
  function freezeAt(sec) {
    document.querySelectorAll('svg').forEach(s => {
      s.pauseAnimations();
      s.setCurrentTime(sec);
    });
  }
  function playAll() {
    document.querySelectorAll('svg').forEach(s => {
      s.setCurrentTime(0);
      s.unpauseAnimations();
    });
  }
</script>
</body>
</html>`;
}

async function main() {
  const svg = await buildSVG();
  fs.writeFileSync(path.join(OUT, 'intro.svg'), svg, 'utf8');
  fs.writeFileSync(
    path.join(OUT, 'intro.wechat.html'),
    `<section style="margin:0 0 18px;width:100%;line-height:0">${svg}</section>\n`,
    'utf8'
  );
  await renderCanvasFrames();
  fs.writeFileSync(path.join(OUT, 'preview.html'), buildPreviewHTML(svg), 'utf8');

  const meta = {
    article_source: 'raw/article/程序员梦哥/GPT Image 叒叒叒更新了，我用它手搓了一套鲁班皮肤.md',
    viewBox: '0 0 1246 220',
    duration_seconds: DUR,
    svg_bytes: Buffer.byteLength(svg, 'utf8'),
    gif_bytes: fs.statSync(path.join(OUT, 'intro.gif')).size,
    zero_text_tags: !svg.includes('<text'),
    zero_image_tags: !svg.includes('<image'),
    zero_script_tags: !svg.includes('<script'),
    path_count: (svg.match(/<path\b/g) || []).length,
    rect_count: (svg.match(/<rect\b/g) || []).length,
    animate_count: (svg.match(/<animate\b/g) || []).length,
    animateTransform_count: (svg.match(/<animateTransform\b/g) || []).length,
    spline_count: (svg.match(/calcMode="spline"/g) || []).length,
    acts: [
      '0.0s-1.35s: 像素梦哥待机 + 程序员梦哥品牌口号与 GPT Image 2.6 标签亮相',
      '1.35s-1.95s: 汉字逐字沿贝塞尔曲线向中心坍缩，交接给 36 枚海洋/珊瑚像素粒子',
      '1.95s-3.30s: DeepSeek 大肥鱼灵感卡带插入左侧卡槽，触发工作台回弹，生成蓝帽海洋鲁班立绘',
      '3.30s-5.00s: 虚线编辑选框精准锁定鲸鱼帽，扫描线扫过将蓝帽局部改为珊瑚粉帽，人物不崩',
      '5.00s-7.15s: 鲸鱼水炮后坐 7px 发射小鲸鱼水弹，右侧弹性展开四技能 GIF、CAD 拆解图、12 张表情包三卡并弹出完成对勾',
      '7.15s-8.00s: 粒子回流复位至品牌口号，无缝闭合循环',
    ],
    wechat_live_verified: false,
  };
  fs.writeFileSync(path.join(OUT, 'motion.json'), JSON.stringify(meta, null, 2) + '\n', 'utf8');
  console.log(JSON.stringify(meta, null, 2));
}

main().catch(err => {
  console.error(err);
  process.exitCode = 1;
});
