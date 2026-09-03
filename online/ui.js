/* Views. Renders into the empty <section>s in the shell. */
'use strict';

var D = load();              // the whole progress record, kept in memory
var QUIZ = null, TICK = null, LAST = null;

function $(id){ return document.getElementById(id); }
function el(t, c, x){
  var n = document.createElement(t);
  if (c) n.className = c;
  if (x !== undefined && x !== null) n.textContent = x;
  return n;
}
function pct(x){ return (x === null || x === undefined) ? '--' : Math.round(x*100)+'%'; }
function band(p){ return (p===null||p===undefined) ? '' : (p<0.6?'low':(p<0.8?'mid':'high')); }
function mmss(s){ s = Math.max(0, Math.round(s)); return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2); }
function tagFor(portion){
  var cls = portion === 'georgia' ? ' ga' : (portion === 'comprehensive' ? ' comp' : '');
  var txt = portion === 'georgia' ? 'GA' : (portion === 'comprehensive' ? 'COMP' : 'NAT');
  return el('span', 'tag' + cls, txt);
}
function persist(){ save(D); }

/* -------------------------------------------------------------- routing */
var VIEWS = ['today','dash','study','cards','vocab','home','math','notebook','weak','quiz','result','plan','setup'];
var VQ = null;
var VOCAB_LOG_OPEN_ONLY = true;
var NB_OPEN_ONLY = true;
var STUDY_TOPIC = null;
function show(v){
  VIEWS.forEach(function(x){ var n = $('view-'+x); if (n) n.hidden = (x !== v); });
  document.querySelectorAll('#rail button').forEach(function(b){
    var on = b.dataset.view === v;
    b.classList.toggle('on', on);
    b.setAttribute('aria-current', on ? 'page' : 'false');
  });
  if (v === 'home') renderHome();
  if (v === 'today') renderToday();
  if (v === 'cards') renderCards();
  if (v === 'vocab') renderVocab();
  if (v === 'study') renderStudy();
  if (v === 'notebook') renderNotebook();
  if (v === 'math') renderMath();
  if (v === 'weak') renderWeak();
  if (v === 'dash') renderDash();
  if (v === 'plan') renderPlan();
  if (v === 'setup') renderSetup();
  window.scrollTo(0,0);
}
document.querySelectorAll('#rail button').forEach(function(b){
  b.onclick = function(){
    if (QUIZ && !confirm('Leave this quiz? It will not be scored.')) return;
    if (QUIZ){ stopTimer(); QUIZ = null; }
    show(b.dataset.view);
  };
});

function ro(key, value, note, hero){
  var d = el('div', 'ro' + (hero ? ' hero' : ''));
  d.appendChild(el('div', 'k', key));
  var v = el('div', 'v', value);
  if (note){
    var s2 = el('small', null, '\u00b7 ' + note);
    v.appendChild(s2);
  }
  d.appendChild(v);
  return d;
}

/* The status strip in the header: the five numbers worth seeing on every screen. */
function countdown(){
  var box = $('readouts');
  if (!box) return;
  box.innerHTML = '';
  var h = headline(D), st = portionStats(D);
  var hero = ro('Readiness', h.exam_pct === null ? '\u2014' : pct(h.exam_pct),
                h.exam_pct === null ? 'no data' : (h.passing ? 'passing' : 'need 75%'), true);
  if (h.exam_pct !== null)
    hero.querySelector('.v').className = 'v ' + (h.passing ? 'good' : 'bad');
  box.appendChild(hero);
  box.appendChild(ro('National',
                     (st.national && st.national.recent_pct != null)
                       ? pct(st.national.recent_pct) : '\u2014', '80 q'));
  box.appendChild(ro('Georgia',
                     (st.georgia && st.georgia.recent_pct != null)
                       ? pct(st.georgia.recent_pct) : '\u2014', '52 q'));
  box.appendChild(ro('Answered', String(h.answered),
                     h.sets + (h.sets === 1 ? ' set' : ' sets')));
  box.appendChild(ro('Days out', h.days_out === null ? '\u2014' : String(h.days_out),
                     h.days_out === null ? 'set a date' : 'until exam'));
}

/* ----------------------------------------------------------------- home */
function renderHome(){
  var v = $('view-home');
  v.innerHTML =
    '<h1>Practice quiz</h1>' +
    '<p class="sub">Pick a portion, choose how many questions, and go. Every question is ' +
    'explained the moment you answer it.</p>' +
    '<div class="card"><div class="row">' +
      '<div><label for="portion">Portion</label><select id="portion">' +
        '<option value="national">National (80 of 132 exam questions)</option>' +
        '<option value="georgia">Georgia state (52 of 132)</option>' +
        '<option value="mixed">Mixed, exam-weighted</option>' +
        '<option value="comprehensive">Comprehensive subtest (drill)</option></select></div>' +
      '<div><label for="topic">Topic</label><select id="topic"></select></div>' +
      '<div style="max-width:118px"><label for="count">Questions</label><select id="count">' +
        '<option>10</option><option selected>20</option><option>30</option><option>50</option>' +
      '</select></div>' +
    '</div><div class="row" style="margin-top:14px">' +
      '<div style="max-width:215px"><label for="timed">Timer</label><select id="timed">' +
        '<option value="1" selected>Timed (75 s/question)</option>' +
        '<option value="0">Untimed</option></select></div>' +
      '<div style="max-width:225px"><label for="difficulty">Difficulty</label><select id="difficulty">' +
        '<option value="harder" selected>Harder mix (default)</option>' +
        '<option value="exam">Exam realistic only</option>' +
        '<option value="hard">Hard + exam</option>' +
        '<option value="any">Full bank</option>' +
        '<option value="core">Core only</option></select></div>' +
      '<div style="flex:0 0 auto"><button class="btn" id="start">Start quiz</button></div>' +
      '<div style="flex:0 0 auto"><button class="btn ghost" id="startWeak">Weak-spot quiz</button></div>' +
      '<div style="flex:0 0 auto"><button class="btn ghost" id="startExam">Full mock exam (132)</button></div>' +
    '</div>' +
    '<p class="muted" style="margin:13px 0 0"><b>Weak-spot mode</b> draws more heavily from ' +
    'topics and individual questions you have missed before. <b>Harder mix</b> pulls about ' +
    'two thirds of its questions from the hard and exam-realistic tiers; ' +
    '<b>Exam realistic</b> is the hardest set, written at PSI difficulty. <b>Comprehensive</b> is a cross-cutting ' +
    'drill (vocabulary, judgment calls, GREC detail, closing math) rather than a section of ' +
    'the real exam.</p></div>' +
    '<div id="homeWeak"></div>';

  fillTopics();
  $('portion').onchange = fillTopics;
  $('start').onclick = function(){
    startQuiz({portion:$('portion').value, count:+$('count').value,
               topic:$('topic').value||null, timed:$('timed').value==='1',
               difficulty:$('difficulty').value});
  };
  $('startWeak').onclick = function(){
    startQuiz({portion:$('portion').value, count:+$('count').value,
               weak_spot:true, timed:$('timed').value==='1',
               difficulty:$('difficulty').value});
  };
  $('startExam').onclick = function(){
    if (!confirm('Full mock exam: 132 questions, about 2 h 45 m. Start?')) return;
    startQuiz({mode:'exam', timed:true, difficulty:$('difficulty').value});
  };
  renderHomeWeak();
}

function fillTopics(){
  var sel = $('topic'), p = $('portion').value;
  sel.innerHTML = '<option value="">All topics (exam-weighted)</option>';
  DATA.topics.forEach(function(t){
    if (p !== 'mixed' && t.portion !== p) return;
    var o = el('option', null, t.label+'  ('+t.exam_questions+' on exam)');
    o.value = t.key; sel.appendChild(o);
  });
}

function renderHomeWeak(){
  var box = $('homeWeak'); box.innerHTML = '';
  var rows = topicReport(D).filter(function(t){ return t.seen > 0; });
  var card = el('div','card');
  if (!rows.length){
    card.appendChild(el('div','empty',
      'No attempts yet. Take a 20-question quiz and this fills in with your weakest topics.'));
    box.appendChild(card); return;
  }
  card.appendChild(el('h2', null, 'Where you stand'));
  var wrap = el('div','scroll'), t = el('table');
  t.innerHTML = '<tr><th>Topic</th><th></th><th class="num">Score</th><th class="num">Qs</th></tr>';
  rows.slice(0,8).forEach(function(r){
    var tr = el('tr'), td = el('td');
    td.appendChild(document.createTextNode(r.label+' '));
    td.appendChild(tagFor(r.portion));
    var td2 = el('td'), track = el('div','bar-track'), fill = el('div','bar-fill '+band(r.pct));
    fill.style.width = Math.round((r.pct||0)*100)+'%';
    track.appendChild(fill); td2.appendChild(track);
    tr.appendChild(td); tr.appendChild(td2);
    tr.appendChild(el('td','num',pct(r.pct)));
    tr.appendChild(el('td','num',String(r.seen)));
    t.appendChild(tr);
  });
  wrap.appendChild(t); card.appendChild(wrap); box.appendChild(card);
}

/* ----------------------------------------------------------------- math */
function renderMath(){
  var v = $('view-math');
  var opts = Object.keys(DATA.math).map(function(k){
    return '<option value="'+k+'">'+DATA.math[k].label+'</option>';
  }).join('');
  v.innerHTML =
    '<h1>Real estate math</h1>' +
    '<p class="sub">Worked solutions after every answer. Each problem type has 70 ' +
    'variants with different numbers, so you learn the method rather than the answer.</p>' +
    '<div class="card"><div class="row">' +
      '<div><label for="mathTopic">Problem type</label><select id="mathTopic">' +
        '<option value="">All types (mixed)</option>'+opts+'</select></div>' +
      '<div style="max-width:118px"><label for="mathCount">Problems</label><select id="mathCount">' +
        '<option>5</option><option selected>10</option><option>15</option><option>25</option>' +
      '</select></div>' +
      '<div style="flex:0 0 auto"><button class="btn" id="startMath">Start math practice</button></div>' +
      '<div style="flex:0 0 auto"><button class="btn ghost" id="startMathWeak">Weak math types</button></div>' +
    '</div></div><div id="mathStats"></div>';
  $('startMath').onclick = function(){
    startQuiz({portion:'math', count:+$('mathCount').value,
               topic:$('mathTopic').value||null, timed:false});
  };
  $('startMathWeak').onclick = function(){
    startQuiz({portion:'math', count:+$('mathCount').value, weak_spot:true, timed:false});
  };
  var box = $('mathStats'), card = el('div','card');
  card.appendChild(el('h2',null,'Your math history'));
  var rows = generatorReport(D).filter(function(g){ return g.seen; });
  if (!rows.length) card.appendChild(el('div','empty','No math attempts yet -- start a set above.'));
  else {
    var wrap = el('div','scroll'), t = el('table');
    t.innerHTML = '<tr><th>Type</th><th class="num">Score</th><th>Concept</th></tr>';
    rows.forEach(function(g){
      var tr = el('tr');
      tr.appendChild(el('td',null,g.label));
      tr.appendChild(el('td','num',pct(g.pct)));
      tr.appendChild(el('td','muted',g.concept));
      t.appendChild(tr);
    });
    wrap.appendChild(t); card.appendChild(wrap);
  }
  box.appendChild(card);
}

