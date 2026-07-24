document.addEventListener('DOMContentLoaded', () => {
  // ==========================================
  // THEME TOGGLE
  // ==========================================
  const themeToggle = document.getElementById('theme-toggle');
  
  // Check for saved theme preference, otherwise use system preference
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      let newTheme = 'light';
      if (currentTheme === 'light') {
        newTheme = 'dark';
      }
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
    });
  }

  // ==========================================
  // MOBILE MENU TOGGLE
  // ==========================================
  const menuToggle = document.getElementById('menu-toggle');
  const navMenu = document.getElementById('nav-menu');

  if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!menuToggle.contains(e.target) && !navMenu.contains(e.target)) {
        navMenu.classList.remove('active');
      }
    });
  }

  // ==========================================
  // FAQ ACCORDION
  // ==========================================
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const trigger = item.querySelector('.faq-trigger');
    if (trigger) {
      trigger.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        // Close other active FAQs
        faqItems.forEach(otherItem => {
          otherItem.classList.remove('active');
        });
        // Toggle current FAQ
        if (!isActive) {
          item.classList.add('active');
        }
      });
    }
  });

  // ==========================================
  // CONTENT FILTERING & PAGINATION SYSTEM
  // ==========================================
  const articleCards    = document.querySelectorAll('.article-card');
  const sidebarTags     = document.querySelectorAll('.sidebar-tag');
  const filterIndicator = document.getElementById('active-filter-indicator');
  const filterLabel     = document.getElementById('filter-label');
  const searchInput     = document.getElementById('search-input');

  let currentFilter = { type: 'all', value: '' };

  const CARDS_PER_PAGE = 8;
  let currentPage = 1;

  function getMatchedCards(searchVal) {
    const matched = [];
    articleCards.forEach(card => {
      const cardCategories = card.dataset.categories ? card.dataset.categories.split(',') : [];
      const cardTags       = card.dataset.tags       ? card.dataset.tags.split(',')       : [];
      const cardTitle      = card.querySelector('.card-title').textContent.toLowerCase();
      const cardExcerpt    = card.querySelector('.card-excerpt').textContent.toLowerCase();

      let matchesFilter = true;
      if (currentFilter.type === 'category') {
        matchesFilter = cardCategories.includes(currentFilter.value);
      } else if (currentFilter.type === 'tag') {
        matchesFilter = cardTags.includes(currentFilter.value);
      }

      let matchesSearch = true;
      if (searchVal) {
        matchesSearch = cardTitle.includes(searchVal) ||
                        cardExcerpt.includes(searchVal) ||
                        cardTags.some(t => t.toLowerCase().includes(searchVal));
      }

      if (matchesFilter && matchesSearch) matched.push(card);
    });
    return matched;
  }

  function renderPagination(totalCards) {
    const isHomepage = !!document.querySelector('.hero-section');
    if (!isHomepage) return;

    let pagerEl = document.getElementById('pagination-bar');
    if (!pagerEl) {
      pagerEl = document.createElement('div');
      pagerEl.id = 'pagination-bar';
      pagerEl.style.cssText = `
        display: flex; align-items: center; justify-content: center;
        gap: 6px; padding: 24px 0 8px; flex-wrap: wrap;
      `;
      const feed = document.querySelector('.content-feed');
      if (feed) feed.appendChild(pagerEl);
    }

    const totalPages = Math.ceil(totalCards / CARDS_PER_PAGE);
    // Hide pagination when filtering/searching (show all results)
    const searchVal = searchInput ? searchInput.value.toLowerCase().trim() : '';
    if (currentFilter.type !== 'all' || searchVal || totalPages <= 1) {
      pagerEl.style.display = 'none';
      return;
    }
    pagerEl.style.display = 'flex';
    pagerEl.className = 'pagination';

    let html = `<button class="pager-btn" ${currentPage === 1 ? 'disabled' : ''}
      onclick="goToPage(${currentPage - 1})">上一页</button>`;

    for (let p = 1; p <= totalPages; p++) {
      html += `<button class="pager-btn ${p === currentPage ? 'active' : ''}"
        onclick="goToPage(${p})">${p}</button>`;
    }

    html += `<button class="pager-btn" ${currentPage === totalPages ? 'disabled' : ''}
      onclick="goToPage(${currentPage + 1})">下一页</button>`;

    pagerEl.innerHTML = html;
  }

  window.goToPage = function(page) {
    const searchVal = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const matched = getMatchedCards(searchVal);
    const totalPages = Math.ceil(matched.length / CARDS_PER_PAGE);
    if (page < 1 || page > totalPages) return;
    currentPage = page;
    updateArticlesVisibility();
    // Scroll to top of feed
    const feedSection = document.getElementById('articles-feed-section');
    if (feedSection) {
      window.scrollTo({ top: feedSection.getBoundingClientRect().top + window.pageYOffset - 80, behavior: 'smooth' });
    }
  };

  function updateArticlesVisibility() {
    const searchVal = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const isHomepage = !!document.querySelector('.hero-section');
    const matched = getMatchedCards(searchVal);

    // Pagination only on homepage with no active filter/search
    const usePagination = isHomepage && currentFilter.type === 'all' && !searchVal;
    const totalPages = Math.ceil(matched.length / CARDS_PER_PAGE);
    if (usePagination && currentPage > totalPages) currentPage = 1;

    const startIdx = usePagination ? (currentPage - 1) * CARDS_PER_PAGE : 0;
    const endIdx   = usePagination ? startIdx + CARDS_PER_PAGE : matched.length;

    const matchedSet = new Set(matched);
    let visibleCount = 0;
    articleCards.forEach(card => {
      if (!matchedSet.has(card)) {
        card.classList.add('card-hidden');
        return;
      }
      const idx = matched.indexOf(card);
      if (idx >= startIdx && idx < endIdx) {
        card.classList.remove('card-hidden');
        visibleCount++;
      } else {
        card.classList.add('card-hidden');
      }
    });

    renderPagination(matched.length);

    // Update filter UI indicator
    if (filterIndicator && filterLabel) {
      if (currentFilter.type !== 'all' || searchVal) {
        filterIndicator.style.display = 'inline-block';
        if (currentFilter.type === 'category') {
          const catNames = {
            'cheap': '便宜机场推荐',
            'premium': '优质机场推荐',
            'established': '老牌机场推荐',
            'curated': '精选汇总'
          };
          filterLabel.textContent = catNames[currentFilter.value] || currentFilter.value;
        } else if (currentFilter.type === 'tag') {
          filterLabel.textContent = `标签: ${currentFilter.value}`;
        } else if (searchVal) {
          filterLabel.textContent = `搜索: "${searchVal}"`;
        }
      } else {
        filterIndicator.style.display = 'none';
      }
    }

    // Handle empty state
    let emptyState = document.getElementById('empty-feed-state');
    if (visibleCount === 0 && articleCards.length > 0) {
      if (!emptyState) {
        emptyState = document.createElement('div');
        emptyState.id = 'empty-feed-state';
        emptyState.classList.remove('card-hidden');
        emptyState.style.padding = '40px 20px';
        emptyState.style.textAlign = 'center';
        emptyState.style.backgroundColor = 'var(--bg-secondary)';
        emptyState.style.border = '1px solid var(--border-color)';
        emptyState.style.borderRadius = 'var(--radius-md)';
        emptyState.innerHTML = `
          <svg style="width: 48px; height: 48px; fill: var(--text-muted); margin-bottom: 12px;" viewBox="0 0 24 24">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/>
          </svg>
          <h3 style="margin-bottom: 8px;">没有找到匹配的文章</h3>
          <p style="color: var(--text-muted); font-size: 0.9rem;">请尝试更换关键字或浏览其他分类。</p>
        `;
        const feed = document.querySelector('.content-feed');
        if (feed) feed.appendChild(emptyState);
      } else {
        emptyState.style.display = 'block';
      }
    } else if (emptyState) {
      emptyState.style.display = 'none';
    }
  }

  // Set filter programmatically
  window.setBlogFilter = function(type, value) {
    currentFilter.type = type;
    currentFilter.value = value;
    currentPage = 1;

    sidebarTags.forEach(tag => {
      if (type === 'tag' && tag.dataset.tag === value) {
        tag.classList.add('active');
      } else {
        tag.classList.remove('active');
      }
    });

    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (type === 'category' && href && href.includes(`filter=${value}`)) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });

    updateArticlesVisibility();

    const contentFeed = document.getElementById('articles-feed-section');
    if (contentFeed) {
      const headerOffset = 80;
      const elementPosition = contentFeed.getBoundingClientRect().top + window.pageYOffset;
      const offsetPosition = elementPosition - headerOffset;
      window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
    }
  };

  // Reset all filters
  window.resetFilters = function() {
    currentFilter.type = 'all';
    currentFilter.value = '';
    currentPage = 1;
    if (searchInput) searchInput.value = '';

    sidebarTags.forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.nav-link').forEach(link => {
      if (link.getAttribute('href') === 'index.html' || link.getAttribute('href') === '/') {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });

    updateArticlesVisibility();
  };

  // Bind Sidebar tags click
  sidebarTags.forEach(tag => {
    tag.addEventListener('click', (e) => {
      const isIndex = window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || !window.location.pathname.includes('.html');
      const tagVal = tag.dataset.tag;
      if (!isIndex) {
        window.location.href = `../index.html?tag=${encodeURIComponent(tagVal)}`;
      } else {
        e.preventDefault();
        setBlogFilter('tag', tagVal);
      }
    });
  });

  // Bind Search input keyup
  if (searchInput) {
    searchInput.addEventListener('input', () => {
      currentPage = 1;
      updateArticlesVisibility();
    });
  }

  // Handle URL parameters on load
  const urlParams = new URLSearchParams(window.location.search);
  const filterParam = urlParams.get('filter');
  const tagParam    = urlParams.get('tag');

  if (articleCards.length > 0) {
    if (filterParam) {
      setBlogFilter('category', filterParam);
    } else if (tagParam) {
      setBlogFilter('tag', tagParam);
    } else {
      updateArticlesVisibility();
    }
  }

  // Clean-up active class on navbar links for static pages (About Us, etc)
  const path = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href');
    if (href && path.includes(href) && href !== 'index.html') {
      link.classList.add('active');
    }
  });

  // ==========================================
  // NAVIGATION SEARCH CONTAINER EXPAND & LOGIC
  // ==========================================
  const navSearchContainer = document.getElementById('nav-search-container');
  const navSearchBtn = document.getElementById('nav-search-btn');
  const navSearchInput = document.getElementById('nav-search-input');

  if (navSearchBtn && navSearchContainer && navSearchInput) {
    navSearchBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isActive = navSearchContainer.classList.contains('active');
      if (!isActive) {
        navSearchContainer.classList.add('active');
        navSearchInput.focus();
      } else {
        const query = navSearchInput.value.trim();
        if (query) {
          performNavSearch(query);
        } else {
          navSearchContainer.classList.remove('active');
        }
      }
    });

    navSearchInput.addEventListener('click', (e) => {
      e.stopPropagation();
    });

    // Close search dropdown when clicking outside
    document.addEventListener('click', (e) => {
      if (!navSearchContainer.contains(e.target) && navSearchContainer.classList.contains('active')) {
        const query = navSearchInput.value.trim();
        if (!query) {
          navSearchContainer.classList.remove('active');
        }
      }
    });

    // Handle enter key on navbar search input
    navSearchInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        performNavSearch(navSearchInput.value.trim());
      }
    });
  }

  // Handle Global Search Parameter on Load
  const searchParam = urlParams.get('search');
  if (searchParam) {
    const mainSearchInput = document.getElementById('search-input');
    if (mainSearchInput) {
      mainSearchInput.value = searchParam;
      // Trigger search filter
      const event = new Event('input', { bubbles: true });
      mainSearchInput.dispatchEvent(event);
      // Also sync navbar search input
      if (navSearchInput) navSearchInput.value = searchParam;
    }
  }
});

