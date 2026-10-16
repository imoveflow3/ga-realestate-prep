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
  return THEMES.indexOf(t) >= 0 ? t : 'light';
}
function applyTheme(mode){
  var root = document.documentElement;
  /* Always set: with no attribute the page is light, so a first visit (and
     the first paint, before this runs) is light whatever the system says. */
  root.setAttribute('data-theme', mode);
  var resolved = (mode === 'auto') ? (systemDark() ? 'dark' : 'light') : mode;
  var b = $('themeBtn');
  if (b){ b.setAttribute('data-shown', resolved);
          $('themeLabel').textContent = mode.charAt(0).toUpperCase() + mode.slice(1); }
}

/* ---------------------------------------------------------- the entrance */
/* A short, quiet opening: the mark settles, the name appears, and it is gone
   inside a second. It used to be a two-and-a-half second flight through a
   corridor of houses and books, which was striking the first time and a toll
   every time after. What is left reads as an app opening, not a title
   sequence, and it never stands between anyone and the login form.

   Same three rules as before: never twice in a session, never on the way back
   from Google or Stripe, and any key or tap ends it. */

var INTRO_KEY = 'ga-prep-intro';
var INTRO_MS = 900;

function introWanted(){
  if (HOME.preview) return false;
  try {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return false;
  } catch(e){}
  var q = new URLSearchParams(location.search);
  if (q.get('auth') || q.get('checkout') || q.get('pay') || q.get('gate')) return false;
  try {
    if (sessionStorage.getItem(INTRO_KEY)) return false;
    sessionStorage.setItem(INTRO_KEY, '1');
  } catch(e){ /* private window: play it once and move on */ }
  return true;
}

function buildIntro(){
  var wrap = el('div', 'intro');
  wrap.id = 'intro';
  wrap.setAttribute('aria-hidden', 'true');
  var mark = el('div', 'intro-mark');
  mark.innerHTML = '<svg viewBox="0 0 512 512" aria-hidden="true">' +
    '<path d="M256 96 L432 236 L400 236 L400 404 L112 404 L112 236 L80 236 Z" ' +
    'fill="none" stroke="currentColor" stroke-width="26" stroke-linejoin="round"/></svg>';
  wrap.appendChild(mark);
  wrap.appendChild(el('div', 'intro-word', 'Real Estate'));
  return wrap;
}

function playIntro(){
  if (!introWanted()){ document.body.classList.add('intro-done'); return; }

  var wrap = buildIntro();
  document.body.classList.add('intro-running');
  document.body.appendChild(wrap);

  var finished = false;
  function finish(){
    if (finished) return;
    finished = true;
    clearTimeout(timer);
    document.removeEventListener('keydown', finish, true);
    wrap.classList.add('done');
    document.body.classList.remove('intro-running');
    document.body.classList.add('intro-done');
    setTimeout(function(){ if (wrap.parentNode) wrap.parentNode.removeChild(wrap); }, 420);
  }

  var timer = setTimeout(finish, INTRO_MS);
  wrap.addEventListener('click', finish);
  wrap.addEventListener('touchstart', finish, {passive: true});
  document.addEventListener('keydown', finish, true);
  document.addEventListener('visibilitychange', function(){
    if (document.visibilityState === 'hidden') finish();
  });
}

/* ------------------------------------------------------------- buying */
var BUYING = false;
/* Start Stripe checkout for one plan. With no plan (old buttons), go and
   pick one first. */
function refCode(){
  var c = null;
  try { c = localStorage.getItem(REF_KEY); } catch(e){}
  return /^[A-Z0-9]{3,24}$/.test(c || '') ? c : '';
}

function buy(plan){
  if (HOME.preview){
    toast('Preview only \u2014 payments are not connected until this is deployed.');
    return;
  }
  if (typeof plan !== 'string' || !plan){ location.href = '/auth?pay=1'; return; }
  if (BUYING) return;
  BUYING = true;
  toast('Opening secure checkout…');
  fetch('/api/checkout', {
    method: 'POST', credentials: 'same-origin',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({plan: plan, code: refCode() || null})
  }).then(function(r){ return r.json(); })
    .then(function(d){
      if (d.url){ location.href = d.url; return; }
      if (d.signin){ location.href = d.signin; return; }
      BUYING = false;
      toast(d.error || 'Could not start checkout. Try again shortly.');
    })['catch'](function(){
      BUYING = false;
      toast('Could not reach the payment service.');
    });
}

/* "$9 a week": the cheapest plan, for the line under the button. */
function fromPrice(){
  var best = null;
  (HOME.plans || []).forEach(function(p){
    if (p.cents && (!best || p.cents < best.cents)) best = p;
  });
  return best ? money(best.cents) + ' a ' + best.per : money(HOME.price);
}

/* Stripe's own page for cancelling, switching plan or changing the card. */
function manageSubscription(){
  toast('Opening your subscription…');
  fetch('/api/billing', {method: 'POST', credentials: 'same-origin'})
    .then(function(r){ return r.json(); })
    .then(function(d){
      if (d.url){ location.href = d.url; return; }
      toast(d.error || 'Could not open your subscription. Try again shortly.');
    })['catch'](function(){ toast('Could not reach the payment service.'); });
}

/* The plans, as cards: weekly, monthly, yearly and "contact us". Prices come
   from the build (HOME.plans); the server charges from its own copy. */
var PLAN_ICONS = {
  weekly:  '<path d="M7 3v3M17 3v3M4 9h16M5 5h14a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z"/>',
  monthly: '<path d="M4 19V9l8-5 8 5v10a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1z"/>',
  yearly:  '<path d="M12 3l2.6 5.6 6.1.7-4.5 4.2 1.2 6L12 16.6 6.6 19.5l1.2-6L3.3 9.3l6.1-.7z"/>',
  affiliate: '<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M17 8v6M14 11h6"/>'
};
/* What each plan costs over time, and what it saves against the others --
   worked out from the prices, so changing a price keeps every line true.
   A year is 52 weeks or 12 months. */
var PER_YEAR = {week: 52, month: 12, year: 1};
function planPoints(p){
  var plans = (HOME.plans || []).filter(function(x){ return x.cents && PER_YEAR[x.per]; });
  var yearly = function(x){ return x.cents * PER_YEAR[x.per]; };
  var cents = function(c){ return money(Math.round(c)); };
  var pts = [];
  var every = {week: 'every week', month: 'every month', year: 'once a year'}[p.per];
  pts.push('Billed ' + money(p.cents) + ' ' + every + ', all features included');
  if (p.per === 'week'){
    pts.push('About ' + cents(p.cents * 52 / 12) + ' a month if you keep it going');
    pts.push('Best for a final week of review before your test');
  } else if (p.per === 'month'){
    pts.push('Works out to about ' + cents(p.cents * 12 / 52) + ' a week');
    pts.push('Enough time for most people to finish the course');
  } else if (p.per === 'year'){
    pts.push('Works out to about ' + cents(p.cents / 12) + ' a month (' +
             cents(p.cents / 52) + ' a week)');
  }
  /* savings against every plan that costs more over a year, nearest first */
  plans.slice().sort(function(a, b){ return yearly(a) - yearly(b); }).forEach(function(o){
    if (o.id === p.id || yearly(o) <= yearly(p)) return;
    var save = yearly(o) - yearly(p);
    var pct = Math.round(save / yearly(o) * 100);
    if (p.per === 'month' && o.per === 'week'){
      pts.push('Save ' + cents(save / 12) + ' a month vs. weekly (' + pct + '% less)');
    } else {
      pts.push('Save ' + cents(save) + ' a year vs. ' + o.name.toLowerCase() +
               ' (' + pct + '% less)');
    }
  });
  if (p.per === 'year') pts.push('Room for a slower pace or a retake');
  pts.push('Cancel any time');
  return pts;
}
function planCards(){
  var grid = el('div', 'plangrid');
  (HOME.plans || []).forEach(function(p){
    var c = el('div', 'plancard' + (p.badge === 'Most popular' ? ' featured' : ''));
    if (p.badge) c.appendChild(el('div', 'planbadge', p.badge));
    var ic = el('div', 'planicon');
    ic.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true">' + (PLAN_ICONS[p.id] || '') + '</svg>';
    c.appendChild(ic);
    c.appendChild(el('h3', null, p.name));
    c.appendChild(el('p', 'plandesc', p.desc));
    var btn;
    if (p.cents){
      var pr = el('div', 'planprice');
      pr.appendChild(el('span', 'amount', money(p.cents)));
      pr.appendChild(el('span', 'per', '/ ' + p.per));
      c.appendChild(pr);
      if (refCode() && REF.ok){
        var off = HOME.affiliate ? HOME.affiliate.discount : 40;
        c.appendChild(el('p', 'reffirst', 'First ' + p.per + ' ' +
          money(Math.round(p.cents * (100 - off) / 100)) + ' with your code'));
      }
      btn = el('button', 'btn wide' + (p.badge === 'Most popular' ? '' : ' ghost'),
               'Choose ' + p.name.toLowerCase());
      btn.disabled = BUYING || ME.canPay === false;
      btn.onclick = function(){ buy(p.id); };
    } else {
      var pr2 = el('div', 'planprice');
      pr2.appendChild(el('span', 'amount talk', 'Earn with us'));
      c.appendChild(pr2);
      btn = el('a', 'btn wide ghost', 'Join program');
      btn.href = '/#affiliate';
    }
    c.appendChild(btn);
    var ul = el('ul', 'planlist');
    (p.cents ? planPoints(p) : ['Refer students preparing for their exam',
                                'We email you the details when you apply']).forEach(function(t){
      ul.appendChild(el('li', null, t));
    });
    c.appendChild(ul);
    grid.appendChild(c);
  });
  return grid;
}

