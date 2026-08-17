# -*- coding: utf-8 -*-
import os

import re

def get_science_article_metadata(slug, title, date):
    html_path = f"articles/{slug}.html"
    if not os.path.exists(html_path):
        return {
            'slug': slug,
            'title': title,
            'date': date,
            'excerpt': f"关于 {title} 的专业科普与配置指南。",
            'categories': ['science'],
            'tags': ['科普专栏'],
            'views': 800,
            'readTime': 5
        }
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html_content)
    excerpt = desc_match.group(1) if desc_match else f"关于 {title} 的专业科普与配置指南。"
    
    kw_match = re.search(r'<meta\s+name="keywords"\s+content="([^"]+)"', html_content)
    keywords_str = kw_match.group(1) if kw_match else ""
    tags = [k.strip() for k in keywords_str.split(',') if k.strip()]
    if not tags:
        tags = ['科普专栏']
        
    categories = ['science']
    lower_title = title.lower()
    if 'clash' in lower_title:
        categories.append('clash')
    if 'shadowrocket' in lower_title or '小火箭' in lower_title:
        categories.append('shadowrocket')
    if 'sing-box' in lower_title:
        categories.append('sing-box')
        
    views = 900 + (len(slug) * 17) % 500
    readTime = 5 + (len(title) % 5)
    
    return {
        'slug': slug,
        'title': title,
        'date': date,
        'excerpt': excerpt,
        'categories': categories,
        'tags': tags,
        'views': views,
        'readTime': readTime
    }

original_card_styles = {
    'best-airports-2026': {
        'style': 'background: linear-gradient(135deg, #6366f1 0%, #3b82f6 100%);',
        'content': '精选汇总<br>2026 梯子合集',
        'badge': '本站精选'
    },
    'sujie-review': {
        'style': 'background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%);',
        'content': '速界机场<br>IEPL 节点',
        'badge': '老牌推荐'
    },
    'edge-review': {
        'style': 'background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);',
        'content': '边缘节点机场<br>无日志专线',
        'badge': '老牌推荐'
    },
    'jilianyun-review': {
        'style': 'background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);',
        'content': '极连云<br>IEPL 专线',
        'badge': '便宜推荐'
    },
    'guangnianti-review': {
        'style': 'background: linear-gradient(135deg, #10b981 0%, #059669 100%);',
        'content': '光年梯<br>高可用流媒体',
        'badge': '老牌推荐'
    },
    'cheap-airports': {
        'style': 'background: linear-gradient(135deg, #ec4899 0%, #db2777 100%);',
        'content': '便宜机场<br>低至十元',
        'badge': '便宜推荐'
    },
    'premium-airports': {
        'style': 'background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);',
        'content': '高端机场<br>专线办公稳定',
        'badge': '老牌推荐'
    },
    'kuaili-review': {
        'style': 'background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);',
        'content': '快狸机场<br>多设备性价比',
        'badge': '便宜推荐'
    },
    'airport-guide-2026': {
        'style': 'background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);',
        'content': 'Clash<br>机场推荐',
        'badge': '科普指南'
    },
    'iplc-guide': {
        'style': 'background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);',
        'content': 'IPLC<br>专线科普',
        'badge': '科普指南'
    },
    'streaming-ai-guide': {
        'style': 'background: linear-gradient(135deg, #10b981 0%, #059669 100%);',
        'content': '流媒体与AI<br>翻墙解锁',
        'badge': '科普指南'
    },
    'guangshuyun-review': {
        'style': 'background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);',
        'content': '光速云<br>IPLC 专线',
        'badge': '老牌推荐'
    },
    'globalyun-review': {
        'style': 'background: linear-gradient(135deg, #10b981 0%, #059669 100%);',
        'content': '全球云<br>BGP 优化',
        'badge': '老牌推荐'
    },
    'shunyun-review': {
        'style': 'background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);',
        'content': '瞬云机场<br>特惠年付小包',
        'badge': '便宜推荐'
    },
    'huanyuyun-review': {
        'style': 'background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);',
        'content': '寰宇云<br>原生 IP 专线',
        'badge': '老牌推荐'
    },
    'subscription-guide': {
        'style': 'background: linear-gradient(135deg, #6c757d 0%, #495057 100%);',
        'content': '网络订阅<br>配置避坑',
        'badge': '科普指南'
    }
}

def get_card_style(article):
    slug = article['slug']
    if slug in original_card_styles:
        return original_card_styles[slug]
        
    title = article['title'].lower()
    if 'clash' in title:
        return {
            'style': 'background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);',
            'content': 'Clash<br>科普教程',
            'badge': '科普指南'
        }
    elif 'shadowrocket' in title or '小火箭' in title or '火箭' in title:
        return {
            'style': 'background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);',
            'content': 'Shadowrocket<br>苹果配置',
            'badge': '科普指南'
        }
    elif 'v2rayng' in title:
        return {
            'style': 'background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);',
            'content': 'V2RayNG<br>安卓配置',
            'badge': '科普指南'
        }
    elif 'openwrt' in title or '路由' in title:
        return {
            'style': 'background: linear-gradient(135deg, #10b981 0%, #059669 100%);',
            'content': 'OpenWrt<br>软路由技术',
            'badge': '科普指南'
        }
    elif 'sing-box' in title:
        return {
            'style': 'background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);',
            'content': 'Sing-box<br>高吞吐分流',
            'badge': '科普指南'
        }
    else:
        return {
            'style': 'background: linear-gradient(135deg, #6c757d 0%, #495057 100%);',
            'content': '网络科普<br>指南',
            'badge': '科普指南'
        }

def build_card_html(article):
    slug = article['slug']
    title = article['title']
    date = article['date']
    excerpt = article['excerpt']
    views = article.get('views', 1000)
    
    cats = article.get('categories', [])
    data_cats = ','.join(cats)
    
    tags = article.get('tags', [])
    data_tags = ','.join(tags)
    
    style_info = get_card_style(article)
    card_style = style_info['style']
    card_content_mask = style_info['content']
    card_badge = style_info['badge']
    
    tags_html = ' '.join([f'<span class="card-tag">{t}</span>' for t in tags[:2]])
    
    return f'''      <article class="article-card" data-categories="{data_cats}" data-tags="{data_tags}">
        <div class="card-image-wrap" style="{card_style}">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.4rem; text-align:center; padding: 20px;">
            {card_content_mask}
          </div>
          <span class="card-badge">{card_badge}</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>{date}</span>
            <span>阅读 ({views})</span>
          </div>
          <h3 class="card-title"><a href="articles/{slug}.html">{title}</a></h3>
          <p class="card-excerpt">{excerpt}</p>
          <div class="card-footer">
            <div class="card-tags">
              {tags_html}
            </div>
            <a href="articles/{slug}.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>'''


links = {
    '极连云': 'https://haozevpn.jlyvipaff.com/#/?code=pfzRz5dR',
    '光年梯': 'https://hjbesu8d.fazuttt.club/#/?code=AixFrykO',
    '边缘节点': 'https://zoio.edgenovaaff.cc/#/?code=Y65i2kCU',
    '快狸': 'https://iu9asffa.kuailitztz2.sbs/#/?code=tmUe2z1n',
    '光速云': 'https://kjlq01.gsyvipaff.cc/#/?code=b1OTkTeL',
    '全球云': 'https://haozevpn.gcvipaff.cc/#/?code=WRQJc2v4',
    '瞬云': 'https://aaa.jichang.best/#/register?code=ClNa0zPm',
    '寰宇云': 'https://vip3.huanyuyunbest.com/#/register?code=K6h5VWw2',
    '速界': 'https://asfweroasf.sujietztz2.xyz/#/?code=C2v7kRVl'
}

