# -*- coding: utf-8 -*-
import os
import re
import urllib.parse
from write_final_pages import science_list, get_science_article_metadata

articles_dir = "articles"

# Create tags for sidebar
tags = ['机场评测', '科普专栏', '低延迟', '4K不卡顿', 'Clash配置', '小火箭', 'Reality协议', 'Hysteria2', '便宜机场', '月付', '按量付费', 'Netflix', 'ChatGPT', '软路由', '游戏专线', '安全防护', 'SSR机场推荐', 'V2Ray节点', 'Shadowsocks', '免费翻墙VPN', 'Trojan协议', 'iPhone翻墙', '安卓VPN', '傻瓜一键翻墙', 'GLaDOS机场', '付费机场', '节点订阅', '流媒体解锁', 'Disney+', 'TikTok加速', '国内电脑VPN']
sidebar_tags_html = "".join([f'<a href="../index.html?tag={urllib.parse.quote(t)}" class="sidebar-tag">{t}</a>' for t in tags])

featured_items = [
    {'slug': 'sujie-review', 'title': '速界 机场评测：不限速不限制设备的高性能 IEPL 节点首选推荐', 'date': '2026-07-03', 'label': 'SJ', 'logo': 'https://i.ibb.co/tpkZpVhs/sujielogo.webp'},
    {'slug': 'edge-review', 'title': '边缘节点 机场（EdgeNova）深度评测：无日志与极速数据中转', 'date': '2026-07-14', 'label': 'BY', 'logo': 'https://i.ibb.co/C5P4QcfT/bianyuanjiedianlogo.webp'},
    {'slug': 'jilianyun-review', 'title': '极连云 机场测速与评测：高性价比 IEPL 专线推荐', 'date': '2026-07-18', 'label': 'JL', 'logo': 'https://i.ibb.co/TxW2rqGj/jilianyunlogo.webp'},
    {'slug': 'guangnianti-review', 'title': '光年梯 机场评测：稳定解锁流媒体与高可用线路方案', 'date': '2026-07-16', 'label': 'GN', 'logo': 'https://i.ibb.co/mCYxy3yM/guanniantilogo.webp'},
    {'slug': 'shunyun-review', 'title': '瞬云 机场测速评测：限时特惠年付小包与高带宽 ANYCAST 连接方案', 'date': '2026-07-06', 'label': 'SY', 'logo': 'https://i.ibb.co/jkR2rZRw/shunyunlogo.webp'},
    {'slug': 'kuaili-review', 'title': '快狸 机场推荐：多设备在线与高性价比备用选择', 'date': '2026-07-10', 'label': 'KL', 'logo': 'https://i.ibb.co/1f4FvF92/kuaililogo.webp'},
    {'slug': 'huanyuyun-review', 'title': '寰宇云 机场评测：高稳定性与极速专线节点官网订阅推荐', 'date': '2026-07-20', 'label': 'HY', 'logo': 'https://i.ibb.co/jZ9ZVgJ7/huanyuyunlogo.webp'},
    {'slug': 'huacloud-review', 'title': '花云 机场评测：老牌 BGP 中继与专线节点测速分流推荐', 'date': '2026-07-21', 'label': 'HC', 'logo': 'https://i.ibb.co/N2YrnGjH/huayunlogo.png'},
    {'slug': 'naixi-review', 'title': '奶昔 机场评测：顶级 IPLC 专线与流媒体解锁深度测评', 'date': '2026-07-22', 'label': 'NX', 'logo': 'https://i.ibb.co/609wzM0L/naixilogo.jpg'}
]

featured_items_html = "\n".join([
    f'''<div class="featured-item">
      <div class="featured-item-img" style="background: #fff; display: flex; align-items: center; justify-content: center; overflow: hidden;"><img src="{item['logo']}" style="width: 100%; height: 100%; object-fit: cover;" alt="{item['label']}"></div>
      <div class="featured-item-content">
        <h4 class="featured-item-title"><a href="{item['slug']}.html">{item['title']}</a></h4>
        <span class="featured-item-date">{item['date']}</span>
      </div>
    </div>'''
    for item in featured_items
])

