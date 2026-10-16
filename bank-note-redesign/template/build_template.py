"""Builds the Bank Note custom-code email template for Constant Contact.

Writes two files next to this script:
  bank-note-template.html         blank starter with placeholder text
  bank-note-sample-2026-10-08.html same template filled with the Oct. 8, 2026, issue

Run: python3 build_template.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent

# Brand colors (match the current Bank Note header)
BLUE = "#0054a6"
NAVY = "#003d7a"
EDU_NAVY = "#00305f"
EDU_SKY = "#3399ff"
TINT = "#eaf2fb"
EDU_WASH = "#f2f7fd"
RULE = "#c6d6ea"
INK = "#1f2a37"
SOFT = "#4b5869"
CANVAS = "#e9eef5"
FONT = "Arial, Helvetica, sans-serif"

PH = "https://placehold.co"  # placeholder images; swap for Constant Contact library URLs


def img(src, alt, width, style=""):
    return (f'<img src="{src}" alt="{alt}" width="{width}" border="0" '
            f'style="display:block;width:100%;max-width:{width}px;height:auto;border:0;'
            f'outline:none;text-decoration:none;{style}">')


def link(text, url="#"):
    return f'<a href="{url}" style="color:{BLUE};font-weight:bold;text-decoration:underline;">{text}</a>'


def p(text, size=16, color=INK, extra=""):
    return (f'<p style="margin:0 0 10px 0;font-family:{FONT};font-size:{size}px;'
            f'line-height:1.5;color:{color};{extra}">{text}</p>')


def h(text, size=22, color=NAVY):
    return (f'<h2 style="margin:0 0 8px 0;font-family:{FONT};font-size:{size}px;'
            f'line-height:1.25;color:{color};font-weight:bold;">{text}</h2>')


def why(text, label="Why it matters:"):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" '
            f'style="margin:0 0 10px 0;"><tr><td style="border-left:4px solid {BLUE};padding:0 0 0 12px;'
            f'font-family:{FONT};font-size:16px;line-height:1.5;color:{INK};">'
            f'<strong style="color:{NAVY};">{label}</strong> {text}</td></tr></table>')


def bullets(items, size=16):
    lis = "".join(f'<li style="margin:0 0 6px 0;">{i}</li>' for i in items)
    return (f'<ul style="margin:0 0 10px 0;padding:0 0 0 22px;font-family:{FONT};'
            f'font-size:{size}px;line-height:1.45;color:{INK};">{lis}</ul>')


def button(text, url="#", bg=BLUE):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td bgcolor="{bg}" style="border-radius:4px;background:{bg};">'
            f'<a href="{url}" style="display:inline-block;padding:12px 20px;font-family:{FONT};'
            f'font-size:15px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:4px;">'
            f'{text}</a></td></tr></table>')


def row(inner, pad="18px 24px", bg="#ffffff", cls="pad"):
    return (f'<tr><td class="{cls}" bgcolor="{bg}" style="padding:{pad};background:{bg};">'
            f'{inner}</td></tr>')


def label(text, bg=BLUE):
    return row(f'<p style="margin:0;font-family:{FONT};font-size:13px;line-height:1.2;color:#ffffff;'
               f'font-weight:bold;letter-spacing:1.5px;text-transform:uppercase;">{text}</p>',
               pad="9px 24px", bg=bg)


def comment(text):
    return f"\n<!-- ===== {text} ===== -->\n"


def two_col(left, right, left_w, right_w, gap=16, valign="top"):
    """Two columns that stack on phones (class="stack")."""
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td class="stack" width="{left_w}" valign="{valign}" style="width:{left_w}px;'
            f'padding:0 {gap // 2}px 0 0;">{left}</td>'
            f'<td class="stack" width="{right_w}" valign="{valign}" style="width:{right_w}px;'
            f'padding:0 0 0 {gap // 2}px;">{right}</td></tr></table>')


def ad(src, alt, url="#"):
    return row(f'<a href="{url}">{img(src, alt, 552)}</a>', pad="12px 24px")


def build(c):
    blocks = []
    add = blocks.append

    add(comment("HEADER (text-based, so it shows even with images off)"))
    header_left = (f'<p style="margin:0;font-family:{FONT};font-size:40px;line-height:1;color:#ffffff;'
                   f'font-weight:bold;letter-spacing:3px;">BANK NOTE</p>'
                   f'<p style="margin:10px 0 0 0;font-family:{FONT};font-size:12px;line-height:1;'
                   f'color:#cfe5ff;letter-spacing:2.5px;">WEEKLY NEWS IN BRIEF</p>')
    header_right = (f'<a href="https://www.iowabankers.com">{img(c["logo"], "Iowa Bankers Association", 160)}</a>')
    add(row(two_col(header_left, header_right, 352, 160, valign="bottom"),
            pad="28px 24px 24px 24px", bg=BLUE))
    add(row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td style="font-family:{FONT};font-size:13px;color:{SOFT};">{c["date"]}</td>'
            f'<td align="right" style="font-family:{FONT};font-size:13px;color:{SOFT};">{c["read"]}</td>'
            f'</tr></table>', pad="10px 24px", cls="pad rule"))

    add(comment("IN THIS ISSUE (edit the lines; 4 to 6 items)"))
    toc = "".join(f'<tr><td width="18" valign="top" style="font-family:{FONT};font-size:15px;line-height:1.5;'
                  f'color:{BLUE};">&#9656;</td><td style="font-family:{FONT};font-size:15px;line-height:1.5;'
                  f'color:{INK};padding:0 0 4px 0;">{t}</td></tr>' for t in c["toc"])
    add(row(f'<p style="margin:0 0 8px 0;font-family:{FONT};font-size:13px;font-weight:bold;'
            f'letter-spacing:1.5px;color:{NAVY};">IN THIS ISSUE</p>'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{toc}</table>',
            bg=TINT))

    add(comment("TOP STORY"))
    add(label("Top story"))
    t = c["top"]
    add(row(two_col(h(t["hed"], 24) + p(t["lede"]), img(t["img"], t["img_alt"], 150), 386, 150)
            + why(t["why"]) + bullets(t["bullets"]) + button(t["button"])))

    add(comment("SPONSOR AD 1"))
    add(ad(c["ads"][0][0], c["ads"][0][1]))

    add(comment("POLICY AND INDUSTRY (copy a HIT block to add one; 2 or 3 per issue)"))
    add(label("Policy and industry"))
    for i, hit in enumerate(c["hits"]):
        top = f"border-top:1px solid {RULE};" if i else ""
        inner = h(hit["hed"], 18) + p(hit["body"]) + why(hit["why"] + " " + link(hit["link"]))
        add(f'<!-- HIT -->\n<tr><td class="pad" style="padding:16px 24px;background:#ffffff;">'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td style="{top}padding:{"14px" if i else "0"} 0 0 0;">{inner}</td></tr></table></td></tr>')
    cal = "".join(f'<li style="margin:0 0 6px 0;"><strong>{d}:</strong> {txt} {link(lk)}</li>'
                  for d, txt, lk in c["calendar"])
    add(f'<!-- MARK YOUR CALENDAR (outside deadlines; delete if none) -->\n'
        f'<tr><td class="pad" style="padding:0 24px 16px 24px;background:#ffffff;">'
        f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
        f'<td style="border-top:1px solid {RULE};padding:14px 0 0 0;">{h("Mark your calendar", 18)}'
        f'<ul style="margin:0;padding:0 0 0 22px;font-family:{FONT};font-size:16px;line-height:1.45;color:{INK};">'
        f'{cal}</ul></td></tr></table></td></tr>')

    add(comment("BY THE NUMBERS"))
    add(label("By the numbers", NAVY))
    n = c["numbers"]
    big = (f'<p style="margin:0;font-family:{FONT};font-size:56px;line-height:1;font-weight:bold;'
           f'color:{BLUE};">{n["big"]}</p>')
    add(row(two_col(big, p(n["text"]) + p(n["source"], 13, SOFT)
                    + why(n["next"] + " " + link(n["link"]), "Your next step:"), 130, 406, valign="middle"),
            bg=TINT))

    add(comment("SPONSOR AD 2"))
    add(ad(c["ads"][1][0], c["ads"][1][1]))

    add(comment("CREDIT HOURS: EDUCATION SECTION (replaces the Education Bulletin)"))
    badge = (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
             f'<td width="52" height="52" align="center" valign="middle" bgcolor="{EDU_SKY}" '
             f'style="width:52px;height:52px;border-radius:26px;background:{EDU_SKY};font-size:26px;'
             f'line-height:52px;">&#127891;</td></tr></table>')
    title = (f'<p style="margin:0;font-family:{FONT};font-size:28px;line-height:1.1;font-weight:bold;'
             f'color:#ffffff;">{c["edu_name"]}</p><p style="margin:5px 0 0 0;font-family:{FONT};'
             f'font-size:12px;letter-spacing:2px;color:#cfe5ff;">{c["edu_tag"]}</p>')
    add(row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td width="66" valign="middle">{badge}</td><td valign="middle">{title}</td></tr></table>',
            pad="18px 24px", bg=EDU_NAVY))

    f = c["featured"]
    add(row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td bgcolor="#ffffff" style="background:#ffffff;border:1px solid {RULE};border-top:4px solid {EDU_SKY};'
            f'padding:14px 16px;">'
            + p("FEATURED", 12, EDU_NAVY, "font-weight:bold;letter-spacing:1.5px;margin-bottom:6px;")
            + h(f["name"], 19) + p(f["when"], 14, EDU_NAVY, "font-weight:bold;") + p(f["text"])
            + button(f["button"], bg=EDU_NAVY) + '</td></tr></table>', bg=EDU_WASH))

    def edu_h(left, right):
        return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" '
                f'style="margin:0 0 10px 0;"><tr><td style="border-bottom:2px solid {EDU_SKY};padding:0 0 4px 0;'
                f'font-family:{FONT};font-size:13px;font-weight:bold;letter-spacing:1.5px;color:{EDU_NAVY};">'
                f'{left}</td><td align="right" style="border-bottom:2px solid {EDU_SKY};padding:0 0 4px 0;'
                f'font-family:{FONT};font-size:13px;color:{SOFT};">{right}</td></tr></table>')

    pill = (f' <span style="background:#cfe5ff;color:{EDU_NAVY};font-size:11px;font-weight:bold;'
            f'letter-spacing:.5px;padding:1px 5px;border-radius:3px;">ALL DAY</span>')
    days = ""
    for day, items in c["webinars"]:
        lis = "".join(f'<p style="margin:0 0 6px 0;font-family:{FONT};font-size:15px;line-height:1.35;">'
                      f'{link(name, "#")}{pill if allday else ""}</p>' for name, allday in items)
        days += (f'<!-- WEBINAR DAY -->\n<tr><td class="stack" width="100" valign="top" style="width:100px;'
                 f'padding:0 10px 8px 0;font-family:{FONT};font-size:14px;line-height:1.35;font-weight:bold;'
                 f'color:{EDU_NAVY};">{day}</td><td class="stack" valign="top" style="padding:0 0 8px 0;">'
                 f'{lis}</td></tr>')
    add('<!-- WEBINARS: list EVERY webinar until the next issue. Copy a WEBINAR DAY row per day. -->')
    add(row(edu_h(c["web_title"], c["web_note"])
            + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{days}</table>',
            pad="6px 24px 8px 24px", bg=EDU_WASH))

    sem = ""
    for name, where, last in c["seminars"]:
        tag = (f'<span style="background:#fde7c4;color:#7a4100;font-size:11px;font-weight:bold;'
               f'letter-spacing:.5px;padding:1px 5px;border-radius:3px;">LAST CALL</span> ' if last else "")
        sem += (f'<p style="margin:0 0 10px 0;font-family:{FONT};font-size:15px;line-height:1.35;">'
                f'{tag}{link(name)}<br><span style="color:{SOFT};font-size:14px;">{where}</span></p>')
    add('<!-- SEMINARS AND SCHOOLS: highlight 3 or 4 -->')
    add(row(edu_h("SEMINARS AND SCHOOLS", "In person") + sem, pad="6px 24px 4px 24px", bg=EDU_WASH))

    add('<!-- TRAINING TOOL OF THE WEEK -->')
    add(row(p(f'<strong style="color:{EDU_NAVY};">Training tool of the week:</strong> {c["tool"]} '
              + link(c["tool_link"])), pad="4px 24px 6px 24px", bg=EDU_WASH))
    add(row(button("See the full education calendar", bg=EDU_NAVY)
            + p(f'Questions about training? {link("Contact IBA Education")}', 13, SOFT, "margin:10px 0 0 0;"),
            pad="6px 24px 20px 24px", bg=EDU_WASH))

    add(comment("SPONSOR ADS 3 AND 4 (side by side; stack on phones)"))
    a3, a4 = c["ads"][2], c["ads"][3]
    add(row(two_col(f'<a href="#">{img(a3[0], a3[1], 268)}</a>', f'<a href="#">{img(a4[0], a4[1], 268)}</a>',
                    276, 276, gap=16), pad="12px 24px"))

    add(comment("FROM THE IBA (one story; full features live on the website)"))
    add(label("From the IBA"))
    i = c["iba"]
    add(row(img(i["img"], i["img_alt"], 600), pad="0", cls="flush"))
    add(row(h(i["hed"], 19) + p(i["text"]) + p(i["caption"], 13, SOFT)
            + why(i["next"] + " " + link(i["link"]), "Your next step:")))

    add(comment("PEOPLE AND PLACES"))
    add(label("People and Places", NAVY))
    sub = lambda t: p(t, 13, NAVY, "font-weight:bold;letter-spacing:1px;margin:6px 0 6px 0;")
    add(row(img(c["pp_img"], "Headshots of this week’s People and Places", 552) + '<div style="height:12px;line-height:12px;">&nbsp;</div>'
            + sub("DEALS") + bullets(c["deals"], 15) + sub("MOVES") + bullets(c["moves"], 15)))

    add(comment("BANKING IN THE COMMUNITY"))
    add(label("Banking in the Community", NAVY))
    b = c["community"]
    add(row(two_col(img(b["img"], b["img_alt"], 180), h(b["hed"], 18) + p(b["text"])
                    + p(b["foot"] + " " + link("Share your bank’s story"), 13, SOFT), 180, 356)))

    add(comment("MEMBER SPOTLIGHT"))
    add(label("Member Spotlight", NAVY))
    m = c["spotlight"]
    add(row(two_col(img(m["img"], m["img_alt"], 150), h(m["hed"], 18) + p(m["text"]) + p(link("Read the full story")),
                    150, 386)))
    add(row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td bgcolor="{TINT}" style="background:{TINT};padding:8px 12px;font-family:{FONT};font-size:13px;'
            f'line-height:1.4;color:{SOFT};">Member Spotlight is brought to you by IBA associate member '
            f'<strong>{m["sponsor"]}</strong>. {link("Nominate a banker")}</td></tr></table>', pad="0 24px 18px 24px"))

    add(comment("PHOTO OF THE WEEK (the happy card: end on something good)"))
    add(label("Photo of the week"))
    ph = c["photo"]
    add(row(img(ph["img"], ph["img_alt"], 600), pad="0", cls="flush"))
    add(row(p(ph["text"], extra="margin:0;")))

    add(comment("SPONSOR AD 5"))
    add(ad(c["ads"][4][0], c["ads"][4][1]))

    add(comment("FOOTER (Constant Contact adds the legal footer with address and unsubscribe)"))
    add(row(p(f'<strong>What would make Bank Note essential to you?</strong> '
              f'<a href="#" style="color:#ffffff;font-weight:bold;text-decoration:underline;">Tell us in one question</a>',
              16, "#ffffff")
            + p('Published by the Iowa Bankers Association. Send news to '
                '<a href="mailto:editor@iowabankers.com" style="color:#ffffff;">editor@iowabankers.com</a>.',
                13, "#cfe5ff", "margin:0;"), pad="20px 24px", bg=NAVY))

    body = "\n".join(blocks)
    return f'''<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>Bank Note</title>
<!--[if mso]><style>table,td,p,a,h2,li{{font-family:Arial,Helvetica,sans-serif !important;}}</style><![endif]-->
<style>
  body {{ margin:0 !important; padding:0 !important; width:100% !important; background:{CANVAS}; }}
  table {{ border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt; }}
  img {{ -ms-interpolation-mode:bicubic; }}
  a {{ color:{BLUE}; }}
  @media only screen and (max-width:620px) {{
    .container {{ width:100% !important; }}
    .pad {{ padding-left:16px !important; padding-right:16px !important; }}
    .stack {{ display:block !important; width:100% !important; max-width:100% !important; padding:0 0 12px 0 !important; }}
    .stack img {{ max-width:180px !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background:{CANVAS};">
<!-- PREHEADER: the gray preview line in the inbox. Constant Contact's custom code emails have no preheader field, so it lives here. -->
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{c["preheader"]}&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CANVAS}" style="background:{CANVAS};">
<tr><td align="center" style="padding:20px 10px;">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:#ffffff;">
{body}
</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr>
</table>
</body>
</html>
'''


def ph(w, hgt, text):
    return f"{PH}/{w}x{hgt}/c6d6ea/003d7a/png?text={text.replace(' ', '+')}"


BLANK = {
    "preheader": "PREHEADER: A second reason to open. Don’t repeat the subject line.",
    "logo": ph(320, 70, "IBA logo (white)"),
    "date": "Thursday, Month Day, 2026", "read": "3-minute read",
    "toc": ["Top story teaser, one line", "Policy item teaser", "By the numbers: the stat in 5 words",
            "<strong>Credit Hours</strong>: X webinars next week", "From the IBA teaser",
            "People and Places: the headline move or deal"],
    "top": {"hed": "HEADLINE: What happened or what to do", "img": ph(300, 300, "Photo 150px"), "img_alt": "PHOTO DESCRIPTION",
            "lede": "LEDE: One sentence with the news.",
            "why": "One or two sentences on what this means for an Iowa banker.",
            "bullets": ["Optional supporting detail.", "Optional supporting detail."],
            "button": "DESCRIPTIVE LINK TEXT"},
    "ads": [(ph(1104, 184, "Sponsor ad 1 (1104x184)"), "SPONSOR NAME: ad message"),
            (ph(1104, 184, "Sponsor ad 2"), "SPONSOR NAME: ad message"),
            (ph(536, 536, "Square ad 3"), "SPONSOR NAME: ad message"),
            (ph(536, 536, "Square ad 4"), "SPONSOR NAME: ad message"),
            (ph(1104, 184, "Sponsor ad 5"), "SPONSOR NAME: ad message")],
    "hits": [{"hed": "HEADLINE: What happened", "body": "One or two sentences with the news.",
              "why": "One sentence on the impact.", "link": "Descriptive link text"},
             {"hed": "HEADLINE: What happened", "body": "One or two sentences with the news.",
              "why": "One sentence on the impact.", "link": "Descriptive link text"}],
    "calendar": [("Mon. DD", "Outside deadline or event, one line.", "Link text")],
    "numbers": {"big": "00%", "text": "One sentence explaining the number.", "source": "Source: NAME OF SOURCE",
                "next": "What a banker can do about it.", "link": "Link text"},
    "edu_name": "Credit Hours", "edu_tag": "TRAINING THAT COUNTS &middot; IBA EDUCATION",
    "featured": {"name": "FEATURED EVENT NAME", "when": "Month DD &middot; City",
                 "text": "One sentence on who it’s for and why to go.", "button": "Register for EVENT"},
    "web_title": "WEBINARS NEXT WEEK", "web_note": "All X, Month DD-DD",
    "webinars": [("Mon., Oct. DD", [("Webinar title", False)]),
                 ("Tue., Oct. DD", [("Webinar title", False), ("All-day webinar title", True)])],
    "seminars": [("Seminar name", "Month DD, City", True), ("Seminar name", "Month DD, City", False),
                 ("Seminar name", "Month DD, City &middot; Month DD, City", False)],
    "tool": "One sentence on this week’s on-demand resource.", "tool_link": "Link text",
    "iba": {"img": ph(1200, 700, "IBA photo 600px wide"), "img_alt": "PHOTO DESCRIPTION", "hed": "HEADLINE",
            "text": "Two or three sentences. The full story lives on the website.",
            "caption": "Photo caption: From left, NAME, BANK; NAME, BANK; and NAME, BANK.",
            "next": "The action you want readers to take.", "link": "Link text"},
    "pp_img": ph(1104, 300, "Headshot strip"),
    "deals": ["<strong>Bank Name</strong>, City, plans to acquire HOLDING COMPANY, holding company of CITY-based BANK."],
    "moves": ["<strong>Bank Name</strong>, City: NAME promoted to TITLE.", "<strong>Bank Name</strong>, City: NAME hired as TITLE."],
    "community": {"img": ph(360, 270, "Community photo"), "img_alt": "PHOTO DESCRIPTION", "hed": "HEADLINE",
                  "text": "Two sentences on what the bank did and for whom.",
                  "foot": "Iowa banks give more than $50.4 million and 300,000 volunteer hours a year."},
    "spotlight": {"img": ph(300, 380, "Headshot"), "img_alt": "NAME", "hed": "HEADLINE",
                  "text": "About 50 words: role, bank, one memorable detail.", "sponsor": "SPONSOR NAME"},
    "photo": {"img": ph(1200, 900, "Photo of the week"), "img_alt": "PHOTO DESCRIPTION",
              "text": "One or two sentences. End on something good."},
}

SAMPLE = {
    **BLANK,
    "preheader": "Plus: 8 webinars next week, a crypto kiosk operator shut down and 2 Iowa bank deals.",
    "date": "Thursday, Oct. 8, 2026",
    "toc": ["The Fed is redrawing its supervision map", "34 states shut down a crypto kiosk operator",
            "By the numbers: Tokenized deposits are coming",
            "<strong>Credit Hours</strong>: 8 webinars next week, plus Mortgage Lending School",
            "Meet the 2026 Leaders in Advocacy grads", "People and Places: 2 Iowa bank deals"],
    "top": {"hed": "The Fed is redrawing its supervision map", "img": ph(300, 300, "Bowman"), "img_alt": "Michelle Bowman",
            "lede": "Fed Vice Chair for Supervision Michelle Bowman announced plans to organize bank supervision into five regions drawn along state lines, replacing the 12 Reserve Bank districts.",
            "why": "If the Fed supervises your bank or holding company, your examiners aren’t changing. The chain of command above them is. Each region gets one leader responsible for supervision, which the Fed says will simplify decisions and improve coordination with other regulators.",
            "bullets": ["Examiners stay in their current Reserve Bank offices and keep the banks they supervise now.",
                        "Bowman announced the plan at the Community Banking Research Conference in St. Louis."],
            "button": "Read Bowman’s speech"},
    "ads": [(ph(1104, 184, "SHAZAM ad"), "SHAZAM: There’s only one you"),
            (ph(1104, 184, "BOK Financial ad"), "BOK Financial Capital Markets"),
            (ph(536, 536, "Wipfli ad"), "Wipfli"), (ph(536, 536, "UBB ad"), "United Bankers’ Bank"),
            (ph(1104, 184, "IBA Printing ad"), "IBA Printing: Save time and money on printing")],
    "hits": [{"hed": "34 states shut down a crypto kiosk operator",
              "body": "State regulators, including the Iowa Division of Banking, reached a $2.5 million settlement with Coinme Inc. over Bank Secrecy Act and anti-money laundering violations. Coinme must end its kiosk operations by Jan. 1, 2027.",
              "why": "Crypto kiosks are a common tool in the scams your front line works to stop, and Iowa’s regulator was at the table.",
              "link": "Read the settlement"},
             {"hed": "Iowa’s economic outlook stays positive",
              "body": "The Iowa Business Council’s third-quarter survey of the state’s 22 largest employers rose slightly to 64.91. Anything above 50 is positive.",
              "why": "Capital spending posted the biggest gain, a good sign for commercial loan demand. Workforce challenges remain a top concern.",
              "link": "See the survey"}],
    "calendar": [("Oct. 13", "ABA’s Core Platform Providers Survey closes. Anonymous, about 15 minutes.", "Take the survey"),
                 ("Nov. 18", "FDIC webinar on disaster recovery partnerships and CRA consideration (rescheduled).", "Register")],
    "numbers": {"big": "18%", "text": "of community banks plan to offer tokenized deposits in the next 12 months, up from 4% that offer them today. Another 16% plan to offer stablecoin solutions, up from 3%.",
                "source": "Source: Conference of State Bank Supervisors, 2026 Annual Survey of Community Banks",
                "next": "The IBA is one of 40 state associations in the BankChain Alliance, an industry-owned payments network targeting a 2027 launch.",
                "link": "Learn about BankChain"},
    "featured": {"name": "2026 IBA Technology Conference", "when": "Oct. 27-28 &middot; Des Moines",
                 "text": "Two days on artificial intelligence, cyber risk management, cybercrime and IT, with time to meet vendors and grow your network.",
                 "button": "Register for the conference"},
    "web_note": "All 8, Oct. 12-15",
    "webinars": [("Mon., Oct. 12", [("Best-Ever Compliance Checklists for Commercial Loans", False)]),
                 ("Tue., Oct. 13", [("FCRA Compliance", False),
                                    ("Completing a SAR: ID Theft, Elder Fraud, Cash and Check Transactions", False),
                                    ("Accurately Completing the SAR: A Workshop Going Beyond the Basics", False)]),
                 ("Wed., Oct. 14", [("Fraudulent Cashier’s Checks: Best Practices for Avoiding Losses", False),
                                    ("2026 Deposit Operations Webinar", True)]),
                 ("Thu., Oct. 15", [("2026 BSA Officer and Staff Webinar", True),
                                    ("Appraisal Bias, AVMs and Reconsiderations of Value: How Should We Handle This?", False)])],
    "seminars": [("Deposit Account Administration Seminar", "Oct. 14, Cedar Rapids &middot; Oct. 15, West Des Moines", True),
                 ("Mortgage Lending School", "Oct. 20-21, Johnston", False),
                 ("Iowa Lending Law Seminar", "Oct. 22, Johnston", False),
                 ("Advanced IRA Seminar", "Oct. 27, Storm Lake &middot; Oct. 28, Johnston &middot; Oct. 29, Cedar Rapids", False)],
    "tool": "New branch manager? IBA’s on-demand webinars cover supervisory skills and running a high-performing branch.",
    "tool_link": "See branch manager training",
    "iba": {"img": ph(1200, 840, "Leaders in Advocacy class"), "img_alt": "The 2026 Leaders in Advocacy class",
            "hed": "Meet the 2026 Leaders in Advocacy grads",
            "text": "Eight bankers wrapped up a year of advocacy training that took them to the Iowa Capitol twice and to Washington to meet with members of Congress, Treasury Secretary Scott Bessent and federal regulators. Each closed the program with a personal advocacy plan for their bank.",
            "caption": "From left: Travis Eagle, Ohnward Bank &amp; Trust; Amy Whitaker, Mediapolis Savings Bank; Josh Craighead, Northwest Bank; Crystal Wright, Community State Bank; Mike Cisney, Lincoln Savings Bank; Nicky Simpson, Bank Midwest; Kelsey Ray, West Bank; and Heather Smith, Denver Savings Bank.",
            "next": "Know an emerging leader? Applications for the 2027 class are open.", "link": "Apply or nominate"},
    "pp_img": ph(1104, 300, "Headshots: Black, Wiersema, Stenberg, Mulholland"),
    "deals": ["<strong>Iowa State Bank</strong>, Algona, and Mid-Iowa Bancshares Co. plan to acquire Swea City Bancorporation Inc., holding company of Estherville-based Bank Plus.",
              "<strong>Blackhawk Bancorporation</strong>, Milan, Ill., plans to acquire Liberty Bancorporation, holding company of Durant-based Liberty Trust &amp; Savings Bank."],
    "moves": ["<strong>Heartland Bank</strong>, Somers: CEO Kevin Black will retire at the end of January after 43 years.",
              "<strong>Citizens First Bank</strong>, Clinton: Kristine Wiersema promoted to Morrison branch manager.",
              "<strong>Northwest Bank</strong>, Spencer: Wendy Stenberg hired as wealth advisor.",
              "<strong>Fortress Bank</strong>, Peoria, Ill.: Jarret Mulholland hired as Des Moines market director."],
    "community": {"img": ph(360, 270, "FreedomBank check"), "img_alt": "FreedomBank presents a $2,000 check",
                  "hed": "FreedomBank backs a veterans memorial",
                  "text": "FreedomBank gave $2,000 to the Giard Northeast Iowa Vietnam Veterans Memorial Park, a community project honoring Vietnam veterans from across northeast Iowa.",
                  "foot": "Iowa banks give more than $50.4 million and 300,000 volunteer hours a year."},
    "spotlight": {"img": ph(300, 380, "Kenedy Backes"), "img_alt": "Kenedy Backes",
                  "hed": "Backes finds the story behind the numbers",
                  "text": "Kenedy Backes, credit portfolio manager at Bankers Trust, calls herself a storyteller: her job is explaining the gray area in the numbers. Best career advice she’s received? Be patient and don’t rush the season you’re in.",
                  "sponsor": "Abrigo"},
    "photo": {"img": ph(1200, 1140, "Photo of the week"), "img_alt": "Matt Johnson and family with Benny, their adopted puppy",
              "text": "Matt Johnson of Community Savings Bank met Benny at the IBA Annual Convention, where the Animal Rescue League was the featured nonprofit. Benny went home with the Johnsons. &#128054;"},
}

if __name__ == "__main__":
    for name, content in [("bank-note-template.html", BLANK), ("bank-note-sample-2026-10-08.html", SAMPLE)]:
        html = build(content)
        for bad in ("[#", "${", "<@", "<script"):
            assert bad not in html, f"{name} contains {bad!r}, which Constant Contact rejects"
        (OUT / name).write_text(html, encoding="utf-8")
        print(f"{name}: {len(html.encode('utf-8')) / 1024:.1f} KB")