science_list = [
    {'slug': 'airport-guide-2026', 'title': '2026年机场排行榜：高性价比翻墙机场科普与横向评测', 'date': '2026-07-22'},
    {'slug': 'iplc-guide', 'title': 'IPLC/IEPL专线科普：4K不卡顿、游戏加速、专线机场完全指南', 'date': '2026-07-22'},
    {'slug': 'streaming-ai-guide', 'title': 'Netflix/ChatGPT/TikTok机场选择指南：流媒体与AI工具加速完全攻略', 'date': '2026-07-22'},
    {'slug': 'clash-tutorial', 'title': 'Clash配置教程：2026年最全Clash节点导入与订阅地址使用完全指南', 'date': '2026-07-23'},
    {'slug': 'shadowrocket-setup', 'title': 'Shadowrocket配置教程：iOS苹果小火箭订阅地址导入与SS/SSR专线配置完全指南', 'date': '2026-07-23'},
    {'slug': 'v2rayng-guide', 'title': 'V2RayNG配置教程：安卓手机一键导入订阅地址与VLESS/VESS网络配置攻略', 'date': '2026-07-23'},
    {'slug': 'lantern-alternative', 'title': '蓝灯Lantern好用吗？2026年蓝灯替代方案与SS/SSR专线中转机场推荐', 'date': '2026-07-23'},
    {'slug': 'reality-protocol', 'title': 'Reality协议科普：什么是Reality协议？安全性与主流客户端配置详解', 'date': '2026-07-23'},
    {'slug': 'hysteria2-vs-tuic', 'title': 'Hysteria2与Tuic协议对比：晚高峰高丢包环境下的最佳UDP翻墙协议选择', 'date': '2026-07-23'},
    {'slug': 'iplc-vs-iepl', 'title': 'IPLC专线机场与IEPL中转有何区别？主流专线机场网络传输架构大科普', 'date': '2026-07-23'},
    {'slug': 'openwrt-router', 'title': 'OpenWrt科普教程：软路由固件插件安装、Clash/Sing-box节点配置完全指南', 'date': '2026-07-23'},
    {'slug': 'vps-vs-airport', 'title': '自建节点对比专线机场：2026年为什么我不建议新手折腾搭建翻墙？', 'date': '2026-07-23'},
    {'slug': 'one-multiplier', 'title': '什么是1倍率机场？如何看懂计费规则，避开机场流量折算陷阱？', 'date': '2026-07-23'},
    {'slug': 'streaming-unlock', 'title': '什么是解锁流媒体节点？Netflix/Disney+ 住宅IP分流选择科普与机场推荐', 'date': '2026-07-23'},
    {'slug': 'clash-subscription', 'title': '网络订阅地址获取与客户端通用配置防跑路避坑常识', 'date': '2026-07-23'},
    {'slug': 'hy2-performance', 'title': 'Hysteria2协议在低带宽晚高峰下的速度实测与Reality/VLESS协议横向评测', 'date': '2026-07-23'},
    {'slug': 'tuic-latency', 'title': 'Tuic协议适合玩外服游戏吗？Tuic低延迟原理分析与SS/SSR专线游戏节点选择', 'date': '2026-07-23'},
    {'slug': 'router-firmware', 'title': '软路由科普深度科普：OpenWrt主流固件插件性能对比与Clash配置教程', 'date': '2026-07-23'},
    {'slug': 'reality-vless-verge', 'title': 'VLESS与Reality协议在Clash Verge中的通用配置与速度优化教程', 'date': '2026-07-23'},
    {'slug': 'shadowrocket-h2', 'title': '小火箭Hysteria2节点怎么配置？iOS Shadowrocket基于UDP的高丢包提速教程', 'date': '2026-07-23'},
    {'slug': 'openwrt-singbox', 'title': 'Sing-box在OpenWrt软路由系统下的配置与高吞吐专线分流教程', 'date': '2026-07-23'},
    {'slug': 'blue-lantern-vpn', 'title': '蓝灯VPN好用吗？为什么老牌翻墙VPN蓝灯连不上与最优机场方案对比', 'date': '2026-07-23'},
    {'slug': 'reality-vless-comparison', 'title': 'Reality混淆协议与传统VLESS/Vmess加密协议安全性与防封锁横向对比', 'date': '2026-07-23'}
]

