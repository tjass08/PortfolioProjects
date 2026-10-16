# Bank Note custom-code template for Constant Contact

| File | Use it for |
| --- | --- |
| `bank-note-template.html` | The blank starter. Paste it into Constant Contact’s custom code editor and save it as the Bank Note template. |
| `bank-note-sample-2026-10-08.html` | The same template filled with the Oct. 8, 2026, issue, so you can see how real content fits |
| `build_template.py` | Regenerates both files if the design changes (`python3 build_template.py`) |

## First-time setup

1. In Constant Contact, create a custom code email. Select everything in the code window, delete it and paste in the whole `bank-note-template.html` file.
2. Turn on **Live Preview** to see it render.
3. **Swap the placeholder images.** Every image points to a gray placeholder (`placehold.co`). Upload the real images to the Constant Contact library, then replace each `src="https://placehold.co/..."` with the library URL. You can also click inside the old URL and use **Insert > Image**. Upload images at twice the display width so they stay sharp: 1104 pixels for full-width ads, 1200 for full-width photos, 300 to 360 for small photos.
4. Replace the logo placeholder with a white IBA logo. The header itself is live text, not an image, so “BANK NOTE” still shows when Outlook blocks images.
5. Save it as the Bank Note template. Ask Constant Contact whether their conversion makes sections editable in the drag-and-drop editor or keeps it in code. If it stays code, follow the weekly steps below.

## Editing each week

Each section is marked with a comment that’s easy to spot in the editor, for example `<!-- ===== TOP STORY ===== -->`. Edit only the words between tags.

- **Preheader:** the first `<div>` after `<body>`. Custom code emails don’t have a preheader field, so it lives here.
- **Repeating items:** to add a policy item, copy everything from one `<!-- HIT -->` to the next. To add a webinar day, copy one `<!-- WEBINAR DAY -->` row.
- **Links:** every `href="#"` is a placeholder. Paste the real URL, with UTM tags, between the quotes.
- **Never type** `[#`, `${` or `<@`. Constant Contact rejects custom code that contains them.

## Before every send

- Check that the legal footer, with the address and unsubscribe link, appears in a test send. Constant Contact should add it automatically to custom code emails, but confirm on the first send.
- Send tests to desktop Outlook, Gmail and a phone. Also check once with images turned off.
- Keep the file under about 100 KB, or Gmail cuts off the end with a “View entire message” link. The sample issue is 36 KB.

## What’s built in

- Table layout with inline styles, which desktop Outlook needs.
- Two-column sections (top story photo, By the numbers, side-by-side ads, Community, Spotlight) stack into one column on phones.
- Light color scheme set, so phones in dark mode are less likely to repaint the blues.
- Every image has alt text and a fixed width, so the layout holds when images are blocked.
