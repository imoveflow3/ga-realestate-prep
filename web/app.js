/* Georgia Real Estate Prep -- single page app, no dependencies. */
'use strict';

var META = null, PROGRESS = null, QUIZ = null, TICK = null, LAST = null;

function $(id){ return document.getElementById(id); }
function el(tag, cls, txt){
  var n = document.createElement(tag);
  if (cls) n.className = cls;
  if (txt !== undefined && txt !== null) n.textContent = txt;
  return n;
}
function api(path, body){
  var opt = body ? {method:'POST', headers:{'Content-Type':'application/json'},
                    body: JSON.stringify(body)} : {};
  return fetch(path, opt).then(function(r){ return r.json(); });
}
function pct(x){ return x === null || x === undefined ? '--' : Math.round(x*100) + '%'; }
function tagFor(portion){
  var cls = portion === 'georgia' ? ' ga' : (portion === 'comprehensive' ? ' comp' : '');
  var txt = portion === 'georgia' ? 'GA' : (portion === 'comprehensive' ? 'COMP' : 'NAT');
  return el('span', 'tag' + cls, txt);
}
function countsOnExam(key){
  var t = (META.topics || []).filter(function(x){ return x.key === key; })[0];
  return !t || t.counts_on_exam !== false;
}
function band(p){ return p === null || p === undefined ? '' : (p < 0.6 ? 'low' : (p < 0.8 ? 'mid' : 'high')); }
function mmss(s){
  s = Math.max(0, Math.round(s));
  return Math.floor(s/60) + ':' + ('0' + (s%60)).slice(-2);
}

/* ------------------------------------------------------------- routing */
function show(view){
  ['home','math','weak','quiz','result','dash','plan'].forEach(function(v){
    var n = $('view-' + v); if (n) n.hidden = (v !== view);
  });
  document.querySelectorAll('nav button').forEach(function(b){
    b.classList.toggle('on', b.dataset.view === view);
  });
  if (view === 'dash') refreshThen(renderDash);
  if (view === 'plan') renderPlan();
  if (view === 'math') renderMathStats();
  if (view === 'weak') refreshThen(renderWeak);
  if (view === 'home') renderHomeWeak();
  window.scrollTo(0, 0);
}
document.querySelectorAll('nav button').forEach(function(b){
  b.onclick = function(){
    if (QUIZ && !confirm('Leave this quiz? It will not be scored.')) return;
    if (QUIZ) stopTimer();
    QUIZ = null;
    show(b.dataset.view);
  };
});

/* ---------------------------------------------------------------- boot */
Promise.all([api('/api/meta'), api('/api/progress')]).then(function(r){
  META = r[0]; PROGRESS = r[1];
  fillTopicPicker(); fillMathPicker(); fillWeakPicker(); fillProfile();
  renderHomeWeak(); renderCountdown();
});

function fillTopicPicker(){
  var sel = $('topic'), portion = $('portion').value;
  sel.innerHTML = '<option value="">All topics (exam-weighted)</option>';
  META.topics.forEach(function(t){
    if (portion !== 'mixed' && t.portion !== portion) return;
    if (portion === 'mixed' && t.portion === 'comprehensive') return;
    var o = el('option', null, t.label + '  (' + t.exam_questions + ' on exam)');
    o.value = t.key; sel.appendChild(o);
  });
}
$('portion').onchange = fillTopicPicker;

function fillMathPicker(){
  var sel = $('mathTopic');
  META.math_topics.forEach(function(t){
    var o = el('option', null, t.label); o.value = t.key; sel.appendChild(o);
  });
}

function fillWeakPicker(){
  var box = $('weakPicker');
  box.innerHTML = '';
  var chosen = (PROGRESS.profile.declared_weak) || [];
  META.topics.forEach(function(t){
    var lab = el('label', 'focus');
    lab.style.cursor = 'pointer';
    var cb = el('input'); cb.type = 'checkbox'; cb.value = t.key;
    cb.checked = chosen.indexOf(t.key) >= 0;
    cb.style.width = 'auto'; cb.style.marginRight = '7px';
    lab.appendChild(cb);
    lab.appendChild(document.createTextNode(t.label));
    var tag = el('span', 'tag' + (t.portion === 'georgia' ? ' ga' : ''),
                 t.portion === 'georgia' ? 'GA' : 'NAT');
    tag.style.marginLeft = '6px';
    lab.appendChild(tag);
    box.appendChild(lab);
  });
}

