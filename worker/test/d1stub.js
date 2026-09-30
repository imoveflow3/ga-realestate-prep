/* A minimum D1 good enough to exercise the gate: the handful of statements
   the Worker actually issues, backed by plain objects. */
export function makeDB() {
  const t = { users: [], sessions: [], login_codes: [], progress: [], stripe_events: [], auth_attempts: [], tokens: [], sends: [] };
  const like = (sql, s) => sql.replace(/\s+/g, ' ').toUpperCase().includes(s);

  function run(sql, args) {
    const q = sql.replace(/\s+/g, ' ').trim();

    /* lookups by our own account id, used once payment carries it */
    if (like(q, 'SELECT ID, EMAIL, PAID FROM USERS WHERE ID')) {
      const u = t.users.find(u => u.id === args[0]);
      return u ? { id: u.id, email: u.email, paid: u.paid } : null;
    }
    if (like(q, 'SELECT ID FROM USERS WHERE ID')) {
      const u = t.users.find(u => u.id === args[0]);
      return u ? { id: u.id } : null;
    }
    if (like(q, 'SELECT ID, EMAIL, PAID FROM USERS WHERE EMAIL'))
      return t.users.find(u => u.email === args[0]) || null;
    if (like(q, 'SELECT PAID FROM USERS WHERE EMAIL')) {
      const u = t.users.find(u => u.email === args[0]);
      return u ? { paid: u.paid } : null;
    }
    if (like(q, 'SELECT ID, PAID FROM USERS WHERE EMAIL')) {
      const u = t.users.find(u => u.email === args[0]);
      return u ? { id: u.id, paid: u.paid } : null;
    }
    if (like(q, 'INSERT INTO USERS')) {
      t.users.push({ id: args[0], email: args[1], paid: 0, created_at: args[2],
                     email_verified: 0, name: null, phone: null, terms_at: null });
      return null;
    }
    if (like(q, 'UPDATE USERS SET PAID = 1')) {
      const u = t.users.find(u => u.id === args[args.length - 1]);
      if (u) { u.paid = 1; u.stripe_id = args[0]; u.paid_at = args[1]; }
      return null;
    }
    if (like(q, 'INSERT INTO SESSIONS')) {
      t.sessions.push({ id: args[0], user_id: args[1], created_at: args[2], expires_at: args[3] });
      return null;
    }
    /* The session join is handled once, further down, where it also returns
       email_verified and name. An earlier copy here won on order and left
       verification permanently undefined. */
    if (like(q, 'DELETE FROM SESSIONS WHERE ID')) {
      t.sessions = t.sessions.filter(s => s.id !== args[0]); return null;
    }
    if (like(q, 'SELECT SENT_AT FROM LOGIN_CODES'))
      return t.login_codes.find(c => c.email === args[0]) || null;
    if (like(q, 'SELECT CODE_HASH'))
      return t.login_codes.find(c => c.email === args[0]) || null;
    if (like(q, 'INSERT INTO LOGIN_CODES')) {
      t.login_codes = t.login_codes.filter(c => c.email !== args[0]);
      t.login_codes.push({ email: args[0], code_hash: args[1], expires_at: args[2],
                           attempts: 0, sent_at: args[3] });
      return null;
    }
    if (like(q, 'UPDATE LOGIN_CODES SET ATTEMPTS')) {
      const c = t.login_codes.find(c => c.email === args[0]);
      if (c) c.attempts++; return null;
    }
    if (like(q, 'DELETE FROM LOGIN_CODES')) {
      t.login_codes = t.login_codes.filter(c => c.email !== args[0]); return null;
    }
    if (like(q, 'SELECT ID, PASSWORD_HASH FROM USERS WHERE EMAIL')) {
      const u = t.users.find(u => u.email === args[0]);
      return u ? { id: u.id, password_hash: u.password_hash || null } : null;
    }
    if (like(q, 'SELECT ID, PAID, PASSWORD_HASH FROM USERS WHERE EMAIL')) {
      const u = t.users.find(u => u.email === args[0]);
      return u ? { id: u.id, paid: u.paid, password_hash: u.password_hash || null } : null;
    }
    /* Specific, because a bare 'UPDATE USERS SET PASSWORD_HASH' also matches
       the longer signup statement and was quietly eating it -- binding the
       name as the id, so the account never got a password at all. */
    if (like(q, 'UPDATE USERS SET PASSWORD_HASH = ? WHERE ID')) {
      const u = t.users.find(u => u.id === args[1]);
      if (u) u.password_hash = args[0];
      return null;
    }
    if (like(q, 'SELECT PAID FROM USERS WHERE ID')) {
      const u = t.users.find(u => u.id === args[0]);
      return u ? { paid: u.paid } : null;
    }
    if (like(q, 'SELECT FAILS, LOCKED_TILL FROM AUTH_ATTEMPTS'))
      return t.auth_attempts.find(a => a.email === args[0]) || null;
    if (like(q, 'INSERT INTO AUTH_ATTEMPTS')) {
      t.auth_attempts = t.auth_attempts.filter(a => a.email !== args[0]);
      t.auth_attempts.push({ email: args[0], fails: args[1], locked_till: args[2] });
      return null;
    }
    if (like(q, 'DELETE FROM AUTH_ATTEMPTS')) {
      t.auth_attempts = t.auth_attempts.filter(a => a.email !== args[0]); return null;
    }
    /* ---- accounts, tokens and send limits ---- */
    if (like(q, 'FROM SESSIONS S JOIN USERS U')) {
      const ses = t.sessions.find(x => x.id === args[0]);
      if (!ses) return null;
      const u = t.users.find(x => x.id === ses.user_id);
      if (!u) return null;
      return { id: u.id, email: u.email, paid: u.paid,
               email_verified: u.email_verified || 0, name: u.name || '',
               expires_at: ses.expires_at };
    }
    if (like(q, 'SELECT EMAIL, NAME, PHONE, EMAIL_VERIFIED, PAID, CREATED_AT')) {
      const u = t.users.find(x => x.id === args[0]);
      return u ? { email: u.email, name: u.name || null, phone: u.phone || null,
                   email_verified: u.email_verified || 0, paid: u.paid,
                   created_at: u.created_at } : null;
    }
    if (like(q, 'SELECT PAID, EMAIL_VERIFIED FROM USERS WHERE ID')) {
      const u = t.users.find(x => x.id === args[0]);
      return u ? { paid: u.paid, email_verified: u.email_verified || 0 } : null;
    }
    if (like(q, 'SELECT ID, PAID, PASSWORD_HASH, EMAIL_VERIFIED FROM USERS WHERE EMAIL')) {
      const u = t.users.find(x => x.email === args[0]);
      return u ? { id: u.id, paid: u.paid, password_hash: u.password_hash || null,
                   email_verified: u.email_verified || 0 } : null;
    }
    if (like(q, 'UPDATE USERS SET PASSWORD_HASH = ?, NAME = ?, PHONE = ?, TERMS_AT')) {
      const u = t.users.find(x => x.id === args[4]);
      if (u) { u.password_hash = args[0]; u.name = args[1]; u.phone = args[2];
               u.terms_at = args[3]; }
      return null;
    }
    if (like(q, 'UPDATE USERS SET PASSWORD_HASH = ?, EMAIL_VERIFIED = 1')) {
      const u = t.users.find(x => x.id === args[1]);
      if (u) { u.password_hash = args[0]; u.email_verified = 1; }
      return null;
    }
    if (like(q, 'UPDATE USERS SET EMAIL_VERIFIED = 1')) {
      const u = t.users.find(x => x.id === args[0]);
      if (u) u.email_verified = 1;
      return null;
    }
    if (like(q, 'UPDATE USERS SET NAME = ?, PHONE = ?')) {
      const u = t.users.find(x => x.id === args[2]);
      if (u) { u.name = args[0]; u.phone = args[1]; }
      return null;
    }
    if (like(q, 'DELETE FROM SESSIONS WHERE USER_ID')) {
      t.sessions = t.sessions.filter(x => x.user_id !== args[0]); return null;
    }
    if (like(q, 'DELETE FROM TOKENS WHERE USER_ID')) {
      t.tokens = t.tokens.filter(x => !(x.user_id === args[0] && x.kind === args[1]));
      return null;
    }
    if (like(q, 'DELETE FROM TOKENS WHERE HASH')) {
      t.tokens = t.tokens.filter(x => x.hash !== args[0]); return null;
    }
    if (like(q, 'INSERT INTO TOKENS')) {
      t.tokens.push({ hash: args[0], user_id: args[1], kind: args[2],
                      payload: args[3], expires_at: args[4], created_at: args[5] });
      return null;
    }
    if (like(q, 'SELECT USER_ID, PAYLOAD, EXPIRES_AT FROM TOKENS')) {
      return t.tokens.find(x => x.hash === args[0] && x.kind === args[1]) || null;
    }
    if (like(q, 'SELECT COUNT, WINDOW_FROM, LAST_AT FROM SENDS'))
      return t.sends.find(x => x.key === args[0]) || null;
    if (like(q, 'INSERT INTO SENDS')) {
      t.sends = t.sends.filter(x => x.key !== args[0]);
      t.sends.push({ key: args[0], count: args[1], window_from: args[2], last_at: args[3] });
      return null;
    }
    if (like(q, 'SELECT ID FROM STRIPE_EVENTS'))
      return t.stripe_events.find(e => e.id === args[0]) || null;
    if (like(q, 'INSERT INTO STRIPE_EVENTS')) {
      t.stripe_events.push({ id: args[0], seen_at: args[1] }); return null;
    }
    if (like(q, 'SELECT DATA FROM PROGRESS'))
      return t.progress.find(p => p.user_id === args[0]) || null;
    if (like(q, 'INSERT INTO PROGRESS')) {
      t.progress = t.progress.filter(p => p.user_id !== args[0]);
      t.progress.push({ user_id: args[0], data: args[1], updated_at: args[2] });
      return null;
    }
    throw new Error('d1stub: unhandled SQL -> ' + q.slice(0, 80));
  }

  return {
    _tables: t,
    prepare(sql) {
      let args = [];
      const api = {
        bind(...a) { args = a; return api; },
        async first() { return run(sql, args); },
        async run() { return { success: true, meta: {} }; },
      };
      // statements that mutate must still execute on .run()
      api.run = async () => { run(sql, args); return { success: true, meta: {} }; };
      return api;
    },
  };
}
