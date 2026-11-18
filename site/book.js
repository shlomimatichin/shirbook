(() => {
  const book = document.getElementById('book');
  const cover = document.getElementById('cover');
  const chapters = document.getElementById('chapters');
  const previous = document.getElementById('previous');
  const next = document.getElementById('next');
  const indicator = document.getElementById('page-indicator');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  let current = location.hash === '#chapters' ? chapters : cover;
  let busy = false;
  let cancelTurn = () => {};

  function settle(target, focus) {
    cancelTurn();
    cancelTurn = () => {};
    for (const page of [cover, chapters]) {
      const active = page === target;
      page.className = `page ${page === cover ? 'cover' : 'contents'}${active ? ' is-active' : ''}`;
      page.inert = !active;
      page.setAttribute('aria-hidden', String(!active));
    }
    current = target;
    previous.hidden = target === cover;
    next.hidden = target === chapters;
    indicator.textContent = target === cover ? 'The cover' : 'Chapters · 1';
    book.classList.remove('busy');
    busy = false;
    if (focus) target.querySelector('h1, h2').focus({ preventScroll: true });
  }

  function turn(target, updateUrl = true) {
    if (busy || target === current) return;
    if (updateUrl) history.pushState(null, '', target === cover ? '#cover' : '#chapters');
    if (reducedMotion.matches) { settle(target, true); return; }
    busy = true;
    book.classList.add('busy');
    // The destination is visible below the turning leaf but stays out of the
    // accessibility tree until the transition finishes.
    target.classList.add('is-under');
    const animated = target === chapters ? current : target;
    animated.classList.add('is-turning', target === chapters ? 'turn-forward' : 'turn-back');
    let finished = false;
    function finish() {
      if (finished) return;
      finished = true;
      clearTimeout(fallback);
      animated.removeEventListener('animationend', finish);
      settle(target, true);
    }
    animated.addEventListener('animationend', finish);
    const fallback = setTimeout(finish, 750);
    cancelTurn = () => {
      finished = true;
      clearTimeout(fallback);
      animated.removeEventListener('animationend', finish);
    };
  }

  next.addEventListener('click', event => { event.preventDefault(); turn(chapters); });
  previous.addEventListener('click', event => { event.preventDefault(); turn(cover); });
  document.addEventListener('keydown', event => {
    if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
    if (event.key === 'ArrowRight' && current === cover) { event.preventDefault(); turn(chapters); }
    if (event.key === 'ArrowLeft' && current === chapters) { event.preventDefault(); turn(cover); }
  });
  addEventListener('popstate', () => { settle(location.hash === '#chapters' ? chapters : cover, true); });
  settle(current, false);
})();