function fillProfile(){
  var p = PROGRESS.profile || {};
  if (p.exam_date) $('examDate').value = p.exam_date;
  if (p.mastery_date) $('masteryDate').value = p.mastery_date;
  if (p.hours_per_week) $('hours').value = p.hours_per_week;
}

function renderCountdown(){
  var p = PROGRESS.profile || {};
  if (!p.exam_date){ $('countdown').textContent = 'salesperson licensing exam'; return; }
  var days = Math.ceil((new Date(p.exam_date + 'T00:00:00') - new Date()) / 86400000);
  $('countdown').textContent = days >= 0
    ? days + ' day' + (days === 1 ? '' : 's') + ' until your exam'
    : 'exam date has passed';
}

/* ------------------------------------------------------- home weak list */
function renderHomeWeak(){
  var box = $('homeWeak');
  box.innerHTML = '';
  var rows = (PROGRESS.topics || []).filter(function(t){ return t.seen > 0; });
  if (!rows.length){
    var c = el('div', 'card');
    c.appendChild(el('div', 'empty',
      'No attempts yet. Take a 20-question quiz and this fills in with your weakest topics.'));
    box.appendChild(c); return;
  }
  var card = el('div', 'card');
  card.appendChild(el('h2', null, 'Where you stand'));
  var t = el('table');
  t.innerHTML = '<tr><th>Topic</th><th></th><th class="num">Score</th><th class="num">Qs</th></tr>';
  rows.slice(0, 8).forEach(function(r){
    var tr = el('tr');
    var td1 = el('td'); td1.appendChild(document.createTextNode(r.label + ' '));
    td1.appendChild(tagFor(r.portion));
    var td2 = el('td');
    var track = el('div', 'bar-track');
    var fill = el('div', 'bar-fill ' + band(r.pct));
    fill.style.width = Math.round((r.pct || 0) * 100) + '%';
    track.appendChild(fill); td2.appendChild(track);
    tr.appendChild(td1); tr.appendChild(td2);
    tr.appendChild(el('td', 'num', pct(r.pct)));
    tr.appendChild(el('td', 'num', String(r.seen)));
    t.appendChild(tr);
  });
  card.appendChild(t);
  box.appendChild(card);
}

/* -------------------------------------------------------------- starting */
function startQuiz(opts){
  api('/api/quiz/start', opts).then(function(r){
    if (r.error){ alert(r.error); return; }
    LAST = opts;
    QUIZ = {
      id: r.session, qs: r.questions, i: 0, answered: 0, correct: 0,
      limit: r.limit_seconds, started: Date.now(), qStart: Date.now(),
      portion: r.portion, locked: false
    };
    show('quiz'); startTimer(); renderQuestion();
  });
}

function diffValue(){ var n = $('difficulty'); return n ? n.value : 'harder'; }

$('start').onclick = function(){
  startQuiz({portion: $('portion').value, count: +$('count').value,
             topic: $('topic').value || null, timed: $('timed').value === '1',
             difficulty: diffValue()});
};
$('startWeak').onclick = function(){
  startQuiz({portion: $('portion').value, count: +$('count').value,
             weak_spot: true, timed: $('timed').value === '1',
             difficulty: diffValue()});
};
$('startExam').onclick = function(){
  if (!confirm('Full mock exam: 132 questions, about 2 h 45 m. Start?')) return;
  startQuiz({mode: 'exam', timed: true, difficulty: diffValue()});
};
$('startMath').onclick = function(){
  startQuiz({portion: 'math', count: +$('mathCount').value,
             topic: $('mathTopic').value || null, timed: false});
};
$('startMathWeak').onclick = function(){
  startQuiz({portion: 'math', count: +$('mathCount').value, weak_spot: true, timed: false});
};

/* ---------------------------------------------------------------- timer */
function startTimer(){
  stopTimer();
  if (!QUIZ.limit){ $('qtimer').textContent = ''; return; }
  TICK = setInterval(function(){
    if (!QUIZ) return stopTimer();
    var left = QUIZ.limit - (Date.now() - QUIZ.started) / 1000;
    $('qtimer').textContent = mmss(left);
    $('qtimer').classList.toggle('warn', left < 120);
    if (left <= 0){ stopTimer(); alert('Time is up. Scoring what you have.'); finish(); }
  }, 500);
}
function stopTimer(){ if (TICK){ clearInterval(TICK); TICK = null; } }

