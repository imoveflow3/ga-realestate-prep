/* The sales page. Carries no question bank -- three sample questions and the
   blueprint counts, nothing a buyer is paying for. */
'use strict';

function $(id){ return document.getElementById(id); }
function el(t, c, x){
  var n = document.createElement(t);
  if (c) n.className = c;
  if (x !== undefined && x !== null) n.textContent = x;
  return n;
}
function money(cents){
  return '$' + (cents % 100 === 0 ? (cents / 100) : (cents / 100).toFixed(2));
}

var TOAST_T = null;
function toast(msg){
  var t = $('toast');
  t.textContent = msg; t.hidden = false;
  if (TOAST_T) clearTimeout(TOAST_T);
  TOAST_T = setTimeout(function(){ t.hidden = true; }, 3400);
}

/* ---- theme, same three states as the app ---- */
var THEME_KEY = 'ga-prep-theme', THEMES = ['auto', 'light', 'dark'];
function systemDark(){
  try { return matchMedia('(prefers-color-scheme: dark)').matches; } catch(e){ return false; }
}
function readTheme(){
  var t; try { t = localStorage.getItem(THEME_KEY); } catch(e){ t = null; }
  return THEMES.indexOf(t) >= 0 ? t : 'auto';
}
function applyTheme(mode){
  var root = document.documentElement;
  if (mode === 'auto') root.removeAttribute('data-theme');
  else root.setAttribute('data-theme', mode);
  var resolved = (mode === 'auto') ? (systemDark() ? 'dark' : 'light') : mode;
  var b = $('themeBtn');
  if (b){ b.setAttribute('data-shown', resolved);
          $('themeLabel').textContent = mode.charAt(0).toUpperCase() + mode.slice(1); }
}

/* ------------------------------------------------------------- buying */
var BUYING = false;
function buy(email){
  if (BUYING) return;
  BUYING = true;
  toast('Opening secure checkout…');
  fetch('/api/checkout', {
    method: 'POST', credentials: 'same-origin',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({email: email || null})
  }).then(function(r){ return r.json(); })
    .then(function(d){
      if (d.url){ location.href = d.url; return; }
      BUYING = false;
      toast(d.error || 'Could not start checkout. Try again shortly.');
    })['catch'](function(){
      BUYING = false;
      toast('Could not reach the payment service.');
    });
}

/* ------------------------------------------------------------ signing in */
var AUTH = {email: '', stage: 'email'};

function openAuth(stage){
  AUTH.stage = stage || 'email';
  renderAuth();
  $('authSheet').hidden = false;
}
function closeAuth(){ $('authSheet').hidden = true; }

