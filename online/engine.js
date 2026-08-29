/* Engine: storage, question selection, scoring, and the study planner.
   A port of greprep/{store,questions,scheduler}.py -- same rules, no server. */
'use strict';

var KEY = 'ga-prep-v1';
var EXAM = DATA.exam;                       // {national:80, georgia:52}
var TOTAL_Q = EXAM.national + EXAM.georgia;

var TOPIC = {};                             // key -> catalog row
DATA.topics.forEach(function(t){ TOPIC[t.key] = t; });
var ORDER = DATA.topics.map(function(t){ return t.key; });

function label(k){ return (TOPIC[k] || {}).label || k; }
function weight(k){ return (TOPIC[k] || {}).exam_questions || 1; }
function portionTopics(p){
  return ORDER.filter(function(k){ return TOPIC[k].portion === p; });
}
var PRACTICE_ONLY = {};
(DATA.practice_only || []).forEach(function(k){ PRACTICE_ONLY[k] = 1; });
var HARDER_SHARE = DATA.harder_share || 0.65;
var DIFFICULTIES = DATA.difficulties || ['harder','any','core','hard'];
var CLOSING_GENS = Object.keys(DATA.math).filter(function(k){ return DATA.math[k].closing; });
function countsOnExam(k){ return !PRACTICE_ONLY[k]; }

/* ------------------------------------------------------------- storage */
var EMPTY = {version:1, profile:{}, attempts:[], topics:{}, subs:{}, items:{}, generators:{}};

function load(){
  var raw;
  try { raw = localStorage.getItem(KEY); } catch(e){ raw = null; }
  if (!raw){
    var fresh = JSON.parse(JSON.stringify(EMPTY));
    // first run on this device: start from the exam settings baked in at build time
    fresh.profile = JSON.parse(JSON.stringify(DATA.profile_default || {}));
    return fresh;
  }
  var d;
  try { d = JSON.parse(raw); } catch(e){ return JSON.parse(JSON.stringify(EMPTY)); }
  Object.keys(EMPTY).forEach(function(k){
    if (d[k] === undefined) d[k] = JSON.parse(JSON.stringify(EMPTY[k]));
  });
  if (!d.profile || !d.profile.exam_date)
    d.profile = JSON.parse(JSON.stringify(DATA.profile_default || {}));
  return d;
}
function save(d){
  try { localStorage.setItem(KEY, JSON.stringify(d)); return true; }
  catch(e){
    alert('Could not save progress. If you are in a private window, browser ' +
          'storage may be blocked and your history will not persist.');
    return false;
  }
}

function bump(bucket, k, correct){
  var r = bucket[k] || (bucket[k] = {seen:0, correct:0, last:0});
  r.seen++; r.last = Date.now()/1000;
  if (correct) r.correct++;
  return r;
}

function recordAttempt(d, portion, mode, answers, elapsed, weakSpot){
  var perTopic = {}, correct = 0;
  answers.forEach(function(a){
    if (a.correct) correct++;
    var t = a.topic || 'unknown';
    var s = perTopic[t] || (perTopic[t] = {seen:0, correct:0});
    s.seen++; if (a.correct) s.correct++;
    bump(d.topics, t, a.correct);
    if (a.qid && a.qid.indexOf('math:') !== 0) bump(d.items, a.qid, a.correct);
    if (a.sub) bump(d.subs, a.sub, a.correct);
    if (a.generator) bump(d.generators, a.generator, a.correct);
  });
  var att = {
    id: Math.random().toString(16).slice(2, 14),
    portion: portion, mode: mode, weak_spot: !!weakSpot,
    at: Date.now()/1000, count: answers.length, correct: correct,
    pct: answers.length ? correct/answers.length : 0,
    seconds: Math.round(elapsed*10)/10,
    topics: perTopic
  };
  d.attempts.push(att);
  return att;
}

/* ------------------------------------------------------------- scoring */
function topicPriority(rec, w){
  var seen = rec ? (rec.seen||0) : 0;
  var corr = rec ? (rec.correct||0) : 0;
  var accuracy, confidence;
  if (!seen){ accuracy = 0.5; confidence = 0; }
  else { accuracy = corr/seen; confidence = Math.min(1, seen/12); }
  return (0.35 + 0.65*confidence) * (1-accuracy) * (1 + w/10);
}