/* ------------------------------------------------------------ signing in */
var AUTH = {email: '', stage: 'email'};
var ME = {signedIn: false, paid: false, email: null, google: false};

var GOOGLE_G =
  '<svg viewBox="0 0 48 48" aria-hidden="true" class="gmark">' +
  '<path fill="#4285F4" d="M45.1 24.5c0-1.6-.1-2.7-.4-3.9H24v7.1h12.1c-.2 1.8-1.6 4.5-4.5 6.3l-.1.3 6.5 5 .4.1c4.1-3.8 6.7-9.4 6.7-15z"/>' +
  '<path fill="#34A853" d="M24 46c5.9 0 10.9-1.9 14.5-5.3l-6.9-5.3c-1.8 1.3-4.3 2.2-7.6 2.2-5.8 0-10.7-3.8-12.5-9l-.3.1-6.7 5.2-.1.3C7.9 41.1 15.4 46 24 46z"/>' +
  '<path fill="#FBBC05" d="M11.5 28.6c-.5-1.4-.8-2.9-.8-4.6s.3-3.2.7-4.6v-.3l-6.8-5.3-.2.1C2.8 16.8 2 20.3 2 24s.8 7.2 2.4 10.1l7.1-5.5z"/>' +
  '<path fill="#EA4335" d="M24 10.4c4.1 0 6.9 1.8 8.5 3.3l6.2-6C34.9 4.2 29.9 2 24 2 15.4 2 7.9 6.9 4.4 13.9l7.1 5.5c1.8-5.2 6.7-9 12.5-9z"/>' +
  '</svg>';

function googleButton(label){
  var b = el('button', 'btn gbtn wide');
  b.innerHTML = GOOGLE_G;
  b.appendChild(el('span', null, label || 'Continue with Google'));
  b.onclick = function(){ location.href = '/api/auth/google'; };
  return b;
}

function signOut(){
  fetch('/api/logout', {method: 'POST', credentials: 'same-origin'})
    .then(function(){ location.href = '/'; })['catch'](function(){ location.href = '/'; });
}

function openAuth(stage){
  if (HOME.preview){
    toast('Preview only — accounts are not connected until this is deployed.');
    return;
  }
  AUTH.stage = stage || 'login';
  renderAuth();
  $('authSheet').hidden = false;
}
function closeAuth(){ $('authSheet').hidden = true; }

function field(parent, id, label, type, opts){
  var l = el('label', null, label); l.setAttribute('for', id);
  parent.appendChild(l);
  var i = el('input');
  i.type = type; i.id = id;
  Object.keys(opts || {}).forEach(function(k){ i[k] = opts[k]; });
  parent.appendChild(i);
  return i;
}

function post(url, body){
  return fetch(url, {
    method: 'POST', credentials: 'same-origin',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(body)
  }).then(function(r){ return r.json().then(function(d){ return {status: r.status, d: d}; }); });
}

/* Where somebody lands after authenticating: into the app if they have paid
   for it, back to the card to pay if they have not. */
function afterAuth(paid){
  location.href = paid ? '/app' : '/?pay=1';
}

function renderAuth(){
  var b = $('authBody');
  b.innerHTML = '';

  if (AUTH.stage === 'signup' || AUTH.stage === 'login'){
    var isNew = AUTH.stage === 'signup';
    b.appendChild(el('h2', null, isNew ? 'Create your account' : 'Log in'));
    b.appendChild(el('p', 'sub', isNew
      ? 'Your progress, your notebook and your study plan are saved to this ' +
        'account, on every device you use.'
      : 'Welcome back. Everything you have done is waiting.'));

    if (ME.google){
      var g = googleButton(isNew ? 'Sign up with Google' : 'Continue with Google');
      g.classList.add('wide');
      b.appendChild(g);
      var div = el('div', 'orline');
      div.appendChild(el('span', null, 'or use an email address'));
      b.appendChild(div);
    }

    var email = field(b, 'authEmail', 'Email address', 'email',
                      {autocomplete: 'email', placeholder: 'you@example.com',
                       value: AUTH.email});
    var pw = field(b, 'authPassword', 'Password', 'password',
                   {autocomplete: isNew ? 'new-password' : 'current-password',
                    placeholder: ''});
    if (isNew){
      b.appendChild(el('p', 'muted',
        'Ten characters or more. Length beats symbols — a short password ' +
        'with punctuation in it is still a short password.'));
    }
    var note = el('div', 'authnote'); note.id = 'authNote';
    b.appendChild(note);

    var acts = el('div', 'wizacts'); acts.style.marginTop = '.9rem';
    var go = el('button', 'btn', isNew ? 'Create account' : 'Log in');
    function submit(){
      AUTH.email = email.value.trim();
      if (!AUTH.email){ note.textContent = 'Put your email in first.'; return; }
      if (!pw.value){ note.textContent = 'Put your password in.'; return; }
      go.disabled = true; note.className = 'authnote'; note.textContent = 'One moment…';
      post(isNew ? '/api/auth/signup' : '/api/auth/login',
           {email: AUTH.email, password: pw.value})
        .then(function(x){
          go.disabled = false;
          if (x.d.error){ note.className = 'authnote bad'; note.textContent = x.d.error; return; }
          afterAuth(x.d.entitled || x.d.paid);
        })['catch'](function(){
          go.disabled = false;
          note.className = 'authnote bad'; note.textContent = 'Network problem. Try again.';
        });
    }
    go.onclick = submit;
    pw.onkeydown = function(e){ if (e.key === 'Enter') submit(); };
    email.onkeydown = function(e){ if (e.key === 'Enter') pw.focus(); };
    acts.appendChild(go);
    var swap = el('button', 'btn ghost',
                  isNew ? 'I already have an account' : 'Create an account');
    swap.onclick = function(){ AUTH.stage = isNew ? 'login' : 'signup'; renderAuth(); };
    acts.appendChild(swap);
    b.appendChild(acts);
    setTimeout(function(){ (AUTH.email ? pw : email).focus(); }, 30);
    return;
  }

  /* The six-digit code, kept for anyone who cannot use either of the above. */
  if (AUTH.stage === 'code'){
    b.appendChild(el('h2', null, 'Check your email'));
    b.appendChild(el('p', 'sub',
      'If ' + AUTH.email + ' has access, a six-digit code is on its way. ' +
      'It expires in fifteen minutes.'));
    var code = field(b, 'authCode', 'Six-digit code', 'text',
                     {inputMode: 'numeric', autocomplete: 'one-time-code',
                      maxLength: 6, placeholder: '000000'});
    var note2 = el('div', 'authnote'); note2.id = 'authNote';
    b.appendChild(note2);
    var acts2 = el('div', 'wizacts'); acts2.style.marginTop = '.9rem';
    var ok = el('button', 'btn', 'Log in');
    ok.onclick = function(){
      ok.disabled = true; note2.textContent = 'Checking…';
      post('/api/login/verify', {email: AUTH.email, code: code.value.trim()})
        .then(function(x){
          ok.disabled = false;
          if (x.d.error){ note2.className = 'authnote bad'; note2.textContent = x.d.error; return; }
          location.href = '/app';
        })['catch'](function(){ ok.disabled = false; note2.textContent = 'Network problem.'; });
    };
    acts2.appendChild(ok);
    var back = el('button', 'btn ghost', 'Back');
    back.onclick = function(){ AUTH.stage = 'login'; renderAuth(); };
    acts2.appendChild(back);
    b.appendChild(acts2);
    setTimeout(function(){ code.focus(); }, 30);
  }
}

