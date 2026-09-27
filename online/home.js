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
/* One screen. What it is, what it costs, a button, and a way back in for
   people who have already bought. Everything a buyer is paying for -- the
   questions, the notes, even the blueprint weightings -- is behind the gate. */

var ICONS = HOME.icons;
function iconEl(name){
  var s = el('span', 'ico');
  s.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true">' + (ICONS[name] || '') + '</svg>';
  return s;
}

function render(){
  var v = $('page'), t = HOME.totals;
  v.innerHTML = '';

  var q = new URLSearchParams(location.search);
  if (q.get('checkout') === 'cancelled') toast('Checkout cancelled — nothing was charged.');
  if (q.get('checkout') === 'error') toast('Something went wrong with that payment.');

  var hero = el('div', 'hero2'), w = el('div', 'wrap');

  if (q.get('gate')){
    w.appendChild(el('div', 'gatenote',
      'That part is inside the app. Get access below, or sign in if you have ' +
      'already bought.'));
  }

  w.appendChild(el('div', 'kicker2',
    money(HOME.price) + ' once · No subscription · Georgia salesperson licence'));
  var h1 = el('h1');
  h1.appendChild(document.createTextNode('Pass the Georgia real estate exam. '));
  h1.appendChild(el('em', null, 'First try.'));
  w.appendChild(h1);
  w.appendChild(el('p', 'lede2',
    t.total + ' practice questions written to the real blueprint and scored the ' +
    'way the real exam scores you — National and Georgia separately, 75% ' +
    'needed on each. Every answer explained, every calculation worked out.'));

  /* the price, the button, and nothing between them */
  var buybox = el('div', 'buybox');
  var tag = el('div', 'pricetag');
  tag.appendChild(el('span', 'amount', money(HOME.price)));
  tag.appendChild(el('span', 'once', 'one payment · lifetime access'));
  buybox.appendChild(tag);
  var go = el('button', 'btn');
  go.textContent = 'Get access — ' + money(HOME.price);
  go.onclick = function(){ buy(); };
  buybox.appendChild(go);
  var si = el('button', 'linkish', 'Already bought? Sign in');
  si.onclick = function(){ openAuth('email'); };
  buybox.appendChild(si);
  w.appendChild(buybox);

  var trust = el('div', 'trustrow');
  ['No subscription', 'Nothing renews', '14-day refund', 'Works offline']
    .forEach(function(x){ trust.appendChild(el('span', 'trust', x)); });
  w.appendChild(trust);
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

  /* what is inside: named, not handed over */
  var inc = el('section', 'lsec');
  var h = el('div', 'lhead');
  h.appendChild(el('div', 'eyebrow', 'What the ' + money(HOME.price) + ' buys'));
  h.appendChild(el('h2', null, 'All of it. There is no higher tier.'));
  inc.appendChild(h);
  var list = el('div', 'inclist');
  HOME.features.forEach(function(r){
    var row = el('div', 'incrow');
    row.appendChild(iconEl(r.icon));
    var txt = el('div');
    txt.appendChild(el('b', null, r.name));
    txt.appendChild(el('span', null, r.desc));
    row.appendChild(txt);
    list.appendChild(row);
  });
  inc.appendChild(list);

  var acts = el('div', 'cta2');
  acts.style.marginTop = '.5rem';
  var go2 = el('button', 'btn');
  go2.textContent = 'Get access — ' + money(HOME.price);
  go2.onclick = function(){ buy(); };
  acts.appendChild(go2);
  inc.appendChild(acts);
  inc.appendChild(el('p', 'muted',
    'Card handled by Stripe — it never touches this site. Not affiliated ' +
    'with the Georgia Real Estate Commission, PSI, or any school, and not a ' +
    'substitute for the 75-hour pre-licence course Georgia requires.'));
  v.appendChild(inc);
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
