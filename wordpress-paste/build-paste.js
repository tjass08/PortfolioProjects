// Builds a script-free version of Spot the Phish that a WordPress editor without administrator
// access can paste into a Custom HTML block. WordPress strips <script>, <style>, inputs and most
// layout CSS from non-admin content, so every style here is inline and limited to properties
// WordPress keeps, and each answer is revealed with the browser's built-in <details> element.
//
// Usage: node wordpress-paste/build-paste.js
// Writes: wordpress-paste/spot-the-phish-wordpress-code.txt
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const OUT = path.join(__dirname, 'spot-the-phish-wordpress-code.txt');
const game = fs.readFileSync(path.join(ROOT, 'spot-the-phish.html'), 'utf8');

// The game keeps its scenarios and ranks as JavaScript array literals.
function arrayLiteral(startMarker) {
  const start = game.indexOf('[', game.indexOf(startMarker));
  let depth = 0;
  for (let i = start; i < game.length; i++) {
    if (game[i] === '[') depth++;
    if (game[i] === ']' && --depth === 0) return Function(`return ${game.slice(start, i + 1)}`)();
  }
  throw new Error(`no array after ${startMarker}`);
}
const scenarios = arrayLiteral('questions() {');
const ranks = arrayLiteral('const ranks =');

// WordPress turns " - " into a dash when it displays a page, and the newsletter avoids dashes.
const REWRITES = [
  ['"Mail Backup Pro" — Publisher', '"Mail Backup Pro" · Publisher'],
  ['Invoice #4471 — remittance update', 'Invoice #4471 (remittance update)'],
  ['Quick note — we', 'Quick note: we'],
  ['verification — call the vendor', 'verification. Call the vendor'],
  ['Routine collaboration — not every', 'Routine collaboration. Not every'],
  ['onto your phone — off the corporate network and past email URL scanning — to a', 'onto your phone, off the corporate network and past email URL scanning, to a'],
  ['Push notifications — 7 prompts', 'Push notifications: 7 prompts'],
  ['VPN certificate expiring — re-validate', 'VPN certificate expiring: re-validate'],
  ['windows.net — public Azure Blob', 'windows.net, which is public Azure Blob'],
  ['The basics are solid — sharpen up', 'The basics are solid. Sharpen up'],
  ['and the scopes — it clicks fast', 'and the scopes. It clicks fast'],
];
const RULES = [
  ['Verify out of band', 'A payment or banking change? Confirm it by calling a number you already trust, never one printed in the message itself.'],
  ['Scopes are the new passwords', 'Consent phishing needs no password. Treat an OAuth app asking to read your mail and files as seriously as a login prompt.'],
  ['Urgency is the weapon', 'Pressure plus secrecy is manipulation, not policy. The more a message rushes you, the more it deserves a slow second look.'],
  ["Report, don't just delete", 'Deleting protects only you. Forwarding to the security team protects everyone the same lure was sent to.'],
];

const clean = (s) => REWRITES.reduce((t, [from, to]) => t.split(from).join(to), s);
// WordPress also strips the CSS that wraps long words, so long addresses and links get zero-width
// spaces after their punctuation to give phones somewhere to break the line.
const breakable = (s) => s.replace(/\S{18,}/g, (token) => token.replace(/([./@:_%?=&-])(?=\S)/g, '$1​'));
const esc = (s) => breakable(clean(s)).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const css = (o) => Object.entries(o).map(([k, v]) => {
  if (String(v).includes('"')) throw new Error(`double quote in style value for ${k}`);
  return `${k}:${v}`;
}).join(';');
const tag = (name, style, inner, attrs = '') => `<${name}${attrs} style="${css(style)}">${inner}</${name}>`;

const C = { board: 'linear-gradient(180deg,#071425 0%,#0b1c31 100%)', card: '#0e2340', line: '#1e3a5f', well: '#0a1a2f', ink: '#e6eef7', body: '#d6e4f2', muted: '#9fb3c8', cyan: '#00a7e1', cyanText: '#4cc3ff', onCyan: '#04121f' };
const SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif";
const MONO = 'ui-monospace,SFMono-Regular,Menlo,Consolas,monospace';
const label = (color) => ({ margin: '0 0 10px', 'font-family': MONO, 'font-size': '12px', 'letter-spacing': '1.5px', 'text-transform': 'uppercase', color, 'font-weight': '700' });
const heading = (size) => ({ margin: '0 0 12px', 'font-family': SANS, 'font-size': size, 'font-weight': '800', 'line-height': '1.15', color: '#ffffff', 'letter-spacing': '-0.5px' });
const para = (extra = {}) => ({ margin: '0 0 14px', 'font-family': SANS, 'font-size': '16px', 'line-height': '1.6', color: C.body, ...extra });
const DIFFICULTY = { Tricky: ['#0f3d2a', '#4ade80'], Expert: ['#3d2a0a', '#ffb648'], Nightmare: ['#3d1212', '#ff6b63'] };
const pill = (text, [bg, fg]) => tag('span', { 'background-color': bg, color: fg, padding: '3px 9px', 'border-radius': '999px', 'font-size': '11px', 'letter-spacing': '1.5px' }, esc(text));

