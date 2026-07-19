import re

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Define all replacements for the 15 cards in index.html
    replacements = {
        # Card 1: Wavetrans
        'data-tags="Wavetrans,IPLC专线,高性价比,流媒体解锁"': 'data-tags="机场评测,最新节点分享,如何订阅购买"',
        '<span class="card-tag">IPLC专线</span>\n              <span class="card-tag">高性价比</span>': 
        '<span class="card-tag">机场评测</span>\n              <span class="card-tag">最新节点分享</span>',

        # Card 2: SpeedCloud
        'data-tags="SpeedCloud,高速,流媒体解锁,全平台支持"': 'data-tags="机场评测,最新节点分享,科学下载"',
        '<span class="card-tag">流媒体解锁</span>\n              <span class="card-tag">高速</span>':
        '<span class="card-tag">机场评测</span>\n              <span class="card-tag">科学下载</span>',

        # Card 3: FastNet
        'data-tags="FastNet,老牌机场,稳定,安全"': 'data-tags="机场评测,不限时长,一键翻墙"',
        '<span class="card-tag">老牌机场</span>\n              <span class="card-tag">稳定</span>':
        '<span class="card-tag">机场评测</span>\n              <span class="card-tag">不限时长</span>',

        # Card 4: CheapSpeed
        'data-tags="CheapSpeed,便宜机场,高性价比"': 'data-tags="机场评测,免费vpn,一键翻墙"',
        '<span class="card-tag">便宜机场</span>\n              <span class="card-tag">高性价比</span>':
        '<span class="card-tag">机场评测</span>\n              <span class="card-tag">免费vpn</span>',

        # Card 5: IPLC vs Direct
        'data-tags="IPLC专线,稳定,高速"': 'data-tags="最新节点分享,科学下载"',
        # (This card uses custom layout/tag strings, we will handle specifically)

        # Card 6: Client Config
        'data-tags="科学上网,全平台支持,Clash,Shadowrocket"': 'data-tags="科学下载,一键翻墙,如何订阅购买"',
        # Handled in replacements for tag list:

        # Card 7: SecureVPN
        'data-tags="SecureVPN,安全,稳定"': 'data-tags="机场评测,一键翻墙"',

        # Card 8: Best Airports 2026
        'data-tags="精选汇总,稳定,高性价比,便宜机场,优质机场,老牌机场"': 'data-tags="机场评测,最新节点分享,如何订阅购买,不限时长"',

        # Card 9: Premium for Gaming
        'data-tags="优质机场,高速,稳定,IPLC专线"': 'data-tags="机场评测,科学下载,最新节点分享"',

        # Card 10: How to choose
        'data-tags="科学上网,稳定,安全,高性价比"': 'data-tags="如何订阅购买,一键翻墙"',

        # Card 11: Established backup
        'data-tags="老牌机场,稳定,安全"': 'data-tags="机场评测,不限时长,如何订阅购买"',

        # Card 12: Cheap for students
        'data-tags="便宜机场,高性价比,流媒体解锁"': 'data-tags="免费vpn,机场评测"',

        # Card 13: Streaming Unlock
        'data-tags="流媒体解锁,IPLC专线,高速,全平台支持"': 'data-tags="机场评测,科学下载"',

        # Card 14: Cross Platform (shares tag pattern with card 6, handled selectively)
        # Card 15: Best deals
        'data-tags="IPLC专线,高性价比,便宜机场,精选汇总"': 'data-tags="如何订阅购买,最新节点分享,免费vpn"',
    }

    # Apply standard tag-block replacements
    for src, dst in replacements.items():
        content = content.replace(src, dst)

    # Detailed card tag list updates
    # Card 5 tags
    content = content.replace(
        '<article class="article-card" data-tags="最新节点分享,科学下载">\n        <div class="card-image-wrap" style="background: linear-gradient(135deg, #ec4899 0%, #db2777 100%);">\n          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:\'Outfit\'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">\n            科普：IPLC<br>与直连区别\n          </div>\n          <span class="card-badge">技术科普</span>\n        </div>\n        <div class="card-content">\n          <div class="card-meta">\n            <span>2026-06-28</span>\n            <span>阅读 (940)</span>\n          </div>\n          <h3 class="card-title"><a href="articles/iplc-vs-direct.html">IPLC 专线与普通直连有什么区别？为什么选择 IPLC 机场？</a></h3>\n          <p class="card-excerpt">在选购机场时，你常常会看到“IPLC专线”和“直连/中转”等字眼。这两者到底有何区别？为什么专线机场的稳定性会高出几个量级？本文通俗科普。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">IPLC专线</span>\n              <span class="card-tag">稳定</span>\n            </div>',
        '<article class="article-card" data-tags="最新节点分享,科学下载">\n        <div class="card-image-wrap" style="background: linear-gradient(135deg, #ec4899 0%, #db2777 100%);">\n          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:\'Outfit\'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">\n            科普：IPLC<br>与直连区别\n          </div>\n          <span class="card-badge">技术科普</span>\n        </div>\n        <div class="card-content">\n          <div class="card-meta">\n            <span>2026-06-28</span>\n            <span>阅读 (940)</span>\n          </div>\n          <h3 class="card-title"><a href="articles/iplc-vs-direct.html">IPLC 专线与普通直连有什么区别？为什么选择 IPLC 机场？</a></h3>\n          <p class="card-excerpt">在选购机场时，你常常会看到“IPLC专线”和“直连/中转”等字眼。这两者到底有何区别？为什么专线机场的稳定性会高出几个量级？本文通俗科普。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">最新节点分享</span>\n              <span class="card-tag">科学下载</span>\n            </div>'
    )

    # Card 6 tags
    content = content.replace(
        '<article class="article-card" data-tags="科学下载,一键翻墙,如何订阅购买">\n        <div class="card-image-wrap" style="background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);">\n          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:\'Outfit\'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">\n            全平台<br>客户端配置\n          </div>\n          <span class="card-badge">新手必看</span>\n        </div>\n        <div class="card-content">\n          <div class="card-meta">\n            <span>2026-06-25</span>\n            <span>阅读 (2310)</span>\n          </div>\n          <h3 class="card-title"><a href="articles/vpn-clients-guide.html">2026 最新科学上网客户端下载与配置指南 (Clash/Shadowrocket/V2rayN)</a></h3>\n          <p class="card-excerpt">拥有了优质的机场订阅，还需要一款好用的客户端才能起飞。本文汇总了 Windows, macOS, iOS 和 Android 平台最主流的客户端配置教程。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">科学上网</span>\n              <span class="card-tag">全平台支持</span>\n            </div>',
        '<article class="article-card" data-tags="科学下载,一键翻墙,如何订阅购买">\n        <div class="card-image-wrap" style="background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);">\n          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:\'Outfit\'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">\n            全平台<br>客户端配置\n          </div>\n          <span class="card-badge">新手必看</span>\n        </div>\n        <div class="card-content">\n          <div class="card-meta">\n            <span>2026-06-25</span>\n            <span>阅读 (2310)</span>\n          </div>\n          <h3 class="card-title"><a href="articles/vpn-clients-guide.html">2026 最新科学上网客户端下载与配置指南 (Clash/Shadowrocket/V2rayN)</a></h3>\n          <p class="card-excerpt">拥有了优质的机场订阅，还需要一款好用的客户端才能起飞。本文汇总了 Windows, macOS, iOS 和 Android 平台最主流的客户端配置教程。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">科学下载</span>\n              <span class="card-tag">如何订阅购买</span>\n            </div>'
    )

    # Card 7 tags
    content = content.replace(
        'h3 class="card-title"><a href="articles/securevpn-review.html">SecureVPN 机场评测：主打安全与隐私的无日志高端机场</a></h3>\n          <p class="card-excerpt">在网络安全日益重要的今天，个人隐私不容忽视。SecureVPN 专为对安全性、匿名性有极端高要求的极客与商务人士打造，全站实行严格无日志审计。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">安全</span>\n              <span class="card-tag">稳定</span>\n            </div>',
        'h3 class="card-title"><a href="articles/securevpn-review.html">SecureVPN 机场评测：主打安全与隐私的无日志高端机场</a></h3>\n          <p class="card-excerpt">在网络安全日益重要的今天，个人隐私不容忽视。SecureVPN 专为对安全性、匿名性有极端高要求的极客与商务人士打造，全站实行严格无日志审计。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">机场评测</span>\n              <span class="card-tag">一键翻墙</span>\n            </div>'
    )

    # Card 8 tags
    content = content.replace(
        'h3 class="card-title"><a href="articles/best-airports-2026.html">精选汇总：2026 年最值得推荐的稳定好用机场梯子合集</a></h3>\n          <p class="card-excerpt">面对市场上成千上万家机场，如何避免踩雷？我们根据过去一年的实测数据，筛选出了在速度、稳定度、性价比和客服售后等方面表现最优秀的机场。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">精选汇总</span>\n              <span class="card-tag">高性价比</span>\n            </div>',
        'h3 class="card-title"><a href="articles/best-airports-2026.html">精选汇总：2026 年最值得推荐的稳定好用机场梯子合集</a></h3>\n          <p class="card-excerpt">面对市场上成千上万家机场，如何避免踩雷？我们根据过去一年的实测数据，筛选出了在速度、稳定度、性价比和客服售后等方面表现最优秀的机场。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">机场评测</span>\n              <span class="card-tag">最新节点分享</span>\n            </div>'
    )

    # Card 9 tags
    content = content.replace(
        'h3 class="card-title"><a href="articles/premium-airports-for-gaming.html">优质机场推荐：适合游戏加速与 4K 视频播放的低延迟机场</a></h3>\n          <p class="card-excerpt">网络联机游戏（如 Steam 游戏、Apex 英雄、英雄联盟手游）对网络延迟和丢包率有着极高的要求。本文为你推荐几款低延迟优质游戏机场。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">优质机场</span>\n              <span class="card-tag">IPLC专线</span>\n            </div>',
        'h3 class="card-title"><a href="articles/premium-airports-for-gaming.html">优质机场推荐：适合游戏加速与 4K 视频播放的低延迟机场</a></h3>\n          <p class="card-excerpt">网络联机游戏（如 Steam 游戏、Apex 英雄、英雄联盟手游）对网络延迟 and 丢包率有着极高的要求。本文为你推荐几款低延迟优质游戏机场。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">机场评测</span>\n              <span class="card-tag">科学下载</span>\n            </div>'
    )

    # Card 10 tags
    content = content.replace(
        'h3 class="card-title"><a href="articles/how-to-choose-airport.html">如何选择适合自己的机场？稳定、安全、性价比多维度对比</a></h3>\n          <p class="card-excerpt">新手在面对市面上形形色色的机场套餐时往往不知从何下手。本文将通过稳定度、安全性、流量价格、客户端兼容等多个维度教你如何科学选购。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">稳定</span>\n              <span class="card-tag">高性价比</span>\n            </div>',
        'h3 class="card-title"><a href="articles/how-to-choose-airport.html">如何选择适合自己的机场？稳定、安全、性价比多维度对比</a></h3>\n          <p class="card-excerpt">新手在面对市面上形形色色的机场套餐时往往不知从何下手。本文将通过稳定度、安全性、流量价格、客户端兼容等多个维度教你如何科学选购。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">如何订阅购买</span>\n              <span class="card-tag">一键翻墙</span>\n            </div>'
    )

    # Card 11 tags
    content = content.replace(
        'h3 class="card-title"><a href="articles/established-airports-backup.html">老牌机场推荐：网络不中断的备用梯子与高可用服务推荐</a></h3>\n          <p class="card-excerpt">俗话说“鸡蛋不要放在同一个篮子里”。对于依靠跨境网络办公的用户，拥有一个稳定高可用的老牌备用机场能够确保网络永不断线。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">老牌机场</span>\n              <span class="card-tag">稳定</span>\n            </div>',
        'h3 class="card-title"><a href="articles/established-airports-backup.html">老牌机场推荐：网络不中断的备用梯子与高可用服务推荐</a></h3>\n          <p class="card-excerpt">俗话说“鸡蛋不要放在同一个篮子里”。对于依靠跨境网络办公的用户，拥有一个稳定高可用的老牌备用机场能够确保网络永不断线。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">机场评测</span>\n              <span class="card-tag">不限时长</span>\n            </div>'
    )

    # Card 12 tags
    content = content.replace(
        'h3 class="card-title"><a href="articles/cheap-airports-for-students.html">便宜好用机场推荐：学生党与轻度用户的性价比之选</a></h3>\n          <p class="card-excerpt">没有收入来源的学生党和偶尔看一眼外网的轻度用户，最希望把成本压缩在 10 元以内。本文精心挑选并实测了几款便宜好用的入门级机场。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">便宜机场</span>\n              <span class="card-tag">高性价比</span>\n            </div>',
        'h3 class="card-title"><a href="articles/cheap-airports-for-students.html">便宜好用机场推荐：学生党与轻度用户的性价比之选</a></h3>\n          <p class="card-excerpt">没有收入来源的学生党和偶尔看一眼外网的轻度用户，最希望把成本压缩在 10 元以内。本文精心挑选并实测了几款便宜好用的入门级机场。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">免费vpn</span>\n              <span class="card-tag">机场评测</span>\n            </div>'
    )

    # Card 13 tags
    content = content.replace(
        'h3 class="card-title"><a href="articles/streaming-unlock-guide.html">流媒体解锁指南：如何利用专线机场畅看海外流媒体</a></h3>\n          <p class="card-excerpt">买了 Netflix/Disney+ 账号却提示“正在使用代理”？本文为你揭秘海外流媒体的防封锁机制，并教你如何利用专线机场完美解锁。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">流媒体解锁</span>\n              <span class="card-tag">高速</span>\n            </div>',
        'h3 class="card-title"><a href="articles/streaming-unlock-guide.html">流媒体解锁指南：如何利用专线机场畅看海外流媒体</a></h3>\n          <p class="card-excerpt">买了 Netflix/Disney+ 账号却提示“正在使用代理”？本文为你揭秘海外流媒体的防封锁机制，并教你如何利用专线机场完美解锁。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">机场评测</span>\n              <span class="card-tag">科学下载</span>\n            </div>'
    )

    # Card 14 tags
    content = content.replace(
        '<article class="article-card" data-tags="一键翻墙,科学下载">\n        <div class="card-image-wrap" style="background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);">\n          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:\'Outfit\'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">\n            全终端<br>翻墙配置教程\n          </div>\n          <span class="card-badge">小白科普</span>\n        </div>\n        <div class="card-content">\n          <div class="card-meta">\n            <span>2026-05-10</span>\n            <span>阅读 (1420)</span>\n          </div>\n          <h3 class="card-title"><a href="articles/cross-platform-setup.html">全平台科学上网配置：从 Windows 到 iOS/Android 机场配置教程</a></h3>\n          <p class="card-excerpt">拥有了多设备的你，如何让所有终端都顺利实现翻墙？本文提供一站式配置教程，从电脑、手机到电视盒子、路由器一应俱全。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">全平台支持</span>\n              <span class="card-tag">科学上网</span>\n            </div>',
        '<article class="article-card" data-tags="一键翻墙,科学下载">\n        <div class="card-image-wrap" style="background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);">\n          <div style="display: flex; align-items: center; justify-content: center; height:100%; color:#fff; font-family:\'Outfit\'; font-weight:800; font-size:1.5rem; text-align:center; padding: 20px;">\n            全终端<br>翻墙配置教程\n          </div>\n          <span class="card-badge">小白科普</span>\n        </div>\n        <div class="card-content">\n          <div class="card-meta">\n            <span>2026-05-10</span>\n            <span>阅读 (1420)</span>\n          </div>\n          <h3 class="card-title"><a href="articles/cross-platform-setup.html">全平台科学上网配置：从 Windows 到 iOS/Android 机场配置教程</a></h3>\n          <p class="card-excerpt">拥有了多设备的你，如何让所有终端都顺利实现翻墙？本文提供一站式配置教程，从电脑、手机到电视盒子、路由器一应俱全。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">一键翻墙</span>\n              <span class="card-tag">科学下载</span>\n            </div>'
    )

    # Card 15 tags
    content = content.replace(
        'h3 class="card-title"><a href="articles/best-deals-airports.html">高性价比 IPLC 机场推荐：双十一与日常优惠力度最大的机场盘点</a></h3>\n          <p class="card-excerpt">想要购买稳定的专线机场，又觉得原价稍微有些高？本文为你盘点各大主流高口碑机场的日常打折规律、优惠码，帮你大幅省钱。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">IPLC专线</span>\n              <span class="card-tag">高性价比</span>\n            </div>',
        'h3 class="card-title"><a href="articles/best-deals-airports.html">高性价比 IPLC 机场推荐：双十一与日常优惠力度最大的机场盘点</a></h3>\n          <p class="card-excerpt">想要购买稳定的专线机场，又觉得原价稍微有些高？本文为你盘点各大主流高口碑机场的日常打折规律、优惠码，帮你大幅省钱。</p>\n          <div class="card-footer">\n            <div class="card-tags">\n              <span class="card-tag">如何订阅购买</span>\n              <span class="card-tag">免费vpn</span>\n            </div>'
    )

    # Sidebar Tag Cloud in index.html (replace Widget 1)
    old_sidebar_tags = '''        <h3 class="widget-title">
          <svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 8.25c-.97 0-1.75-.78-1.75-1.75s.78-1.75 1.75-1.75 1.75.78 1.75 1.75S6.47 8.25 5.5 8.25z"/></svg>
          热门机场标签
        </h3>
        <div class="tags-cloud">
          <a href="#" class="sidebar-tag" data-tag="Wavetrans">Wavetrans</a>
          <a href="#" class="sidebar-tag" data-tag="SpeedCloud">SpeedCloud</a>
          <a href="#" class="sidebar-tag" data-tag="FastNet">FastNet</a>
          <a href="#" class="sidebar-tag" data-tag="CheapSpeed">CheapSpeed</a>
          <a href="#" class="sidebar-tag" data-tag="SecureVPN">SecureVPN</a>
          <a href="#" class="sidebar-tag" data-tag="IPLC专线">IPLC专线</a>
          <a href="#" class="sidebar-tag" data-tag="高速">高速</a>
          <a href="#" class="sidebar-tag" data-tag="稳定">稳定</a>
          <a href="#" class="sidebar-tag" data-tag="安全">安全</a>
          <a href="#" class="sidebar-tag" data-tag="高性价比">高性价比</a>
          <a href="#" class="sidebar-tag" data-tag="流媒体解锁">流媒体解锁</a>
          <a href="#" class="sidebar-tag" data-tag="全平台支持">全平台支持</a>
          <a href="#" class="sidebar-tag" data-tag="科学上网">科学上网</a>
          <a href="#" class="sidebar-tag" data-tag="Clash">Clash</a>
          <a href="#" class="sidebar-tag" data-tag="Shadowrocket">Shadowrocket</a>
        </div>'''

    new_sidebar_tags = '''        <h3 class="widget-title">
          <svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 8.25c-.97 0-1.75-.78-1.75-1.75s.78-1.75 1.75-1.75 1.75.78 1.75 1.75S6.47 8.25 5.5 8.25z"/></svg>
          热门标签
        </h3>
        <div class="tags-cloud">
          <a href="#" class="sidebar-tag" data-tag="机场评测">机场评测</a>
          <a href="#" class="sidebar-tag" data-tag="不限时长">不限时长</a>
          <a href="#" class="sidebar-tag" data-tag="科学下载">科学下载</a>
          <a href="#" class="sidebar-tag" data-tag="最新节点分享">最新节点分享</a>
          <a href="#" class="sidebar-tag" data-tag="免费vpn">免费vpn</a>
          <a href="#" class="sidebar-tag" data-tag="一键翻墙">一键翻墙</a>
          <a href="#" class="sidebar-tag" data-tag="如何订阅购买">如何订阅购买</a>
        </div>'''

    content = content.replace(old_sidebar_tags, new_sidebar_tags)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated.")