function weakWeights(topicRecs, declared){
  var dec = {};
  (declared||[]).forEach(function(k){ dec[k] = 1; });
  var out = {};
  ORDER.forEach(function(k){
    var rec = (topicRecs||{})[k];
    var s = 0.05 + topicPriority(rec, weight(k));
    if (dec[k]) s += ((rec && rec.seen >= 10) ? 0.20 : 0.60);
    out[k] = s;
  });
  return out;
}

function allocate(weights, total){
  var keys = Object.keys(weights).filter(function(k){ return weights[k] > 0; });
  if (!keys.length) return {};
  var sum = 0; keys.forEach(function(k){ sum += weights[k]; });
  var out = {}, used = 0;
  keys.forEach(function(k){ out[k] = Math.floor(total*weights[k]/sum); used += out[k]; });
  keys.sort(function(a,b){ return weights[b]-weights[a]; });
  for (var i = 0; used < total; i++, used++) out[keys[i % keys.length]]++;
  return out;
}

function shuffle(a){
  for (var i = a.length-1; i > 0; i--){
    var j = Math.floor(Math.random()*(i+1)), t = a[i]; a[i] = a[j]; a[j] = t;
  }
  return a;
}

/* ------------------------------------------------------------ selection */
function missedSet(d){
  var s = {};
  Object.keys(d.items||{}).forEach(function(id){
    var r = d.items[id];
    if (r.seen > r.correct) s[id] = 1;
  });
  return s;
}

function tier(rows, level){
  return rows.filter(function(r){ return (r.difficulty || 1) === level; });
}
function byDifficulty(rows, d){
  if (d === 'core') return tier(rows, 1).length ? tier(rows, 1) : rows;
  if (d === 'hard') return tier(rows, 2).length ? tier(rows, 2) : rows;
  return rows;
}
function order(rows, missed){
  return shuffle(rows.filter(function(r){ return missed[r.id]; }))
    .concat(shuffle(rows.filter(function(r){ return !missed[r.id]; })));
}
function pickFromTopic(pool, topic, n, missed, d){
  var rows = pool.filter(function(r){ return r.topic === topic; });
  if (!rows.length || n <= 0) return [];
  if (d === 'harder'){
    var wantHard = Math.round(n * HARDER_SHARE);
    var hard = order(tier(rows, 2), missed).slice(0, wantHard);
    var used = {};
    hard.forEach(function(r){ used[r.id] = 1; });
    var rest = order(rows.filter(function(r){ return !used[r.id]; }), missed);
    return hard.concat(rest).slice(0, n);
  }
  return order(byDifficulty(rows, d), missed).slice(0, n);
}

function mathPick(n, kinds){
  var pool = (kinds && kinds.length) ? kinds : Object.keys(DATA.math);
  var out = [], spin = shuffle(pool.slice());
  for (var i = 0; i < n; i++){
    if (!spin.length) spin = shuffle(pool.slice());
    var k = spin.pop(), set = DATA.math[k];
    if (!set || !set.q.length) continue;
    var j = Math.floor(Math.random()*set.q.length), row = set.q[j];
    out.push({
      id: 'math:'+k+':'+j,
      portion: set.closing ? 'comprehensive' : 'national',
      topic: set.closing ? 'comp/closing-math' : 'national/math',
      generator: k, q: row[0], choices: row[1], answer: row[2],
      steps: row[3], concept: set.concept, difficulty: 2,
      explain: 'Correct answer: '+row[1][row[2]]+'. '+set.concept
    });
  }
  return out;
}

function allRows(){
  var out = [];
  ['national','georgia','comprehensive'].forEach(function(p){
    out = out.concat(DATA.banks[p] || []);
  });
  return out;
}

