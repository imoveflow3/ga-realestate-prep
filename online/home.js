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
  if (HOME.preview){
    toast('Preview only \u2014 payments are not connected until this is deployed.');
    return;
  }
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
  if (HOME.preview){
    toast('Preview only \u2014 accounts are not connected until this is deployed.');
    return;
  }
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

function lsec(eyebrow, title, blurb){
  var sec = el('section', 'lsec');
  var h = el('div', 'lhead');
  if (eyebrow) h.appendChild(el('div', 'eyebrow', eyebrow));
  h.appendChild(el('h2', null, title));
  if (blurb) h.appendChild(el('p', null, blurb));
  sec.appendChild(h);
  return sec;
}

/* The list of what is included: names and a phrase. Named, not handed over. */
function includedList(){
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
  return list;
}

function openApp(){ location.href = HOME.appHref || '/buy'; }

function priceButton(label){
  var b = el('button', 'btn');
  /* Open access: the front door goes live before anything can take a payment,
     so the button opens the app rather than asking for money nobody can pay. */
  if (HOME.openAccess){
    b.textContent = label || 'Start studying';
    b.onclick = openApp;
    return b;
  }
  b.textContent = label || ('Get access — ' + money(HOME.price));
  b.onclick = function(){
    if (HOME.page === 'buy') return buy();
    if (HOME.preview){ HOME.page = 'buy'; render(); window.scrollTo(0, 0); return; }
    location.href = '/buy';
  };
  return b;
}

function noticeFor(q){
  if (q.get('gate')) return 'That part is inside the app. Get access below, or ' +
                            'sign in if you have already bought.';
  return null;
}

/* ------------------------------------------------------- the minimal page */
/* Sign up, sign in, pay. Nothing else competing for the decision.
   HOME.layout picks this over the long welcome page; both are built from the
   same data, so switching back is one flag in the build. */
function renderMinimal(v, q){
  var t = HOME.totals;
  var wrap = el('div', 'gatewrap');
  var card = el('div', 'gatecard');

  var note = noticeFor(q);
  if (note) card.appendChild(el('div', 'gatenote', note));

  var mark = el('div', 'gatemark');
  mark.innerHTML = '<svg viewBox="0 0 512 512" aria-hidden="true">' +
    '<path d="M256 96 L432 236 L400 236 L400 404 L112 404 L112 236 L80 236 Z" ' +
    'fill="none" stroke="currentColor" stroke-width="30" stroke-linejoin="round"/></svg>';
  card.appendChild(mark);

  card.appendChild(el('h1', null, 'Georgia Real Estate Exam Prep'));
  card.appendChild(el('p', 'gatelede',
    t.total + ' practice questions, ' + t.terms + ' defined terms and worked ' +
    'maths for the salesperson licensing exam.'));

  if (!HOME.openAccess){
    var price = el('div', 'gateprice');
    price.appendChild(el('span', 'amount', money(HOME.price)));
    price.appendChild(el('span', 'once', 'one payment \u00b7 lifetime access'));
    card.appendChild(price);
  }

  var acts = el('div', 'gateacts');
  var go = el('button', 'btn wide');
  if (HOME.openAccess){
    go.textContent = 'Start studying';
    go.onclick = openApp;
  } else {
    go.textContent = 'Get access \u2014 ' + money(HOME.price);
    go.onclick = function(){ buy(); };
  }
  acts.appendChild(go);

  if (!HOME.openAccess){
    var si = el('button', 'btn ghost wide', 'I already have an account');
    si.onclick = function(){ openAuth('email'); };
    acts.appendChild(si);
  }
  card.appendChild(acts);

  card.appendChild(el('p', 'gatefine', HOME.openAccess
    ? 'Free to use right now. Accounts and saved progress are on the way.'
    : 'No subscription. Nothing renews. Full refund within 14 days.'));

  wrap.appendChild(card);
  v.appendChild(wrap);
}

