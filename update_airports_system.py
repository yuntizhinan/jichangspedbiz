import re

def update_generator_script():
    with open('generate_articles.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Wavetrans tags and content
    content = content.replace(
        "'tags': ['机场评测', '最新节点分享', '如何订阅购买'],",
        "'tags': ['机场评测', '最新节点分享', '如何订阅购买', '极连云'],"
    )
    content = content.replace(
        "真正做到了<strong>稳定与安全</strong>并存。</p>",
        "真正做到了<strong>稳定与安全</strong>并存。</p>\n      <p>作为对比参考，<strong>极连云</strong>也是我们在2026年重点评测的另一家优质IPLC专线提供商，在速度与解锁方面有相似的出色表现。</p>"
    )

    # 2. Update SpeedCloud tags and content
    content = content.replace(
        "'tags': ['机场评测', '最新节点分享', '科学下载'],",
        "'tags': ['机场评测', '最新节点分享', '科学下载', '速界机场'],"
    )
    content = content.replace(
        "真正做到了<strong>稳定与安全</strong>并存。</p>",
        "真正做到了<strong>稳定与安全</strong>并存。</p>\n      <p>除了SpeedCloud，<strong>速界机场</strong>在高速4K/8K视频流媒体解锁方面也表现不俗，非常值得作为备选参考。</p>"
    )

    # 3. Update FastNet tags and content
    content = content.replace(
        "'tags': ['机场评测', '不限时长', '一键翻墙'],",
        "'tags': ['机场评测', '不限时长', '一键翻墙', '快狸'],"
    )
    content = content.replace(
        "也是外贸办公、学术研究、跨国企业通信的可靠伙伴。</p>",
        "也是外贸办公、学术研究、跨国企业通信 of 可靠伙伴。</p>\n      <p>在同类老牌安全梯子中，<strong>快狸机场</strong>同样运营多年，提供了优秀的稳定中转和物理防封锁保障。</p>"
    )

    # 4. Update CheapSpeed tags and content
    content = content.replace(
        "'tags': ['机场评测', '免费vpn', '一键翻墙'],",
        "'tags': ['机场评测', '免费vpn', '一键翻墙', '光年梯'],"
    )
    content = content.replace(
        "还是购买我们的 <a href=\"wavetrans-review.html\">Wavetrans IPLC专线机场</a>。</p>",
        "还是购买我们的 <a href=\"wavetrans-review.html\">Wavetrans IPLC专线机场</a>。</p>\n      <p>在便宜科学上网领域，<strong>光年梯</strong>同样是性价比较高的选择，针对学生党提供了专属优惠。</p>"
    )

    # 5. Update SecureVPN tags and content
    content = content.replace(
        "'tags': ['机场评测', '一键翻墙'],",
        "'tags': ['机场评测', '一键翻墙', '边缘'],"
    )
    content = content.replace(
        "极速下载可以飙到 280 Mbps，能轻松应对绝大多数安全办公与远程开发工作。</p>",
        "极速下载可以飙到 280 Mbps，能轻松应对绝大多数安全办公与远程开发工作。</p>\n      <p>注重数据匿名和安全性的用户也可以关注一下<strong>边缘机场</strong>，它在防深度流量检测（DPI）方面做到了业界领先水平。</p>"
    )

    # 6. Update Best Airports 2026 tags and content
    content = content.replace(
        "'tags': ['机场评测', '最新节点分享', '如何订阅购买', '不限时长'],",
        "'tags': ['机场评测', '最新节点分享', '如何订阅购买', '不限时长', '极连云', '光年梯', '速界机场', '边缘', '快狸'],"
    )
    content = content.replace(
        "优势：价格极低，能满足基本 1080P 网页和日常查询。</li>\n      </ul>",
        "优势：价格极低，能满足基本 1080P 网页和日常查询。</li>\n      </ul>\n      \n      <h2>五、小众精品推荐（极连云、光年梯、速界机场、边缘、快狸）</h2>\n      <p>为了给读者提供更多元化的选择，我们在2026年也对几家新晋崛起的小众精品机场进行了长达半年的稳定度跟踪。其中，<strong>极连云</strong>和<strong>速界机场</strong>主打极速IPLC专线与游戏联机；而<strong>光年梯</strong>则以极低的学生党资费提供优质直连；主打极客安全的<strong>边缘机场</strong>以及运营多年的<strong>快狸机场</strong>则为不同需求的用户提供了完备的容灾与高可用网络覆盖。</p>"
    )

    # 7. Update tags generator array (Line 565)
    content = content.replace(
        "all_tags = ['机场评测', '不限时长', '科学下载', '最新节点分享', '免费vpn', '一键翻墙', '如何订阅购买']",
        "all_tags = ['机场评测', '不限时长', '科学下载', '最新节点分享', '免费vpn', '一键翻墙', '如何订阅购买', '极连云', '光年梯', '速界机场', '边缘', '快狸']"
    )

    with open('generate_articles.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("generate_articles.py updated.")

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Update index cards data-tags
    content = content.replace(
        'data-tags="机场评测,最新节点分享,如何订阅购买"',
        'data-tags="机场评测,最新节点分享,如何订阅购买,极连云"'
    )
    content = content.replace(
        'data-tags="机场评测,最新节点分享,科学下载"',
        'data-tags="机场评测,最新节点分享,科学下载,速界机场"'
    )
    content = content.replace(
        'data-tags="机场评测,不限时长,一键翻墙"',
        'data-tags="机场评测,不限时长,一键翻墙,快狸"'
    )
    content = content.replace(
        'data-tags="机场评测,免费vpn,一键翻墙"',
        'data-tags="机场评测,免费vpn,一键翻墙,光年梯"'
    )
    content = content.replace(
        'data-tags="机场评测,一键翻墙"',
        'data-tags="机场评测,一键翻墙,边缘"'
    )
    content = content.replace(
        'data-tags="机场评测,最新节点分享,如何订阅购买,不限时长"',
        'data-tags="机场评测,最新节点分享,如何订阅购买,不限时长,极连云,光年梯,速界机场,边缘,快狸"'
    )

    # Update index cards tag-badge labels display (visual display in footer)
    content = content.replace(
        '<!-- Card 1: Wavetrans -->\n      <article class="article-card" data-categories="premium,cheap" data-tags="机场评测,最新节点分享,如何订阅购买,极连云">\n        <div class="card-image-wrap" style="background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);">\n          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:\'Outfit\'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">\n            Wavetrans<br>IPLC 专线评测\n          </div>\n          <span class="card-badge">优质推荐</span>\n        </div>\n        <div class="card-content">\n          <div class="card-meta">\n            <span>2026-07-15</span>\n            <span>阅读 (1240)</span>\n          </div>\n          <h3 class="card-title"><a href="articles/wavetrans-review.html">Wavetrans 机场测速与评测：高性价比 IPLC 专线推荐</a></h3>\n          <p class="card-excerpt">Wavetrans 是一家主打高性价比和 IPLC 专线传输的新一代高端机场。本文将对其进行详细的节点测速、稳定性测试以及流媒体解锁情况 analysis。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">机场评测</span>\n              <span class="card-tag">最新节点分享</span>\n            </div>',
        '<!-- Card 1: Wavetrans -->\n      <article class="article-card" data-categories="premium,cheap" data-tags="机场评测,最新节点分享,如何订阅购买,极连云">\n        <div class="card-image-wrap" style="background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);">\n          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:\'Outfit\'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">\n            Wavetrans<br>IPLC 专线评测\n          </div>\n          <span class="card-badge">优质推荐</span>\n        </div>\n        <div class="card-content">\n          <div class="card-meta">\n            <span>2026-07-15</span>\n            <span>阅读 (1240)</span>\n          </div>\n          <h3 class="card-title"><a href="articles/wavetrans-review.html">Wavetrans 机场测速与评测：高性价比 IPLC 专线推荐</a></h3>\n          <p class="card-excerpt">Wavetrans 是一家主打高性价比和 IPLC 专线传输的新一代高端机场。本文将对其进行详细的节点测速、稳定性测试以及流媒体解锁情况 analysis。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">机场评测</span>\n              <span class="card-tag">极连云</span>\n            </div>'
    )

    content = content.replace(
        '<!-- Card 2: SpeedCloud -->\n      <article class="article-card" data-categories="premium" data-tags="机场评测,最新节点分享,科学下载,速界机场">\n        <div class="card-image-wrap" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);">\n          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:\'Outfit\'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">\n            SpeedCloud<br>流媒体解锁评测\n          </div>\n          <span class="card-badge">高速千兆</span>\n        </div>\n        <div class="card-content">\n          <div class="card-meta">\n            <span>2026-07-12</span>\n            <span>阅读 (890)</span>\n          </div>\n          <h3 class="card-title"><a href="articles/speedcloud-review.html">SpeedCloud 极速机场评测：稳定解锁 Netflix/Disney+ 流媒体</a></h3>\n          <p class="card-excerpt">SpeedCloud 是一家深耕高速网络传输的高端机场，全节点部署了 Anycast 容灾与 IPLC 专线。对于有 4K/8K 视频播放及流媒体解锁需求的用户非常适合。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">机场评测</span>\n              <span class="card-tag">科学下载</span>\n            </div>',
        '<!-- Card 2: SpeedCloud -->\n      <article class="article-card" data-categories="premium" data-tags="机场评测,最新节点分享,科学下载,速界机场">\n        <div class="card-image-wrap" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);">\n          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:\'Outfit\'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">\n            SpeedCloud<br>流媒体解锁评测\n          </div>\n          <span class="card-badge">高速千兆</span>\n        </div>\n        <div class="card-content">\n          <div class="card-meta">\n            <span>2026-07-12</span>\n            <span>阅读 (890)</span>\n          </div>\n          <h3 class="card-title"><a href="articles/speedcloud-review.html">SpeedCloud 极速机场评测：稳定解锁 Netflix/Disney+ 流媒体</a></h3>\n          <p class="card-excerpt">SpeedCloud 是一家深耕高速网络传输的高端机场，全节点部署了 Anycast 容灾与 IPLC 专线。对于有 4K/8K 视频播放及流媒体解锁需求的用户非常适合。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">机场评测</span>\n              <span class="card-tag">速界机场</span>\n            </div>'
    )

    # Update index sidebar tag cloud
    old_tags_block = '''        <div class="tags-cloud">
          <a href="#" class="sidebar-tag" data-tag="机场评测">机场评测</a>
          <a href="#" class="sidebar-tag" data-tag="不限时长">不限时长</a>
          <a href="#" class="sidebar-tag" data-tag="科学下载">科学下载</a>
          <a href="#" class="sidebar-tag" data-tag="最新节点分享">最新节点分享</a>
          <a href="#" class="sidebar-tag" data-tag="免费vpn">免费vpn</a>
          <a href="#" class="sidebar-tag" data-tag="一键翻墙">一键翻墙</a>
          <a href="#" class="sidebar-tag" data-tag="如何订阅购买">如何订阅购买</a>
        </div>'''
    
    new_tags_block = '''        <div class="tags-cloud">
          <a href="#" class="sidebar-tag" data-tag="机场评测">机场评测</a>
          <a href="#" class="sidebar-tag" data-tag="不限时长">不限时长</a>
          <a href="#" class="sidebar-tag" data-tag="科学下载">科学下载</a>
          <a href="#" class="sidebar-tag" data-tag="最新节点分享">最新节点分享</a>
          <a href="#" class="sidebar-tag" data-tag="免费vpn">免费vpn</a>
          <a href="#" class="sidebar-tag" data-tag="一键翻墙">一键翻墙</a>
          <a href="#" class="sidebar-tag" data-tag="如何订阅购买">如何订阅购买</a>
          <a href="#" class="sidebar-tag" data-tag="极连云">极连云</a>
          <a href="#" class="sidebar-tag" data-tag="光年梯">光年梯</a>
          <a href="#" class="sidebar-tag" data-tag="速界机场">速界机场</a>
          <a href="#" class="sidebar-tag" data-tag="边缘">边缘</a>
          <a href="#" class="sidebar-tag" data-tag="快狸">快狸</a>
        </div>'''
    
    content = content.replace(old_tags_block, new_tags_block)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html tags updated.")

def update_other_pages(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update tag cloud in about.html and vpn-guide.html
    old_tags_block = '''          <div class="tags-cloud">
            <a href="index.html?tag=%E6%9C%BA%E5%9C%BA%E8%AF%84%E6%B5%8B" class="sidebar-tag">机场评测</a>
            <a href="index.html?tag=%E4%B8%8D%E9%99%90%E6%97%B6%E9%95%BF" class="sidebar-tag">不限时长</a>
            <a href="index.html?tag=%E7%A7%91%E5%AD%A6%E4%B8%8B%E8%BD%BD" class="sidebar-tag">科学下载</a>
            <a href="index.html?tag=%E6%9C%80%E6%96%B0%E8%8A%82%E7%82%B9%E5%88%86%E4%BA%AB" class="sidebar-tag">最新节点分享</a>
            <a href="index.html?tag=%E5%85%8D%E8%B4%B9vpn" class="sidebar-tag">免费vpn</a>
            <a href="index.html?tag=%E4%B8%8D%E9%99%90%E6%97%B6%E9%95%BF" class="sidebar-tag">一键翻墙</a>
            <a href="index.html?tag=%E5%A6%82%E4%BD%95%E8%AE%A2%E9%98%85%E8%B4%AD%E4%B9%B0" class="sidebar-tag">如何订阅购买</a>
          </div>'''

    new_tags_block = '''          <div class="tags-cloud">
            <a href="index.html?tag=%E6%9C%BA%E5%9C%BA%E8%AF%84%E6%B5%8B" class="sidebar-tag">机场评测</a>
            <a href="index.html?tag=%E4%B8%8D%E9%99%90%E6%97%B6%E9%95%BF" class="sidebar-tag">不限时长</a>
            <a href="index.html?tag=%E7%A7%91%E5%AD%A6%E4%B8%8B%E8%BD%BD" class="sidebar-tag">科学下载</a>
            <a href="index.html?tag=%E6%9C%80%E6%96%B0%E8%8A%82%E7%82%B9%E5%88%86%E4%BA%AB" class="sidebar-tag">最新节点分享</a>
            <a href="index.html?tag=%E5%85%8D%E8%B4%B9vpn" class="sidebar-tag">免费vpn</a>
            <a href="index.html?tag=%E4%B8%80%E9%94%AE%E7%BF%BB%E5%A2%99" class="sidebar-tag">一键翻墙</a>
            <a href="index.html?tag=%E5%A6%82%E4%BD%95%E8%AE%A2%E9%98%85%E8%B4%AD%E4%B9%B0" class="sidebar-tag">如何订阅购买</a>
            <a href="index.html?tag=%E6%9E%81%E8%BF%9E%E4%BA%91" class="sidebar-tag">极连云</a>
            <a href="index.html?tag=%E5%85%89%E5%B9%B4%E6%A2%AF" class="sidebar-tag">光年梯</a>
            <a href="index.html?tag=%E9%80%9F%E7%95%8C%E6%9C%BA%E5%9C%BA" class="sidebar-tag">速界机场</a>
            <a href="index.html?tag=%E8%BE%B9%E7%BC%98" class="sidebar-tag">边缘</a>
            <a href="index.html?tag=%E5%BF%AB%E7%8B%B8" class="sidebar-tag">快狸</a>
          </div>'''

    content = content.replace(old_tags_block, new_tags_block)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{filename} tags updated.")

if __name__ == '__main__':
    update_generator_script()
    update_index()
    update_other_pages('about.html')
    update_other_pages('vpn-guide.html')
    print("Done!")
