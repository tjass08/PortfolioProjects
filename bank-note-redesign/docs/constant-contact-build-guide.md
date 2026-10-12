# Building the new Bank Note in Constant Contact

How to build the redesigned issue with Constant Contact’s standard drag-and-drop blocks. No custom code. The working mockup is `prototype/bank-note-prototype.html`. Open it in a browser and turn on **Show Constant Contact blocks** to see which block builds each section.

## One-time setup: build a master template

1. Copy a recent Bank Note campaign so the header, colors and footer carry over.
2. Delete everything between the header image and the footer.
3. Build the skeleton below with placeholder text in every block, such as “HEADLINE: what happened or what to do.”
4. Name it **Bank Note MASTER (do not send)** and copy it each week instead of last week’s issue. Copying last week’s issue is how old content and old structure creep back in.
5. Set the global styles once (fonts, link color, button color) so every weekly copy inherits them. Stick with Arial or another web-safe font so desktop Outlook renders it as designed.

## The skeleton, block by block

| # | Section | Constant Contact block | Notes |
| --- | --- | --- | --- |
| 0 | Subject and preheader | Email settings | Subject names the top story. The preheader adds a second reason to open and doesn’t repeat the subject. |
| 1 | Header | Image block | Current Bank Note banner, unchanged |
| 2 | Date and read time | Text block | “Thursday, Oct. 8, 2026 · 3-minute read” |
| 3 | In this issue | Text block with a light section fill | 4 to 6 one-line teasers, plain text (see below) |
| 4 | Section label | Text block with a blue fill | Reuse this one label block for every section: copy it and change the words. |
| 5 | Top story | Image + Text block, Text block, Button block | Headline, one-sentence lede, **Why it matters:**, 1 or 2 bullets, one button |
| 6 | Sponsor ad 1 | Image block (linked) | Highest-value ad position, right below the top story |
| 7 | Policy and industry | Text blocks separated by Divider blocks | 2 or 3 items: bold headline, 1 to 2 sentences, **Why it matters:** plus a link |
| 8 | By the numbers | 2-column layout: Text block and Text block | One big stat on the left, context and **Your next step:** on the right |
| 9 | Sponsor ad 2 | Image block | |
| 10 | Coming up | Text block | Bold date, one line, one link. Events, education and deadlines live here and nowhere else. |
| 11 | Sponsor ads 3 and 4 | 2-column layout: Image block and Image block | Square ads side by side |
| 12 | From the IBA | Image block and Text block | At most one IBA story. Full features live on the website. |
| 13 | People and Places | Image block (headshot strip) and Text block | Split into **Deals** and **Moves**, one line each |
| 14 | Banking in the Community | Image + Text block (image left) | Photo, 2 sentences, submit link |
| 15 | Member Spotlight | Image + Text block, Text block (sponsor line) | About 50 words plus “Read her story” |
| 16 | Photo of the week | Image block and Text block | The closing “happy card” |
| 17 | Sponsor ad 5 | Image block | |
| 18 | Footer | Text block and the required Footer block | Feedback question, editor email, legal footer |

Sections 12 to 16 are the standing member sections. They stay in the same order every week so readers learn where to find them.

## Things Constant Contact won’t do, and the workaround

- **No jump links.** Constant Contact’s editor doesn’t support anchor links inside an email, and its staff say Gmail and Outlook handle them poorly. “In this issue” is a plain-text scan list. That still meets the goal: telling a banker in a few seconds whether to keep reading.
- **No per-reader content.** Everyone gets the same issue. Order the issue for the typical banker and let “In this issue” do the personalizing.
- **Image + Text blocks stack on phones.** That’s fine. Keep images small (150 to 200 pixels wide) so a phone reader isn’t scrolling past a giant headshot.

## Tag links so clicks show by section

Constant Contact’s click report lists clicks by URL. For a section-level view in Google Analytics, add the same UTM tags to each link, changing only `utm_content`:

```
?utm_source=banknote&utm_medium=email&utm_campaign=bn-2026-10-08&utm_content=top-story
```

Use `top-story`, `policy-1`, `policy-2`, `numbers`, `coming-up`, `from-iba`, `people-places`, `community`, `spotlight`, `photo`. After 8 to 12 issues you’ll know which sections earn clicks. That data answers the open questions in `proposed-structure.md` better than opinions will.

## Weekly production checklist

1. Copy the master. Pick the top story first: “Is this the most important thing for an Iowa banker this week?”
2. Fill sections top to bottom. If a section has nothing good this week, delete it. Don’t fill it for the sake of filling it.
3. Write “In this issue,” the subject and the preheader last.
4. Check the length. Target 900 words or less, not counting the footer. (The prototype is 748.)
5. Have policy staff check every “Why it matters” line on regulatory items.
6. Send tests to a phone and to desktop Outlook, with images on and off.
7. Score the issue against `redesign-checklist.md`.

## Same template for IBMC and IBIS

Each company keeps its own Constant Contact account, contacts and billing, and nothing here changes that. Once the Bank Note master works, rebuild the same skeleton in the IBMC and IBIS accounts with their own header, colors and section names. The writing format (headline, lede, Why it matters, link) carries over unchanged.

## Sponsor considerations

The prototype keeps all five ad units from the Oct. 8 issue. A shorter issue helps sponsors: each ad sits closer to the top, so more readers scroll past it. Before launch:

- Confirm sponsor contracts allow the new ad positions.
- Confirm the Member Spotlight sponsor accepts a one-line credit (“brought to you by IBA associate member Abrigo”) in place of the full paragraph, or link the full description.
- Consider whether five ads in a 750-word issue is too heavy. Four may read better, with the fifth position rotating.