/* ====================================================================== */
/* The authentication page.                                               */
/*                                                                        */
/* Two tabs over one card. Every field has a visible label, its own error  */
/* line underneath, and keeps what was typed when a sibling fails -- the   */
/* thing that makes forms infuriating is being made to type it all again.  */
/* ====================================================================== */

var FORM = {tab: 'signup', values: {}, errors: {}, busy: false, notice: null};

function fieldRow(parent, opts){
  var wrap = el('div', 'field' + (FORM.errors[opts.name] ? ' bad' : ''));
  var lab = el('label', null, opts.label);
  lab.setAttribute('for', 'f_' + opts.name);
  wrap.appendChild(lab);

  var inputWrap = el('div', 'inputwrap');
  var i = el('input');
  i.id = 'f_' + opts.name;
  i.name = opts.name;
  i.type = opts.type || 'text';
  if (opts.autocomplete) i.autocomplete = opts.autocomplete;
  if (opts.inputMode) i.inputMode = opts.inputMode;
  if (opts.placeholder) i.placeholder = opts.placeholder;
  i.value = FORM.values[opts.name] || '';
  i.oninput = function(){ FORM.values[opts.name] = i.value; };
  if (FORM.errors[opts.name]){
    i.setAttribute('aria-invalid', 'true');
    i.setAttribute('aria-describedby', 'e_' + opts.name);
  }
  inputWrap.appendChild(i);

  /* Show/hide, so a long passphrase can be checked before it is submitted. */
  if (opts.type === 'password'){
    var eye = el('button', 'peek', 'Show');
    eye.type = 'button';
    eye.setAttribute('aria-label', 'Show password');
    eye.onclick = function(){
      var showing = i.type === 'text';
      i.type = showing ? 'password' : 'text';
      eye.textContent = showing ? 'Show' : 'Hide';
      eye.setAttribute('aria-label', (showing ? 'Show' : 'Hide') + ' password');
      i.focus();
    };
    inputWrap.appendChild(eye);
  }
  wrap.appendChild(inputWrap);

  if (opts.hint && !FORM.errors[opts.name]) wrap.appendChild(el('p', 'fieldhint', opts.hint));
  if (FORM.errors[opts.name]){
    var e = el('p', 'fielderr', FORM.errors[opts.name]);
    e.id = 'e_' + opts.name;
    wrap.appendChild(e);
  }
  parent.appendChild(wrap);
  return i;
}

function authNotice(kind, text, actionLabel, onAction){
  var n = el('div', 'authbanner ' + (kind || ''));
  n.appendChild(el('p', null, text));
  if (actionLabel){
    var b = el('button', 'btn mini', actionLabel);
    b.onclick = onAction;
    n.appendChild(b);
  }
  return n;
}

function submitForm(url, payload, onOk){
  if (FORM.busy) return;
  FORM.busy = true;
  FORM.errors = {};
  renderAuthPage();
  post(url, payload).then(function(x){
    FORM.busy = false;
    if (x.d.fields){ FORM.errors = x.d.fields; renderAuthPage(); focusFirstError(); return; }
    if (x.d.error){ FORM.notice = {kind: 'bad', text: x.d.error}; renderAuthPage(); return; }
    onOk(x.d);
  })['catch'](function(){
    FORM.busy = false;
    FORM.notice = {kind: 'bad', text: 'Could not reach the server. Try again.'};
    renderAuthPage();
  });
}

function focusFirstError(){
  var first = document.querySelector('.field.bad input');
  if (first) first.focus();
}

/* Where somebody lands the moment they are authenticated. Paid people go
   into the app. Everybody else stays exactly where they are: signing in and
   paying are two steps of one card, not two pages. */
function afterAuthed(d){
  var next = null;
  try { next = sessionStorage.getItem('ga-prep-after-auth');
        sessionStorage.removeItem('ga-prep-after-auth'); } catch(e){}
  if (next === 'affiliate'){ location.href = '/#affiliate'; return; }
  /* Sign up, then pay, then pick a state: the app sends anyone without a
     state to the picker on the way in, so paid people can go straight there. */
  if (d.entitled || d.paid) { location.href = '/app'; return; }
  ME.signedIn = true;
  if (FORM.values.email) ME.email = FORM.values.email;
  ME.verified = (d.verified !== false);
  if (typeof d.canPay === 'boolean') ME.canPay = d.canPay;
  /* Whether an address was actually confirmed by email is a fact about this
     deployment, not about the person. Carry it so the card can tell the
     truth about it. */
  PAY.justMade  = (d.created === true);
  PAY.emailSent = (d.emailSent === true);
  FORM.tab = 'pay';
  FORM.notice = null;
  FORM.errors = {};
  renderAuthPage();
  window.scrollTo(0, 0);
}

var PAY = {justMade: false, emailSent: false};

/* Whether this person may use the app, which is not the same question as
   whether they paid for it: the owner of the site has access without ever
   having bought it. The server decides and sends `entitled`; older
   deployments only send `paid`, so fall back to that. */
function hasAccess(){
  if (typeof ME.entitled === 'boolean') return ME.entitled;
  return !!ME.paid;
}

/* The second half of the one page: signed in, not paid yet, one button. */
function payStep(card, wrap, v){
  /* Just the plans: a heading and the four cards, nothing else to read.
     Renewal and refund terms are on Stripe's checkout page and in /terms. */
  document.title = 'Checkout \u2014 Real Estate Exam Prep';
  wrap.classList.add('planwrap');
  card.classList.add('plancardwrap');
  var mark = card.querySelector('.gatemark');
  if (mark) mark.remove();
  card.appendChild(el('h1', null, 'Choose your plan'));
  var code = refCode();
  if (code && REF.ok === null && !REF.checking){
    REF.checking = true;
    fetch('/api/affiliate/check?code=' + encodeURIComponent(code))
      .then(function(r){ return r.json(); })
      .then(function(d){ REF.ok = !!d.ok; })['catch'](function(){ REF.ok = false; })
      .then(function(){ REF.checking = false; renderAuthPage(); });
  }
  if (code && REF.ok){
    card.appendChild(el('div', 'refbanner', 'Code ' + code + ' applied \u2014 ' +
      (HOME.affiliate ? HOME.affiliate.discount : 40) + '% off your first payment'));
  }
  if (ME.canPay === false){
    /* A button that cannot take money is worse than no button. */
    card.appendChild(authNotice('warn',
      'Card payments are not connected on this site yet, so checkout cannot ' +
      'open. Nothing is wrong with your account \u2014 it is waiting for you.'));
  }
  card.appendChild(planCards());
  wrap.appendChild(card);
  v.appendChild(wrap);
}

