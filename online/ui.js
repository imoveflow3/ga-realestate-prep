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
var VIEWS = ['dash','study','home','math','weak','quiz','result','plan','setup'];
var STUDY_TOPIC = null;
function show(v){
  VIEWS.forEach(function(x){ var n = $('view-'+x); if (n) n.hidden = (x !== v); });
  document.querySelectorAll('#rail button').forEach(function(b){
    var on = b.dataset.view === v;
    b.classList.toggle('on', on);
    b.setAttribute('aria-current', on ? 'page' : 'false');
  });
  if (v === 'home') renderHome();
  if (v === 'study') renderStudy();
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
      '<div style="max-width:210px"><label for="difficulty">Difficulty</label><select id="difficulty">' +
        '<option value="harder" selected>Harder mix (default)</option>' +
        '<option value="hard">Hard only</option>' +
        '<option value="any">Full bank</option>' +
        '<option value="core">Core only</option></select></div>' +
      '<div style="flex:0 0 auto"><button class="btn" id="start">Start quiz</button></div>' +
      '<div style="flex:0 0 auto"><button class="btn ghost" id="startWeak">Weak-spot quiz</button></div>' +
      '<div style="flex:0 0 auto"><button class="btn ghost" id="startExam">Full mock exam (132)</button></div>' +
    '</div>' +
    '<p class="muted" style="margin:13px 0 0"><b>Weak-spot mode</b> draws more heavily from ' +
    'topics and individual questions you have missed before. <b>Harder mix</b> pulls about ' +
    'two thirds of its questions from the hard tier; <b>Comprehensive</b> is a cross-cutting ' +
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
  LAST = opts;
  QUIZ = {qs:qs, i:0, correct:0, answers:new Array(qs.length),
          portion: (opts.mode === 'exam') ? 'mixed' : opts.portion,
          mode: opts.mode || (opts.topic ? 'topic' : 'quiz'),
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
  $('qhard').hidden = ((q.difficulty || 1) !== 2);
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
                          choice:choice, correct:correct,
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
                    choice:null, correct:false, seconds:0});
    }
  });
  var att = recordAttempt(D, q.portion, q.mode, answers,
                          (Date.now()-q.started)/1000, q.weak);
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
    D.attempts = []; D.topics = {}; D.subs = {}; D.items = {}; D.generators = {};
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
  var mathN = 0;
  Object.keys(DATA.math).forEach(function(k){ mathN += DATA.math[k].q.length; });
  var written = 0, hard = 0;
  Object.keys(DATA.banks).forEach(function(k){
    written += DATA.banks[k].length;
    hard += DATA.banks[k].filter(function(r){ return r.difficulty === 2; }).length;
  });
  var vocabN = 0;
  Object.keys(DATA.study.topics).forEach(function(k){
    vocabN += DATA.study.topics[k].vocab.length;
  });
  $('bankcount').textContent = written + ' questions (' + hard + ' hard) + ' + mathN +
    ' math problems + study notes on ' + Object.keys(DATA.study.topics).length +
    ' topics (' + vocabN + ' terms)';
  countdown();
  show('home');
})();
