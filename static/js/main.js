/* ============================================================
   NADI-VERSE™ | main.js
   Scroll reveal + nav scroll + hero counters + hamburger menu
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Navbar scroll effect ── */
  const nav = document.querySelector('nav');
  const onScroll = () => {
    if (window.scrollY > 40) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ── Hamburger menu ── */
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('nav-links');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      navLinks.classList.toggle('open');
      const isOpen = navLinks.classList.contains('open');
      hamburger.setAttribute('aria-expanded', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close on link click
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        document.body.style.overflow = '';
      });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!hamburger.contains(e.target) && !navLinks.contains(e.target)) {
        navLinks.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  }

  /* ── IntersectionObserver scroll-reveal ── */
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        // Don't unobserve — keeps elements visible
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  });

  document.querySelectorAll('.reveal').forEach(el => {
    revealObserver.observe(el);
  });

  /* ── Dosha bar animation (results page) ── */
  const doshaObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll('.dosha-fill').forEach(fill => {
          const target = fill.dataset.target || '0';
          fill.style.width = target + '%';
        });
        doshaObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  const doshaSection = document.querySelector('.dosha-bar-group');
  if (doshaSection) doshaObserver.observe(doshaSection);

  /* ── Counter animation (hero stats) ── */
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll('[data-count]').forEach(el => {
          animateCounter(el);
        });
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  const heroStats = document.querySelector('.hero-stats');
  if (heroStats) counterObserver.observe(heroStats);

  function animateCounter(el) {
    const target = parseInt(el.dataset.count, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 1800;
    const start = performance.now();

    function update(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      // Ease out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target) + suffix;
      if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  }

  /* ── Smooth active nav link on scroll ── */
  const sections = document.querySelectorAll('section[id]');
  const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');

  const activeSectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navAnchors.forEach(a => a.classList.remove('active-nav'));
        const target = document.querySelector(`.nav-links a[href="#${entry.target.id}"]`);
        if (target) target.classList.add('active-nav');
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => activeSectionObserver.observe(s));

  /* ── Tech arch node stagger animation ── */
  const archNodes = document.querySelectorAll('.arch-node');
  const archObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        archNodes.forEach((node, i) => {
          setTimeout(() => {
            node.style.opacity = '1';
            node.style.transform = 'translateY(0)';
          }, i * 120);
        });
        archObserver.disconnect();
      }
    });
  }, { threshold: 0.2 });

  if (archNodes.length) {
    archNodes.forEach(node => {
      node.style.opacity = '0';
      node.style.transform = 'translateY(20px)';
      node.style.transition = 'opacity 0.5s ease, transform 0.5s ease, background 0.35s ease, box-shadow 0.35s ease';
    });
    archObserver.observe(archNodes[0].closest('#tech-arch') || archNodes[0]);
  }

  /* ── Roadmap stagger ── */
  const roadmapItems = document.querySelectorAll('.roadmap-item');
  const roadmapObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        roadmapItems.forEach((item, i) => {
          setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'translateX(0)';
          }, i * 150);
        });
        roadmapObserver.disconnect();
      }
    });
  }, { threshold: 0.1 });

  if (roadmapItems.length) {
    roadmapItems.forEach(item => {
      item.style.opacity = '0';
      item.style.transform = 'translateX(-20px)';
      item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });
    const roadmapSection = document.querySelector('#roadmap');
    if (roadmapSection) roadmapObserver.observe(roadmapSection);
  }

});
