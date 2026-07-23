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
  // CONTENT FILTERING (CATEGORIES & TAGS)
  // ==========================================
  const articleCards = document.querySelectorAll('.article-card');
  const sidebarTags = document.querySelectorAll('.sidebar-tag');
  const filterIndicator = document.getElementById('active-filter-indicator');
  const filterLabel = document.getElementById('filter-label');
  const searchInput = document.getElementById('search-input');

  // Categories mapping (mapping URL query / filter name to HTML classes/attributes)
  // Categories: cheap (便宜机场), premium (优质机场), established (老牌机场), curated (精选汇总)
  let currentFilter = {
    type: 'all', // 'all', 'category', 'tag', 'search'
    value: ''
  };

  let isFeedExpanded = false;

  function updateArticlesVisibility() {
    let visibleCount = 0;
    let totalMatches = 0;
    const searchVal = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const isHomepage = !!document.querySelector('.hero-section');

    articleCards.forEach(card => {
      const cardCategories = card.dataset.categories ? card.dataset.categories.split(',') : [];
      const cardTags = card.dataset.tags ? card.dataset.tags.split(',') : [];
      const cardTitle = card.querySelector('.card-title').textContent.toLowerCase();
      const cardExcerpt = card.querySelector('.card-excerpt').textContent.toLowerCase();

      let matchesFilter = true;

      // 1. Check Category/Tag filter
      if (currentFilter.type === 'category') {
        matchesFilter = cardCategories.includes(currentFilter.value);
      } else if (currentFilter.type === 'tag') {
        matchesFilter = cardTags.includes(currentFilter.value);
      }

      // 2. Check Search text
      let matchesSearch = true;
      if (searchVal) {
        matchesSearch = cardTitle.includes(searchVal) || 
                        cardExcerpt.includes(searchVal) || 
                        cardTags.some(t => t.toLowerCase().includes(searchVal));
      }

      // Final decision
      if (matchesFilter && matchesSearch) {
        totalMatches++;
        // Limit on homepage when not filtering and not expanded
        if (isHomepage && currentFilter.type === 'all' && !searchVal && !isFeedExpanded) {
          if (totalMatches <= 5) {
            card.style.display = 'grid';
            visibleCount++;
          } else {
            card.style.display = 'none';
          }
        } else {
          card.style.display = 'grid';
          visibleCount++;
        }
      } else {
        card.style.display = 'none';
      }
    });

    // Update Expand Button UI
    const expandContainer = document.getElementById('expand-btn-container');
    if (isHomepage && currentFilter.type === 'all' && !searchVal) {
      if (expandContainer) {
        expandContainer.style.display = 'flex';
        const expandBtn = document.getElementById('expand-articles-btn');
        if (expandBtn) {
          if (isFeedExpanded) {
            expandBtn.innerHTML = `收起文章列表 <svg class="expand-chevron" style="transform: rotate(180deg);" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z" fill="currentColor"/></svg>`;
          } else {
            const hiddenCount = Math.max(0, totalMatches - 5);
            expandBtn.innerHTML = `展开全部 ${totalMatches} 篇文章 <svg class="expand-chevron" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z" fill="currentColor"/></svg>`;
          }
        }
      }
    } else {
      if (expandContainer) {
        expandContainer.style.display = 'none';
      }
    }

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

    // Handle empty state if no articles match
    let emptyState = document.getElementById('empty-feed-state');
    if (visibleCount === 0 && articleCards.length > 0) {
      if (!emptyState) {
        emptyState = document.createElement('div');
        emptyState.id = 'empty-feed-state';
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
    
    // Update tag active classes in sidebar
    sidebarTags.forEach(tag => {
      if (type === 'tag' && tag.dataset.tag === value) {
        tag.classList.add('active');
      } else {
        tag.classList.remove('active');
      }
    });

    // Update active class on main navbar
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

    // Scroll to the main articles section if it's far below (e.g. mobile or landing header page)
    const contentFeed = document.getElementById('articles-feed-section');
    if (contentFeed) {
      const headerOffset = 80;
      const elementPosition = contentFeed.getBoundingClientRect().top + window.pageYOffset;
      const offsetPosition = elementPosition - headerOffset;
      
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  };

  // Reset all filters
  window.resetFilters = function() {
    currentFilter.type = 'all';
    currentFilter.value = '';
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
      // If we are not on the index page, redirect to index with tag query
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
      updateArticlesVisibility();
    });
  }

  // Handle URL parameters on load
  const urlParams = new URLSearchParams(window.location.search);
  const filterParam = urlParams.get('filter');
  const tagParam = urlParams.get('tag');

  // Only apply URL parameters or default visibility if we are on index
  if (articleCards.length > 0) {
    const isHomepage = !!document.querySelector('.hero-section');
    const contentFeed = document.querySelector('.content-feed');
    if (isHomepage && contentFeed) {
      const expandBtnContainer = document.createElement('div');
      expandBtnContainer.id = 'expand-btn-container';
      expandBtnContainer.className = 'expand-btn-container';
      expandBtnContainer.innerHTML = `
        <button class="expand-articles-btn" id="expand-articles-btn">
          展开全部文章
          <svg class="expand-chevron" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z" fill="currentColor"/></svg>
        </button>
      `;
      contentFeed.appendChild(expandBtnContainer);
      
      const expandArticlesBtn = document.getElementById('expand-articles-btn');
      if (expandArticlesBtn) {
        expandArticlesBtn.addEventListener('click', () => {
          isFeedExpanded = !isFeedExpanded;
          updateArticlesVisibility();
          
          // If collapsing, scroll smoothly back to the top of feed section
          if (!isFeedExpanded) {
            const feedSection = document.getElementById('articles-feed-section');
            if (feedSection) {
              const headerOffset = 80;
              const elementPosition = feedSection.getBoundingClientRect().top + window.pageYOffset;
              const offsetPosition = elementPosition - headerOffset;
              window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
              });
            }
          }
        });
      }
    }

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
  // NAVIGATION SEARCH DROPDOWN TOGGLE & LOGIC
  // ==========================================
  const navSearchBtn = document.getElementById('nav-search-btn');
  const searchDropdownMenu = document.getElementById('search-dropdown-menu');
  const navSearchInput = document.getElementById('nav-search-input');

  if (navSearchBtn && searchDropdownMenu) {
    navSearchBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      searchDropdownMenu.classList.toggle('show');
      if (searchDropdownMenu.classList.contains('show') && navSearchInput) {
        navSearchInput.focus();
      }
    });

    // Close search dropdown when clicking outside
    document.addEventListener('click', (e) => {
      if (!searchDropdownMenu.contains(e.target) && e.target !== navSearchBtn && !navSearchBtn.contains(e.target)) {
        searchDropdownMenu.classList.remove('show');
      }
    });

    // Handle enter key on navbar search input
    if (navSearchInput) {
      navSearchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
          performNavSearch(navSearchInput.value.trim());
        }
      });
    }
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
