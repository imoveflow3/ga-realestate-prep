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
var VIEWS = ['welcome','today','dash','study','cards','vocab','home','math',
             'notebook','saved','weak','quiz','result','plan','setup','about',
             'admin','users'];

/* Served from behind the paywall, this build has no reason to sell itself:
   the reader has already bought. It skips the front door and drops the
   "free, no signup" language, which is now simply untrue. */
var PAID = (typeof window !== 'undefined') && window.__PAID__ === true;

/* Two different questions. PAID decides what the copy may claim. FRONTDOOR
   decides whether the app still needs a landing page of its own -- once the
   site has one at /, a second one inside the app is just a wrong turn. It
   holds the href back to that front door, or null. */
var FRONTDOOR = (typeof window !== 'undefined' && window.__FRONTDOOR__)
                  ? window.__FRONTDOOR__ : null;
var NO_LANDING = PAID || !!FRONTDOOR;

/* Everything reachable from the navigation, in one table, so the desktop rail,
   the phone tab bar and the More sheet can never drift apart. */
var NAV = [
  {v:'welcome',  name:'Home',       desc:'What this is, and a question to try'},
  {v:'today',    name:'Today',      desc:'Five things to do right now'},
  {v:'study',    name:'Study',      desc:'Read the material, topic by topic'},
  {v:'home',     name:'Practice',   desc:'Timed quizzes and the full mock exam'},
  {v:'dash',     name:'Progress',   desc:'Where you stand against the 75% pass mark'},
  {v:'vocab',    name:'Vocab',      desc:'See the definition, name the term'},
  {v:'cards',    name:'Flashcards', desc:'Spaced repetition on what you keep missing'},
  {v:'math',     name:'Math',       desc:'Every calculation, worked step by step'},
  {v:'notebook', name:'Notebook',   desc:'Every question you have got wrong'},
  {v:'saved',    name:'Bookmarks',  desc:'Lessons you saved to come back to'},
  {v:'weak',     name:'Weak spots', desc:'Drill the narrow topics dragging you down'},
  {v:'plan',     name:'Study plan', desc:'A week-by-week schedule to your test date'},
  {v:'setup',    name:'Account settings', desc:'Your details, devices and sign-out'},
  {v:'about',    name:'About',      desc:'What this is, who made it, what it is not'}
];
if (NO_LANDING) NAV = NAV.filter(function(n){ return n.v !== 'welcome'; });
var TABS = ['today','study','home','dash'];          // the phone tab bar
var NOHASH = {quiz:1, result:1};                     // not worth a shareable link
var VQ = null;
var VOCAB_LOG_OPEN_ONLY = true;
var NB_OPEN_ONLY = true;
var STUDY_TOPIC = null;
var HASHLOCK = false;
var CURRENT = null;

/* The size of the real exam, counted from the blueprint rather than typed
   into sentences. It was typed into sentences, the blueprint changed, and
   six different places went on claiming 132 for a 152-question exam. */
function examScored(portion){
  var p = DATA.portions[portion];
  return (p && !p.practice_only) ? (p.scored || 0) : 0;
}
function examTotal(){
  var n = 0;
  for (var k in DATA.portions) if (DATA.portions.hasOwnProperty(k)) n += examScored(k);
  return n;
}
function examMinutes(){
  var n = 0;
  for (var k in DATA.portions){
    if (!DATA.portions.hasOwnProperty(k)) continue;
    var p = DATA.portions[k];
    if (!p.practice_only) n += (p.minutes || 0);
  }
  return n;
}
/* Seconds a real candidate gets per question, rounded to something a person
   would say out loud. */
function examPace(){
  var t = examTotal();
  return DATA.spq || (t ? Math.round(examMinutes() * 60 / t / 5) * 5 : 75);
}
function hoursPhrase(mins){
  var h = Math.floor(mins / 60), m = mins % 60;
  return m ? (h + ' h ' + m + ' m') : (h + ' hours');
}

var RENDERERS = {
  welcome: function(){ renderWelcome(); },
  home: function(){ renderHome(); },
  today: function(){ renderToday(); },
  cards: function(){ renderCards(); },
  vocab: function(){ renderVocab(); },
  study: function(){ renderStudy(); },
  notebook: function(){ renderNotebook(); },
  saved: function(){ renderSaved(); },
  math: function(){ renderMath(); },
  weak: function(){ renderWeak(); },
  dash: function(){ renderDash(); },
  plan: function(){ renderPlan(); },
  setup: function(){ renderSetup(); },
  admin: function(){ renderAdmin(); },
  users: function(){ renderUsers(); },
  about: function(){ renderAbout(); }
};

function show(v, silent){
  if (VIEWS.indexOf(v) < 0) v = 'today';
  CURRENT = v;
  VIEWS.forEach(function(x){ var n = $('view-'+x); if (n) n.hidden = (x !== v); });

  document.querySelectorAll('#rail button').forEach(function(b){
    var on = b.dataset.view === v;
    b.classList.toggle('on', on);
    b.setAttribute('aria-current', on ? 'page' : 'false');
  });
  /* A quiz launched from Practice should keep Practice lit, not light nothing. */
  var lit = (v === 'quiz' || v === 'result') ? 'home' : v;
  document.querySelectorAll('#tabbar button').forEach(function(b){
    var on = b.dataset.view === lit ||
             (b.dataset.view === '__more' && TABS.indexOf(lit) < 0 && lit !== 'welcome');
    b.classList.toggle('on', on);
    b.setAttribute('aria-current', on && b.dataset.view !== '__more' ? 'page' : 'false');
  });

  /* the tab bar is a trap door out of a half-finished quiz: take it away */
  document.body.classList.toggle('inquiz', v === 'quiz');

  /* the front door hides the rail and the status strip -- neither means
     anything to someone who has just arrived -- and offers one way in */
  var landing = (v === 'welcome' && WIZ.step === 0 && !NO_LANDING);
  document.body.classList.toggle('landing', landing);
  var ab = $('appBtn');
  if (ab){
    ab.hidden = !landing;
    ab.onclick = function(){ navTo(onboarded(D) ? 'today' : 'home'); };
  }

  if (RENDERERS[v]) RENDERERS[v]();

  if (!silent && !NOHASH[v]){
    HASHLOCK = true;
    try { location.hash = (v === 'today') ? '' : '#' + v; } catch(e){}
    setTimeout(function(){ HASHLOCK = false; }, 0);
  }
  window.scrollTo(0, 0);
  var m = $('main');
  if (m && v !== 'quiz') m.focus({preventScroll: true});
}

/* Guards the one destructive thing navigation can do: bin a running quiz. */
function navTo(v){
  if (QUIZ && !confirm('Leave this quiz? It will not be scored.')) return false;
  if (QUIZ){ stopTimer(); QUIZ = null; document.body.classList.remove('inquiz'); }
  closeSheet();
  closeDrawer();
  show(v);
  return true;
}

function routeFromHash(){
  var v = (location.hash || '').replace(/^#\/?/, '');
  if (!v) return onboarded(D) ? 'today' : 'welcome';
  if (VIEWS.indexOf(v) < 0 || NOHASH[v]) return onboarded(D) ? 'today' : 'welcome';
  return v;
}

window.addEventListener('hashchange', function(){
  if (HASHLOCK) return;
  var want = routeFromHash();
  if (want === CURRENT) return;
  if (QUIZ){ stopTimer(); QUIZ = null; document.body.classList.remove('inquiz'); }
  closeSheet();
  show(want, true);
});

/* Home is the sales page. When the site has one of its own, the app's
   copy of it has nothing left to say. */
if (NO_LANDING){
  document.querySelectorAll('#rail button[data-view="welcome"]')
    .forEach(function(b){ b.remove(); });
}
document.querySelectorAll('#rail button').forEach(function(b){
  b.onclick = function(){ navTo(b.dataset.view); };
});
document.querySelectorAll('#tabbar button').forEach(function(b){
  b.onclick = function(){
    if (b.dataset.view === '__more'){ openDrawer(); return; }
    navTo(b.dataset.view);
  };
});
document.querySelectorAll('[data-goto]').forEach(function(b){
  b.onclick = function(){ navTo(b.dataset.goto); };
});

/* ------------------------------------------------------- stray taps ----
   Showing something new directly under the finger means the tail of that same
   tap lands on whatever just appeared: the More sheet opened and shut again in
   one touch, and the setup wizard silently ticked a topic nobody chose. A
   press and the click it produces always share an element, so remember where
   the press landed and drop any click that did not start on what it hit. */
var PRESSED = null;
document.addEventListener('pointerdown', function(e){ PRESSED = e.target; }, true);
document.addEventListener('mousedown', function(e){ PRESSED = e.target; }, true);

function strayClick(node){
  return !!(node && PRESSED && node !== PRESSED && !node.contains(PRESSED));
}

/* ------------------------------------------------------------ more sheet */
function openSheet(){
  var list = $('sheetList');
  list.innerHTML = '';
  NAV.forEach(function(n){
    if (TABS.indexOf(n.v) >= 0) return;         // already on the bar
    var b = el('button');
    b.className = (n.v === CURRENT) ? 'on' : '';
    b.appendChild(el('span','sn', n.name));
    b.appendChild(el('span','sd', n.desc));
    b.onclick = function(){ navTo(n.v); };
    list.appendChild(b);
  });
  $('moreSheet').hidden = false;
  $('sheetClose').focus();
}
function closeSheet(){ $('moreSheet').hidden = true; }

/* ---- the phone drawer ---- */
function openDrawer(){
  document.body.classList.add('drawer-open');
  var s = $('drawerScrim'); if (s) s.hidden = false;
}
function closeDrawer(){
  document.body.classList.remove('drawer-open');
  var s = $('drawerScrim'); if (s) s.hidden = true;
}
$('sheetScrim').onclick = function(){
  if (strayClick($('sheetScrim'))) return;   // the tap that opened it
  closeSheet();
};

/* The drawer's three controls: open it, close it, dismiss it. */
(function(){
  var open = $('menuBtn'), shut = $('drawerClose'), scrim = $('drawerScrim');
  if (open) open.onclick = openDrawer;
  if (shut) shut.onclick = closeDrawer;
  if (scrim) scrim.onclick = function(){
    if (strayClick(scrim)) return;           // the tap that opened it
    closeDrawer();
  };
})();
$('sheetClose').onclick = closeSheet;

/* ---------------------------------------------------------------- toast */
var TOAST_T = null;
function toast(msg){
  var t = $('toast');
  t.textContent = msg; t.hidden = false;
  if (TOAST_T) clearTimeout(TOAST_T);
  TOAST_T = setTimeout(function(){ t.hidden = true; }, 2600);
}

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
  /* Five dashes over the words "no data" is a worse first impression than no
     strip at all, so it stays hidden until the visitor has given it something
     to report. */
  if (!D.attempts.length && !(D.profile && D.profile.exam_date)){
    box.hidden = true;
    return;
  }
  box.hidden = false;
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
  box.appendChild(examReadout(h.days_out));
}

