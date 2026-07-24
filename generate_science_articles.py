# -*- coding: utf-8 -*-
import re

def update_templates():
    # 1. 读取本地最新的完美网页
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    with open('vpn-guide.html', 'r', encoding='utf-8') as f:
        vpn_guide_content = f.read()
        
    with open('archives.html', 'r', encoding='utf-8') as f:
        archives_content = f.read()

    # 2. 读取生成器脚本
    with open('write_final_pages.py', 'r', encoding='utf-8') as f:
        script = f.read()

    # 3. 正则替换 index 页面模板 (注意将 f""" 改为普通 """ 避免 {} 字符冲突)
    # 在替换时，由于原始的 HTML 文件里有可能会有三引号 """（比如在 JS、属性里或者正文里），
    # 在 Python 脚本里被包裹在三引号中可能会导致提早结束。
    # 幸好我们检查过，HTML 文件中没有任何连续的三个双引号 """，所以可以直接安全包裹！
    
    # 3.1 替换 index
    pattern_index = re.compile(r'def write_index\(\):\s*html\s*=\s*f?""".*?"""\s*with open\(\'index\.html\'', re.DOTALL)
    replacement_index = 'def write_index():\n    html = """' + index_content.replace('\\', '\\\\').replace('$', '\\$') + '"""\n\n    with open(\'index.html\''
    script, count1 = pattern_index.subn(lambda m: replacement_index, script)
    print(f"Index template replaced: {count1} occurrence(s)")

    # 3.2 替换 vpn-guide
    pattern_vpn = re.compile(r'def write_vpn_guide\(\):\s*html\s*=\s*f?""".*?"""\s*with open\(\'vpn-guide\.html\'', re.DOTALL)
    replacement_vpn = 'def write_vpn_guide():\n    html = """' + vpn_guide_content.replace('\\', '\\\\').replace('$', '\\$') + '"""\n\n    with open(\'vpn-guide.html\''
    script, count2 = pattern_vpn.subn(lambda m: replacement_vpn, script)
    print(f"VPN Guide template replaced: {count2} occurrence(s)")

    # 3.3 替换 archives
    pattern_archives = re.compile(r'def write_archives\(\):\s*html\s*=\s*f?""".*?"""\s*with open\(\'archives\.html\'', re.DOTALL)
    replacement_archives = 'def write_archives():\n    html = """' + archives_content.replace('\\', '\\\\').replace('$', '\\$') + '"""\n\n    with open(\'archives.html\''
    script, count3 = pattern_archives.subn(lambda m: replacement_archives, script)
    print(f"Archives template replaced: {count3} occurrence(s)")

    # 4. 写回脚本
    with open('write_final_pages.py', 'w', encoding='utf-8') as f:
        f.write(script)
    print("write_final_pages.py successfully updated with latest HTML templates!")

if __name__ == '__main__':
    update_templates()