/* ----------------------------------------------------------------- quiz */
function startQuiz(opts){
  var qs = (opts.mode === 'exam') ? mockExam(opts.difficulty)
         : select(opts.portion, opts.count, {weak_spot:opts.weak_spot,
                                             topic:opts.topic, sub:opts.sub,
                                             progress:D,
                                             difficulty:opts.difficulty});
  if (!qs.length){ alert('No questions matched that selection.'); return; }
  startQuizWith(qs, opts);
}

function startQuizWith(qs, opts){
  LAST = opts;
  QUIZ = {qs:qs, i:0, correct:0, answers:new Array(qs.length),
          portion: (opts.mode === 'exam') ? 'mixed' : opts.portion,
          mode: opts.mode || (opts.topic ? 'topic' : 'quiz'),
          dayTask: opts.dayTask || null,
          weak: !!opts.weak_spot, locked:false,
          limit: opts.timed === false ? 0 : qs.length*DATA.spq,
          started: Date.now(), qStart: Date.now()};
  $('view-quiz').innerHTML =
    '<div class="progressbar"><div id="qprog" style="width:0"></div></div>' +
    '<div class="qhead"><div><span class="tag" id="qtag"></span> ' +
      '<span class="tag hard" id="qhard" hidden>Hard</span> ' +
      '<span class="muted" id="qcount"></span></div>' +
      '<div class="timer" id="qtimer"></div></div>' +
    '<div class="card"><div class="eyebrow" id="qtopic"></div>' +
      '<div class="qtext" id="qtext"></div><div class="choices" id="qchoices"></div>' +
      '<div id="qfeedback"></div></div>' +
    '<div class="row"><div style="flex:0 0 auto">' +
      '<button class="btn" id="qnext" disabled>Next</button></div>' +
      '<div style="flex:0 0 auto"><button class="btn ghost" id="qquit">End &amp; score</button></div></div>';
  $('qnext').onclick = function(){
    if (QUIZ.i >= QUIZ.qs.length-1) return finish();
    QUIZ.i++; renderQuestion();
  };
  $('qquit').onclick = function(){
    if (confirm('End the quiz now and score what you have answered?')) finish();
  };
  show('quiz'); startTimer(); renderQuestion();
}

function startTimer(){
  stopTimer();
  if (!QUIZ.limit){ $('qtimer').textContent = ''; return; }
  TICK = setInterval(function(){
    if (!QUIZ) return stopTimer();
    var left = QUIZ.limit - (Date.now()-QUIZ.started)/1000;
    $('qtimer').textContent = mmss(left);
    $('qtimer').classList.toggle('warn', left < 120);
    if (left <= 0){ stopTimer(); alert('Time is up. Scoring what you have.'); finish(); }
  }, 500);
}
function stopTimer(){ if (TICK){ clearInterval(TICK); TICK = null; } }

function renderQuestion(){
  var q = QUIZ.qs[QUIZ.i];
  QUIZ.locked = false; QUIZ.qStart = Date.now();
  $('qprog').style.width = (QUIZ.i/QUIZ.qs.length*100)+'%';
  $('qcount').textContent = 'Question '+(QUIZ.i+1)+' of '+QUIZ.qs.length;
  var ga = q.portion === 'georgia', comp = q.portion === 'comprehensive';
  $('qtag').textContent = comp ? 'Comprehensive'
                        : (q.generator ? 'Math' : (ga ? 'Georgia' : 'National'));
  $('qtag').className = 'tag' + (ga ? ' ga' : (comp ? ' comp' : ''));
  var tier = q.difficulty || 1;
  $('qhard').hidden = (tier < 2);
  $('qhard').textContent = (tier === 3) ? 'Exam' : 'Hard';
  $('qhard').className = 'tag hard' + (tier === 3 ? ' exam' : '');
  $('qtopic').textContent = label(q.topic);
  $('qtext').textContent = q.q;
  $('qfeedback').innerHTML = '';
  $('qnext').disabled = true;
  $('qnext').textContent = (QUIZ.i === QUIZ.qs.length-1) ? 'Finish' : 'Next';
  var box = $('qchoices'); box.innerHTML = '';
  q.choices.forEach(function(text, k){
    var b = el('button','choice');
    b.appendChild(el('span','k','ABCD'[k]));
    b.appendChild(el('span', null, text));
    b.onclick = function(){ answer(k); };
    box.appendChild(b);
  });
}

function answer(choice){
  if (QUIZ.locked) return;
  QUIZ.locked = true;
  var q = QUIZ.qs[QUIZ.i], correct = (choice === q.answer);
  if (correct) QUIZ.correct++;
  QUIZ.answers[QUIZ.i] = {qid:q.id, topic:q.topic, sub:q.sub||null,
                          generator:q.generator||null,
                          choice:choice, correct:correct, q:q,
                          seconds:(Date.now()-QUIZ.qStart)/1000};
  var btns = $('qchoices').children;
  for (var k = 0; k < btns.length; k++){
    btns[k].disabled = true;
    if (k === q.answer) btns[k].classList.add('correct');
    else if (k === choice) btns[k].classList.add('wrong');
  }
  var fb = el('div','feedback '+(correct?'ok':'no'));
  fb.appendChild(el('div','verdict', correct ? 'Correct' : 'Not quite'));
  if (!correct)
    fb.appendChild(el('div', null, 'Correct answer: '+'ABCD'[q.answer]+'. '+q.choices[q.answer]));
  if (q.steps && q.steps.length){
    var ol = el('ol','steps');
    q.steps.forEach(function(s){ ol.appendChild(el('li', null, s)); });
    fb.appendChild(ol);
  } else if (q.explain){
    fb.appendChild(el('div', null, q.explain));
  }
  if (q.concept){
    var c = el('div','concept');
    c.appendChild(el('b', null, 'Concept tested: '));
    c.appendChild(document.createTextNode(q.concept));
    fb.appendChild(c);
  }
  $('qfeedback').appendChild(fb);
  $('qnext').disabled = false;
  $('qnext').focus();
}

document.addEventListener('keydown', function(e){
  if (VQ && !$('view-vocab').hidden){
    var vk = 'abcd'.indexOf((e.key || '').toLowerCase());
    if (vk >= 0 && !VQ.locked){ answerVocab(vk, $('view-vocab')); return; }
    var vn = $('vnext');
    if ((e.key === 'Enter' || e.key === ' ') && vn && !vn.disabled){
      e.preventDefault(); vn.click(); return;
    }
  }
  if (!QUIZ || $('view-quiz').hidden) return;
  var k = 'abcd'.indexOf((e.key||'').toLowerCase());
  if (k >= 0 && k < QUIZ.qs[QUIZ.i].choices.length && !QUIZ.locked){ answer(k); return; }
  if ((e.key === 'Enter' || e.key === ' ') && !$('qnext').disabled){
    e.preventDefault(); $('qnext').click();
  }
});

function finish(){
  stopTimer();
  var q = QUIZ; QUIZ = null;
  var answers = [];
  q.answers.forEach(function(a){ if (a) answers.push(a); });
  q.answers.forEach(function(a, i){
    if (!a){
      var x = q.qs[i];
      answers.push({qid:x.id, topic:x.topic, sub:x.sub||null,
                    generator:x.generator||null,
                    choice:null, correct:false, q:x, seconds:0});
    }
  });
  var att = recordAttempt(D, q.portion, q.mode, answers,
                          (Date.now()-q.started)/1000, q.weak);
  if (q.dayTask) markDone(D, q.dayTask);
  persist(); countdown();
  renderResult(att); show('result');
}

function renderResult(a){
  var v = $('view-result');
  v.innerHTML = '<h1>Results</h1><div id="resultBody"></div>' +
    '<div class="row" style="margin-top:10px">' +
    '<div style="flex:0 0 auto"><button class="btn" id="againSame">Another quiz</button></div>' +
    '<div style="flex:0 0 auto"><button class="btn ghost" id="againWeak">Drill my weak spots</button></div>' +
    '<div style="flex:0 0 auto"><button class="btn ghost" id="toDash">See dashboard</button></div></div>';
  if (a.correct < a.count){
    var nb = el('div', 'card');
    nb.appendChild(cardHead('Review what you missed', 'notebook'));
    nb.appendChild(el('p', 'muted',
      (a.count - a.correct) + ' question' + ((a.count - a.correct) === 1 ? '' : 's') +
      ' from this quiz went to your notebook, with the correct answer and why.'));
    var row = el('div', 'row');
    var d0 = el('div'); d0.style.flex = '0 0 auto';
    var b0 = el('button', 'btn', 'Open notebook');
    b0.onclick = function(){ NB_OPEN_ONLY = true; show('notebook'); };
    d0.appendChild(b0); row.appendChild(d0);
    nb.appendChild(row);
    box.appendChild(nb);
  }

  $('againSame').onclick = function(){ startQuiz(LAST || {portion:'national', count:20}); };
  $('againWeak').onclick = function(){
    startQuiz({portion:(LAST&&LAST.portion==='math')?'national':((LAST&&LAST.portion)||'national'),
               count:20, weak_spot:true, timed:true});
  };
  $('toDash').onclick = function(){ show('dash'); };

  var box = $('resultBody'), head = el('div','card'), g = el('div','grid g3');
  [['Score',pct(a.pct)],['Correct',a.correct+' of '+a.count],['Time',mmss(a.seconds)]]
    .forEach(function(p){
      var d = el('div');
      d.appendChild(el('div','muted',p[0]));
      d.appendChild(el('div','stat',p[1]));
      g.appendChild(d);
    });
  head.appendChild(g);
  head.appendChild(el('p','muted', a.pct >= 0.75
    ? 'At or above 75% -- that is roughly the zone you want to be in before exam day.'
    : 'Georgia requires 75% to pass. Keep drilling the topics below.'));
  box.appendChild(head);

  var keys = Object.keys(a.topics||{});
  if (keys.length){
    var card = el('div','card');
    card.appendChild(el('h2',null,'This attempt, by topic'));
    var wrap = el('div','scroll'), t = el('table');
    t.innerHTML = '<tr><th>Topic</th><th class="num">Correct</th><th class="num">Score</th></tr>';
    keys.map(function(k){ var v2 = a.topics[k]; return {k:k, v:v2, p:v2.correct/v2.seen}; })
        .sort(function(x,y){ return x.p - y.p; })
        .forEach(function(r){
          var tr = el('tr');
          tr.appendChild(el('td',null,label(r.k)));
          tr.appendChild(el('td','num',r.v.correct+'/'+r.v.seen));
          tr.appendChild(el('td','num',pct(r.p)));
          t.appendChild(tr);
        });
    wrap.appendChild(t); card.appendChild(wrap); box.appendChild(card);
  }
}