function renderAuth(){
  var b = $('authBody');
  b.innerHTML = '';
  if (AUTH.stage === 'email'){
    b.appendChild(el('h2', null, 'Sign in'));
    b.appendChild(el('p', 'sub',
      'Already bought? Put in the email address you paid with and we will send ' +
      'you a six-digit code.'));
    var lab = el('label', null, 'Email address'); lab.setAttribute('for', 'authEmail');
    b.appendChild(lab);
    var inp = el('input'); inp.type = 'email'; inp.id = 'authEmail';
    inp.autocomplete = 'email'; inp.value = AUTH.email;
    inp.placeholder = 'you@example.com';
    b.appendChild(inp);
    var note = el('div', 'muted'); note.id = 'authNote'; note.style.marginTop = '.6rem';
    b.appendChild(note);
    var acts = el('div', 'wizacts'); acts.style.marginTop = '.9rem';
    var go = el('button', 'btn', 'Send me a code');
    go.onclick = function(){
      AUTH.email = inp.value.trim();
      if (!AUTH.email){ note.textContent = 'Put your email in first.'; return; }
      go.disabled = true; note.textContent = 'Sending…';
      fetch('/api/login/start', {
        method: 'POST', credentials: 'same-origin',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email: AUTH.email})
      }).then(function(r){ return r.json().then(function(d){ return {s: r.status, d: d}; }); })
        .then(function(x){
          go.disabled = false;
          if (x.d.error){ note.textContent = x.d.error; return; }
          AUTH.stage = 'code'; renderAuth();
        })['catch'](function(){ go.disabled = false; note.textContent = 'Network problem. Try again.'; });
    };
    acts.appendChild(go);
    var nope = el('button', 'btn ghost', 'I have not bought yet');
    nope.onclick = function(){ closeAuth(); buy(inp.value.trim()); };
    acts.appendChild(nope);
    b.appendChild(acts);
    setTimeout(function(){ inp.focus(); }, 30);
    return;
  }

  b.appendChild(el('h2', null, 'Check your email'));
  b.appendChild(el('p', 'sub',
    'If ' + AUTH.email + ' has access, a six-digit code is on its way. ' +
    'It expires in fifteen minutes.'));
  var lab2 = el('label', null, 'Six-digit code'); lab2.setAttribute('for', 'authCode');
  b.appendChild(lab2);
  var code = el('input'); code.id = 'authCode'; code.inputMode = 'numeric';
  code.autocomplete = 'one-time-code'; code.maxLength = 6; code.placeholder = '000000';
  b.appendChild(code);
  var note2 = el('div', 'muted'); note2.id = 'authNote'; note2.style.marginTop = '.6rem';
  b.appendChild(note2);
  var acts2 = el('div', 'wizacts'); acts2.style.marginTop = '.9rem';
  var ok = el('button', 'btn', 'Sign in');
  ok.onclick = function(){
    ok.disabled = true; note2.textContent = 'Checking…';
    fetch('/api/login/verify', {
      method: 'POST', credentials: 'same-origin',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email: AUTH.email, code: code.value.trim()})
    }).then(function(r){ return r.json().then(function(d){ return {s: r.status, d: d}; }); })
      .then(function(x){
        ok.disabled = false;
        if (x.d.error){ note2.textContent = x.d.error; return; }
        location.href = '/app';
      })['catch'](function(){ ok.disabled = false; note2.textContent = 'Network problem.'; });
  };
  acts2.appendChild(ok);
  var back = el('button', 'btn ghost', 'Use a different email');
  back.onclick = function(){ AUTH.stage = 'email'; renderAuth(); };
  acts2.appendChild(back);
  b.appendChild(acts2);
  setTimeout(function(){ code.focus(); }, 30);
}

/* ----------------------------------------------------------- the page */
var ICONS = HOME.icons;
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
function tagFor(portion){
  var cls = portion === 'georgia' ? ' ga' : (portion === 'comprehensive' ? ' comp' : '');
  var txt = portion === 'georgia' ? 'GA' : (portion === 'comprehensive' ? 'COMP' : 'NAT');
  return el('span', 'tag' + cls, txt);
}

