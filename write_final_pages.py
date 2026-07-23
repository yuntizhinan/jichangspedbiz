# -*- coding: utf-8 -*-
import os

links = {
    '极连云': 'https://ugewe.jilianat.homes/#/?code=9ygBtCN8',
    '光年梯': 'https://hjbesu8d.fazuttt.club/#/?code=AixFrykO',
    '边缘': 'https://asfeoasf.bianyuntztz2.cyou/#/?code=Y65i2kCU',
    '快狸': 'https://iu9asffa.kuailitztz2.sbs/#/?code=tmUe2z1n',
    '光速云': 'https://kjlq01.gsyvipaff.cc/#/?code=b1OTkTeL',
    '全球云': 'https://haozevpn.gcvipaff.cc/#/?code=WRQJc2v4',
    '瞬云': 'https://aaa.jichang.best/#/register?code=ClNa0zPm',
    '寰宇云': 'https://vip3.huanyuyunbest.com/#/register?code=K6h5VWw2',
    '速界': 'https://asfweroasf.sujietztz2.xyz/#/?code=C2v7kRVl'
}

def write_index():
    html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>机场速递 (jichangspeed.biz) - 2026稳定安全高速便宜机场推荐与官网订阅评测</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="机场速递 (jichangspeed.biz) 专注于2026年最新稳定、安全、高速、便宜、高性价比机场推荐。提供极连云、光年梯、边缘、快狸、光速云、全球云、瞬云、寰宇云、速界等官网入口。">
  <meta name="keywords" content="极连云, 光年梯, 边缘, 快狸, 光速云, 全球云, 瞬云, 寰宇云, 速界, 机场推荐, 稳定机场, 安全翻墙, 高速中转, jichangspeed.biz">
  <meta name="robots" content="index, follow">
  
  <!-- GEO Tags -->
  <meta name="geo.region" content="CN-GD" />
  <meta name="geo.placename" content="Guangdong" />
  <meta name="geo.position" content="23.12908;113.26436" />
  <meta name="ICBM" content="23.12908, 113.26436" />
  
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <!-- Header -->
  <header class="header">
    <div class="container header-container">
      <a href="index.html" class="logo" onclick="resetFilters(); return false;">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M12 22V12M12 12L4 7.5M12 12l8-4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>机场速递</span>
      </a>
      
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">☰</button>
      
      <nav class="nav" id="nav-menu">
        <a href="articles/cheap-airports.html" class="nav-link">便宜机场推荐</a>
        <a href="articles/premium-airports.html" class="nav-link">优质机场推荐</a>
        <a href="articles/kuaili-review.html" class="nav-link">老牌机场推荐</a>
        <a href="articles/best-airports-2026.html" class="nav-link">精选汇总</a>
        <a href="vpn-guide.html" class="nav-link">科学上网</a>
        <a href="about.html" class="nav-link">关于我们</a>
        
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
      <input type="text" id="search-input" class="search-input" placeholder="输入关键字搜索，例如：极连云, 光年梯, 边缘, 快狸, 光速云, 全球云, 瞬云, 寰宇云, 速界...">
      <div class="search-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      </div>
    </div>
  </section>

  <!-- Core Features Highlights -->
  <section class="core-features-section container">
    <div class="core-features-grid">
      <div class="core-feature-card">
        <div class="core-feature-icon">🚀</div>
        <h3 class="core-feature-title">IEPL/IPLC 物理专线</h3>
        <p class="core-feature-desc">绕过公共网络拥堵，端到端延迟低且不惧特殊时期阻断。</p>
      </div>
      <div class="core-feature-card">
        <div class="core-feature-icon">🛡️</div>
        <h3 class="core-feature-title">自研一键连接</h3>
        <p class="core-feature-desc">边缘与快狸提供专用定制客户端，免去繁琐配置，一键起飞。</p>
      </div>
      <div class="core-feature-card">
        <div class="core-feature-icon">💰</div>
        <h3 class="core-feature-title">极致高性价比</h3>
        <p class="core-feature-desc">月付最低 15 元起，年付折合每月仅需几元，体验高规格加速。</p>
      </div>
      <div class="core-feature-card">
        <div class="core-feature-icon">💻</div>
        <h3 class="core-feature-title">多终端不限设备</h3>
        <p class="core-feature-desc">极连云、光速云、寰宇云、速界等套餐不限制同时在线设备，共享超值。</p>
      </div>
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
            <span class="stat-num">13</span>
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
          <a href="https://t.me/yuntizhinan" target="_blank" title="Telegram 频道" class="social-btn">
            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 0 0-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .24z"/></svg>
          </a>
          <a href="mailto:support@jichangspeed.biz" title="联系邮箱" class="social-btn">
            <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          </a>
          <a href="sitemap.xml" title="网站地图" class="social-btn">
            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
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
          <a href="#" class="sidebar-tag" data-tag="机场评测">机场评测</a>
          <a href="#" class="sidebar-tag" data-tag="不限时长">不限时长</a>
          <a href="#" class="sidebar-tag" data-tag="科学下载">科学下载</a>
          <a href="#" class="sidebar-tag" data-tag="最新节点分享">最新节点分享</a>
          <a href="#" class="sidebar-tag" data-tag="免费vpn">免费vpn</a>
          <a href="#" class="sidebar-tag" data-tag="一键翻墙">一键翻墙</a>
          <a href="#" class="sidebar-tag" data-tag="如何订阅购买">如何订阅购买</a>
          <a href="#" class="sidebar-tag" data-tag="极连云">极连云</a>
          <a href="#" class="sidebar-tag" data-tag="光年梯">光年梯</a>
          <a href="#" class="sidebar-tag" data-tag="边缘">边缘</a>
          <a href="#" class="sidebar-tag" data-tag="快狸">快狸</a>
          <a href="#" class="sidebar-tag" data-tag="光速云">光速云</a>
          <a href="#" class="sidebar-tag" data-tag="全球云">全球云</a>
          <a href="#" class="sidebar-tag" data-tag="瞬云">瞬云</a>
          <a href="#" class="sidebar-tag" data-tag="寰宇云">寰宇云</a>
          <a href="#" class="sidebar-tag" data-tag="速界">速界</a>
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
            <div class="featured-item-img" style="background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:800; font-size:0.75rem; font-family:'Outfit';">JL</div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/jilianyun-review.html">极连云 机场测速与评测：高性价比 IEPL 专线推荐</a></h4>
              <span class="featured-item-date">2026-07-18</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:800; font-size:0.75rem; font-family:'Outfit';">GN</div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/guangnianti-review.html">光年梯 机场评测：稳定解锁流媒体与高可用线路方案</a></h4>
              <span class="featured-item-date">2026-07-16</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:800; font-size:0.75rem; font-family:'Outfit';">SJ</div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/sujie-review.html">速界 机场评测：不限速不限制设备的高性能 IEPL 节点首选推荐</a></h4>
              <span class="featured-item-date">2026-07-03</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: linear-gradient(135deg, #a855f7 0%, #9333ea 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:800; font-size:0.75rem; font-family:'Outfit';">SY</div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/shunyun-review.html">瞬云 机场测速评测：限时特惠年付小包与高带宽 ANYCAST 连接方案</a></h4>
              <span class="featured-item-date">2026-07-06</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: linear-gradient(135deg, #059669 0%, #047857 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:800; font-size:0.75rem; font-family:'Outfit';">HY</div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="articles/huanyuyun-review.html">寰宇云 机场评测：不限在线设备与原生 IP 解锁的专线选择</a></h4>
              <span class="featured-item-date">2026-07-04</span>
            </div>
          </div>
        </div>
      </div>
    </aside>

    <!-- Right Column: Articles Feed -->
    <section class="content-feed">
      <div class="feed-header">
        <h2 class="feed-title">最新专线测速与购买订阅评测</h2>
        <div class="active-filter-indicator" id="active-filter-indicator">
          当前过滤：<span id="filter-label" style="font-weight: 700;">-</span>
          <a href="#" onclick="resetFilters(); return false;" style="margin-left: 8px; text-decoration: underline; cursor: pointer; color: var(--text-muted);">清除</a>
        </div>
      </div>

      <!-- 13 Article Cards -->
      
      <!-- Card 1: 极连云 -->
      <article class="article-card" data-categories="premium,cheap" data-tags="机场评测,最新节点分享,如何订阅购买,极连云">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            极连云<br>IEPL专线评测
          </div>
          <span class="card-badge">IEPL专线</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-18</span>
            <span>阅读 (2180)</span>
          </div>
          <h3 class="card-title"><a href="articles/jilianyun-review.html">极连云 机场测速与评测：高性价比 IEPL 专线推荐</a></h3>
          <p class="card-excerpt">极连云是一家提供超高性价比 IEPL 专线的网络加速机场。所有节点均为 x1 倍率，晚高峰不限速，并且不限制同时在线的客户端数。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">极连云</span>
              <span class="card-tag">机场评测</span>
            </div>
            <a href="articles/jilianyun-review.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 2: 光年梯 -->
      <article class="article-card" data-categories="cheap,premium" data-tags="机场评测,不限时长,科学下载,光年梯">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            光年梯<br>高性价比推荐
          </div>
          <span class="card-badge">流媒体解锁</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-16</span>
            <span>阅读 (1810)</span>
          </div>
          <h3 class="card-title"><a href="articles/guangnianti-review.html">光年梯 机场评测：稳定解锁流媒体与高可用线路方案</a></h3>
          <p class="card-excerpt">光年梯全专线支持，最高可提供2.5Gbps速率，入门套餐低至18元/月有110GB流量，支持流媒体AI完美解锁。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">光年梯</span>
              <span class="card-tag">不限时长</span>
            </div>
            <a href="articles/guangnianti-review.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 3: 边缘 -->
      <article class="article-card" data-categories="premium,established" data-tags="机场评测,最新节点分享,一键翻墙,边缘">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #1e293b 0%, #475569 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            边缘（极界）<br>极速高隐私
          </div>
          <span class="card-badge">一键客户端</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-14</span>
            <span>阅读 (1560)</span>
          </div>
          <h3 class="card-title"><a href="articles/edge-review.html">边缘 机场（极界）深度评测：无日志与极速数据中转</a></h3>
          <p class="card-excerpt">边缘机场主打无日志高隐私安全防护，拥有60+节点覆盖，自研客户端一键接入使用，支持重置9折及年付85折优惠。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">边缘</span>
              <span class="card-tag">一键翻墙</span>
            </div>
            <a href="articles/edge-review.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 4: 快狸 -->
      <article class="article-card" data-categories="established,cheap" data-tags="机场评测,不限时长,如何订阅购买,快狸">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            快狸（狸机场）<br>自研客户端一键
          </div>
          <span class="card-badge">多设备不限</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-10</span>
            <span>阅读 (1730)</span>
          </div>
          <h3 class="card-title"><a href="articles/kuaili-review.html">快狸 机场推荐：多设备在线与高性价比备用选择</a></h3>
          <p class="card-excerpt">快狸不限制同时在线设备数量，提供自研一键连接客户端，月狸套餐低至15元起，非常适合作为高可用网络备用通道。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">快狸</span>
              <span class="card-tag">如何订阅购买</span>
            </div>
            <a href="articles/kuaili-review.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 5: 光速云 -->
      <article class="article-card" data-categories="premium,cheap" data-tags="机场评测,最新节点分享,科学下载,光速云">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            光速云<br>全球IPLC专线
          </div>
          <span class="card-badge">IPLC专线</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-09</span>
            <span>阅读 (2120)</span>
          </div>
          <h3 class="card-title"><a href="articles/guangshuyun-review.html">光速云 机场深度评测：全球 IPLC 专线与多端在线连接方案</a></h3>
          <p class="card-excerpt">光速云提供全球IPLC物理专线，最高2.5Gbps速率，月付低至17元，原生IP解锁流媒体，支持多设备同时在线。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">光速云</span>
              <span class="card-tag">科学下载</span>
            </div>
            <a href="articles/guangshuyun-review.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 6: 全球云 -->
      <article class="article-card" data-categories="premium,established" data-tags="不限时长,一键翻墙,如何订阅购买,全球云">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            全球云<br>BGP智能优化不限时
          </div>
          <span class="card-badge">流量永久有效</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-07</span>
            <span>阅读 (1890)</span>
          </div>
          <h3 class="card-title"><a href="articles/globalyun-review.html">全球云 机场评测：不限时 BGP 智能优化与永久有效大容量包推荐</a></h3>
          <p class="card-excerpt">全球云提供不设到期重置的BGP不限时套餐，一次购买流量永久有效，支持解除常规单账户设备锁限制。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">全球云</span>
              <span class="card-tag">不限时长</span>
            </div>
            <a href="articles/globalyun-review.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 7: 瞬云 -->
      <article class="article-card" data-categories="cheap,established" data-tags="机场评测,不限时长,科学下载,瞬云">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #a855f7 0%, #9333ea 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            瞬云<br>Anycast高速节点
          </div>
          <span class="card-badge">高吞吐中转</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-06</span>
            <span>阅读 (1880)</span>
          </div>
          <h3 class="card-title"><a href="articles/shunyun-review.html">瞬云 机场测速评测：限时特惠年付小包与高带宽 ANYCAST 连接方案</a></h3>
          <p class="card-excerpt">瞬云提供 Anycast 高速路由节点中转，晚高峰延迟低，行者及纵横套餐支持超大流量，三年付优惠享受高达 25% 折扣。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">瞬云</span>
              <span class="card-tag">科学下载</span>
            </div>
            <a href="articles/shunyun-review.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 8: 寰宇云 -->
      <article class="article-card" data-categories="premium,established" data-tags="一键翻墙,如何订阅购买,最新节点分享,寰宇云">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #059669 0%, #047857 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            寰宇云<br>不限设备数量
          </div>
          <span class="card-badge">流媒体原生IP</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-04</span>
            <span>阅读 (2010)</span>
          </div>
          <h3 class="card-title"><a href="articles/huanyuyun-review.html">寰宇云 机场评测：不限在线设备与原生 IP 解锁的专线选择</a></h3>
          <p class="card-excerpt">寰宇云提供不限在线设备数的专线网络覆盖。限定年付套餐低至 ¥79/年，全原生 IP 完美解锁奈飞和 AI 工具。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">寰宇云</span>
              <span class="card-tag">最新节点分享</span>
            </div>
            <a href="articles/huanyuyun-review.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 9: 速界 -->
      <article class="article-card" data-categories="premium,cheap,established" data-tags="机场评测,一键翻墙,如何订阅购买,速界">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            速界<br>千兆不限速设备
          </div>
          <span class="card-badge">不限速设备</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-03</span>
            <span>阅读 (1950)</span>
          </div>
          <h3 class="card-title"><a href="articles/sujie-review.html">速界 机场评测：不限速不限制设备的高性能 IEPL 节点首选推荐</a></h3>
          <p class="card-excerpt">速界提供不限速、不限制连接的设备数的专线网络加速。年付仅¥90起，60+节点全覆盖，支持一键自研软件使用。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">速界</span>
              <span class="card-tag">机场评测</span>
            </div>
            <a href="articles/sujie-review.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 10: 精选汇总 -->
      <article class="article-card" data-categories="curated" data-tags="机场评测,最新节点分享,如何订阅购买,不限时长,极连云,光年梯,边缘,快狸,光速云,全球云,瞬云,寰宇云,速界">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #ec4899 0%, #db2777 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            2026 梯子<br>精选大汇总
          </div>
          <span class="card-badge">本站精选</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-08</span>
            <span>阅读 (2540)</span>
          </div>
          <h3 class="card-title"><a href="articles/best-airports-2026.html">精选汇总：2026 年最值得推荐的稳定好用机场梯子合集</a></h3>
          <p class="card-excerpt">如何挑选真实好用的加速器？本篇根据长期测速和连通率监控，总结出 2026 年最值得入手的 9 大机场推荐。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">机场评测</span>
              <span class="card-tag">极连云</span>
            </div>
            <a href="articles/best-airports-2026.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 11: 便宜机场 -->
      <article class="article-card" data-categories="cheap" data-tags="免费vpn,机场评测,光年梯,快狸,光速云,瞬云,寰宇云,速界">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            低价首选<br>便宜机场合集
          </div>
          <span class="card-badge">超低价格</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-05</span>
            <span>阅读 (2090)</span>
          </div>
          <h3 class="card-title"><a href="articles/cheap-airports.html">便宜机场推荐：10元左右高性价比机场首选（光年梯与快狸）</a></h3>
          <p class="card-excerpt">预算有限又想看高清视频？本文盘点寰宇云¥79/年、光年梯¥18/月、速界¥90/年、快狸¥15/月、瞬云¥99/年等平价方案。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">免费vpn</span>
              <span class="card-tag">寰宇云</span>
            </div>
            <a href="articles/cheap-airports.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 12: 优质机场 -->
      <article class="article-card" data-categories="premium" data-tags="机场评测,最新节点分享,极连云,边缘,光速云,全球云,寰宇云,速界">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #14b8a6 0%, #0d9488 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            高端稳定<br>专线办公推荐
          </div>
          <span class="card-badge">高端专线</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-07-02</span>
            <span>阅读 (1520)</span>
          </div>
          <h3 class="card-title"><a href="articles/premium-airports.html">优质机场推荐：适合4K视频与办公的稳定专线机场推荐（极连云与边缘）</a></h3>
          <p class="card-excerpt">跨国视频会议、学术研发丢包监控。极连云、边缘、速界、寰宇云、全球云等专线大吞吐服务是您的首选方案。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">极连云</span>
              <span class="card-tag">边缘</span>
            </div>
            <a href="articles/premium-airports.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

      <!-- Card 13: 订阅购买指南 -->
      <article class="article-card" data-categories="curated" data-tags="如何订阅购买,一键翻墙,科学下载,极连云,光年梯,边缘,快狸,光速云,全球云,瞬云,寰宇云,速界">
        <div class="card-image-wrap" style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);">
          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:'Outfit'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">
            如何订阅<br>配置购买指南
          </div>
          <span class="card-badge">新手必读</span>
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span>2026-06-28</span>
            <span>阅读 (1880)</span>
          </div>
          <h3 class="card-title"><a href="articles/subscription-guide.html">如何订阅购买：极连云、光年梯、边缘、快狸一键配置与购买指南</a></h3>
          <p class="card-excerpt">新手一站式购买及一键通用客户端导入教程。教你如何安全注册、快速支付充值、实现全平台跨越访问。</p>
          <div class="card-footer">
            <div class="card-tags">
              <span class="card-tag">如何订阅购买</span>
              <span class="card-tag">一键翻墙</span>
            </div>
            <a href="articles/subscription-guide.html" class="read-more">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>

    </section>
  </main>

  <!-- User Reviews / Testimonials Section -->
  <section class="reviews-section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">用户评价与真实使用反馈</h2>
        <p class="section-subtitle">听听来自网络技术工程师、跨境商务人士与极客玩家的切身体会</p>
      </div>

      <div class="reviews-grid">
        <div class="review-card">
          <div class="review-rating">
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          </div>
          <p class="review-content">
            "寰宇云和速界最棒的一点就是完全不限在线客户端设备数，这对于我们整个设计团队共享海外图片/素材站实在太合适了。原生IP解锁Netflix和AI非常稳定。"
          </p>
          <div class="review-author">
            <div class="author-avatar">L</div>
            <div class="author-info">
              <span class="author-name">Alex Li</span>
              <span class="author-role">高级全栈开发工程师</span>
            </div>
          </div>
        </div>

        <div class="review-card">
          <div class="review-rating">
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          </div>
          <p class="review-content">
            "速界所有节点不限速，Anycast物理中继带宽不限速，晚高峰看4K超高清几乎秒开。季付付优惠省了不少预算！"
          </p>
          <div class="review-author">
            <div class="author-avatar">W</div>
            <div class="author-info">
              <span class="author-name">王美静</span>
              <span class="author-role">海外影视博主</span>
            </div>
          </div>
        </div>

        <div class="review-card">
          <div class="review-rating">
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:var(--warning);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          </div>
          <p class="review-content">
            "这几个推荐机场（极连云、瞬云、寰宇云、速界等）在特殊时期都提供了备用域名和强大的防屏蔽支持，基本上做到了全年断网率接近0%，推荐注册购买。"
          </p>
          <div class="review-author">
            <div class="author-avatar">Z</div>
            <div class="author-info">
              <span class="author-name">张小凡</span>
              <span class="author-role">在读研究生</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="faq-section container">
    <div class="section-header">
      <h2 class="section-title">常见问题 FAQ</h2>
      <p class="section-subtitle">解答您关于科学上网专线购买与一键配置的疑惑</p>
    </div>

    <div class="faq-container">
      <div class="faq-item">
        <button class="faq-trigger">
          <span>什么是专线网络？为什么比直连加速稳定？</span>
          <svg class="faq-chevron" viewBox="0 0 24 24" style="width:20px; height:20px;"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"/></svg>
        </button>
        <div class="faq-content">
          <p>专线网络（如极连云、光速云、速界的 IEPL/IPLC 专线，以及瞬云、寰宇云的高带宽 ANYCAST/IPLC 中转）是物理层直连线路，其流量不经过公共网关防火墙过滤，因此在网络高流量拥堵或敏感时期也能保持超低连通延迟与 0 丢包率。</p>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-trigger">
          <span>一键订阅和一键客户端是指什么？</span>
          <svg class="faq-chevron" viewBox="0 0 24 24" style="width:20px; height:20px;"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"/></svg>
        </button>
        <div class="faq-content">
          <p>极连云、光年梯、边缘、快狸、光速云、全球云、瞬云、寰宇云与速界都在后台控制面板提供了快捷的一键导入通用客户端功能。此外，部分机场如边缘、快狸和速界更是提供了定制化自研客户端，下载后直接登录即可一键开始加速。</p>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-trigger">
          <span>购买服务后遇到问题如何获得售后支持？</span>
          <svg class="faq-chevron" viewBox="0 0 24 24" style="width:20px; height:20px;"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"/></svg>
        </button>
        <div class="faq-content">
          <p>所有推荐机场均在面板后台设置了工单咨询版块。寰宇云和速界等品牌拥有极速工单客服响应，如果在使用过程中遇到任何关于线路、导入配置或者充值方面的疑问，请直接在所选机场官网的后台控制台提单咨询。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <h3 class="footer-brand-title">机场速递</h3>
          <p>jichangspeed.biz 专注于2026年最新高速、便宜、安全专线网络节点测速和评测。我们致力于打破虚假宣传，为您提供真实可靠的极连云、光年梯、边缘、快狸、光速云、全球云、瞬云、寰宇云、速界官网订阅入口。</p>
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
            <li><a href="{links['光年梯']}" target="_blank" class="footer-link">光年梯官网 ↗</a></li>
            <li><a href="{links['边缘']}" target="_blank" class="footer-link">边缘官网 ↗</a></li>
            <li><a href="{links['快狸']}" target="_blank" class="footer-link">快狸官网 ↗</a></li>
            <li><a href="{links['光速云']}" target="_blank" class="footer-link">光速云官网 ↗</a></li>
            <li><a href="{links['全球云']}" target="_blank" class="footer-link">全球云官网 ↗</a></li>
            <li><a href="{links['瞬云']}" target="_blank" class="footer-link">瞬云官网 ↗</a></li>
            <li><a href="{links['寰宇云']}" target="_blank" class="footer-link">寰宇云官网 ↗</a></li>
            <li><a href="{links['速界']}" target="_blank" class="footer-link">速界官网 ↗</a></li>
          </ul>
        </div>

        <div class="footer-links-col">
          <h4 class="footer-links-title">合作联系</h4>
          <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 8px;">商务与测速投稿请发邮件：</p>
          <ul class="footer-links-list" style="font-size: 0.85rem;">
            <li>邮箱: support@jichangspeed.biz</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 机场速递 (jichangspeed.biz) 保留所有权利。</p>
        <div class="footer-bottom-links">
          <a href="sitemap.xml" class="footer-link">网站地图</a>
          <a href="robots.txt" class="footer-link">Robots.txt</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html written.")

def write_about():
    html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>关于我们 - 机场速递博客 (jichangspeed.biz)</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="关于机场速递 (jichangspeed.biz) —— 我们的定位、测速准则、核心价值与联系方式。提供极连云、光年梯、边缘、快狸、光速云、全球云、瞬云、寰宇云、速界等高品质专线梯子官网入口。">
  <meta name="keywords" content="关于我们, 机场速递, 机场评测, 极连云, 光年梯, 边缘, 快狸, 光速云, 全球云, 瞬云, 寰宇云, 速界, jichangspeed.biz">
  <meta name="robots" content="index, follow">
  
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <!-- Header -->
  <header class="header">
    <div class="container header-container">
      <a href="index.html" class="logo">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M12 22V12M12 12L4 7.5M12 12l8-4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>机场速递</span>
      </a>
      
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">☰</button>
      
      <nav class="nav" id="nav-menu">
        <a href="articles/cheap-airports.html" class="nav-link">便宜机场推荐</a>
        <a href="articles/premium-airports.html" class="nav-link">优质机场推荐</a>
        <a href="articles/kuaili-review.html" class="nav-link">老牌机场推荐</a>
        <a href="articles/best-airports-2026.html" class="nav-link">精选汇总</a>
        <a href="vpn-guide.html" class="nav-link">科学上网</a>
        <a href="about.html" class="nav-link active">关于我们</a>
        
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
          <p>安全、高速、平稳地获取海外学术信息与商用数据是每一位开发者、设计师、跨境电商以及外贸从业者的刚需。我们致力于通过真实、透明的评估测试，为您提供真实可靠的极连云、光年梯、边缘、快狸、光速云、全球云、瞬云、寰宇云、速界官网订阅入口。</p>

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
            <a href="index.html?tag=%E8%BE%B9%E7%BC%98" class="sidebar-tag">边缘</a>
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
          <p>jichangspeed.biz 专注于2026年最新高速、便宜、安全专线网络节点测速和评测。我们致力于为用户提供真实可靠的极连云、光年梯、边缘、快狸、光速云、全球云、瞬云、寰宇云、速界官网订阅入口。</p>
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
            <li><a href="{links['光年梯']}" target="_blank" class="footer-link">光年梯官网 ↗</a></li>
            <li><a href="{links['边缘']}" target="_blank" class="footer-link">边缘官网 ↗</a></li>
            <li><a href="{links['快狸']}" target="_blank" class="footer-link">快狸官网 ↗</a></li>
            <li><a href="{links['光速云']}" target="_blank" class="footer-link">光速云官网 ↗</a></li>
            <li><a href="{links['全球云']}" target="_blank" class="footer-link">全球云官网 ↗</a></li>
            <li><a href="{links['瞬云']}" target="_blank" class="footer-link">瞬云官网 ↗</a></li>
            <li><a href="{links['寰宇云']}" target="_blank" class="footer-link">寰宇云官网 ↗</a></li>
            <li><a href="{links['速界']}" target="_blank" class="footer-link">速界官网 ↗</a></li>
          </ul>
        </div>

        <div class="footer-links-col">
          <h4 class="footer-links-title">合作联系</h4>
          <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 8px;">商务与测速投稿请发邮件：</p>
          <ul class="footer-links-list" style="font-size: 0.85rem;">
            <li>邮箱: support@jichangspeed.biz</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 机场速递 (jichangspeed.biz) 保留所有权利。</p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
"""
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("about.html written.")

def write_vpn_guide():
    html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>网络订阅配置与下载指南 - 机场速递博客 (jichangspeed.biz)</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="科学上网配置购买一站式指南。涵盖电脑客户端、安卓客户端与iOS苹果客户端下载与通用一键订阅导入教程，推荐使用极连云、光年梯、边缘、快狸、光速云、全球云、瞬云、寰宇云、速界官网订阅服务。">
  <meta name="keywords" content="配置配置, 订阅下载, 客户端导入, 极连云, 光年梯, 边缘, 快狸, 光速云, 全球云, 瞬云, 寰宇云, 速界, jichangspeed.biz">
  <meta name="robots" content="index, follow">
  
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <!-- Header -->
  <header class="header">
    <div class="container header-container">
      <a href="index.html" class="logo">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M12 22V12M12 12L4 7.5M12 12l8-4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>机场速递</span>
      </a>
      
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">☰</button>
      
      <nav class="nav" id="nav-menu">
        <a href="articles/cheap-airports.html" class="nav-link">便宜机场推荐</a>
        <a href="articles/premium-airports.html" class="nav-link">优质机场推荐</a>
        <a href="articles/kuaili-review.html" class="nav-link">老牌机场推荐</a>
        <a href="articles/best-airports-2026.html" class="nav-link">精选汇总</a>
        <a href="vpn-guide.html" class="nav-link active">科学上网</a>
        <a href="about.html" class="nav-link">关于我们</a>
        
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
      <span>科学上网</span>
    </div>

    <div class="main-layout">
      <!-- Left Column: Setup Guide -->
      <article class="content-feed">
        <div class="article-header">
          <h1 class="article-title-large">翻墙客户端一键订阅与通用配置指南</h1>
        </div>

        <div class="article-body">
          <p>进行专线网络浏览，我们需要两个基础要素：第一是**机场的官网订阅链接**，第二是**运行在设备上的软件客户端**。下面以极连云、光年梯、边缘、快狸、光速云、全球云、瞬云、寰宇云与速界为例，教您如何快速导入使用。</p>

          <h2>一、一键自研客户端（最简单）</h2>
          <p>如果您选择的是 <strong><a href="{links['边缘']}" target="_blank">边缘 (极界)</a></strong>、<strong><a href="{links['快狸']}" target="_blank">快狸 机场</a></strong> 或 <strong><a href="{links['速界']}" target="_blank">速界官网</a></strong>：</p>
          <ul>
            <li>登录对应的官网后台，点击 <strong>“下载自研客户端”</strong>，下载后一键登录您的注册账户，即可实现自动更新节点、一键开启翻墙，无需手动复制订阅，适合新手小白。</li>
          </ul>

          <h2>二、通用客户端一键订阅导入</h2>
          <p>如果您使用的是 <strong>极连云</strong>、<strong>光年梯</strong>、<strong>光速云</strong>、<strong>全球云</strong>、<strong>瞬云</strong>、<strong>寰宇云</strong>，可以通过通用配置一键导入使用：</p>
          <ul>
            <li>登录官网后台，购买套餐后，点击“快捷导入”选项中的“一键导入配置”，软件会自动跳转并导入节点数据。同步完成后开启连接开关即可。</li>
          </ul>
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
            <a href="index.html?tag=%E8%BE%B9%E7%BC%98" class="sidebar-tag">边缘</a>
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
          <p>jichangspeed.biz 专注于2026年最新高速、便宜、安全专线网络节点测速和评测。我们致力于为用户提供真实可靠的极连云、光年梯、边缘、快狸、光速云、全球云, 瞬云、寰宇云、速界官网订阅入口。</p>
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
            <li><a href="{links['光年梯']}" target="_blank" class="footer-link">光年梯官网 ↗</a></li>
            <li><a href="{links['边缘']}" target="_blank" class="footer-link">边缘官网 ↗</a></li>
            <li><a href="{links['快狸']}" target="_blank" class="footer-link">快狸官网 ↗</a></li>
            <li><a href="{links['光速云']}" target="_blank" class="footer-link">光速云官网 ↗</a></li>
            <li><a href="{links['全球云']}" target="_blank" class="footer-link">全球云官网 ↗</a></li>
            <li><a href="{links['瞬云']}" target="_blank" class="footer-link">瞬云官网 ↗</a></li>
            <li><a href="{links['寰宇云']}" target="_blank" class="footer-link">寰宇云官网 ↗</a></li>
            <li><a href="{links['速界']}" target="_blank" class="footer-link">速界官网 ↗</a></li>
          </ul>
        </div>

        <div class="footer-links-col">
          <h4 class="footer-links-title">合作联系</h4>
          <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 8px;">商务与测速投稿请发邮件：</p>
          <ul class="footer-links-list" style="font-size: 0.85rem;">
            <li>邮箱: support@jichangspeed.biz</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 机场速递 (jichangspeed.biz) 保留所有权利。</p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
"""
    with open('vpn-guide.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("vpn-guide.html written.")

def write_sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://jichangspeed.biz/</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/about.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/vpn-guide.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <!-- 13 Articles -->
  <url>
    <loc>https://jichangspeed.biz/articles/jilianyun-review.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/guangnianti-review.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/edge-review.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/kuaili-review.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/guangshuyun-review.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/globalyun-review.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/shunyun-review.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/huanyuyun-review.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/sujie-review.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/best-airports-2026.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/cheap-airports.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/premium-airports.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://jichangspeed.biz/articles/subscription-guide.html</loc>
    <lastmod>2026-07-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>
"""
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml)
    print("sitemap.xml written.")

if __name__ == '__main__':
    write_index()
    write_about()
    write_vpn_guide()
    write_sitemap()
    print("All final parent pages generated successfully!")