/* ------------------------------------------------------- the welcome page */
function renderWelcome(v, q){
  var t = HOME.totals;

  var hero = el('div', 'hero2'), w = el('div', 'wrap');
  var note = noticeFor(q);
  if (note) w.appendChild(el('div', 'gatenote', note));

  w.appendChild(el('div', 'kicker2', HOME.openAccess
    ? 'Georgia salesperson licence \u00b7 Free while it is open'
    : 'Georgia salesperson licence \u00b7 Built to the real exam blueprint'));
  var h1 = el('h1');
  h1.appendChild(document.createTextNode('Pass the Georgia real estate exam. '));
  h1.appendChild(el('em', null, 'First try.'));
  w.appendChild(h1);
  w.appendChild(el('p', 'lede2',
    t.total + ' practice questions scored the way the real exam scores you — ' +
    'National and Georgia separately, 75% needed on each. Every answer explained ' +
    'the moment you give it, every calculation worked out a step at a time.'));

  var cta = el('div', 'cta2');
  cta.appendChild(priceButton());
  if (!HOME.openAccess){
    var si = el('button', 'btn ghost', 'Already bought? Sign in');
    si.onclick = function(){ openAuth('email'); };
    cta.appendChild(si);
  }
  w.appendChild(cta);
  w.appendChild(el('p', 'fineprint', HOME.openAccess
    ? 'Free to use right now. Accounts and saved progress are on the way.'
    : 'One payment. No subscription, nothing renews, and a full refund within ' +
      '14 days if it is not for you.'));
  hero.appendChild(w);

  var band = el('div', 'statband');
  [[String(t.total), 'practice questions'], [String(t.terms), 'terms defined'],
   [String(t.topics), 'topics covered'],
   HOME.openAccess ? ['$0', 'to use right now']
                   : [money(HOME.price), 'once, not monthly']]
    .forEach(function(r){
      var d = el('div');
      d.appendChild(el('div', 'n', r[0]));
      d.appendChild(el('div', 'l', r[1]));
      band.appendChild(d);
    });
  hero.appendChild(band);
  v.appendChild(hero);

  /* who it is for */
  var who = lsec('Who this is for', 'Three people, mostly.', null);
  var cards = el('div', 'steps3');
  HOME.audience.forEach(function(r){
    var c = el('div', 'step3');
    c.appendChild(el('h3', null, r[0]));
    c.appendChild(el('p', null, r[1]));
    cards.appendChild(c);
  });
  who.appendChild(cards);
  v.appendChild(who);

  /* why it exists */
  var why = lsec('Why it exists', HOME.why.title, null);
  HOME.why.paras.forEach(function(x){
    var p = el('p', 'sub', x);
    p.style.maxWidth = '62ch';
    why.appendChild(p);
  });
  v.appendChild(why);

  /* how it works */
  var how = lsec('How it works', 'Read it, quiz it, hunt down what is left.',
    'The app decides what you do next, so you are not the one choosing — ' +
    'which is where most study time gets lost.');
  var st = el('div', 'steps3');
  HOME.steps.forEach(function(r){
    var c = el('div', 'step3');
    c.appendChild(el('div', 'sno', r[0]));
    c.appendChild(el('h3', null, r[1]));
    c.appendChild(el('p', null, r[2]));
    st.appendChild(c);
  });
  how.appendChild(st);
  v.appendChild(how);

  /* what is inside */
  var inc = lsec('What is inside', 'All of it. There is no higher tier.', null);
  inc.appendChild(includedList());
  v.appendChild(inc);

  /* the honest part */
  var honest = lsec('The honest part', 'What this is not.', null);
  var ul = el('ul'); ul.className = 'plainlist';
  HOME.honest.forEach(function(x){ ul.appendChild(el('li', null, x)); });
  honest.appendChild(ul);
  v.appendChild(honest);

  /* close */
  var end = el('div', 'endcta');
  if (HOME.openAccess){
    end.appendChild(el('h2', null, 'Start with one quiz.'));
    end.appendChild(el('p', null,
      'Twenty questions takes about fifteen minutes and tells you more about ' +
      'where you stand than a week of reading will.'));
    end.appendChild(priceButton('Open the app'));
    v.appendChild(end);
    return;
  }
  end.appendChild(el('h2', null, 'One payment. Yours for good.'));
  end.appendChild(el('p', null,
    'Nothing renews and there is nothing to cancel. If it is not what you ' +
    'wanted, email within 14 days and get your money back.'));
  end.appendChild(priceButton('See what you get — ' + money(HOME.price)));
  v.appendChild(end);
}

