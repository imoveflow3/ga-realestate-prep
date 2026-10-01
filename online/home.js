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
  wrap.appendChild(el('div', 'intro-word', 'Georgia Real Estate'));
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
      if (d.signin){ location.href = d.signin; return; }
      BUYING = false;
      toast(d.error || 'Could not start checkout. Try again shortly.');
    })['catch'](function(){
      BUYING = false;
      toast('Could not reach the payment service.');
    });
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
                    placeholder: isNew ? 'at least 8 characters' : ''});
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
          afterAuth(x.d.paid);
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

function afterAuthed(d){
  if (d.paid) { location.href = '/app'; return; }
  if (d.verified === false){ location.href = '/auth?verify=sent'; return; }
  location.href = '/?pay=1';
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
    'sent': ['good', 'Account created. Check your email for the confirmation ' +
                     'link, then log in.']
  }[q.get('verify')];
  if (said) card.appendChild(authNotice(said[0], said[1]));
  if (q.get('gate')) card.appendChild(authNotice('warn',
    'That part of the site needs an account. Create one or log in below.'));
  if (FORM.notice) card.appendChild(authNotice(FORM.notice.kind, FORM.notice.text));

  if (q.get('reset')) return resetForm(card, wrap, v, q.get('reset'));
  if (FORM.tab === 'forgot') return forgotForm(card, wrap, v);

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
    fieldRow(form, {name: 'name', label: 'Full name', type: 'text',
                    autocomplete: 'name', placeholder: 'First Last'});
    fieldRow(form, {name: 'email', label: 'Email address', type: 'email',
                    autocomplete: 'email', placeholder: 'you@example.com'});
    fieldRow(form, {name: 'phone', label: 'Mobile number', type: 'tel',
                    autocomplete: 'tel', inputMode: 'tel',
                    placeholder: '(404) 555-0182',
                    hint: 'United States (+1). Used for account recovery.'});
    fieldRow(form, {name: 'password', label: 'Password', type: 'password',
                    autocomplete: 'new-password',
                    hint: 'At least 8 characters. Length matters more than symbols.'});
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
                  autocomplete: 'new-password',
                  hint: 'At least 8 characters.'});
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
function openApp(){
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

  card.appendChild(el('h1', null,
    'Prepare for your Georgia real estate exam with a clear study plan.'));
  card.appendChild(el('p', 'gatelede',
    'Study state-specific topics, practice exam-style questions, and track ' +
    'your progress in one place.'));

  var acts = el('div', 'gateacts');

  /* Signed in and paid: nothing left to sell. */
  if (!HOME.openAccess && ME.signedIn && ME.paid){
    card.appendChild(el('p', 'whoami', 'Signed in as ' + ME.email));
    var go = el('button', 'btn wide', 'Continue studying');
    go.onclick = function(){ location.href = '/app'; };
    acts.appendChild(go);
    card.appendChild(acts);
    card.appendChild(previewList());
    var out = el('button', 'linkish', 'Sign out');
    out.onclick = signOut;
    card.appendChild(out);
    wrap.appendChild(card); v.appendChild(wrap);
    return;
  }

  /* Signed in, not paid: one thing to do. */
  if (!HOME.openAccess && ME.signedIn && !ME.paid){
    card.appendChild(el('p', 'whoami', 'Signed in as ' + ME.email));
    var price = el('div', 'gateprice');
    price.appendChild(el('span', 'amount', money(HOME.price)));
    price.appendChild(el('span', 'once', 'one payment, no subscription'));
    card.appendChild(price);
    var pay = el('button', 'btn wide');
    pay.textContent = 'Pay ' + money(HOME.price) + ' and start studying';
    pay.onclick = function(){ buy(); };
    acts.appendChild(pay);
    card.appendChild(acts);
    card.appendChild(previewList());
    card.appendChild(el('p', 'gatefine',
      'Full refund within 14 days. Nothing renews.'));
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
    card.appendChild(el('p', 'gatefine',
      'Free to use. Accounts and saved progress are on the way.'));
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
  card.appendChild(el('p', 'gatefine',
    money(HOME.price) + ' once for full access. No subscription, nothing ' +
    'renews, full refund within 14 days.'));
  wrap.appendChild(card);
  v.appendChild(wrap);
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
  if (HOME.page === 'auth') return renderAuthPage();
  if (HOME.page === 'buy') return renderBuy(v, q);
  if (HOME.layout === 'minimal') return renderMinimal(v, q);
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
    if (ME.signedIn && ME.paid){ location.href = '/app'; return; }
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