/* ------------------------------------------------------------- question */
function renderQuestion(){
  var q = QUIZ.qs[QUIZ.i];
  QUIZ.locked = false;
  QUIZ.qStart = Date.now();
  $('qprog').style.width = (QUIZ.i / QUIZ.qs.length * 100) + '%';
  $('qcount').textContent = 'Question ' + (QUIZ.i + 1) + ' of ' + QUIZ.qs.length;
  var isGA = q.portion === 'georgia', isComp = q.portion === 'comprehensive';
  $('qtag').textContent = isComp ? 'Comprehensive'
                        : (q.generator ? 'Math' : (isGA ? 'Georgia' : 'National'));
  $('qtag').className = 'tag' + (isGA ? ' ga' : (isComp ? ' comp' : ''));
  $('qhard').hidden = ((q.difficulty || 1) !== 2);
  $('qtopic').textContent = q.topic_label;
  $('qtext').textContent = q.q;
  $('qfeedback').innerHTML = '';
  $('qnext').disabled = true;
  $('qnext').textContent = (QUIZ.i === QUIZ.qs.length - 1) ? 'Finish' : 'Next';

  var box = $('qchoices');
  box.innerHTML = '';
  q.choices.forEach(function(text, k){
    var b = el('button', 'choice');
    b.appendChild(el('span', 'k', 'ABCD'[k]));
    b.appendChild(el('span', null, text));
    b.onclick = function(){ answer(k); };
    box.appendChild(b);
  });
}

function answer(choice){
  if (QUIZ.locked) return;
  QUIZ.locked = true;
  var secs = (Date.now() - QUIZ.qStart) / 1000;
  api('/api/quiz/answer', {session: QUIZ.id, index: QUIZ.i,
                           choice: choice, seconds: secs}).then(function(r){
    if (r.error){ alert(r.error); QUIZ = null; show('home'); return; }
    QUIZ.answered++;
    if (r.correct) QUIZ.correct++;
    var btns = $('qchoices').children;
    for (var k = 0; k < btns.length; k++){
      btns[k].disabled = true;
      if (k === r.answer) btns[k].classList.add('correct');
      else if (k === choice) btns[k].classList.add('wrong');
    }
    var fb = el('div', 'feedback ' + (r.correct ? 'ok' : 'no'));
    fb.appendChild(el('div', 'verdict', r.correct ? 'Correct' : 'Not quite'));
    if (!r.correct)
      fb.appendChild(el('div', null, 'Correct answer: ' + 'ABCD'[r.answer] + '. ' + r.answer_text));
    if (r.steps && r.steps.length){
      var ol = el('ol', 'steps');
      r.steps.forEach(function(s){ ol.appendChild(el('li', null, s)); });
      fb.appendChild(ol);
    } else if (r.explain){
      fb.appendChild(el('div', null, r.explain));
    }
    if (r.concept){
      var c = el('div', 'concept');
      c.appendChild(el('b', null, 'Concept tested: '));
      c.appendChild(document.createTextNode(r.concept));
      fb.appendChild(c);
    }
    $('qfeedback').innerHTML = '';
    $('qfeedback').appendChild(fb);
    $('qnext').disabled = false;
    $('qnext').focus();
  });
}

$('qnext').onclick = function(){
  if (QUIZ.i >= QUIZ.qs.length - 1) return finish();
  QUIZ.i++;
  renderQuestion();
};
$('qquit').onclick = function(){
  if (confirm('End the quiz now and score what you have answered?')) finish();
};
document.addEventListener('keydown', function(e){
  if (!QUIZ || $('view-quiz').hidden) return;
  var k = 'abcd'.indexOf(e.key.toLowerCase());
  if (k >= 0 && !QUIZ.locked) answer(k);
  if ((e.key === 'Enter' || e.key === ' ') && !$('qnext').disabled){
    e.preventDefault(); $('qnext').click();
  }
});

/* -------------------------------------------------------------- finish */
function finish(){
  stopTimer();
  var sid = QUIZ.id;
  QUIZ = null;
  api('/api/quiz/finish', {session: sid}).then(function(r){
    if (r.error){ alert(r.error); show('home'); return; }
    PROGRESS = r.progress;
    renderResult(r.attempt);
    renderCountdown();
    show('result');
  });
}

