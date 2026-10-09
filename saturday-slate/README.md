# Saturday Slate

A weekly, shareable football guide across three leagues — **College**, **NFL**, and **Iowa high school (Des Moines metro)** — with Central kickoff times, TV, lines, and Iowa / Iowa State / the Vikings featured in depth.

- **Live artifact:** https://claude.ai/artifact/NUTViU2hjxQhx7y2SGdGLF
- **Shareable page:** [`saturday-slate.html`](../saturday-slate.html) (repo root) — a self-contained standalone build.

## Files

| File | Purpose |
| --- | --- |
| `saturday-slate/fragment.html` | The source. Holds the `DATA` object (all games/teams/lines) plus styles and render script. This is what gets published to the Claude artifact. |
| `saturday-slate/build.mjs` | Wraps the fragment in a full HTML document → writes `../saturday-slate.html`. |
| `saturday-slate.html` (root) | The built standalone page you can open or host directly. |

## Updating each week

1. Edit the `DATA` object in `saturday-slate/fragment.html` (times are **Central**; leave a field `null` if you can't verify it).
2. Rebuild the standalone:
   ```
   node saturday-slate/build.mjs
   ```
3. Publish `fragment.html` to the Claude artifact (same URL as above).
4. Commit and push.

This refresh runs automatically every Thursday morning. **College coverage includes Friday-night games, not just Saturday** — Friday Power-4 matchups are tagged by conference (`day:"FRI"`) so they appear in the conference tabs.