function renderAuthPage(){
  var v = $('page');
  v.innerHTML = '';
  var q = new URLSearchParams(location.search);

  var wrap = el('div', 'authwrap');
  var card = el('div', 'authcard');

  var mark = el('div', 'gatemark');
  mark.innerHTML = '<svg viewBox="0 0 512 512" aria-hidden="true">' +
    '<path d="M256 96 L432 236 L400 236 L400 404 L112 404 L112 236 L80 236 Z" ' +
    'fill="none" stroke="currentColor" stroke-width="30" stroke-linejoin="round"/></svg>';
  card.appendChild(mark);

  /* things the server sent us back with */
  var said = {
    'ok': ['good', 'Your email is confirmed. You can log in.'],
    'bad': ['bad', 'That confirmation link is not valid or has expired. ' +
                   'Log in and we will send a new one.'],
    'needed': ['warn', 'Confirm your email address to carry on. ' +
                       'Check your inbox for the link.'],
    'sent': ['good', 'Account created. If a confirmation link reaches your ' +
                     'inbox it will secure the account; you can log in now ' +
                     'either way.']
  }[q.get('verify')];
  if (said) card.appendChild(authNotice(said[0], said[1]));
  if (q.get('gate')) card.appendChild(authNotice('warn',
    'That part of the site needs an account. Create one or log in below.'));
  if (FORM.notice) card.appendChild(authNotice(FORM.notice.kind, FORM.notice.text));

  if (q.get('reset')) return resetForm(card, wrap, v, q.get('reset'));
  if (FORM.tab === 'forgot') return forgotForm(card, wrap, v);
  /* Already signed in and unpaid, whether from a moment ago or a week ago:
     the till is this page. */
  if (ME.signedIn && hasAccess()){ location.href = '/app'; return; }
  if (FORM.tab === 'pay' || ME.signedIn) return payStep(card, wrap, v);

  /* ---- the two tabs ---- */
  var tabs = el('div', 'authtabs');
  tabs.setAttribute('role', 'tablist');
  [['signup', 'Create account'], ['login', 'Log in']].forEach(function(t){
    var b = el('button', 'authtab' + (FORM.tab === t[0] ? ' on' : ''), t[1]);
    b.setAttribute('role', 'tab');
    b.setAttribute('aria-selected', FORM.tab === t[0] ? 'true' : 'false');
    b.onclick = function(){ FORM.tab = t[0]; FORM.errors = {}; FORM.notice = null;
                            renderAuthPage(); };
    tabs.appendChild(b);
  });
  card.appendChild(tabs);

  if (ME.google){
    var g = googleButton(FORM.tab === 'signup' ? 'Sign up with Google'
                                               : 'Continue with Google');
    g.classList.add('wide');
    card.appendChild(g);
    var or = el('div', 'orline');
    or.appendChild(el('span', null, 'or use an email address'));
    card.appendChild(or);
  }

  var form = el('form', 'authform');
  form.noValidate = true;

  if (FORM.tab === 'signup'){
    fieldRow(form, {name: 'name', label: 'First name', type: 'text',
                    autocomplete: 'given-name', placeholder: 'First name'});
    fieldRow(form, {name: 'email', label: 'Email address', type: 'email',
                    autocomplete: 'email', placeholder: 'you@example.com'});
    fieldRow(form, {name: 'phone', label: 'Mobile number', type: 'tel',
                    autocomplete: 'tel', inputMode: 'tel',
                    placeholder: '(404) 555-0182',
                    hint: 'United States (+1). Used for account recovery.'});
    fieldRow(form, {name: 'password', label: 'Password', type: 'password',
                    autocomplete: 'new-password'});
    fieldRow(form, {name: 'password2', label: 'Confirm password', type: 'password',
                    autocomplete: 'new-password'});

    var termsWrap = el('div', 'field checkfield' + (FORM.errors.terms ? ' bad' : ''));
    var lab = el('label', 'checkline');
    var cb = el('input'); cb.type = 'checkbox'; cb.id = 'f_terms';
    cb.checked = !!FORM.values.terms;
    cb.onchange = function(){ FORM.values.terms = cb.checked; };
    lab.appendChild(cb);
    var txt = el('span');
    txt.appendChild(document.createTextNode('I agree to the '));
    var t1 = el('a', null, 'Terms of Service'); t1.href = '/terms'; t1.target = '_blank';
    txt.appendChild(t1);
    txt.appendChild(document.createTextNode(' and '));
    var t2 = el('a', null, 'Privacy Policy'); t2.href = '/privacy'; t2.target = '_blank';
    txt.appendChild(t2);
    txt.appendChild(document.createTextNode('.'));
    lab.appendChild(txt);
    termsWrap.appendChild(lab);
    if (FORM.errors.terms) termsWrap.appendChild(el('p', 'fielderr', FORM.errors.terms));
    form.appendChild(termsWrap);

    var go = el('button', 'btn wide', FORM.busy ? 'Creating your account…'
                                                : 'Create account');
    go.type = 'submit';
    go.disabled = FORM.busy;
    form.appendChild(go);
    form.onsubmit = function(e){
      e.preventDefault();
      submitForm('/api/auth/signup', {
        name: FORM.values.name, email: FORM.values.email, phone: FORM.values.phone,
        password: FORM.values.password, password2: FORM.values.password2,
        terms: !!FORM.values.terms
      }, afterAuthed);
    };
  } else {
    fieldRow(form, {name: 'email', label: 'Email address', type: 'email',
                    autocomplete: 'email', placeholder: 'you@example.com'});
    fieldRow(form, {name: 'password', label: 'Password', type: 'password',
                    autocomplete: 'current-password'});

    var forgot = el('button', 'linkish', 'Forgot your password?');
    forgot.type = 'button';
    forgot.onclick = function(){ FORM.tab = 'forgot'; FORM.errors = {};
                                 FORM.notice = null; renderAuthPage(); };
    form.appendChild(forgot);

    var go2 = el('button', 'btn wide', FORM.busy ? 'Signing in…' : 'Log in');
    go2.type = 'submit';
    go2.disabled = FORM.busy;
    form.appendChild(go2);
    form.onsubmit = function(e){
      e.preventDefault();
      submitForm('/api/auth/login',
                 {email: FORM.values.email, password: FORM.values.password},
                 afterAuthed);
    };
  }

  card.appendChild(form);
  wrap.appendChild(card);
  v.appendChild(wrap);
  setTimeout(focusFirstError, 30);
}

function forgotForm(card, wrap, v){
  card.appendChild(el('h1', null, 'Reset your password'));
  card.appendChild(el('p', 'gatelede',
    'Put in your email address and we will send you a link. It works for an hour.'));
  var form = el('form', 'authform');
  form.noValidate = true;
  fieldRow(form, {name: 'email', label: 'Email address', type: 'email',
                  autocomplete: 'email', placeholder: 'you@example.com'});
  var go = el('button', 'btn wide', FORM.busy ? 'Sending…' : 'Send the link');
  go.type = 'submit'; go.disabled = FORM.busy;
  form.appendChild(go);
  var back = el('button', 'linkish', 'Back to log in');
  back.type = 'button';
  back.onclick = function(){ FORM.tab = 'login'; FORM.notice = null; renderAuthPage(); };
  form.appendChild(back);
  form.onsubmit = function(e){
    e.preventDefault();
    submitForm('/api/auth/forgot', {email: FORM.values.email}, function(){
      /* The same answer whether or not that address is registered. */
      FORM.tab = 'login';
      FORM.notice = {kind: 'good', text: 'If that address has an account, a reset ' +
                                         'link is on its way. Check your inbox.'};
      renderAuthPage();
    });
  };
  card.appendChild(form);
  wrap.appendChild(card);
  v.appendChild(wrap);
}