function renderResult(a){
  var box = $('resultBody');
  box.innerHTML = '';
  var head = el('div', 'card');
  var g = el('div', 'grid g3');
  [['Score', pct(a.pct)], ['Correct', a.correct + ' of ' + a.count],
   ['Time', mmss(a.seconds)]].forEach(function(p){
    var d = el('div');
    d.appendChild(el('div', 'muted', p[0]));
    d.appendChild(el('div', 'stat', p[1]));
    g.appendChild(d);
  });
  head.appendChild(g);
  var passish = a.pct >= 0.75;
  head.appendChild(el('p', 'muted', passish
    ? 'At or above 75% -- that is roughly the zone you want to be in before exam day.'
    : 'Georgia requires 75% to pass. Keep drilling the topics below.'));
  box.appendChild(head);

  var rows = Object.keys(a.topics || {});
  if (rows.length){
    var card = el('div', 'card');
    card.appendChild(el('h2', null, 'This attempt, by topic'));
    var t = el('table');
    t.innerHTML = '<tr><th>Topic</th><th class="num">Correct</th><th class="num">Score</th></tr>';
    rows.map(function(k){
      var v = a.topics[k];
      return {k: k, v: v, p: v.correct / v.seen};
    }).sort(function(x, y){ return x.p - y.p; }).forEach(function(r){
      var label = (META.topics.filter(function(t2){ return t2.key === r.k; })[0] || {}).label || r.k;
      var tr = el('tr');
      tr.appendChild(el('td', null, label));
      tr.appendChild(el('td', 'num', r.v.correct + '/' + r.v.seen));
      tr.appendChild(el('td', 'num', pct(r.p)));
      t.appendChild(tr);
    });
    card.appendChild(t);
    box.appendChild(card);
  }
}

$('againSame').onclick = function(){ startQuiz(LAST || {portion:'national', count:20}); };
$('againWeak').onclick = function(){
  startQuiz({portion: (LAST && LAST.portion) || 'national', count: 20, weak_spot: true, timed: true});
};
$('toDash').onclick = function(){ show('dash'); };

function refreshThen(fn){
  api('/api/progress').then(function(p){ PROGRESS = p; renderCountdown(); fn(); });
}