/* The date readout has four states and the old one only had two, so a visitor
   with no date saw a bare dash and a visitor whose date had passed saw a
   negative number counting further into the past. */
function examReadout(days){
  var box = null;
  if (days === null) box = ro('Exam date', '\u2014', 'tap to set');
  else if (days < 0) box = ro('Exam date', 'PAST', 'tap to fix');
  if (box){
    box.classList.add('tappable');
    box.onclick = function(){ navTo('plan'); };
    return box;
  }
  if (days > 1) return ro('Days out', String(days), 'until exam');
  if (days === 1) return ro('Days out', '1', 'exam tomorrow');
  return ro('Exam', 'TODAY', 'good luck');
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
        '<option value="national">National (' + examScored('national') + ' of ' +
          examTotal() + ' exam questions)</option>' +
        '<option value="georgia">Georgia state (' + examScored('georgia') + ' of ' +
          examTotal() + ')</option>' +
        '<option value="mixed">Mixed, exam-weighted</option>' +
        '<option value="comprehensive">Comprehensive subtest (drill)</option></select></div>' +
      '<div><label for="topic">Topic</label><select id="topic"></select></div>' +
      '<div style="max-width:118px"><label for="count">Questions</label><select id="count">' +
        '<option>10</option><option selected>20</option><option>30</option><option>50</option>' +
      '</select></div>' +
    '</div><div class="row" style="margin-top:14px">' +
      '<div style="max-width:215px"><label for="timed">Timer</label><select id="timed">' +
        '<option value="1" selected>Exam pace (' + examPace() + ' s/question)</option>' +
        '<option value="tight">Tight (60 s/question)</option>' +
        '<option value="0">Untimed</option></select></div>' +
      '<div style="max-width:225px"><label for="difficulty">Difficulty</label><select id="difficulty">' +
        '<option value="harder" selected>Harder mix (default)</option>' +
        '<option value="exam">Exam realistic only</option>' +
        '<option value="hard">Hard + exam</option>' +
        '<option value="any">Full bank</option>' +
        '<option value="core">Core only</option></select></div>' +
      '<div style="flex:0 0 auto"><button class="btn" id="start">Start quiz</button></div>' +
      '<div style="flex:0 0 auto"><button class="btn ghost" id="startWeak">Weak-spot quiz</button></div>' +
      '<div style="flex:0 0 auto"><button class="btn ghost" id="startExam">Full mock exam (' + examTotal() + ')</button></div>' +
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
               topic:$('topic').value||null, timed:$('timed').value!=='0',
               spq:paceChosen(), difficulty:$('difficulty').value});
  };
  $('startWeak').onclick = function(){
    startQuiz({portion:$('portion').value, count:+$('count').value,
               weak_spot:true, timed:$('timed').value!=='0',
               spq:paceChosen(), difficulty:$('difficulty').value});
  };
  $('startExam').onclick = function(){
    if (!confirm('Full mock exam: ' + examTotal() + ' questions, ' +
                 hoursPhrase(examMinutes()) + ' at exam pace. Start?')) return;
    startQuiz({mode:'exam', timed:true, difficulty:$('difficulty').value});
  };
  renderHomeWeak();
}

/* Untimed, exam pace, or deliberately tighter than the real thing. */
function paceChosen(){
  var v = $('timed') ? $('timed').value : '1';
  return v === 'tight' ? 60 : null;
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
          limit: opts.timed === false ? 0 : qs.length*(opts.spq || DATA.spq),
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
    '<div class="kbhint"><span>Keyboard:</span><kbd>A</kbd><kbd>B</kbd><kbd>C</kbd>' +
      '<kbd>D</kbd><span>or</span><kbd>1</kbd>&ndash;<kbd>4</kbd><span>to answer, ' +
      '</span><kbd>Enter</kbd><span>for the next one.</span></div>' +
    '<div class="qacts"><button class="btn" id="qnext" disabled>Next</button>' +
      '<button class="btn ghost" id="qquit">End &amp; score</button></div>';
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

var MISSED_CARD = null;
function renderResult(a){
  MISSED_CARD = null;
  var v = $('view-result');
  v.innerHTML = '<h1>Results</h1><div id="resultBody"></div>' +
    '<div class="row" style="margin-top:10px">' +
    '<div style="flex:0 0 auto"><button class="btn" id="againSame">Another quiz</button></div>' +
    '<div style="flex:0 0 auto"><button class="btn ghost" id="againWeak">Drill my weak spots</button></div>' +
    '<div style="flex:0 0 auto"><button class="btn ghost" id="toDash">See dashboard</button></div></div>';
  var box = $('resultBody');
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
    MISSED_CARD = nb;
  }

  $('againSame').onclick = function(){ startQuiz(LAST || {portion:'national', count:20}); };
  $('againWeak').onclick = function(){
    startQuiz({portion:(LAST&&LAST.portion==='math')?'national':((LAST&&LAST.portion)||'national'),
               count:20, weak_spot:true, timed:true});
  };
  $('toDash').onclick = function(){ show('dash'); };

  var head = el('div','card'), g = el('div','grid g3');
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
  if (MISSED_CARD) box.appendChild(MISSED_CARD);

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
      'Practice questions and Vocabulary are open.';
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
    'bank. Recognising a term is easier than recalling it, so use Flashcards too.'));
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