function select(portion, count, opts){
  opts = opts || {};
  var d = opts.progress || load();
  var missed = missedSet(d);
  var diff = opts.difficulty || 'harder';
  if (DIFFICULTIES.indexOf(diff) < 0) diff = 'harder';

  if (opts.sub){
    // one "little topic": its own questions, then generated math for a math
    // subtopic, then the rest of the parent topic so the drill is full length
    var rows = allRows();
    var own = shuffle(rows.filter(function(r){ return r.sub === opts.sub; }));
    var out2 = own.slice(0, count);
    if (out2.length < count){
      var gens = Object.keys(DATA.math).filter(function(k){
        return opts.sub.slice(-(DATA.math[k].label.length + 1)) === '|' + DATA.math[k].label;
      });
      if (gens.length) out2 = out2.concat(mathPick(count - out2.length, gens));
    }
    if (out2.length < count){
      var parent = opts.sub.split('|')[0], have = {};
      out2.forEach(function(r){ have[r.id] = 1; });
      var rest = shuffle(rows.filter(function(r){
        return r.topic === parent && !have[r.id];
      }));
      out2 = out2.concat(rest.slice(0, count - out2.length));
    }
    return out2.slice(0, count);
  }

  if (portion === 'math'){
    var kinds = null;
    if (opts.topic && DATA.math[opts.topic]) kinds = [opts.topic];
    else if (opts.weak_spot){
      var scored = Object.keys(DATA.math).map(function(k){
        return {k:k, s:topicPriority(d.generators[k], 5)};
      }).sort(function(a,b){ return b.s-a.s; });
      kinds = scored.slice(0, Math.max(4, Math.ceil(scored.length/2)))
                    .map(function(x){ return x.k; });
    }
    return mathPick(count, kinds);
  }

  if (portion === 'mixed'){
    var nN = Math.round(count * EXAM.national / TOTAL_Q);
    return select('national', nN, opts).concat(select('georgia', count - nN, opts));
  }

  var pool = DATA.banks[portion] || [];
  if (opts.topic){
    var chosen = pickFromTopic(pool, opts.topic, count, missed, diff);
    if (opts.topic === 'national/math' && chosen.length < count)
      chosen = chosen.concat(mathPick(count - chosen.length, null));
    else if (opts.topic === 'comp/closing-math'){
      // blend written debit/credit items with generated arithmetic
      var keep = Math.max(1, Math.floor(count / 2));
      chosen = chosen.slice(0, keep).concat(mathPick(count - keep, CLOSING_GENS));
    }
    return chosen.slice(0, count);
  }

  var weights = {};
  if (opts.weak_spot){
    var all = weakWeights(d.topics, (d.profile||{}).declared_weak);
    portionTopics(portion).forEach(function(k){ weights[k] = all[k]; });
  } else {
    portionTopics(portion).forEach(function(k){ weights[k] = weight(k); });
  }

  var plan = allocate(weights, count), out = [];
  Object.keys(plan).forEach(function(t){
    var got = pickFromTopic(pool, t, plan[t], missed, diff);
    if (got.length < plan[t] && t === 'national/math')
      got = got.concat(mathPick(plan[t] - got.length, null));
    else if (got.length < plan[t] && t === 'comp/closing-math')
      got = got.concat(mathPick(plan[t] - got.length, CLOSING_GENS));
    out = out.concat(got);
  });

  if (out.length < count){
    var need = count - out.length;
    if (portion === 'national') out = out.concat(mathPick(need, null));
    else if (portion === 'comprehensive') out = out.concat(mathPick(need, CLOSING_GENS));
    else {
      var have = {}; out.forEach(function(r){ have[r.id] = 1; });
      out = out.concat(shuffle(pool.filter(function(r){ return !have[r.id]; })).slice(0, need));
    }
  }
  return shuffle(out).slice(0, count);
}

function mockExam(diff){
  // the comprehensive subtest is a drill, not a section of the real exam
  var o = {difficulty: diff};
  return select('national', EXAM.national, o).concat(select('georgia', EXAM.georgia, o));
}

/* -------------------------------------------------------------- reports */
function topicReport(d){
  return ORDER.map(function(k){
    var t = TOPIC[k], rec = d.topics[k];
    var seen = rec ? rec.seen : 0, corr = rec ? rec.correct : 0;
    return {topic:k, portion:t.portion, label:t.label, blurb:t.blurb,
            exam_questions:t.exam_questions, seen:seen, correct:corr,
            pct: seen ? corr/seen : null,
            priority: topicPriority(rec, t.exam_questions)};
  }).sort(function(a,b){ return b.priority - a.priority; });
}

