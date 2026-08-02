# -*- coding: utf-8 -*-
import os
import re
import json

def optimize_article_head(filepath):
    filename = os.path.basename(filepath)
    slug = os.path.splitext(filename)[0]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Extract Title
    title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    title = title_match.group(1) if title_match else filename
    clean_title = title.split(" - ")[0].strip()
    
    # Extract Description
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html, re.IGNORECASE)
    description = desc_match.group(1).strip() if desc_match else f"{clean_title} - 机场速递专业科普与配置指南。"
    
    # Extract Keywords
    kw_match = re.search(r'<meta\s+name="keywords"\s+content="([^"]*)"', html, re.IGNORECASE)
    keywords = kw_match.group(1).strip() if kw_match else "机场推荐, 科学上网, 翻墙教程"
    
    # Clean out any old injected metadata from head if present
    html = re.sub(r'<!-- SEO/GEO Injected Metadata Start -->.*?<!-- SEO/GEO Injected Metadata End -->', '', html, flags=re.DOTALL)
    html = re.sub(r'<meta name="robots" content="[^"]*">', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<link rel="canonical" href="[^"]*">', '', html, flags=re.IGNORECASE)
    
    canonical_url = f"https://jichangspeed.biz/articles/{filename}"
    
    head_metadata = f"""<!-- SEO/GEO Injected Metadata Start -->
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{canonical_url}">
  <!-- OpenGraph Meta Tags -->
  <meta property="og:site_name" content="机场速递 (jichangspeed.biz)">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{clean_title} - 机场速递">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://i.ibb.co/tpkZpVhs/sujielogo.webp">
  <!-- Twitter Card Meta Tags -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{clean_title} - 机场速递">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="https://i.ibb.co/tpkZpVhs/sujielogo.webp">
  <!-- Schema.org JSON-LD Structured Data for AI & Search Engines -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "TechArticle",
        "@id": "{canonical_url}#article",
        "isPartOf": {{
          "@type": "WebPage",
          "@id": "{canonical_url}"
        }},
        "headline": "{clean_title}",
        "description": "{description}",
        "inLanguage": "zh-CN",
        "publisher": {{
          "@type": "Organization",
          "name": "机场速递",
          "url": "https://jichangspeed.biz/"
        }}
      }}
    ]
  }}
  </script>
  <!-- SEO/GEO Injected Metadata End -->"""

    # Inject into </head>
    if '</head>' in html:
        html = html.replace('</head>', f'{head_metadata}\n</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Successfully injected head SEO/GEO metadata into: {filepath}")

def main():
    articles_dir = "articles"
    if not os.path.exists(articles_dir):
        print(f"Directory {articles_dir} not found.")
        return
        
    for filename in os.listdir(articles_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(articles_dir, filename)
            optimize_article_head(filepath)

if __name__ == "__main__":
    main()
