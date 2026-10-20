"""Builds bank-note-template-copy.html, the one-click copy helper page. Run: python3 build_copy_page.py . bank-note-template-copy.html"""
import json, sys
from pathlib import Path
d = Path(sys.argv[1]); out = Path(sys.argv[2])
blank = (d/"bank-note-template.html").read_text(); sample = (d/"bank-note-sample-2026-10-08.html").read_text()
data = json.dumps({"blank": blank, "sample": sample}).replace("</", "<\\/")
page = r'''<title>Bank Note Template</title>
<style>
/* Layout: a single working column. Steps first, the copy buttons second, the live preview last. */
:root { --bg:#eef2f7; --panel:#ffffff; --fg:#14213a; --muted:#56667e; --line:#cbd6e4; --accent:#0054a6; --accent-fg:#ffffff; --ok:#1d7a3e;
  --font:"Source Sans 3","Segoe UI",Arial,sans-serif; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#0f1724; --panel:#172235; --fg:#e3e9f3; --muted:#9db0c9; --line:#2c3b54; --accent:#7db3ff; --accent-fg:#0b1422; --ok:#6fd38f; color-scheme:dark; } }
:root[data-theme="dark"] { --bg:#0f1724; --panel:#172235; --fg:#e3e9f3; --muted:#9db0c9; --line:#2c3b54; --accent:#7db3ff; --accent-fg:#0b1422; --ok:#6fd38f; color-scheme:dark; }
* { box-sizing:border-box; }
body { background:var(--bg); color:var(--fg); font-family:var(--font); font-size:16px; line-height:1.5; padding-inline:16px; padding-block:28px 48px; }
.wrap { max-width:760px; margin:0 auto; display:flex; flex-direction:column; gap:20px; }
h1 { font-size:clamp(26px,4vw,34px); margin:0; text-wrap:balance; } h2 { font-size:19px; margin:0; }
.lead { color:var(--muted); margin:0; max-width:62ch; }
.card { background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:18px 20px; display:grid; gap:12px; }
ol { margin:0; padding-left:22px; display:grid; gap:8px; } li { padding-left:4px; }
kbd { font:600 13px ui-monospace,Menlo,Consolas,monospace; border:1px solid var(--line); border-bottom-width:2px; border-radius:4px; padding:1px 6px; background:var(--bg); }
.choices { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:12px; }
.choice { border:1px solid var(--line); border-radius:8px; padding:14px; display:grid; gap:8px; align-content:start; }
.choice p { margin:0; color:var(--muted); font-size:14px; }
button { font:700 16px var(--font); border-radius:6px; padding:11px 16px; cursor:pointer; border:1px solid var(--accent); }
button.primary { background:var(--accent); color:var(--accent-fg); }
button.ghost { background:transparent; color:var(--accent); font-size:14px; padding:7px 12px; }
button:focus-visible { outline:3px solid var(--accent); outline-offset:2px; }
.status { font-size:14px; font-weight:700; color:var(--ok); min-height:1.4em; margin:0; }
textarea { width:100%; height:120px; font:12px ui-monospace,Menlo,Consolas,monospace; border:1px solid var(--line); border-radius:6px; background:var(--bg); color:var(--fg); padding:8px; }
.tabs { display:flex; gap:8px; flex-wrap:wrap; }
.tabs button[aria-pressed="true"] { background:var(--accent); color:var(--accent-fg); }
.frame { border:1px solid var(--line); border-radius:8px; overflow:hidden; background:#e9eef5; }
iframe { display:block; width:100%; height:900px; border:0; }
.note { font-size:14px; color:var(--muted); margin:0; }
</style>
<div class="wrap">
  <header style="display:grid;gap:8px">
    <h1>Bank Note template</h1>
    <p class="lead">Copy the email with one click and paste it into Constant Contact’s code window. No coding needed.</p>
  </header>

  <section class="card">
    <h2>Pick one and copy it</h2>
    <div class="choices">
      <div class="choice">
        <strong>Blank template</strong>
        <p>Use this to set up your saved template. Every spot to fill in starts with “EDIT.”</p>
        <button class="primary" type="button" id="copy-blank">Copy blank template</button>
      </div>
      <div class="choice">
        <strong>Oct. 8 sample issue</strong>
        <p>The same design filled with a real week, so you can see how it looks finished.</p>
        <button class="primary" type="button" id="copy-sample">Copy sample issue</button>
      </div>
    </div>
    <p class="status" id="status" role="status" aria-live="polite"></p>
    <div id="fallback" style="display:grid;gap:8px">
      <p class="note"><strong>Button not working?</strong> Click inside the box below, press <kbd>Ctrl</kbd>+<kbd>A</kbd> then <kbd>Ctrl</kbd>+<kbd>C</kbd> (<kbd>Cmd</kbd> on a Mac). The box holds the <span id="fallback-kind">blank template</span>.</p>
      <textarea id="fallback-text" readonly aria-label="Template code"></textarea>
    </div>
  </section>

  <section class="card">
    <h2>Paste it into Constant Contact</h2>
    <ol>
      <li>Open your custom code email, the screen with the numbered lines.</li>
      <li>Click anywhere inside the code window.</li>
      <li>Press <kbd>Ctrl</kbd>+<kbd>A</kbd> (<kbd>Cmd</kbd>+<kbd>A</kbd> on a Mac) to select the starter code that’s there.</li>
      <li>Press <kbd>Ctrl</kbd>+<kbd>V</kbd> (<kbd>Cmd</kbd>+<kbd>V</kbd>) to paste. The starter code is replaced. Line 1 should now read <code>&lt;!DOCTYPE html&gt;</code>, with about 125 lines below it. If the window is empty, nothing was copied, so go back and use the box above.</li>
      <li>Turn on <strong>Live Preview</strong> to see the email, then click <strong>Save</strong>.</li>
    </ol>
    <p class="note">Gray boxes are placeholder images. Swap them for your real photos and ads before sending. The README in the project folder walks through that.</p>
  </section>

  <section class="card">
    <h2>Changing the words each week</h2>
    <ol>
      <li>In the code window, find the word you want to change. Every spot in the blank template starts with “EDIT,” and every section is labeled in capitals, like <strong>2. THE TOP STORY</strong>.</li>
      <li>Type over the words only. Leave anything inside &lt; &gt; brackets alone.</li>
      <li>Check Live Preview as you go. If something looks broken, press <kbd>Ctrl</kbd>+<kbd>Z</kbd> to undo.</li>
    </ol>
  </section>

  <section class="card">
    <h2>Preview</h2>
    <div class="tabs" role="toolbar" aria-label="Preview">
      <button class="ghost" type="button" id="tab-sample" aria-pressed="true">Oct. 8 sample</button>
      <button class="ghost" type="button" id="tab-blank" aria-pressed="false">Blank template</button>
    </div>
    <div class="frame"><iframe id="preview" title="Email preview" sandbox=""></iframe></div>
    <p class="note">Sample photos are shown here for reference only. In Constant Contact they start as gray placeholders.</p>
  </section>
</div>
<script type="application/json" id="data">__DATA__</script>
<script>
(function () {
  var D = JSON.parse(document.getElementById('data').textContent);
  var status = document.getElementById('status');
  var fb = document.getElementById('fallback'), fbt = document.getElementById('fallback-text');
  function copy(kind, label) {
    var text = D[kind];
    fbt.value = text; document.getElementById('fallback-kind').textContent = label;
    function fallback() {
      fbt.focus(); fbt.select();
      status.textContent = 'Automatic copy was blocked. The code is selected in the box below. Press Ctrl+C (Cmd+C on a Mac) now.';
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        status.textContent = '✓ Copied the ' + label + ' (' + text.split('\n').length + ' lines). Now paste it into Constant Contact.';
      }, fallback);
    } else { fallback(); }
  }
  fbt.value = D.blank;
  document.getElementById('copy-blank').addEventListener('click', function () { copy('blank', 'blank template'); });
  document.getElementById('copy-sample').addEventListener('click', function () { copy('sample', 'sample issue'); });

  var MAP = { 'Bowman':'bowman','SHAZAM':'ad-shazam','BOK':'ad-bok','Wipfli':'ad-wipfli','UBB':'ad-ubb','IBA+Printing':'ad-iba-printing',
    'Leaders':'leaders-advocacy','Headshots':'people-places','FreedomBank':'freedombank','Kenedy':'backes','Photo+of+the+week':'photo-of-week' };
  function box(w, h, t) {
    var svg = '<svg xmlns="http://www.w3.org/2000/svg" width="' + w + '" height="' + h + '"><rect width="100%" height="100%" fill="#c6d6ea"/>' +
      '<text x="50%" y="50%" fill="#003d7a" font-family="Arial" font-size="' + Math.max(14, Math.round(w / 18)) + '" text-anchor="middle" dominant-baseline="middle">' + t + '</text></svg>';
    return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
  }
  function previewHtml(kind) {
    return D[kind].replace(/src="https:\/\/placehold\.co\/(\d+)x(\d+)\/[^"]*?text=([^"]*)"/g, function (m, w, h, t) {
      if (kind === 'sample') { for (var k in MAP) { if (t.indexOf(k) === 0) return 'src="images/' + MAP[k] + '.jpg"'; } }
      return 'src="' + box(w, h, decodeURIComponent(t.replace(/\+/g, ' '))) + '"';
    });
  }
  var frame = document.getElementById('preview');
  var tabs = { sample: document.getElementById('tab-sample'), blank: document.getElementById('tab-blank') };
  function show(kind) {
    var base = '<base href="' + location.href.replace(/[^\/]*$/, '') + '">';
    frame.srcdoc = previewHtml(kind).replace('<head>', '<head>' + base);
    tabs.sample.setAttribute('aria-pressed', String(kind === 'sample'));
    tabs.blank.setAttribute('aria-pressed', String(kind === 'blank'));
  }
  tabs.sample.addEventListener('click', function () { show('sample'); });
  tabs.blank.addEventListener('click', function () { show('blank'); });
  show('sample');
})();
</script>
'''
out.write_text(page.replace("__DATA__", data))
print(len(page) + len(data))