function weakestReport(d, limit){
  var rows = topicReport(d);
  var attempted = rows.filter(function(r){ return r.seen >= 3; });
  var unseen = rows.filter(function(r){ return r.seen < 3; });
  attempted.sort(function(a, b){
    // weakest first, then by how much the topic is worth on the exam
    if (a.pct !== b.pct) return a.pct - b.pct;
    return b.exam_questions - a.exam_questions;
  });
  return {weak: attempted.slice(0, limit || 8), untested: unseen};
}

function portionStats(d){
  var out = {};
  ['national','georgia','comprehensive'].forEach(function(p){
    var rows = d.attempts.filter(function(a){ return a.portion === p; });
    if (!rows.length){ out[p] = {attempts:0, pct:null, recent_pct:null, trend:null}; return; }
    var tq = 0, tc = 0;
    rows.forEach(function(r){ tq += r.count; tc += r.correct; });
    var recent = rows.slice(-3), rq = 0, rc = 0;
    recent.forEach(function(r){ rq += r.count; rc += r.correct; });
    var trend = null;
    if (rows.length >= 2){
      var half = rows.slice(0, Math.max(1, Math.floor(rows.length/2))), hq = 0, hc = 0;
      half.forEach(function(r){ hq += r.count; hc += r.correct; });
      trend = (rc/(rq||1)) - (hc/(hq||1));
    }
    out[p] = {attempts:rows.length, questions:tq, pct:tc/(tq||1),
              recent_pct:rc/(rq||1), trend:trend, last:rows[rows.length-1].at};
  });
  return out;
}

function trendSeries(d){
  var s = {};
  d.attempts.forEach(function(a){
    Object.keys(a.topics||{}).forEach(function(t){
      var v = a.topics[t];
      if (!v.seen) return;
      (s[t] || (s[t] = [])).push({at:a.at, pct:v.correct/v.seen, seen:v.seen});
    });
  });
  return s;
}

function subReport(d, minSeen, limit){
  minSeen = minSeen || 2;
  var rows = [];
  Object.keys(d.subs || {}).forEach(function(key){
    var rec = d.subs[key];
    if (rec.seen < minSeen) return;
    var cut = key.indexOf('|');
    var topic = key.slice(0, cut), label = key.slice(cut + 1);
    var t = TOPIC[topic];
    if (!t) return;
    rows.push({sub: key, label: label, topic: topic, topic_label: t.label,
               portion: t.portion, exam_questions: t.exam_questions,
               counts_on_exam: countsOnExam(topic),
               seen: rec.seen, correct: rec.correct, pct: rec.correct / rec.seen});
  });
  rows.sort(function(a, b){
    if (a.pct !== b.pct) return a.pct - b.pct;
    return b.exam_questions - a.exam_questions;
  });
  return limit ? rows.slice(0, limit) : rows;
}

function generatorReport(d){
  return Object.keys(DATA.math).map(function(k){
    var rec = d.generators[k];
    var seen = rec ? rec.seen : 0, corr = rec ? rec.correct : 0;
    return {key:k, label:DATA.math[k].label, concept:DATA.math[k].concept,
            seen:seen, correct:corr, pct: seen ? corr/seen : null};
  }).sort(function(a,b){
    return (a.pct === null ? 0.5 : a.pct) - (b.pct === null ? 0.5 : b.pct);
  });
}

/* ------------------------------------------------- dashboard tables ---- */
function _sliceStats(rows){
  /* rows: [{seen, correct}] in attempt order -> totals, recent, trend */
  var qs = 0, corr = 0;
  rows.forEach(function(r){ qs += r.seen; corr += r.correct; });
  var recent = rows.slice(-3), rq = 0, rc = 0;
  recent.forEach(function(r){ rq += r.seen; rc += r.correct; });
  var trend = null;
  if (rows.length >= 2){
    var half = rows.slice(0, Math.max(1, Math.floor(rows.length / 2))), hq = 0, hc = 0;
    half.forEach(function(r){ hq += r.seen; hc += r.correct; });
    if (hq && rq) trend = (rc / rq) - (hc / hq);
  }
  return {sets: rows.length, qs: qs, correct: corr,
          pct: qs ? corr / qs : null,
          recent_pct: rq ? rc / rq : null,
          trend: trend};
}

