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


GOLD = "#c8930a"
CREAM = "#fdf6e3"


def section(title, sub, bg=NAVY):
    """Big section header: title plus a one-line description."""
    return row(f'<p style="margin:0;font-family:{FONT};font-size:20px;line-height:1.2;color:#ffffff;'
               f'font-weight:bold;">{title}</p>'
               f'<p style="margin:4px 0 0 0;font-family:{FONT};font-size:13px;line-height:1.3;color:#cfe5ff;">'
               f'{sub}</p>', pad="14px 24px", bg=bg)


def sublabel(text, color=NAVY, rule=BLUE):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" '
            f'style="margin:0 0 10px 0;"><tr><td style="border-bottom:2px solid {rule};padding:0 0 4px 0;'
            f'font-family:{FONT};font-size:13px;font-weight:bold;letter-spacing:1.5px;color:{color};">'
            f'{text}</td></tr></table>')


def build(c):
    blocks = []
    add = blocks.append

    add(comment("HEADER (text-based, so it shows even with images off)"))
    header_left = (f'<p style="margin:0;font-family:{FONT};font-size:40px;line-height:1;color:#ffffff;'
                   f'font-weight:bold;letter-spacing:3px;">BANK NOTE</p>'
                   f'<p style="margin:10px 0 0 0;font-family:{FONT};font-size:12px;line-height:1;'
                   f'color:#cfe5ff;letter-spacing:2.5px;">WEEKLY NEWS IN BRIEF</p>')
    header_right = f'<a href="https://www.iowabankers.com">{img(c["logo"], "Iowa Bankers Association", 160)}</a>'
    add(row(two_col(header_left, header_right, 352, 160, valign="bottom"), pad="28px 24px 24px 24px", bg=BLUE))
    add(row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td style="font-family:{FONT};font-size:13px;color:{SOFT};">{c["date"]}</td>'
            f'<td align="right" style="font-family:{FONT};font-size:13px;color:{SOFT};">{c["read"]}</td>'
            f'</tr></table>', pad="10px 24px"))

    # 1. WHAT'S IN THIS EDITION
    add(comment("1. WHAT'S IN THIS EDITION (one line per section, 4 to 6 lines)"))
    toc = "".join(f'<tr><td width="18" valign="top" style="font-family:{FONT};font-size:15px;line-height:1.5;'
                  f'color:{BLUE};">&#9656;</td><td style="font-family:{FONT};font-size:15px;line-height:1.5;'
                  f'color:{INK};padding:0 0 4px 0;">{t}</td></tr>' for t in c["toc"])
    add(row(f'<p style="margin:0 0 8px 0;font-family:{FONT};font-size:13px;font-weight:bold;'
            f'letter-spacing:1.5px;color:{NAVY};">WHAT’S IN THIS EDITION</p>'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{toc}</table>',
            bg=TINT))

    # 2. THE TOP STORY
    add(comment("2. THE TOP STORY (one lead item: the week's most important news)"))
    add(label("The top story"))
    t = c["top"]
    add(row(two_col(h(t["hed"], 24) + p(t["lede"]), img(t["img"], t["img_alt"], 150), 386, 150)
            + why(t["why"]) + bullets(t["bullets"]) + button(t["button"])))

    add(comment("SPONSOR AD 1"))
    add(ad(c["ads"][0][0], c["ads"][0][1]))

    # 3. BANKING BRIEFS
    add(comment("3. BANKING BRIEFS (quick news roundup; most relevant and urgent first; copy a BRIEF to add one)"))
    add(section("Banking briefs", "The week’s news, fast. Most urgent first."))
    for i, b in enumerate(c["briefs"]):
        top = f"border-top:1px solid {RULE};padding-top:14px;" if i else ""
        stat = ""
        if b.get("stat"):
            stat = (f'<p style="margin:0 0 6px 0;font-family:{FONT};font-size:40px;line-height:1;'
                    f'font-weight:bold;color:{BLUE};">{b["stat"]}</p>')
        inner = (f'<p style="margin:0 0 4px 0;font-family:{FONT};font-size:12px;font-weight:bold;'
                 f'letter-spacing:1.2px;color:{SOFT};">{b["tag"]}</p>' + stat + h(b["hed"], 18) + p(b["body"])
                 + why(b["why"] + " " + link(b["link"]), b.get("why_label", "Why it matters:")))
        add(f'<!-- BRIEF -->\n<tr><td class="pad" style="padding:{"16px" if not i else "0"} 24px 14px 24px;background:#ffffff;">'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td style="{top}">{inner}</td></tr></table></td></tr>')

    add(comment("SPONSOR AD 2"))
    add(ad(c["ads"][1][0], c["ads"][1][1]))

    # 4. ACROSS IOWA'S BANKING INDUSTRY
    add(comment("4. ACROSS IOWA'S BANKING INDUSTRY (member news and recognition)"))
    add(section("Across Iowa’s banking industry", "Member news, milestones and recognition"))
    i = c["iba"]
    add('<!-- RECOGNITION STORY (one per issue) -->')
    add(row(img(i["img"], i["img_alt"], 552) + '<div style="height:12px;line-height:12px;">&nbsp;</div>'
            + h(i["hed"], 19) + p(i["text"]) + p(i["caption"], 13, SOFT)
            + why(i["next"] + " " + link(i["link"]), "Your next step:")))
    add('<!-- PEOPLE AND PLACES -->')
    sub = lambda t: p(t, 13, NAVY, "font-weight:bold;letter-spacing:1px;margin:6px 0 6px 0;")
    add(row(sublabel("PEOPLE AND PLACES") + img(c["pp_img"], "Headshots of this week’s People and Places", 552)
            + '<div style="height:12px;line-height:12px;">&nbsp;</div>'
            + sub("DEALS") + bullets(c["deals"], 15) + sub("MOVES") + bullets(c["moves"], 15), pad="6px 24px 14px 24px"))
    b = c["community"]
    add('<!-- BANKING IN THE COMMUNITY -->')
    add(row(sublabel("BANKING IN THE COMMUNITY")
            + two_col(img(b["img"], b["img_alt"], 180), h(b["hed"], 18) + p(b["text"])
                      + p(b["foot"] + " " + link("Share your bank’s story"), 13, SOFT), 180, 356),
            pad="6px 24px 14px 24px"))
    ph_ = c["photo"]
    add('<!-- PHOTO OF THE WEEK -->')
    add(row(sublabel("PHOTO OF THE WEEK") + img(ph_["img"], ph_["img_alt"], 552)
            + '<div style="height:10px;line-height:10px;">&nbsp;</div>' + p(ph_["text"], extra="margin:0;"),
            pad="6px 24px 20px 24px"))

    add(comment("SPONSOR ADS 3 AND 4 (side by side; stack on phones)"))
    a3, a4 = c["ads"][2], c["ads"][3]
    add(row(two_col(f'<a href="#">{img(a3[0], a3[1], 268)}</a>', f'<a href="#">{img(a4[0], a4[1], 268)}</a>',
                    276, 276, gap=16), pad="12px 24px"))

    # 5. MEMBER SPOTLIGHT
    add(comment("5. MEMBER SPOTLIGHT (dedicated feature space)"))
    m = c["spotlight"]
    card = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CREAM}" '
            f'style="background:{CREAM};border-top:6px solid {GOLD};">'
            f'<tr><td class="pad" style="padding:20px 24px 6px 24px;">'
            f'<p style="margin:0;font-family:{FONT};font-size:12px;font-weight:bold;letter-spacing:2px;color:{GOLD};">'
            f'&#9733; MEMBER SPOTLIGHT</p></td></tr>'
            f'<tr><td class="pad" style="padding:8px 24px 0 24px;">'
            + two_col(img(m["img"], m["img_alt"], 200),
                      f'<p style="margin:0 0 2px 0;font-family:{FONT};font-size:26px;line-height:1.15;font-weight:bold;color:{NAVY};">{m["name"]}</p>'
                      f'<p style="margin:0 0 12px 0;font-family:{FONT};font-size:14px;line-height:1.35;color:{SOFT};">{m["title"]}</p>'
                      + h(m["hed"], 18) + p(m["text"]), 200, 336)
            + f'</td></tr><tr><td class="pad" style="padding:6px 24px 0 24px;">'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td style="border-left:4px solid {GOLD};padding:4px 0 4px 14px;font-family:Georgia, serif;'
            f'font-size:20px;line-height:1.35;font-style:italic;color:{NAVY};">{m["highlight"]}</td></tr></table>'
            f'</td></tr><tr><td class="pad" style="padding:16px 24px 8px 24px;">'
            + button(f'Read {m["pronoun"]} story', bg=NAVY)
            + f'</td></tr><tr><td class="pad" style="padding:8px 24px 20px 24px;font-family:{FONT};font-size:13px;'
            f'line-height:1.4;color:{SOFT};">Member Spotlight is brought to you by IBA associate member '
            f'<strong>{m["sponsor"]}</strong>. {link("Nominate a banker")}</td></tr></table>')
    add(f'<tr><td style="padding:0;">{card}</td></tr>')

    # 6. DATES, RESOURCES, EVENTS, DEADLINES
    add(comment("6. DATES, EVENTS, RESOURCES AND DEADLINES (everything to act on, in one place)"))
    add(section("Dates and deadlines", "Events, training, resources and deadlines to act on", bg=EDU_NAVY))

    dl = "".join(f'<!-- DEADLINE -->\n<tr><td class="stack" width="92" valign="top" style="width:92px;padding:0 10px 10px 0;'
                 f'font-family:{FONT};font-size:14px;line-height:1.35;font-weight:bold;color:{NAVY};">{d}</td>'
                 f'<td class="stack" valign="top" style="padding:0 0 10px 0;font-family:{FONT};font-size:15px;'
                 f'line-height:1.4;color:{INK};">{txt} {link(lk)}</td></tr>' for d, txt, lk in c["deadlines"])
    add('<!-- DEADLINES (surveys, applications, regulator events; copy a DEADLINE row to add one) -->')
    add(row(sublabel("DEADLINES") + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{dl}</table>',
            pad="16px 24px 8px 24px"))

    add('<!-- CREDIT HOURS: IBA EDUCATION (replaces the Education Bulletin) -->')
    badge = (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
             f'<td width="44" height="44" align="center" valign="middle" bgcolor="{EDU_SKY}" '
             f'style="width:44px;height:44px;border-radius:22px;background:{EDU_SKY};font-size:22px;'
             f'line-height:44px;">&#127891;</td></tr></table>')
    title = (f'<p style="margin:0;font-family:{FONT};font-size:24px;line-height:1.1;font-weight:bold;'
             f'color:{EDU_NAVY};">{c["edu_name"]}</p><p style="margin:4px 0 0 0;font-family:{FONT};'
             f'font-size:12px;letter-spacing:2px;color:{SOFT};">{c["edu_tag"]}</p>')
    add(row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td width="58" valign="middle">{badge}</td><td valign="middle">{title}</td></tr></table>',
            pad="18px 24px 12px 24px", bg=EDU_WASH))
    f = c["featured"]
    add(row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td bgcolor="#ffffff" style="background:#ffffff;border:1px solid {RULE};border-top:4px solid {EDU_SKY};'
            f'padding:14px 16px;">'
            + p("FEATURED", 12, EDU_NAVY, "font-weight:bold;letter-spacing:1.5px;margin-bottom:6px;")
            + h(f["name"], 19) + p(f["when"], 14, EDU_NAVY, "font-weight:bold;") + p(f["text"])
            + button(f["button"], bg=EDU_NAVY) + '</td></tr></table>', pad="0 24px 16px 24px", bg=EDU_WASH))

    pill = (f' <span style="background:#cfe5ff;color:{EDU_NAVY};font-size:11px;font-weight:bold;'
            f'letter-spacing:.5px;padding:1px 5px;border-radius:3px;">ALL DAY</span>')
    days = ""
    for day, items in c["webinars"]:
        lis = "".join(f'<p style="margin:0 0 6px 0;font-family:{FONT};font-size:15px;line-height:1.35;">'
                      f'{link(name)}{pill if allday else ""}</p>' for name, allday in items)
        days += (f'<!-- WEBINAR DAY -->\n<tr><td class="stack" width="100" valign="top" style="width:100px;'
                 f'padding:0 10px 8px 0;font-family:{FONT};font-size:14px;line-height:1.35;font-weight:bold;'
                 f'color:{EDU_NAVY};">{day}</td><td class="stack" valign="top" style="padding:0 0 8px 0;">'
                 f'{lis}</td></tr>')
    add('<!-- WEBINARS: list EVERY webinar until the next issue. Copy a WEBINAR DAY row per day. -->')
    add(row(sublabel(c["web_title"], EDU_NAVY, EDU_SKY)
            + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{days}</table>',
            pad="0 24px 8px 24px", bg=EDU_WASH))
    sem = ""
    for name, where, last in c["seminars"]:
        tag = (f'<span style="background:#fde7c4;color:#7a4100;font-size:11px;font-weight:bold;'
               f'letter-spacing:.5px;padding:1px 5px;border-radius:3px;">LAST CALL</span> ' if last else "")
        sem += (f'<p style="margin:0 0 10px 0;font-family:{FONT};font-size:15px;line-height:1.35;">'
                f'{tag}{link(name)}<br><span style="color:{SOFT};font-size:14px;">{where}</span></p>')
    add('<!-- SEMINARS AND SCHOOLS: highlight 3 or 4 -->')
    add(row(sublabel("SEMINARS AND SCHOOLS (IN PERSON)", EDU_NAVY, EDU_SKY) + sem, pad="6px 24px 6px 24px", bg=EDU_WASH))
    add(row(button("See the full education calendar", bg=EDU_NAVY)
            + p(f'Questions about training? {link("Contact IBA Education")}', 13, SOFT, "margin:10px 0 0 0;"),
            pad="4px 24px 20px 24px", bg=EDU_WASH))

    res = "".join(f'<!-- RESOURCE -->\n<p style="margin:0 0 10px 0;font-family:{FONT};font-size:15px;line-height:1.4;color:{INK};">'
                  f'<strong style="color:{NAVY};">{name}:</strong> {txt} {link(lk)}</p>' for name, txt, lk in c["resources"])
    add('<!-- USEFUL RESOURCES (copy a RESOURCE line to add one) -->')
    add(row(sublabel("USEFUL RESOURCES") + res, pad="18px 24px 12px 24px"))

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
    .stack img {{ max-width:200px !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background:{CANVAS};">
<!-- PREHEADER: the gray preview line in the inbox. Constant Contact's custom code emails have no preheader field, so it lives here. -->
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{c["preheader"]}&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;</div>
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
    "preheader": "EDIT PREHEADER: A second reason to open. Don’t repeat the subject line.",
    "logo": ph(320, 70, "IBA logo (white)"),
    "date": "EDIT DATE: Thursday, Month Day, 2026", "read": "3-minute read",
    "toc": ["EDIT: Top story teaser, one line", "EDIT: Banking briefs teaser",
            "EDIT: Across Iowa’s banking industry teaser", "EDIT: Member Spotlight: NAME, BANK",
            "EDIT: Dates and deadlines: X webinars next week"],
    "top": {"hed": "EDIT HEADLINE: What happened or what to do", "img": ph(300, 300, "Photo"), "img_alt": "EDIT PHOTO DESCRIPTION",
            "lede": "EDIT LEDE: One sentence with the news.",
            "why": "EDIT: One or two sentences on what this means for an Iowa banker.",
            "bullets": ["EDIT: Optional supporting detail.", "EDIT: Optional supporting detail."],
            "button": "EDIT BUTTON TEXT"},
    "ads": [(ph(1104, 184, "Sponsor ad 1"), "EDIT SPONSOR NAME"), (ph(1104, 184, "Sponsor ad 2"), "EDIT SPONSOR NAME"),
            (ph(536, 536, "Square ad 3"), "EDIT SPONSOR NAME"), (ph(536, 536, "Square ad 4"), "EDIT SPONSOR NAME"),
            (ph(1104, 184, "Sponsor ad 5"), "EDIT SPONSOR NAME")],
    "briefs": [{"tag": "EDIT TOPIC (e.g., REGULATION)", "hed": "EDIT HEADLINE", "body": "EDIT: One or two sentences with the news.",
                "why": "EDIT: One sentence on the impact.", "link": "EDIT LINK TEXT"},
               {"tag": "EDIT TOPIC", "hed": "EDIT HEADLINE", "body": "EDIT: One or two sentences with the news.",
                "why": "EDIT: One sentence on the impact.", "link": "EDIT LINK TEXT"},
               {"tag": "BY THE NUMBERS", "stat": "00%", "hed": "EDIT HEADLINE", "body": "EDIT: One sentence explaining the number.",
                "why": "EDIT: What a banker can do about it.", "why_label": "Your next step:", "link": "EDIT LINK TEXT"}],
    "iba": {"img": ph(1104, 640, "Recognition photo"), "img_alt": "EDIT PHOTO DESCRIPTION", "hed": "EDIT HEADLINE",
            "text": "EDIT: Two or three sentences. The full story lives on the website.",
            "caption": "EDIT CAPTION: From left, NAME, BANK; NAME, BANK; and NAME, BANK.",
            "next": "EDIT: The action you want readers to take.", "link": "EDIT LINK TEXT"},
    "pp_img": ph(1104, 300, "Headshot strip"),
    "deals": ["EDIT: <strong>Bank Name</strong>, City, plans to acquire HOLDING COMPANY."],
    "moves": ["EDIT: <strong>Bank Name</strong>, City: NAME promoted to TITLE.", "EDIT: <strong>Bank Name</strong>, City: NAME hired as TITLE."],
    "community": {"img": ph(360, 270, "Community photo"), "img_alt": "EDIT PHOTO DESCRIPTION", "hed": "EDIT HEADLINE",
                  "text": "EDIT: Two sentences on what the bank did and for whom.",
                  "foot": "Iowa banks give more than $50.4 million and 300,000 volunteer hours a year."},
    "photo": {"img": ph(1104, 760, "Photo of the week"), "img_alt": "EDIT PHOTO DESCRIPTION",
              "text": "EDIT: One or two sentences about the photo."},
    "spotlight": {"img": ph(400, 500, "Headshot"), "img_alt": "EDIT NAME", "name": "EDIT NAME",
                  "title": "EDIT Title, Bank Name", "hed": "EDIT HEADLINE",
                  "text": "EDIT: About 50 words: role, what drives them, one memorable detail.",
                  "highlight": "EDIT: One standout line or piece of advice.", "pronoun": "their", "sponsor": "EDIT SPONSOR NAME"},
    "deadlines": [("EDIT Oct. DD", "EDIT: Survey, application or regulator event, one line.", "EDIT LINK TEXT")],
    "edu_name": "Credit Hours", "edu_tag": "TRAINING THAT COUNTS &middot; IBA EDUCATION",
    "featured": {"name": "EDIT FEATURED EVENT", "when": "EDIT Month DD &middot; City",
                 "text": "EDIT: One sentence on who it’s for and why to go.", "button": "EDIT: Register for EVENT"},
    "web_title": "WEBINARS NEXT WEEK",
    "webinars": [("EDIT Mon., Oct. DD", [("EDIT Webinar title", False)]),
                 ("EDIT Tue., Oct. DD", [("EDIT Webinar title", False), ("EDIT All-day webinar title", True)])],
    "seminars": [("EDIT Seminar name", "EDIT Month DD, City", True), ("EDIT Seminar name", "EDIT Month DD, City", False)],
    "resources": [("Training tool of the week", "EDIT: One sentence on the on-demand resource.", "EDIT LINK TEXT"),
                  ("EDIT RESOURCE NAME", "EDIT: One sentence on what it helps with.", "EDIT LINK TEXT")],
}

SAMPLE = {
    **BLANK,
    "preheader": "Plus: 8 webinars next week, a crypto kiosk operator shut down and 2 Iowa bank deals.",
    "date": "Thursday, Oct. 8, 2026",
    "toc": ["The Fed is redrawing its supervision map",
            "Briefs: 34 states shut down a crypto kiosk operator",
            "Across Iowa: 2026 Leaders in Advocacy grads and 2 bank deals",
            "Member Spotlight: Kenedy Backes, Bankers Trust",
            "Dates and deadlines: 8 webinars next week, plus Mortgage Lending School"],
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
    "briefs": [{"tag": "FRAUD AND COMPLIANCE", "hed": "34 states shut down a crypto kiosk operator",
                "body": "State regulators, including the Iowa Division of Banking, reached a $2.5 million settlement with Coinme Inc. over Bank Secrecy Act and anti-money laundering violations. Coinme must end its kiosk operations by Jan. 1, 2027.",
                "why": "Crypto kiosks are a common tool in the scams your front line works to stop, and Iowa’s regulator was at the table.",
                "link": "Read the settlement"},
               {"tag": "PAYMENTS", "stat": "18%", "hed": "Community banks are lining up for tokenized deposits",
                "body": "That’s the share of community banks that plan to offer tokenized deposits in the next 12 months, up from 4% today, according to the Conference of State Bank Supervisors. Another 16% plan stablecoin solutions, up from 3%.",
                "why": "The IBA is one of 40 state associations in the BankChain Alliance, an industry-owned payments network targeting a 2027 launch.",
                "why_label": "Your next step:", "link": "Learn about BankChain"},
               {"tag": "IOWA ECONOMY", "hed": "Iowa’s economic outlook stays positive",
                "body": "The Iowa Business Council’s third-quarter survey of the state’s 22 largest employers rose slightly to 64.91. Anything above 50 is positive.",
                "why": "Capital spending posted the biggest gain, a good sign for commercial loan demand. Workforce challenges remain a top concern.",
                "link": "See the survey"}],
    "iba": {"img": ph(1104, 773, "Leaders in Advocacy class"), "img_alt": "The 2026 Leaders in Advocacy class",
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
    "photo": {"img": ph(1104, 1050, "Photo of the week"), "img_alt": "Matt Johnson and family with Benny, their adopted puppy",
              "text": "Matt Johnson of Community Savings Bank met Benny at the IBA Annual Convention, where the Animal Rescue League was the featured nonprofit. Benny went home with the Johnsons. &#128054;"},
    "spotlight": {"img": ph(400, 500, "Kenedy Backes"), "img_alt": "Kenedy Backes", "name": "Kenedy Backes",
                  "title": "Credit portfolio manager, Bankers Trust", "hed": "Finding the story behind the numbers",
                  "text": "Backes calls herself a storyteller. Her job is explaining the gray area in the numbers, because financial analysis isn’t always black and white. Outside the bank, the seasoned traveler, who once spent 10 months teaching English in Spain, bikes around town with friends and family.",
                  "highlight": "Best career advice she’s received: Be patient and don’t rush the season you’re in.",
                  "pronoun": "her", "sponsor": "Abrigo"},
    "deadlines": [("Oct. 13", "ABA’s Core Platform Providers Survey closes. Anonymous, about 15 minutes.", "Take the survey"),
                  ("Open now", "Applications for the 2027 Leaders in Advocacy class.", "Apply"),
                  ("Nov. 18", "FDIC webinar on disaster recovery partnerships and CRA consideration (rescheduled).", "Register")],
    "featured": {"name": "2026 IBA Technology Conference", "when": "Oct. 27-28 &middot; Des Moines",
                 "text": "Two days on artificial intelligence, cyber risk management, cybercrime and IT, with time to meet vendors and grow your network.",
                 "button": "Register for the conference"},
    "web_title": "WEBINARS NEXT WEEK (ALL 8)",
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
    "resources": [("Training tool of the week", "New branch manager? IBA’s on-demand webinars cover supervisory skills and running a high-performing branch.", "See branch manager training"),
                  ("Compliance Brief", "Stacy West covers digital credentials under CIP and SAR confidentiality guidance in the September video.", "Watch the brief"),
                  ("Fraud campaigns", "ABA’s new #BanksNeverAskThat and #PracticeSafeChecks videos are ready to share with customers.", "Get the materials")],
}

if __name__ == "__main__":
    for name, content in [("bank-note-template.html", BLANK), ("bank-note-sample-2026-10-08.html", SAMPLE)]:
        html = build(content)
        for bad in ("[#", "${", "<@", "<script"):
            assert bad not in html, f"{name} contains {bad!r}, which Constant Contact rejects"
        (OUT / name).write_text(html, encoding="utf-8")
        print(f"{name}: {len(html.encode('utf-8')) / 1024:.1f} KB")