function resetForm(card, wrap, v, token){
  card.appendChild(el('h1', null, 'Choose a new password'));
  var form = el('form', 'authform');
  form.noValidate = true;
  fieldRow(form, {name: 'password', label: 'New password', type: 'password',
                  autocomplete: 'new-password'});
  fieldRow(form, {name: 'password2', label: 'Confirm new password', type: 'password',
                  autocomplete: 'new-password'});
  var go = el('button', 'btn wide', FORM.busy ? 'Saving…' : 'Save and sign in');
  go.type = 'submit'; go.disabled = FORM.busy;
  form.appendChild(go);
  form.onsubmit = function(e){
    e.preventDefault();
    submitForm('/api/auth/reset', {token: token, password: FORM.values.password,
                                   password2: FORM.values.password2}, afterAuthed);
  };
  card.appendChild(form);
  wrap.appendChild(card);
  v.appendChild(wrap);
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

function reducedMotion(){
  try { return matchMedia('(prefers-reduced-motion: reduce)').matches; }
  catch(e){ return false; }
}

/* The stylesheet opts into a cross-document transition, but the browser only
   runs one if the incoming page reaches first paint inside its budget, and a
   1.17 MB document does not. Measured: pageswap reported "plain". So do the
   fade here rather than trusting a transition that silently declines. */
/* ------------------------------------------------------ choosing a state */
/* Start studying asks one thing first: which state's exam. The choice is
   kept on this device (STATE_KEY, a two-letter code) for the app to read.
   Only Georgia has its own state-law material so far; any other state gets
   the national material, which every state's exam shares, and says so. */
var STATE_KEY = 'ga-prep-state';
var US_STATES = [
  ['AL','Alabama'],['AK','Alaska'],['AZ','Arizona'],['AR','Arkansas'],
  ['CA','California'],['CO','Colorado'],['CT','Connecticut'],['DE','Delaware'],
  ['FL','Florida'],['GA','Georgia'],['HI','Hawaii'],['ID','Idaho'],
  ['IL','Illinois'],['IN','Indiana'],['IA','Iowa'],['KS','Kansas'],
  ['KY','Kentucky'],['LA','Louisiana'],['ME','Maine'],['MD','Maryland'],
  ['MA','Massachusetts'],['MI','Michigan'],['MN','Minnesota'],
  ['MS','Mississippi'],['MO','Missouri'],['MT','Montana'],['NE','Nebraska'],
  ['NV','Nevada'],['NH','New Hampshire'],['NJ','New Jersey'],
  ['NM','New Mexico'],['NY','New York'],['NC','North Carolina'],
  ['ND','North Dakota'],['OH','Ohio'],['OK','Oklahoma'],['OR','Oregon'],
  ['PA','Pennsylvania'],['RI','Rhode Island'],['SC','South Carolina'],
  ['SD','South Dakota'],['TN','Tennessee'],['TX','Texas'],['UT','Utah'],
  ['VT','Vermont'],['VA','Virginia'],['WA','Washington'],
  ['WV','West Virginia'],['WI','Wisconsin'],['WY','Wyoming']
];
var STATES_READY = ['GA'];              // states with their own law material

function savedState(){
  var c; try { c = localStorage.getItem(STATE_KEY); } catch(e){ c = null; }
  return US_STATES.some(function(r){ return r[0] === c; }) ? c : '';
}

/* The exam at a glance for one state, from greprep/states.json. Only what an
   official source states; anything it does not is left out, never guessed. */
function stateFacts(code){
  var f = (HOME.states || {})[code];
  if (!f) return null;
  var box = el('div', 'statefacts');
  var dl = el('dl');
  function row(k, v, sub){
    if (v === undefined || v === null || v === '') return;
    var dt = el('dt', null, k), dd = el('dd');
    if (typeof v === 'string') dd.textContent = v; else dd.appendChild(v);
    if (sub) dd.appendChild(el('small', null, sub));
    dl.appendChild(dt); dl.appendChild(dd);
  }
  var exam = f.single ? ('One ' + f.state + '-question exam')
    : (f.national && f.state) ? (f.national + ' national + ' + f.state + ' state questions')
    : f.national ? (f.national + ' national questions') : null;
  row('The exam', exam || f.note, (exam && f.note && !f.single) ? f.note : null);
  row('To pass', f.pass || 'See the official handbook');
  if (f.minutes) {
    var h = Math.floor(f.minutes / 60), m = f.minutes % 60;
    row('Time', (h ? h + ' hr' : '') + (h && m ? ' ' : '') + (m ? m + ' min' : ''));
  }
  row('Course first', f.hours ? f.hours + ' hours' : null, f.hours_note);
  row('Given by', f.vendor);
  if (f.license) row('License', f.license);
  if (f.fee) row('Exam fee', '$' + f.fee, f.fee_note || null);
  box.appendChild(dl);
  var links = el('p', 'statelinks');
  var a1 = el('a', null, f.regulator); a1.href = f.regulator_url;
  a1.target = '_blank'; a1.rel = 'noopener';
  var a2 = el('a', null, 'official source'); a2.href = f.src;
  a2.target = '_blank'; a2.rel = 'noopener';
  links.appendChild(a1);
  links.appendChild(document.createTextNode(' \u00b7 '));
  links.appendChild(a2);
  box.appendChild(links);
  return box;
}

/* ------------------------------------------------- the affiliate program */
/* Reached from "Join program" on the plans. Three states: how it works with
   a way to sign up; signed in, one tap to get a code; and the code itself,
   with a share link and ideas for spreading it. */
var AFF = {loaded: false, info: null, busy: false, error: '', mode: 'signup',
           values: {}, fields: {}, fresh: false};
var REF_KEY = 'ga-prep-ref';          // an affiliate code brought in by a link
var REF = {ok: null, checking: false};  // is that code live? asked once

function renderAffiliate(v){
  var wrap = el('div', 'gatewrap statewrap affwrap');
  var card = el('div', 'gatecard affcard');
  wrap.appendChild(card);
  v.appendChild(wrap);
  document.body.classList.add('onescreen');

  if (!AFF.loaded){
    card.appendChild(el('p', 'gatelede', 'Loading…'));
    fetch('/api/affiliate', {credentials: 'same-origin'})
      .then(function(r){ return r.json(); })
      .then(function(d){ AFF.info = d; })['catch'](function(){ AFF.info = null; })
      .then(function(){ AFF.loaded = true; if (HOME.page === 'affiliate') render(); });
    return;
  }
  var info = AFF.info || {};
  var aff = HOME.affiliate || {discount: 40, share: 25};
  if (info.code) return affiliateHome(card, info.code, aff);

  var mark = el('div', 'gatemark');
  mark.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" ' +
    'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">' +
    '<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M17 8v6M14 11h6"/></svg>';
  card.appendChild(mark);
  card.appendChild(el('h1', null, 'Become an affiliate'));
  card.appendChild(el('p', 'gatelede',
    'Share the site with people studying for their real estate exam, and earn ' +
    'money every time they sign up with your code.'));
  var steps = el('ol', 'affsteps');
  [['Get your own promo code',
    'Join below and your code is made on the spot — it is yours alone.'],
   ['Share it',
    'Anyone who uses your code gets ' + aff.discount + '% off their first payment ' +
    'on the weekly, monthly or yearly plan.'],
   ['Earn ' + aff.share + '% of every payment',
    'Not just the first one — you earn on every renewal for as long as they ' +
    'stay subscribed.']].forEach(function(r, i){
    var li = el('li');
    li.appendChild(el('span', 'affno', String(i + 1)));
    var body = el('div');
    body.appendChild(el('b', null, r[0]));
    body.appendChild(el('p', null, r[1]));
    li.appendChild(body);
    steps.appendChild(li);
  });
  card.appendChild(steps);
  if (AFF.error) card.appendChild(authNotice('bad', AFF.error));

  /* Signed in already: one tap for the code. */
  if (info.signedIn){
    var acts = el('div', 'gateacts');
    var join = el('button', 'btn wide', AFF.busy ? 'Making your code…' : 'Get my promo code');
    join.disabled = AFF.busy;
    join.onclick = function(){ makeCode(info); };
    acts.appendChild(join);
    acts.appendChild(affBack());
    card.appendChild(acts);
    return;
  }

  /* Not signed in: email and password, right here, then the code. */
  var login = AFF.mode === 'login';
  var form = el('form', 'authform affform');
  form.noValidate = true;
  function input(name, label, type, auto){
    var f = el('div', 'field' + (AFF.fields[name] ? ' bad' : ''));
    var lab = el('label', null, label); lab.htmlFor = 'aff_' + name;
    var i = el('input'); i.id = 'aff_' + name; i.type = type; i.autocomplete = auto;
    i.value = AFF.values[name] || '';
    i.oninput = function(){ AFF.values[name] = i.value; };
    f.appendChild(lab); f.appendChild(i);
    if (AFF.fields[name]) f.appendChild(el('p', 'fielderr', AFF.fields[name]));
    form.appendChild(f);
  }
  input('email', 'Email address', 'email', 'email');
  input('password', 'Password', 'password', login ? 'current-password' : 'new-password');
  if (!login){
    input('password2', 'Confirm password', 'password', 'new-password');
    var tw = el('div', 'field checkfield' + (AFF.fields.terms ? ' bad' : ''));
    var tl = el('label', 'checkline');
    var cb = el('input'); cb.type = 'checkbox'; cb.checked = !!AFF.values.terms;
    cb.onchange = function(){ AFF.values.terms = cb.checked; };
    tl.appendChild(cb);
    var tt = el('span');
    tt.appendChild(document.createTextNode('I agree to the '));
    var t1 = el('a', null, 'Terms of Service'); t1.href = '/terms'; t1.target = '_blank';
    tt.appendChild(t1); tt.appendChild(document.createTextNode('.'));
    tl.appendChild(tt); tw.appendChild(tl);
    if (AFF.fields.terms) tw.appendChild(el('p', 'fielderr', AFF.fields.terms));
    form.appendChild(tw);
  }
  var go = el('button', 'btn wide', AFF.busy ? 'Making your code…'
    : (login ? 'Log in and get my code' : 'Get my promo code'));
  go.type = 'submit'; go.disabled = AFF.busy;
  form.appendChild(go);
  form.onsubmit = function(e){
    e.preventDefault();
    if (AFF.busy) return;
    AFF.busy = true; AFF.error = ''; AFF.fields = {}; render();
    var v2 = AFF.values;
    var req = login
      ? post('/api/auth/login', {email: v2.email, password: v2.password})
      : post('/api/auth/signup', {email: v2.email, password: v2.password,
                                  password2: v2.password2, terms: !!v2.terms, affiliate: true});
    req.then(function(x){
      if (x.d.fields || x.d.error){
        AFF.busy = false;
        AFF.fields = x.d.fields || {};
        AFF.error = x.d.error || '';
        render();
        return;
      }
      AFF.busy = false;
      makeCode({signedIn: true});
    })['catch'](function(){
      AFF.busy = false; AFF.error = 'Could not reach the server. Try again.'; render();
    });
  };
  card.appendChild(form);
  var sw = el('button', 'linkish', login ? 'New here? Sign up instead'
                                         : 'Already have an account? Log in');
  sw.type = 'button';
  sw.onclick = function(){ AFF.mode = login ? 'signup' : 'login'; AFF.fields = {}; AFF.error = ''; render(); };
  card.appendChild(sw);
  var acts2 = el('div', 'gateacts');
  acts2.appendChild(affBack());
  card.appendChild(acts2);
}

function affBack(){
  var back = el('button', 'btn ghost wide', 'Back');
  back.type = 'button';
  back.onclick = function(){ if (history.length > 1) history.back(); else location.href = '/'; };
  return back;
}

/* Ask the server for this account's code, then show it. */
function makeCode(info){
  AFF.busy = true; AFF.error = ''; render();
  fetch('/api/affiliate/join', {method: 'POST', credentials: 'same-origin'})
    .then(function(r){ return r.json(); })
    .then(function(d){
      AFF.busy = false;
      if (d.code){ AFF.info = Object.assign({}, info, {signedIn: true, code: d.code}); AFF.fresh = true; }
      else AFF.error = d.error || 'Could not make your code. Try again.';
      /* now signed in either way: ME should know, for Continue */
      return fetch('/api/me', {credentials: 'same-origin'}).then(function(r){ return r.json(); })
        .then(function(me){ if (me) ME = me; });
    })['catch'](function(){ AFF.busy = false; AFF.error = 'Could not reach the server. Try again.'; })
    .then(function(){ render(); });
}

/* The affiliate's own page: the code, the link, the money, the ideas. */
function affiliateHome(card, code, aff){
  card.classList.add('affhome');
  card.appendChild(el('h1', null, AFF.fresh ? 'Here is your promo code' : 'Your promo code'));
  card.appendChild(authNotice('good', 'Save this code. We will email you a confirmation.'));
  card.appendChild(el('p', 'gatelede', 'Anyone who uses it gets ' + aff.discount +
    '% off their first payment. You earn ' + aff.share + '% of every payment they ' +
    'make, renewals included.'));

  function copyRow(label, value, cls){
    var row = el('div', 'affcopy ' + (cls || ''));
    row.appendChild(el('span', 'afflabel', label));
    var box = el('div', 'affbox');
    box.appendChild(el('code', null, value));
    var b = el('button', 'btn', 'Copy');
    b.type = 'button';
    b.onclick = function(){
      var done = function(){ b.textContent = 'Copied'; setTimeout(function(){ b.textContent = 'Copy'; }, 1600); };
      try { navigator.clipboard.writeText(value).then(done, done); } catch(e){ done(); }
    };
    box.appendChild(b);
    row.appendChild(box);
    return row;
  }
  var link = location.origin + '/?code=' + encodeURIComponent(code);
  card.appendChild(copyRow('Your code', code, 'big'));
  card.appendChild(copyRow('Your link — applies the code for them', link));
  var top = el('button', 'btn wide affcontinue', 'Continue');
  top.onclick = function(){ location.href = hasAccess() ? '/' : '/auth?pay=1'; };
  card.appendChild(top);

  /* What one referral is worth, from the real prices. */
  var earn = el('div', 'affearn');
  earn.appendChild(el('span', 'afflabel', 'What one sign-up earns you'));
  var tbl = el('div', 'affearngrid');
  (HOME.plans || []).forEach(function(p){
    if (!p.cents) return;
    var first = p.cents * (100 - aff.discount) / 100 * aff.share / 100;
    var later = p.cents * aff.share / 100;
    var d = el('div');
    d.appendChild(el('b', null, p.name));
    d.appendChild(el('span', null, money(Math.round(first)) + ' on the first ' + p.per));
    d.appendChild(el('span', null, money(Math.round(later)) + ' every ' + p.per + ' after'));
    tbl.appendChild(d);
  });
  earn.appendChild(tbl);
  card.appendChild(earn);

  /* Ideas for bringing people in. */
  var ideas = el('div', 'affideas');
  ideas.appendChild(el('h2', null, 'Ways to get people using your code'));
  [['TikTok and Instagram Reels',
    'Film a quick "studying for my real estate exam" video: show a practice question, ' +
    'guess the answer, reveal the explanation. Put your code on screen and in the caption.'],
   ['Post your study routine',
    'A day-in-the-life, your study plan counting down to test day, or your mock exam ' +
    'score going up. People studying for the same exam relate to it.'],
   ['Put it in your bio',
    'Add your link to your Instagram, TikTok and YouTube bios so every video sends people to it.'],
   ['YouTube and YouTube Shorts',
    'Short tips on tricky topics — agency, contracts, real estate math — then point to the ' +
    'site for practice questions with every answer explained.'],
   ['Tell your classmates',
    'Anyone in your pre-licensing course is studying for the same test. Share your code in ' +
    'the class group chat.'],
   ['Refer friends and family',
    'Know someone thinking about getting their license? Send them your link.'],
   ['Brokerages and new agents',
    'If you work with a brokerage, share it with people they are bringing on who still have ' +
    'to pass the exam.'],
   ['Real estate groups',
    'Facebook groups and forums for new agents and exam takers — where the rules allow, ' +
    'answer questions and share your link.']].forEach(function(r){
    var d = el('div', 'affidea');
    d.appendChild(el('b', null, r[0]));
    d.appendChild(el('p', null, r[1]));
    ideas.appendChild(d);
  });
  card.appendChild(ideas);

  var why = el('div', 'affwhy');
  why.appendChild(el('h2', null, 'What to say about the site'));
  var ul = el('ul', 'planlist');
  [(HOME.totals ? HOME.totals.total.toLocaleString('en-US') + '+' : 'Hundreds of') +
     ' practice questions, every answer explained the moment you answer',
   'Mock exams scored the way the real exam is, national and state parts separately',
   'A study plan built around your test date, so you always know what to do next',
   'Lessons on every topic, flashcards, vocabulary and real estate math step by step',
   'Works on any phone, and your progress is saved on every device',
   'Your code gets them ' + aff.discount + '% off their first payment'].forEach(function(t){
    ul.appendChild(el('li', null, t));
  });
  why.appendChild(ul);
  card.appendChild(why);

  card.appendChild(el('p', 'gatefine',
    'When you share, say you earn from your code (for example "#ad" or "I earn a ' +
    'commission") — it is required by law. Payouts are monthly; we will email you ' +
    'at your account address to set up how you get paid.'));
  /* Continue: on to paying. Having a code is not access -- the study site
     is for paid accounts only, affiliates included. */
  var acts = el('div', 'gateacts');
  var cont = el('button', 'btn wide', 'Continue');
  cont.onclick = function(){ location.href = hasAccess() ? '/' : '/auth?pay=1'; };
  acts.appendChild(cont);
  card.appendChild(acts);
}

/* Start studying lands here first; Back (or the browser's back) returns home. */
function openApp(){
  HOME.page = 'state';
  try { history.pushState({page: 'state'}, '', '#state'); } catch(e){}
  render();
  window.scrollTo(0, 0);
}

function renderState(v){
  /* With accounts, the order is sign up, then state, then the app: nobody
     reaches this screen without an account. */
  if (!HOME.openAccess && !HOME.preview && !ME.signedIn){
    location.replace('/auth');
    return;
  }
  var wrap = el('div', 'gatewrap statewrap');
  var card = el('div', 'gatecard statecard');
  var mark = el('div', 'gatemark');
  mark.innerHTML = '<svg viewBox="0 0 512 512" aria-hidden="true">' +
    '<path d="M256 96 L432 236 L400 236 L400 404 L112 404 L112 236 L80 236 Z" ' +
    'fill="none" stroke="currentColor" stroke-width="30" stroke-linejoin="round"/></svg>';
  card.appendChild(mark);
  card.appendChild(el('h1', null, 'Which state are you studying for?'));
  card.appendChild(el('p', 'gatelede',
    'Pick the state where you will take your licensing exam.'));

  var field = el('div', 'field statefield');
  var label = el('label', null, 'Your state');
  label.htmlFor = 'statePick';
  var pick = el('select');
  pick.id = 'statePick';
  var none = el('option', null, 'Choose your state');
  none.value = '';
  pick.appendChild(none);
  US_STATES.forEach(function(r){
    var o = el('option', null, r[1]);
    o.value = r[0];
    pick.appendChild(o);
  });
  pick.value = savedState();
  field.appendChild(label);
  field.appendChild(pick);
  card.appendChild(field);

  var facts = el('div', 'statefactswrap');
  facts.setAttribute('aria-live', 'polite');
  card.appendChild(facts);
  var note = el('p', 'statenote');
  card.appendChild(note);

  var acts = el('div', 'gateacts');
  var go = el('button', 'btn wide', 'Continue');
  var back = el('button', 'btn ghost wide', 'Back');
  acts.appendChild(go);
  acts.appendChild(back);
  card.appendChild(acts);

  function sync(){
    var code = pick.value;
    go.disabled = !code;
    facts.innerHTML = '';
    var fx = code ? stateFacts(code) : null;
    if (fx) facts.appendChild(fx);
    var name = '';
    US_STATES.forEach(function(r){ if (r[0] === code) name = r[1]; });
    note.textContent = (!code || STATES_READY.indexOf(code) >= 0) ? '' :
      name + '\u2019s own state-law questions are on the way. For now, study ' +
      'the national sections \u2014 they are on every state\u2019s exam. The ' +
      'state sections in the app are Georgia\u2019s.';
  }
  pick.onchange = sync;
  sync();

  go.onclick = function(){
    if (!pick.value) return;
    try { localStorage.setItem(STATE_KEY, pick.value); } catch(e){}
    if (HOME.openAccess) return goToApp();
    /* Signed in: into the app if they have it, otherwise on to paying. */
    location.href = hasAccess() ? '/app' : '/auth?pay=1';
  };
  back.onclick = function(){
    /* Arrived from the front page: step back through history. Arrived on
       #state directly: there is nothing behind it, so swap in the front page. */
    if (history.state && history.state.page === 'state') return history.back();
    HOME.page = 'welcome';
    try { history.replaceState(null, '', location.pathname + location.search); } catch(e){}
    render();
  };

  wrap.appendChild(card);
  v.appendChild(wrap);
  document.body.classList.add('onescreen');   // one screen, like the front page
  pick.focus();
}

function goToApp(){
  var href = HOME.appHref || '/buy';
  if (reducedMotion()){ location.href = href; return; }
  document.body.classList.add('leaving');
  setTimeout(function(){ location.href = href; }, 170);
}

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
  if (q.get('gate')) return 'That part is inside the app. Sign in below to get to it.';
  if (q.get('auth') === 'cancelled') return 'Sign-in was cancelled. Nothing happened.';
  if (q.get('auth') === 'expired') return 'That sign-in took too long. Try again.';
  if (q.get('auth') === 'failed') return 'Google could not sign you in. Try again.';
  if (q.get('auth') === 'unavailable') return 'Google sign-in is not switched on yet.';
  /* Somebody who has just deleted their account lands here signed out. Saying
     nothing would look like the button had failed. */
  if (q.get('deleted')) return 'Your account and everything on it have been ' +
                               'deleted. Nothing is kept.';
  if (q.get('cancelled')) return 'Payment cancelled. Nothing was charged, and ' +
                                 'your account is still here.';
  return null;
}