function topicTable(d){
  /* one row per topic, in exam order, with per-attempt history folded in */
  var hist = {};
  d.attempts.forEach(function(a){
    Object.keys(a.topics || {}).forEach(function(t){
      var v = a.topics[t];
      if (!v.seen) return;
      (hist[t] || (hist[t] = [])).push(v);
    });
  });
  return ORDER.map(function(k){
    var t = TOPIC[k];
    var st = _sliceStats(hist[k] || []);
    st.topic = k; st.portion = t.portion; st.label = t.label;
    st.exam_questions = t.exam_questions;
    st.counts_on_exam = countsOnExam(k);
    return st;
  });
}

function sectionTable(d){
  /* one row per section, folding every attempt that belongs to it */
  var out = [];
  ['national', 'georgia', 'comprehensive'].forEach(function(p){
    var keys = {};
    portionTopics(p).forEach(function(k){ keys[k] = 1; });
    var rows = [];
    d.attempts.forEach(function(a){
      var seen = 0, corr = 0;
      Object.keys(a.topics || {}).forEach(function(t){
        if (!keys[t]) return;
        seen += a.topics[t].seen; corr += a.topics[t].correct;
      });
      if (seen) rows.push({seen: seen, correct: corr});
    });
    var st = _sliceStats(rows);
    st.portion = p;
    st.name = {national: 'National', georgia: 'Georgia state',
               comprehensive: 'Comprehensive'}[p];
    st.scored = (DATA.portions[p] || {}).scored || 0;
    out.push(st);
  });
  return out;
}

function headline(d){
  /* the readout strip: overall standing against the 75% pass mark */
  var all = [];
  d.attempts.forEach(function(a){
    var keys = {};
    portionTopics('national').concat(portionTopics('georgia'))
      .forEach(function(k){ keys[k] = 1; });
    var seen = 0, corr = 0;
    Object.keys(a.topics || {}).forEach(function(t){
      if (!keys[t]) return;
      seen += a.topics[t].seen; corr += a.topics[t].correct;
    });
    if (seen) all.push({seen: seen, correct: corr});
  });
  var overall = _sliceStats(all);
  var answered = 0;
  d.attempts.forEach(function(a){ answered += a.count; });
  var days = null;
  var exam = asDate((d.profile || {}).exam_date);
  if (exam){
    var t = new Date(); t.setHours(0, 0, 0, 0);
    days = Math.round((exam - t) / 86400000);
  }
  return {exam_pct: overall.recent_pct, sets: d.attempts.length,
          answered: answered, days_out: days,
          trend: overall.trend, passing: overall.recent_pct !== null
                                          && overall.recent_pct >= 0.75};
}

/* ---------------------------------------------------------------- plan */
function asDate(v){
  if (!v) return null;
  var p = String(v).slice(0,10).split('-');
  if (p.length !== 3) return null;
  var d = new Date(+p[0], +p[1]-1, +p[2]);
  return isNaN(d) ? null : d;
}
function iso(d){
  return d.getFullYear() + '-' + ('0'+(d.getMonth()+1)).slice(-2) + '-' + ('0'+d.getDate()).slice(-2);
}
function addDays(d, n){ var x = new Date(d); x.setDate(x.getDate()+n); return x; }
function dayDiff(a, b){ return Math.round((a-b)/86400000); }

function phasePlan(n){
  if (n <= 1) return ['Drill & mock'];
  if (n === 2) return ['Weak-area drill','Mock exams & review'];
  if (n === 3) return ['Weak-area drill','Full coverage','Mock exams & review'];
  var build = Math.max(1, Math.round(n*0.45));
  var drill = Math.max(1, Math.round(n*0.35));
  var final_ = Math.max(1, n - build - drill);
  var out = [];
  for (var i=0;i<build;i++) out.push('Build coverage');
  for (i=0;i<drill;i++) out.push('Weak-area drill');
  for (i=0;i<final_;i++) out.push('Mock exams & review');
  return out.slice(0, n);
}

function why(r){
  if (r.pct !== null && r.seen >= 4)
    return 'you are at '+Math.round(r.pct*100)+'% here ('+r.seen+' questions), worth '+r.exam_questions+' on the exam';
  if (r.declared_weak) return 'you flagged this as a weak area; worth '+r.exam_questions+' on the exam';
  if (!r.seen) return 'no data yet -- worth '+r.exam_questions+' questions on the exam';
  return 'only '+r.seen+' questions attempted; worth '+r.exam_questions+' on the exam';
}

