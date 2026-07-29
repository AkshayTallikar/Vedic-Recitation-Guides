(function () {
  var GUIDES = window.GUIDES || [];
  if (!GUIDES.length) return;

  // ---- shared DOM ----
  var tabsEl = document.getElementById('tabs');
  var periodbar = document.getElementById('periodbar');
  var list = document.getElementById('list');
  var search = document.getElementById('search');
  var countEl = document.getElementById('count');
  var noticeEl = document.getElementById('guide-notice');
  var titleEl = document.getElementById('h-title');
  var srcA = document.getElementById('h-src');
  var subEl = document.getElementById('h-sub');
  var creditEl = document.getElementById('h-credit');

  var audio = document.getElementById('audio');
  var player = document.getElementById('player');
  var pp = document.getElementById('pp');
  var pt = document.getElementById('pt');
  var seek = document.getElementById('seek');
  var tt = document.getElementById('tt');
  var speedsEl = document.getElementById('speeds');

  // ---- helpers ----
  function toSec(mmss) { var p = mmss.split(':'); return (+p[0]) * 60 + (+p[1]); }
  function fmt(s) {
    if (isNaN(s)) s = 0;
    var m = Math.floor(s / 60), x = Math.floor(s % 60);
    return m + ':' + (x < 10 ? '0' : '') + x;
  }
  function esc(t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

  // Replace the {p}/{pe} time-of-day tokens with the selected period's words.
  function subst(t) {
    if (!t) return t || '';
    if (!curP) return t;
    return t.replace(/\{p\}/g, curP.word).replace(/\{pe\}/g, curP.en);
  }
  // Overlay the current period's overrides onto a section, then run token subst.
  function resolve(s) {
    var r = s, k;
    if (s.periods && curP && s.periods[curP.key]) {
      r = {};
      for (k in s) r[k] = s[k];
      var pv = s.periods[curP.key];
      for (k in pv) r[k] = pv[k];
    }
    return r;
  }

  // ---- period bar (time-of-day selector) ----
  function buildPeriodBar() {
    if (!guide.periods) { periodbar.hidden = true; periodbar.innerHTML = ''; return; }
    periodbar.hidden = false;
    var h = '<span class="plabel">' + esc(guide.periodLabel || 'Time of day') + '</span><span class="pseg">';
    guide.periods.forEach(function (p, i) {
      h += '<button data-pi="' + i + '"' + (p === curP ? ' class="active"' : '') + '>' + esc(p.label) + '</button>';
    });
    periodbar.innerHTML = h + '</span>';
  }
  periodbar.addEventListener('click', function (e) {
    var b = e.target.closest('button[data-pi]');
    if (!b || !guide.periods) return;
    curP = guide.periods[+b.dataset.pi];
    buildPeriodBar();
    buildList();
  });

  // ---- per-guide state ----
  var guide, secs, cards, current = -1;
  var curP = null; // current time-of-day period (for guides with s.periods)
  var rate = 1;
  var seeking = false;

  // ---- tabs ----
  GUIDES.forEach(function (g, gi) {
    var b = document.createElement('button');
    b.className = 'tab';
    b.innerHTML = '<span class="tname">' + esc(g.title) + '</span>' +
                  '<span class="tlabel">' + esc(g.tabLabel || '') + '</span>';
    b.addEventListener('click', function () { selectGuide(gi); });
    tabsEl.appendChild(b);
  });

  function selectGuide(gi) {
    // stop playback on switch
    audio.pause();
    audio.removeAttribute('src');
    current = -1;
    player.classList.remove('show');

    guide = GUIDES[gi];
    secs = guide.sections;
    curP = guide.periods ? guide.periods[0] : null;
    Array.prototype.forEach.call(tabsEl.children, function (t, i) {
      t.classList.toggle('active', i === gi);
    });
    titleEl.textContent = guide.title;
    document.title = guide.title + ' — Recitation Guide';
    subEl.textContent = guide.subtitle;
    creditEl.textContent = guide.sourceCredit;
    srcA.href = guide.source;
    srcA.textContent = guide.sourceLabel || 'YouTube';
    search.value = '';
    search.placeholder = guide.searchPlaceholder || 'Search a step (e.g. Śaṅkha, abhiṣeka, naivedya)…';
    noticeEl.hidden = !!guide.hideNotice;
    buildPeriodBar();
    buildList();
  }

  function buildList() {
    list.innerHTML = '';
    cards = [];
    var lastGroup = '';
    secs.forEach(function (s, i) {
      if (s.group !== lastGroup) {
        var gh = document.createElement('div');
        gh.className = 'group-head';
        gh.textContent = s.group;
        list.appendChild(gh);
        lastGroup = s.group;
      }
      var rs = resolve(s);
      var mantra = subst(rs.mantra), meaning = subst(rs.meaning),
          action = subst(rs.action), contemplate = subst(rs.contemplate),
          skt = subst(rs.sanskrit), devanagari = subst(rs.devanagari),
          title = subst(rs.title);
      var hasAudio = s.audio ? true : !guide.noAudio;
      var ytLink = (hasAudio && s.start) ? guide.source + '&t=' + toSec(s.start) + 's' : '';
      var timeHtml = s.start ? ('<div class="time">⏱ ' + s.start + '–' + s.end + '</div>')
        : (s.page ? ('<div class="time">📖 p. ' + esc(s.page) + '</div>') : '');
      var card = document.createElement('article');
      card.className = 'card';
      card.id = 'sec-' + s.id;
      card.dataset.search = (title + ' ' + (skt || '') + ' ' + mantra + ' ' + devanagari + ' ' + meaning + ' ' +
        (contemplate || '') + ' ' + (action || '')).toLowerCase();
      card.innerHTML =
        '<div class="top">' +
          '<div class="num">' + s.id + '</div>' +
          '<div class="titles">' +
            '<h2>' + esc(title) +
              (s.periods ? ' <span class="pvary" title="This mantra changes with the selected sandhyā">changes by sandhyā</span>' : '') +
              (s.verify ? ' <span class="badge" title="Reconstructed from audio — verify">verify</span>' : '') +
            '</h2>' +
            (skt ? '<div class="skt">' + esc(skt) + '</div>' : '') +
            timeHtml +
          '</div>' +
          (hasAudio ? '<button class="playbtn" data-idx="' + i + '"><span class="ico">▶</span> Play</button>' : '') +
        '</div>' +
        (mantra ? '<div class="mantra">' +
          (guide.mantraLabel ? '<span class="lbl">' + esc(guide.mantraLabel) + '</span>' : '') +
          esc(mantra) + '</div>' : '') +
        (devanagari ? '<div class="devanagari"><span class="lbl">Sanskrit</span>' + esc(devanagari) + '</div>' : '') +
        ((meaning || contemplate || action)
          ? '<div class="explain' + ((contemplate || action) ? ' has-rahasya' : '') + '">' +
              (meaning ? '<div class="meaning"><span class="lbl">Meaning</span>' + esc(meaning) + '</div>' : '') +
              ((contemplate || action)
                ? '<div class="rahasya">' +
                    (contemplate ? '<div class="blk"><span class="lbl lbl-c">Contemplate</span>' + esc(contemplate) + '</div>' : '') +
                    (action ? '<div class="blk"><span class="lbl lbl-a">Action</span>' + esc(action) + '</div>' : '') +
                  '</div>'
                : '') +
            '</div>'
          : '') +
        (s.html || '') +
        (ytLink ? '<div class="yt"><a href="' + ytLink + '" target="_blank" rel="noopener">▶ Watch this step on YouTube ↗</a></div>' : '');
      if (hasAudio) card.__audio = s.audioFile || (guide.audioDir + '/' + s.id + '-' + s.slug + '.mp3');
      list.appendChild(card);
      cards.push(card);
    });
    countEl.textContent = cards.length + ' steps';
    applyFilter();
  }

  // ---- search ----
  function applyFilter() {
    var q = search.value.trim().toLowerCase();
    var shown = 0;
    cards.forEach(function (c) {
      var hit = !q || c.dataset.search.indexOf(q) > -1;
      c.style.display = hit ? '' : 'none';
      if (hit) shown++;
    });
    document.querySelectorAll('.group-head').forEach(function (g) {
      var n = g.nextElementSibling, any = false;
      while (n && !n.classList.contains('group-head')) {
        if (n.classList.contains('card') && n.style.display !== 'none') { any = true; break; }
        n = n.nextElementSibling;
      }
      g.style.display = any ? '' : 'none';
    });
    countEl.textContent = q ? (shown + ' of ' + cards.length + ' steps') : (cards.length + ' steps');
  }
  search.addEventListener('input', applyFilter);

  // ---- player ----
  function load(idx, autoplay) {
    if (idx < 0 || idx >= cards.length) return;
    if (current === idx) { toggle(); return; }
    current = idx;
    var c = cards[idx], s = secs[idx];
    audio.src = c.__audio;
    audio.playbackRate = rate;
    pt.textContent = s.id + ' · ' + s.title;
    player.classList.add('show');
    cards.forEach(function (x) { x.classList.remove('playing'); });
    c.classList.add('playing');
    syncBtns();
    if (autoplay !== false) audio.play();
  }
  function toggle() { if (audio.paused) audio.play(); else audio.pause(); }
  function syncBtns() {
    var playing = !audio.paused;
    pp.textContent = playing ? '❚❚' : '▶';
    document.querySelectorAll('.playbtn').forEach(function (b) {
      var idx = +b.dataset.idx;
      b.innerHTML = (idx === current && playing)
        ? '<span class="ico">❚❚</span> Pause'
        : '<span class="ico">▶</span> Play';
    });
  }

  list.addEventListener('click', function (e) {
    var b = e.target.closest('.playbtn');
    if (b) load(+b.dataset.idx);
  });
  pp.addEventListener('click', toggle);
  document.getElementById('prev').addEventListener('click', function () { load(current - 1); });
  document.getElementById('next').addEventListener('click', function () { load(current + 1); });
  speedsEl.addEventListener('click', function (e) {
    var b = e.target.closest('.spd');
    if (!b) return;
    rate = parseFloat(b.dataset.rate);
    audio.playbackRate = rate;
    Array.prototype.forEach.call(speedsEl.children, function (x) {
      x.classList.toggle('is-on', x === b);
    });
  });

  audio.addEventListener('play', syncBtns);
  audio.addEventListener('pause', syncBtns);
  audio.addEventListener('ended', function () {
    if (current + 1 < cards.length) load(current + 1); else syncBtns();
  });
  audio.addEventListener('timeupdate', function () {
    if (seeking || !audio.duration) return;
    seek.value = (audio.currentTime / audio.duration) * 100;
    tt.textContent = fmt(audio.currentTime) + ' / ' + fmt(audio.duration);
  });
  seek.addEventListener('input', function () { seeking = true; });
  seek.addEventListener('change', function () {
    if (audio.duration) audio.currentTime = (seek.value / 100) * audio.duration;
    seeking = false;
  });

  document.addEventListener('keydown', function (e) {
    if (e.target.tagName === 'INPUT') return;
    if (e.code === 'Space' && current > -1) { e.preventDefault(); toggle(); }
    else if (e.code === 'ArrowRight' && e.altKey) load(current + 1);
    else if (e.code === 'ArrowLeft' && e.altKey) load(current - 1);
  });

  // ---- init ----
  selectGuide(0);
})();