function savedCountLabel(){
  var n = savedList(D).length;
  return n ? (n + (n === 1 ? ' saved lesson' : ' saved lessons')) : null;
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

  /* Where you are, in words, before the title tells you what you are reading. */
  var crumbs = el('nav', 'crumbs');
  var c1 = el('button', 'linkish', 'Lessons');
  c1.onclick = function(){ STUDY_TOPIC = null; renderStudy(); };
  crumbs.appendChild(c1);
  crumbs.appendChild(el('span', 'sep', '/'));
  crumbs.appendChild(el('span', null,
    n.portion === 'georgia' ? 'Georgia portion'
      : (n.portion === 'comprehensive' ? 'Practice topics' : 'National portion')));
  head.appendChild(crumbs);

  var hd = el('div', 'cardhead');
  var left = el('div');
  left.appendChild(el('h1', null, n.label));
  left.appendChild(el('div', 'muted',
    n.counts_on_exam ? ('about ' + n.exam_questions + ' of the ' + examTotal() +
                        ' scored questions come from this topic')
                     : 'A drill topic — not a scored section of the exam'));
  hd.appendChild(left);
  var back = el('button', 'btn mini ghost', 'All lessons');
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
  acts.appendChild(bookmarkButton(n.topic));
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
    'drill. Broad topic quizzes live under Practice questions and Progress.</p>' +
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

/* A page header: title, one line of purpose, optional actions. Every page
   gets the same one, so the eye always lands in the same place. */
function pageHead(title, blurb, actions){
  var h = el('header', 'pagehead');
  var t = el('div', 'ph-text');
  t.appendChild(el('h1', null, title));
  if (blurb) t.appendChild(el('p', 'ph-sub', blurb));
  h.appendChild(t);
  if (actions && actions.length){
    var a = el('div', 'ph-acts');
    actions.forEach(function(x){ a.appendChild(x); });
    h.appendChild(a);
  }
  return h;
}

/* An empty state that says what to do about it rather than apologising. */
function emptyState(title, body, actionLabel, onAction){
  var box = el('div', 'emptystate');
  box.appendChild(el('h3', null, title));
  box.appendChild(el('p', null, body));
  if (actionLabel){
    var b = el('button', 'btn', actionLabel);
    b.onclick = onAction;
    box.appendChild(b);
  }
  return box;
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

  if (p.rolling){
    var had = (D.profile || {}).exam_date;
    var note = el('div','card');
    note.appendChild(cardHead(had ? 'Your exam date has passed' : 'No exam date set',
                              had ? 'was ' + had : 'rolling plan'));
    note.appendChild(el('p','sub', had
      ? 'The schedule below is a rolling four weeks from today instead of a ' +
        'countdown. Put in a new date to pace it properly, or clear the old one ' +
        'and carry on without one.'
      : 'The schedule below runs four weeks from today. Add a date above and it ' +
        'will re-pace itself to the time you actually have.'));
    if (had){
      var wr = el('div','wizacts');
      var clr = el('button','btn ghost', 'Clear the old date');
      clr.onclick = function(){
        D.profile.exam_date = null; D.profile.mastery_date = null;
        persist(); countdown(); renderPlan();
      };
      wr.appendChild(clr);
      note.appendChild(wr);
    }
    box.appendChild(note);
  }

  var head = el('div','card'), g = el('div','grid g3');
  [[p.rolling ? 'Days in this block' : 'Days to exam', String(p.days_to_exam)],
   [p.rolling ? 'Days of study planned' : 'Days to your mastery date',
    String(p.days_to_mastery)],
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
/* ---------------------------------------------------------- account ----
   Only exists behind the paywall build, where there is a server holding the
   account. The static build has no account to show. */
function accountCard(into){
  if (!PAID) return;
  var card = el('div', 'card');
  card.appendChild(cardHead('Your account', 'name, contact and sign-in'));
  var body = el('div'); body.id = 'acctBody';
  body.appendChild(el('p', 'muted', 'Loading\u2026'));
  card.appendChild(body);
  into.insertBefore(card, into.firstChild.nextSibling);

  fetch('/api/account', {credentials: 'same-origin'})
    .then(function(r){ return r.ok ? r.json() : null; })
    .then(function(a){
      if (!a){ body.innerHTML = ''; body.appendChild(el('p', 'muted',
        'Could not load your account just now.')); return; }
      drawAccount(body, a);
    })['catch'](function(){
      body.innerHTML = '';
      body.appendChild(el('p', 'muted', 'Could not reach the server.'));
    });
}

function drawAccount(body, a){
  body.innerHTML = '';

  /* Confirmation that the role took, and nothing more. Everything an
     administrator can actually do is checked on the server; this badge is
     only a readout. */
  if (a.role === 'admin'){
    var who = el('div', 'listrow');
    var whoMain = el('div', 'lr-main');
    whoMain.appendChild(el('div', 'lr-title', 'Administrator'));
    whoMain.appendChild(el('div', 'lr-sub',
      'This account can reach things a studying account cannot.'));
    who.appendChild(whoMain);
    who.appendChild(el('span', 'statuspill ok', 'Admin'));
    body.appendChild(who);
  }

  var em = el('div', 'listrow');
  var emMain = el('div', 'lr-main');
  emMain.appendChild(el('div', 'lr-title', a.email));
  emMain.appendChild(el('div', 'lr-sub', a.verified
    ? 'Email confirmed'
    : 'Email not confirmed yet \u2014 confirm it so you can recover this account'));
  em.appendChild(emMain);
  var badge = el('span', 'statuspill ' + (a.verified ? 'ok' : 'warn'),
                 a.verified ? 'Verified' : 'Unverified');
  em.appendChild(badge);
  body.appendChild(em);

  if (!a.verified){
    var resend = el('button', 'btn mini', 'Send the confirmation email again');
    resend.onclick = function(){
      resend.disabled = true;
      fetch('/api/auth/resend', {method: 'POST', credentials: 'same-origin'})
        .then(function(r){ return r.json().then(function(d){ return {s: r.status, d: d}; }); })
        .then(function(x){
          resend.disabled = false;
          toast(x.d.error || 'Sent. Check your inbox.');
        })['catch'](function(){ resend.disabled = false; toast('Could not send that.'); });
    };
    body.appendChild(resend);
  }

  var form = el('div', 'authform');
  form.style.marginTop = '1rem';
  var nameIn = accountField(form, 'acctName', 'Full name', 'text', 'name', a.name);
  var phoneIn = accountField(form, 'acctPhone', 'Mobile number', 'tel', 'tel', a.phone);
  var note = el('p', 'fieldhint'); note.id = 'acctNote';
  form.appendChild(note);
  var save = el('button', 'btn', 'Save changes');
  save.onclick = function(){
    save.disabled = true; note.className = 'fieldhint'; note.textContent = 'Saving\u2026';
    fetch('/api/account', {method: 'PUT', credentials: 'same-origin',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({name: nameIn.value, phone: phoneIn.value})})
      .then(function(r){ return r.json(); })
      .then(function(d){
        save.disabled = false;
        if (d.fields){
          note.className = 'fielderr';
          note.textContent = d.fields.name || d.fields.phone;
          return;
        }
        note.className = 'fieldhint';
        note.textContent = 'Saved.';
        phoneIn.value = d.phone || '';
      })['catch'](function(){
        save.disabled = false;
        note.className = 'fielderr'; note.textContent = 'Could not save that.';
      });
  };
  form.appendChild(save);
  body.appendChild(form);

  var out = el('button', 'btn ghost', 'Sign out');
  out.style.marginTop = '1rem';
  out.onclick = function(){
    if (!confirm('Sign out on this device? Your progress is saved to your account.')) return;
    fetch('/api/logout', {method: 'POST', credentials: 'same-origin'})
      .then(function(){ location.href = '/'; })['catch'](function(){ location.href = '/'; });
  };
  body.appendChild(out);

  body.appendChild(el('p', 'muted',
    'To change the email address on this account, contact support so we can ' +
    'confirm the new one belongs to you.'));

  passwordBlock(body, a);
  dataBlock(body, a);
}

/* ---- changing the password without leaving the page ------------------- */
function passwordBlock(body, a){
  var wrap = el('details', 'acctfold');
  var sum = el('summary', null, a.hasPassword === false
    ? 'Set a password' : 'Change your password');
  wrap.appendChild(sum);
  var inner = el('div', 'authform');
  var cur = null;
  if (a.hasPassword !== false){
    cur = accountField(inner, 'pwCur', 'Current password', 'password',
                       'current-password', '');
  } else {
    inner.appendChild(el('p', 'fieldhint',
      'You signed in with Google, so there is no current password to confirm. ' +
      'Setting one gives you a second way in.'));
  }
  var a1 = accountField(inner, 'pwNew', 'New password', 'password',
                        'new-password', '');
  var a2 = accountField(inner, 'pwNew2', 'Confirm new password', 'password',
                        'new-password', '');
  var note = el('p', 'fieldhint');
  inner.appendChild(note);
  var go = el('button', 'btn', 'Save the new password');
  go.onclick = function(){
    note.className = 'fieldhint'; note.textContent = 'Saving\u2026';
    go.disabled = true;
    fetch('/api/account/password', {method: 'POST', credentials: 'same-origin',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({current: cur ? cur.value : '',
                            password: a1.value, password2: a2.value})})
      .then(function(r){ return r.json(); })
      .then(function(d){
        go.disabled = false;
        if (d.fields){
          note.className = 'fielderr';
          note.textContent = d.fields.current || d.fields.password || d.fields.password2;
          return;
        }
        if (d.error){ note.className = 'fielderr'; note.textContent = d.error; return; }
        note.className = 'fieldhint';
        note.textContent = 'Saved. Any other device signed in to this account ' +
                           'has been signed out.';
        if (cur) cur.value = '';
        a1.value = ''; a2.value = '';
      })['catch'](function(){
        go.disabled = false;
        note.className = 'fielderr'; note.textContent = 'Could not reach the server.';
      });
  };
  inner.appendChild(go);
  wrap.appendChild(inner);
  body.appendChild(wrap);
}

/* ---- taking it with you, or taking it away ---------------------------- */
function dataBlock(body, a){
  var wrap = el('details', 'acctfold');
  wrap.appendChild(el('summary', null, 'Your data'));
  var inner = el('div');

  inner.appendChild(el('p', 'fieldhint',
    'Download every row this site holds about you \u2014 your details, your ' +
    'progress and your sign-in history \u2014 as a JSON file. Your password is ' +
    'not in it, because it is stored only as a hash and cannot be read back.'));
  var dl = el('button', 'btn ghost', 'Export my data');
  dl.onclick = function(){
    /* A plain navigation, so the browser's own download machinery handles
       the file rather than us building a blob and hoping. */
    location.href = '/api/account/export';
  };
  inner.appendChild(dl);

  inner.appendChild(el('hr', 'acctrule'));
  inner.appendChild(el('h3', 'acctdanger', 'Delete this account'));
  inner.appendChild(el('p', 'fieldhint',
    'This removes your account, your progress and every device you are signed ' +
    'in on. It happens immediately and it cannot be undone. ' +
    (a.paid ? 'It does not refund your payment \u2014 ask for that separately ' +
              'before you delete, because afterwards we cannot match you to it.'
            : '')));
  var form = el('div', 'authform');
  var pw = null;
  if (a.hasPassword !== false){
    pw = accountField(form, 'delPw', 'Your password', 'password',
                      'current-password', '');
  }
  var word = accountField(form, 'delWord', 'Type DELETE to confirm', 'text',
                          'off', '');
  var note = el('p', 'fieldhint');
  form.appendChild(note);
  var go = el('button', 'btn danger', 'Delete my account permanently');
  go.onclick = function(){
    if (!confirm('Delete this account and all of your progress? ' +
                 'This cannot be undone.')) return;
    note.className = 'fieldhint'; note.textContent = 'Deleting\u2026';
    go.disabled = true;
    fetch('/api/account/delete', {method: 'POST', credentials: 'same-origin',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({password: pw ? pw.value : '', confirm: word.value})})
      .then(function(r){ return r.json(); })
      .then(function(d){
        if (d.ok){ location.href = '/?deleted=1'; return; }
        go.disabled = false;
        note.className = 'fielderr';
        note.textContent = (d.fields && (d.fields.password || d.fields.confirm))
                           || d.error || 'Could not delete that.';
      })['catch'](function(){
        go.disabled = false;
        note.className = 'fielderr'; note.textContent = 'Could not reach the server.';
      });
  };
  form.appendChild(go);
  inner.appendChild(form);
  wrap.appendChild(inner);
  body.appendChild(wrap);
}

function accountField(parent, id, label, type, autocomplete, value){
  var wrap = el('div', 'field');
  var l = el('label', null, label); l.setAttribute('for', id);
  wrap.appendChild(l);
  var i = el('input');
  i.id = id; i.type = type; i.autocomplete = autocomplete;
  if (type === 'tel') i.inputMode = 'tel';
  i.value = value || '';
  wrap.appendChild(i);
  parent.appendChild(wrap);
  return i;
}

function renderSetup(){
  var v = $('view-setup');
  /* Two different truths, and saying the wrong one is worse than saying
     nothing. Behind the paywall the account carries the progress and it
     follows you to any device you sign in on. In the free static build
     there is no server, so the browser really is the only copy. */
  var lede = PAID
    ? 'Your progress is saved to your account, so it follows you to any device ' +
      'you sign in on. The export below is for keeping your own copy.'
    : 'Your progress is stored in this browser only, so each device keeps its ' +
      'own history. Use export and import to move it between them.';
  var moveHead = PAID ? 'Keep your own copy' : 'Move progress between devices';
  var moveSub = PAID
    ? 'Export copies your history as text you can paste anywhere. Importing ' +
      'replaces what is on this account, on every device.'
    : 'Export copies your history as text. On the other device, paste it below ' +
      'and choose Import.';
  v.innerHTML =
    '<h1>Setup</h1><p class="sub">' + lede + '</p>' +
    '<div class="card"><h2>' + moveHead + '</h2>' +
      '<p class="muted">' + moveSub + ' <b>Export settings only</b> moves your ' +
      'exam date, study hours and weak areas without the scores.</p>' +
      '<div class="row" style="margin-bottom:12px">' +
        '<div style="flex:0 0 auto"><button class="btn" id="doExport">Export everything</button></div>' +
        '<div style="flex:0 0 auto"><button class="btn ghost" id="doSettings">Export settings only</button></div>' +
        '<div style="flex:0 0 auto"><button class="btn ghost" id="doCopy">Copy to clipboard</button></div>' +
        '<div style="flex:0 0 auto"><button class="btn ghost" id="doImport">Import what is in the box</button></div>' +
      '</div>' +
      '<textarea id="ioBox" rows="7" spellcheck="false" placeholder="Exported progress appears here."></textarea>' +
      '<div class="muted" id="ioNote" style="margin-top:8px"></div></div>' +
    '<div class="card"><h2>Start over</h2>' +
      '<p class="muted">Clears every attempt and score. Your exam date and weak-area ' +
      'choices are kept.' + (PAID ? ' This clears it on your account, so it ' +
      'goes on every device you are signed in on.' : '') + '</p>' +
      '<button class="btn danger" id="doReset">Erase my history</button></div>' +
    '<div class="card"><h2>What is in here</h2><div id="bankBox"></div></div>';

  $('doExport').onclick = function(){
    $('ioBox').value = JSON.stringify(D);
    $('ioNote').textContent = 'Exported ' + D.attempts.length + ' attempts.';
  };
  $('doSettings').onclick = function(){
    var pr = D.profile || {};
    $('ioBox').value = JSON.stringify({profile: {
      exam_date: pr.exam_date || null,
      mastery_date: pr.mastery_date || null,
      hours_per_week: pr.hours_per_week || 8,
      declared_weak: pr.declared_weak || []
    }});
    $('ioNote').textContent = 'Just your exam date, hours and weak areas. Paste ' +
      'this on another device to set it up without copying scores across.';
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
    /* Two shapes are worth accepting: a whole history, and just the four
       settings. Setting up a new phone usually means wanting the second --
       the exam date, the hours and the weak areas -- without dragging one
       device's scores along with it. */
    var settingsOnly = d && !Array.isArray(d.attempts) && d.profile &&
                       typeof d.profile === 'object';
    if (settingsOnly){
      D.profile = D.profile || {};
      ['exam_date', 'mastery_date', 'hours_per_week', 'declared_weak']
        .forEach(function(k){
          if (d.profile[k] !== undefined) D.profile[k] = d.profile[k];
        });
      D.profile.onboarded = true;
      persist(); countdown();
      $('ioNote').textContent = 'Settings restored. The scores on this device ' +
        'were left alone.';
      return;
    }
    if (!d || !Array.isArray(d.attempts)){
      $('ioNote').textContent = 'That does not look like a progress export.'; return;
    }
    if (!confirm('Replace this device’s history with the imported one? ' +
                 'This device currently has ' + D.attempts.length + ' attempts.')) return;
    Object.keys(EMPTY).forEach(function(k){
      if (d[k] === undefined) d[k] = JSON.parse(JSON.stringify(EMPTY[k]));
    });
    if (!d.profile) d.profile = {};
    d.profile.onboarded = true;
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
  accountCard(v);
}

/* ============================================================ app chrome */

/* ---- theme: auto, then whatever the reader overrides it to ---- */
var THEME_KEY = 'ga-prep-theme';
var THEMES = ['auto', 'light', 'dark'];

function systemDark(){
  try { return window.matchMedia('(prefers-color-scheme: dark)').matches; }
  catch(e){ return false; }
}
/* A preference belongs to the person, not the laptop. It rides along in the
   profile so it syncs with everything else, with localStorage as the local
   cache that lets the first paint happen before any of that loads. */
function readTheme(){
  var fromAccount = D && D.profile && D.profile.theme;
  if (THEMES.indexOf(fromAccount) >= 0) return fromAccount;
  var t;
  try { t = localStorage.getItem(THEME_KEY); } catch(e){ t = null; }
  return THEMES.indexOf(t) >= 0 ? t : 'auto';
}
function applyTheme(mode){
  var root = document.documentElement;
  if (mode === 'auto') root.removeAttribute('data-theme');
  else root.setAttribute('data-theme', mode);
  var resolved = (mode === 'auto') ? (systemDark() ? 'dark' : 'light') : mode;
  var b = $('themeBtn');
  if (b){
    b.setAttribute('data-shown', resolved);
    b.title = 'Theme: ' + mode + ' — tap to change';
    $('themeLabel').textContent = mode.charAt(0).toUpperCase() + mode.slice(1);
  }
}
function cycleTheme(){
  var next = THEMES[(THEMES.indexOf(readTheme()) + 1) % THEMES.length];
  try { localStorage.setItem(THEME_KEY, next); } catch(e){}
  D.profile = D.profile || {};
  D.profile.theme = next;
  persist();
  applyTheme(next);
  toast('Theme: ' + next);
}

/* ---- share ---- */
function doShare(){
  var url = location.origin + location.pathname;
  var payload = {title: 'Georgia Real Estate Exam Prep',
                 text: 'Free practice for the Georgia salesperson exam — ' +
                       'no signup, works offline.',
                 url: url};
  if (navigator.share){
    navigator.share(payload)['catch'](function(){});
    return;
  }
  if (navigator.clipboard && navigator.clipboard.writeText){
    navigator.clipboard.writeText(url).then(function(){
      toast('Link copied');
    })['catch'](function(){ prompt('Copy this link:', url); });
    return;
  }
  prompt('Copy this link:', url);
}

/* ---- install to the home screen ---- */
var INSTALL_EVENT = null;
window.addEventListener('beforeinstallprompt', function(e){
  e.preventDefault();
  INSTALL_EVENT = e;
  var b = $('installBtn');
  if (b) b.hidden = false;
});
window.addEventListener('appinstalled', function(){
  INSTALL_EVENT = null;
  var b = $('installBtn');
  if (b) b.hidden = true;
  toast('Installed — open it from your home screen');
});

/* iOS never fires beforeinstallprompt, so say the words instead of hiding it. */
function iosInstallHelp(){
  return 'On iPhone or iPad: tap the Share button in Safari, then ' +
         '"Add to Home Screen".';
}
function isIOS(){
  return /iP(hone|ad|od)/.test(navigator.userAgent) ||
         (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
}
function standalone(){
  try {
    return window.matchMedia('(display-mode: standalone)').matches ||
           navigator.standalone === true;
  } catch(e){ return false; }
}

/* ---- escape closes whatever is open ---- */
document.addEventListener('keydown', function(e){
  if (e.key !== 'Escape') return;
  if (!$('moreSheet').hidden){ closeSheet(); return; }
  if (document.body.classList.contains('drawer-open')){ closeDrawer(); return; }
});

/* 1-4 alongside a-d: people reach for the number row on a numeric question. */
document.addEventListener('keydown', function(e){
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  var n = '1234'.indexOf(e.key || '');
  if (n < 0) return;
  if (VQ && !$('view-vocab').hidden && !VQ.locked){ answerVocab(n, $('view-vocab')); return; }
  if (QUIZ && !$('view-quiz').hidden && !QUIZ.locked &&
      n < QUIZ.qs[QUIZ.i].choices.length){ answer(n); }
});


/* ======================================================================
   The front door.

   For sixteen months this page opened straight onto a dashboard full of
   somebody else's numbers. That is fine for the one person who built it and
   useless for anyone arriving from a link, so first-time visitors get shown
   what this is, what it costs and where their data lives, and are asked the
   two questions the study plan actually needs.
   ====================================================================== */

function totals(){
  var math = 0;
  Object.keys(DATA.math).forEach(function(k){ math += DATA.math[k].q.length; });
  var written = 0;
  Object.keys(DATA.banks).forEach(function(k){ written += DATA.banks[k].length; });
  var terms = 0, topics = Object.keys(DATA.study.topics);
  topics.forEach(function(k){ terms += DATA.study.topics[k].vocab.length; });
  return {written: written, math: math, terms: terms, topics: topics.length,
          total: written + math};
}

function factBox(value, key){
  var d = el('div','fact');
  d.appendChild(el('div','fv', value));
  d.appendChild(el('div','fk', key));
  return d;
}

var WIZ = {step: 0, date: '', hours: 8, weak: [], at: 0, used: false};

function ghostClick(node){
  return (Date.now() - WIZ.at < 300) || strayClick(node);
}

function wizStep(n){
  WIZ.step = n;
  WIZ.at = Date.now();
  WIZ.used = true;                  // distinguishes the wizard from a tile click
  renderWelcome();
  document.body.classList.toggle('landing', n === 0 && !NO_LANDING);
  if ($('appBtn')) $('appBtn').hidden = (n !== 0) || NO_LANDING;
  window.scrollTo(0, 0);
}

function renderWelcome(){
  var v = $('view-welcome');
  v.innerHTML = '';
  if (NO_LANDING && WIZ.step === 0) WIZ.step = 1;   // the front door already did this
  if (WIZ.step === 0) return welcomeIntro(v);
  if (NO_LANDING && WIZ.step === 1){
    var hi = el('div', 'card');
    hi.appendChild(cardHead('You are in', 'two quick questions'));
    hi.appendChild(el('p', 'sub',
      'Everything is unlocked. Answer these and the app paces itself around ' +
      'your test date \u2014 you can change both later under Study plan.'));
    v.appendChild(hi);
  }
  return welcomeWizard(v);
}

var ICONS = {
  quiz:  '<rect x="3.5" y="3.5" width="17" height="17" rx="4"/><path d="M8.6 12.2l2.3 2.4 4.5-5"/>',
  book:  '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5Z"/><path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5"/>',
  math:  '<rect x="4" y="3" width="16" height="18" rx="3"/><path d="M8 8h8M8 12h3M8 16h3M15 12v4M13 14h4"/>',
  cards: '<rect x="3" y="7" width="13" height="13" rx="2.5"/><path d="M7.5 4h11A2.5 2.5 0 0 1 21 6.5v11"/>',
  target:'<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.4"/><path d="M12 1.6v2.6M12 19.8v2.6M22.4 12h-2.6M4.2 12H1.6"/>',
  note:  '<path d="M5 3.5h14v17l-3.2-2.2-3.4 2.2-3.4-2.2L5.8 20.5Z"/><path d="M9 8.5h6M9 12.5h6"/>',
  clock: '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v5.3l3.3 2"/>',
  shield:'<path d="M12 3l7 2.8v5.6c0 4.2-2.9 7.6-7 9.6-4.1-2-7-5.4-7-9.6V5.8Z"/><path d="M9 12.2l2.1 2.2 4-4.4"/>'
};
function iconEl(name){
  var s = el('span', 'ico');
  s.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true">' + (ICONS[name] || '') + '</svg>';
  return s;
}

function lsec(eyebrow, title, blurb){
  var s = el('section', 'lsec');
  var h = el('div', 'lhead');
  if (eyebrow) h.appendChild(el('div', 'eyebrow', eyebrow));
  h.appendChild(el('h2', null, title));
  if (blurb) h.appendChild(el('p', null, blurb));
  s.appendChild(h);
  return s;
}

/* One real question off the bank, rendered the way the quiz renders it. It
   is the most honest thing the page can show: no screenshot, no mockup, the
   actual article. */
function sampleQuestion(){
  var pool = (DATA.banks.national || []).filter(function(q){
    return q.explain && q.explain.length > 90 && q.q.length < 190 &&
           (q.difficulty || 1) >= 2;
  });
  if (!pool.length) pool = DATA.banks.national || [];
  if (!pool.length) return null;
  return pool[Math.floor(Math.random() * pool.length)];
}

function sampleBlock(){
  var q = sampleQuestion();
  if (!q) return null;
  var wrap = el('div', 'sample');
  var top = el('div', 'stop');
  top.appendChild(el('span', null, 'A real question from the bank'));
  top.appendChild(tagFor(q.portion));
  if ((q.difficulty || 1) >= 2){
    var t = el('span', 'tag hard' + ((q.difficulty === 3) ? ' exam' : ''));
    t.textContent = (q.difficulty === 3) ? 'Exam' : 'Hard';
    top.appendChild(t);
  }
  wrap.appendChild(top);

  var body = el('div', 'sbody');
  body.appendChild(el('div', 'sq', q.q));
  var opts = el('div', 'choices');
  var answered = false;
  var buttons = [];
  var hint = null;
  q.choices.forEach(function(text, k){
    var b = el('button', 'choice');
    b.appendChild(el('span', 'k', 'ABCD'[k]));
    b.appendChild(el('span', null, text));
    b.onclick = function(){
      if (answered) return;
      answered = true;
      buttons.forEach(function(x, i){
        x.disabled = true;
        if (i === q.answer) x.classList.add('correct');
        else if (i === k) x.classList.add('wrong');
      });
      var fb = el('div', 'feedback ' + (k === q.answer ? 'ok' : 'no'));
      fb.appendChild(el('div', 'verdict', k === q.answer ? 'Correct' : 'Not quite'));
      fb.appendChild(el('div', null, q.explain));
      if (q.concept){
        var c = el('div', 'concept');
        c.appendChild(el('b', null, 'Concept tested: '));
        c.appendChild(document.createTextNode(q.concept));
        fb.appendChild(c);
      }
      if (hint) hint.hidden = true;   // it has done its job once they pick
      body.appendChild(fb);
      var more = el('div', 'row');
      more.style.marginTop = '.3rem';
      var go = el('button', 'btn', 'Take a full quiz');
      go.onclick = function(){ finishOnboarding('home'); };
      var d = el('div'); d.style.flex = '0 0 auto'; d.appendChild(go);
      more.appendChild(d);
      body.appendChild(more);
    };
    buttons.push(b);
    opts.appendChild(b);
  });
  hint = el('p', 'muted',
    'Pick one — every answer is explained the moment you give it, ' +
    'and it names the concept being tested.');
  body.appendChild(opts);
  body.appendChild(hint);
  wrap.appendChild(body);
  return wrap;
}

function welcomeIntro(v){
  var t = totals();

  /* ------------------------------------------------------------- hero */
  var hero = el('div', 'hero2');
  var w = el('div', 'wrap');
  w.appendChild(el('div', 'kicker2', 'Free · No signup · Georgia salesperson licence'));
  var h1 = el('h1');
  h1.appendChild(document.createTextNode('Pass the Georgia real estate exam. '));
  h1.appendChild(el('em', null, 'Free.'));
  w.appendChild(h1);
  w.appendChild(el('p', 'lede2',
    'Practice questions written to the real blueprint and scored the way the ' +
    'real exam scores you — National and Georgia separately, 75% needed on ' +
    'each. Everything is explained, nothing is locked, and it works with no signal.'));

  var cta = el('div', 'cta2');
  var go = el('button', 'btn', 'Start studying');
  go.onclick = function(){ wizStep(1); };
  cta.appendChild(go);
  var see = el('button', 'btn ghost', 'Try a question first');
  see.onclick = function(){
    var s = document.getElementById('sampleAnchor');
    if (s) s.scrollIntoView({behavior: 'smooth', block: 'start'});
  };
  cta.appendChild(see);
  w.appendChild(cta);
  w.appendChild(el('p', 'fineprint',
    'No account, no card, no ads. Your answers never leave your device.'));
  hero.appendChild(w);

  var band = el('div', 'statband');
  [[String(t.total), 'practice questions'], [String(t.terms), 'terms defined'],
   [String(t.topics), 'topics covered'], ['$0', 'now and always']]
    .forEach(function(r){
      var d = el('div');
      d.appendChild(el('div', 'n', r[0]));
      d.appendChild(el('div', 'l', r[1]));
      band.appendChild(d);
    });
  hero.appendChild(band);
  v.appendChild(hero);

  /* --------------------------------------------------------- the goods */
  var s1 = lsec('What you get', 'Six things, and all of them are free.',
    'Open any of them now — you can set your exam date later, or never.');
  var tiles = el('div', 'tiles');
  [['quiz', 'Practice quizzes', 'Timed sets that mirror the real split, scored ' +
    'National and Georgia separately because that is how you pass or fail.', 'home'],
   ['book', 'Study notes', t.terms + ' terms defined in plain sentences, with a ' +
    'short check-yourself quiz after every section.', 'study'],
   ['math', 'Math, worked out', 'Every calculation broken into steps you can ' +
    'follow — prorations, commissions, points, loan-to-value, area.', 'math'],
   ['cards', 'Vocabulary drill', 'You read the definition and name the term. ' +
    'Categories unlock as you pass them.', 'vocab'],
   ['target', 'Weak-spot targeting', 'The narrow sub-topics dragging your score ' +
    'down, each with its own drill.', 'weak'],
   ['note', 'Your notebook', 'Every question you get wrong, kept with the right ' +
    'answer and the reason, until you stop getting it wrong.', 'notebook']
  ].forEach(function(r){
    var b = el('button', 'tile');
    b.appendChild(iconEl(r[0]));
    b.appendChild(el('h3', null, r[1]));
    b.appendChild(el('p', null, r[2]));
    b.appendChild(el('div', 'go', 'Open →'));
    b.onclick = function(){ finishOnboarding(r[3]); };
    tiles.appendChild(b);
  });
  s1.appendChild(tiles);
  v.appendChild(s1);

  /* ------------------------------------------------------- the article */
  var s2 = lsec('See for yourself', 'Here is one, right now.',
    'No screenshots and no sales pitch — this is pulled live from the ' +
    'question bank, at the difficulty the real thing is written to.');
  s2.id = 'sampleAnchor';
  var sample = sampleBlock();
  if (sample) s2.appendChild(sample);
  v.appendChild(s2);

  /* --------------------------------------------------------- blueprint */
  var s3 = lsec('What is on the exam', 'The whole blueprint, weighted.',
    'Georgia scores the two portions separately and you must clear 75% on each. ' +
    'A strong average will not save a weak half, so this app tracks them apart.');
  var bp = el('div', 'blueprint');
  [['national', 'National portion', DATA.exam.national],
   ['georgia', 'Georgia portion', DATA.exam.georgia]].forEach(function(r){
    var col = el('div', 'bpcol');
    var h = el('h3');
    h.appendChild(document.createTextNode(r[1]));
    h.appendChild(el('span', null, r[2] + ' questions'));
    col.appendChild(h);
    DATA.topics.filter(function(x){ return x.portion === r[0]; })
      .sort(function(a, b){ return b.exam_questions - a.exam_questions; })
      .forEach(function(x){
        var row = el('div', 'bprow');
        row.appendChild(el('b', null, x.label));
        row.appendChild(el('i', null, String(x.exam_questions)));
        col.appendChild(row);
      });
    bp.appendChild(col);
  });
  s3.appendChild(bp);
  v.appendChild(s3);

  /* --------------------------------------------------------- how it works */
  var s4 = lsec('How it works', 'Read it, quiz it, hunt down what is left.',
    'The app decides what you do next so you are not the one choosing, ' +
    'which is where most study time gets lost.');
  var st = el('div', 'steps3');
  [['01', 'Read it once', 'Notes for every topic on the blueprint, in plain ' +
    'sentences, with a short quiz after each section so it sticks the first time.'],
   ['02', 'Quiz until it holds', 'Timed sets at the real difficulty. Every answer ' +
    'tells you why it is right and names the concept being tested.'],
   ['03', 'Attack the gaps', 'Anything you miss lands in the Notebook and on the ' +
    'flashcard deck, and comes back until it stops being a gap.']
  ].forEach(function(r){
    var c = el('div', 'step3');
    c.appendChild(el('div', 'sno', r[0]));
    c.appendChild(el('h3', null, r[1]));
    c.appendChild(el('p', null, r[2]));
    st.appendChild(c);
  });
  s4.appendChild(st);
  v.appendChild(s4);

  /* --------------------------------------------------------------- faq */
  var s5 = lsec('Before you ask', 'The honest answers.', null);
  var faq = el('div', 'faq');
  [['Is it actually free?',
    'Yes, and there is nothing to upgrade to. No account, no card, no ads, no ' +
    'trial that runs out. It was built by one person studying for this exam and ' +
    'kept online afterwards because it worked.'],
   ['Where do the Georgia rules come from?',
    'The Georgia Real Estate Commission’s own InfoBase and the Georgia Code, ' +
    'read chapter by chapter, rather than a commercial cram guide. That matters ' +
    'where the guides are wrong — continuing education in Georgia is 24 hours ' +
    'per four-year renewal, not the 36 that national study guides tend to quote.'],
   ['Does it work on my phone?',
    'It is built for one. Open it in your browser and add it to your home screen ' +
    'and it behaves like an app, including with no signal — the whole question ' +
    'bank is already on the device.'],
   ['Where do my scores go?',
    'Into your browser on that device, and nowhere else. There is no server, no ' +
    'account and no analytics. The flip side is that clearing your browser data ' +
    'clears your history, so there is an export under Your data.'],
   ['Is this official?',
    'No. It is not affiliated with, endorsed by, or connected to the Georgia Real ' +
    'Estate Commission, PSI, or any school. It is practice material and not legal ' +
    'advice, and it is no substitute for the 75-hour pre-licence course Georgia ' +
    'requires before you may sit the exam.']
  ].forEach(function(r){
    var d = el('details');
    var sm = el('summary'); sm.appendChild(document.createTextNode(r[0]));
    d.appendChild(sm);
    d.appendChild(el('p', null, r[1]));
    faq.appendChild(d);
  });
  s5.appendChild(faq);
  v.appendChild(s5);

  /* --------------------------------------------------------- last word */
  var end = el('div', 'endcta');
  end.appendChild(el('h2', null, 'Start with one quiz.'));
  end.appendChild(el('p', null,
    'Twenty questions takes about fifteen minutes and tells you more about ' +
    'where you stand than a week of reading will.'));
  var eb = el('button', 'btn', 'Set up my plan — 20 seconds');
  eb.onclick = function(){ wizStep(1); };
  end.appendChild(eb);
  var skip = el('button', 'btn mini ghost', 'or skip straight to a quiz');
  skip.style.cssText = 'background:transparent;border-color:transparent;' +
                       'color:inherit;opacity:.85;text-decoration:underline';
  skip.onclick = function(){ finishOnboarding('home'); };
  end.appendChild(skip);
  v.appendChild(end);
}

function wizDots(n){
  var d = el('div','wizdots');
  for (var i = 1; i <= 2; i++) d.appendChild(el('i', i <= n ? 'on' : ''));
  var t = el('span','muted', 'Step ' + n + ' of 2');
  d.appendChild(t);
  return d;
}

function welcomeWizard(v){
  var card = el('div','card wiz');
  card.appendChild(wizDots(WIZ.step));

  if (WIZ.step === 1){
    card.appendChild(el('h1', null, 'When do you sit the exam?'));
    card.appendChild(el('p','sub',
      'This sets the pace of your study plan and the countdown in the header. ' +
      'You can change it any time, and you can leave it blank.'));

    var row = el('div','row');
    var d1 = el('div');
    var l1 = el('label', null, 'Exam date'); l1.setAttribute('for','wizDate');
    d1.appendChild(l1);
    var inp = el('input'); inp.type = 'date'; inp.id = 'wizDate'; inp.value = WIZ.date;
    d1.style.maxWidth = '260px';
    var today = new Date(); today.setHours(0,0,0,0);
    inp.min = today.toISOString().slice(0,10);
    inp.onchange = function(){ WIZ.date = inp.value; };
    d1.appendChild(inp);
    row.appendChild(d1);

    var d2 = el('div'); d2.style.maxWidth = '180px';
    var l2 = el('label', null, 'Hours a week you can study');
    l2.setAttribute('for','wizHours');
    d2.appendChild(l2);
    var hrs = el('input'); hrs.type = 'number'; hrs.id = 'wizHours';
    hrs.min = '1'; hrs.max = '40'; hrs.value = String(WIZ.hours);
    hrs.onchange = function(){ WIZ.hours = +hrs.value || 8; };
    d2.appendChild(hrs);
    row.appendChild(d2);
    card.appendChild(row);

    var acts = el('div','wizacts');
    var next = el('button','btn', 'Next');
    next.onclick = function(){ WIZ.date = inp.value; WIZ.hours = +hrs.value || 8;
                               wizStep(2); };
    acts.appendChild(next);
    var none = el('button','btn ghost', 'Not booked yet');
    none.onclick = function(){ WIZ.date = ''; wizStep(2); };
    acts.appendChild(none);
    if (!NO_LANDING){
      acts.appendChild(el('span','spacer'));
      var back = el('button','btn mini ghost', 'Back');
      back.onclick = function(){ wizStep(0); };
      acts.appendChild(back);
    }
    card.appendChild(acts);
    v.appendChild(card);
    return;
  }

  card.appendChild(el('h1', null, 'Which parts worry you most?'));
  card.appendChild(el('p','sub',
    'Whatever you tick gets pushed to the front of your plan and into the ' +
    'weak-spot drill from day one, before you have taken a single quiz. ' +
    'Guessing is fine — your actual scores take over as soon as you start.'));

  ['national','georgia'].forEach(function(portion){
    var rows = DATA.topics.filter(function(t){ return t.portion === portion; });
    if (!rows.length) return;
    var h = el('div','eyebrow', portion === 'georgia'
      ? 'Georgia portion · 52 questions' : 'National portion · 80 questions');
    h.style.marginTop = '.6rem';
    card.appendChild(h);
    var grid = el('div','pickgrid');
    rows.forEach(function(t){
      var b = el('button','opt' + (WIZ.weak.indexOf(t.key) >= 0 ? ' on' : ''));
      b.appendChild(el('span','box', '✓'));
      var txt = el('span');
      txt.appendChild(el('span','pn', t.label));
      txt.appendChild(el('span','pd', t.exam_questions + ' questions on the exam'));
      b.appendChild(txt);
      b.setAttribute('aria-pressed', WIZ.weak.indexOf(t.key) >= 0 ? 'true' : 'false');
      b.onclick = function(){
        if (ghostClick(b)) return;
        var at = WIZ.weak.indexOf(t.key);
        if (at >= 0) WIZ.weak.splice(at, 1); else WIZ.weak.push(t.key);
        b.classList.toggle('on', at < 0);
        b.setAttribute('aria-pressed', at < 0 ? 'true' : 'false');
      };
      grid.appendChild(b);
    });
    card.appendChild(grid);
  });

  var acts2 = el('div','wizacts');
  acts2.style.marginTop = '.4rem';
  var done = el('button','btn', 'Start studying');
  done.onclick = function(){ if (ghostClick(done)) return; finishOnboarding('today'); };
  acts2.appendChild(done);
  var dunno = el('button','btn ghost', 'Not sure yet');
  dunno.onclick = function(){ if (ghostClick(dunno)) return; WIZ.weak = []; finishOnboarding('today'); };
  acts2.appendChild(dunno);
  acts2.appendChild(el('span','spacer'));
  var back2 = el('button','btn mini ghost', 'Back');
  back2.onclick = function(){ wizStep(1); };
  acts2.appendChild(back2);
  card.appendChild(acts2);
  v.appendChild(card);
}

function finishOnboarding(goto){
  D.profile = D.profile || {};
  D.profile.onboarded = true;

  /* Only the wizard gets to write settings. Opening a tile from the home page
     also lands here, and it used to save its untouched defaults over whatever
     was already there -- eight hours a week on top of a saved ten. */
  if (WIZ.used){
    if (WIZ.date){
      D.profile.exam_date = WIZ.date;
      // aim to be done a few days early; that gap is where revision happens
      var m = new Date(WIZ.date + 'T00:00:00');
      m.setDate(m.getDate() - 5);
      var start = new Date(); start.setHours(0,0,0,0);
      D.profile.mastery_date = (m > start) ? m.toISOString().slice(0,10) : WIZ.date;
    }
    if (WIZ.hours) D.profile.hours_per_week = WIZ.hours;
    if (WIZ.weak.length) D.profile.declared_weak = WIZ.weak.slice();
  }
  WIZ.step = 0; WIZ.used = false;
  persist();
  countdown();
  show(goto || 'today');
}

/* ------------------------------------------------------------------ about */
function renderAbout(){
  var v = $('view-about'), t = totals();
  v.innerHTML = '';
  v.appendChild(el('h1', null, 'About this site'));
  v.appendChild(el('p','sub', PAID
    ? 'A study tool for the Georgia real estate salesperson licensing exam, ' +
      'built by one person preparing for that exam and kept going afterwards ' +
      'because it worked. You bought it once; it is yours.'
    : 'A free, open study tool for the Georgia real estate salesperson licensing ' +
      'exam. It was built by one person preparing for that exam, and kept online ' +
      'afterwards because it worked.'));

  var what = el('div','card');
  what.appendChild(cardHead('What is in it', 'built ' + BUILD));
  var wrap = el('div','scroll'), tab = el('table');
  tab.innerHTML = '<tr><th>Section</th><th class="num">Size</th></tr>';
  [['Written exam-style questions', t.written],
   ['Generated math problems, each with worked steps', t.math],
   ['Topics with full study notes', t.topics],
   ['Vocabulary terms defined', t.terms]].forEach(function(r){
    var tr = el('tr');
    tr.appendChild(el('td', null, r[0]));
    tr.appendChild(el('td','num', String(r[1])));
    tab.appendChild(tr);
  });
  wrap.appendChild(tab); what.appendChild(wrap);
  v.appendChild(what);

  var src = el('div','card');
  src.appendChild(cardHead('Where the Georgia material comes from', 'sourcing'));
  src.appendChild(el('p','sub',
    'The Georgia rules in these notes were taken from the Georgia Real Estate ' +
    'Commission’s own InfoBase and from the Georgia Code, chapter by ' +
    'chapter, rather than from a commercial cram guide. That matters in places ' +
    'where the guides get it wrong — continuing education, for one, is 24 ' +
    'hours per four-year renewal in Georgia, not the 36 that national study ' +
    'guides tend to quote.'));
  src.appendChild(el('p','sub',
    'The national half follows the standard content outline used by the ' +
    'licensing exams: agency, contracts, financing, valuation, property ' +
    'ownership, transfer of title, practice and disclosures, and the maths.'));
  v.appendChild(src);

  var warn = el('div','card');
  warn.appendChild(cardHead('What this is not', 'read this bit'));
  var ul = el('ul'); ul.className = 'plainlist';
  ['Not affiliated with, endorsed by, or connected to the Georgia Real Estate ' +
   'Commission, PSI, or any school or exam vendor.',
   'Not legal advice, and not an official statement of Georgia law. Rules ' +
   'change; grec.state.ga.us is the authority, not this page.',
   'Not a substitute for the 75-hour pre-licence course Georgia requires before ' +
   'you may sit the exam.',
   (PAID ? 'Not a guarantee of anything. You bought practice material, and ' +
           'practice is only worth what you put into it.'
         : 'Not a guarantee of anything. It is practice, and practice is ' +
           'only worth what you put into it.')].forEach(function(x){
    ul.appendChild(el('li', null, x));
  });
  warn.appendChild(ul);
  v.appendChild(warn);

  var priv = el('div','card');
  priv.appendChild(cardHead('Privacy', PAID ? 'your email, and nothing else'
                                            : 'short version: none collected'));
  priv.appendChild(el('p','sub', PAID
    ? 'Your email address and your study progress, and nothing else. No name, ' +
      'no tracking, no advertising, no analytics. Card details are handled ' +
      'entirely by Stripe and never touch this site. Progress is stored against ' +
      'your account so it follows you between devices, and a copy is kept in ' +
      'this browser so the app keeps working with no signal.'
    : 'There is no account, no server and no analytics. Your answers and scores ' +
      'are written to this browser’s local storage and never leave the ' +
      'device. The page loads two font files from Google Fonts; everything else ' +
      '— every question, every note — is inside the page you already ' +
      'downloaded, which is why it keeps working with no signal.'));
  var go = el('button','btn ghost');
  go.textContent = 'Export or erase my data';
  go.onclick = function(){ navTo('setup'); };
  priv.appendChild(go);
  v.appendChild(priv);

  var sh = el('div','card');
  if (PAID){
    sh.appendChild(cardHead('Your account', 'signed in'));
    sh.appendChild(el('p','sub',
      'Your progress is saved against your account, so signing in on another ' +
      'device picks up exactly where you left off.'));
    var out = el('button','btn ghost');
    out.textContent = 'Sign out';
    out.onclick = function(){
      if (!confirm('Sign out on this device? Your progress is saved.')) return;
      fetch('/api/logout', {method: 'POST', credentials: 'same-origin'})
        .then(function(){ location.href = '/'; })['catch'](function(){ location.href = '/'; });
    };
    sh.appendChild(out);
  } else {
    sh.appendChild(cardHead('Pass it on', 'if it helped'));
    sh.appendChild(el('p','sub',
      'Someone in your pre-licence class is studying from a photocopy right ' +
      'now. This is free and there is nothing to sign up for.'));
    var b2 = el('button','btn');
    b2.textContent = 'Share this site';
    b2.onclick = doShare;
    sh.appendChild(b2);
  }
  v.appendChild(sh);
}

/* ----------------------------------------------------------------- boot */
(function(){
  applyTheme(readTheme());
  try {
    window.matchMedia('(prefers-color-scheme: dark)')
      .addEventListener('change', function(){
        if (readTheme() === 'auto') applyTheme('auto');
      });
  } catch(e){}

  $('themeBtn').onclick = cycleTheme;
  $('shareBtn').onclick = doShare;
  $('brand').onclick = function(){
    if (FRONTDOOR){ location.href = FRONTDOOR; return; }
    navTo(onboarded(D) ? 'today' : 'welcome');
  };
  $('installBtn').onclick = function(){
    if (INSTALL_EVENT){ INSTALL_EVENT.prompt(); INSTALL_EVENT = null; return; }
    alert(iosInstallHelp());
  };
  if (isIOS() && !standalone()) $('installBtn').hidden = false;

  var recovered = backfillMisses(D);
  if (recovered) persist();

  var t = totals();
  var hard = 0, exam = 0;
  Object.keys(DATA.banks).forEach(function(k){
    hard += DATA.banks[k].filter(function(r){ return r.difficulty === 2; }).length;
    exam += DATA.banks[k].filter(function(r){ return r.difficulty === 3; }).length;
  });
  $('bankcount').textContent = t.written + ' questions (' + hard + ' hard, ' + exam +
    ' exam-realistic) + ' + t.math +
    ' math problems + study notes on ' + t.topics + ' topics (' + t.terms + ' terms)';

  countdown();
  loadAccount();
  show(routeFromHash(), true);

  if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0){
    window.addEventListener('load', function(){
      navigator.serviceWorker.register('sw.js')['catch'](function(){});
    });
  }
})();

/* ====================================================================== */
/* Bookmarks.                                                             */
/*                                                                        */
/* A lesson you meant to come back to. Saved against the account, so it is */
/* there on the next device, and empty until you save something -- which   */
/* the empty state says plainly rather than pretending to be a feature.    */
/* ====================================================================== */

function bookmarkButton(topicKey, onChange){
  var b = el('button', 'bookmark' + (isSaved(D, topicKey) ? ' on' : ''));
  function paint(){
    var on = isSaved(D, topicKey);
    b.className = 'bookmark' + (on ? ' on' : '');
    b.setAttribute('aria-pressed', on ? 'true' : 'false');
    b.title = on ? 'Remove bookmark' : 'Save this lesson for later';
    b.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true">' +
      '<path d="M6 3.5h12v17l-6-4.2-6 4.2Z" fill="' + (on ? 'currentColor' : 'none') +
      '" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>' +
      '<span>' + (on ? 'Saved' : 'Save') + '</span>';
  }
  paint();
  b.onclick = function(e){
    e.stopPropagation();
    toggleSaved(D, topicKey);
    persist();
    paint();
    toast(isSaved(D, topicKey) ? 'Saved to bookmarks' : 'Removed from bookmarks');
    if (onChange) onChange();
  };
  return b;
}

function renderSaved(){
  var v = $('view-saved');
  v.innerHTML = '';
  v.appendChild(pageHead('Bookmarks',
    'Lessons you saved to come back to. They stay on your account.'));

  var rows = savedList(D);
  if (!rows.length){
    var box = el('div', 'card');
    box.appendChild(emptyState(
      'No bookmarks yet',
      'Open a lesson and choose Save to keep it here. Useful for the handful ' +
      'of topics you know you will need to read twice.',
      'Browse lessons', function(){ navTo('study'); }));
    v.appendChild(box);
    return;
  }

  var card = el('div', 'card');
  card.appendChild(cardHead('Saved lessons',
                            rows.length + (rows.length === 1 ? ' lesson' : ' lessons')));
  var list = el('div', 'rowlist');
  rows.forEach(function(r){
    var row = el('div', 'listrow');
    var who = el('div', 'lr-main');
    var nm = el('div', 'lr-title');
    nm.appendChild(document.createTextNode(r.label));
    nm.appendChild(tagFor(r.portion));
    who.appendChild(nm);
    who.appendChild(el('div', 'lr-sub',
      countsOnExam(r.key) ? (r.weight + ' questions on the exam')
                          : 'Practice topic, not a section of the exam'));
    row.appendChild(who);

    var acts = el('div', 'lr-acts');
    var open = el('button', 'btn mini', 'Open lesson');
    open.onclick = function(){ STUDY_TOPIC = r.key; navTo('study'); };
    acts.appendChild(open);
    acts.appendChild(bookmarkButton(r.key, renderSaved));
    row.appendChild(acts);
    list.appendChild(row);
  });
  card.appendChild(list);
  v.appendChild(card);
}

/* ======================================================================
   Who you are, and what that lets you see.

   ACCOUNT is filled from /api/me once at boot. Nothing here decides
   permission -- the server does that on every request. This only decides
   what is worth putting on screen, and hiding a button is not security.
   ====================================================================== */

var ACCOUNT = null;

function initials(name, email){
  var n = (name || '').trim();
  if (n){
    var parts = n.split(/\s+/);
    return (parts[0][0] + (parts.length > 1 ? parts[parts.length - 1][0] : '')).toUpperCase();
  }
  return (email || '?').slice(0, 2).toUpperCase();
}

function loadAccount(){
  if (!PAID) return;                       // the static build has no account
  fetch('/api/me', {credentials: 'same-origin'})
    .then(function(r){ return r.ok ? r.json() : null; })
    .then(function(me){
      if (!me || !me.signedIn) return;
      ACCOUNT = me;
      paintProfile();
      if (me.role === 'admin') revealAdmin();
    })['catch'](function(){});
}

function paintProfile(){
  var box = $('profile');
  if (!box || !ACCOUNT) return;
  box.hidden = false;
  $('profileInitials').textContent = initials(ACCOUNT.name, ACCOUNT.email);
  $('profileName').textContent = ACCOUNT.name || ACCOUNT.email;

  var menu = $('profileMenu');
  menu.innerHTML = '';
  var head = el('div', 'pm-head');
  head.appendChild(el('div', 'pm-name', ACCOUNT.name || 'Your account'));
  head.appendChild(el('div', 'pm-email', ACCOUNT.email));
  if (ACCOUNT.role === 'admin'){
    head.appendChild(el('span', 'statuspill ok pm-role', 'Administrator'));
  } else if (!ACCOUNT.verified){
    head.appendChild(el('span', 'statuspill warn pm-role', 'Email unconfirmed'));
  }
  menu.appendChild(head);

  function item(label, fn, cls){
    var b = el('button', cls || '', label);
    b.setAttribute('role', 'menuitem');
    b.onclick = function(){ closeProfile(); fn(); };
    menu.appendChild(b);
  }
  if (ACCOUNT.role === 'admin'){
    item('Admin overview', function(){ navTo('admin'); });
    item('Users', function(){ navTo('users'); });
  }
  item('Account settings', function(){ navTo('setup'); });
  item('Sign out', function(){
    if (!confirm('Sign out on this device? Your progress is saved.')) return;
    fetch('/api/logout', {method: 'POST', credentials: 'same-origin'})
      .then(function(){ location.href = '/'; })['catch'](function(){ location.href = '/'; });
  }, 'danger');

  var btn = $('profileBtn');
  btn.onclick = function(e){
    e.stopPropagation();
    menu.hidden ? openProfile() : closeProfile();
  };
}

function openProfile(){
  $('profileMenu').hidden = false;
  $('profileBtn').setAttribute('aria-expanded', 'true');
}
function closeProfile(){
  var m = $('profileMenu');
  if (m) m.hidden = true;
  var b = $('profileBtn');
  if (b) b.setAttribute('aria-expanded', 'false');
}
document.addEventListener('click', function(e){
  var box = $('profile');
  if (box && !box.contains(e.target)) closeProfile();
});
document.addEventListener('keydown', function(e){
  if (e.key === 'Escape') closeProfile();
});

function revealAdmin(){
  document.querySelectorAll('.adminonly').forEach(function(n){ n.hidden = false; });
  document.querySelectorAll('#rail button.adminonly').forEach(function(b){
    b.onclick = function(){ navTo(b.dataset.view); };
  });
}

/* ------------------------------------------------------------- admin ---- */

function adminFetch(path, into, draw){
  into.innerHTML = '';
  into.appendChild(el('p', 'muted', 'Loading…'));
  fetch(path, {credentials: 'same-origin'})
    .then(function(r){
      if (r.status === 403){ throw new Error('This account is not an administrator.'); }
      if (!r.ok) throw new Error('Could not load that.');
      return r.json();
    })
    .then(function(d){ into.innerHTML = ''; draw(d); })
    ['catch'](function(e){
      into.innerHTML = '';
      into.appendChild(el('p', 'muted', e.message));
    });
}

function when(ts){
  if (!ts) return '—';
  var d = new Date(ts * 1000);
  return d.toISOString().slice(0, 10);
}

function renderAdmin(){
  var v = $('view-admin');
  v.innerHTML = '';
  v.appendChild(pageHead('Admin overview',
    'Everything on this page is visible only to administrators, and is ' +
    'checked on the server rather than hidden in the interface.'));
  var card = el('div', 'card');
  card.appendChild(cardHead('Accounts', 'all time'));
  var body = el('div');
  card.appendChild(body);
  v.appendChild(card);

  adminFetch('/api/admin/stats', body, function(d){
    var grid = el('div', 'adminstats');
    [[d.total, 'total accounts'],
     [d.last7, 'signed up this week'],
     [d.last30, 'signed up this month'],
     [d.paid, 'have paid'],
     [d.verified, 'confirmed their email'],
     [d.activeLast7, 'studied this week']
    ].forEach(function(r){
      var c = el('div', 'astat');
      c.appendChild(el('div', 'n', String(r[0])));
      c.appendChild(el('div', 'l', r[1]));
      grid.appendChild(c);
    });
    body.appendChild(grid);
    var go = el('button', 'btn ghost', 'See every account');
    go.style.marginTop = '1rem';
    go.onclick = function(){ navTo('users'); };
    body.appendChild(go);
  });
}

var USER_QUERY = '';

function renderUsers(){
  var v = $('view-users');
  v.innerHTML = '';
  v.appendChild(pageHead('Users', 'Everyone who has created an account.'));

  var card = el('div', 'card');
  var row = el('div', 'searchrow');
  var q = el('input');
  q.type = 'search'; q.placeholder = 'Search name or email'; q.value = USER_QUERY;
  row.appendChild(q);
  var find = el('button', 'btn mini', 'Search');
  find.onclick = function(){ USER_QUERY = q.value.trim(); load(); };
  q.onkeydown = function(e){ if (e.key === 'Enter') find.click(); };
  row.appendChild(find);
  if (USER_QUERY){
    var clear = el('button', 'btn mini ghost', 'Clear');
    clear.onclick = function(){ USER_QUERY = ''; renderUsers(); };
    row.appendChild(clear);
  }
  card.appendChild(row);
  var body = el('div');
  card.appendChild(body);
  v.appendChild(card);

  function load(){
    adminFetch('/api/admin/users?limit=200' +
               (USER_QUERY ? '&q=' + encodeURIComponent(USER_QUERY) : ''),
               body, function(d){
      if (!d.users.length){
        body.appendChild(emptyState(
          USER_QUERY ? 'Nobody matches that' : 'No accounts yet',
          USER_QUERY ? 'Try a different name or email address.'
                     : 'Accounts appear here as soon as people sign up.'));
        return;
      }
      body.appendChild(el('p', 'muted',
        d.total + (d.total === 1 ? ' account' : ' accounts') +
        (USER_QUERY ? ' matching "' + USER_QUERY + '"' : '')));
      var wrap = el('div', 'scroll'), t = el('table', 'usertable');
      t.innerHTML = '<tr><th>Name</th><th>Email</th><th>Joined</th>' +
                    '<th>Last studied</th><th>Status</th></tr>';
      d.users.forEach(function(u){
        var tr = el('tr');
        var who = el('td', 'who');
        who.appendChild(el('div', null, u.name || '—'));
        if (u.phone) who.appendChild(el('div', 'uemail', u.phone));
        tr.appendChild(who);
        var em = el('td');
        em.appendChild(el('div', 'uemail', u.email));
        tr.appendChild(em);
        tr.appendChild(el('td', null, when(u.created_at)));
        tr.appendChild(el('td', null, when(u.last_active)));
        var st = el('td');
        if (u.role === 'admin') st.appendChild(el('span', 'statuspill ok', 'Admin'));
        else if (u.paid) st.appendChild(el('span', 'statuspill ok', 'Paid'));
        else st.appendChild(el('span', 'statuspill warn',
                               u.verified ? 'Free' : 'Unconfirmed'));
        tr.appendChild(st);
        t.appendChild(tr);
      });
      wrap.appendChild(t);
      body.appendChild(wrap);
    });
  }
  load();
}