/* ----------------------------------------------------------- weak spots */
function renderWeak(){
  var box = $('weakBody');
  box.innerHTML = '';

  var rows = (PROGRESS.topics || []);
  var weak = rows.filter(function(r){ return r.seen >= 3; })
                 .sort(function(a, b){
                   if (a.pct !== b.pct) return a.pct - b.pct;
                   return b.exam_questions - a.exam_questions;
                 }).slice(0, 10);
  var untested = rows.filter(function(r){ return r.seen < 3; });

  var act = el('div', 'card');
  act.appendChild(el('h2', null, 'Drill everything you are weakest at'));
  act.appendChild(el('p', 'muted',
    'Weak-spot mode weights topics by your miss rate and by what they are worth on the ' +
    'exam, and puts questions you have already missed at the front of the queue.'));
  var row = el('div', 'row');
  [['Weak spots: National', 'national'], ['Weak spots: Georgia', 'georgia'],
   ['Weak spots: both portions', 'mixed']].forEach(function(p){
    var d = el('div'); d.style.flex = '0 0 auto';
    var b = el('button', 'btn' + (p[1] === 'mixed' ? ' ghost' : ''), p[0] + ' (20)');
    b.onclick = function(){
      startQuiz({portion: p[1], count: 20, weak_spot: true, timed: true, difficulty: 'harder'});
    };
    d.appendChild(b); row.appendChild(d);
  });
  act.appendChild(row);
  box.appendChild(act);

  var card = el('div', 'card');
  card.appendChild(el('h2', null, 'Your weakest topics'));
  if (!weak.length){
    card.appendChild(el('div', 'empty',
      'Not enough data yet. Answer at least 3 questions in a topic and it appears here.'));
  } else {
    var t = el('table');
    t.innerHTML = '<tr><th>Topic</th><th></th><th class="num">Score</th>' +
                  '<th class="num">Asked</th><th class="num">On exam</th><th></th></tr>';
    weak.forEach(function(r){
      var tr = el('tr'), td = el('td');
      td.appendChild(document.createTextNode(r.label + ' '));
      td.appendChild(tagFor(r.portion));
      tr.appendChild(td);
      var td2 = el('td'), track = el('div', 'bar-track');
      var fill = el('div', 'bar-fill ' + band(r.pct));
      fill.style.width = Math.round((r.pct || 0) * 100) + '%';
      track.appendChild(fill); td2.appendChild(track); tr.appendChild(td2);
      tr.appendChild(el('td', 'num', pct(r.pct)));
      tr.appendChild(el('td', 'num', String(r.seen)));
      tr.appendChild(el('td', 'num',
        countsOnExam(r.topic) ? String(r.exam_questions) : 'drill'));
      var td3 = el('td');
      var b = el('button', 'btn ghost', 'Drill 15');
      b.onclick = function(){
        startQuiz({portion: r.portion, count: 15, topic: r.topic,
                   timed: false, difficulty: 'harder'});
      };
      td3.appendChild(b); tr.appendChild(td3);
      t.appendChild(tr);
    });
    card.appendChild(t);
    card.appendChild(el('p', 'muted',
      'Score is your all-time accuracy in that topic. "On exam" is how many of the 132 ' +
      'scored questions come from it \u2014 a low score in a heavily weighted topic costs ' +
      'you the most points.'));
  }
  box.appendChild(card);

  var mrows = (PROGRESS.generators || []).filter(function(g){
    return g.seen >= 2 && g.pct !== null && g.pct < 0.8;
  });
  if (mrows.length){
    var mc = el('div', 'card');
    mc.appendChild(el('h2', null, 'Math types to drill'));
    var mt = el('table');
    mt.innerHTML = '<tr><th>Type</th><th class="num">Score</th><th></th></tr>';
    mrows.slice(0, 6).forEach(function(g){
      var tr = el('tr');
      tr.appendChild(el('td', null, g.label));
      tr.appendChild(el('td', 'num', pct(g.pct)));
      var td = el('td'), b = el('button', 'btn ghost', 'Drill 10');
      b.onclick = function(){
        startQuiz({portion: 'math', count: 10, topic: g.key, timed: false});
      };
      td.appendChild(b); tr.appendChild(td); mt.appendChild(tr);
    });
    mc.appendChild(mt); box.appendChild(mc);
  }

  if (untested.length){
    var uc = el('div', 'card');
    uc.appendChild(el('h2', null, 'Not tested yet'));
    uc.appendChild(el('p', 'muted',
      'Fewer than 3 questions answered. Unknown is not the same as weak, but it is worth ' +
      'finding out before exam day.'));
    var list = el('div', 'focuslist');
    untested.forEach(function(r){
      var d = el('div', 'focus');
      d.style.cssText = 'display:flex;justify-content:space-between;align-items:center;gap:10px';
      var left = el('div');
      left.appendChild(el('b', null, r.label));
      left.appendChild(document.createTextNode(' '));
      left.appendChild(tagFor(r.portion));
      left.appendChild(el('div', 'muted', r.seen ? (r.seen + ' answered so far') : 'never attempted'));
      d.appendChild(left);
      var b = el('button', 'btn ghost', 'Drill 10');
      b.onclick = function(){
        startQuiz({portion: r.portion, count: 10, topic: r.topic, timed: false, difficulty: 'harder'});
      };
      d.appendChild(b);
      list.appendChild(d);
    });
    uc.appendChild(list); box.appendChild(uc);
  }
}

