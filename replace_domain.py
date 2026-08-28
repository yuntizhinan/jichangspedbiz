# -*- coding: utf-8 -*-
import os

target_dir = os.path.dirname(os.path.abspath(__file__))

extensions = ('.py', '.js', '.html', '.xml', '.txt', '.json', '.md')
exclude_dirs = {'.git', '__pycache__', 'node_modules', '.vscode', '.idea'}

replacements = [
    ('https://jichangspeed.biz/', 'https://vpnstuijian.com/'),
    ('https://jichangspeed.biz', 'https://vpnstuijian.com'),
    ('http://jichangspeed.biz', 'https://vpnstuijian.com'),
    ('https://jichangsped.biz/', 'https://vpnstuijian.com/'),
    ('https://jichangsped.biz', 'https://vpnstuijian.com'),
    ('http://jichangsped.biz', 'https://vpnstuijian.com'),
    ('jichangspeed.biz', 'vpnstuijian.com'),
    ('jichangsped.biz', 'vpnstuijian.com'),
]

updated_files = []

for root, dirs, files in os.walk(target_dir):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith(extensions) and file not in ('replace_domain.py', 'main.js'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for old_str, new_str in replacements:
                    new_content = new_content.replace(old_str, new_str)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    rel_path = os.path.relpath(filepath, target_dir)
                    updated_files.append(rel_path)
                    print(f"Updated: {rel_path}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"\nFinished updating {len(updated_files)} files.")

