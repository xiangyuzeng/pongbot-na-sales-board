export const metadata = {
  title: '庞伯特 PONGBOT · 北美销售负责人 · 面试答题板',
  description: '58题 · 10模块 · 市场速查·产品/赛道·竞品·STAR行为·销售打法·反问 · 终面（CEO 张海波）',
};
export default function RootLayout({ children }) {
  return (
    <html lang="zh-CN">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
      </head>
      <body>{children}</body>
    </html>
  );
}
