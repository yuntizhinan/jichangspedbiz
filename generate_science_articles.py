# -*- coding: utf-8 -*-
import os

def replace_text_globally():
    # 替换 LOGO 的通用子函数
    def update_logo_content(content):
        # 归一化换行符为 \n 方便多行匹配
        content_norm = content.replace("\r\n", "\n")
        
        old_svg = """<svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M12 22V12M12 12L4 7.5M12 12l8-4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>"""
        
        new_svg = """<svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10" fill="var(--accent-primary)" />
          <path d="M12 6L18 13L14 12.5L14.5 17L12 15L9.5 17L10 12.5 L6 13Z" fill="#ffffff" />
        </svg>"""
        
        # 尝试标准缩进替换
        content_norm = content_norm.replace(old_svg, new_svg)
        
        # 尝试少两个空格缩进的替换
        old_svg_alt = """<svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M12 22V12M12 12L4 7.5M12 12l8-4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>"""
        content_norm = content_norm.replace(old_svg_alt, new_svg)
        
        # 将归一化后的换行符还原为系统默认
        return content_norm.replace("\n", os.linesep)

    # 1. 替换 write_final_pages.py
    if os.path.exists("write_final_pages.py"):
        with open("write_final_pages.py", "r", encoding="utf-8") as f:
            content = f.read()
        
        # 替换普通文本与下拉菜单
        content = content.replace("科学上网</a>", "科普专栏</a>")
        content = content.replace("<span>科学上网</span>", "<span>科普专栏</span>")
        content = content.replace("三、科学上网", "三、科普专栏")
        content = content.replace("网络科学上网", "网络加速")
        content = content.replace("OpenWrt科学上网", "OpenWrt科普")
        content = content.replace("软路由科学上网", "软路由科普")
        content = content.replace("motto\">2026稳定安全高速便宜机场推荐与官网订阅评测", "motto\">2026稳定安全高速便宜机场推荐与官网订阅评测")
        
        # 将 motto 里的“科学上网”换为“科普专栏”
        content = content.replace("提供低门槛的科学上网科普", "提供低门槛的科普专栏")
        content = content.replace("科学上网一站式指南", "科普专栏一站式指南")
        content = content.replace("科学上网配置购买", "科普专栏配置购买")
        
        # 文章定义里也有科学上网
        content = content.replace("OpenWrt科学上网教程", "OpenWrt科普教程")
        content = content.replace("科学上网订阅地址", "网络订阅地址")
        content = content.replace("软路由科学上网深度", "软路由技术科普")
        content = content.replace("自建节点对比专线机场：2026年为什么我不建议新手折腾搭建翻墙？", "自建节点对比专线机场：2026年为什么我不建议新手折腾搭建翻墙？")
        
        # 替换 LOGO
        content = update_logo_content(content)
        
    def add_cache_busting_version(content):
        # 先回退，以防重复追加
        content = content.replace('js/main.js?v=20260724', 'js/main.js')
        content = content.replace('../js/main.js?v=20260724', '../js/main.js')
        content = content.replace('css/style.css?v=20260724', 'css/style.css')
        content = content.replace('../css/style.css?v=20260724', '../css/style.css')
        
        # 加上最新的版本号
        content = content.replace('js/main.js', 'js/main.js?v=20260724')
        content = content.replace('../js/main.js', '../js/main.js?v=20260724')
        content = content.replace('css/style.css', 'css/style.css?v=20260724')
        content = content.replace('../css/style.css', '../css/style.css?v=20260724')
        return content

    # 1. 替换 write_final_pages.py
    if os.path.exists("write_final_pages.py"):
        with open("write_final_pages.py", "r", encoding="utf-8") as f:
            content = f.read()
        
        # 替换普通文本与下拉菜单
        content = content.replace("科学上网</a>", "科普专栏</a>")
        content = content.replace("<span>科学上网</span>", "<span>科普专栏</span>")
        content = content.replace("三、科学上网", "三、科普专栏")
        content = content.replace("网络科学上网", "网络加速")
        content = content.replace("OpenWrt科学上网", "OpenWrt科普")
        content = content.replace("软路由科学上网", "软路由科普")
        content = content.replace("motto\">2026稳定安全高速便宜机场推荐与官网订阅评测", "motto\">2026稳定安全高速便宜机场推荐与官网订阅评测")
        
        # 将 motto 里的“科学上网”换为“科普专栏”
        content = content.replace("提供低门槛的科学上网科普", "提供低门槛的科普专栏")
        content = content.replace("科学上网一站式指南", "科普专栏一站式指南")
        content = content.replace("科学上网配置购买", "科普专栏配置购买")
        
        # 文章定义里也有科学上网
        content = content.replace("OpenWrt科学上网教程", "OpenWrt科普教程")
        content = content.replace("科学上网订阅地址", "网络订阅地址")
        content = content.replace("软路由科学上网深度", "软路由技术科普")
        content = content.replace("自建节点对比专线机场：2026年为什么我不建议新手折腾搭建翻墙？", "自建节点对比专线机场：2026年为什么我不建议新手折腾搭建翻墙？")
        
        # 替换 LOGO & 版本号
        content = update_logo_content(content)
        content = add_cache_busting_version(content)
        
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
        
        # 替换 LOGO & 版本号
        content = update_logo_content(content)
        content = add_cache_busting_version(content)
        
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
                
                # 面包屑、所属版块和导航项
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
                
                # 替换 LOGO & 版本号
                html = update_logo_content(html)
                html = add_cache_busting_version(html)
                
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(html)
        print("Updated HTML files in articles directory")

if __name__ == '__main__':
    replace_text_globally()