def write_index():
    from generate_final_site import article_list
    global science_list
    
    full_science_list = []
    for s in science_list:
        meta = get_science_article_metadata(s['slug'], s['title'], s['date'])
        full_science_list.append(meta)
        
    all_articles_map = {}
    for a in article_list:
        all_articles_map[a['slug']] = a
    for a in full_science_list:
        all_articles_map[a['slug']] = a
        
    original_slugs = [
        'best-airports-2026',
        'sujie-review',
        'edge-review',
        'jilianyun-review',
        'guangnianti-review',
        'cheap-airports',
        'premium-airports',
        'kuaili-review',
        'airport-guide-2026',
        'iplc-guide',
        'streaming-ai-guide',
        'guangshuyun-review',
        'globalyun-review',
        'shunyun-review',
        'huanyuyun-review',
        'subscription-guide'
    ]
    
    sorted_articles = []
    for slug in original_slugs:
        if slug in all_articles_map:
            sorted_articles.append(all_articles_map[slug])
            
    remaining_articles = []
    for s in full_science_list:
        if s['slug'] not in original_slugs:
            remaining_articles.append(s)
            
    remaining_articles.sort(key=lambda x: x['date'], reverse=True)
    sorted_articles.extend(remaining_articles)
    
    cards_html_list = []
    for a in sorted_articles:
        cards_html_list.append(build_card_html(a))
    cards_html = '\n'.join(cards_html_list)

    html = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>机场速递 (jichangspeed.biz) - 2026稳定安全高速便宜机场推荐与官网订阅评测</title>
  <!-- SEO Meta Tags -->
  <meta name="description" content="机场速递 (jichangspeed.biz) 专注于2026年最新稳定、安全、高速、便宜、高性价比机场推荐。提供极连云、光年梯、边缘节点、快狸、光速云、全球云、瞬云、寰宇云、速界等官网入口。">
  <meta name="keywords" content="极连云, 光年梯, 边缘节点, 快狸, 光速云, 全球云, 瞬云, 寰宇云, 速界, 机场推荐, 稳定机场, 安全翻墙, 高速中转, jichangspeed.biz">
  <meta name="robots" content="index, follow">
  <!-- GEO Tags -->
  <meta name="geo.region" content="CN-GD" />
  <meta name="geo.placename" content="Guangdong" />
  <meta name="geo.position" content="23.12908;113.26436" />
  <meta name="ICBM" content="23.12908, 113.26436" />
    <!-- Favicon / Site Icons -->
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
  <link rel="stylesheet" href="css/style.css?v=20260731">
  <style>
    /* 强力保证夜间模式下 Logo span 文本显示为清晰的纯白色，不受外部样式缓存影响 */
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
      <a href="index.html" class="logo" onclick="resetFilters(); return false;">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10" fill="var(--accent-primary)" />
          <path d="M12 6L18 13L14 12.5L14.5 17L12 15L9.5 17L10 12.5 L6 13Z" fill="#ffffff" />
        </svg>
        <span>机场速递</span>
      </a>
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">☰</button>
      <nav class="nav" id="nav-menu">
        <a href="index.html" class="nav-link">主页</a>
        <!-- Item 1: 机场推荐 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">机场推荐 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="articles/cheap-airports.html" class="dropdown-item">便宜机场推荐</a>
            <a href="articles/premium-airports.html" class="dropdown-item">优质机场推荐</a>
            <a href="articles/kuaili-review.html" class="dropdown-item">老牌机场推荐</a>
          </div>
        </div>
        <!-- Item 2: 机场资讯 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">机场资讯 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="articles/best-airports-2026.html" class="dropdown-item">精选汇总</a>
            <a href="vpn-guide.html" class="dropdown-item">科普专栏</a>
          </div>
        </div>
        <!-- Item 3: 更多 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">更多 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="archives.html" class="dropdown-item">文章归档</a>
            <a href="about.html" class="dropdown-item">关于我们</a>
            <a href="#" class="dropdown-item" onclick="showFriendsModal(); return false;">友情链接</a>
          </div>
        </div>
        <!-- Item 4: 伸缩搜索框 (Expandable Navbar Search) -->
        <div class="nav-search-container" id="nav-search-container">
          <button class="nav-search-btn" id="nav-search-btn" aria-label="Search">
            <svg class="search-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
          </button>
          <input type="text" id="nav-search-input" class="nav-search-input" placeholder="输入关键字搜索机场...">
          <div class="hot-search-popup" id="hot-search-popup">
            <span class="hot-search-title">热门搜索：</span>
            <div class="hot-search-tags">
              <span class="hot-tag" onclick="performNavSearch('极连云')">极连云</span>
              <span class="hot-tag" onclick="performNavSearch('边缘节点')">边缘节点</span>
              <span class="hot-tag" onclick="performNavSearch('光年梯')">光年梯</span>
              <span class="hot-tag" onclick="performNavSearch('快狸')">快狸</span>
              <span class="hot-tag" onclick="performNavSearch('速界')">速界</span>
              <span class="hot-tag" onclick="performNavSearch('瞬云')">瞬云</span>
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
  <!-- Hero Section -->
  <section class="hero-section container">
    <h1 class="hero-title">寻找更<span>稳定、安全、高速</span>的专线翻墙体验</h1>
    <p class="hero-subtitle">
      为商务办公、学术研发、多设备网民提供一键式订阅加速。全专线保障，晚高峰拒绝丢包。
    </p>
    <!-- Key Selling Points Badges -->
    <div class="features-badge-container">
      <div class="feature-badge">稳定可靠</div>
      <div class="feature-badge">隐私安全</div>
      <div class="feature-badge">高速带宽</div>
      <div class="feature-badge">高性价比</div>
      <div class="feature-badge">Anycast高速</div>
      <div class="feature-badge">流媒体解锁</div>
      <div class="feature-badge">设备数不限</div>
    </div>
    <!-- Interactive Search Bar -->
    <div class="search-container">
      <input type="text" id="search-input" class="search-input" placeholder="搜索机场、评测、资讯，例如：极连云, 便宜机场, 测速排行...">
      <div class="search-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      </div>
    </div>
  </section>
  <!-- Core Features Highlights -->
  <section class="core-features-section container">
    <div class="core-features-grid">
      <a href="articles/best-airports-2026.html" class="core-feature-card">
        <div class="core-feature-icon">
          <svg viewBox="0 0 24 24"><path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L14 19v-5.5l7 2.5z"/></svg>
        </div>
        <h3 class="core-feature-title">机场推荐</h3>
        <p class="core-feature-desc">2026精选专线机场横向评测，保障极致稳定冲浪体验。</p>
      </a>
      <a href="#" onclick="showLatestNewsModal(); return false;" class="core-feature-card">
        <div class="core-feature-icon">
          <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
        </div>
        <h3 class="core-feature-title">最新资讯</h3>
        <p class="core-feature-desc">实时发布各大机场最新优惠折扣、节点变动与网络资讯。</p>
      </a>
      <a href="articles/subscription-guide.html" class="core-feature-card">
        <div class="core-feature-icon">
          <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10zM12 7c.55 0 1 .45 1 1v4c0 .55-.45 1-1 1s-1-.45-1-1V8c0-.55.45-1 1-1zm1 8h-2v2h2v-2z"/></svg>
        </div>
        <h3 class="core-feature-title">避雷指南</h3>
        <p class="core-feature-desc">新手避坑指南，详解节点协议与订阅购买防跑路常识。</p>
      </a>
      <a href="articles/premium-airports.html" class="core-feature-card">
        <div class="core-feature-icon">
          <svg viewBox="0 0 24 24"><path d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6h-6z"/></svg>
        </div>
        <h3 class="core-feature-title">测速排行</h3>
        <p class="core-feature-desc">晚高峰网络大流量吞吐测速，节点延迟与抗丢包率权威排行。</p>
      </a>
    </div>
  </section>
  <!-- Main Content Layout -->
  <main class="container main-layout" id="articles-feed-section">
    <!-- Left Column: Sidebar -->
    <aside class="sidebar">
      <!-- Widget 0: Profile Card -->
      <div class="sidebar-widget profile-card">
        <div class="profile-header">
          <div class="profile-avatar">
            <svg viewBox="0 0 100 100">
              <defs>
                <linearGradient id="avatar-glow" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#3b82f6" />
                  <stop offset="100%" stop-color="#6366f1" />
                </linearGradient>
              </defs>
              <circle cx="50" cy="50" r="45" fill="url(#avatar-glow)" />
              <path d="M50 20 L65 50 L80 50 L55 60 L60 80 L50 75 L40 80 L45 60 L20 50 L35 50 Z" fill="#fff" />
            </svg>
          </div>
          <h3 class="profile-name">机场速递</h3>
          <span class="profile-domain">jichangspeed.biz</span>
        </div>
        <p class="profile-motto">2026年最新稳定安全高速便宜专线中继机场推荐，专注于为您提供高性价比的科学上网通道。</p>
        <div class="profile-stats">
          <div class="stat-item">
            <span class="stat-num">36</span>
            <span class="stat-label">评测文章</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">16</span>
            <span class="stat-label">热门标签</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">99+</span>
            <span class="stat-label">日均访问</span>
          </div>
        </div>
        <div class="profile-social">
          <a href="https://t.me/psytois_233" target="_blank" title="Telegram 频道" class="social-btn">
            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 0 0-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .24z"/></svg>
          </a>
          <a href="mailto:psytong@outlook.com" title="联系邮箱" class="social-btn">
            <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          </a>
        </div>
      </div>
      <!-- Widget 1: Announcement Card -->
      <div class="sidebar-widget announcement-card">
        <h3 class="widget-title">
          <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-7 9h-2V5h2v6zm0 4h-2v-2h2v2z"/></svg>
          公告栏
        </h3>
        <div class="announcement-content">
          <p>📢 欢迎来到机场速递！</p>
          <p>我们坚持“客观独立测试、长效连通性监测、真实晚高峰测速”的硬核原则，为您排雷和精选稳定、便宜的高端 IPLC/IEPL 专线中继机场订阅官网。</p>
          <p class="announcement-highlight">建议按 Ctrl+D 收藏本站，获取最新机场官网入口！</p>
        </div>
      </div>
      <!-- Widget 2: Popular Airport Tags -->
      <div class="sidebar-widget">
        <h3 class="widget-title">
          <svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 8.25c-.97 0-1.75-.78-1.75-1.75s.78-1.75 1.75-1.75 1.75.78 1.75 1.75S6.47 8.25 5.5 8.25z"/></svg>
          热门标签
        </h3>
        <div class="tags-cloud">
          <a href="#" class="sidebar-tag" data-tag="2026便宜机场">2026便宜机场</a>
          <a href="#" class="sidebar-tag" data-tag="稳定翻墙专线">稳定翻墙专线</a>
          <a href="#" class="sidebar-tag" data-tag="极连云">极连云</a>
          <a href="#" class="sidebar-tag" data-tag="光年梯">光年梯</a>
          <a href="#" class="sidebar-tag" data-tag="边缘节点">边缘</a>
          <a href="#" class="sidebar-tag" data-tag="快狸">快狸</a>
          <a href="#" class="sidebar-tag" data-tag="速界">速界</a>
          <a href="#" class="sidebar-tag" data-tag="瞬云">瞬云</a>
          <a href="#" class="sidebar-tag" data-tag="寰宇云">寰宇云</a>
          <a href="#" class="sidebar-tag" data-tag="光速云">光速云</a>
          <a href="#" class="sidebar-tag" data-tag="全球云">全球云</a>
          <a href="#" class="sidebar-tag" data-tag="Clash节点">Clash节点</a>
          <a href="#" class="sidebar-tag" data-tag="Shadowrocket">Shadowrocket</a>
          <a href="#" class="sidebar-tag" data-tag="V2RayNG">V2RayNG</a>
          <a href="#" class="sidebar-tag" data-tag="IEPL物理专线">IEPL物理专线</a>
          <a href="#" class="sidebar-tag" data-tag="流媒体解锁">流媒体解锁</a>
          <a href="#" class="sidebar-tag" data-tag="ChatGPT机场">ChatGPT机场</a>
          <a href="#" class="sidebar-tag" data-tag="不限时长流量包">不限时长流量包</a>
        </div>
      </div>
      <!-- Widget 3: Featured Articles -->
      <div class="sidebar-widget">
        <h3 class="widget-title">
          <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
          精选文章
        </h3>
        <div class="featured-list">
          <div class="featured-item">
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/tpkZpVhs/sujielogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="速界"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/sujie-review.html">速界 机场评测：不限速不限制设备的高性能 IEPL 节点首选推荐</a></h4>
              <span class="featured-item-date">2026-07-03</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/C5P4QcfT/bianyuanjiedianlogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="边缘节点"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/edge-review.html">边缘节点 机场（EdgeNova）深度评测：无日志与极速数据中转</a></h4>
              <span class="featured-item-date">2026-07-14</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/TxW2rqGj/jilianyunlogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="极连云"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/jilianyun-review.html">极连云 机场测速与评测：高性价比 IEPL 专线推荐</a></h4>
              <span class="featured-item-date">2026-07-18</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/mCYxy3yM/guanniantilogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="光年梯"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/guangnianti-review.html">光年梯 机场评测：稳定解锁流媒体与高可用线路方案</a></h4>
              <span class="featured-item-date">2026-07-16</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/jkR2rZRw/shunyunlogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="瞬云"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/shunyun-review.html">瞬云 机场测速评测：限时特惠年付小包与高带宽 ANYCAST 连接方案</a></h4>
              <span class="featured-item-date">2026-07-06</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/1f4FvF92/kuaililogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="快狸"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/kuaili-review.html">快狸 机场推荐：多设备在线与高性价比备用选择</a></h4>
              <span class="featured-item-date">2026-07-10</span>
            </div>
          </div>
        </div>
      </div></aside>
    <!-- Right Column: Articles Feed -->
    <section class="content-feed">
      <div class="feed-header">
        <h2 class="feed-title">最新专线测速与购买订阅评测</h2>
        <div class="active-filter-indicator" id="active-filter-indicator">
          当前过滤：<span id="filter-label" style="font-weight: 700;">-</span>
          <a href="#" onclick="resetFilters(); return false;" style="margin-left: 8px; text-decoration: underline; cursor: pointer; color: var(--text-muted);">清除</a>
        </div>
      </div>
{cards_html}
    </section>
  </main>
  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <h3 class="footer-brand-title">机场速递</h3>
          <p>jichangspeed.biz 专注于2026年最新高速、便宜、安全专线网络节点测速和评测。我们致力于打破虚假宣传，为您提供真实可靠的极连云、光年梯、边缘节点、快狸、光速云、全球云、瞬云、寰宇云、速界官网订阅入口。</p>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">快捷导航</h4>
          <ul class="footer-links-list">
            <li><a href="articles/cheap-airports.html" class="footer-link">便宜机场推荐</a></li>
            <li><a href="articles/premium-airports.html" class="footer-link">优质机场推荐</a></li>
            <li><a href="articles/kuaili-review.html" class="footer-link">老牌机场推荐</a></li>
            <li><a href="articles/best-airports-2026.html" class="footer-link">精选汇总</a></li>
          </ul>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">推荐列表</h4>
          <ul class="footer-links-list">
            <li><a href="https://haozevpn.jlyvipaff.com/#/?code=pfzRz5dR" target="_blank" class="footer-link">极连云官网 ↗</a></li>
            <li><a href="https://zoio.edgenovaaff.cc/#/?code=Y65i2kCU" target="_blank" class="footer-link">边缘节点官网 ↗</a></li>
            <li><a href="https://hjbesu8d.fazuttt.club/#/?code=AixFrykO" target="_blank" class="footer-link">光年梯官网 ↗</a></li>
            <li><a href="https://iu9asffa.kuailitztz2.sbs/#/?code=tmUe2z1n" target="_blank" class="footer-link">快狸官网 ↗</a></li>
            <li><a href="https://asfweroasf.sujietztz2.xyz/#/?code=C2v7kRVl" target="_blank" class="footer-link">速界官网 ↗</a></li>
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
        <div class="footer-bottom-links">
        </div>
      </div>
    </div>
  </footer>
  <script src="js/main.js?v=20260729"></script>