function ranked(d){
  var dec = {};
  ((d.profile||{}).declared_weak||[]).forEach(function(k){ dec[k]=1; });
  return ORDER.filter(countsOnExam).map(function(k){
    var t = TOPIC[k], rec = d.topics[k];
    var seen = rec ? rec.seen : 0, corr = rec ? rec.correct : 0;
    var s = topicPriority(rec, t.exam_questions);
    if (dec[k]) s += rec ? 0.20 : 0.45;
    return {topic:k, portion:t.portion, label:t.label, exam_questions:t.exam_questions,
            declared_weak:!!dec[k], seen:seen, pct: seen ? corr/seen : null, score:s};
  }).sort(function(a,b){ return b.score - a.score; });
}

function bufferPlan(days){
  if (days <= 0) return [];
  var out = ['Light review only -- no new material.'];
  if (days >= 2) out.push('One 132-question mock exam, timed, at your real exam time of day.');
  if (days >= 3) out.push('Re-read every explanation you missed on the last two mocks.');
  out.push('Day before: 20-question math sprint, then stop. Sleep beats cramming.');
  return out;
}

function buildPlan(d){
  var prof = d.profile || {};
  var exam = asDate(prof.exam_date);
  if (!exam) return {error:'Set an exam date to generate a schedule.'};
  var mastery = asDate(prof.mastery_date) || exam;
  if (mastery > exam) mastery = exam;
  var hours = prof.hours_per_week || 8;

  var today = new Date(); today.setHours(0,0,0,0);
  var daysExam = dayDiff(exam, today), daysMastery = dayDiff(mastery, today);
  var planDays = Math.max(1, daysMastery);
  var nWeeks = Math.max(1, Math.ceil(planDays/7));
  var phases = phasePlan(nWeeks);

  var all = ranked(d);
  var nat = all.filter(function(r){ return r.portion === 'national'; });
  var ga = all.filter(function(r){ return r.portion === 'georgia'; });
  var shareN = EXAM.national/TOTAL_Q;
  var nFocusN = Math.max(2, Math.round(3*shareN)+1);
  var nFocusG = Math.max(2, Math.round(3*(1-shareN))+1);

  var weeks = [], cursor = today, ni = 0, gi = 0;
  for (var i = 0; i < nWeeks; i++){
    var start = cursor, end = addDays(start, 6);
    if (end > mastery) end = mastery;
    var phase = phases[i], focus = [], tasks;
    if (phase === 'Mock exams & review'){
      focus = nat.slice(0,2).concat(ga.slice(0,2));
      tasks = ['Take one FULL mock exam (132 questions, National + Georgia).',
               'Review every miss and write the rule in your own words.',
               'Run Weak-spot mode twice on whatever the mock exposes.',
               'Do one 15-question math sprint daily.'];
    } else {
      for (var j = 0; j < nFocusN; j++) focus.push(nat[ni++ % nat.length]);
      for (j = 0; j < nFocusG; j++) focus.push(ga[gi++ % ga.length]);
      tasks = (phase === 'Weak-area drill')
        ? ['Weak-spot quiz, 20 questions, once per study day.',
           'Two 20-question topic quizzes on the focus topics below.',
           'Math practice mode: 10 problems daily, read every solution.']
        : ['One 20-question quiz per focus topic below.',
           'One 25-question National quiz to keep breadth.',
           'Math practice mode: 10 problems, 3x this week.'];
    }
    var wq = Math.round(hours*25);
    weeks.push({
      week:i+1, phase:phase, start:iso(start), end:iso(end),
      target_questions:wq,
      national_questions:Math.round(wq*shareN),
      georgia_questions:wq - Math.round(wq*shareN),
      focus: focus.map(function(r){
        return {topic:r.topic, label:r.label, portion:r.portion, why:why(r)};
      }),
      tasks: tasks
    });
    cursor = addDays(end, 1);
    if (cursor > mastery) break;
  }

  return {
    exam_date: iso(exam), mastery_date: iso(mastery),
    days_to_exam: daysExam, days_to_mastery: daysMastery,
    buffer_days: Math.max(0, dayDiff(exam, mastery)),
    weeks: weeks,
    weighting: {national:EXAM.national, georgia:EXAM.georgia},
    buffer_plan: bufferPlan(Math.max(0, dayDiff(exam, mastery)))
  };
}