function scenarioCard(q, i) {
  const verdict = q.isPhish
    ? tag('p', { margin: '0 0 12px', padding: '10px 14px', 'border-radius': '8px', 'background-color': '#3d1212', 'border-left': '4px solid #ff5a52', color: '#ffd9d6', 'font-family': SANS, 'font-size': '16px', 'font-weight': '700' }, `<strong>PHISHING</strong> · ${esc(q.term)}`)
    : tag('p', { margin: '0 0 12px', padding: '10px 14px', 'border-radius': '8px', 'background-color': '#0f3d2a', 'border-left': '4px solid #2fd47e', color: '#c9f7dc', 'font-family': SANS, 'font-size': '16px', 'font-weight': '700' }, '<strong>LEGITIMATE</strong> · This one is safe');
  const rule = tag('p', { margin: '0', padding: '12px 14px', border: `1px solid ${C.line}`, 'border-radius': '8px', 'background-color': C.well, color: C.body, 'font-family': SANS, 'font-size': '15px', 'line-height': '1.55' },
    `${tag('span', { 'font-family': MONO, 'font-size': '12px', 'letter-spacing': '1.5px', 'text-transform': 'uppercase', color: C.cyanText, 'font-weight': '700' }, 'Ranger&#8217;s rule')}<br>${esc(q.takeaway)}`);
  const message = tag('div', { 'background-color': C.well, 'border-left': `4px solid ${C.cyan}`, 'border-radius': '8px', padding: '12px 14px', margin: '0 0 14px' },
    tag('p', { margin: '0 0 6px', 'font-family': MONO, 'font-size': '13px', 'line-height': '1.5', color: C.muted }, `From: ${esc(q.from)}`) +
    tag('p', { margin: '0 0 10px', 'font-family': SANS, 'font-size': '17px', 'font-weight': '700', 'line-height': '1.35', color: '#ffffff' }, esc(q.subject)) +
    tag('p', { margin: '0', 'font-family': SANS, 'font-size': '15px', 'line-height': '1.6', color: C.body }, esc(q.body)));
  const reveal = tag('details', { margin: '0' },
    tag('summary', { cursor: 'pointer', 'background-color': C.cyan, color: C.onCyan, 'font-family': SANS, 'font-weight': '800', 'font-size': '15px', padding: '12px 16px', 'border-radius': '10px' }, 'Phishing or legitimate? Decide, then tap to reveal') +
    tag('div', { padding: '16px 2px 2px' }, verdict + tag('p', para({ margin: '0 0 12px' }), esc(q.explain)) + rule));
  return tag('div', { 'background-color': C.card, border: `1px solid ${C.line}`, 'border-radius': '14px', padding: '18px', margin: '0 0 18px' },
    tag('p', label('#7fb2d9'), `Scenario ${i + 1} of ${scenarios.length} &nbsp;${pill(q.difficulty, DIFFICULTY[q.difficulty] || DIFFICULTY.Expert)}`) +
    tag('p', label('#ffb648'), esc(q.channel)) + message + reveal);
}

const scoreLines = ranks.map((r, i) => {
  const range = i === 0 ? `${r.min} right` : `${r.min} to ${ranks[i - 1].min - 1} right`;
  return tag('p', para({ margin: '0 0 10px' }), `${tag('strong', { color: '#ffffff' }, `${range}: ${esc(r.title)}.`)} ${esc(r.blurb)}`);
}).join('');

const ruleCards = RULES.map(([title, text], i) => tag('div', { 'background-color': C.card, border: `1px solid ${C.line}`, 'border-radius': '12px', padding: '16px 18px', margin: '0 0 12px' },
  tag('p', label(C.cyanText), `0${i + 1}`) + tag('p', { margin: '0 0 6px', 'font-family': SANS, 'font-size': '17px', 'font-weight': '800', color: '#ffffff' }, esc(title)) + tag('p', para({ margin: '0', 'font-size': '15px' }), esc(text)))).join('');

const html = tag('div', { background: C.board, color: C.ink, 'border-radius': '18px', padding: '26px 16px', margin: '0 auto', 'max-width': '860px', 'font-family': SANS, 'line-height': '1.5' },
  tag('p', label(C.cyanText), 'IBA // Cybersecurity Awareness Month') +
  tag('h2', heading('34px'), 'Can you outsmart <span style="color:#4cc3ff">the phish?</span>') +
  tag('p', para({ 'font-size': '17px' }), 'Eight real-world lures, built for people who already know the basics. The Cyber Risk Ranger says most pros miss at least two. Prove him wrong.') +
  tag('div', { 'background-color': C.well, border: `1px solid ${C.line}`, 'border-radius': '12px', padding: '14px 16px', margin: '0 0 24px' },
    tag('p', label(C.cyanText), 'How to play') +
    tag('p', para({ margin: '0', 'font-size': '15px' }), 'Read each message the way the Ranger would: the sender, the Reply-To, where any link really goes and what it asks you to do. Decide whether it&#8217;s phishing or legitimate, then tap the blue bar under it to see if you were right. Keep count as you go.')) +
  scenarios.map(scenarioCard).join('') +
  tag('div', { 'background-color': C.card, border: `1px solid ${C.cyan}`, 'border-radius': '14px', padding: '22px', margin: '6px 0 26px' },
    tag('h3', heading('24px'), 'How did you do?') + tag('p', para(), 'Count your correct calls and find your rank.') + scoreLines) +
  tag('h3', heading('24px'), 'Four rules the Ranger never breaks') + ruleCards +
  tag('p', { margin: '22px 0 0', 'font-family': MONO, 'font-size': '12px', 'letter-spacing': '1.5px', 'text-transform': 'uppercase', color: C.muted, 'text-align': 'center' }, 'In honor of Cybersecurity Awareness Month &#183; October 2026<br>Cyber Risk Ranger &#183; Iowa Bankers Association'),
  ' class="alignwide"');

for (const bad of ['—', '–', ' - ', '--', '<script', '<style', 'display:']) {
  if (html.includes(bad)) throw new Error(`output contains ${JSON.stringify(bad)}`);
}
fs.writeFileSync(OUT, html + '\n');
console.log(`${scenarios.length} scenarios, ${ranks.length} ranks -> ${path.relative(ROOT, OUT)} (${html.length.toLocaleString()} characters)`);
