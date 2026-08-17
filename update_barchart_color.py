import os
import re

file_path = r'C:\Users\psyto\Desktop\jichangsped.biz\articles\airport-guide-2026.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace background:var(--accent-primary) with a light, fresh sky-blue gradient
new_content = content.replace('background:var(--accent-primary)', 'background:linear-gradient(90deg, #bae6fd, #38bdf8)')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated bar chart colors to light sky blue.")
