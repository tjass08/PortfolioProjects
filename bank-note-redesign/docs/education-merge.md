# Folding the Education Bulletin into Bank Note

The Education Bulletin is being sunset. About 90% of its contacts already get Bank Note, so its content moves into Bank Note as a standing section. That serves a separate incentive goal: fewer emails to members. The mockup is `prototype/bank-note-education-merge.html`.

## Education’s requirements

| Requirement | How the section meets it |
| --- | --- |
| Every webinar listed, each with a clickable link | Every webinar between this issue and the next is listed by day, and each title is its own registration link. No “see more webinars” shortcut. |
| Other events can be highlighted, with a link to the rest | “Seminars and schools” shows 3 or 4 in-person events, plus a button to the full education calendar |
| *(Bulletin carryover)* Training tool of the week | Kept as one line with a link |

Confirm with Education: does “every webinar” mean every webinar before the next issue, or everything on the calendar? The mockup uses a rolling window, which matches what the Bulletin did.

## Section name

Recommended: **Credit Hours**. Credit is the banker’s business, and credit hours are what training earns. It works as a label, an “In this issue” line and a subject-line hook: “Credit Hours: 8 webinars next week.”

Alternatives: **Compound Interest** (learning builds on itself), **Capital Gains** (keeps the Bulletin’s “Opportunities for growth” spirit), **The Learning Ledger** (every training on the books) and **Rate Sheet** (training at a glance, in a format every banker knows).

Let Education make the final pick. Choosing the name helps them own the section. Banner images for all five are in `prototype/images/banners/` at 1200 pixels wide, ready to upload to Constant Contact at 600.

## Where it sits in the issue

Credit Hours replaces the old Coming up section, in the same position: after By the numbers and sponsor ad 2, before From the IBA. Outside deadlines (ABA surveys, regulator webinars) move to a short “Mark your calendar” item at the end of Policy and industry.

Credit Hours also gets a line in “In this issue” every week, such as “Credit Hours: 8 webinars next week, plus Mortgage Lending School.” That puts training above the fold even though the section sits mid-issue.

## Section structure (Constant Contact blocks)

1. **Banner.** Image block with the name banner. Same image every week.
2. **Featured.** Text block with a white card look and a Button block. One event that Education wants pushed hardest that week, with dates, location, one sentence and a register button.
3. **Webinars.** One Text block. Bold day (“Tue., Oct. 13”), then each webinar title as a link. Tag all-day sessions “All day.” Use one column, not the Bulletin’s two: Constant Contact stacks columns on phones, which scrambles the date order.
4. **Seminars and schools.** One Text block with 3 or 4 events. Linked name, then dates and cities on the next line. Add “Last call” to anything happening before the next issue.
5. **Training tool of the week.** One Text block, one sentence and a link.
6. **Calendar link.** Button block (“See the full education calendar”) plus a one-line “Contact IBA Education” Text block.

Give the whole section a light blue fill so it reads as its own space within Bank Note.

## Weekly workflow with Education

| When | Who | What |
| --- | --- | --- |
| Tuesday by noon | Education | Send the webinar list for the window (each title, date and link), the featured event and the tool of the week |
| Wednesday | Marketing | Build the section, write the “In this issue” line and the featured blurb |
| Wednesday | Education | Quick proof of the section: titles, dates and links |
| Thursday | Marketing | Bank Note sends |

A shared spreadsheet with columns for title, date, link, type and featured (yes or no) is easier than email. Education keeps it current, and marketing copies from it.

## Tracking (Education will want proof)

Tag every education link with UTM parameters so Google Analytics shows clicks per webinar:

```
?utm_source=banknote&utm_medium=email&utm_campaign=bn-2026-10-08&utm_content=edu-webinar-fcra
```

Use `edu-featured`, `edu-webinar-[short-name]`, `edu-seminar-[short-name]`, `edu-tool` and `edu-calendar`. Before the switch, pull 8 to 12 weeks of Education Bulletin clicks and webinar registrations from the Bulletin as the baseline. Then report the same numbers to Education monthly after the merge. If webinar registrations hold or rise, the merge has earned its keep.

## Sunsetting the Bulletin

1. **Handle the other 10%.** Export Bulletin contacts who aren’t on the Bank Note list. Decide with Education whether to add them to Bank Note, which is the same sender and the same kind of content, or invite them to subscribe. Adding them, plus an easy opt-out, keeps the most webinar reach.
2. **Send a final Bulletin**, two weeks before the switch: “Education Bulletin is moving into Bank Note. Find every webinar in Credit Hours each Thursday.” Show a screenshot of the new section.
3. **First merged issue.** Give Credit Hours the top “In this issue” line and a short note introducing the section.
4. **Retire the list** after the final send. Keep the list, but stop scheduled sends.

## Length

Adding the section takes the Oct. 8 prototype from about 750 words to about 950. About 210 of those are education listings, which bankers scan rather than read. To stay near the target, write tightly elsewhere. In a heavy news week, cut a policy item before cutting webinars.
