# Bank Note custom-code template for Constant Contact

| File | Use it for |
| --- | --- |
| `bank-note-template.html` | The blank starter. Paste it into Constant Contact’s custom code editor and save it as the Bank Note template. |
| `bank-note-sample-2026-10-08.html` | The same template filled with the Oct. 8, 2026, issue, so you can see how real content fits |
| `bank-note-template-copy.html` | A helper page with one-click Copy buttons, paste steps and a preview. Published as a private Claude artifact. |
| `build_template.py` | Regenerates both files if the design changes (`python3 build_template.py`) |
| `build_copy_page.py` | Rebuilds the copy helper page after the template changes |

## Look and feel

A modern, Axios-style design: a white page with rounded corners, a “Bank Note.” wordmark, emoji story labels and bold lead-ins (“Driving the news:”, “Why it matters:”, “Zoom in:”, “Your next step:”). Sections open with a large emoji and a short blue underline instead of solid color bars. Sponsor ads carry a small “A message from SPONSOR” label. Member Spotlight and Credit Hours sit in rounded tinted cards so they stand out.

Emoji render in color in Gmail, Apple Mail and phones. Older desktop Outlook may show some in black and white. Rounded corners appear square in desktop Outlook, which is fine.

## Section order

1. What’s in this edition
2. The top story (“1 big thing”)
3. Banking briefs: a quick news roundup, most urgent first. A brief can carry a big stat (the old By the numbers).
4. Across Iowa’s banking industry: a recognition story, People and Places, Banking in the Community and Photo of the week
5. Member Spotlight: its own gold-trimmed feature card with a large photo and a highlighted line
6. Dates and deadlines: deadlines, the Credit Hours education section (every webinar listed) and useful resources

Five sponsor ad slots sit between sections.

## First-time setup

1. In Constant Contact, create a custom code email. Select everything in the code window, delete it and paste in the whole `bank-note-template.html` file.
2. Turn on **Live Preview** to see it render.
3. **Swap the placeholder images.** Every image points to a gray placeholder (`placehold.co`). Upload the real images to the Constant Contact library, then replace each `src="https://placehold.co/..."` with the library URL. You can also click inside the old URL and use **Insert > Image**. Upload images at twice the display width so they stay sharp: 1072 pixels wide for full-width photos and ads, 516 for square ads and 280 to 400 for small photos.
4. Replace the logo placeholder with the full-color IBA logo (the header is white now). The “Bank Note.” wordmark is live text, not an image, so it still shows when Outlook blocks images.
5. Save it as the Bank Note template. Ask Constant Contact whether their conversion makes sections editable in the drag-and-drop editor or keeps it in code. If it stays code, follow the weekly steps below.

## Editing each week

Each section is marked with a comment that’s easy to spot in the editor, for example `<!-- ===== 2. THE TOP STORY (1 big thing) ===== -->`. Edit only the words between tags.

- **Preheader:** the first `<div>` after `<body>`. Custom code emails don’t have a preheader field, so it lives here.
- **Repeating items:** to add a brief, copy everything from one `<!-- BRIEF -->` to the next. Deadline rows (`<!-- DEADLINE -->`) and resources (`<!-- RESOURCE -->`) work the same way. To change an emoji, replace its code (like `&#9889;`) or paste an emoji directly. To add a webinar day, copy one `<!-- WEBINAR DAY -->` row.
- **Links:** every `href="#"` is a placeholder. Paste the real URL, with UTM tags, between the quotes.
- **Never type** `[#`, `${` or `<@`. Constant Contact rejects custom code that contains them.

## Before every send

- Check that the legal footer, with the address and unsubscribe link, appears in a test send. Constant Contact should add it automatically to custom code emails, but confirm on the first send.
- Send tests to desktop Outlook, Gmail and a phone. Also check once with images turned off.
- Keep the file under about 100 KB, or Gmail cuts off the end with a “View entire message” link. The sample issue is about 54 KB.

## What’s built in

- Table layout with inline styles, which desktop Outlook needs.
- Two-column sections (top story photo, side-by-side ads, Community, Spotlight, deadlines, webinars) stack into one column on phones.
- Light color scheme set, so phones in dark mode are less likely to repaint the blues.
- Every image has alt text and a fixed width, so the layout holds when images are blocked.
