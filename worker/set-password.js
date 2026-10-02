/* Set a password on a local development account.
 *
 *   node set-password.js you@example.com
 *
 * Prompts for the new password without echoing it, hashes it with exactly
 * the same PBKDF2 the Worker uses, writes it to the local D1, and clears any
 * failed-attempt lockout on the way through.
 *
 * Local only. In production people reset their own password by email -- there
 * is deliberately no route that lets anybody set somebody else's.
 */
import { execFileSync } from 'node:child_process';
import readline from 'node:readline';
import { hash } from './src/password.js';

const email = (process.argv[2] || '').trim().toLowerCase();
if (!email) {
  console.error('Usage: node set-password.js you@example.com');
  process.exit(1);
}

function d1(sql) {
  return execFileSync('npx', ['wrangler', 'd1', 'execute', 'ga-prep', '--local',
                              '--command', sql, '--json'],
                      { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
}

const found = JSON.parse(d1(
  `SELECT email FROM users WHERE lower(email) = '${email.replace(/'/g, "''")}';`
))[0].results;
if (!found.length) {
  console.error(`No account on ${email}. Accounts here:`);
  for (const r of JSON.parse(d1('SELECT email FROM users;'))[0].results) {
    console.error('  ' + r.email);
  }
  process.exit(1);
}

/* Read without echoing, the way a password prompt should behave. */
function askHidden(question) {
  return new Promise(resolve => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    const onData = char => {
      if (['\n', '\r', '\u0004'].includes(char.toString())) {
        process.stdin.removeListener('data', onData);
      } else {
        process.stdout.write('\u001b[2K\u001b[200D' + question);
      }
    };
    process.stdout.write(question);
    process.stdin.on('data', onData);
    rl.question('', answer => { rl.close(); process.stdout.write('\n'); resolve(answer); });
  });
}

const pw = await askHidden('New password      : ');
const again = await askHidden('Type it again     : ');
if (!pw) { console.error('Nothing entered. Nothing changed.'); process.exit(1); }
if (pw !== again) { console.error('Those did not match. Nothing changed.'); process.exit(1); }

const stored = await hash(pw);
d1(`UPDATE users SET password_hash = '${stored}' WHERE lower(email) = '${email}';`);
d1(`DELETE FROM auth_attempts WHERE lower(email) = '${email}';`);

console.log(`\nPassword set for ${email}, and the failed-attempt count cleared.`);
console.log('You can log in now -- no need to restart the server.');