/* ---------------------------------------------------------------- today */
function taskAction(t, plan){
  if (t.key === 'vocab'){
    if (!t.meta) return null;
    return function(){
      startVocab({topic: t.meta.topic, count: 15, dayTask: 'vocab'});
    };
  }
  if (t.key === 'read'){
    return function(){
      markDone(D, 'read'); persist();
      STUDY_TOPIC = t.meta ? t.meta.topic : null;
      show('study');
    };
  }
  if (t.key === 'notebook'){
    return t.count ? function(){ startNotebookRetry(); } : null;
  }
  if (t.key === 'topic'){
    return function(){
      if (t.meta){
        startQuiz({portion: t.meta.portion, count: 15, topic: t.meta.topic,
                   timed: false, difficulty: 'harder', dayTask: 'topic'});
      } else {
        startQuiz({portion: 'mixed', count: 15, weak_spot: true, timed: true,
                   difficulty: 'harder', dayTask: 'topic'});
      }
    };
  }
  if (t.key === 'math'){
    return function(){
      startQuiz({portion: 'math', count: 10, weak_spot: true, timed: false,
                 dayTask: 'math'});
    };
  }
  return null;
}

function renderToday(){
  var v = $('view-today');
  v.className = '';
  v.innerHTML = '<div id="todayBody"></div>';
  var box = $('todayBody');
  var plan = todayPlan(D);
  var r = readiness(D);

  /* ---- the header: where you stand, and what is next ---- */
  var head = el('div', 'card');
  head.appendChild(cardHead('Today', plan.date +
    (plan.streak > 1 ? '  ·  ' + plan.streak + '-day streak' : '')));

  var bar = el('div', 'progressbar');
  var fill = el('div');
  fill.style.width = (plan.doneCount / plan.total * 100) + '%';
  bar.appendChild(fill);
  head.appendChild(bar);

  var g = el('div', 'grid g3');
  var d1 = el('div', 'metric');
  d1.appendChild(el('div', 'eyebrow', 'Today'));
  var ring = el('div', 'ring');
  ring.appendChild(el('span', 'big', String(plan.doneCount)));
  ring.appendChild(el('span', 'of', 'of ' + plan.total + ' done'));
  d1.appendChild(ring);
  g.appendChild(d1);

  function portionMetric(label, pr){
    var d = el('div', 'metric');
    d.appendChild(el('div', 'eyebrow', label));
    d.appendChild(el('div', 'stat' + (pr.current === null ? ''
      : (pr.current >= 0.75 ? ' good' : ' bad')),
      pr.current === null ? '—' : pct(pr.current)));
    d.appendChild(el('div', 'muted', pr.current === null ? 'no data yet'
      : (pr.current >= 0.75 ? 'clearing 75%' : 'below 75%')));
    return d;
  }
  g.appendChild(portionMetric('National', r.national));
  g.appendChild(portionMetric('Georgia', r.georgia));
  head.appendChild(g);

  if (r.national.current !== null && r.georgia.current !== null &&
      (r.national.current < 0.75) !== (r.georgia.current < 0.75)){
    var warn = el('div', 'callout trap');
    warn.style.cssText = 'font-family:"Barlow",sans-serif;font-size:.92rem;line-height:1.55';
    warn.textContent = 'The two portions are scored separately and you must clear 75% ' +
      'on each. Your ' + (r.blocker === 'georgia' ? 'Georgia' : 'National') +
      ' portion is below the mark, so a healthy average does not mean a pass.';
    head.appendChild(warn);
  }

  if (plan.allDone){
    var d = el('div', 'callout');
    d.style.cssText = 'border-left-color:var(--ok);font-family:"Barlow",sans-serif;' +
      'font-size:.95rem;line-height:1.55';
    d.textContent = 'Everything for today is done. Anything further is a bonus — ' +
      'the Practice and Vocab tabs are open.';
    head.appendChild(d);
  } else {
    var nextTask = plan.tasks.filter(function(t){ return t.key === plan.nextKey; })[0];
    if (nextTask){
      var go = el('div', 'row');
      var gd = el('div'); gd.style.flex = '0 0 auto';
      var gb = el('button', 'btn', 'Start next: ' + nextTask.name.toLowerCase());
      var fn = taskAction(nextTask, plan);
      gb.onclick = fn;
      gd.appendChild(gb); go.appendChild(gd);
      head.appendChild(go);
    }
  }
  box.appendChild(head);

  /* ---- the queue ---- */
  var work = el('div', 'card');
  work.appendChild(cardHead('Your five', 'finish one and the next opens'));
  var list = el('div', 'tasklist');
  plan.tasks.forEach(function(t){
    var isNext = (t.key === plan.nextKey);
    var row = el('div', 'task' + (t.done ? ' done' : (isNext ? ' next' : '')));
    var w = el('div', 'tw');
    var nm = el('div', 'tn', t.name);
    if (isNext && !t.done) nm.appendChild(el('span', 'tag', 'next'));
    w.appendChild(nm);
    w.appendChild(el('div', 'td', t.desc));
    if (t.key === 'vocab' && t.meta){
      var pbar = el('div', 'bar-track');
      pbar.style.marginTop = '.4rem';
      var pf = el('div', 'bar-fill ' + band(t.meta.pct));
      pf.style.width = Math.round(t.meta.pct * 100) + '%';
      pbar.appendChild(pf);
      w.appendChild(pbar);
    }
    row.appendChild(w);
    if (t.done){
      row.appendChild(el('span', 'tick', '✓'));
    } else if (t.count > 0){
      var b = el('button', 'btn' + (isNext ? '' : ' ghost'), 'Start');
      b.onclick = taskAction(t, plan);
      row.appendChild(b);
    } else {
      row.appendChild(el('span', 'muted', 'nothing due'));
    }
    list.appendChild(row);
  });
  work.appendChild(list);
  box.appendChild(work);

  /* ---- vocabulary progress across all categories ---- */
  var vp = vocabProgress(D);
  var passed = vp.filter(function(x){ return x.passed; }).length;
  var vc = el('div', 'card');
  vc.appendChild(cardHead('Definitions by category',
    passed + ' of ' + vp.length + ' categories passed'));
  vc.appendChild(el('p', 'muted',
    'A category passes at 90% of its terms known — meaning you have got each one ' +
    'right twice. Today serves the next unpassed category, heaviest on the exam first.'));
  var wrap = el('div', 'scroll'), t2 = el('table', 'stats');
  t2.innerHTML = '<tr><th>Category</th><th class="num">Known</th>' +
                 '<th></th><th class="num">On exam</th><th></th></tr>';
  vp.forEach(function(x){
    var nm = el('td');
    nm.appendChild(document.createTextNode(x.label + ' '));
    nm.appendChild(tagFor(x.portion));
    if (x.passed) nm.appendChild(el('span', 'tag', 'passed'));
    var td = el('td');
    var track = el('div', 'bar-track');
    var f2 = el('div', 'bar-fill ' + (x.passed ? 'high' : band(x.pct)));
    f2.style.width = Math.round(x.pct * 100) + '%';
    track.appendChild(f2); td.appendChild(track);
    var act = el('td');
    var ab = el('button', 'btn mini' + (x.passed ? ' ghost' : ''),
                x.passed ? 'REVIEW' : 'LEARN');
    ab.onclick = (function(topic){
      return function(){ startVocab({topic: topic, count: 15}); };
    })(x.topic);
    act.appendChild(ab);
    t2.appendChild(statRow([
      nm,
      el('td', 'num', x.known + '/' + x.total),
      td,
      el('td', 'num', countsOnExam(x.topic) ? String(x.weight) : 'drill'),
      act
    ]));
  });
  wrap.appendChild(t2); vc.appendChild(wrap);
  box.appendChild(vc);
  window.scrollTo(0, 0);
}

function startNotebookRetry(){
  var due = notebookDue(D);
  if (!due.length){ show('notebook'); return; }
  var pool = [];
  var index = {};
  ['national', 'georgia', 'comprehensive'].forEach(function(p){
    (DATA.banks[p] || []).forEach(function(r){ index[r.id] = r; });
  });
  due.forEach(function(m){ if (index[m.qid]) pool.push(index[m.qid]); });
  if (!pool.length){ show('notebook'); return; }
  startQuizWith(shuffle(pool).slice(0, 20), {
    portion: 'mixed', mode: 'notebook', timed: false, dayTask: 'notebook'
  });
}

/* ---------------------------------------------------------------- cards */
var CARD_OPTS = {mode: 'due', limit: 25};
var CARD_FROM_TODAY = false;
var DECK = null;

function renderCards(){
  var v = $('view-cards');
  v.className = '';
  if (DECK && DECK.i < DECK.list.length) return renderCard(v);
  v.innerHTML = '<div id="cardsBody"></div>';
  var box = $('cardsBody');
  var cc = cardCounts(D);

  if (DECK && DECK.i >= DECK.list.length){
    var done = el('div', 'card');
    done.appendChild(cardHead('Deck finished', DECK.right + ' of ' + DECK.list.length + ' known'));
    done.appendChild(el('p', 'muted',
      'Cards you knew move up the ladder and come back later. Cards you missed ' +
      'come back today.'));
    var again = el('div', 'row');
    var d0 = el('div'); d0.style.flex = '0 0 auto';
    var b0 = el('button', 'btn', 'Another set');
    b0.onclick = function(){ DECK = null; startDeck(CARD_OPTS); };
    d0.appendChild(b0); again.appendChild(d0);
    if (CARD_FROM_TODAY){
      var d1 = el('div'); d1.style.flex = '0 0 auto';
      var b1 = el('button', 'btn ghost', 'Back to today');
      b1.onclick = function(){ DECK = null; CARD_FROM_TODAY = false; show('today'); };
      d1.appendChild(b1); again.appendChild(d1);
    }
    done.appendChild(again);
    box.appendChild(done);
    DECK = null;
  }

  var head = el('div', 'card');
  head.appendChild(cardHead('Vocabulary cards', cc.total + ' terms'));
  head.appendChild(el('p', 'sub',
    'Every term from the study notes, drilled by recall rather than reading. ' +
    'Say the meaning out loud, flip, and mark yourself honestly — cards you miss ' +
    'come back sooner.'));
  var g = el('div', 'grid g3');
  [['Due now', cc.due], ['Learned', cc.learned], ['Not seen yet', cc.unseen]]
    .forEach(function(p){
      var d = el('div', 'metric');
      d.appendChild(el('div', 'eyebrow', p[0]));
      d.appendChild(el('div', 'stat', String(p[1])));
      g.appendChild(d);
    });
  head.appendChild(g);
  var row = el('div', 'row');
  [['Due now (25)', {mode: 'due', limit: 25}],
   ['Ones I keep missing', {mode: 'weak', limit: 20}],
   ['New terms (20)', {mode: 'new', limit: 20}]].forEach(function(o, i){
    var d = el('div'); d.style.flex = '0 0 auto';
    var b = el('button', 'btn' + (i ? ' ghost' : ''), o[0]);
    b.onclick = function(){ CARD_FROM_TODAY = false; startDeck(o[1]); };
    d.appendChild(b); row.appendChild(d);
  });
  head.appendChild(row);
  box.appendChild(head);

  var pick = el('div', 'card');
  pick.appendChild(cardHead('By topic', 'pick a deck'));
  var list = el('div', 'topiclist');
  Object.keys(DATA.study.topics).forEach(function(tk){
    var t = DATA.study.topics[tk];
    var mine = cards().filter(function(c){ return c.topic === tk; });
    var due = mine.filter(function(c){
      var r = D.srs[c.id]; return !r || (r.due || 0) <= Date.now() / 1000;
    }).length;
    var rowx = el('div', 'topicrow'), who = el('div', 'who');
    who.appendChild(el('div', 'nm', t.label));
    who.appendChild(el('div', 'bl', mine.length + ' terms · ' + due + ' due'));
    rowx.appendChild(who);
    var acts = el('div', 'acts');
    var b = el('button', 'btn mini', 'DRILL');
    b.onclick = function(){
      CARD_FROM_TODAY = false; startDeck({topic: tk, mode: 'all', limit: 30});
    };
    acts.appendChild(b);
    rowx.appendChild(acts);
    list.appendChild(rowx);
  });
  pick.appendChild(list);
  box.appendChild(pick);
  window.scrollTo(0, 0);
}

