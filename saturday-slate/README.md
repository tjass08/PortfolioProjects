# Saturday Slate

A weekly, shareable football **publication** across three leagues — **College**, **NFL**, and **Iowa high school (Des Moines metro)** — with Central kickoff times, TV, lines, a premium front page, playoff outlooks, and Iowa / Iowa State / the Vikings featured in depth.

- **Live artifact:** https://claude.ai/artifact/NUTViU2hjxQhx7y2SGdGLF
- **Shareable page:** [`saturday-slate.html`](../saturday-slate.html) (repo root) — a self-contained standalone build.

## Files

| File | Purpose |
| --- | --- |
| `saturday-slate/fragment.html` | The source. Holds the `DATA` object (everything the page shows) plus styles and the render script. Published to the Claude artifact. |
| `saturday-slate/build.mjs` | Wraps the fragment in a full HTML document → writes `../saturday-slate.html`. |
| `saturday-slate.html` (root) | The built standalone page you can open or host directly. |
| `saturday-slate/editions/` | Immutable weekly snapshots (`YYYY-MM-DD-weekN.html`) + `manifest.json` (dates, predictions). Archive of every Thursday edition. |

## What the page includes

- **Cover / front page** (cross-league, above the league toggles): masthead + edition date, a Thursday **Briefing**, the five biggest **Storylines**, a ranked **Big Board** of the best games across all three leagues, **superlatives** (biggest rivalry / most at stake / best upset shot), an **Iowa Spotlight**, and a cross-league **Kickoff Windows** timeline.
- **League toggles** (College · NFL · Iowa HS) — preserved — each with: Game of the Week hero, **Tyler's Teams** (now with playoff-probability bars, trend, standing, recent form & next game), a **Playoff Outlook / Race** section (standings + risers/fallers), the filterable slate, and rankings.
- **Enhanced previews**: marquee games expand to *Why it matters*, *What to watch*, *Key matchup*, each team's keys, *Upset watch*, and a clearly-labeled **projection** (winner, score, confidence).

## `DATA` object (what to edit each week)

Top level: `updated`, `edition {label,date,briefing}`, `storylines[]`, `bigBoard[]`, `superlatives{rivalry,stakes,upset}`, `iowaSpotlight{text,bullets[]}`, then `college` / `nfl` / `hs`.

Each league: `label, tag, sub, gameOfWeek, teams[], games[]`, plus `poll` (college) and `playoffRace {title,sub,standings?,cols[],note}`.

Each featured **team** may carry `playoff {standing, trend:"up"|"down"|"flat", trendText, bars[], paths[], threats[], note}` and `form {recent[],upcoming[]}`. A `bar` is either numeric (`lo,hi,disp,src,asOf`) or a `scenario:true` (`disp,src,asOf`).

Each **game** may add `matters, watch, matchup, keys{away,home}, upset, pick{winner,score,conf,confLabel,rationale}` for a deep preview (keep routine games compact).

## How the numbers work (methodology)

- **Playoff / postseason odds** are **published third-party estimates** — ESPN FPI, betting-market implied probabilities, and public simulation models — each cited with a **source** and an **as-of date**, and shown as a **range** when models disagree. They are *not* a proprietary model. The CFP committee adds selection uncertainty no win-loss model fully captures.
- **College Football Playoff (2026 format):** 12 teams — automatic bids to the ACC, Big Ten, Big 12 and SEC champions plus the top Group-of-5 champion; the other seven are at-large by the committee's final ranking; the four highest-ranked teams get first-round byes.
- **Iowa HS (Class 5A):** the 16-team field is set purely by **RPI** — there is no public probability model, so we show RPI position and qualification scenarios, never a manufactured percentage.
- Where no defensible number exists (Iowa State's CFP odds; all HS), we show standings/scenarios instead.
- **Projections** (winner/score/confidence) are editorial, clearly labeled — not verified facts or betting advice. We never fabricate stats, injuries, lines or results; unverifiable fields are left blank/`null`.

## Updating each week

1. Edit the `DATA` object in `saturday-slate/fragment.html` (times are **Central**; leave a field `null` if you can't verify it). Refresh the front page (`edition.briefing`, `storylines`, `bigBoard`, `superlatives`, `iowaSpotlight`), each team's `playoff`/`form`, and each league's `playoffRace`.
2. Rebuild: `node saturday-slate/build.mjs`
3. Snapshot the edition: `cp saturday-slate.html saturday-slate/editions/<YYYY-MM-DD>-week<N>.html` and add it to `editions/manifest.json`.
4. Publish `fragment.html` to the Claude artifact (same URL) and commit + push.

Runs automatically every Thursday morning. **College coverage includes Friday-night games** (`day:"FRI"`, tagged by conference).

## Limits (honest)

This is a **static** page refreshed weekly — no backend or live API. Game-day live scores/weather and an in-page archive browser are intentionally **not** wired in (they'd add runtime fragility); past editions live in `editions/` and in git history.
