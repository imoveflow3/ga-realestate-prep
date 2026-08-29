/* Georgia Real Estate Prep -- single page app, no dependencies. */
'use strict';

var META = null, PROGRESS = null, QUIZ = null, TICK = null, LAST = null;
var STUDY = null, STUDY_TOPIC = null;
var NB_OPEN_ONLY = true;

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
  ['dash','study','home','math','notebook','weak','quiz','result','plan'].forEach(function(v){
    var n = $('view-' + v); if (n) n.hidden = (v !== view);
  });
  document.querySelectorAll('#rail button').forEach(function(b){
    var on = b.dataset.view === view;
    b.classList.toggle('on', on);
    b.setAttribute('aria-current', on ? 'page' : 'false');
  });
  if (view === 'dash') refreshThen(renderDash);
  if (view === 'plan') renderPlan();
  if (view === 'study') renderStudy();
  if (view === 'notebook') refreshThen(renderNotebook);
  if (view === 'math') renderMathStats();
  if (view === 'weak') refreshThen(renderWeak);
  if (view === 'home') renderHomeWeak();
  window.scrollTo(0, 0);
}
document.querySelectorAll('#rail button').forEach(function(b){
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
  renderCountdown(); show('dash');
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

function ro(key, value, note, hero){
  var d = el('div', 'ro' + (hero ? ' hero' : ''));
  d.appendChild(el('div', 'k', key));
  var v = el('div', 'v', value);
  if (note) v.appendChild(el('small', null, '\u00b7 ' + note));
  d.appendChild(v);
  return d;
}

/* The status strip in the header: the five numbers worth seeing on every screen. */
function renderCountdown(){
  var box = $('readouts');
  if (!box) return;
  box.innerHTML = '';
  var h = PROGRESS.headline || {}, st = PROGRESS.portions || {};
  var hero = ro('Readiness', h.exam_pct == null ? '\u2014' : pct(h.exam_pct),
                h.exam_pct == null ? 'no data' : (h.passing ? 'passing' : 'need 75%'), true);
  if (h.exam_pct != null)
    hero.querySelector('.v').className = 'v ' + (h.passing ? 'good' : 'bad');
  box.appendChild(hero);
  box.appendChild(ro('National', (st.national && st.national.recent_pct != null)
                                   ? pct(st.national.recent_pct) : '\u2014', '80 q'));
  box.appendChild(ro('Georgia', (st.georgia && st.georgia.recent_pct != null)
                                  ? pct(st.georgia.recent_pct) : '\u2014', '52 q'));
  box.appendChild(ro('Answered', String(h.answered || 0),
                     (h.sets || 0) + ((h.sets === 1) ? ' set' : ' sets')));
  box.appendChild(ro('Days out', h.days_out == null ? '\u2014' : String(h.days_out),
                     h.days_out == null ? 'set a date' : 'until exam'));
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

/* -------------------------------------------------------------- notebook */
function nbOption(item, i){
  var row = el('div', 'nbopt' +
    (i === item.answer ? ' right' : (i === item.chose ? ' chose' : '')));
  row.appendChild(el('span', 'k', 'ABCD'[i]));
  row.appendChild(el('span', null, item.choices[i]));
  if (i === item.answer) row.appendChild(el('span', 'flag', 'correct'));
  else if (i === item.chose) row.appendChild(el('span', 'flag', 'you picked'));
  return row;
}

function notebookEntry(item){
  var wrap = el('div', 'nbitem' + (item.cleared ? ' done' : ''));
  var meta = el('div', 'nbmeta');
  if (item.subtopic) meta.appendChild(el('span', null, item.subtopic));
  if (item.difficulty === 2) meta.appendChild(el('span', 'tag hard', 'Hard'));
  if (item.times > 1) meta.appendChild(el('span', null, 'missed ' + item.times + '×'));
  if (item.cleared) meta.appendChild(el('span', 'tag', 'got it since'));
  if (item.recovered)
    meta.appendChild(el('span', null, 'from earlier quizzes'));
  else if (item.chose === null)
    meta.appendChild(el('span', null, 'ran out of time'));
  wrap.appendChild(meta);
  wrap.appendChild(el('p', 'nbq', item.q));
  var opts = el('div', 'nbopts');
  item.choices.forEach(function(_, i){ opts.appendChild(nbOption(item, i)); });
  wrap.appendChild(opts);
  if (item.recovered){
    wrap.appendChild(el('div', 'muted',
      'Recovered from a quiz you took before the notebook existed, so the answer ' +
      'you picked was not recorded — only that you missed it.'));
  }
  var why = el('div', 'nbwhy');
  if (item.steps && item.steps.length){
    why.appendChild(el('div', 'lab', 'How to get there'));
    var ol = el('ol', 'steps');
    item.steps.forEach(function(st){ ol.appendChild(el('li', null, st)); });
    why.appendChild(ol);
  } else if (item.explain){
    why.appendChild(el('div', 'lab', 'Why that is the answer'));
    why.appendChild(richPara(null, item.explain));
  }
  if (item.concept) why.appendChild(el('div', 'lab', 'Concept: ' + item.concept));
  wrap.appendChild(why);
  var acts = el('div', 'nbacts');
  acts.appendChild(studyButton(item.topic, 'STUDY THIS'));
  if (item.sub){
    var d = el('button', 'btn mini', 'DRILL IT');
    d.onclick = function(){
      startQuiz({portion:item.portion, count:10, sub:item.sub, timed:false, difficulty:'harder'});
    };
    acts.appendChild(d);
  } else if (item.generator){
    var g = el('button', 'btn mini', 'MORE LIKE THIS');
    g.onclick = function(){
      startQuiz({portion:'math', count:10, topic:item.generator, timed:false});
    };
    acts.appendChild(g);
  }
  var rm = el('button', 'btn mini ghost', 'REMOVE');
  rm.onclick = function(){
    api('/api/notebook/forget', {qid:item.qid}).then(function(r){
      if (r.progress) PROGRESS = r.progress;
      renderNotebook();
    });
  };
  acts.appendChild(rm);
  wrap.appendChild(acts);
  return wrap;
}

function renderNotebook(){
  var v = $('view-notebook');
  v.className = 'reading';
  var box = $('nbBody');
  box.innerHTML = '';
  var counts = PROGRESS.miss_counts || {open:0, cleared:0, total:0};
  var head = el('div','card');
  head.appendChild(cardHead('Notebook','every question you have got wrong'));
  head.appendChild(el('p','sub',
    'Each question you missed, grouped by topic, with the answer you picked, the ' +
    'right one, and why. Get the same question right later and it is marked off — ' +
    'so what stays open is what you still have not learned.'));
  if (counts.total){
    var f = el('div','nbfilter');
    var ob = el('button','btn' + (NB_OPEN_ONLY?'':' ghost'), 'Still open (' + counts.open + ')');
    ob.onclick = function(){ NB_OPEN_ONLY = true; renderNotebook(); };
    var ab = el('button','btn' + (NB_OPEN_ONLY?' ghost':''), 'All (' + counts.total + ')');
    ab.onclick = function(){ NB_OPEN_ONLY = false; renderNotebook(); };
    f.appendChild(ob); f.appendChild(ab);
    if (counts.cleared) f.appendChild(el('span','muted', counts.cleared + ' cleared so far'));
    head.appendChild(f);
  }
  box.appendChild(head);

  var rows = (PROGRESS.misses || []).filter(function(m){ return NB_OPEN_ONLY ? !m.cleared : true; });
  if (!rows.length){
    var e = el('div','card');
    e.appendChild(el('div','empty', counts.total
      ? 'Nothing open — you have got every missed question right since. Switch to All to review them again.'
      : 'Nothing here yet. Take a quiz and anything you miss lands in this notebook automatically.'));
    box.appendChild(e); window.scrollTo(0,0); return;
  }
  var byTopic = {};
  rows.forEach(function(r){ (byTopic[r.topic] || (byTopic[r.topic] = [])).push(r); });
  (META.topics || []).forEach(function(t){
    var items = byTopic[t.key];
    if (!items) return;
    var card = el('div','card'), hd = el('div','cardhead');
    hd.appendChild(el('h2', null, t.label));
    hd.appendChild(el('span','hint',
      items.length + (items.length===1?' question':' questions') +
      (t.counts_on_exam !== false ? ' · ' + t.exam_questions + ' on exam' : ' · drill')));
    card.appendChild(hd);
    var list = el('div','nbgroup');
    items.forEach(function(i){ list.appendChild(notebookEntry(i)); });
    card.appendChild(list);
    box.appendChild(card);
  });
  window.scrollTo(0,0);
}

/* ---------------------------------------------------------------- study */
function studyButton(topicKey, label){
  var b = el('button', 'btn mini ghost', label || 'STUDY');
  b.onclick = function(){ STUDY_TOPIC = topicKey; show('study'); };
  return b;
}

/* Build a text fragment, styling runs of capitals so they read as emphasis
   rather than shouting once the text is set in serif at reading size. */
var CAPS_RE = /\b[A-Z][A-Z&.''-]+(?:\s+[A-Z][A-Z&.''-]+)*\b/g;
function richText(text){
  var frag = document.createDocumentFragment();
  var last = 0, m;
  CAPS_RE.lastIndex = 0;
  while ((m = CAPS_RE.exec(text)) !== null){
    if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
    frag.appendChild(el('span', 'caps', m[0]));
    last = m.index + m[0].length;
  }
  if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
  return frag;
}
function richPara(cls, text){
  var n = el('p', cls);
  n.appendChild(richText(text));
  return n;
}

/* "Acceleration - on default the balance is due" reads far better as a bolded
   term followed by its explanation, so split the label out where there is one. */
function bulletItem(text){
  var li = el('li');
  var m = /^(.{2,48}?)\s+(?:--|-|–)\s+(.+)$/.exec(text);
  if (m && !/[.?!]$/.test(m[1])){
    li.appendChild(el('span', 'term', m[1]));
    li.appendChild(richText(m[2]));
  } else {
    li.appendChild(richText(text));
  }
  return li;
}

function renderStudy(){
  if (!STUDY){
    $('studyBody').innerHTML = '<div class="card"><div class="empty">Loading notes…</div></div>';
    api('/api/study').then(function(d){ STUDY = d; renderStudy(); });
    return;
  }
  $('view-study').className = 'reading';
  if (STUDY_TOPIC && STUDY.topics[STUDY_TOPIC]) return renderStudyTopic(STUDY.topics[STUDY_TOPIC]);

  var box = $('studyBody');
  box.innerHTML = '';
  var intro = el('div', 'card');
  intro.appendChild(cardHead('Study', 'read it, then quiz it'));
  intro.appendChild(el('p', 'sub',
    'Notes for every topic you are quizzed on — definitions, the rules, worked ' +
    'examples, Georgia differences, and the mistakes that cost people marks.'));
  box.appendChild(intro);

  var NAMES = {national:'National portion', georgia:'Georgia state portion',
               comprehensive:'Comprehensive subtest'};
  ['national','georgia','comprehensive'].forEach(function(portion){
    var keys = Object.keys(STUDY.topics).filter(function(k){
      return STUDY.topics[k].portion === portion; });
    if (!keys.length) return;
    var card = el('div','card');
    card.appendChild(cardHead(NAMES[portion],
      portion==='comprehensive' ? 'cross-cutting drill'
        : (portion==='national' ? '80 questions' : '52 questions')));
    var list = el('div','topiclist');
    keys.forEach(function(k){
      var n = STUDY.topics[k];
      var row = el('div','topicrow'), who = el('div','who');
      who.appendChild(el('div','nm', n.label));
      who.appendChild(el('div','bl', n.blurb));
      row.appendChild(who);
      var acts = el('div','acts');
      acts.appendChild(el('span','cnt',
        (n.counts_on_exam ? n.exam_questions + ' on exam \u00b7 ' : 'drill \u00b7 ') +
        n.vocab.length + ' terms'));
      acts.appendChild(studyButton(k,'READ'));
      var qb = el('button','btn mini','QUIZ');
      qb.onclick = (function(key,p){
        return function(){
          startQuiz({portion:p, count:15, topic:key, timed:false, difficulty:'harder'});
        };
      })(k, n.portion);
      acts.appendChild(qb);
      row.appendChild(acts);
      list.appendChild(row);
    });
    card.appendChild(list);
    box.appendChild(card);
  });

  var src = el('div','card');
  src.appendChild(cardHead('Where this comes from','sources'));
  src.appendChild(el('p','muted',
    'These notes were written for this app. Georgia facts are checked against the ' +
    'Commission’s own published reference; federal rules against the agencies that ' +
    'issue them. No commercial exam-prep book is reproduced here.'));
  var list = el('div','callouts');
  (STUDY.sources||[]).forEach(function(s2){
    var d = el('div','callout');
    var a = el('a', null, s2.name);
    a.href = s2.url; a.target='_blank'; a.rel='noopener noreferrer';
    a.style.cssText = 'color:var(--accent);font-family:\"Barlow\",sans-serif;font-weight:600';
    d.appendChild(a);
    d.appendChild(document.createTextNode(' \u2014 ' + s2.by + '. ' + s2.note));
    list.appendChild(d);
  });
  src.appendChild(list);
  box.appendChild(src);
}

/* A short self-test after each section. Deliberately NOT recorded against your
   scores - these check that you took the reading in, and counting them would
   flatter the readiness number on the dashboard. */
function checkBlock(sec){
  var qs = sec.check || [];
  if (!qs.length) return null;
  var box = el('div', 'check');
  var head = el('div', 'checkhead');
  head.appendChild(el('span', null, 'Check yourself'));
  var score = el('span', 'checkscore', '0 / ' + qs.length);
  head.appendChild(score);
  box.appendChild(head);

  var right = 0;
  qs.forEach(function(q){
    var wrap = el('div', 'checkq');
    wrap.appendChild(el('p', 'cq', q.q));
    var opts = el('div', 'copts');
    var why = el('div', 'cwhy');
    why.hidden = true;
    q.choices.forEach(function(text, i){
      var b = el('button', 'copt', text);
      b.onclick = function(){
        var correct = (i === q.answer);
        if (correct) right++;
        score.textContent = right + ' / ' + qs.length;
        Array.prototype.forEach.call(opts.children, function(btn, j){
          btn.disabled = true;
          if (j === q.answer) btn.className = 'copt right';
          else if (j === i) btn.className = 'copt wrong';
        });
        why.className = 'cwhy ' + (correct ? 'ok' : 'no');
        why.innerHTML = '';
        why.appendChild(el('b', null, correct ? 'Correct' : 'Not quite'));
        why.appendChild(document.createTextNode(q.why));
        why.hidden = false;
      };
      opts.appendChild(b);
    });
    wrap.appendChild(opts);
    wrap.appendChild(why);
    box.appendChild(wrap);
  });
  return box;
}

function renderStudyTopic(n){
  var box = $('studyBody');
  box.innerHTML = '';
  var head = el('div','card'), hd = el('div','cardhead'), left = el('div');
  left.appendChild(el('h1', null, n.label));
  left.appendChild(el('div','muted',
    n.counts_on_exam ? (n.exam_questions + ' of the 132 scored questions come from this topic')
                     : 'A drill topic — not a scored section of the exam'));
  hd.appendChild(left);
  var back = el('button','btn mini ghost','ALL TOPICS');
  back.onclick = function(){ STUDY_TOPIC = null; renderStudy(); };
  hd.appendChild(back);
  head.appendChild(hd);
  head.appendChild(richPara('sub', n.summary));
  var acts = el('div','row');
  [['Quiz me on this (15)',15],['Quick check (5)',5]].forEach(function(a){
    var d = el('div'); d.style.flex='0 0 auto';
    var b = el('button','btn' + (a[1]===5?' ghost':''), a[0]);
    b.onclick = function(){
      startQuiz({portion:n.portion, count:a[1], topic:n.topic, timed:false, difficulty:'harder'});
    };
    d.appendChild(b); acts.appendChild(d);
  });
  head.appendChild(acts);
  box.appendChild(head);

  n.sections.forEach(function(sec){
    var c = el('div','card');
    c.appendChild(el('h2', null, sec.h));
    (sec.p||[]).forEach(function(para){ c.appendChild(richPara(null, para)); });
    if (sec.l && sec.l.length){
      var ul = el('ul');
      sec.l.forEach(function(i){ ul.appendChild(bulletItem(i)); });
      c.appendChild(ul);
    }
    var chk = checkBlock(sec);
    if (chk) c.appendChild(chk);
    box.appendChild(c);
  });

  if (n.vocab.length){
    var vc = el('div','card');
    vc.appendChild(cardHead('Vocabulary', n.vocab.length + ' terms'));
    var vl = el('div','vocablist');
    n.vocab.forEach(function(pair){
      var item = el('div','vocabitem');
      item.appendChild(el('div','vterm', pair[0]));
      var vd = el('div','vdef'); vd.appendChild(richText(pair[1]));
      item.appendChild(vd);
      vl.appendChild(item);
    });
    vc.appendChild(vl);
    box.appendChild(vc);
  }

  if (n.examples.length){
    var ec = el('div','card');
    ec.appendChild(cardHead('Worked examples','follow the steps'));
    n.examples.forEach(function(ex){
      var w = el('div','example');
      w.appendChild(el('h3', null, ex.t));
      var setup = el('div','setup'); setup.appendChild(richText(ex.s));
      w.appendChild(setup);
      var ol = el('ol','steps');
      ex.w.forEach(function(step){ ol.appendChild(el('li', null, step)); });
      w.appendChild(ol);
      var k = el('div','takeaway');
      k.appendChild(el('b', null, 'Takeaway'));
      k.appendChild(richText(ex.k));
      w.appendChild(k);
      ec.appendChild(w);
    });
    box.appendChild(ec);
  }

  [['Georgia differences','where Georgia departs from the national rule', n.ga, 'ga'],
   ['Common traps','where marks get lost', n.traps, 'trap']].forEach(function(blk){
    if (!blk[2] || !blk[2].length) return;
    var c = el('div','card');
    c.appendChild(cardHead(blk[0], blk[1]));
    var l = el('div','callouts');
    blk[2].forEach(function(i){
      var d = el('div','callout ' + blk[3]);
      d.appendChild(richText(i));
      l.appendChild(d);
    });
    c.appendChild(l); box.appendChild(c);
  });

  var foot = el('div','card'), frow = el('div','row');
  var d1 = el('div'); d1.style.flex='0 0 auto';
  var b1 = el('button','btn','Quiz me on this topic');
  b1.onclick = function(){
    startQuiz({portion:n.portion, count:15, topic:n.topic, timed:false, difficulty:'harder'});
  };
  d1.appendChild(b1); frow.appendChild(d1);
  var d2 = el('div'); d2.style.flex='0 0 auto';
  var b2 = el('button','btn ghost','Back to all topics');
  b2.onclick = function(){ STUDY_TOPIC = null; renderStudy(); };
  d2.appendChild(b2); frow.appendChild(d2);
  foot.appendChild(frow); box.appendChild(foot);
  window.scrollTo(0,0);
}

/* ----------------------------------------------------------- weak spots */
function renderWeak(){
  var box = $('weakBody');
  box.innerHTML = '';

  var rows = (PROGRESS.topics || []);
  var untested = rows.filter(function(r){ return r.seen < 3; });
  var subs = PROGRESS.subs || [];

  var act = el('div', 'card');
  act.appendChild(cardHead('Drill everything at once', 'weighted by miss rate and exam value'));
  act.appendChild(el('p', 'muted',
    'Weak-spot mode weights topics by how you have scored and by what they are worth on ' +
    'the exam, and puts questions you have already missed at the front of the queue.'));
  var row = el('div', 'row');
  [['National', 'national'], ['Georgia', 'georgia'], ['Both portions', 'mixed']]
    .forEach(function(p){
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
  card.appendChild(cardHead('Sub-topics you are weakest at', 'lowest accuracy first'));
  if (!subs.length){
    card.appendChild(el('div', 'empty',
      'Nothing ranked yet. Answer at least 2 questions in a sub-topic and it appears here ' +
      'with its own drill button.'));
  } else {
    var t = el('table', 'stats');
    t.innerHTML = '<tr><th>Weak spot</th><th>Topic</th><th class="num">Correct</th>' +
                  '<th class="num">Accuracy</th><th></th><th></th></tr>';
    subs.forEach(function(r){
      var parent = el('td');
      parent.appendChild(document.createTextNode(r.topic_label + ' '));
      parent.appendChild(tagFor(r.portion));
      t.appendChild(statRow([
        el('td', null, r.label), parent,
        el('td', 'num', r.correct + '/' + r.seen),
        el('td', 'num', pct(r.pct)), accuracyCell(r.pct),
        actionCell('DRILL', (function(sub, p){
          return function(){
            startQuiz({portion: p, count: 10, sub: sub, timed: false, difficulty: 'harder'});
          };
        })(r.sub, r.portion))
      ]));
    });
    var w = el('div', 'scroll'); w.appendChild(t); card.appendChild(w);
    card.appendChild(el('p', 'muted',
      'A drill starts with every question written for that sub-topic, then fills out the set ' +
      'from the rest of its parent topic so you always get a full round.'));
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

function cardHead(title, hint){
  var h = el('div', 'cardhead');
  h.appendChild(el('h2', null, title));
  if (hint) h.appendChild(el('span', 'hint', hint));
  return h;
}
function accuracyCell(p){
  var td = el('td'), track = el('div', 'bar-track');
  var fill = el('div', 'bar-fill ' + band(p));
  fill.style.width = Math.round((p || 0) * 100) + '%';
  track.appendChild(fill); td.appendChild(track);
  return td;
}
function trendCell(trend){
  if (trend === null || trend === undefined) return el('td', 'num muted', '—');
  var pts = Math.round(trend * 100);
  var td = el('td', 'num ' + (pts > 0 ? 'up' : (pts < 0 ? 'down' : '')));
  td.textContent = (pts > 0 ? '+' : '') + pts;
  return td;
}
function actionCell(label, fn){
  var td = el('td');
  var b = el('button', 'btn mini' + (label === 'START' ? ' ghost' : ''), label);
  b.onclick = fn; td.appendChild(b);
  return td;
}
function statRow(cells){
  var tr = el('tr');
  cells.forEach(function(c){ tr.appendChild(c); });
  return tr;
}

function renderDash(){
  var box = $('dashBody');
  box.innerHTML = '';

  if (!PROGRESS.total_attempts){
    var e = el('div', 'card');
    e.appendChild(el('div', 'empty',
      'No attempts recorded yet. Take a quiz and every table below fills in.'));
    box.appendChild(e); return;
  }

  var sec = el('div', 'card');
  sec.appendChild(cardHead('Sections', 'recent accuracy'));
  var st = el('table', 'stats');
  st.innerHTML = '<tr><th>Section</th><th class="num">Sets</th><th class="num">Qs</th>' +
                 '<th class="num">Recent</th><th></th><th class="num">Trend</th><th></th></tr>';
  (PROGRESS.sections || []).forEach(function(r){
    var name = el('td');
    name.appendChild(el('b', null, r.name));
    name.appendChild(document.createTextNode(' '));
    name.appendChild(r.scored ? el('span', 'tag', r.scored + ' on exam')
                              : el('span', 'tag comp', 'drill'));
    st.appendChild(statRow([
      name, el('td', 'num', String(r.sets)), el('td', 'num', String(r.qs)),
      el('td', 'num', r.recent_pct == null ? '—' : pct(r.recent_pct)),
      accuracyCell(r.recent_pct), trendCell(r.trend),
      actionCell(r.sets ? 'DRILL' : 'START', (function(p, has){
        return function(){
          startQuiz({portion: p, count: 20, weak_spot: has, timed: true, difficulty: 'harder'});
        };
      })(r.portion, !!r.sets))
    ]));
  });
  var sw = el('div', 'scroll'); sw.appendChild(st); sec.appendChild(sw);
  box.appendChild(sec);

  var tc = el('div', 'card');
  tc.appendChild(cardHead('Topics', 'badge is questions on the real exam'));
  var tt = el('table', 'stats');
  tt.innerHTML = '<tr><th>Topic</th><th class="num">Sets</th><th class="num">Qs</th>' +
                 '<th class="num">Recent</th><th></th><th class="num">Trend</th><th></th></tr>';
  var last = null;
  (PROGRESS.topic_table || []).forEach(function(r){
    if (r.portion !== last){
      last = r.portion;
      var hr = el('tr', 'grouprow');
      var cell = el('td', null, {national:'National portion', georgia:'Georgia state portion',
                                 comprehensive:'Comprehensive subtest'}[r.portion]);
      cell.colSpan = 7; hr.appendChild(cell); tt.appendChild(hr);
    }
    var name = el('td');
    name.appendChild(document.createTextNode(r.label + ' '));
    name.appendChild(r.counts_on_exam ? el('span', 'tag', String(r.exam_questions))
                                      : el('span', 'tag comp', 'drill'));
    tt.appendChild(statRow([
      name, el('td', 'num', String(r.sets)), el('td', 'num', String(r.qs)),
      el('td', 'num', r.recent_pct == null ? '—' : pct(r.recent_pct)),
      accuracyCell(r.recent_pct), trendCell(r.trend),
      actionCell(r.sets ? 'DRILL' : 'START', (function(t, p){
        return function(){
          startQuiz({portion: p, count: 15, topic: t, timed: false, difficulty: 'harder'});
        };
      })(r.topic, r.portion))
    ]));
  });
  var tw = el('div', 'scroll'); tw.appendChild(tt); tc.appendChild(tw);
  box.appendChild(tc);

  var subs = (PROGRESS.subs || []).slice(0, 12);
  var wc = el('div', 'card');
  wc.appendChild(cardHead('Weak spots', 'the little topics you got wrong'));
  if (!subs.length){
    wc.appendChild(el('div', 'empty',
      'Answer at least 2 questions in a sub-topic and the weak ones are listed here, ' +
      'each with its own drill.'));
  } else {
    var wt = el('table', 'stats');
    wt.innerHTML = '<tr><th>Weak spot</th><th>Topic</th><th class="num">Correct</th>' +
                   '<th class="num">Accuracy</th><th></th><th></th><th></th></tr>';
    subs.forEach(function(r){
      var parent = el('td');
      parent.appendChild(document.createTextNode(r.topic_label + ' '));
      parent.appendChild(tagFor(r.portion));
      var sbtn = el('td'); sbtn.appendChild(studyButton(r.topic, 'STUDY'));
      wt.appendChild(statRow([
        el('td', null, r.label), parent,
        el('td', 'num', r.correct + '/' + r.seen),
        el('td', 'num', pct(r.pct)), accuracyCell(r.pct), sbtn,
        actionCell('DRILL', (function(sub, p){
          return function(){
            startQuiz({portion: p, count: 10, sub: sub, timed: false, difficulty: 'harder'});
          };
        })(r.sub, r.portion))
      ]));
    });
    var ww = el('div', 'scroll'); ww.appendChild(wt); wc.appendChild(ww);
    wc.appendChild(el('p', 'muted',
      'A drill starts with every question written for that sub-topic, then fills out the ' +
      'set from the rest of its parent topic.'));
  }
  box.appendChild(wc);

  var mrows = (PROGRESS.generators || []).filter(function(x){ return x.seen; });
  var mc = el('div', 'card');
  mc.appendChild(cardHead('Math by problem type', 'weakest first'));
  if (!mrows.length){
    mc.appendChild(el('div', 'empty', 'No math attempts yet.'));
  } else {
    var mt = el('table', 'stats');
    mt.innerHTML = '<tr><th>Type</th><th class="num">Correct</th>' +
                   '<th class="num">Accuracy</th><th></th><th></th></tr>';
    mrows.forEach(function(x){
      mt.appendChild(statRow([
        el('td', null, x.label), el('td', 'num', x.correct + '/' + x.seen),
        el('td', 'num', pct(x.pct)), accuracyCell(x.pct),
        actionCell('DRILL', (function(k){
          return function(){ startQuiz({portion:'math', count:10, topic:k, timed:false}); };
        })(x.key))
      ]));
    });
    var mw = el('div', 'scroll'); mw.appendChild(mt); mc.appendChild(mw);
  }
  box.appendChild(mc);

  var series = PROGRESS.trends || {};
  var hasTrend = Object.keys(series).some(function(k){ return series[k].length >= 2; });
  if (hasTrend){
    var trc = el('div', 'card');
    trc.appendChild(cardHead('Score trend over time', 'dashed line is the 75% pass mark'));
    (PROGRESS.topics || []).forEach(function(t){
      var sd = series[t.topic];
      if (!sd || sd.length < 2) return;
      var row = el('div', 'trendrow'), who = el('div', 'who'), name = el('div');
      name.appendChild(el('b', null, t.label));
      name.appendChild(document.createTextNode(' '));
      name.appendChild(tagFor(t.portion));
      who.appendChild(name);
      who.appendChild(el('div', 'muted', pct(t.pct) + ' overall, ' + t.seen + ' questions'));
      row.appendChild(who);
      var chart = el('div'); chart.style.color = 'var(--accent)';
      chart.appendChild(sparkline(sd, 280, 84));
      row.appendChild(chart); trc.appendChild(row);
    });
    box.appendChild(trc);
  }
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