// ==========================================
// GLOBAL NAVIGATION ACTIONS (SEARCH & FRIENDS MODAL)
// ==========================================
window.performNavSearch = function(term) {
  if (!term) return;
  const mainSearchInput = document.getElementById('search-input');
  if (mainSearchInput) {
    // Already on homepage
    mainSearchInput.value = term;
    const event = new Event('input', { bubbles: true });
    mainSearchInput.dispatchEvent(event);
    
    // Sync navbar search input
    const navSearchInput = document.getElementById('nav-search-input');
    if (navSearchInput) navSearchInput.value = term;
    
    // Close dropdown
    const searchDropdown = document.getElementById('search-dropdown-menu');
    if (searchDropdown) searchDropdown.classList.remove('show');
    
    // Scroll to articles feed section
    const articlesSection = document.getElementById('articles-feed-section');
    if (articlesSection) {
      articlesSection.scrollIntoView({ behavior: 'smooth' });
    }
  } else {
    // On subpage, redirect to index with query
    const isSubpage = window.location.pathname.includes('/articles/');
    const redirectUrl = isSubpage ? '../index.html' : 'index.html';
    window.location.href = `${redirectUrl}?search=${encodeURIComponent(term)}`;
  }
}

window.showFriendsModal = function() {
  let modal = document.getElementById('friends-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'friends-modal';
    modal.className = 'friends-modal-overlay';
    modal.innerHTML = `
      <div class="friends-modal-content">
        <h3 class="friends-modal-title">友情链接</h3>
        <p class="friends-modal-desc">欢迎各大网络技术、科学上网、极客分享博客交换友链。申请请发送邮件至：1962952406@qq.com</p>
        <div class="friends-links-grid">
          <a href="https://ugewe.jilianat.homes/#/?code=9ygBtCN8" target="_blank" class="friend-link-item">极连云官网</a>
          <a href="https://hjbesu8d.fazuttt.club/#/?code=AixFrykO" target="_blank" class="friend-link-item">光年梯官网</a>
          <a href="https://asfeoasf.bianyuntztz2.cyou/#/?code=Y65i2kCU" target="_blank" class="friend-link-item">边缘节点</a>
          <a href="https://iu9asffa.kuailitztz2.sbs/#/?code=tmUe2z1n" target="_blank" class="friend-link-item">快狸官网</a>
          <a href="https://asfweroasf.sujietztz2.xyz/#/?code=C2v7kRVl" target="_blank" class="friend-link-item">速界官网</a>
          <a href="https://aaa.jichang.best/#/register?code=ClNa0zPm" target="_blank" class="friend-link-item">瞬云官网</a>
        </div>
        <button class="friends-modal-close" onclick="closeFriendsModal()">关闭</button>
      </div>
    `;
    document.body.appendChild(modal);
    
    // Allow closing on clicking overlay backdrop
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeFriendsModal();
      }
    });
  }
  // Force reflow
  modal.offsetHeight;
  modal.classList.add('active');
}