/* ------------------------------------------------------- the minimal page */
/* Sign up, sign in, pay. Nothing else competing for the decision.
   HOME.layout picks this over the long welcome page; both are built from the
   same data, so switching back is one flag in the build. */
function renderMinimal(v, q){
  var wrap = el('div', 'gatewrap');
  var card = el('div', 'gatecard');

  var note = noticeFor(q);
  if (note) card.appendChild(el('div', 'gatenote', note));

  var mark = el('div', 'gatemark');
  mark.innerHTML = '<svg viewBox="0 0 512 512" aria-hidden="true">' +
    '<path d="M256 96 L432 236 L400 236 L400 404 L112 404 L112 236 L80 236 Z" ' +
    'fill="none" stroke="currentColor" stroke-width="30" stroke-linejoin="round"/></svg>';
  card.appendChild(mark);

  card.appendChild(el('h1', null, 'Pass the real estate exam.'));
  card.appendChild(el('p', 'gatelede',
    'A study plan built around your test date, ' +
    HOME.totals.total.toLocaleString('en-US') + ' practice questions, and ' +
    'mock exams scored the way the real one is — national and Georgia parts ' +
    'separately.'));

  var acts = el('div', 'gateacts');

  /* Signed in with access: nothing left to sell. */
  if (!HOME.openAccess && ME.signedIn && hasAccess()){
    card.appendChild(el('p', 'whoami', 'Signed in as ' + ME.email));
    var go = el('button', 'btn wide', 'Continue studying');
    go.onclick = function(){ location.href = '/app'; };
    acts.appendChild(go);
    if (ME.paid){
      var manage = el('button', 'btn ghost wide', 'Manage subscription');
      manage.onclick = manageSubscription;
      acts.appendChild(manage);
    }
    card.appendChild(acts);
    card.appendChild(previewList());
    var out = el('button', 'linkish', 'Sign out');
    out.onclick = signOut;
    card.appendChild(out);
    wrap.appendChild(card); v.appendChild(wrap);
    return;
  }

  /* Signed in, not paid: one thing to do. */
  if (!HOME.openAccess && ME.signedIn && !hasAccess()){
    card.appendChild(el('p', 'whoami', 'Signed in as ' + ME.email));
    var pay = el('button', 'btn wide', 'Choose a plan');
    pay.onclick = function(){ location.href = '/auth?pay=1'; };
    acts.appendChild(pay);
    card.appendChild(acts);
    card.appendChild(previewList());
    card.appendChild(el('p', 'gatefine', 'Plans from ' + fromPrice() +
      '. Cancel any time.'));
    var out2 = el('button', 'linkish', 'Use a different account');
    out2.onclick = signOut;
    card.appendChild(out2);
    wrap.appendChild(card); v.appendChild(wrap);
    return;
  }

  /* Open access: no accounts behind this host. */
  if (HOME.openAccess){
    var open = el('button', 'btn wide', 'Start studying');
    open.onclick = openApp;
    acts.appendChild(open);
    card.appendChild(acts);
    card.appendChild(previewList());
    wrap.appendChild(card); v.appendChild(wrap);
    return;
  }

  /* Not signed in: one primary way in, which is the auth page. */
  var start = el('button', 'btn wide', 'Start studying');
  start.onclick = function(){ location.href = '/auth'; };
  acts.appendChild(start);
  var already = el('button', 'btn ghost wide', 'I already have an account');
  already.onclick = function(){ location.href = '/auth?tab=login'; };
  acts.appendChild(already);
  card.appendChild(acts);
  card.appendChild(previewList());
  card.appendChild(el('p', 'gatefine', 'Plans from ' + fromPrice() +
    '. Cancel any time.'));
  wrap.appendChild(card);
  v.appendChild(wrap);
}

