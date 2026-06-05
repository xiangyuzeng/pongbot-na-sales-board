# 庞伯特 PONGBOT · 北美销售负责人 · 面试答题板

58题 · 10模块的面试答题板，面向 **庞伯特 / PONGBOT（上海创屹科技）北美销售负责人** 岗位的 **CEO 张海波终面**。内容覆盖：市场背景速查、开场必答、公司·产品·赛道认知、竞争格局、Foxx 经历深挖、PayPal 经历、销售能力 & 北美打法、行为 STAR、战略·风险·收尾、反问环节。

答案为中文（终面以普通话进行），并融入了对 PONGBOT 的深度研究：手-眼-脑 AI 平台与数据飞轮、Aura / Aura S 产品与定价、PACE/Aura 众筹战绩、北美网球/匹克球/板式网球市场数据、竞品对比，以及需要诚实应对的本土化缺口（FCC/保修/美国零售/合作关系）。

基于 **Next.js 14 + React 18**，纯内联样式、浅色主题，客户端 localStorage 记录复习进度。

## 本地开发

```bash
npm install
npm run dev
# http://localhost:3000
```

## 部署到 Vercel

1. 把此仓库 Push 到 GitHub
2. 在 [vercel.com/new](https://vercel.com/new) 导入此仓库
3. Vercel 自动识别 Next.js，默认配置直接 **Deploy**

无需环境变量，无外部依赖。

## 重新生成题库

题库内容由 `tools/build_data.py` 生成（自动计算 `charCount`、卡片 id）。修改该脚本中的 `MODULES` 后重新生成：

```bash
python3 tools/build_data.py   # 写入 app/data.js
```

## 模块构成

| 模块 | 题数 |
|------|------|
| 📌 市场背景速查 | 3 |
| 🎬 开场必答 | 6 |
| 🏢 公司·产品·赛道认知 | 6 |
| ⚡ 竞争格局 | 5 |
| 🛒 Foxx 经历深挖 | 7 |
| 💳 PayPal 经历 | 3 |
| 📈 销售能力 & 北美打法 | 9 |
| 🗣️ 行为 STAR | 7 |
| 🧠 战略·风险·收尾 | 5 |
| 🔄 反问环节 | 7 |
| **合计** | **58** |

## 题型

🗣️ 行为面试 · 🔍 项目深挖 · 🎾 产品·市场 · 📈 销售打法 · 🔄 反问环节