def compile_all():
    print(f"Loaded {len(science_list)} science articles to compile.")
    for idx, s in enumerate(science_list):
        slug = s['slug']
        title = s['title']
        date = s['date']
        
        fpath = os.path.join(articles_dir, f"{slug}.html")
        if not os.path.exists(fpath):
            print(f"Error: {fpath} does not exist!")
            continue
            
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Get metadata
        meta = get_science_article_metadata(slug, title, date)
        excerpt = meta['excerpt']
        tags_list = meta['tags']
        views = meta['views']
        
        # Parse body content
        start_idx = content.find('<div class="article-body">')
        if start_idx == -1:
            start_idx = content.find('<article class="content-feed">')
            if start_idx != -1:
                start_idx = content.find('>', start_idx) + 1
        else:
            start_idx += len('<div class="article-body">')
            
        end_idx = content.find('<div class="card-footer"')
        if end_idx == -1:
            end_idx = content.find('<!-- Prev/Next Navigation')
        if end_idx == -1:
            end_idx = content.find('</article>')
        if end_idx == -1:
            end_idx = content.find('</body>')
            
        if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
            # If parsing fails or it's a simple fragment with just body paragraphs:
            body_html = content
            # Clean up wrap tags if they are already in the file
            if "<body>" in body_html:
                body_html = body_html.split("<body>")[1]
            if "</body>" in body_html:
                body_html = body_html.split("</body>")[0]
            if '<div class="article-body">' in body_html:
                body_html = body_html.split('<div class="article-body">')[1]
            if '</div>' in body_html:
                body_html = body_html.rsplit('</div>', 1)[0]
        else:
            body_html = content[start_idx:end_idx].strip()
            
        # Build tags HTML
        tags_html = " ".join([f'<a href="../index.html?tag={urllib.parse.quote(t)}" class="card-tag">{t}</a>' for t in tags_list])
        
        # Prev/Next nav
        prev_idx = idx - 1 if idx > 0 else len(science_list) - 1
        next_idx = (idx + 1) % len(science_list)
        prev_art = science_list[prev_idx]
        next_art = science_list[next_idx]
        
        # Build full HTML
        full_html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <script>
    (function() {{
      let savedTheme = null;
      try {{
        savedTheme = localStorage.getItem('theme');
      }} catch (e) {{}}
      const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const theme = savedTheme === 'dark' || (!savedTheme && systemPrefersDark) ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', theme);
    }})();
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - 机场速递 (jichangspeed.biz)</title>
  <!-- SEO Meta Tags -->
  <meta name="description" content="{excerpt}">
  <meta name="keywords" content="{', '.join(tags_list)}, 稳定, 安全, 高速, 便宜, 性价比, 机场, Clash, Shadowrocket, V2RayNG, 科学上网, 翻墙, jichangspeed.biz">
  <meta name="robots" content="index, follow">
  <!-- GEO Tags -->
  <meta name="geo.region" content="CN-GD" />
  <meta name="geo.placename" content="Guangdong" />
  <meta name="geo.position" content="23.12908;113.26436" />
  <meta name="ICBM" content="23.12908, 113.26436" />
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://jichangspeed.biz/articles/{slug}.html">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{excerpt}">
  <meta property="og:image" content="https://jichangspeed.biz/images/og-share.jpg">
  
    <!-- Favicon / Site Icons -->
  <link rel="icon" type="image/x-icon" href="../favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="../favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="../favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="../apple-touch-icon.png">
  <link rel="stylesheet" href="../css/style.css?v=20260731">
  <style>
    [data-theme="dark"] .logo span {{
      background: none !important;
      -webkit-background-clip: unset !important;
      -webkit-text-fill-color: #ffffff !important;
      color: #ffffff !important;
    }}
  </style>
