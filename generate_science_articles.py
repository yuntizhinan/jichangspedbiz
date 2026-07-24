# -*- coding: utf-8 -*-
import os

def replace_text_globally():
    target_old = "科学上网"
    target_new = "科普专栏"
    
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
        content = content.replace("motto\">2026稳定安全高速便宜机场推荐与官网订阅评测", "motto\">2026稳定安全高速便宜机场推荐与官网订阅评测") # 保持motto
        
        # 将 motto 里的“科学上网”换为“科普专栏”
        content = content.replace("提供低门槛的科学上网科普", "提供低门槛的科普专栏")
        content = content.replace("科学上网一站式指南", "科普专栏一站式指南")
        content = content.replace("科学上网配置购买", "科普专栏配置购买")
        
        # 文章定义里也有科学上网
        content = content.replace("OpenWrt科学上网教程", "OpenWrt科普教程")
        content = content.replace("科学上网订阅地址", "网络订阅地址")
        content = content.replace("软路由科学上网深度", "软路由技术科普")
        content = content.replace("自建节点对比专线机场：2026年为什么我不建议新手折腾搭建翻墙？", "自建节点对比专线机场：2026年为什么我不建议新手折腾搭建翻墙？")
        
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
                
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(html)
        print("Updated HTML files in articles directory")

if __name__ == '__main__':
    replace_text_globally()

