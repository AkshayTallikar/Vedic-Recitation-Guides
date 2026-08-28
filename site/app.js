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
  var practiceBtn = document.getElementById('practice');

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
  function actionRunHtml(actionRun, guide) {
    var html = '<div class="guided-block action-block">' +
      '<span class="lbl">' + esc(guide.structuredActionLabel || 'Action · English') + '</span>';
    actionRun.forEach(function (action) {
      html += '<div class="action-english">' + esc(action.english || '') + '</div>';
    });
    var spokenActions = actionRun.filter(function (action) {
      return !!action.sourceRoman;
    });
    if (spokenActions.length) {
      html += '<details class="spoken-source"><summary>' +
        esc(guide.structuredSourceLabel || 'Original spoken source') +
        '</summary>';
      spokenActions.forEach(function (action) {
        html += '<div>' + esc(action.sourceRoman) + '</div>';
      });
      html += '</details>';
    }
    return html + '</div>';
  }
  function recitationBlockHtml(text, guide) {
    return '<div class="guided-block recitation-block">' +
      '<span class="lbl">' + esc(guide.structuredMantraLabel || 'Sanskrit recitation') + '</span>' +
      '<div>' + esc(text || '') + '</div>' +
      '</div>';
  }
  function usesActionsAtBottom(guide) {
    return guide.key === 'deva-pooja-four-part-complete';
  }
  function structuredTranscriptHtml(blocks, guide, mode) {
    if (!blocks || !blocks.length) return '';
    if (usesActionsAtBottom(guide)) {
      var recitations = [];
      var actions = [];
      blocks.forEach(function (block) {
        if (block.kind === 'action') actions.push(block);
        else if (block.text) recitations.push(block.text);
      });
      var bottomHtml = '';
      if (mode === 'actions') {
        if (actions.length) bottomHtml = actionRunHtml(actions, guide);
      } else if (recitations.length) {
        bottomHtml = recitationBlockHtml(recitations.join('\n\n'), guide);
      }
      return bottomHtml ? '<div class="guided-flow">' + bottomHtml + '</div>' : '';
    }
    var html = '<div class="guided-flow">';
    var i = 0;
    while (i < blocks.length) {
      var block = blocks[i];
      if (block.kind === 'action') {
        var actionRun = [];
        while (i < blocks.length && blocks[i].kind === 'action') {
          actionRun.push(blocks[i]);
          i++;
        }
        html += actionRunHtml(actionRun, guide);
      } else {
        html += recitationBlockHtml(block.text, guide);
        i++;
      }
    }
    return html + '</div>';
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
  var practiceEnabled = false;
  var repetition = 1;
  var seeking = false;

  function practiceActive() {
    return guide && guide.practiceMode === 'repeat3' && practiceEnabled;
  }
  function syncPractice() {
    var available = guide && guide.practiceMode === 'repeat3';
    practiceBtn.hidden = !available;
    if (available) practiceBtn.textContent = guide.practiceLabel || '↻ 3× Practice';
    practiceBtn.classList.toggle('is-on', available && practiceEnabled);
    practiceBtn.setAttribute('aria-pressed', available && practiceEnabled ? 'true' : 'false');
    practiceBtn.title = practiceEnabled
      ? 'Practice mode on: each verse plays three times'
      : 'Play each verse three times before moving on';
  }
  function setPlayerTitle() {
    if (current < 0 || !secs[current]) return;
    var s = secs[current];
    pt.textContent = s.id + ' · ' + s.title + (practiceActive() ? ' · Repeat ' + repetition + '/3' : '');
  }

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
    repetition = 1;
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
    syncPractice();
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
          originalScript = subst(rs.originalScript),
          captionOriginal = subst(rs.captionOriginal),
          structuredBlocks = rs.structuredBlocks || [],
          displayAction = (usesActionsAtBottom(guide) && structuredBlocks.length) ? '' : action,
          title = subst(rs.title);
      var structuredSearch = structuredBlocks.map(function (block) {
        return (block.text || '') + ' ' + (block.english || '') + ' ' +
          (block.sourceRoman || '') + ' ' + (block.sourceOriginal || '');
      }).join(' ');
      var hasAudio = s.audio ? true : !guide.noAudio;
      var sectionSource = s.sourceVideo || guide.source;
      var sectionStart = typeof s.startSeconds === 'number'
        ? s.startSeconds
        : (s.start ? toSec(s.start) : 0);
      var ytLink = (hasAudio && sectionSource)
        ? sectionSource + (sectionSource.indexOf('?') > -1 ? '&' : '?') +
          't=' + Math.round(sectionStart) + 's'
        : '';
      var timeHtml = s.start ? ('<div class="time">⏱ ' + s.start + '–' + s.end + '</div>')
        : (s.page ? ('<div class="time">📖 p. ' + esc(s.page) + '</div>') : '');
      var card = document.createElement('article');
      card.className = 'card';
      card.id = 'sec-' + s.id;
      card.dataset.search = (title + ' ' + (skt || '') + ' ' + mantra + ' ' +
        originalScript + ' ' + devanagari + ' ' + captionOriginal + ' ' +
        structuredSearch + ' ' + meaning + ' ' +
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
        structuredTranscriptHtml(structuredBlocks, guide) +
        (mantra
          ? (structuredBlocks.length
              ? (guide.hideLosslessReferences ? '' :
                  '<details class="caption-ref lossless-roman"><summary>' +
                    esc(guide.mantraLabel || 'Complete untouched Roman transcript') +
                  '</summary><div class="mantra">' + esc(mantra) + '</div></details>')
              : '<div class="mantra">' +
                  (guide.mantraLabel ? '<span class="lbl">' + esc(guide.mantraLabel) + '</span>' : '') +
                  esc(mantra) + '</div>')
          : '') +
        (originalScript && !guide.hideLosslessReferences
          ? '<details class="caption-ref script-ref"><summary>' +
              esc(guide.originalScriptLabel || 'Exact original transcription') +
            '</summary><div class="devanagari">' + esc(originalScript) + '</div></details>'
          : '') +
        (devanagari
          ? (guide.collapseDevanagari
              ? '<details class="caption-ref"><summary>' +
                  esc(guide.devanagariLabel || 'Secondary transcription') +
                '</summary><div class="devanagari">' + esc(devanagari) + '</div></details>'
              : '<div class="devanagari"><span class="lbl">' +
                  esc(guide.devanagariLabel || 'Sanskrit') +
                '</span>' + esc(devanagari) + '</div>')
          : '') +
        (captionOriginal
          ? '<details class="caption-ref"><summary>' +
              esc(guide.captionOriginalLabel || 'Exact original captions') +
            '</summary><div class="devanagari">' + esc(captionOriginal) + '</div></details>'
          : '') +
        ((meaning || contemplate || displayAction)
          ? '<div class="explain' + ((contemplate || displayAction) ? ' has-rahasya' : '') + '">' +
              (meaning ? '<div class="meaning"><span class="lbl">Meaning</span>' + esc(meaning) + '</div>' : '') +
              ((contemplate || displayAction)
                ? '<div class="rahasya">' +
                    (contemplate ? '<div class="blk"><span class="lbl lbl-c">Contemplate</span>' + esc(contemplate) + '</div>' : '') +
                    (displayAction ? '<div class="blk"><span class="lbl lbl-a">Action</span>' + esc(displayAction) + '</div>' : '') +
                  '</div>'
                : '') +
            '</div>'
          : '') +
        (usesActionsAtBottom(guide) ? structuredTranscriptHtml(structuredBlocks, guide, 'actions') : '') +
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
    repetition = 1;
    var c = cards[idx];
    audio.src = c.__audio;
    audio.playbackRate = rate;
    setPlayerTitle();
    player.classList.add('show');
    cards.forEach(function (x) { x.classList.remove('playing'); });
    c.classList.add('playing');
    syncBtns();
    if (autoplay !== false) audio.play();
  }
  function toggle() {
    if (audio.paused) {
      if (audio.ended) {
        repetition = 1;
        audio.currentTime = 0;
        setPlayerTitle();
      }
      audio.play();
    } else audio.pause();
  }
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
  practiceBtn.addEventListener('click', function () {
    practiceEnabled = !practiceEnabled;
    repetition = 1;
    syncPractice();
    setPlayerTitle();
  });

  audio.addEventListener('play', syncBtns);
  audio.addEventListener('pause', syncBtns);
  audio.addEventListener('ended', function () {
    if (practiceActive() && repetition < 3) {
      repetition++;
      audio.currentTime = 0;
      setPlayerTitle();
      audio.play();
    } else if (current + 1 < cards.length) {
      load(current + 1);
    } else {
      syncBtns();
    }
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