function startDeck(opts){
  CARD_OPTS = opts;
  var list = cardDeck(D, opts);
  if (!list.length){
    alert('No cards match that right now — try "New terms" or a topic deck.');
    return;
  }
  DECK = {list: list, i: 0, right: 0, shown: false};
  show('cards');
}

function renderCard(v){
  var c = DECK.list[DECK.i];
  var st = cardState(D, c);
  v.innerHTML = '<div id="cardsBody"></div>';
  var box = $('cardsBody');
  var card = el('div', 'card');

  var meta = el('div', 'cardmeta');
  meta.appendChild(el('span', null, c.topic_label));
  var right = el('span', null, (DECK.i + 1) + ' / ' + DECK.list.length);
  meta.appendChild(right);
  card.appendChild(meta);

  var stage = el('div', 'cardstage');
  var flip = el('div', 'flip');
  if (!DECK.shown){
    flip.appendChild(el('div', 'side', 'Term'));
    flip.appendChild(el('div', 'term', c.term));
    flip.appendChild(el('div', 'hintline', 'Say the meaning, then tap to check'));
    flip.onclick = function(){ DECK.shown = true; renderCard(v); };
  } else {
    flip.appendChild(el('div', 'side', c.term));
    flip.appendChild(el('div', 'def', c.def));
    flip.style.cursor = 'default';
  }
  stage.appendChild(flip);

  var acts = el('div', 'cardacts');
  if (!DECK.shown){
    var show1 = el('button', 'btn', 'Show the meaning');
    show1.onclick = function(){ DECK.shown = true; renderCard(v); };
    acts.appendChild(show1);
  } else {
    var no = el('button', 'btn ghost', 'Didn’t know it');
    no.onclick = function(){ gradeCard(c, false, v); };
    var yes = el('button', 'btn', 'Knew it');
    yes.onclick = function(){ gradeCard(c, true, v); };
    acts.appendChild(no); acts.appendChild(yes);
  }
  stage.appendChild(acts);

  var bar = el('div', 'cardmeta');
  var boxes = el('div', 'boxbar');
  for (var i = 1; i <= 5; i++){
    boxes.appendChild(el('i', (st.box >= i ? 'on' : '')));
  }
  var lab = el('span', null, st.seen ? ('box ' + st.box + ' of 5') : 'new card');
  bar.appendChild(lab);
  bar.appendChild(boxes);
  stage.appendChild(bar);

  card.appendChild(stage);
  box.appendChild(card);

  var out = el('div', 'card');
  var orow = el('div', 'row');
  var od = el('div'); od.style.flex = '0 0 auto';
  var ob = el('button', 'btn ghost', 'End deck');
  ob.onclick = function(){ DECK.i = DECK.list.length; renderCards(); };
  od.appendChild(ob); orow.appendChild(od);
  var sd = el('div'); sd.style.flex = '0 0 auto';
  var sb = el('button', 'btn ghost', 'Read this topic');
  sb.onclick = function(){ DECK = null; STUDY_TOPIC = c.topic; show('study'); };
  sd.appendChild(sb); orow.appendChild(sd);
  out.appendChild(orow);
  box.appendChild(out);
  window.scrollTo(0, 0);
}

function gradeCard(c, knew, v){
  srsGrade(D, c.id, knew);
  if (knew) DECK.right++;
  persist();
  DECK.i++; DECK.shown = false;
  if (DECK.i >= DECK.list.length){
    if (CARD_FROM_TODAY){ markDone(D, 'cards'); persist(); }
    renderCards();
  } else {
    renderCard(v);
  }
}

/* ---------------------------------------------------------- vocab quiz */
function renderVocab(){
  var v = $('view-vocab');
  v.className = '';
  if (VQ && VQ.i < VQ.list.length) return renderVocabQ(v);
  v.innerHTML = '<div id="vocabBody"></div>';
  var box = $('vocabBody');

  if (VQ && VQ.i >= VQ.list.length){
    if (VQ.opts.dayTask){ markDone(D, VQ.opts.dayTask); persist(); }
    var done = el('div', 'card');
    done.appendChild(cardHead('Set finished',
      VQ.right + ' of ' + VQ.list.length + ' correct'));
    if (VQ.opts.topic){
      var after = vocabProgress(D).filter(function(x){
        return x.topic === VQ.opts.topic; })[0];
      if (after){
        var line = el('div', 'callout');
        line.style.cssText = 'font-family:"Barlow",sans-serif;font-size:.95rem;' +
          'line-height:1.55;border-left-color:' + (after.passed ? 'var(--ok)' : 'var(--accent)');
        if (after.passed){
          var nxt = nextVocabCategory(D);
          line.textContent = after.label + ' passed — ' + after.known + ' of ' +
            after.total + ' terms known.' +
            (nxt ? ' Next up: ' + nxt.label + '.' : ' Every category is now passed.');
          if (nxt){
            var nb3 = el('button', 'btn mini');
            nb3.textContent = 'START ' + nxt.label.toUpperCase();
            nb3.style.marginTop = '.5rem';
            nb3.onclick = function(){ VQ = null; startVocab({topic: nxt.topic, count: 15}); };
            line.appendChild(document.createElement('br'));
            line.appendChild(nb3);
          }
        } else {
          line.textContent = after.label + ': ' + after.known + ' of ' + after.total +
            ' terms known (' + Math.round(after.pct * 100) + '%). Passes at 90%.';
        }
        done.appendChild(line);
      }
    }
    var missed = VQ.missed;
    if (missed.length){
      done.appendChild(el('p', 'muted', 'Terms you missed:'));
      var ml = el('div', 'callouts');
      missed.forEach(function(m){
        var d = el('div', 'callout trap');
        d.style.cssText = 'font-family:"Barlow",sans-serif;font-size:.95rem;line-height:1.55';
        d.appendChild(el('b', null, m.term));
        d.appendChild(document.createTextNode(' — ' + m.def));
        ml.appendChild(d);
      });
      done.appendChild(ml);
    } else {
      done.appendChild(el('p', 'muted', 'Clean sweep.'));
    }
    var again = el('div', 'row');
    var a1 = el('div'); a1.style.flex = '0 0 auto';
    var b1 = el('button', 'btn', 'Another set');
    b1.onclick = function(){ var o = VQ.opts; VQ = null; startVocab(o); };
    a1.appendChild(b1); again.appendChild(a1);
    if (missed.length){
      var a2 = el('div'); a2.style.flex = '0 0 auto';
      var b2 = el('button', 'btn ghost', 'Drill just the ones I missed');
      b2.onclick = function(){
        var o = {mode: 'weak', count: Math.max(5, missed.length),
                 topic: VQ.opts.topic, portion: VQ.opts.portion};
        VQ = null; startVocab(o);
      };
      a2.appendChild(b2); again.appendChild(a2);
    }
    done.appendChild(again);
    box.appendChild(done);
    VQ = null;
  }

  var head = el('div', 'card');
  head.appendChild(cardHead('Vocab', 'definition first — you pick the term'));
  head.appendChild(el('p', 'sub',
    'You are shown a definition and choose the term it belongs to, from four ' +
    'options drawn from the same topic. Pick a category below, or drill the whole ' +
    'bank. Recognising a term is easier than recalling it, so use the Cards tab too.'));
  var row = el('div', 'row');
  [['Everything (15)', {count: 15}],
   ['National only (15)', {portion: 'national', count: 15}],
   ['Georgia only (15)', {portion: 'georgia', count: 15}],
   ['Ones I keep missing', {mode: 'weak', count: 15}]].forEach(function(o, i){
    var d = el('div'); d.style.flex = '0 0 auto';
    var b = el('button', 'btn' + (i ? ' ghost' : ''), o[0]);
    b.onclick = function(){ startVocab(o[1]); };
    d.appendChild(b); row.appendChild(d);
  });
  head.appendChild(row);
  box.appendChild(head);

  var NAMES = {national: 'National portion', georgia: 'Georgia state portion',
               comprehensive: 'Comprehensive subtest'};
  var rows = vocabTopics(D);
  ['national', 'georgia', 'comprehensive'].forEach(function(portion){
    var mine = rows.filter(function(r){ return r.portion === portion; });
    if (!mine.length) return;
    var card = el('div', 'card');
    card.appendChild(cardHead(NAMES[portion], 'pick a category'));
    var grid = el('div', 'catgrid');
    mine.forEach(function(r){
      var b = el('button', 'cat');
      b.appendChild(el('span', 'cn', r.label));
      b.appendChild(el('span', 'cs',
        r.total + ' terms · ' + r.due + ' due · ' + r.learned + ' learned'));
      b.onclick = function(){
        startVocab({topic: r.topic, count: Math.min(20, r.total)});
      };
      grid.appendChild(b);
    });
    card.appendChild(grid);
    box.appendChild(card);
  });

  box.appendChild(vocabMissLog());
  window.scrollTo(0, 0);
}


function vocabMissLog(){
  var counts = vocabMissCounts(D);
  var card = el('div', 'card');
  card.appendChild(cardHead('Terms you have got wrong',
    counts.total ? (counts.open + ' still shaky · ' + counts.learned + ' learned since')
                 : 'nothing yet'));

  if (!counts.total){
    card.appendChild(el('div', 'empty',
      'Nothing here yet. Any definition you miss is logged automatically and stays ' +
      'until you have got it right twice.'));
    return card;
  }

  card.appendChild(el('p', 'muted',
    'A term leaves the shaky list once you have answered it correctly twice. ' +
    'Missing it again puts it straight back.'));

  var f = el('div', 'nbfilter');
  var ob = el('button', 'btn' + (VOCAB_LOG_OPEN_ONLY ? '' : ' ghost'),
              'Still shaky (' + counts.open + ')');
  ob.onclick = function(){ VOCAB_LOG_OPEN_ONLY = true; renderVocab(); };
  var ab = el('button', 'btn' + (VOCAB_LOG_OPEN_ONLY ? ' ghost' : ''),
              'All I have missed (' + counts.total + ')');
  ab.onclick = function(){ VOCAB_LOG_OPEN_ONLY = false; renderVocab(); };
  f.appendChild(ob); f.appendChild(ab);
  if (counts.open){
    var db = el('button', 'btn ghost', 'Drill these');
    db.onclick = function(){
      var ids = vocabMisses(D, {openOnly: true}).map(function(r){ return r.id; });
      startVocab({ids: ids, count: Math.min(20, ids.length)});
    };
    f.appendChild(db);
  }
  card.appendChild(f);

  var rows = vocabMisses(D, {openOnly: VOCAB_LOG_OPEN_ONLY});
  var wrap = el('div', 'scroll'), t = el('table', 'stats');
  t.innerHTML = '<tr><th>Term</th><th>Definition</th><th>Category</th>' +
                '<th class="num">Missed</th><th></th></tr>';
  rows.forEach(function(r){
    var term = el('td');
    term.appendChild(el('b', null, r.term));
    if (r.known) term.appendChild(el('span', 'tag', 'learned'));
    var cat = el('td');
    cat.appendChild(document.createTextNode(r.topic_label + ' '));
    cat.appendChild(tagFor(r.portion));
    var act = el('td');
    var b = el('button', 'btn mini', 'RETRY');
    b.onclick = (function(id){
      return function(){ startVocab({ids: [id], count: 1}); };
    })(r.id);
    act.appendChild(b);
    var def = el('td', null, r.def);
    def.style.cssText = 'white-space:normal;min-width:230px;max-width:40ch';
    t.appendChild(statRow([
      term, def, cat,
      el('td', 'num', r.wrong + '×'),
      act
    ]));
  });
  wrap.appendChild(t); card.appendChild(wrap);
  return card;
}