/* ----------------------------------------------------------- the buy page */
function renderBuy(v, q){
  var t = HOME.totals;

  var hero = el('div', 'hero2'), w = el('div', 'wrap');
  var note = noticeFor(q);
  if (note) w.appendChild(el('div', 'gatenote', note));

  var back = el('button', 'linkish', '← Back to the home page');
  back.style.cssText = 'align-self:flex-start;margin-bottom:.2rem';
  back.onclick = function(){
    if (HOME.preview){ HOME.page = 'welcome'; render(); window.scrollTo(0, 0); return; }
    location.href = '/';
  };
  w.appendChild(back);

  w.appendChild(el('div', 'kicker2',
    money(HOME.price) + ' once · No subscription · Lifetime access'));
  w.appendChild(el('h1', null, 'Get access.'));
  w.appendChild(el('p', 'lede2',
    'All ' + t.total + ' questions, the study notes, the maths and the drills. ' +
    'One payment, and the account is yours.'));

  var buybox = el('div', 'buybox');
  var tag = el('div', 'pricetag');
  tag.appendChild(el('span', 'amount', money(HOME.price)));
  tag.appendChild(el('span', 'once', 'one payment · lifetime access'));
  buybox.appendChild(tag);
  var go = el('button', 'btn');
  go.textContent = 'Pay ' + money(HOME.price) + ' with Stripe';
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
  v.appendChild(hero);

  var inc = lsec('What the ' + money(HOME.price) + ' buys',
                 'Everything below. There is no higher tier.', null);
  inc.appendChild(includedList());
  var acts = el('div', 'cta2');
  acts.style.marginTop = '.5rem';
  var go2 = el('button', 'btn');
  go2.textContent = 'Pay ' + money(HOME.price) + ' with Stripe';
  go2.onclick = function(){ buy(); };
  acts.appendChild(go2);
  inc.appendChild(acts);
  var fine = el('p', 'muted',
    'Card handled by Stripe — it never touches this site. Full refund ' +
    'within 14 days if it is not for you. By buying you agree to the terms.');
  fine.style.maxWidth = '46rem';
  inc.appendChild(fine);
  v.appendChild(inc);
}

function render(){
  var v = $('page');
  v.innerHTML = '';
  if (HOME.preview){
    var pv = el('div', 'previewbar');
    pv.appendChild(el('b', null, 'Preview'));
    pv.appendChild(el('span', null,
      ' \u2014 this is how the site will look. Buying and signing in start ' +
      'working once it is deployed.'));
    v.appendChild(pv);
  }
  var q = new URLSearchParams(location.search);
  if (q.get('checkout') === 'cancelled') toast('Checkout cancelled — nothing was charged.');
  if (q.get('checkout') === 'error') toast('Something went wrong with that payment.');
  if (HOME.page === 'buy') return renderBuy(v, q);
  if (HOME.layout === 'minimal') return renderMinimal(v, q);
  return renderWelcome(v, q);
}

/* ------------------------------------------------------------------ boot */
(function(){
  applyTheme(readTheme());
  $('themeBtn').onclick = function(){
    var next = THEMES[(THEMES.indexOf(readTheme()) + 1) % THEMES.length];
    try { localStorage.setItem(THEME_KEY, next); } catch(e){}
    applyTheme(next);
  };
  /* On the welcome page this leads to the buy page; on the buy page it pays. */
  var onBuyPage = (HOME.page === 'buy');
  if (HOME.openAccess) $('signinBtn').hidden = true;
  if (HOME.layout === 'minimal' && HOME.page !== 'buy'){
    $('buyBtn').hidden = true;          // the card below is the whole point
    $('signinBtn').hidden = true;
  }
  /* The price is all over the page already; in the header it only forces a
     wrap on a phone. */
  $('buyBtn').textContent = HOME.openAccess ? 'Open the app'
    : (onBuyPage ? ('Pay ' + money(HOME.price)) : 'Get access');
  $('buyBtn').onclick = function(){
    if (HOME.openAccess) return openApp();
    if (HOME.page === 'buy') return buy();
    if (HOME.preview){ HOME.page = 'buy'; render(); window.scrollTo(0, 0); return; }
    location.href = '/buy';
  };
  $('signinBtn').onclick = function(){ openAuth('email'); };
  $('authScrim').onclick = closeAuth;
  $('brand').onclick = function(){ location.href = '/'; };
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && !$('authSheet').hidden) closeAuth();
  });
  render();

  /* Somebody already signed in should not be sold to again. Open access has
     no accounts and no API behind it, so there is nothing to ask. */
  if (HOME.openAccess || HOME.preview) return;
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