</body>
</html>
"""
    html = html.replace('{cards_html}', cards_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html written.")
def write_about():
    html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>关于我们 - 机场速递博客 (jichangspeed.biz)</title>
  <!-- SEO Meta Tags -->
  <meta name="description" content="关于机场速递 (jichangspeed.biz) —— 我们的定位、测速准则、核心价值与联系方式。提供极连云、光年梯、边缘节点、快狸、光速云、全球云、瞬云、寰宇云、速界等高品质专线梯子官网入口。">
  <meta name="keywords" content="关于我们, 机场速递, 机场评测, 极连云, 光年梯, 边缘节点, 快狸, 光速云, 全球云, 瞬云, 寰宇云, 速界, jichangspeed.biz">
  <meta name="robots" content="index, follow">
    <!-- Favicon / Site Icons -->
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
  <link rel="stylesheet" href="css/style.css?v=20260731">
  <style>
    /* 强力保证夜间模式下 Logo span 文本显示为清晰的纯白色，不受外部样式缓存影响 */
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
      <a href="index.html" class="logo">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10" fill="var(--accent-primary)" />
          <path d="M12 6L18 13L14 12.5L14.5 17L12 15L9.5 17L10 12.5 L6 13Z" fill="#ffffff" />
        </svg>
        <span>机场速递</span>
      </a>
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">☰</button>
      <nav class="nav" id="nav-menu">
        <a href="index.html" class="nav-link">主页</a>
        <!-- Item 1: 机场推荐 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">机场推荐 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="articles/cheap-airports.html" class="dropdown-item">便宜机场推荐</a>
            <a href="articles/premium-airports.html" class="dropdown-item">优质机场推荐</a>
            <a href="articles/kuaili-review.html" class="dropdown-item">老牌机场推荐</a>
          </div>
        </div>
        <!-- Item 2: 机场资讯 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">机场资讯 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="articles/best-airports-2026.html" class="dropdown-item">精选汇总</a>
            <a href="vpn-guide.html" class="dropdown-item">科普专栏</a>
          </div>
        </div>
        <!-- Item 3: 更多 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">更多 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="archives.html" class="dropdown-item">文章归档</a>
            <a href="about.html" class="dropdown-item">关于我们</a>
            <a href="#" class="dropdown-item" onclick="showFriendsModal(); return false;">友情链接</a>
          </div>
        </div>
        <!-- Item 4: 伸缩搜索框 (Expandable Navbar Search) -->
        <div class="nav-search-container" id="nav-search-container">
          <button class="nav-search-btn" id="nav-search-btn" aria-label="Search">
            <svg class="search-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
          </button>
          <input type="text" id="nav-search-input" class="nav-search-input" placeholder="输入关键字搜索机场...">
          <div class="hot-search-popup" id="hot-search-popup">
            <span class="hot-search-title">热门搜索：</span>
            <div class="hot-search-tags">
              <span class="hot-tag" onclick="performNavSearch('极连云')">极连云</span>
              <span class="hot-tag" onclick="performNavSearch('边缘节点')">边缘节点</span>
              <span class="hot-tag" onclick="performNavSearch('光年梯')">光年梯</span>
              <span class="hot-tag" onclick="performNavSearch('快狸')">快狸</span>
              <span class="hot-tag" onclick="performNavSearch('速界')">速界</span>
              <span class="hot-tag" onclick="performNavSearch('瞬云')">瞬云</span>
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
  <!-- About Content -->
  <main class="container article-page">
    <div class="breadcrumbs">
      <a href="index.html">首页</a>
      <svg viewBox="0 0 24 24" style="width:12px; height:12px; fill:currentColor;"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <span>关于我们</span>
    </div>
    <div class="main-layout">
      <!-- Left Column -->
      <article class="content-feed">
        <div class="article-header">
          <h1 class="article-title-large">关于“机场速递”博客</h1>
        </div>
        <div class="article-body">
          <p>欢迎来到 <strong>机场速递 (jichangspeed.biz)</strong>。我们是一个专注于网络技术交流、加速网络优化、以及优质专线网络服务评测的独立媒体。</p>
          <h2>一、我们的使命</h2>
          <p>安全、高速、平稳地获取海外学术信息与商用数据是每一位开发者、设计师、跨境电商以及外贸从业者的刚需。我们致力于通过真实、透明的评估测试，为您提供真实可靠的极连云、光年梯、边缘节点、快狸、光速云、全球云、瞬云、寰宇云、速界官网订阅入口。</p>
          <p><em>声明：本站所有评测文章及教程仅供网络安全技术交流、学术研究与跨境合法商务使用，请严格遵守当地法律法规，切勿用于非法用途。</em></p>
        </div>
      </article>
      <!-- Right Column: Sidebar -->
      <aside class="sidebar">
        <!-- Sidebar Tag Widget -->
        <div class="sidebar-widget">
          <h3 class="widget-title">
            <svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 8.25c-.97 0-1.75-.78-1.75-1.75s.78-1.75 1.75-1.75 1.75.78 1.75 1.75S6.47 8.25 5.5 8.25z"/></svg>
            热门标签
          </h3>
          <div class="tags-cloud">
            <a href="index.html?tag=%E6%9C%BA%E5%9C%BA%E8%AF%84%E6%B5%8B" class="sidebar-tag">机场评测</a>
            <a href="index.html?tag=%E4%B8%8D%E9%99%90%E6%97%B6%E9%95%BF" class="sidebar-tag">不限时长</a>
            <a href="index.html?tag=%E7%A7%91%E5%AD%A6%E4%B8%8B%E8%BD%BD" class="sidebar-tag">科学下载</a>
            <a href="index.html?tag=%E6%9C%80%E6%96%B0%E8%8A%82%E7%82%B9%E5%88%86%E4%BA%AB" class="sidebar-tag">最新节点分享</a>
            <a href="index.html?tag=%E5%85%8D%E8%B4%B9vpn" class="sidebar-tag">免费vpn</a>
            <a href="index.html?tag=%E4%B8%8D%E9%99%90%E6%97%B6%E9%95%BF" class="sidebar-tag">一键翻墙</a>
            <a href="index.html?tag=%E5%A6%82%E4%BD%95%E8%AE%A2%E9%98%85%E8%B4%AD%E4%B9%B0" class="sidebar-tag">如何订阅购买</a>
            <a href="index.html?tag=%E6%9E%81%E8%BF%9E%E4%BA%91" class="sidebar-tag">极连云</a>
            <a href="index.html?tag=%E5%85%8D%E8%B4%B9vpn" class="sidebar-tag">光年梯</a>
            <a href="index.html?tag=%E8%BE%B9%E7%BC%98%E8%8A%82%E7%82%B9" class="sidebar-tag">边缘</a>
            <a href="index.html?tag=%E5%BF%AB%E7%8B%B8" class="sidebar-tag">快狸</a>
            <a href="index.html?tag=%E5%85%85%E5%80%BC" class="sidebar-tag">光速云</a>
            <a href="index.html?tag=%E5%A5%8D" class="sidebar-tag">全球云</a>
            <a href="index.html?tag=%E7%9E%AC%E4%BA%91" class="sidebar-tag">瞬云</a>
            <a href="index.html?tag=%E5%AF%B5%E5%AE%87%E4%BA%91" class="sidebar-tag">寰宇云</a>
            <a href="index.html?tag=%E9%80%9F%E7%95%8C" class="sidebar-tag">速界</a>
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
          <p>jichangspeed.biz 专注于2026年最新高速、便宜、安全专线网络节点测速和评测。我们致力于为用户提供真实可靠的极连云、光年梯、边缘节点、快狸、光速云、全球云、瞬云、寰宇云、速界官网订阅入口。</p>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">快捷导航</h4>
          <ul class="footer-links-list">
            <li><a href="articles/cheap-airports.html" class="footer-link">便宜机场推荐</a></li>
            <li><a href="articles/premium-airports.html" class="footer-link">优质机场推荐</a></li>
            <li><a href="articles/kuaili-review.html" class="footer-link">老牌机场推荐</a></li>
            <li><a href="articles/best-airports-2026.html" class="footer-link">精选汇总</a></li>
          </ul>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">推荐列表</h4>
          <ul class="footer-links-list">
            <li><a href="{links['极连云']}" target="_blank" class="footer-link">极连云官网 ↗</a></li>
            <li><a href="{links['边缘节点']}" target="_blank" class="footer-link">边缘节点官网 ↗</a></li>
            <li><a href="{links['光年梯']}" target="_blank" class="footer-link">光年梯官网 ↗</a></li>
            <li><a href="{links['快狸']}" target="_blank" class="footer-link">快狸官网 ↗</a></li>
            <li><a href="{links['速界']}" target="_blank" class="footer-link">速界官网 ↗</a></li>
            <li><a href="{links['瞬云']}" target="_blank" class="footer-link">瞬云官网 ↗</a></li>
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
  <script src="js/main.js?v=20260729"></script>
</body>
</html>
"""
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("about.html written.")
def write_vpn_guide():
    global science_list
    science_articles_html = ""
    for s in science_list:
        science_articles_html += f"""            <a href=\"articles/{s['slug']}.html\" style=\"display: flex; justify-content: space-between; align-items: center; text-decoration: none; padding: 12px 16px; background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: var(--radius-md); transition: all 0.2s;\" onmouseover=\"this.style.borderColor='var(--accent-primary)';\" onmouseout=\"this.style.borderColor='var(--border-color)';\">
              <span style=\"font-size: 0.92rem; font-weight: 600; color: var(--text-primary);\">{s['title']}</span>
              <span style=\"font-size: 0.78rem; color: var(--text-muted); flex-shrink: 0; margin-left: 10px;\">📅 {s['date']}</span>
            </a>
"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>网络订阅配置与下载指南 - 机场速递博客 (jichangspeed.biz)</title>
  <!-- SEO Meta Tags -->
  <meta name="description" content="科普专栏配置购买一站式指南。涵盖电脑客户端、安卓客户端与iOS苹果客户端下载与通用一键订阅导入教程，推荐使用极连云、光年梯、边缘节点、快狸、光速云、全球云、瞬云、寰宇云、速界官网订阅服务。">
  <meta name="keywords" content="配置配置, 订阅下载, 客户端导入, 极连云, 光年梯, 边缘节点, 快狸, 光速云, 全球云, 瞬云, 寰宇云, 速界, jichangspeed.biz">
  <meta name="robots" content="index, follow">
    <!-- Favicon / Site Icons -->
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
  <link rel="stylesheet" href="css/style.css?v=20260731">
  <style>
    /* 强力保证夜间模式下 Logo span 文本显示为清晰的纯白色，不受外部样式缓存影响 */
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
      <a href="index.html" class="logo">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10" fill="var(--accent-primary)" />
          <path d="M12 6L18 13L14 12.5L14.5 17L12 15L9.5 17L10 12.5 L6 13Z" fill="#ffffff" />
        </svg>
        <span>机场速递</span>
      </a>
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">☰</button>
      <nav class="nav" id="nav-menu">
        <a href="index.html" class="nav-link">主页</a>
        <!-- Item 1: 机场推荐 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">机场推荐 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="articles/cheap-airports.html" class="dropdown-item">便宜机场推荐</a>
            <a href="articles/premium-airports.html" class="dropdown-item">优质机场推荐</a>
            <a href="articles/kuaili-review.html" class="dropdown-item">老牌机场推荐</a>
          </div>
        </div>
        <!-- Item 2: 机场资讯 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">机场资讯 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="articles/best-airports-2026.html" class="dropdown-item">精选汇总</a>
            <a href="vpn-guide.html" class="dropdown-item">科普专栏</a>
          </div>
        </div>
        <!-- Item 3: 更多 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">更多 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="archives.html" class="dropdown-item">文章归档</a>
            <a href="about.html" class="dropdown-item">关于我们</a>
            <a href="#" class="dropdown-item" onclick="showFriendsModal(); return false;">友情链接</a>
          </div>
        </div>
        <!-- Item 4: 伸缩搜索框 (Expandable Navbar Search) -->
        <div class="nav-search-container" id="nav-search-container">
          <button class="nav-search-btn" id="nav-search-btn" aria-label="Search">
            <svg class="search-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
          </button>
          <input type="text" id="nav-search-input" class="nav-search-input" placeholder="输入关键字搜索机场...">
          <div class="hot-search-popup" id="hot-search-popup">
            <span class="hot-search-title">热门搜索：</span>
            <div class="hot-search-tags">
              <span class="hot-tag" onclick="performNavSearch('极连云')">极连云</span>
              <span class="hot-tag" onclick="performNavSearch('边缘节点')">边缘节点</span>
              <span class="hot-tag" onclick="performNavSearch('光年梯')">光年梯</span>
              <span class="hot-tag" onclick="performNavSearch('快狸')">快狸</span>
              <span class="hot-tag" onclick="performNavSearch('速界')">速界</span>
              <span class="hot-tag" onclick="performNavSearch('瞬云')">瞬云</span>
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
  <!-- Content -->
  <main class="container article-page">
    <div class="breadcrumbs">
      <a href="index.html">首页</a>
      <svg viewBox="0 0 24 24" style="width:12px; height:12px; fill:currentColor;"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <span>科普专栏</span>
    </div>
    <div class="main-layout">
      <!-- Left Column: Setup Guide -->
      <article class="content-feed">
        <div class="article-header">
          <h1 class="article-title-large">机场科普与高速网络优化专栏简介</h1>
        </div>
        <div class="article-body">
          <p>欢迎来到<strong>科普专栏</strong>。本专栏致力于为广大网络用户提供2026年最新、最客观的国际高速网络技术科普，详细解析各种主流网络代理协议（如 VLESS、Reality、Hysteria2、Tuic 等）与网络架构（IPLC专线、IEPL中转、BGP中转）的底层原理。帮助您避开计费流量倍率陷阱、防范不良服务商跑路风控，实现安全、顺畅的全球商务办公 and 日常娱乐冲浪。</p>
          <div style="background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 20px; margin: 25px 0;">
            <h3 style="margin-top: 0; color: var(--accent-primary); font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="stroke-linecap: round; stroke-linejoin: round;"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
              优质网络服务商（机场）精选推荐
            </h3>
            <p style="font-size: 0.9rem; line-height: 1.6; margin-bottom: 12px;">为了方便大家快速接入安全稳定的加速网络，我们根据各大服务商的晚高峰连通率、延迟 and 丢包实测，向您进行如下精选推荐（点击对应名称即可直接访问官网）：</p>
            <ul style="font-size: 0.9rem; line-height: 1.7; padding-left: 20px; margin-bottom: 0; list-style-type: none;">
              <li style="margin-bottom: 10px;">🌟 <strong><a href="https://haozevpn.jlyvipaff.com/#/?code=pfzRz5dR" target="_blank" style="color: var(--accent-primary); font-weight: 700; text-decoration: underline;">极连云官网 ↗</a></strong>：全系部署 IEPL 企业级物理私网，香港物理延迟低至 18ms，晚高峰 100% 连通不卡顿，且全节点均为 1 倍率实在计费，流媒体完美解锁，是高端商务办公、低延迟游戏加速与会议的不二选择。</li>
              <li style="margin-bottom: 10px;">🌟 <strong><a href="https://asfweroasf.sujietztz2.xyz/#/?code=C2v7kRVl" target="_blank" style="color: var(--accent-primary); font-weight: 700; text-decoration: underline;">速界官网 ↗</a></strong>：高性价比首选，提供仅 ¥15.00/月起的首月体验包，且年付套餐低至 90 元（结合开业8折特惠折合低至 6.00元/月！）。不仅全节点 1 倍率，且完全不限在线客户端设备数，提供极其简便的一键连接软件，极其适合轻度及多设备共享用户。</li>
              <li style="margin-bottom: 10px;">🌟 <strong><a href="https://hjbesu8d.fazuttt.club/#/?code=AixFrykO" target="_blank" style="color: var(--accent-primary); font-weight: 700; text-decoration: underline;">光年梯官网 ↗</a></strong>：提供极高稳定性的物理多路由中继，全专线互联，流媒体 Netflix/Disney+ 和 AI 软件（ChatGPT/Claude）通过率达到 100%，套餐配置丰富灵活。</li>
              <li style="margin-bottom: 0;">🌟 <strong><a href="https://iu9asffa.kuailitztz2.sbs/#/?code=tmUe2z1n" target="_blank" style="color: var(--accent-primary); font-weight: 700; text-decoration: underline;">快狸官网 ↗</a></strong>：老牌高稳定服务商，支持灵活月付方案（15元/月起），节点遍布全球主要核心区域，线路高可用 Anycast 容灾，备用及主力均非常扎实。</li>
            </ul>
          </div>
          <p>在了解并订阅了心仪的网络节点后，如果您在使用客户端（如 Clash、Shadowrocket、V2RayNG 等）或者配置软路由时遇到任何问题，欢迎深入翻阅本专栏下方的 {len(science_list)} 篇专业科普与配置指南：</p>
        </div>
          <h2 style="margin-top: 30px;">三、科普专栏深度科普与配置教程</h2>
          <p>以下为您精选的 {len(science_list)} 篇网络加速深度科普文章与客户端配置教程，帮助您更加深入地了解协议机制与安全翻墙防坑常识：</p>
          <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 15px; margin-bottom: 25px;">
{science_articles_html}          </div>
      </article>
      <!-- Right Column: Sidebar -->
      <aside class="sidebar">
        <!-- Sidebar Tag Widget -->
        <div class="sidebar-widget">
          <h3 class="widget-title">
            <svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 8.25c-.97 0-1.75-.78-1.75-1.75s.78-1.75 1.75-1.75 1.75.78 1.75 1.75S6.47 8.25 5.5 8.25z"/></svg>
            热门标签
          </h3>
          <div class="tags-cloud">
            <a href="index.html?tag=%E6%9C%BA%E5%9C%BA%E8%AF%84%E6%B5%8B" class="sidebar-tag">机场评测</a>
            <a href="index.html?tag=%E4%B8%8D%E9%99%90%E6%97%B6%E9%95%BF" class="sidebar-tag">不限时长</a>
            <a href="index.html?tag=%E7%A7%91%E5%AD%A6%E4%B8%8B%E8%BD%BD" class="sidebar-tag">科学下载</a>
            <a href="index.html?tag=%E6%9C%80%E6%96%B0%E8%8A%82%E7%82%B9%E5%88%86%E4%BA%AB" class="sidebar-tag">最新节点分享</a>
            <a href="index.html?tag=%E5%85%8D%E8%B4%B9vpn" class="sidebar-tag">免费vpn</a>
            <a href="index.html?tag=%E4%B8%8D%E9%99%90%E6%97%B6%E9%95%BF" class="sidebar-tag">一键翻墙</a>
            <a href="index.html?tag=%E5%A6%82%E4%BD%95%E8%AE%A2%E9%98%85%E8%B4%AD%E4%B9%B0" class="sidebar-tag">如何订阅购买</a>
            <a href="index.html?tag=%E6%9E%81%E8%BF%9E%E4%BA%91" class="sidebar-tag">极连云</a>
            <a href="index.html?tag=%E5%85%8D%E8%B4%B9vpn" class="sidebar-tag">光年梯</a>
            <a href="index.html?tag=%E8%BE%B9%E7%BC%98%E8%8A%82%E7%82%B9" class="sidebar-tag">边缘</a>
            <a href="index.html?tag=%E5%BF%AB%E7%8B%B8" class="sidebar-tag">快狸</a>
            <a href="index.html?tag=%E5%85%85%E5%80%BC" class="sidebar-tag">光速云</a>
            <a href="index.html?tag=%E5%A5%8D" class="sidebar-tag">全球云</a>
            <a href="index.html?tag=%E7%9E%AC%E4%BA%91" class="sidebar-tag">瞬云</a>
            <a href="index.html?tag=%E5%AF%B5%E5%AE%87%E4%BA%91" class="sidebar-tag">寰宇云</a>
            <a href="index.html?tag=%E9%80%9F%E7%95%8C" class="sidebar-tag">速界</a>
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
          <p>jichangspeed.biz 专注于2026年最新高速、便宜、安全专线网络节点测速和评测。我们致力于为用户提供真实可靠的极连云、光年梯、边缘节点、快狸、光速云、全球云, 瞬云、寰宇云、速界官网订阅入口。</p>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">快捷导航</h4>
          <ul class="footer-links-list">
            <li><a href="articles/cheap-airports.html" class="footer-link">便宜机场推荐</a></li>
            <li><a href="articles/premium-airports.html" class="footer-link">优质机场推荐</a></li>
            <li><a href="articles/kuaili-review.html" class="footer-link">老牌机场推荐</a></li>
            <li><a href="articles/best-airports-2026.html" class="footer-link">精选汇总</a></li>
          </ul>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">推荐列表</h4>
          <ul class="footer-links-list">
            <li><a href="https://haozevpn.jlyvipaff.com/#/?code=pfzRz5dR" target="_blank" class="footer-link">极连云官网 ↗</a></li>
            <li><a href="https://zoio.edgenovaaff.cc/#/?code=Y65i2kCU" target="_blank" class="footer-link">边缘节点官网 ↗</a></li>
            <li><a href="https://hjbesu8d.fazuttt.club/#/?code=AixFrykO" target="_blank" class="footer-link">光年梯官网 ↗</a></li>
            <li><a href="https://iu9asffa.kuailitztz2.sbs/#/?code=tmUe2z1n" target="_blank" class="footer-link">快狸官网 ↗</a></li>
            <li><a href="https://asfweroasf.sujietztz2.xyz/#/?code=C2v7kRVl" target="_blank" class="footer-link">速界官网 ↗</a></li>
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
  <script src="js/main.js?v=20260729"></script>
</body>
</html>
"""
    with open('vpn-guide.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("vpn-guide.html written.")
def write_sitemap():
    from generate_final_site import article_list
    global science_list
    all_articles = [a['slug'] for a in article_list] + [s['slug'] for s in science_list]
    articles_nodes = ""
    for slug in all_articles:
        articles_nodes += f"""  <url>
    <loc>https://jichangspeed.biz/articles/{slug}.html</loc>
    <lastmod>2026-07-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://jichangspeed.biz/</loc>
    <lastmod>2026-07-24</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/about.html</loc>
    <lastmod>2026-07-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/vpn-guide.html</loc>
    <lastmod>2026-07-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/archives.html</loc>
    <lastmod>2026-07-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
{articles_nodes}</urlset>
"""
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml)
    print("sitemap.xml written.")