function sampleBlock(){
  var q = HOME.samples[Math.floor(Math.random() * HOME.samples.length)];
  if (!q) return null;
  var wrap = el('div', 'sample');
  var top = el('div', 'stop');
  top.appendChild(el('span', null, 'A real question from the bank'));
  top.appendChild(tagFor(q.portion));
  if ((q.difficulty || 1) >= 2){
    var t = el('span', 'tag hard' + (q.difficulty === 3 ? ' exam' : ''));
    t.textContent = q.difficulty === 3 ? 'Exam' : 'Hard';
    top.appendChild(t);
  }
  wrap.appendChild(top);
  var body = el('div', 'sbody');
  body.appendChild(el('div', 'sq', q.q));
  var opts = el('div', 'choices'), answered = false, buttons = [], hint = null;
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
      if (hint) hint.hidden = true;
      var fb = el('div', 'feedback ' + (k === q.answer ? 'ok' : 'no'));
      fb.appendChild(el('div', 'verdict', k === q.answer ? 'Correct' : 'Not quite'));
      fb.appendChild(el('div', null, q.explain));
      if (q.concept){
        var c = el('div', 'concept');
        c.appendChild(el('b', null, 'Concept tested: '));
        c.appendChild(document.createTextNode(q.concept));
        fb.appendChild(c);
      }
      body.appendChild(fb);
      var row = el('div', 'row'); row.style.marginTop = '.3rem';
      var d = el('div'); d.style.flex = '0 0 auto';
      var go = el('button', 'btn');
      go.textContent = 'Get the other ' + (HOME.totals.total - HOME.samples.length) +
                       ' — ' + money(HOME.price);
      go.onclick = function(){ buy(); };
      d.appendChild(go); row.appendChild(d);
      body.appendChild(row);
    };
    buttons.push(b);
    opts.appendChild(b);
  });
  hint = el('p', 'muted',
    'Pick one — every answer is explained the moment you give it, and it ' +
    'names the concept being tested.');
  body.appendChild(opts);
  body.appendChild(hint);
  wrap.appendChild(body);
  return wrap;
}

