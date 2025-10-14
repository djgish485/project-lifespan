// Placeholder for potential future charting; current score card is static HTML.
// We avoid adding Chart.js now to keep the stack light.
// If needed, we can enhance to render a radar chart from data attributes.

// Lightweight popover for inline reference anchors with class `ref-pop`.
// Usage in Markdown/HTML:
//   <sup><a class="ref-pop" href="https://doi.org/..." data-ref-url="https://doi.org/...">1</a></sup>
// Shows a small popover near the anchor with a clickable link.

(function() {
  function attachRefPopovers() {
    // Clean up any existing popovers to avoid duplicates on rerender
    document.querySelectorAll('.ref-popover').forEach(function(n){ n.remove(); });
    document.querySelectorAll('a.ref-pop').forEach(function(a){
      let pop = null;
      let hideTimer = null;
      const url = a.getAttribute('data-ref-url') || a.getAttribute('href');
      const summary = a.getAttribute('data-ref-summary') || '';
      function position(popEl){
        const r = a.getBoundingClientRect();
        const x = (window.scrollX || window.pageXOffset) + r.left;
        const y = (window.scrollY || window.pageYOffset) + r.bottom + 6;
        popEl.style.left = x + 'px';
        popEl.style.top = y + 'px';
      }
      const show = function() {
        if (!url) return;
        if (hideTimer) { clearTimeout(hideTimer); hideTimer = null; }
        if (pop) return;
        pop = document.createElement('div');
        pop.className = 'ref-popover';
        if (summary) {
          const p = document.createElement('div');
          p.className = 'ref-popover__summary';
          p.textContent = summary;
          pop.appendChild(p);
        }
        const link = document.createElement('a');
        link.href = url;
        link.target = '_blank';
        link.rel = 'noopener';
        link.textContent = url;
        pop.appendChild(link);
        document.body.appendChild(pop);
        position(pop);
        // Keep visible when hovering popover
        pop.addEventListener('mouseenter', function(){ if (hideTimer) { clearTimeout(hideTimer); hideTimer = null; } });
        pop.addEventListener('mouseleave', function(){ scheduleHide(); });
        window.addEventListener('scroll', function(){ if (pop) position(pop); }, { passive: true });
        window.addEventListener('resize', function(){ if (pop) position(pop); });
      };
      function destroy(){ if (pop && pop.parentNode) pop.parentNode.removeChild(pop); pop = null; }
      function scheduleHide(){ if (hideTimer) return; hideTimer = setTimeout(function(){ destroy(); hideTimer = null; }, 150); }
      a.addEventListener('mouseenter', show);
      a.addEventListener('mouseleave', scheduleHide);
      a.addEventListener('focus', show);
      a.addEventListener('blur', scheduleHide);
    });
  }

  // Support MkDocs Material SPA navigation
  if (typeof document$ !== 'undefined' && document$.subscribe) {
    document$.subscribe(function() { attachRefPopovers(); });
  } else {
    document.addEventListener('DOMContentLoaded', attachRefPopovers);
  }
})();
