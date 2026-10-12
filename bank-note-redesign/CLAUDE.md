# Bank Note Redesign

Project context for Claude Code. Read this first, then the files in `docs/` as needed.

## Who I am

- Tyler, Marketing and Communications Specialist at the Iowa Bankers Association (IBA) in Des Moines, Iowa.
- I support communications for IBA and two affiliates: IBMC (Iowa Bankers Mortgage Corporation) and IBIS (Iowa Bankers Insurance and Services).
- Work spans email marketing, newsletter production, video, analytics, copywriting and AP style editing.

## The project

Redesign and reformat **Bank Note**, IBA’s weekly member e-newsletter for Iowa bankers. This is a major incentive comp goal for the year.

**The problem:** Bank Note is too long, and every issue leads with a feature article whether or not it’s the most important news that week.

**The goal:** A shorter, more scannable, Axios-style issue (Smart Brevity) that gets bankers to the point fast, explains why things matter and lets them choose what to read. Better banker experience, measured by clicks and registrations.

## Decisions made so far

- **Keep** the popular member sections: People and Places (promotions, new roles, M&As), Banking in the Community and Member Spotlight.
- **Replace** the automatic top feature article with the week’s most important news, written with a “Why it matters” line. A feature can still earn the top slot when it’s the biggest story.
- **Add** an “In this issue” scan list at the top so readers can pick what they want.
- **Shorten** the issue. Working target: about 900 words, 5 to 8 items, a three-minute read.
- **Model:** Axios (Smart Brevity). Quick-hitting, but with the “why it matters” depth, not just news updates.
- **Measure** success with click-based metrics, not open rate (Apple Mail Privacy Protection inflates opens).

## Where things stand

- Done: research-backed criteria report (also exists as a Claude Doc in claude.ai, titled “Bank Note Redesign: Research-Backed Criteria”). Its contents are mirrored in `docs/`.
- Done: Prototype 1, the Oct. 8, 2026, issue rebuilt in the new format and mapped to Constant Contact blocks (`prototype/`), plus a build guide, platform notes on Axios HQ and a checklist scorecard.
- Next: build the master template in Constant Contact, add UTM tags, pull baseline click data from recent issues and talk with 5 to 10 member bankers.
- Open questions are listed in `docs/proposed-structure.md`.

## Files

| File | What’s in it |
| --- | --- |
| `docs/research-findings.md` | Bottom line plus the research table (attention, skimming, length, benchmarks) |
| `docs/redesign-checklist.md` | Criteria to check every outline and weekly issue against |
| `docs/proposed-structure.md` | Draft issue skeleton with word targets and open questions |
| `docs/measurement-plan.md` | Metrics, baseline approach and test plan |
| `docs/axios-session-notes.md` | My notes from the Axios Salt Lake City speaker session |
| `docs/sources.md` | All research sources with links |
| `docs/constant-contact-build-guide.md` | Block-by-block build of the new issue in Constant Contact, UTM tagging and weekly checklist |
| `docs/platform-options.md` | Stay in Constant Contact vs. Axios HQ, with pricing and demo questions |
| `docs/prototype-scorecard.md` | Prototype 1 scored against the checklist, before and after numbers |
| `prototype/bank-note-prototype.html` | Working mockup of the Oct. 8 issue in the new format (open in a browser) |

## How to work with me

- **AP style always.** Curly (typographic) apostrophes and quotes. No Oxford comma in simple series.
- **Minimal-intervention edits** with a short, transparent explanation of what changed and why.
- **Prototype before pitch.** I’d rather see a working draft issue or template than a memo about one.
- **Behavioral outcomes over vanity metrics.** Clicks, click-to-open and registrations, not opens.
- I talk casually in working sessions, but anything audience-facing should be polished.
- Audience test for every piece of content: “Is this important to an Iowa banker, and why?”
- If AI summarizes source material (regulatory updates, reports), verify against the original.

## Likely next tasks in this repo

- Build a prototype Bank Note issue (HTML email or Markdown draft) using the proposed structure and a real week’s content.
- Create a reusable issue template and a writing guide for item formats (headline, lede, Why it matters, link).
- Score drafts against `docs/redesign-checklist.md`.
- Analyze exported email platform data (clicks by section, device mix, open times) to set a baseline.
