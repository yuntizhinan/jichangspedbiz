# -*- coding: utf-8 -*-
import os
import re

def replace_text_globally():
    def inject_theme_script(html):
        # Remove old script version without try-catch if present
        old_script_str = """  <script>
    (function() {
      const savedTheme = localStorage.getItem('theme');
      const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const theme = savedTheme === 'dark' || (!savedTheme && systemPrefersDark) ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', theme);
    })();
  </script>"""
        html = html.replace(old_script_str, "")
        
        if 'try {' in html and 'localStorage.getItem(\'theme\')' in html:
            return html
        script = """<head>
  <script>
    (function() {
      let savedTheme = null;
      try {
        savedTheme = localStorage.getItem('theme');
      } catch (e) {}
      const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const theme = savedTheme === 'dark' || (!savedTheme && systemPrefersDark) ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', theme);
    })();
  </script>"""
        return html.replace('<head>', script)

    # 替换精选文章列表的子函数
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
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/tpkZpVhs/sujielogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="速界"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="{prefix}sujie-review.html">速界 机场评测：不限速不限制设备的高性能 IEPL 节点首选推荐</a></h4>
              <span class="featured-item-date">2026-07-03</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/C5P4QcfT/bianyuanjiedianlogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="边缘"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="{prefix}edge-review.html">边缘 机场（EdgeNova）深度评测：无日志与极速数据中转</a></h4>
              <span class="featured-item-date">2026-07-14</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/TxW2rqGj/jilianyunlogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="极连云"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="{prefix}jilianyun-review.html">极连云 机场测速与评测：高性价比 IEPL 专线推荐</a></h4>
              <span class="featured-item-date">2026-07-18</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/mCYxy3yM/guanniantilogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="光年梯"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="{prefix}guangnianti-review.html">光年梯 机场评测：稳定解锁流媒体与高可用线路方案</a></h4>
              <span class="featured-item-date">2026-07-16</span>
            </div>
          </div>
          <div class="featured-item">
            <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/jkR2rZRw/shunyunlogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="瞬云"></div>
            <div class="featured-item-content">
              <h4 class="featured-item-title"><a href="{prefix}shunyun-review.html">瞬云 机场测速评测：限时特惠年付小包与高带宽 ANYCAST 连接方案</a></h4>
              <span class="featured-item-date">2026-07-06</span>
            </div>
          </div>
                    <div class="featured-item">
              <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/1f4FvF92/kuaililogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="快狸"></div>
              <div class="featured-item-content">
                <h4 class="featured-item-title"><a href="{prefix}kuaili-review.html">快狸 机场推荐：多设备在线与高性价比备用选择</a></h4>
                <span class="featured-item-date">2026-07-10</span>
              </div>
            </div>
          </div>
      </div>"""
            
            content_norm = content_norm[:idx] + new_featured_html + content_norm[end_idx:]
            content_norm = content_norm.replace('<div class="featured-list">', '<div class="featured-list-done">', 1)
            
        content_norm = content_norm.replace('<div class="featured-list-done">', '<div class="featured-list">')
        return content_norm

    def remove_footer_links(content):
        content_norm = content.replace("\r\n", "\n")
        block1 = """          <div class="footer-links">
            <a href="sitemap.xml" class="footer-link">网站地图</a>
            <a href="robots.txt" class="footer-link">Robots.txt</a>
          </div>"""
        content_norm = content_norm.replace(block1, "")
        
        block1_alt = """      <div class="footer-links">
        <a href="sitemap.xml" class="footer-link">网站地图</a>
        <a href="robots.txt" class="footer-link">Robots.txt</a>
      </div>"""
        content_norm = content_norm.replace(block1_alt, "")

        block2 = """          <div class="footer-links">
            <a href="../sitemap.xml" class="footer-link">网站地图</a>
            <a href="../robots.txt" class="footer-link">Robots.txt</a>
          </div>"""
        content_norm = content_norm.replace(block2, "")
        
        block2_alt = """      <div class="footer-links">
        <a href="../sitemap.xml" class="footer-link">网站地图</a>
        <a href="../robots.txt" class="footer-link">Robots.txt</a>
      </div>"""
        content_norm = content_norm.replace(block2_alt, "")

        content_norm = content_norm.replace('<a href="sitemap.xml" class="footer-link">网站地图</a>', '')
        content_norm = content_norm.replace('<a href="robots.txt" class="footer-link">Robots.txt</a>', '')
        content_norm = content_norm.replace('<a href="../sitemap.xml" class="footer-link">网站地图</a>', '')
        content_norm = content_norm.replace('<a href="../robots.txt" class="footer-link">Robots.txt</a>', '')
        return content_norm

    def insert_featured_list_widget(content, is_subpage=False):
        if 'featured-list' in content:
            return content
            
        prefix = "" if is_subpage else "articles/"
        
        featured_widget = f"""        <!-- Sidebar Featured Widget -->
        <div class="sidebar-widget">
          <h3 class="widget-title">
            <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
            精选文章
          </h3>
          <div class="featured-list">
            <div class="featured-item">
              <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/tpkZpVhs/sujielogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="速界"></div>
              <div class="featured-item-content">
                <h4 class="featured-item-title"><a href="{prefix}sujie-review.html">速界 机场评测：不限速不限制设备的高性能 IEPL 节点首选推荐</a></h4>
                <span class="featured-item-date">2026-07-03</span>
              </div>
            </div>
            <div class="featured-item">
              <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/C5P4QcfT/bianyuanjiedianlogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="边缘"></div>
              <div class="featured-item-content">
                <h4 class="featured-item-title"><a href="{prefix}edge-review.html">边缘 机场（EdgeNova）深度评测：无日志与极速数据中转</a></h4>
                <span class="featured-item-date">2026-07-14</span>
              </div>
            </div>
            <div class="featured-item">
              <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/TxW2rqGj/jilianyunlogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="极连云"></div>
              <div class="featured-item-content">
                <h4 class="featured-item-title"><a href="{prefix}jilianyun-review.html">极连云 机场测速与评测：高性价比 IEPL 专线推荐</a></h4>
                <span class="featured-item-date">2026-07-18</span>
              </div>
            </div>
            <div class="featured-item">
              <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/mCYxy3yM/guanniantilogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="光年梯"></div>
              <div class="featured-item-content">
                <h4 class="featured-item-title"><a href="{prefix}guangnianti-review.html">光年梯 机场评测：稳定解锁流媒体与高可用线路方案</a></h4>
                <span class="featured-item-date">2026-07-16</span>
              </div>
            </div>
            <div class="featured-item">
              <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/jkR2rZRw/shunyunlogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="瞬云"></div>
              <div class="featured-item-content">
                <h4 class="featured-item-title"><a href="{prefix}shunyun-review.html">瞬云 机场测速评测：限时特惠年付小包与高带宽 ANYCAST 连接方案</a></h4>
                <span class="featured-item-date">2026-07-06</span>
              </div>
            </div>
                      <div class="featured-item">
              <div class="featured-item-img" style="background: #fff; display:flex; align-items:center; justify-content:center; border: 1px solid var(--border-color); overflow: hidden; border-radius: var(--radius-sm);"><img src="https://i.ibb.co/1f4FvF92/kuaililogo.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="快狸"></div>
              <div class="featured-item-content">
                <h4 class="featured-item-title"><a href="{prefix}kuaili-review.html">快狸 机场推荐：多设备在线与高性价比备用选择</a></h4>
                <span class="featured-item-date">2026-07-10</span>
              </div>
            </div>
          </div>
        </div>"""
        
        content_norm = content.replace("\r\n", "\n")
        if "</aside>" in content_norm:
            content_norm = content_norm.replace("</aside>", featured_widget + "\n      </aside>", 1)
        return content_norm

    # 1. 遍历修改 articles/ 目录下的所有文章 HTML
    articles_dir = "articles"
    if os.path.exists(articles_dir):
        for fname in os.listdir(articles_dir):
            if fname.endswith(".html"):
                fpath = os.path.join(articles_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    html = f.read()
                
                # 面包屑、所属版块和导航项文字替换
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
                
                # 升级精选文章侧边栏与页脚
                html = update_featured_list_in_html(html, is_subpage=True)
                html = remove_footer_links(html)
                # 强行在没有侧边栏列表的页面中注入精选文章列表
                html = insert_featured_list_widget(html, is_subpage=True)
                # 全局替换极界为 EdgeNova
                html = html.replace("极界", "EdgeNova")
                html = inject_theme_script(html)
                
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(html)
        print("Updated HTML files in articles directory")

    # 2. 遍历修改主目录下的 parent html 页面
    for fname in os.listdir('.'):
        if fname.endswith('.html'):
            with open(fname, 'r', encoding='utf-8') as f:
                html = f.read()
            html = html.replace("极界", "EdgeNova")
            # 同样对主目录下的 parent 页（如 vpn-guide.html）进行侧边栏精选列表注入
            html = insert_featured_list_widget(html, is_subpage=False)
            html = inject_theme_script(html)
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(html)
    print("Updated parent HTML files")

if __name__ == '__main__':
    replace_text_globally()
