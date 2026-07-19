# -*- coding: utf-8 -*-
import os

files_to_update = [
    'generate_final_site.py',
    'write_final_pages.py',
    'generate_articles.py',
    'generate_articles.js',
    'robots.txt'
]

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace('jichangsped.biz', 'jichangspeed.biz')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated domains in: {filename}")
    else:
        print(f"File not found, skipping: {filename}")

print("Domain replacement complete.")