/* --------------------------------------------------- the 3D study machine */
/* The path a student takes, as a machine filling the first screen: study plan,
   lessons, practice, mock exam, pass. Pure garnish -- the card works the
   moment the page paints, and three.js (assets/hero3d.js, ~160 KB gzipped)
   only loads once the stage is on screen. No WebGL, a data-saver connection
   or a failed load and the stage removes itself, leaving the card alone. */
var HERO = null;
var HERO_STEPS = ['Study plan', 'Lessons', 'Practice', 'Mock exam', 'Pass'];

function dropHero(){
  if (HERO && HERO.dispose) HERO.dispose();
  HERO = null;
}

function mountHero(v){
  var wrap = v.querySelector('.gatewrap');
  var conn = navigator.connection;
  if (!wrap || (conn && conn.saveData) || !window.IntersectionObserver) return;

  var stage = el('div', 'hero3d');
  var scene = el('div', 'hero3d-scene');
  scene.setAttribute('role', 'img');
  scene.setAttribute('aria-label', 'A model of the study path as a machine: ' +
    'study plan, lessons, practice, mock exam, pass. A card rides the belt ' +
    'from one station to the next.');
  stage.appendChild(scene);

  var nav = el('div', 'hero3d-steps');
  nav.setAttribute('role', 'group');
  nav.setAttribute('aria-label', 'Look at a step');
  var buttons = HERO_STEPS.map(function(name, i){
    var b = el('button', 'hero3d-step');
    b.type = 'button';
    b.setAttribute('aria-pressed', 'false');
    b.appendChild(el('span', 'no', String(i + 1).padStart(2, '0')));
    b.appendChild(document.createTextNode(name));
    nav.appendChild(b);
    return b;
  });
  stage.appendChild(nav);
  wrap.classList.add('has3d');
  wrap.appendChild(stage);

  var token = HERO = {};
  var focused = -1;
  function showFocus(i){
    focused = i;
    buttons.forEach(function(b, j){ b.setAttribute('aria-pressed', String(j === i)); });
  }
  function showStep(i){
    buttons.forEach(function(b, j){ b.classList.toggle('live', j === i); });
  }
  /* One screen, no scrolling. Wide screens always: the CSS sheds the extras
     (feature list, icon, fine print) as the window gets shorter. A phone too
     short for even the headline and button scrolls instead of cutting them
     off -- and then the wheel and a finger go back to the page. */
  var sceneApi = null;
  function fit(){
    var body = document.body;
    body.classList.add('onescreen');
    if (matchMedia('(max-width: 980px)').matches &&
        wrap.scrollHeight > wrap.clientHeight + 1)
      body.classList.remove('onescreen');
    if (sceneApi) sceneApi.setInteractive(body.classList.contains('onescreen'));
  }
  var fitQueued = false;
  function refit(){
    if (fitQueued) return;
    fitQueued = true;
    requestAnimationFrame(function(){ fitQueued = false; fit(); });
  }
  function unfit(){
    window.removeEventListener('resize', refit);
    document.body.classList.remove('onescreen');
  }
  fit();
  window.addEventListener('resize', refit);

  function giveUp(){
    if (HERO !== token) return;
    HERO = null;
    unfit();
    stage.remove();
    wrap.classList.remove('has3d');
  }

  var seen = new IntersectionObserver(function(entries){
    if (!entries[0].isIntersecting) return;
    seen.disconnect();
    var src = new URL('assets/hero3d.js', document.baseURI).href;
    import(src).then(function(mod){
      if (HERO !== token) return;           // the page re-rendered meanwhile
      if (!mod.supported()) return giveUp();
      var api = mod.mount(scene, {
        onStep: showStep,
        onFocus: showFocus,
        onReady: function(){ stage.classList.add('ready'); },
        /* matches the CSS breakpoint where the words sit on the scene */
        frameRight: function(){ return matchMedia('(min-width: 981px)').matches; },
        interactive: function(){ return document.body.classList.contains('onescreen'); }
      });
      if (!api) return giveUp();
      sceneApi = api;
      token.dispose = function(){ unfit(); api.dispose(); };
      buttons.forEach(function(b, i){
        b.onclick = function(){
          var next = (focused === i) ? -1 : i;  // a second press goes back out
          api.focus(next);
          showFocus(next);
        };
      });
    })['catch'](giveUp);
  }, {rootMargin: '200px'});
  seen.observe(stage);
  token.dispose = function(){ unfit(); seen.disconnect(); };
}