/* ----------------------------------------------------------- dashboard */
function sparkline(points, w, h){
  var ns = 'http://www.w3.org/2000/svg';
  var svg = document.createElementNS(ns, 'svg');
  svg.setAttribute('viewBox', '0 0 ' + w + ' ' + h);
  svg.setAttribute('width', w); svg.setAttribute('height', h);
  [0.5, 0.75, 1].forEach(function(y){
    var ln = document.createElementNS(ns, 'line');
    var yy = h - y * (h - 12) - 6;
    ln.setAttribute('x1', 22); ln.setAttribute('x2', w);
    ln.setAttribute('y1', yy); ln.setAttribute('y2', yy);
    ln.setAttribute('class', 'gl'); ln.setAttribute('stroke-dasharray', y === 0.75 ? '3 3' : '');
    svg.appendChild(ln);
    var tx = document.createElementNS(ns, 'text');
    tx.setAttribute('x', 0); tx.setAttribute('y', yy + 3);
    tx.textContent = Math.round(y * 100) + '%';
    svg.appendChild(tx);
  });
  if (points.length){
    var step = points.length > 1 ? (w - 30) / (points.length - 1) : 0;
    var d = points.map(function(p, i){
      var x = 24 + i * step, y = h - p.pct * (h - 12) - 6;
      return (i ? 'L' : 'M') + x.toFixed(1) + ' ' + y.toFixed(1);
    }).join(' ');
    var path = document.createElementNS(ns, 'path');
    path.setAttribute('d', d); path.setAttribute('fill', 'none');
    path.setAttribute('stroke', 'currentColor'); path.setAttribute('stroke-width', '2');
    path.setAttribute('stroke-linejoin', 'round');
    svg.appendChild(path);
    points.forEach(function(p, i){
      var c = document.createElementNS(ns, 'circle');
      c.setAttribute('cx', 24 + i * step);
      c.setAttribute('cy', h - p.pct * (h - 12) - 6);
      c.setAttribute('r', 2.5); c.setAttribute('fill', 'currentColor');
      svg.appendChild(c);
    });
  }
  return svg;
}

function renderDash(){
  var box = $('dashBody');
  box.innerHTML = '';
  if (!PROGRESS.total_attempts){
    var c = el('div', 'card');
    c.appendChild(el('div', 'empty', 'No attempts recorded yet. Take a quiz first.'));
    box.appendChild(c); return;
  }
  var head = el('div', 'card');
  var g = el('div', 'grid g3');
  var NAMES = {national:'National portion', georgia:'Georgia portion',
               comprehensive:'Comprehensive subtest'};
  ['national', 'georgia', 'comprehensive'].forEach(function(p){
    var s = PROGRESS.portions[p] || {};
    var d = el('div');
    d.appendChild(el('div', 'muted', NAMES[p]));
    d.appendChild(el('div', 'stat', pct(s.recent_pct)));
    var note = s.attempts ? (s.attempts + ' attempts, ' + s.questions + ' questions') : 'no attempts yet';
    if (s.trend !== null && s.trend !== undefined){
      note += ' | trend ' + (s.trend >= 0 ? '+' : '') + Math.round(s.trend * 100) + ' pts';
    }
    d.appendChild(el('div', 'muted', note));
    g.appendChild(d);
  });
  var d3 = el('div');
  d3.appendChild(el('div', 'muted', 'Total attempts'));
  d3.appendChild(el('div', 'stat', String(PROGRESS.total_attempts)));
  g.appendChild(d3);
  head.appendChild(g);
  box.appendChild(head);

  var card = el('div', 'card');
  card.appendChild(el('h2', null, 'Score trend by topic'));
  card.appendChild(el('p', 'muted',
    'Each point is one quiz that included the topic. Dashed line is the 75% pass mark.'));
  var any = false;
  (PROGRESS.topics || []).forEach(function(t){
    var series = (PROGRESS.trends || {})[t.topic];
    if (!series || !series.length) return;
    any = true;
    var row = el('div');
    row.style.cssText = 'display:flex;gap:14px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line)';
    var left = el('div'); left.style.cssText = 'flex:1;min-width:150px';
    var name = el('div');
    name.appendChild(el('b', null, t.label));
    name.appendChild(document.createTextNode(' '));
    name.appendChild(tagFor(t.portion));
    left.appendChild(name);
    left.appendChild(el('div', 'muted', pct(t.pct) + ' overall, ' + t.seen +
                        ' questions | worth ' + t.exam_questions + ' on the exam'));
    var right = el('div');
    right.style.color = 'var(--accent)';
    right.appendChild(sparkline(series, 280, 84));
    row.appendChild(left); row.appendChild(right);
    card.appendChild(row);
  });
  if (!any) card.appendChild(el('div', 'empty', 'Take a couple of quizzes to see trends.'));
  box.appendChild(card);

  var mc = el('div', 'card');
  mc.appendChild(el('h2', null, 'Math by problem type'));
  var mt = el('table');
  mt.innerHTML = '<tr><th>Type</th><th class="num">Correct</th><th class="num">Score</th></tr>';
  var seenAny = false;
  (PROGRESS.generators || []).forEach(function(gn){
    if (!gn.seen) return;
    seenAny = true;
    var tr = el('tr');
    tr.appendChild(el('td', null, gn.label));
    tr.appendChild(el('td', 'num', gn.correct + '/' + gn.seen));
    tr.appendChild(el('td', 'num', pct(gn.pct)));
    mt.appendChild(tr);
  });
  if (seenAny) mc.appendChild(mt);
  else mc.appendChild(el('div', 'empty', 'No math attempts yet.'));
  box.appendChild(mc);
}