def update_page_sidebar(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the tag sidebar in subpages
    old_block_regex = r'<h3 class="widget-title">\s*<svg.*?>.*?</svg>\s*热门机场标签\s*</h3>\s*<div class="tags-cloud">.*?</div>'
    
    new_block = '''<h3 class="widget-title">
            <svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 8.25c-.97 0-1.75-.78-1.75-1.75s.78-1.75 1.75-1.75 1.75.78 1.75 1.75S6.47 8.25 5.5 8.25z"/></svg>
            热门标签
          </h3>
          <div class="tags-cloud">
            <a href="index.html?tag=%E6%9C%BA%E5%9C%BA%E8%AF%84%E6%B5%8B" class="sidebar-tag">机场评测</a>
            <a href="index.html?tag=%E4%B8%8D%E9%99%90%E6%97%B6%E9%95%BF" class="sidebar-tag">不限时长</a>
            <a href="index.html?tag=%E7%A7%91%E5%AD%A6%E4%B8%8B%E8%BD%BD" class="sidebar-tag">科学下载</a>
            <a href="index.html?tag=%E6%9C%80%E6%96%B0%E8%8A%82%E7%82%B9%E5%88%86%E4%BA%AB" class="sidebar-tag">最新节点分享</a>
            <a href="index.html?tag=%E5%85%8D%E8%B4%B9vpn" class="sidebar-tag">免费vpn</a>
            <a href="index.html?tag=%E4%B8%8D%E9%99%90%E6%97%B6%E9%95%BF" class="sidebar-tag">一键翻墙</a>
            <a href="index.html?tag=%E5%A6%82%E4%BD%95%E8%AE%A2%E9%98%85%E8%B4%AD%E4%B9%B0" class="sidebar-tag">如何订阅购买</a>
          </div>'''
    
    content = re.sub(old_block_regex, new_block, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{filename} updated.")

if __name__ == '__main__':
    update_index()
    update_page_sidebar('about.html')
    update_page_sidebar('vpn-guide.html')
    print("Done updating everywhere!")