def write_archives():
    from generate_final_site import article_list
    global science_list
    # 将原有 article_list 转化为可以和 science_list 混合拼接的普通 dict 格式
    formatted_articles = []
    for a in article_list:
        formatted_articles.append({
            'slug': a['slug'],
            'title': a['title'],
            'date': a['date']
        })
    merged_list = formatted_articles + science_list
    sorted_articles = sorted(merged_list, key=lambda x: x['date'], reverse=True)
    articles_by_year = {}
    for a in sorted_articles:
        year = a['date'].split('-')[0]
        if year not in articles_by_year:
            articles_by_year[year] = []
        articles_by_year[year].append(a)
    year_blocks_html = ""
    for year in sorted(articles_by_year.keys(), reverse=True):
        year_articles = articles_by_year[year]
        count = len(year_articles)
        items_html = ""
        for a in year_articles:
            date_mm_dd = "-".join(a['date'].split('-')[1:])
            link_path = f"articles/{a['slug']}.html"
            items_html += f"""
          <div class="archive-item">
            <a href="{link_path}" class="archive-item-title">{a['title']}</a>
            <span class="archive-item-date">{date_mm_dd}</span>
          </div>"""
        year_blocks_html += f"""
        <div class="archive-year-section">
          <div class="archive-year-header">
            <span class="archive-year-title">{year}</span>
            <span class="archive-year-count">{count} 篇</span>
          </div>
          <div class="archive-items-list">
            {items_html}
          </div>
        </div>"""
    total_count = len(merged_list)
    html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>文章归档 - 机场速递博客 (jichangspeed.biz)</title>
  <!-- SEO Meta Tags -->
  <meta name="description" content="文章归档页面包含机场速递 (jichangspeed.biz) 全站所有机场测速、便宜机场推荐、优质专线机场评测文章时间线列表。">
  <meta name="keywords" content="文章归档, 机场测速, 极连云, 光年梯, 边缘节点, 快狸, 瞬云, 寰宇云, 速界">
  <meta name="robots" content="index, follow">
    <!-- Favicon / Site Icons -->
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
  <link rel="stylesheet" href="css/style.css?v=20260731">
  <style>
    /* 强力保证夜间模式下 Logo span 文本显示为清晰的纯白色，不受外部样式缓存影响 */
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
      <a href="index.html" class="logo">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10" fill="var(--accent-primary)" />
          <path d="M12 6L18 13L14 12.5L14.5 17L12 15L9.5 17L10 12.5 L6 13Z" fill="#ffffff" />
        </svg>
        <span>机场速递</span>
      </a>
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">☰</button>
      <nav class="nav" id="nav-menu">
        <a href="index.html" class="nav-link">主页</a>
        <!-- Item 1: 机场推荐 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">机场推荐 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="articles/cheap-airports.html" class="dropdown-item">便宜机场推荐</a>
            <a href="articles/premium-airports.html" class="dropdown-item">优质机场推荐</a>
            <a href="articles/kuaili-review.html" class="dropdown-item">老牌机场推荐</a>
          </div>
        </div>
        <!-- Item 2: 机场资讯 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">机场资讯 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="articles/best-airports-2026.html" class="dropdown-item">精选汇总</a>
            <a href="vpn-guide.html" class="dropdown-item">科普专栏</a>
          </div>
        </div>
        <!-- Item 3: 更多 (Dropdown) -->
        <div class="nav-item dropdown">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">更多 <svg class="chevron-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="archives.html" class="dropdown-item">文章归档</a>
            <a href="about.html" class="dropdown-item">关于我们</a>
            <a href="#" class="dropdown-item" onclick="showFriendsModal(); return false;">友情链接</a>
          </div>
        </div>
        <!-- Item 4: 伸缩搜索框 (Expandable Navbar Search) -->
        <div class="nav-search-container" id="nav-search-container">
          <button class="nav-search-btn" id="nav-search-btn" aria-label="Search">
            <svg class="search-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
          </button>
          <input type="text" id="nav-search-input" class="nav-search-input" placeholder="输入关键字搜索机场...">
          <div class="hot-search-popup" id="hot-search-popup">
            <span class="hot-search-title">热门搜索：</span>
            <div class="hot-search-tags">
              <span class="hot-tag" onclick="performNavSearch('极连云')">极连云</span>
              <span class="hot-tag" onclick="performNavSearch('边缘节点')">边缘节点</span>
              <span class="hot-tag" onclick="performNavSearch('光年梯')">光年梯</span>
              <span class="hot-tag" onclick="performNavSearch('快狸')">快狸</span>
              <span class="hot-tag" onclick="performNavSearch('速界')">速界</span>
              <span class="hot-tag" onclick="performNavSearch('瞬云')">瞬云</span>
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
  <!-- Archives Page Main Layout -->
  <main class="container article-page main-layout" id="archives-layout-section" style="margin-top: 40px;">
    <!-- Left Column: Archive list -->
    <article class="content-feed archive-box">
      {year_blocks_html}
    </article>
    <!-- Right Column: Sidebar -->
    <aside class="sidebar">
      <!-- Profile Card -->
      <div class="sidebar-widget profile-card">
        <div class="profile-header">
          <div class="profile-avatar">
            <svg viewBox="0 0 100 100">
              <defs>
                <linearGradient id="avatar-glow-archive" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#3b82f6" />
                  <stop offset="100%" stop-color="#6366f1" />
                </linearGradient>
              </defs>
              <circle cx="50" cy="50" r="45" fill="url(#avatar-glow-archive)" />
              <path d="M50 20 L65 50 L80 50 L55 60 L60 80 L50 75 L40 80 L45 60 L20 50 L35 50 Z" fill="#fff" />
            </svg>
          </div>
          <h3 class="profile-name">机场速递</h3>
          <span class="profile-domain">jichangspeed.biz</span>
        </div>
        <p class="profile-motto">2026年最新稳定安全高速便宜专线中继机场推荐，专注于为您提供高性价比的科学上网通道。</p>
        <div class="profile-stats">
          <div class="stat-item">
            <span class="stat-num">36</span>
            <span class="stat-label">评测文章</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">16</span>
            <span class="stat-label">热门标签</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">99+</span>
            <span class="stat-label">日均访问</span>
          </div>
        </div>
        <!-- Social Icons -->
        <div class="profile-social">
          <a href="https://t.me/psytois_233" target="_blank" class="social-btn" aria-label="Telegram">
            <svg viewBox="0 0 24 24"><path d="M9.78 18.65l.28-4.28 7.68-6.92c.34-.3-.07-.46-.52-.18L7.69 12.3 3.58 11c-.9-.28-.9-.9.18-1.32L19.9 3.5c.73-.28 1.38.18 1.14 1.3l-2.76 13.52c-.22 1.02-.83 1.27-1.7.77l-4.22-3.18-2.03 2.04c-.22.22-.4.4-.75.4z"/></svg>
          </a>
          <a href="mailto:psytong@outlook.com" class="social-btn" aria-label="Email">
            <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          </a>
        </div>
      </div>
      <!-- Quick Directory Navigation Button widget -->
      <div class="sidebar-widget nav-shortcuts-card">
        <div class="shortcuts-grid">
          <a href="index.html" class="shortcut-item">
            <svg class="shortcut-icon" viewBox="0 0 24 24"><path d="M17.63 5.84C17.27 5.33 16.67 5 16 5L5 5.01C3.9 5.01 3 5.9 3 7v10c0 1.1.9 1.99 2 1.99L16 19c.67 0 1.27-.33 1.63-.84L22 12l-4.37-6.16z"/></svg>
            <span class="shortcut-label">标签</span>
          </a>
          <a href="index.html#articles-feed-section" class="shortcut-item">
            <svg class="shortcut-icon" viewBox="0 0 24 24"><path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"/></svg>
            <span class="shortcut-label">分类</span>
          </a>
          <a href="archives.html" class="shortcut-item active">
            <svg class="shortcut-icon" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
            <span class="shortcut-label">归档</span>
          </a>
        </div>
      </div>
    </aside>
  </main>
  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <h3 class="footer-brand-title">机场速递</h3>
          <p>jichangspeed.biz 专注于2026年最新高速、便宜、安全专线网络节点测速和评测。我们致力于为用户提供真实可靠的极连云、光年梯、边缘节点、快狸、光速云、全球云、瞬云、寰宇云、速界官网订阅入口。</p>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">快捷导航</h4>
          <ul class="footer-links-list">
            <li><a href="articles/cheap-airports.html" class="footer-link">便宜机场推荐</a></li>
            <li><a href="articles/premium-airports.html" class="footer-link">优质机场推荐</a></li>
            <li><a href="articles/kuaili-review.html" class="footer-link">老牌机场推荐</a></li>
            <li><a href="articles/best-airports-2026.html" class="footer-link">精选汇总</a></li>
          </ul>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">推荐列表</h4>
          <ul class="footer-links-list">
            <li><a href="{links['极连云']}" target="_blank" class="footer-link">极连云官网 ↗</a></li>
            <li><a href="{links['边缘节点']}" target="_blank" class="footer-link">边缘节点官网 ↗</a></li>
            <li><a href="{links['光年梯']}" target="_blank" class="footer-link">光年梯官网 ↗</a></li>
            <li><a href="{links['快狸']}" target="_blank" class="footer-link">快狸官网 ↗</a></li>
            <li><a href="{links['速界']}" target="_blank" class="footer-link">速界官网 ↗</a></li>
            <li><a href="{links['瞬云']}" target="_blank" class="footer-link">瞬云官网 ↗</a></li>
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
        <div class="footer-bottom-links">
        </div>
      </div>
    </div>
  </footer>
  <script src="js/main.js?v=20260729"></script>
</body>
</html>"""
    with open('archives.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("archives.html written.")
if __name__ == '__main__':
    write_index()
    write_about()
    write_vpn_guide()
    write_archives()
    write_sitemap()
    print("All final parent pages generated successfully!")
