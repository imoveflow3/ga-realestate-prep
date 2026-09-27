/* A minimum D1 good enough to exercise the gate: the handful of statements
   the Worker actually issues, backed by plain objects. */
export function makeDB() {
  const t = { users: [], sessions: [], login_codes: [], progress: [], stripe_events: [] };
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
      t.users.push({ id: args[0], email: args[1], paid: 0, created_at: args[2] });
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
    if (like(q, 'FROM SESSIONS S JOIN USERS U')) {
      const s = t.sessions.find(s => s.id === args[0]);
      if (!s) return null;
      const u = t.users.find(u => u.id === s.user_id);
      if (!u) return null;
      return { id: u.id, email: u.email, paid: u.paid, expires_at: s.expires_at };
    }
    if (like(q, 'DELETE FROM SESSIONS')) {
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