function render(){
  var v = $('page'), t = HOME.totals;
  v.innerHTML = '';

  var q = new URLSearchParams(location.search);
  if (q.get('gate')){
    var g = el('div', 'card');
    g.style.cssText = 'border-left:3px solid var(--caution);margin-bottom:1rem';
    g.appendChild(el('h2', null, 'That part needs an account'));
    g.appendChild(el('p', 'sub',
      'The quizzes, notes, math and drills are behind the one-time ' +
      money(HOME.price) + '. Sign in if you have already bought.'));
    v.appendChild(g);
  }
  if (q.get('checkout') === 'cancelled') toast('Checkout cancelled — nothing was charged.');
  if (q.get('checkout') === 'error') toast('Something went wrong with that payment.');

  /* hero */
  var hero = el('div', 'hero2'), w = el('div', 'wrap');
  w.appendChild(el('div', 'kicker2',
    money(HOME.price) + ' once · No subscription · Georgia salesperson licence'));
  var h1 = el('h1');
  h1.appendChild(document.createTextNode('Pass the Georgia real estate exam. '));
  h1.appendChild(el('em', null, 'First try.'));
  w.appendChild(h1);
  w.appendChild(el('p', 'lede2',
    t.total + ' practice questions written to the real blueprint and scored the ' +
    'way the real exam scores you — National and Georgia separately, 75% ' +
    'needed on each. Every answer explained. One payment, yours for good.'));
  var cta = el('div', 'cta2');
  var go = el('button', 'btn');
  go.textContent = 'Get access — ' + money(HOME.price);
  go.onclick = function(){ buy(); };
  cta.appendChild(go);
  var see = el('button', 'btn ghost', 'Try a question first');
  see.onclick = function(){
    var s = $('sampleAnchor');
    if (s) s.scrollIntoView({behavior: 'smooth', block: 'start'});
  };
  cta.appendChild(see);
  w.appendChild(cta);
  w.appendChild(el('p', 'fineprint',
    'One payment of ' + money(HOME.price) + '. No subscription, no renewals. ' +
    'Full refund within 14 days if it is not for you.'));
  hero.appendChild(w);

  var band = el('div', 'statband');
  [[String(t.total), 'practice questions'], [String(t.terms), 'terms defined'],
   [String(t.topics), 'topics covered'], [money(HOME.price), 'once, not monthly']]
    .forEach(function(r){
      var d = el('div');
      d.appendChild(el('div', 'n', r[0]));
      d.appendChild(el('div', 'l', r[1]));
      band.appendChild(d);
    });
  hero.appendChild(band);
  v.appendChild(hero);

  /* what you get */
  var s1 = lsec('What the ' + money(HOME.price) + ' buys', 'Six tools, one payment, no renewals.',
    'Everything below is included. There is no higher tier and nothing else to buy.');
  var tiles = el('div', 'tiles');
  HOME.features.forEach(function(r){
    var b = el('div', 'tile');
    b.appendChild(iconEl(r.icon));
    b.appendChild(el('h3', null, r.name));
    b.appendChild(el('p', null, r.desc));
    tiles.appendChild(b);
  });
  s1.appendChild(tiles);
  v.appendChild(s1);

  /* sample */
  var s2 = lsec('See for yourself', 'Here is one, on the house.',
    'Pulled from the same bank you get, at the difficulty the real thing is ' +
    'written to. Answer it and see exactly what the explanations look like.');
  s2.id = 'sampleAnchor';
  var sample = sampleBlock();
  if (sample) s2.appendChild(sample);
  v.appendChild(s2);

  /* blueprint */
  var s3 = lsec('What is on the exam', 'The whole blueprint, weighted.',
    'Georgia scores the two portions separately and you must clear 75% on each. ' +
    'A strong average will not save a weak half, so the app tracks them apart.');
  var bp = el('div', 'blueprint');
  [['national', 'National portion', HOME.exam.national],
   ['georgia', 'Georgia portion', HOME.exam.georgia]].forEach(function(r){
    var col = el('div', 'bpcol'), h = el('h3');
    h.appendChild(document.createTextNode(r[1]));
    h.appendChild(el('span', null, r[2] + ' questions'));
    col.appendChild(h);
    HOME.topics.filter(function(x){ return x.portion === r[0]; })
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

  /* faq */
  var s5 = lsec('Before you buy', 'The honest answers.', null);
  var faq = el('div', 'faq');
  HOME.faq.forEach(function(r){
    var d = el('details'), sm = el('summary');
    sm.appendChild(document.createTextNode(r[0]));
    d.appendChild(sm);
    d.appendChild(el('p', null, r[1]));
    faq.appendChild(d);
  });
  s5.appendChild(faq);
  v.appendChild(s5);

  /* close */
  var end = el('div', 'endcta');
  end.appendChild(el('h2', null, 'One payment. Yours for good.'));
  end.appendChild(el('p', null,
    'No subscription to cancel and no renewal to forget. If it is not what you ' +
    'wanted, email within 14 days and get your money back.'));
  var eb = el('button', 'btn');
  eb.textContent = 'Get access — ' + money(HOME.price);
  eb.onclick = function(){ buy(); };
  end.appendChild(eb);
  var si = el('button', 'btn mini ghost', 'already bought? sign in');
  si.style.cssText = 'background:transparent;border-color:transparent;color:inherit;' +
                     'opacity:.85;text-decoration:underline';
  si.onclick = function(){ openAuth('email'); };
  end.appendChild(si);
  v.appendChild(end);
}

/* ------------------------------------------------------------------ boot */
(function(){
  applyTheme(readTheme());
  $('themeBtn').onclick = function(){
    var next = THEMES[(THEMES.indexOf(readTheme()) + 1) % THEMES.length];
    try { localStorage.setItem(THEME_KEY, next); } catch(e){}
    applyTheme(next);
  };
  $('buyBtn').textContent = 'Get access — ' + money(HOME.price);
  $('buyBtn').onclick = function(){ buy(); };
  $('signinBtn').onclick = function(){ openAuth('email'); };
  $('authScrim').onclick = closeAuth;
  $('brand').onclick = function(){ location.href = '/'; };
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && !$('authSheet').hidden) closeAuth();
  });
  render();

  /* Somebody already signed in should not be sold to again. */
  fetch('/api/me', {credentials: 'same-origin'})
    .then(function(r){ return r.json(); })
    .then(function(me){
      if (me && me.paid){
        $('buyBtn').textContent = 'Open the app';
        $('buyBtn').onclick = function(){ location.href = '/app'; };
        $('signinBtn').hidden = true;
      }
    })['catch'](function(){});
})();