window.closeFriendsModal = function() {
  const modal = document.getElementById('friends-modal');
  if (modal) {
    modal.classList.remove('active');
  }
}

window.showLatestNewsModal = function() {
  let modal = document.getElementById('latest-news-modal');
  if (modal) {
    modal.remove(); // 每次删除旧的重新构建以应用最新主题色
  }
  
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  const modalBg = isDark ? '#1e293b' : '#ffffff';
  const itemBg = isDark ? '#0f172a' : '#f8fafc';
  const borderCol = isDark ? '#334155' : '#e2e8f0';
  const textCol = isDark ? '#f8fafc' : '#1e293b';
  const textMuted = isDark ? '#94a3b8' : '#64748b';

  modal = document.createElement('div');
  modal.id = 'latest-news-modal';
  modal.className = 'friends-modal-overlay';
  modal.innerHTML = `
    <div class="friends-modal-content" style="max-width: 520px; text-align: left; position: relative; background-color: ${modalBg} !important; backdrop-filter: none !important; -webkit-backdrop-filter: none !important; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04) !important;">
      <h3 class="friends-modal-title" style="text-align: center; font-size: 1.4rem; font-weight: 800; margin-top: 4px; margin-bottom: 8px; color: ${textCol} !important;">🔥 最新资讯与科普</h3>
      <p class="friends-modal-desc" style="text-align: center; margin-bottom: 20px; color: ${textMuted} !important;">实时发布本站最新深度评测、IPLC/IEPL专线科普与科学上网场景指南。</p>
      
      <div style="display: flex; flex-direction: column; gap: 14px; margin-bottom: 24px; max-height: 380px; overflow-y: auto; padding-right: 4px;">
        
        <a href="articles/airport-guide-2026.html" style="display: block; text-decoration: none; padding: 14px; background: ${itemBg} !important; border: 1px solid ${borderCol} !important; border-radius: var(--radius-md); transition: all 0.2s;" onmouseover="this.style.borderColor='var(--accent-primary)';" onmouseout="this.style.borderColor='${borderCol}';">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 0.75rem; font-weight: 700; background: var(--accent-gradient); color: #fff; padding: 2px 8px; border-radius: 4px;">排行榜</span>
            <span style="font-size: 0.75rem; color: ${textMuted};">2026-07-22</span>
          </div>
          <h4 style="font-size: 0.95rem; font-weight: 700; color: ${textCol}; margin: 6px 0 4px;">2026年机场排行榜：高性价比翻墙机场科普与横向评测</h4>
          <p style="font-size: 0.8rem; color: ${textMuted}; line-height: 1.4; margin: 0;">什么是机场？便宜/月付/按量付费机场全面对比，8大主流机场横向评分与选购建议。</p>
        </a>

        <a href="articles/iplc-guide.html" style="display: block; text-decoration: none; padding: 14px; background: ${itemBg} !important; border: 1px solid ${borderCol} !important; border-radius: var(--radius-md); transition: all 0.2s;" onmouseover="this.style.borderColor='var(--accent-primary)';" onmouseout="this.style.borderColor='${borderCol}';">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 0.75rem; font-weight: 700; background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 100%); color: #fff; padding: 2px 8px; border-radius: 4px;">技术科普</span>
            <span style="font-size: 0.75rem; color: ${textMuted};">2026-07-22</span>
          </div>
          <h4 style="font-size: 0.95rem; font-weight: 700; color: ${textCol}; margin: 6px 0 4px;">IPLC/IEPL专线科普：游戏加速与4K不卡顿完全指南</h4>
          <p style="font-size: 0.8rem; color: ${textMuted}; line-height: 1.4; margin: 0;">深度解析 IPLC、IEPL、BGP 三种线路的区别，晚高峰延迟数据实测与游戏联机加速推荐。</p>
        </a>

        <a href="articles/streaming-ai-guide.html" style="display: block; text-decoration: none; padding: 14px; background: ${itemBg} !important; border: 1px solid ${borderCol} !important; border-radius: var(--radius-md); transition: all 0.2s;" onmouseover="this.style.borderColor='var(--accent-primary)';" onmouseout="this.style.borderColor='${borderCol}';">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 0.75rem; font-weight: 700; background: linear-gradient(135deg, #7c3aed 0%, #6366f1 100%); color: #fff; padding: 2px 8px; border-radius: 4px;">选购攻略</span>
            <span style="font-size: 0.75rem; color: ${textMuted};">2026-07-22</span>
          </div>
          <h4 style="font-size: 0.95rem; font-weight: 700; color: ${textCol}; margin: 6px 0 4px;">Netflix/ChatGPT/TikTok机场选择指南：流媒体与AI工具加速攻略</h4>
          <p style="font-size: 0.8rem; color: ${textMuted}; line-height: 1.4; margin: 0;">不同使用场景下的最优机场推荐，含详细兼容性对比表，教你如何规避AI地区检测。</p>
        </a>

        <a href="articles/cheap-airports.html" style="display: block; text-decoration: none; padding: 14px; background: ${itemBg} !important; border: 1px solid ${borderCol} !important; border-radius: var(--radius-md); transition: all 0.2s;" onmouseover="this.style.borderColor='var(--accent-primary)';" onmouseout="this.style.borderColor='${borderCol}';">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 0.75rem; font-weight: 700; background: #8b5cf6; color: #fff; padding: 2px 8px; border-radius: 4px;">便宜机场</span>
            <span style="font-size: 0.75rem; color: ${textMuted};">2026-07-05</span>
          </div>
          <h4 style="font-size: 0.95rem; font-weight: 700; color: ${textCol}; margin: 6px 0 4px;">便宜机场推荐：10元左右高性价比机场首选</h4>
          <p style="font-size: 0.8rem; color: ${textMuted}; line-height: 1.4; margin: 0;">预算有限又想看高清视频？盘点低价专线中性价比最具杀伤力的平价梯子选择。</p>
        </a>

      </div>
      <button class="friends-modal-close" style="width: 100%; border: 1px solid ${borderCol} !important; background-color: ${itemBg} !important; color: ${textCol} !important;" onclick="closeLatestNewsModal()">关闭</button>
    </div>
  `;
  document.body.appendChild(modal);
  
  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeLatestNewsModal();
    }
  });
  
  modal.offsetHeight;
  modal.classList.add('active');
}

window.closeLatestNewsModal = function() {
  const modal = document.getElementById('latest-news-modal');
  if (modal) {
    modal.classList.remove('active');
  }
}

