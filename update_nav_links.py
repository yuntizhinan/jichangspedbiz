import re

def update_index_nav():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header navigation in index.html (removing the onclick triggers for these two)
    content = content.replace(
        '<a href="index.html?filter=premium" class="nav-link" onclick="setBlogFilter(\'category\', \'premium\'); return false;">优质机场推荐</a>',
        '<a href="articles/premium-airports-for-gaming.html" class="nav-link">优质机场推荐</a>'
    )
    content = content.replace(
        '<a href="index.html?filter=established" class="nav-link" onclick="setBlogFilter(\'category\', \'established\'); return false;">老牌机场推荐</a>',
        '<a href="articles/established-airports-backup.html" class="nav-link">老牌机场推荐</a>'
    )

    # Replace footer navigation in index.html
    content = content.replace(
        '<li><a href="index.html?filter=premium" class="footer-link" onclick="setBlogFilter(\'category\', \'premium\'); return false;">优质机场推荐</a></li>',
        '<li><a href="articles/premium-airports-for-gaming.html" class="footer-link">优质机场推荐</a></li>'
    )
    content = content.replace(
        '<li><a href="index.html?filter=established" class="footer-link" onclick="setBlogFilter(\'category\', \'established\'); return false;">老牌机场推荐</a></li>',
        '<li><a href="articles/established-airports-backup.html" class="footer-link">老牌机场推荐</a></li>'
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html nav updated.")

def update_page_nav(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header nav in subpages (About, VPN client guide)
    content = content.replace(
        '<a href="index.html?filter=premium" class="nav-link">优质机场推荐</a>',
        '<a href="articles/premium-airports-for-gaming.html" class="nav-link">优质机场推荐</a>'
    )
    content = content.replace(
        '<a href="index.html?filter=established" class="nav-link">老牌机场推荐</a>',
        '<a href="articles/established-airports-backup.html" class="nav-link">老牌机场推荐</a>'
    )

    # Replace footer nav in subpages
    content = content.replace(
        '<li><a href="index.html?filter=premium" class="footer-link">优质机场推荐</a></li>',
        '<li><a href="articles/premium-airports-for-gaming.html" class="footer-link">优质机场推荐</a></li>'
    )
    content = content.replace(
        '<li><a href="index.html?filter=established" class="footer-link">老牌机场推荐</a></li>',
        '<li><a href="articles/established-airports-backup.html" class="footer-link">老牌机场推荐</a></li>'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{filename} nav updated.")

if __name__ == '__main__':
    update_index_nav()
    update_page_nav('about.html')
    update_page_nav('vpn-guide.html')
    print("Subpage navigation links updated.")