function renderMathStats(){
  var box = $('mathStats');
  box.innerHTML = '';
  var rows = (PROGRESS.generators || []).filter(function(g){ return g.seen; });
  var card = el('div', 'card');
  card.appendChild(el('h2', null, 'Your math history'));
  if (!rows.length){
    card.appendChild(el('div', 'empty', 'No math attempts yet -- start a set above.'));
  } else {
    var t = el('table');
    t.innerHTML = '<tr><th>Type</th><th class="num">Score</th><th>Concept</th></tr>';
    rows.forEach(function(g){
      var tr = el('tr');
      tr.appendChild(el('td', null, g.label));
      tr.appendChild(el('td', 'num', pct(g.pct)));
      tr.appendChild(el('td', 'muted', g.concept));
      t.appendChild(tr);
    });
    card.appendChild(t);
  }
  box.appendChild(card);
}

/* ---------------------------------------------------------------- plan */
$('savePlan').onclick = function(){
  var weak = [];
  $('weakPicker').querySelectorAll('input:checked').forEach(function(c){ weak.push(c.value); });
  api('/api/profile', {
    exam_date: $('examDate').value || null,
    mastery_date: $('masteryDate').value || null,
    hours_per_week: +$('hours').value || 8,
    declared_weak: weak
  }).then(function(){
    return api('/api/progress');
  }).then(function(p){
    PROGRESS = p; renderCountdown(); renderPlan();
  });
};

function renderPlan(){
  var box = $('planBody');
  box.innerHTML = '<div class="card"><div class="empty">Building plan...</div></div>';
  api('/api/plan').then(function(p){
    box.innerHTML = '';
    if (p.error){
      var c = el('div', 'card');
      c.appendChild(el('div', 'empty', p.error));
      box.appendChild(c); return;
    }
    var head = el('div', 'card');
    var g = el('div', 'grid g3');
    [['Days to exam', String(p.days_to_exam)],
     ['Days to your mastery date', String(p.days_to_mastery)],
     ['Exam split', p.weighting.national + ' national / ' + p.weighting.georgia + ' Georgia']
    ].forEach(function(r){
      var d = el('div');
      d.appendChild(el('div', 'muted', r[0]));
      d.appendChild(el('div', 'stat small', r[1]));
      g.appendChild(d);
    });
    head.appendChild(g);
    box.appendChild(head);

    p.weeks.forEach(function(w){
      var c = el('div', 'card');
      var wk = el('div', 'week');
      wk.appendChild(el('h3', null, 'Week ' + w.week + ' -- ' + w.phase));
      wk.appendChild(el('div', 'when', w.start + ' to ' + w.end + '  |  target ' +
        w.target_questions + ' questions (' + w.national_questions + ' national, ' +
        w.georgia_questions + ' Georgia)'));
      var ul = el('ul');
      w.tasks.forEach(function(t){ ul.appendChild(el('li', null, t)); });
      wk.appendChild(ul);
      if (w.focus.length){
        var fl = el('div', 'focuslist');
        w.focus.forEach(function(f){
          var d = el('div', 'focus');
          d.appendChild(el('b', null, f.label));
          d.appendChild(el('span', 'tag' + (f.portion === 'georgia' ? ' ga' : ''),
                          f.portion === 'georgia' ? ' GA ' : ' NAT '));
          d.appendChild(el('div', 'muted', f.why));
          fl.appendChild(d);
        });
        wk.appendChild(fl);
      }
      c.appendChild(wk);
      box.appendChild(c);
    });

    if (p.buffer_plan && p.buffer_plan.length){
      var b = el('div', 'card');
      b.appendChild(el('h2', null, 'Final ' + p.buffer_days + ' days before the exam'));
      var ul2 = el('ul');
      p.buffer_plan.forEach(function(t){ ul2.appendChild(el('li', null, t)); });
      b.appendChild(ul2);
      box.appendChild(b);
    }
  });
}