function startVocab(opts){
  var list = vocabQuestions(D, opts);
  if (list.length < 1){
    alert('That category needs at least four terms to build a multiple choice set.');
    return;
  }
  var before = opts.topic ? vocabProgress(D).filter(function(x){
    return x.topic === opts.topic; })[0] : null;
  VQ = {list: list, i: 0, right: 0, missed: [], locked: false, opts: opts,
        before: before};
  show('vocab');
}

function renderVocabQ(v){
  var q = VQ.list[VQ.i];
  v.innerHTML = '<div id="vocabBody"></div>';
  var box = $('vocabBody');

  var prog = el('div', 'progressbar');
  var bar = el('div');
  bar.style.width = (VQ.i / VQ.list.length * 100) + '%';
  prog.appendChild(bar);
  box.appendChild(prog);

  var card = el('div', 'card');
  var hd = el('div', 'cardmeta');
  var left = el('span');
  left.appendChild(document.createTextNode(q.topic_label + ' '));
  left.appendChild(tagFor(q.portion));
  hd.appendChild(left);
  hd.appendChild(el('span', null, (VQ.i + 1) + ' / ' + VQ.list.length +
    '  ·  ' + VQ.right + ' right'));
  card.appendChild(hd);

  var panel = el('div', 'defpanel');
  panel.appendChild(el('div', 'lab', 'Which term does this define?'));
  panel.appendChild(el('div', 'dtext', q.def));
  card.appendChild(panel);

  var opts = el('div', 'termopts');
  q.choices.forEach(function(text, i){
    var b = el('button', 'termopt');
    b.appendChild(el('span', 'k', 'ABCD'[i]));
    b.appendChild(el('span', null, text));
    b.onclick = function(){ answerVocab(i, v); };
    opts.appendChild(b);
  });
  card.appendChild(opts);

  var fb = el('div');
  fb.id = 'vfeedback';
  card.appendChild(fb);
  box.appendChild(card);

  var foot = el('div', 'card');
  var frow = el('div', 'row');
  var d1 = el('div'); d1.style.flex = '0 0 auto';
  var nx = el('button', 'btn', VQ.i === VQ.list.length - 1 ? 'Finish' : 'Next');
  nx.id = 'vnext';
  nx.disabled = true;
  nx.onclick = function(){ VQ.i++; VQ.locked = false; renderVocab(); };
  d1.appendChild(nx); frow.appendChild(d1);
  var d2 = el('div'); d2.style.flex = '0 0 auto';
  var en = el('button', 'btn ghost', 'End set');
  en.onclick = function(){ VQ.i = VQ.list.length; renderVocab(); };
  d2.appendChild(en); frow.appendChild(d2);
  var d3 = el('div'); d3.style.flex = '0 0 auto';
  var rd = el('button', 'btn ghost', 'Read this topic');
  rd.onclick = function(){ VQ = null; STUDY_TOPIC = q.topic; show('study'); };
  d3.appendChild(rd); frow.appendChild(d3);
  foot.appendChild(frow);
  box.appendChild(foot);
  window.scrollTo(0, 0);
}

function answerVocab(choice, v){
  if (VQ.locked) return;
  VQ.locked = true;
  var q = VQ.list[VQ.i];
  var correct = (choice === q.answer);
  if (correct) VQ.right++;
  else VQ.missed.push({term: q.term, def: q.def});
  srsGrade(D, q.id, correct);
  persist();

  var btns = document.querySelectorAll('.termopt');
  for (var i = 0; i < btns.length; i++){
    btns[i].disabled = true;
    if (i === q.answer){
      btns[i].className = 'termopt right';
      btns[i].appendChild(el('span', 'flag', 'correct'));
    } else if (i === choice){
      btns[i].className = 'termopt wrong';
      btns[i].appendChild(el('span', 'flag', 'you picked'));
    }
  }
  var fb = el('div', 'feedback ' + (correct ? 'ok' : 'no'));
  fb.appendChild(el('div', 'verdict', correct ? 'Correct' : 'Not quite'));
  if (!correct){
    var p1 = el('div');
    p1.appendChild(el('b', null, q.term));
    p1.appendChild(document.createTextNode(' — ' + q.def));
    fb.appendChild(p1);
  }
  $('vfeedback').appendChild(fb);
  var nx = $('vnext');
  nx.disabled = false;
  nx.focus();
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
  if (item.difficulty >= 2)
    meta.appendChild(el('span', 'tag hard' + (item.difficulty === 3 ? ' exam' : ''),
                        item.difficulty === 3 ? 'Exam' : 'Hard'));
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
  if (item.concept){
    var c = el('div', 'lab');
    c.textContent = 'Concept: ' + item.concept;
    why.appendChild(c);
  }
  wrap.appendChild(why);

  var acts = el('div', 'nbacts');
  var study = studyButton(item.topic, 'STUDY THIS');
  acts.appendChild(study);
  if (item.sub){
    var d = el('button', 'btn mini', 'DRILL IT');
    d.onclick = function(){
      startQuiz({portion: item.portion, count: 10, sub: item.sub,
                 timed: false, difficulty: 'harder'});
    };
    acts.appendChild(d);
  } else if (item.generator){
    var g = el('button', 'btn mini', 'MORE LIKE THIS');
    g.onclick = function(){
      startQuiz({portion: 'math', count: 10, topic: item.generator, timed: false});
    };
    acts.appendChild(g);
  }
  var rm = el('button', 'btn mini ghost', 'REMOVE');
  rm.onclick = function(){
    forgetMiss(D, item.qid); persist(); renderNotebook();
  };
  acts.appendChild(rm);
  wrap.appendChild(acts);
  return wrap;
}

function renderNotebook(){
  var v = $('view-notebook');
  v.className = 'reading';
  v.innerHTML = '<div id="nbBody"></div>';
  var box = $('nbBody');

  var counts = missCounts(D);
  var head = el('div', 'card');
  head.appendChild(cardHead('Notebook', 'every question you have got wrong'));
  head.appendChild(el('p', 'sub',
    'Each question you missed, grouped by topic, with the answer you picked, the ' +
    'right one, and why. Get the same question right later and it is marked off — ' +
    'so what stays open is what you still have not learned.'));

  if (counts.total){
    var f = el('div', 'nbfilter');
    var openBtn = el('button', 'btn' + (NB_OPEN_ONLY ? '' : ' ghost'),
                     'Still open (' + counts.open + ')');
    openBtn.onclick = function(){ NB_OPEN_ONLY = true; renderNotebook(); };
    var allBtn = el('button', 'btn' + (NB_OPEN_ONLY ? ' ghost' : ''),
                    'All (' + counts.total + ')');
    allBtn.onclick = function(){ NB_OPEN_ONLY = false; renderNotebook(); };
    f.appendChild(openBtn);
    f.appendChild(allBtn);
    if (counts.cleared){
      f.appendChild(el('span', 'muted', counts.cleared + ' cleared so far'));
    }
    head.appendChild(f);
  }
  box.appendChild(head);

  var groups = missGroups(D, NB_OPEN_ONLY);
  if (!groups.length){
    var e = el('div', 'card');
    e.appendChild(el('div', 'empty', counts.total
      ? 'Nothing open — you have got every missed question right since. Switch to All to review them again.'
      : 'Nothing here yet. Take a quiz and anything you miss lands in this notebook automatically.'));
    box.appendChild(e);
    window.scrollTo(0, 0);
    return;
  }

  groups.forEach(function(g){
    var card = el('div', 'card');
    var hd = el('div', 'cardhead');
    var t = el('h2', null, g.label);
    hd.appendChild(t);
    hd.appendChild(el('span', 'hint',
      g.items.length + (g.items.length === 1 ? ' question' : ' questions') +
      (g.counts_on_exam ? ' · ' + g.exam_questions + ' on exam' : ' · drill')));
    card.appendChild(hd);
    var list = el('div', 'nbgroup');
    g.items.forEach(function(item){ list.appendChild(notebookEntry(item)); });
    card.appendChild(list);
    box.appendChild(card);
  });
  window.scrollTo(0, 0);
}

/* ---------------------------------------------------------------- study */
function studyFor(topicKey){
  return (DATA.study && DATA.study.topics) ? DATA.study.topics[topicKey] : null;
}

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

