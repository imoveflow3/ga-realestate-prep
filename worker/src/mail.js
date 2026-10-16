/* Sending email, free: through the site's own Gmail account over SMTP.

   Gmail accepts mail from an account it can sign in to with an app password
   (Google Account -> Security -> App passwords), and delivers it as a real
   message from that address -- so it lands in inboxes, not spam, without a
   domain of our own. About 500 messages a day, which is plenty here.

   Set with:   wrangler secret put GMAIL_APP_PASSWORD
   and GMAIL_USER (the address) in wrangler.toml [vars].

   Resend is still used instead if RESEND_API_KEY is set (it needs a domain).
   Without 2-Step Verification there are no app passwords; then a Google Apps
   Script in the same account sends instead (MAIL_SCRIPT_URL / _SECRET).
   The socket module only exists on Cloudflare, so it is imported when a
   message is actually sent -- the tests, which never reach here, can run in
   Node. */

export function emailConfigured(env) {
  return !!(env.RESEND_API_KEY || (env.GMAIL_USER && env.GMAIL_APP_PASSWORD) ||
            (env.MAIL_SCRIPT_URL && env.MAIL_SCRIPT_SECRET));
}

export async function sendMail(env, to, subject, text) {
  if (env.RESEND_API_KEY) return sendResend(env, to, subject, text);
  if (env.GMAIL_USER && env.GMAIL_APP_PASSWORD) {
    try {
      await sendGmail(env, to, subject, text);
      return {};
    } catch (e) {
      console.error('email: Gmail refused:', e.message);
      return { error: 'email-send-failed' };
    }
  }
  if (env.MAIL_SCRIPT_URL && env.MAIL_SCRIPT_SECRET) return sendScript(env, to, subject, text);
  return { error: 'email-not-configured' };
}

/* The no-2-Step-Verification route: a Google Apps Script web app running in
   the site's Gmail account (worker/mail-script.gs) sends the message with
   MailApp. It only acts on requests carrying the shared secret. Apps Script
   answers a POST with a redirect to the result, which fetch follows. */
async function sendScript(env, to, subject, text) {
  try {
    const res = await fetch(env.MAIL_SCRIPT_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify({ secret: env.MAIL_SCRIPT_SECRET, to: safeAddress(to),
                             subject, text,
                             name: env.MAIL_FROM_NAME || 'Real Estate Exam Prep' }),
      redirect: 'follow',
    });
    const out = (await res.text()).trim();
    if (res.ok && out === 'ok') return {};
    console.error('email: script said', res.status, out.slice(0, 200));
    return { error: 'email-send-failed' };
  } catch (e) {
    console.error('email: script unreachable:', e.message);
    return { error: 'email-send-failed' };
  }
}

async function sendResend(env, to, subject, text) {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`,
               'Content-Type': 'application/json' },
    body: JSON.stringify({ from: env.FROM_EMAIL || 'login@example.com',
                           to: [to], subject, text }),
  });
  return res.ok ? {} : { error: 'email-send-failed' };
}

/* ------------------------------------------------------------------ SMTP */

const b64 = (s) => btoa(String.fromCharCode(...new TextEncoder().encode(s)));

/* "Subject" and the sender's name may carry non-ASCII (an em dash, say);
   RFC 2047 wraps them so every mail client shows them right. */
const header = (s) => /^[\x20-\x7e]*$/.test(s) ? s : `=?UTF-8?B?${b64(s)}?=`;

/* An address as typed by a customer must never smuggle in a header. */
function safeAddress(a) {
  const s = String(a || '').trim();
  if (!/^[^\s<>@,;]+@[^\s<>@,;]+$/.test(s)) throw new Error('bad address');
  return s;
}

function buildMessage(from, fromName, to, subject, text) {
  /* The body goes out base64-encoded: no line can start with a lone "."
     (which would end the message early), and any character is safe. */
  const body = b64(text.replace(/\r?\n/g, '\r\n')).replace(/.{1,76}/g, '$&\r\n');
  const id = `<${crypto.randomUUID()}@${from.split('@')[1]}>`;
  return [
    `From: ${header(fromName)} <${from}>`,
    `To: <${to}>`,
    `Subject: ${header(subject)}`,
    `Date: ${new Date().toUTCString()}`,
    `Message-ID: ${id}`,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: base64',
    '',
    body,
  ].join('\r\n');
}

async function sendGmail(env, rawTo, subject, text) {
  const from = safeAddress(env.GMAIL_USER);
  const to = safeAddress(rawTo);
  const { connect } = await import('cloudflare:sockets');
  /* Port 465 is TLS from the first byte, so the password never crosses
     the wire in the clear. */
  const socket = connect({ hostname: 'smtp.gmail.com', port: 465 },
                         { secureTransport: 'on', allowHalfOpen: false });
  const writer = socket.writable.getWriter();
  const reader = socket.readable.getReader();
  const enc = new TextEncoder(), dec = new TextDecoder();
  let buffer = '';

  /* One reply: lines until the one whose 4th character is a space
     ("250-..." continues, "250 ..." ends). */
  async function reply() {
    for (;;) {
      const lines = buffer.split('\r\n');
      for (let i = 0; i < lines.length - 1; i++) {
        if (/^\d{3} /.test(lines[i])) {
          buffer = lines.slice(i + 1).join('\r\n');
          return { code: Number(lines[i].slice(0, 3)), text: lines.slice(0, i + 1).join(' ') };
        }
      }
      const { value, done } = await reader.read();
      if (done) throw new Error('connection closed');
      buffer += dec.decode(value, { stream: true });
    }
  }
  async function say(line, want) {
    await writer.write(enc.encode(line + '\r\n'));
    const r = await reply();
    if (!want.includes(r.code)) throw new Error(`${line.split(' ')[0]} -> ${r.text.slice(0, 160)}`);
    return r;
  }

  try {
    const hello = await reply();
    if (hello.code !== 220) throw new Error('greeting ' + hello.text.slice(0, 160));
    await say('EHLO realestateexamprep', [250]);
    await say('AUTH LOGIN', [334]);
    await say(b64(from), [334]);
    await say(b64(String(env.GMAIL_APP_PASSWORD).replace(/\s+/g, '')), [235]);
    await say(`MAIL FROM:<${from}>`, [250]);
    await say(`RCPT TO:<${to}>`, [250, 251]);
    await say('DATA', [354]);
    const msg = buildMessage(from, env.MAIL_FROM_NAME || 'Real Estate Exam Prep', to, subject, text);
    await say(msg + '\r\n.', [250]);
    await writer.write(enc.encode('QUIT\r\n')).catch(() => {});
  } finally {
    try { await socket.close(); } catch (e) { /* already closed */ }
  }
}