</head>
<body>
  <!-- Header -->
  <header class="header">
    <div class="container header-container">
      <a href="../index.html" class="logo">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10" fill="var(--accent-primary)" />
          <path d="M12 6L18 13L14 12.5L14.5 17L12 15L9.5 17L10 12.5 L6 13Z" fill="#ffffff" />
        </svg>
        <span>机场速递</span>
      </a>
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">☰</button>
      <nav class="nav" id="nav-menu">
        <a href="../index.html" class="nav-link">主页</a>
        <!-- Item 1: 机场推荐 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">机场推荐 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="cheap-airports.html" class="dropdown-item">便宜机场推荐</a>
            <a href="premium-airports.html" class="dropdown-item">优质机场推荐</a>
            <a href="kuaili-review.html" class="dropdown-item">老牌机场推荐</a>
          </div>
        </div>
        <!-- Item 2: 评测与指南 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">评测与指南 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="best-airports-2026.html" class="dropdown-item">精选汇总</a>
            <a href="../vpn-guide.html" class="dropdown-item">科普专栏</a>
          </div>
        </div>
        <!-- Item 3: 更多 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">更多 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="../archives.html" class="dropdown-item">归档</a>
            <a href="../about.html" class="dropdown-item">关于</a>
          </div>
        </div>
        <!-- Item 4: 搜索 (Expandable Navbar Search) -->
        <div class="nav-search-container" id="nav-search-container">
          <button class="nav-search-btn" id="nav-search-btn" aria-label="Search">
            <svg class="search-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
          </button>
          <input type="text" id="nav-search-input" class="nav-search-input" placeholder="搜索...">
          <div class="hot-search-popup" id="hot-search-popup">
            <span class="hot-search-title">热门搜索</span>
            <div class="hot-search-tags">
              <span class="hot-tag" onclick="performNavSearch('极连云')">极连云</span>
              <span class="hot-tag" onclick="performNavSearch('边缘节点')">边缘节点</span>
              <span class="hot-tag" onclick="performNavSearch('快狸')">快狸</span>
              <span class="hot-tag" onclick="performNavSearch('速界')">速界</span>
            </div>
          </div>
        </div>
        <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Theme">
          <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
          <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>
      </nav>
    </div>
  </header>
  
  <!-- Article Layout -->
  <main class="container article-page">
    <div class="breadcrumbs">
      <a href="../index.html">首页</a>
      <svg viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <a href="../vpn-guide.html">科普专栏</a>
      <svg viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <span>正文</span>
    </div>
    <div class="main-layout">
      <!-- Left Column: Article Content -->
      <article class="content-feed">
        <div class="article-header">
          <div class="card-meta" style="margin-bottom: 12px;">
            <span class="card-badge" style="position: static; background: var(--accent-gradient) !important; color: #fff !important;">
              科普专栏
            </span>
            <span>
              <svg viewBox="0 0 24 24"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/></svg>
              {date}
            </span>
            <span>
              <svg viewBox="0 0 24 24"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
              阅读 ({views})
            </span>
          </div>
          <h1 class="article-title-large">{title}</h1>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 16px; align-items: center;">
            <span style="font-size: 0.85rem; font-weight: 600; color: var(--text-muted);">所属版块: </span>
            <a href="../vpn-guide.html" class="card-badge" style="position: static; text-decoration: none;">科普专栏</a>
          </div>
        </div>
        
        <div class="article-body">
          {body_html}
        </div>
        
        <div class="card-footer" style="padding-top: 24px; border-top: 1px dashed var(--border-color); margin-top: 20px;">
          <div class="card-tags">
            {tags_html}
          </div>
        </div>
        <!-- Prev/Next Navigation -->
        <div class="article-navigation">
          <a href="{prev_art['slug']}.html" class="article-nav-card">
            <span class="article-nav-label">← 上一篇</span>
            <span class="article-nav-title">{prev_art['title']}</span>
          </a>
          <a href="{next_art['slug']}.html" class="article-nav-card" style="text-align: right;">
            <span class="article-nav-label">下一篇 →</span>
            <span class="article-nav-title">{next_art['title']}</span>
          </a>
        </div>
      </article>
      <!-- Right Column: Sidebar -->
      <aside class="sidebar">
        <!-- Widget: Popular Tags -->
        <div class="sidebar-widget">
          <h3 class="widget-title">
            <svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 8.25c-.97 0-1.75-.78-1.75-1.75s.78-1.75 1.75-1.75 1.75.78 1.75 1.75S6.47 8.25 5.5 8.25z"/></svg>
            热门标签
          </h3>
          <div class="tags-cloud">
            {sidebar_tags_html}
          </div>
        </div>
        <!-- Widget: Featured Articles -->
        <div class="sidebar-widget">
          <h3 class="widget-title">
            <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
            精选文章
          </h3>
          <div class="featured-list">
            {featured_items_html}
          </div>
        </div>
      </aside>
    </div>
  </main>
  
  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <h3 class="footer-brand-title">机场速递</h3>
          <p>jichangspeed.biz 专注于2026年最新高速、便宜、安全专线网络节点测速 and 评测。我们致力于打破虚假宣传，为您提供真实的主力官网订阅入口。</p>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">快捷导航</h4>
          <ul class="footer-links-list">
            <li><a href="cheap-airports.html" class="footer-link">便宜机场推荐</a></li>
            <li><a href="premium-airports.html" class="footer-link">优质机场推荐</a></li>
            <li><a href="kuaili-review.html" class="footer-link">老牌机场推荐</a></li>
            <li><a href="best-airports-2026.html" class="footer-link">精选汇总</a></li>
          </ul>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">推荐列表</h4>
          <ul class="footer-links-list">
            <li><a href="https://haozevpn.jlyvipaff.com/#/?code=pfzRz5dR" target="_blank" class="footer-link">极连云官网 ↗</a></li>
            <li><a href="https://zoio.edgenovaaff.cc/#/?code=Y65i2kCU" target="_blank" class="footer-link">边缘节点官网 ↗</a></li>
            <li><a href="https://19629.gntaff.com/#/?code=AixFrykO" target="_blank" class="footer-link">光年梯官网 ↗</a></li>
            <li><a href="https://196295.kuailiaff.com/#/?code=tmUe2z1n" target="_blank" class="footer-link">快狸官网 ↗</a></li>
            <li><a href="https://lqy001.speedworldaff.com/#/?code=C2v7kRVl" target="_blank" class="footer-link">速界官网 ↗</a></li>
            <li><a href="https://aaa.jichang.best/#/register?code=ClNa0zPm" target="_blank" class="footer-link">瞬云官网 ↗</a></li>
          </ul>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">合作联系</h4>
          <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 8px;">商务与测速投稿请发邮件：</p>
          <ul class="footer-links-list" style="font-size: 0.85rem;">
            <li>邮箱: <a href="mailto:psytong@outlook.com" class="footer-link">psytong@outlook.com</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 机场速递 (jichangspeed.biz) 保留所有权利。</p>
      </div>
    </div>
  </footer>
  <script src="../js/main.js?v=20260729"></script>
</body>
</html>"""
        
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"Successfully compiled: {slug}.html")

if __name__ == '__main__':
    compile_all()