function renderStudy(){
  var v = $('view-study');
  v.className = 'reading';
  if (STUDY_TOPIC && studyFor(STUDY_TOPIC)) return renderStudyTopic(v, studyFor(STUDY_TOPIC));

  v.innerHTML = '<div id="studyBody"></div>';
  var box = $('studyBody');

  var intro = el('div', 'card');
  intro.appendChild(cardHead('Study', 'read it, then quiz it'));
  intro.appendChild(el('p', 'sub',
    'Notes for every topic you are quizzed on — the rules, the vocabulary, worked ' +
    'examples, where Georgia differs from the national rule, and the mistakes that ' +
    'cost people marks. Open a topic to read it, then quiz yourself without leaving ' +
    'the page.'));
  var sc = el('div', 'card');
  sc.appendChild(cardHead('Look something up', 'searches every note and term'));
  var sbox = el('div', 'searchbox');
  var inp = el('input');
  inp.type = 'search';
  inp.placeholder = 'escheat, points, binding agreement date…';
  inp.setAttribute('aria-label', 'Search the study notes');
  sbox.appendChild(inp);
  sc.appendChild(sbox);
  var results = el('div');
  results.style.cssText = 'display:flex;flex-direction:column;gap:.7rem;margin-top:.5rem';
  sc.appendChild(results);
  inp.oninput = function(){ runSearch(inp.value, results); };
  box.appendChild(sc);

  box.appendChild(intro);

  var NAMES = {national: 'National portion', georgia: 'Georgia state portion',
               comprehensive: 'Comprehensive subtest'};
  ['national', 'georgia', 'comprehensive'].forEach(function(portion){
    var keys = Object.keys(DATA.study.topics).filter(function(k){
      return DATA.study.topics[k].portion === portion;
    });
    if (!keys.length) return;
    var card = el('div', 'card');
    card.appendChild(cardHead(NAMES[portion],
      portion === 'comprehensive' ? 'cross-cutting drill'
                                  : (portion === 'national' ? '80 questions' : '52 questions')));
    var list = el('div', 'topiclist');
    keys.forEach(function(k){
      var n = DATA.study.topics[k];
      var row = el('div', 'topicrow');
      var who = el('div', 'who');
      who.appendChild(el('div', 'nm', n.label));
      who.appendChild(el('div', 'bl', n.blurb));
      row.appendChild(who);
      var acts = el('div', 'acts');
      acts.appendChild(el('span', 'cnt',
        (n.counts_on_exam ? n.exam_questions + ' on exam · ' : 'drill · ') +
        n.vocab.length + ' terms'));
      acts.appendChild(studyButton(k, 'READ'));
      var qb = el('button', 'btn mini', 'QUIZ');
      qb.onclick = (function(key, p){
        return function(){
          startQuiz({portion: p, count: 15, topic: key, timed: false, difficulty: 'harder'});
        };
      })(k, n.portion);
      acts.appendChild(qb);
      row.appendChild(acts);
      list.appendChild(row);
    });
    card.appendChild(list);
    box.appendChild(card);
  });

  var src = el('div', 'card');
  src.appendChild(cardHead('Where this comes from', 'sources'));
  src.appendChild(el('p', null,
    'These notes were written for this app. Georgia facts are checked against the ' +
    'Commission’s own published reference and the code sections it quotes; federal ' +
    'rules against the agencies that issue them. No commercial exam-prep book is ' +
    'reproduced here.'));
  var slist = el('div', 'callouts');
  (DATA.study.sources || []).forEach(function(s2){
    var d = el('div', 'callout');
    var a = el('a', null, s2.name);
    a.href = s2.url; a.target = '_blank'; a.rel = 'noopener noreferrer';
    a.style.cssText = 'color:var(--accent);font-family:"Barlow",sans-serif;font-weight:600';
    d.appendChild(a);
    d.appendChild(document.createTextNode(' — ' + s2.by + '. ' + s2.note));
    slist.appendChild(d);
  });
  src.appendChild(slist);
  box.appendChild(src);
  window.scrollTo(0, 0);
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

  var answered = 0, right = 0;
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
        answered++;
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

function highlight(text, needle){
  var frag = document.createDocumentFragment();
  var low = text.toLowerCase(), n = needle.toLowerCase(), at = 0, i;
  while ((i = low.indexOf(n, at)) !== -1){
    if (i > at) frag.appendChild(document.createTextNode(text.slice(at, i)));
    frag.appendChild(el('mark', null, text.slice(i, i + needle.length)));
    at = i + needle.length;
  }
  frag.appendChild(document.createTextNode(text.slice(at)));
  return frag;
}

function runSearch(term, into){
  into.innerHTML = '';
  term = (term || '').trim();
  if (term.length < 2) return;
  var n = term.toLowerCase(), hits = [];
  var tops = DATA.study.topics;
  Object.keys(tops).forEach(function(tk){
    var t = tops[tk];
    t.vocab.forEach(function(pair){
      if (pair[0].toLowerCase().indexOf(n) !== -1 ||
          pair[1].toLowerCase().indexOf(n) !== -1){
        hits.push({topic: tk, where: t.label + ' · vocabulary',
                   text: pair[0] + ' — ' + pair[1], rank: 0});
      }
    });
    t.sections.forEach(function(sec){
      var body = (sec.p || []).concat(sec.l || []);
      body.forEach(function(line){
        if (line.toLowerCase().indexOf(n) !== -1){
          hits.push({topic: tk, where: t.label + ' · ' + sec.h, text: line, rank: 1});
        }
      });
    });
  });
  hits.sort(function(a, b){ return a.rank - b.rank; });
  if (!hits.length){
    into.appendChild(el('div', 'muted', 'Nothing found for “' + term + '”.'));
    return;
  }
  into.appendChild(el('div', 'muted',
    hits.length + (hits.length === 1 ? ' match' : ' matches')));
  hits.slice(0, 25).forEach(function(h){
    var d = el('div', 'hit');
    d.appendChild(el('div', 'where', h.where));
    var snip = el('div', 'snip');
    var txt = h.text.length > 260 ? h.text.slice(0, 260) + '…' : h.text;
    snip.appendChild(highlight(txt, term));
    d.appendChild(snip);
    var go = el('div');
    go.appendChild(studyButton(h.topic, 'OPEN TOPIC'));
    d.appendChild(go);
    into.appendChild(d);
  });
}

function renderStudyTopic(v, n){
  v.innerHTML = '<div id="studyBody"></div>';
  var box = $('studyBody');

  var head = el('div', 'card');
  var hd = el('div', 'cardhead');
  var left = el('div');
  left.appendChild(el('h1', null, n.label));
  left.appendChild(el('div', 'muted',
    n.counts_on_exam ? (n.exam_questions + ' of the 132 scored questions come from this topic')
                     : 'A drill topic — not a scored section of the exam'));
  hd.appendChild(left);
  var back = el('button', 'btn mini ghost', 'ALL TOPICS');
  back.onclick = function(){ STUDY_TOPIC = null; renderStudy(); };
  hd.appendChild(back);
  head.appendChild(hd);
  head.appendChild(richPara('sub', n.summary));
  var acts = el('div', 'row');
  [['Quiz me on this (15)', 15], ['Quick check (5)', 5]].forEach(function(a){
    var d = el('div'); d.style.flex = '0 0 auto';
    var b = el('button', 'btn' + (a[1] === 5 ? ' ghost' : ''), a[0]);
    b.onclick = function(){
      startQuiz({portion: n.portion, count: a[1], topic: n.topic, timed: false,
                 difficulty: 'harder'});
    };
    d.appendChild(b); acts.appendChild(d);
  });
  head.appendChild(acts);
  box.appendChild(head);

  n.sections.forEach(function(sec){
    var c = el('div', 'card');
    c.appendChild(el('h2', null, sec.h));
    (sec.p || []).forEach(function(para){ c.appendChild(el('p', null, para)); });
    if (sec.l && sec.l.length){
      var ul = el('ul');
      sec.l.forEach(function(item){ ul.appendChild(bulletItem(item)); });
      c.appendChild(ul);
    }
    var chk = checkBlock(sec);
    if (chk) c.appendChild(chk);
    box.appendChild(c);
  });

  if (n.vocab.length){
    var vc = el('div', 'card');
    vc.appendChild(cardHead('Vocabulary', n.vocab.length + ' terms'));
    var vl = el('div', 'vocablist');
    n.vocab.forEach(function(pair){
      var item = el('div', 'vocabitem');
      item.appendChild(el('div', 'vterm', pair[0]));
      var vd = el('div', 'vdef'); vd.appendChild(richText(pair[1]));
      item.appendChild(vd);
      vl.appendChild(item);
    });
    vc.appendChild(vl);
    box.appendChild(vc);
  }

  if (n.examples.length){
    var ec = el('div', 'card');
    ec.appendChild(cardHead('Worked examples', 'follow the steps'));
    n.examples.forEach(function(ex){
      var w = el('div', 'example');
      w.appendChild(el('h3', null, ex.t));
      var setup = el('div', 'setup'); setup.appendChild(richText(ex.s));
      w.appendChild(setup);
      var ol = el('ol', 'steps');
      ex.w.forEach(function(step){ ol.appendChild(el('li', null, step)); });
      w.appendChild(ol);
      var k = el('div', 'takeaway');
      k.appendChild(el('b', null, 'Takeaway'));
      k.appendChild(richText(ex.k));
      w.appendChild(k);
      ec.appendChild(w);
    });
    box.appendChild(ec);
  }

  [['Georgia differences', 'where Georgia departs from the national rule', n.ga, 'ga'],
   ['Common traps', 'where marks get lost', n.traps, 'trap']].forEach(function(blk){
    if (!blk[2] || !blk[2].length) return;
    var c = el('div', 'card');
    c.appendChild(cardHead(blk[0], blk[1]));
    var l = el('div', 'callouts');
    blk[2].forEach(function(item){
      var c2 = el('div', 'callout ' + blk[3]);
      c2.appendChild(richText(item));
      l.appendChild(c2);
    });
    c.appendChild(l);
    box.appendChild(c);
  });

  var foot = el('div', 'card');
  var frow = el('div', 'row');
  var d1 = el('div'); d1.style.flex = '0 0 auto';
  var b1 = el('button', 'btn', 'Quiz me on this topic');
  b1.onclick = function(){
    startQuiz({portion: n.portion, count: 15, topic: n.topic, timed: false,
               difficulty: 'harder'});
  };
  d1.appendChild(b1); frow.appendChild(d1);
  var d2 = el('div'); d2.style.flex = '0 0 auto';
  var b2 = el('button', 'btn ghost', 'Back to all topics');
  b2.onclick = function(){ STUDY_TOPIC = null; renderStudy(); };
  d2.appendChild(b2); frow.appendChild(d2);
  foot.appendChild(frow);
  box.appendChild(foot);
  window.scrollTo(0, 0);
}

/* ----------------------------------------------------------- weak spots */
function drillButton(topicKey, portion, count){
  var b = el('button', 'btn ghost', 'Drill ' + count);
  b.onclick = function(){
    startQuiz({portion: portion, count: count, topic: topicKey,
               timed: false, difficulty: 'harder'});
  };
  return b;
}

function renderWeak(){
  var v = $('view-weak');
  v.innerHTML =
    '<h1>Weak spots</h1>' +
    '<p class="sub">The small things you have actually gotten wrong, each with its own ' +
    'drill. Broad topic quizzes live on the Practice tab and the Dashboard.</p>' +
    '<div id="weakBody"></div>';
  var box = $('weakBody');

  var missedCount = 0;
  Object.keys(D.items || {}).forEach(function(id){
    var r = D.items[id];
    if (r.seen > r.correct) missedCount++;
  });

  var act = el('div', 'card');
  act.appendChild(cardHead('Drill everything at once', 'weighted by miss rate and exam value'));
  act.appendChild(el('p', 'muted',
    'Weak-spot mode weights topics by how you have scored and by what they are worth ' +
    'on the exam, and puts questions you have already missed at the front of the queue.' +
    (missedCount ? ' You currently have ' + missedCount + ' previously missed question' +
     (missedCount === 1 ? '' : 's') + ' in the pool.' : '')));
  var row = el('div', 'row');
  [['National', 'national'], ['Georgia', 'georgia'], ['Both portions', 'mixed']]
    .forEach(function(p){
      var d = el('div'); d.style.flex = '0 0 auto';
      var b = el('button', 'btn' + (p[1] === 'mixed' ? ' ghost' : ''), p[0] + ' (20)');
      b.onclick = function(){
        startQuiz({portion: p[1], count: 20, weak_spot: true, timed: true,
                   difficulty: 'harder'});
      };
      d.appendChild(b); row.appendChild(d);
    });
  act.appendChild(row);
  box.appendChild(act);

  /* the little topics, ranked */
  var subs = subReport(D, 2);
  var card = el('div', 'card');
  card.appendChild(cardHead('Sub-topics you are weakest at', 'lowest accuracy first'));
  if (!subs.length){
    card.appendChild(el('div', 'empty',
      'Nothing ranked yet. Answer at least 2 questions in a sub-topic and it appears ' +
      'here with its own drill button.'));
  } else {
    var wrap = el('div', 'scroll'), t = el('table', 'stats');
    t.innerHTML = '<tr><th>Weak spot</th><th>Topic</th><th class="num">Correct</th>' +
                  '<th class="num">Accuracy</th><th></th><th></th><th></th></tr>';
    subs.forEach(function(r){
      var parent = el('td');
      parent.appendChild(document.createTextNode(r.topic_label + ' '));
      parent.appendChild(tagFor(r.portion));
      var study = el('td');
      study.appendChild(studyButton(r.topic, 'STUDY'));
      t.appendChild(statRow([
        el('td', null, r.label),
        parent,
        el('td', 'num', r.correct + '/' + r.seen),
        el('td', 'num', pct(r.pct)),
        accuracyCell(r.pct),
        study,
        actionCell('DRILL', (function(sub, p){
          return function(){
            startQuiz({portion: p, count: 10, sub: sub, timed: false, difficulty: 'harder'});
          };
        })(r.sub, r.portion))
      ]));
    });
    wrap.appendChild(t); card.appendChild(wrap);
    card.appendChild(el('p', 'muted',
      'A drill starts with every question written for that sub-topic, then fills out the ' +
      'set from the rest of its parent topic so you always get a full round.'));
  }
  box.appendChild(card);

  /* math problem types */
  var mrows = generatorReport(D).filter(function(g){ return g.seen >= 2 && g.pct < 0.8; });
  if (mrows.length){
    var mc = el('div', 'card');
    mc.appendChild(cardHead('Math types to drill', 'under 80%'));
    var mwrap = el('div', 'scroll'), mt = el('table', 'stats');
    mt.innerHTML = '<tr><th>Type</th><th class="num">Correct</th><th class="num">Accuracy</th>' +
                   '<th></th><th></th></tr>';
    mrows.slice(0, 8).forEach(function(g){
      mt.appendChild(statRow([
        el('td', null, g.label),
        el('td', 'num', g.correct + '/' + g.seen),
        el('td', 'num', pct(g.pct)),
        accuracyCell(g.pct),
        actionCell('DRILL', (function(k){
          return function(){ startQuiz({portion:'math', count:10, topic:k, timed:false}); };
        })(g.key))
      ]));
    });
    mwrap.appendChild(mt); mc.appendChild(mwrap);
    box.appendChild(mc);
  }

  /* topics with too little data to judge */
  var rep = weakestReport(D, 10);
  if (rep.untested.length){
    var uc = el('div', 'card');
    uc.appendChild(cardHead('Not tested yet', 'unknown is not the same as weak'));
    uc.appendChild(el('p', 'muted',
      'Fewer than 3 questions answered in these topics. Worth finding out before exam day.'));
    var list = el('div', 'focuslist');
    rep.untested.forEach(function(r){
      var d = el('div', 'focus');
      d.style.cssText = 'display:flex;justify-content:space-between;align-items:center;gap:10px';
      var left = el('div');
      left.appendChild(el('b', null, r.label));
      left.appendChild(document.createTextNode(' '));
      left.appendChild(tagFor(r.portion));
      left.appendChild(el('div', 'muted',
        r.seen ? (r.seen + ' answered so far') : 'never attempted'));
      d.appendChild(left);
      d.appendChild(drillButton(r.topic, r.portion, 10));
      list.appendChild(d);
    });
    uc.appendChild(list); box.appendChild(uc);
  }
}

/* ----------------------------------------------------------- dashboard */
function sparkline(points, w, h){
  var ns = 'http://www.w3.org/2000/svg';
  var svg = document.createElementNS(ns,'svg');
  svg.setAttribute('viewBox','0 0 '+w+' '+h);
  svg.setAttribute('width', w); svg.setAttribute('height', h);
  svg.setAttribute('class','spark'); svg.setAttribute('role','img');
  [0.5,0.75,1].forEach(function(y){
    var yy = h - y*(h-14) - 7;
    var ln = document.createElementNS(ns,'line');
    ln.setAttribute('x1',26); ln.setAttribute('x2',w);
    ln.setAttribute('y1',yy); ln.setAttribute('y2',yy);
    ln.setAttribute('class','gl');
    if (y === 0.75) ln.setAttribute('stroke-dasharray','3 3');
    svg.appendChild(ln);
    var tx = document.createElementNS(ns,'text');
    tx.setAttribute('x',0); tx.setAttribute('y',yy+3);
    tx.textContent = Math.round(y*100)+'%';
    svg.appendChild(tx);
  });
  if (points.length){
    var step = points.length > 1 ? (w-32)/(points.length-1) : 0;
    var d = points.map(function(p,i){
      return (i?'L':'M')+(28+i*step).toFixed(1)+' '+(h-p.pct*(h-14)-7).toFixed(1);
    }).join(' ');
    var path = document.createElementNS(ns,'path');
    path.setAttribute('d',d); path.setAttribute('fill','none');
    path.setAttribute('stroke','currentColor'); path.setAttribute('stroke-width','2');
    path.setAttribute('stroke-linejoin','round'); path.setAttribute('stroke-linecap','round');
    svg.appendChild(path);
    points.forEach(function(p,i){
      var c = document.createElementNS(ns,'circle');
      c.setAttribute('cx',28+i*step); c.setAttribute('cy',h-p.pct*(h-14)-7);
      c.setAttribute('r', i === points.length-1 ? 3.4 : 2.4);
      c.setAttribute('fill','currentColor');
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
  var td = el('td');
  var track = el('div', 'bar-track');
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
  b.onclick = fn;
  td.appendChild(b);
  return td;
}

function statRow(cells){
  var tr = el('tr');
  cells.forEach(function(c){ tr.appendChild(c); });
  return tr;
}

function renderDash(){
  var v = $('view-dash');
  v.innerHTML = '<div id="dashBody"></div>';
  var box = $('dashBody');

  if (!D.attempts.length){
    var empty = el('div', 'card');
    empty.appendChild(el('div', 'empty',
      'No attempts recorded yet. Take a quiz and every table below fills in.'));
    box.appendChild(empty);
    return;
  }

  var sec = el('div', 'card');
  sec.appendChild(cardHead('Sections', 'recent accuracy'));
  var swrap = el('div', 'scroll'), st = el('table', 'stats');
  st.innerHTML = '<tr><th>Section</th><th class="num">Sets</th><th class="num">Qs</th>' +
                 '<th class="num">Recent</th><th></th><th class="num">Trend</th><th></th></tr>';
  sectionTable(D).forEach(function(r){
    var name = el('td');
    name.appendChild(el('b', null, r.name));
    name.appendChild(document.createTextNode(' '));
    name.appendChild(r.scored ? el('span', 'tag', r.scored + ' on exam')
                              : el('span', 'tag comp', 'drill'));
    st.appendChild(statRow([
      name,
      el('td', 'num', String(r.sets)),
      el('td', 'num', String(r.qs)),
      el('td', 'num', r.recent_pct === null ? '—' : pct(r.recent_pct)),
      accuracyCell(r.recent_pct),
      trendCell(r.trend),
      actionCell(r.sets ? 'DRILL' : 'START', (function(p, hasData){
        return function(){
          startQuiz({portion: p, count: 20, weak_spot: hasData,
                     timed: true, difficulty: 'harder'});
        };
      })(r.portion, !!r.sets))
    ]));
  });
  swrap.appendChild(st); sec.appendChild(swrap);
  box.appendChild(sec);

  var tc = el('div', 'card');
  tc.appendChild(cardHead('Topics', 'badge is questions on the real exam'));
  var twrap = el('div', 'scroll'), tt = el('table', 'stats');
  tt.innerHTML = '<tr><th>Topic</th><th class="num">Sets</th><th class="num">Qs</th>' +
                 '<th class="num">Recent</th><th></th><th class="num">Trend</th>' +
                 '<th></th><th></th></tr>';
  var lastPortion = null;
  topicTable(D).forEach(function(r){
    if (r.portion !== lastPortion){
      lastPortion = r.portion;
      var head = el('tr', 'grouprow');
      var cell = el('td', null, {national: 'National portion',
                                 georgia: 'Georgia state portion',
                                 comprehensive: 'Comprehensive subtest'}[r.portion]);
      cell.colSpan = 8;
      head.appendChild(cell);
      tt.appendChild(head);
    }
    var name = el('td');
    name.appendChild(document.createTextNode(r.label + ' '));
    name.appendChild(r.counts_on_exam
      ? el('span', 'tag', String(r.exam_questions))
      : el('span', 'tag comp', 'drill'));
    tt.appendChild(statRow([
      name,
      el('td', 'num', String(r.sets)),
      el('td', 'num', String(r.qs)),
      el('td', 'num', r.recent_pct === null ? '—' : pct(r.recent_pct)),
      accuracyCell(r.recent_pct),
      trendCell(r.trend),
      actionCell(r.sets ? 'DRILL' : 'START', (function(t, p){
        return function(){
          startQuiz({portion: p, count: 15, topic: t, timed: false, difficulty: 'harder'});
        };
      })(r.topic, r.portion))
    ]));
  });
  twrap.appendChild(tt); tc.appendChild(twrap);
  box.appendChild(tc);

  var subs = subReport(D, 2, 12);
  var wc = el('div', 'card');
  wc.appendChild(cardHead('Weak spots', 'the little topics you got wrong'));
  if (!subs.length){
    wc.appendChild(el('div', 'empty',
      'Answer at least 2 questions in a sub-topic and the weak ones are listed here, ' +
      'each with its own drill.'));
  } else {
    var wwrap = el('div', 'scroll'), wt = el('table', 'stats');
    wt.innerHTML = '<tr><th>Weak spot</th><th>Topic</th><th class="num">Correct</th>' +
                   '<th class="num">Accuracy</th><th></th><th></th><th></th></tr>';
    subs.forEach(function(r){
      var parent = el('td');
      parent.appendChild(document.createTextNode(r.topic_label + ' '));
      parent.appendChild(tagFor(r.portion));
      var study = el('td');
      study.appendChild(studyButton(r.topic, 'STUDY'));
      wt.appendChild(statRow([
        el('td', null, r.label),
        parent,
        el('td', 'num', r.correct + '/' + r.seen),
        el('td', 'num', pct(r.pct)),
        accuracyCell(r.pct),
        study,
        actionCell('DRILL', (function(sub, p){
          return function(){
            startQuiz({portion: p, count: 10, sub: sub, timed: false, difficulty: 'harder'});
          };
        })(r.sub, r.portion))
      ]));
    });
    wwrap.appendChild(wt); wc.appendChild(wwrap);
    wc.appendChild(el('p', 'muted',
      'A drill starts with every question written for that sub-topic, then fills out ' +
      'the set from the rest of its parent topic.'));
  }
  box.appendChild(wc);

  var mrows = generatorReport(D).filter(function(x){ return x.seen; });
  var mc = el('div', 'card');
  mc.appendChild(cardHead('Math by problem type', 'weakest first'));
  if (!mrows.length){
    mc.appendChild(el('div', 'empty', 'No math attempts yet.'));
  } else {
    var mwrap = el('div', 'scroll'), mt = el('table', 'stats');
    mt.innerHTML = '<tr><th>Type</th><th class="num">Correct</th>' +
                   '<th class="num">Accuracy</th><th></th><th></th></tr>';
    mrows.forEach(function(x){
      mt.appendChild(statRow([
        el('td', null, x.label),
        el('td', 'num', x.correct + '/' + x.seen),
        el('td', 'num', pct(x.pct)),
        accuracyCell(x.pct),
        actionCell('DRILL', (function(k){
          return function(){
            startQuiz({portion: 'math', count: 10, topic: k, timed: false});
          };
        })(x.key))
      ]));
    });
    mwrap.appendChild(mt); mc.appendChild(mwrap);
  }
  box.appendChild(mc);

  var series = trendSeries(D);
  var hasTrend = Object.keys(series).some(function(k){ return series[k].length >= 2; });
  if (hasTrend){
    var trc = el('div', 'card');
    trc.appendChild(cardHead('Score trend over time', 'dashed line is the 75% pass mark'));
    topicReport(D).forEach(function(t){
      var sdata = series[t.topic];
      if (!sdata || sdata.length < 2) return;
      var row = el('div', 'trendrow'), who = el('div', 'who'), name = el('div');
      name.appendChild(el('b', null, t.label));
      name.appendChild(document.createTextNode(' '));
      name.appendChild(tagFor(t.portion));
      who.appendChild(name);
      who.appendChild(el('div', 'muted', pct(t.pct) + ' overall, ' + t.seen + ' questions'));
      row.appendChild(who);
      var chart = el('div');
      chart.appendChild(sparkline(sdata, 280, 84));
      row.appendChild(chart);
      trc.appendChild(row);
    });
    box.appendChild(trc);
  }
}

/* ----------------------------------------------------------------- plan */
function renderPlan(){
  var v = $('view-plan'), p = D.profile || {};
  v.innerHTML =
    '<h1>Study plan</h1><p class="sub">Weighted for the real exam: 80 national ' +
    'questions, 52 Georgia.</p>' +
    '<div class="card"><div class="row">' +
      '<div><label for="examDate">Exam date</label><input type="date" id="examDate"></div>' +
      '<div><label for="masteryDate">Want to be done by</label><input type="date" id="masteryDate"></div>' +
      '<div style="max-width:150px"><label for="hours">Study hours/week</label>' +
        '<input type="number" id="hours" min="1" max="40" value="8"></div>' +
      '<div style="flex:0 0 auto"><button class="btn" id="savePlan">Save &amp; rebuild plan</button></div>' +
    '</div><div style="margin-top:15px">' +
      '<label>Topics you know are weak (these get pushed to the front)</label>' +
      '<div id="weakPicker" class="grid g3" style="margin-top:7px"></div></div></div>' +
    '<div id="planBody"></div>';
  if (p.exam_date) $('examDate').value = p.exam_date;
  if (p.mastery_date) $('masteryDate').value = p.mastery_date;
  if (p.hours_per_week) $('hours').value = p.hours_per_week;

  var picked = p.declared_weak || [], box = $('weakPicker');
  DATA.topics.forEach(function(t){
    var lab = el('label','pick');
    var cb = el('input'); cb.type = 'checkbox'; cb.value = t.key;
    cb.checked = picked.indexOf(t.key) >= 0;
    lab.appendChild(cb);
    var span = el('span');
    span.appendChild(document.createTextNode(t.label+' '));
    span.appendChild(tagFor(t.portion));
    lab.appendChild(span);
    box.appendChild(lab);
  });

  $('savePlan').onclick = function(){
    var weak = [];
    box.querySelectorAll('input:checked').forEach(function(c){ weak.push(c.value); });
    D.profile = D.profile || {};
    D.profile.exam_date = $('examDate').value || null;
    D.profile.mastery_date = $('masteryDate').value || null;
    D.profile.hours_per_week = +$('hours').value || 8;
    D.profile.declared_weak = weak;
    persist(); countdown(); drawPlan();
  };
  drawPlan();
}

function drawPlan(){
  var box = $('planBody'); box.innerHTML = '';
  var p = buildPlan(D);
  if (p.error){
    var c = el('div','card');
    c.appendChild(el('div','empty',p.error));
    box.appendChild(c); return;
  }
  var head = el('div','card'), g = el('div','grid g3');
  [['Days to exam',String(p.days_to_exam)],
   ['Days to your mastery date',String(p.days_to_mastery)],
   ['Exam split',p.weighting.national+' national / '+p.weighting.georgia+' Georgia']
  ].forEach(function(r){
    var d = el('div');
    d.appendChild(el('div','muted',r[0]));
    d.appendChild(el('div','stat small',r[1]));
    g.appendChild(d);
  });
  head.appendChild(g); box.appendChild(head);

  p.weeks.forEach(function(w){
    var c = el('div','card'), wk = el('div','week');
    wk.appendChild(el('h3', null, 'Week '+w.week+' -- '+w.phase));
    wk.appendChild(el('div','when', w.start+' to '+w.end+'  |  target '+w.target_questions+
      ' questions ('+w.national_questions+' national, '+w.georgia_questions+' Georgia)'));
    var ul = el('ul');
    w.tasks.forEach(function(t){ ul.appendChild(el('li', null, t)); });
    wk.appendChild(ul);
    if (w.focus.length){
      var fl = el('div','focuslist');
      w.focus.forEach(function(f){
        var d = el('div','focus'), line = el('div');
        line.appendChild(el('b', null, f.label));
        line.appendChild(document.createTextNode(' '));
        line.appendChild(tagFor(f.portion));
        d.appendChild(line);
        d.appendChild(el('div','muted',f.why));
        fl.appendChild(d);
      });
      wk.appendChild(fl);
    }
    c.appendChild(wk); box.appendChild(c);
  });

  if (p.buffer_plan.length){
    var b = el('div','card');
    b.appendChild(el('h2',null,'Final '+p.buffer_days+' days before the exam'));
    var ul2 = el('ul');
    p.buffer_plan.forEach(function(t){ ul2.appendChild(el('li', null, t)); });
    b.appendChild(ul2); box.appendChild(b);
  }
}

/* ---------------------------------------------------------------- setup */
function renderSetup(){
  var v = $('view-setup');
  v.innerHTML =
    '<h1>Setup</h1><p class="sub">Your progress is stored in this browser only, so each ' +
    'device keeps its own history. Use export and import to move it between them.</p>' +
    '<div class="card"><h2>Move progress between devices</h2>' +
      '<p class="muted">Export copies your whole history as text. On the other device, ' +
      'paste it below and choose Import.</p>' +
      '<div class="row" style="margin-bottom:12px">' +
        '<div style="flex:0 0 auto"><button class="btn" id="doExport">Export to the box below</button></div>' +
        '<div style="flex:0 0 auto"><button class="btn ghost" id="doCopy">Copy to clipboard</button></div>' +
        '<div style="flex:0 0 auto"><button class="btn ghost" id="doImport">Import what is in the box</button></div>' +
      '</div>' +
      '<textarea id="ioBox" rows="7" spellcheck="false" placeholder="Exported progress appears here."></textarea>' +
      '<div class="muted" id="ioNote" style="margin-top:8px"></div></div>' +
    '<div class="card"><h2>Start over</h2>' +
      '<p class="muted">Clears every attempt and score. Your exam date and weak-area ' +
      'choices are kept.</p>' +
      '<button class="btn danger" id="doReset">Erase my history</button></div>' +
    '<div class="card"><h2>What is in here</h2><div id="bankBox"></div></div>';

  $('doExport').onclick = function(){
    $('ioBox').value = JSON.stringify(D);
    $('ioNote').textContent = 'Exported ' + D.attempts.length + ' attempts.';
  };
  $('doCopy').onclick = function(){
    if (!$('ioBox').value) $('ioBox').value = JSON.stringify(D);
    $('ioBox').select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch(e){ ok = false; }
    if (!ok && navigator.clipboard){
      navigator.clipboard.writeText($('ioBox').value).then(function(){
        $('ioNote').textContent = 'Copied.';
      });
      return;
    }
    $('ioNote').textContent = ok ? 'Copied.' : 'Could not copy -- select the text and copy manually.';
  };
  $('doImport').onclick = function(){
    var raw = $('ioBox').value.trim();
    if (!raw){ $('ioNote').textContent = 'Paste exported progress into the box first.'; return; }
    var d;
    try { d = JSON.parse(raw); }
    catch(e){ $('ioNote').textContent = 'That is not valid exported progress.'; return; }
    if (!d || !Array.isArray(d.attempts)){
      $('ioNote').textContent = 'That does not look like a progress export.'; return;
    }
    if (!confirm('Replace this device’s history with the imported one? ' +
                 'This device currently has ' + D.attempts.length + ' attempts.')) return;
    Object.keys(EMPTY).forEach(function(k){
      if (d[k] === undefined) d[k] = JSON.parse(JSON.stringify(EMPTY[k]));
    });
    D = d; persist(); countdown();
    $('ioNote').textContent = 'Imported ' + D.attempts.length + ' attempts.';
  };
  $('doReset').onclick = function(){
    if (!confirm('Erase all attempts and scores? This cannot be undone.')) return;
    D.attempts = []; D.topics = {}; D.subs = {};
    D.items = {}; D.generators = {}; D.misses = {};
    persist(); renderSetup();
  };

  var mathN = 0;
  Object.keys(DATA.math).forEach(function(k){ mathN += DATA.math[k].q.length; });
  function count(k, hardOnly){
    var rows = DATA.banks[k] || [];
    return hardOnly ? rows.filter(function(r){ return r.difficulty === 2; }).length : rows.length;
  }
  var box = $('bankBox'), wrap = el('div','scroll'), t = el('table');
  t.innerHTML = '<tr><th>Bank</th><th class="num">Questions</th></tr>';
  [['National portion (' + count('national', true) + ' hard)', count('national')],
   ['Georgia portion (' + count('georgia', true) + ' hard)', count('georgia')],
   ['Comprehensive subtest (all hard)', count('comprehensive')],
   ['Math problems (' + Object.keys(DATA.math).length + ' types)', mathN],
   ['Attempts recorded on this device', D.attempts.length]].forEach(function(r){
    var tr = el('tr');
    tr.appendChild(el('td', null, r[0]));
    tr.appendChild(el('td','num', String(r[1])));
    t.appendChild(tr);
  });
  wrap.appendChild(t); box.appendChild(wrap);
}

/* ----------------------------------------------------------------- boot */
(function(){
  var recovered = backfillMisses(D);
  if (recovered) persist();
  var mathN = 0;
  Object.keys(DATA.math).forEach(function(k){ mathN += DATA.math[k].q.length; });
  var written = 0, hard = 0, exam = 0;
  Object.keys(DATA.banks).forEach(function(k){
    written += DATA.banks[k].length;
    hard += DATA.banks[k].filter(function(r){ return r.difficulty === 2; }).length;
    exam += DATA.banks[k].filter(function(r){ return r.difficulty === 3; }).length;
  });
  var vocabN = 0;
  Object.keys(DATA.study.topics).forEach(function(k){
    vocabN += DATA.study.topics[k].vocab.length;
  });
  $('bankcount').textContent = written + ' questions (' + hard + ' hard, ' + exam +
    ' exam-realistic) + ' + mathN +
    ' math problems + study notes on ' + Object.keys(DATA.study.topics).length +
    ' topics (' + vocabN + ' terms)';
  countdown();
  show('home');
})();
