# -*- coding: utf-8 -*-
import os
import re

def replace_text_globally():
    # 替换 LOGO 的通用子函数
    def update_logo_content(content):
        content_norm = content.replace("\r\n", "\n")
        
        old_svg = """<svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M12 22V12M12 12L4 7.5M12 12l8-4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>"""
        
        new_svg = """<svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10" fill="var(--accent-primary)" />
          <path d="M12 6L18 13L14 12.5L14.5 17L12 15L9.5 17L10 12.5 L6 13Z" fill="#ffffff" />
        </svg>"""
        
        content_norm = content_norm.replace(old_svg, new_svg)
        
        old_svg_alt = """<svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M12 22V12M12 12L4 7.5M12 12l8-4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>"""
        content_norm = content_norm.replace(old_svg_alt, new_svg)
        return content_norm.replace("\n", os.linesep)

    def add_cache_busting_version(content):
        content = content.replace('js/main.js?v=20260724', 'js/main.js')
        content = content.replace('../js/main.js?v=20260724', '../js/main.js')
        content = content.replace('css/style.css?v=20260724', 'css/style.css')
        content = content.replace('../css/style.css?v=20260724', '../css/style.css')
        
        content = content.replace('js/main.js', 'js/main.js?v=20260724')
        content = content.replace('../js/main.js', '../js/main.js?v=20260724')
        content = content.replace('css/style.css', 'css/style.css?v=20260724')
        content = content.replace('../css/style.css', '../css/style.css?v=20260724')
        return content

    def inject_dark_logo_style_for_python(content):
        # Python 脚本的多行 f-string 模板，必须使用双大括号逃逸 CSS 大括号
        style_block = """  <style>
    /* 强力保证夜间模式下 Logo span 文本显示为清晰的纯白色，不受外部样式缓存影响 */
    [data-theme="dark"] .logo span {{
      background: none !important;
      -webkit-background-clip: unset !important;
      -webkit-text-fill-color: #ffffff !important;
      color: #ffffff !important;
    }}
  </style>"""
        if "强力保证夜间模式下 Logo span 文本" in content:
            return content
        return content.replace("</head>", style_block + "\n</head>")

    def inject_dark_logo_style_for_html(content):
        # 普通静态 HTML 页面中，使用正常单大括号
        style_block = """  <style>
    /* 强力保证夜间模式下 Logo span 文本显示为清晰的纯白色，不受外部样式缓存影响 */
    [data-theme="dark"] .logo span {
      background: none !important;
      -webkit-background-clip: unset !important;
      -webkit-text-fill-color: #ffffff !important;
      color: #ffffff !important;
    }
  </style>"""
        if "强力保证夜间模式下 Logo span 文本" in content:
            return content
        return content.replace("</head>", style_block + "\n</head>")

    def update_featured_list_in_html(content, is_subpage=False):
        content_norm = content.replace("\r\n", "\n")
        prefix = "" if is_subpage else "articles/"
        
        while '<div class="featured-list">' in content_norm:
            idx = content_norm.find('<div class="featured-list">')
            end_idx = content_norm.find('</aside>', idx)
            if end_idx == -1:
                break
                
            new_featured_html = f"""<div class="featured-list">
          <div class="featured-item">
            <div class="featured-item-img" style="background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:800; font-size:0.75rem; font-family:'Outfit';">JL</div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="{prefix}jilianyun-review.html">极连云 机场测速与评测：高性价比 IEPL 专线推荐</a></h4>
              <span class="featured-item-date">2026-07-18</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:800; font-size:0.75rem; font-family:'Outfit';">GN</div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="{prefix}guangnianti-review.html">光年梯 机场评测：稳定解锁流媒体与高可用线路方案</a></h4>
              <span class="featured-item-date">2026-07-16</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:800; font-size:0.75rem; font-family:'Outfit';">BY</div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="{prefix}edge-review.html">边缘 机场（极界）深度评测：无日志与极速数据中转</a></h4>
              <span class="featured-item-date">2026-07-14</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:800; font-size:0.75rem; font-family:'Outfit';">SJ</div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="{prefix}sujie-review.html">速界 机场评测：不限速不限制设备的高性能 IEPL 节点首选推荐</a></h4>
              <span class="featured-item-date">2026-07-03</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: linear-gradient(135deg, #a855f7 0%, #9333ea 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:800; font-size:0.75rem; font-family:'Outfit';">SY</div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="{prefix}shunyun-review.html">瞬云 机场测速评测：限时特惠年付小包与高带宽 ANYCAST 连接方案</a></h4>
              <span class="featured-item-date">2026-07-06</span>
            </div>
          </div>
        </div>
      </div>"""
            
            content_norm = content_norm[:idx] + new_featured_html + content_norm[end_idx:]
            content_norm = content_norm.replace('<div class="featured-list">', '<div class="featured-list-done">', 1)
            
        content_norm = content_norm.replace('<div class="featured-list-done">', '<div class="featured-list">')
        return content_norm.replace("\n", os.linesep)

    # 1. 替换 write_final_pages.py
    if os.path.exists("write_final_pages.py"):
        with open("write_final_pages.py", "r", encoding="utf-8") as f:
            content = f.read()
        
        content = content.replace("科学上网</a>", "科普专栏</a>")
        content = content.replace("<span>科学上网</span>", "<span>科普专栏</span>")
        content = content.replace("三、科学上网", "三、科普专栏")
        content = content.replace("网络科学上网", "网络加速")
        content = content.replace("OpenWrt科学上网", "OpenWrt科普")
        content = content.replace("软路由科学上网", "软路由科普")
        content = content.replace("motto\">2026稳定安全高速便宜机场推荐与官网订阅评测", "motto\">2026稳定安全高速便宜机场推荐与官网订阅评测")
        
        content = content.replace("提供低门槛的科学上网科普", "提供低门槛 of 科普专栏")
        content = content.replace("科学上网一站式指南", "科普专栏一站式指南")
        content = content.replace("科学上网配置购买", "科普专栏配置购买")
        
        content = content.replace("OpenWrt科学上网教程", "OpenWrt科普教程")
        content = content.replace("科学上网订阅地址", "网络订阅地址")
        content = content.replace("软路由科学上网深度", "软路由技术科普")
        content = content.replace("自建节点对比专线机场：2026年为什么我不建议新手折腾搭建翻墙？", "自建节点对比专线机场：2026年为什么我不建议新手折腾搭建翻墙？")
        
        content = update_logo_content(content)
        content = add_cache_busting_version(content)
        content = update_featured_list_in_html(content, is_subpage=False)
        content = inject_dark_logo_style_for_python(content)
        
        with open("write_final_pages.py", "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated write_final_pages.py")

    # 2. 替换 generate_final_site.py
    if os.path.exists("generate_final_site.py"):
        with open("generate_final_site.py", "r", encoding="utf-8") as f:
            content = f.read()
            
        content = content.replace("科学上网</a>", "科普专栏</a>")
        content = content.replace("<span>科学上网</span>", "<span>科普专栏</span>")
        content = content.replace("提供低门槛的科学上网科普", "提供低门槛的科普专栏")
        content = content.replace("所属版块: 科学上网", "所属版块: 科普专栏")
        
        old_array_pattern = r"featured_items\s*=\s*\[.*?\]"
        new_array_str = """featured_items = [
        {'slug': 'jilianyun-review', 'title': '极连云 机场测速与评测：高性价比 IEPL 专线推荐', 'date': '2026-07-18', 'label': 'JL', 'color': 'linear-gradient(135deg, #3b82f6 0%, #6366f1 100%)'},
        {'slug': 'guangnianti-review', 'title': '光年梯 机场评测：稳定解锁流媒体与高可用线路方案', 'date': '2026-07-16', 'label': 'GN', 'color': 'linear-gradient(135deg, #10b981 0%, #059669 100%)'},
        {'slug': 'edge-review', 'title': '边缘 机场（极界）深度评测：无日志与极速数据中转', 'date': '2026-07-14', 'label': 'BY', 'color': 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)'},
        {'slug': 'sujie-review', 'title': '速界 机场评测：不限速不限制设备的高性能 IEPL 节点首选推荐', 'date': '2026-07-03', 'label': 'SJ', 'color': 'linear-gradient(135deg, #f43f5e 0%, #e11d48 100%)'},
        {'slug': 'shunyun-review', 'title': '瞬云 机场测速评测：限时特惠年付小包与高带宽 ANYCAST 连接方案', 'date': '2026-07-06', 'label': 'SY', 'color': 'linear-gradient(135deg, #a855f7 0%, #9333ea 100%)'}
    ]"""
        content_norm = content.replace("\r\n", "\n")
        content_norm = re.sub(old_array_pattern, new_array_str, content_norm, flags=re.DOTALL)
        content = content_norm.replace("\n", os.linesep)
        
        content = update_logo_content(content)
        content = add_cache_busting_version(content)
        content = inject_dark_logo_style_for_python(content)
        
        with open("generate_final_site.py", "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated generate_final_site.py")

    # 3. 遍历修改 articles/ 目录下的所有文章 HTML
    articles_dir = "articles"
    if os.path.exists(articles_dir):
        for fname in os.listdir(articles_dir):
            if fname.endswith(".html"):
                fpath = os.path.join(articles_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    html = f.read()
                
                html = html.replace("科学上网</a>", "科普专栏</a>")
                html = html.replace("<span>科学上网</span>", "<span>科普专栏</span>")
                html = html.replace("科学上网科普", "科普专栏")
                html = html.replace("科学上网一站式指南", "科普专栏一站式指南")
                html = html.replace("科学上网配置购买", "科普专栏配置购买")
                html = html.replace("提供低门槛的科学上网科普", "提供低门槛的科普专栏")
                html = html.replace("所属版块: 科学上网", "所属版块: 科普专栏")
                html = html.replace("OpenWrt科学上网", "OpenWrt技术")
                html = html.replace("软路由科学上网", "软路由技术")
                html = html.replace("科学上网订阅地址", "网络订阅地址")
                
                html = update_logo_content(html)
                html = add_cache_busting_version(html)
                html = update_featured_list_in_html(html, is_subpage=True)
                html = inject_dark_logo_style_for_html(html)
                
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(html)
        print("Updated HTML files in articles directory")

if __name__ == '__main__':
    replace_text_globally()