/* What you get, in four lines. Not statistics, not cards, not a pitch. */
function previewList(){
  var list = el('ul', 'preview');
  [['Study plan', 'paced to your test date'],
   ['Lessons', 'every topic on the exam blueprint'],
   ['Practice questions', 'scored National and Georgia separately'],
   ['Saved progress', 'on every device you sign in to']
  ].forEach(function(r){
    var li = el('li');
    li.appendChild(el('b', null, r[0]));
    li.appendChild(el('span', null, r[1]));
    list.appendChild(li);
  });
  return list;
}

/* ------------------------------------------------------- the welcome page */
function renderWelcome(v, q){
  var t = HOME.totals;

  var hero = el('div', 'hero2'), w = el('div', 'wrap');
  var note = noticeFor(q);
  if (note) w.appendChild(el('div', 'gatenote', note));

  w.appendChild(el('div', 'kicker2', HOME.openAccess
    ? 'Georgia salesperson licence \u00b7 Built to the real exam blueprint'
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
    ? 'Accounts and saved progress are on the way.'
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
  dropHero();
  document.body.classList.remove('onescreen');
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
  if (HOME.page === 'auth') return renderAuthPage();
  if (HOME.page === 'state') return renderState(v);
  if (HOME.page === 'affiliate') return renderAffiliate(v);
  if (HOME.page === 'buy' && !HOME.preview){
    location.replace(ME.signedIn ? '/auth?pay=1' : '/auth');
    return;
  }
  if (HOME.page === 'buy') return renderBuy(v, q);
  if (HOME.layout === 'minimal'){ renderMinimal(v, q); mountHero(v); return; }
  return renderWelcome(v, q);
}

/* ------------------------------------------------------------------ boot */
(function(){
  playIntro();

  /* Back out of the app and the browser may restore this page from bfcache
     exactly as it was left -- mid-fade, at opacity zero. Clear it on every
     show, or the front door comes back invisible. */
  window.addEventListener('pageshow', function(){
    document.body.classList.remove('leaving');
  });

  applyTheme(readTheme());
  /* #state is the state screen: it survives a reload, and the browser's
     Back leaves it for the front page. */
  /* Arrived through an affiliate's link (?code=JORDAN27): keep the code for
     checkout and tidy the address bar. */
  try {
    var qc = new URLSearchParams(location.search).get('code');
    if (qc && /^[A-Za-z0-9]{3,24}$/.test(qc)){
      localStorage.setItem(REF_KEY, qc.toUpperCase());
      var u = new URL(location.href); u.searchParams.delete('code');
      history.replaceState(history.state, '', u.pathname + u.search + u.hash);
    }
  } catch(e){}
  if (location.hash === '#state') HOME.page = 'state';
  if (location.hash === '#affiliate') HOME.page = 'affiliate';
  window.addEventListener('popstate', function(){
    var want = (location.hash === '#state') ? 'state'
             : (location.hash === '#affiliate') ? 'affiliate' : 'welcome';
    if (HOME.page === want) return;
    HOME.page = want;
    render();
  });
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
  $('buyBtn').textContent = HOME.openAccess ? 'Start studying'
    : (onBuyPage ? ('Pay ' + money(HOME.price))
                 : (ME.signedIn ? 'Continue studying' : 'Start studying'));
  $('buyBtn').onclick = function(){
    if (HOME.openAccess) return openApp();
    if (ME.signedIn && hasAccess()){ location.href = '/app'; return; }
    if (!ME.signedIn){ location.href = '/auth'; return; }
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
  /* The card says something different to a stranger, to somebody signed in
     who has not paid, and to somebody who has. Only the server knows which,
     so ask before drawing rather than drawing twice. */
  var q0 = new URLSearchParams(location.search);
  if (q0.get('tab') === 'login') FORM.tab = 'login';
  if (HOME.openAccess || HOME.preview){ render(); return; }
  /* Including on /auth, which needs to know before it decides what to show. */
  fetch('/api/me', {credentials: 'same-origin'})
    .then(function(r){ return r.json(); })
    .then(function(me){ if (me) ME = me; })
    ['catch'](function(){})
    .then(function(){ render(); });
})();
