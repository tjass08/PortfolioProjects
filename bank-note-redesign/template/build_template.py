"""Builds the Bank Note custom-code email template for Constant Contact (modern, Axios-style).

Writes two files next to this script:
  bank-note-template.html          blank starter with EDIT placeholders
  bank-note-sample-2026-10-08.html same template filled with the Oct. 8, 2026, issue

Run: python3 build_template.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent

INK = "#111827"      # headlines and body
BODY = "#273142"
SOFT = "#5b6577"     # captions, meta
LINE = "#e3e7ee"     # hairline rules
BLUE = "#0054a6"     # IBA blue: links, accents
NAVY = "#002e5d"
WASH = "#f4f7fb"     # soft panels
SKY = "#e6f0fb"
GOLD = "#b7791f"
CREAM = "#fff8eb"
PAGE = "#f1f3f6"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
PH = "https://placehold.co"

T = 'role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"'


def img(src, alt, width, radius=10):
    return (f'<img src="{src}" alt="{alt}" width="{width}" border="0" style="display:block;width:100%;'
            f'max-width:{width}px;height:auto;border:0;border-radius:{radius}px;outline:none;text-decoration:none;">')


def a(text, url="#"):
    return f'<a href="{url}" style="color:{BLUE};font-weight:600;text-decoration:underline;">{text}</a>'


def p(text, size=17, color=BODY, extra=""):
    return (f'<p style="margin:0 0 14px 0;font-family:{FONT};font-size:{size}px;line-height:1.55;'
            f'color:{color};{extra}">{text}</p>')


def lead(label, text):
    """Axios-style bold lead-in: 'Why it matters: ...'"""
    return p(f'<strong style="color:{INK};">{label}</strong> {text}')


def hed(text, size=24):
    return (f'<h2 style="margin:0 0 12px 0;font-family:{FONT};font-size:{size}px;line-height:1.25;'
            f'color:{INK};font-weight:800;letter-spacing:-0.3px;">{text}</h2>')


def kicker(text, color=BLUE):
    return (f'<p style="margin:0 0 6px 0;font-family:{FONT};font-size:13px;line-height:1.3;color:{color};'
            f'font-weight:700;letter-spacing:0.6px;text-transform:uppercase;">{text}</p>')


def dots(items):
    rows = "".join(f'<tr><td width="20" valign="top" style="font-family:{FONT};font-size:17px;line-height:1.55;'
                   f'color:{BLUE};font-weight:700;">&bull;</td><td style="font-family:{FONT};font-size:17px;'
                   f'line-height:1.55;color:{BODY};padding:0 0 8px 0;">{i}</td></tr>' for i in items)
    return f'<table {T} style="margin:0 0 14px 0;">{rows}</table>'


def button(text, url="#", bg=BLUE):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:4px 0 4px 0;"><tr>'
            f'<td bgcolor="{bg}" style="border-radius:999px;background:{bg};">'
            f'<a href="{url}" style="display:inline-block;padding:12px 22px;font-family:{FONT};font-size:15px;'
            f'font-weight:700;color:#ffffff;text-decoration:none;border-radius:999px;">{text} &rarr;</a>'
            f'</td></tr></table>')


def row(inner, pad="0 32px 0 32px", bg="#ffffff"):
    return f'<tr><td class="pad" bgcolor="{bg}" style="padding:{pad};background:{bg};">{inner}</td></tr>'


def rule(pad="8px 32px 28px 32px"):
    return row(f'<table {T}><tr><td style="border-top:1px solid {LINE};font-size:0;line-height:0;">&nbsp;</td></tr></table>', pad)


def section(emoji, title, sub):
    """Section opener: big emoji, bold title, one-line description, short blue underline."""
    return row(f'<p style="margin:0;font-family:{FONT};font-size:30px;line-height:1;">{emoji}</p>'
               f'<p style="margin:10px 0 2px 0;font-family:{FONT};font-size:28px;line-height:1.15;color:{INK};'
               f'font-weight:800;letter-spacing:-0.5px;">{title}</p>'
               f'<p style="margin:0 0 12px 0;font-family:{FONT};font-size:15px;line-height:1.4;color:{SOFT};">{sub}</p>'
               f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
               f'<td width="48" height="4" bgcolor="{BLUE}" style="width:48px;height:4px;background:{BLUE};'
               f'border-radius:2px;font-size:0;line-height:0;">&nbsp;</td></tr></table>',
               pad="12px 32px 26px 32px")


def two(left, right, lw, rw, gap=20, valign="top"):
    return (f'<table {T}><tr><td class="stack" width="{lw}" valign="{valign}" style="width:{lw}px;padding:0 {gap//2}px 0 0;">'
            f'{left}</td><td class="stack" width="{rw}" valign="{valign}" style="width:{rw}px;padding:0 0 0 {gap//2}px;">'
            f'{right}</td></tr></table>')


def ad(src, alt, sponsor):
    return row(f'<p style="margin:0 0 8px 0;font-family:{FONT};font-size:11px;letter-spacing:1px;color:{SOFT};'
               f'text-transform:uppercase;">A message from {sponsor}</p><a href="#">{img(src, alt, 536, 8)}</a>',
               pad="4px 32px 30px 32px")


def note(text):
    return f"\n<!-- ===== {text} ===== -->\n"


def build(c):
    B = []
    add = B.append

    add(note("HEADER"))
    add(f'<tr><td bgcolor="{BLUE}" style="height:6px;background:{BLUE};font-size:0;line-height:0;">&nbsp;</td></tr>')
    word = (f'<p style="margin:0;font-family:{FONT};font-size:38px;line-height:1;color:{INK};font-weight:800;'
            f'letter-spacing:-1px;">Bank Note<span style="color:{BLUE};">.</span></p>'
            f'<p style="margin:8px 0 0 0;font-family:{FONT};font-size:14px;line-height:1.3;color:{SOFT};">'
            f'The week in Iowa banking, in brief</p>')
    add(row(two(word, f'<a href="https://www.iowabankers.com">{img(c["logo"], "Iowa Bankers Association", 150, 0)}</a>',
                366, 150, valign="middle"), pad="26px 32px 18px 32px"))
    add(row(f'<table {T}><tr><td style="border-top:1px solid {LINE};border-bottom:1px solid {LINE};padding:10px 0;'
            f'font-family:{FONT};font-size:13px;color:{SOFT};">{c["date"]}</td>'
            f'<td align="right" style="border-top:1px solid {LINE};border-bottom:1px solid {LINE};padding:10px 0;'
            f'font-family:{FONT};font-size:13px;color:{SOFT};">&#9201;&#65039; {c["read"]}</td></tr></table>',
            pad="0 32px 24px 32px"))

    add(note("1. WHAT'S IN THIS EDITION (greeting, then one line per section)"))
    add(row(p(f'<strong style="color:{INK};">&#128075; {c["hello"]}</strong> {c["hello_text"]}')))
    toc = "".join(f'<tr><td width="32" valign="top" style="font-family:{FONT};font-size:18px;line-height:1.5;">{e}</td>'
                  f'<td style="font-family:{FONT};font-size:16px;line-height:1.5;color:{BODY};padding:0 0 8px 0;">{t}</td></tr>'
                  for e, t in c["toc"])
    add(row(f'<table {T}><tr><td bgcolor="{WASH}" style="background:{WASH};border-radius:12px;padding:18px 20px 10px 20px;">'
            + kicker("&#128236; What’s in this edition", NAVY)
            + f'<table {T} style="margin-top:8px;">{toc}</table></td></tr></table>', pad="0 32px 30px 32px"))

    add(note("2. THE TOP STORY (1 big thing)"))
    t = c["top"]
    add(row(kicker(f'{t["emoji"]} 1 big thing') + hed(t["hed"], 28)))
    if t.get("side"):  # small headshot beside the lede instead of a full-width photo
        add(row(two(lead("Driving the news:", t["lede"]), img(t["img"], t["img_alt"], 140, 70), 376, 140)))
        news = ""
    else:
        add(row(img(t["img"], t["img_alt"], 536) + '<div style="height:16px;line-height:16px;">&nbsp;</div>'))
        news = lead("Driving the news:", t["lede"])
    add(row(news + lead("Why it matters:", t["why"])
            + p(f'<strong style="color:{INK};">Zoom in:</strong>', extra="margin-bottom:6px;") + dots(t["bullets"])
            + button(t["button"])))
    add(rule("22px 32px 26px 32px"))

    add(note("SPONSOR AD 1"))
    add(ad(*c["ads"][0]))

    add(note("3. BANKING BRIEFS (most urgent first; copy a BRIEF to add one)"))
    add(section("&#9889;", "Banking briefs", "The week’s news, fast. Most urgent first."))
    for i, b in enumerate(c["briefs"]):
        stat = ""
        if b.get("stat"):
            stat = (f'<p style="margin:0 0 8px 0;font-family:{FONT};font-size:48px;line-height:1;font-weight:800;'
                    f'color:{BLUE};letter-spacing:-1px;">{b["stat"]}</p>')
        add('<!-- BRIEF -->')
        add(row(kicker(f'{b["emoji"]} {b["tag"]}') + stat + hed(b["hed"], 21) + p(b["body"])
                + lead(b.get("why_label", "Why it matters:"), b["why"] + " " + a(b["link"]))))
        add(rule("4px 32px 24px 32px"))

    add(note("SPONSOR AD 2"))
    add(ad(*c["ads"][1]))

    add(note("4. ACROSS IOWA'S BANKING INDUSTRY (member news and recognition)"))
    add(section("&#127805;", "Across Iowa’s banking industry", "Member news, milestones and recognition"))
    i = c["iba"]
    add('<!-- RECOGNITION STORY -->')
    add(row(kicker(f'{i["emoji"]} {i["tag"]}') + hed(i["hed"], 21) + img(i["img"], i["img_alt"], 536)
            + '<div style="height:8px;line-height:8px;">&nbsp;</div>' + p(i["caption"], 13, SOFT) + p(i["text"])
            + lead("Your next step:", i["next"] + " " + a(i["link"]))))
    add(rule("4px 32px 24px 32px"))
    add('<!-- PEOPLE AND PLACES -->')
    pp = (kicker("&#129309; People and Places") + hed("Who’s moving, who’s merging", 21)
          + img(c["pp_img"], "Headshots of this week’s People and Places", 536, 8)
          + '<div style="height:14px;line-height:14px;">&nbsp;</div>'
          + p(f'<strong style="color:{INK};">&#127974; Deals</strong>', extra="margin-bottom:6px;") + dots(c["deals"])
          + p(f'<strong style="color:{INK};">&#128260; Moves</strong>', extra="margin-bottom:6px;") + dots(c["moves"]))
    add(row(pp))
    add(rule("0 32px 24px 32px"))
    b = c["community"]
    add('<!-- BANKING IN THE COMMUNITY -->')
    add(row(kicker("&#10084;&#65039; Banking in the Community")
            + two(img(b["img"], b["img_alt"], 200), hed(b["hed"], 19) + p(b["text"])
                  + p(b["foot"] + " " + a("Share your bank’s story"), 14, SOFT), 200, 316)))
    add(rule("4px 32px 24px 32px"))
    ph_ = c["photo"]
    add('<!-- PHOTO OF THE WEEK -->')
    add(row(kicker("&#128248; Photo of the week") + img(ph_["img"], ph_["img_alt"], 536)
            + '<div style="height:12px;line-height:12px;">&nbsp;</div>' + p(ph_["text"]), pad="0 32px 14px 32px"))

    add(note("SPONSOR ADS 3 AND 4 (side by side; stack on phones)"))
    (s3, a3, n3), (s4, a4, n4) = c["ads"][2], c["ads"][3]
    add(row(f'<p style="margin:0 0 8px 0;font-family:{FONT};font-size:11px;letter-spacing:1px;color:{SOFT};'
            f'text-transform:uppercase;">Messages from {n3} and {n4}</p>'
            + two(f'<a href="#">{img(s3, a3, 258, 8)}</a>', f'<a href="#">{img(s4, a4, 258, 8)}</a>', 268, 268),
            pad="10px 32px 30px 32px"))

    add(note("5. MEMBER SPOTLIGHT (feature card)"))
    m = c["spotlight"]
    card = (f'<table {T}><tr><td bgcolor="{CREAM}" style="background:{CREAM};border-radius:16px;padding:24px 24px 20px 24px;">'
            + kicker("&#11088; Member Spotlight", GOLD)
            + f'<div style="height:6px;line-height:6px;">&nbsp;</div>'
            + two(img(m["img"], m["img_alt"], 180, 14),
                  f'<p style="margin:0 0 2px 0;font-family:{FONT};font-size:26px;line-height:1.15;font-weight:800;'
                  f'color:{INK};letter-spacing:-0.5px;">{m["name"]}</p>'
                  f'<p style="margin:0 0 14px 0;font-family:{FONT};font-size:14px;line-height:1.35;color:{SOFT};">{m["title"]}</p>'
                  + hed(m["hed"], 18) + p(m["text"], 16), 180, 308)
            + f'<table {T} style="margin:6px 0 16px 0;"><tr><td bgcolor="#ffffff" style="background:#ffffff;border-radius:12px;'
            f'padding:16px 18px;font-family:Georgia, \'Times New Roman\', serif;font-size:20px;line-height:1.4;'
            f'font-style:italic;color:{INK};">&#128172; {m["highlight"]}</td></tr></table>'
            + button(f'Read {m["pronoun"]} story', bg=GOLD)
            + p(f'Brought to you by IBA associate member <strong>{m["sponsor"]}</strong>. {a("Nominate a banker")}',
                13, SOFT, "margin:14px 0 0 0;")
            + '</td></tr></table>')
    add(row(card, pad="0 32px 34px 32px"))

    add(note("6. DATES AND DEADLINES (everything to act on, in one place)"))
    add(section("&#128467;&#65039;", "Dates and deadlines", "Events, training, resources and deadlines to act on"))

    dl = "".join(f'<!-- DEADLINE -->\n<tr><td class="stack" width="96" valign="top" style="width:96px;padding:0 12px 12px 0;">'
                 f'<span style="display:inline-block;background:{SKY};color:{NAVY};font-family:{FONT};font-size:13px;'
                 f'font-weight:700;border-radius:6px;padding:3px 8px;">{d}</span></td>'
                 f'<td class="stack" valign="top" style="padding:0 0 12px 0;font-family:{FONT};font-size:16px;'
                 f'line-height:1.5;color:{BODY};">{txt} {a(lk)}</td></tr>' for d, txt, lk in c["deadlines"])
    add('<!-- DEADLINES (copy a DEADLINE row to add one) -->')
    add(row(kicker("&#9200; Deadlines") + f'<table {T} style="margin-top:6px;">{dl}</table>', pad="0 32px 14px 32px"))

    add('<!-- CREDIT HOURS: IBA EDUCATION (replaces the Education Bulletin) -->')
    f = c["featured"]
    pill = (f' <span style="background:#ffffff;color:{NAVY};border:1px solid #bcd3ee;font-size:11px;font-weight:700;'
            f'border-radius:999px;padding:1px 7px;">ALL DAY</span>')
    days = ""
    for day, items in c["webinars"]:
        lis = "".join(f'<p style="margin:0 0 7px 0;font-family:{FONT};font-size:15px;line-height:1.4;">'
                      f'{a(name)}{pill if allday else ""}</p>' for name, allday in items)
        days += (f'<!-- WEBINAR DAY -->\n<tr><td class="stack" width="100" valign="top" style="width:100px;padding:0 12px 10px 0;'
                 f'font-family:{FONT};font-size:14px;line-height:1.4;font-weight:700;color:{NAVY};">{day}</td>'
                 f'<td class="stack" valign="top" style="padding:0 0 10px 0;">{lis}</td></tr>')
    sem = ""
    for name, where, last in c["seminars"]:
        tag = (f'<span style="background:#fde7c4;color:#7a4100;font-size:11px;font-weight:700;border-radius:999px;'
               f'padding:1px 7px;">&#128293; LAST CALL</span> ' if last else "")
        sem += (f'<p style="margin:0 0 12px 0;font-family:{FONT};font-size:15px;line-height:1.4;">{tag}{a(name)}<br>'
                f'<span style="color:{SOFT};font-size:14px;">&#128205; {where}</span></p>')
    edu = (f'<table {T}><tr><td bgcolor="{SKY}" style="background:{SKY};border-radius:16px;padding:22px 22px 20px 22px;">'
           f'<p style="margin:0;font-family:{FONT};font-size:24px;line-height:1.15;font-weight:800;color:{NAVY};'
           f'letter-spacing:-0.4px;">&#127891; {c["edu_name"]}</p>'
           f'<p style="margin:4px 0 16px 0;font-family:{FONT};font-size:14px;color:{SOFT};">{c["edu_tag"]}</p>'
           f'<table {T}><tr><td bgcolor="#ffffff" style="background:#ffffff;border-radius:12px;padding:16px 18px;">'
           + kicker("&#10024; Featured") + hed(f["name"], 19)
           + p(f'&#128197; {f["when"]}', 15, NAVY, "font-weight:700;margin-bottom:8px;") + p(f["text"], 16)
           + button(f["button"], bg=NAVY) + '</td></tr></table>'
           + '<div style="height:18px;line-height:18px;">&nbsp;</div>'
           + kicker(f'&#128187; {c["web_title"]}', NAVY)
           + '<!-- WEBINARS: list EVERY webinar until the next issue. Copy a WEBINAR DAY row per day. -->'
           + f'<table {T} style="margin-top:8px;">{days}</table>'
           + '<div style="height:8px;line-height:8px;">&nbsp;</div>'
           + kicker("&#127979; Seminars and schools", NAVY) + '<!-- SEMINARS: highlight 3 or 4 -->'
           + f'<div style="height:6px;line-height:6px;">&nbsp;</div>{sem}'
           + button("See the full education calendar", bg=NAVY)
           + p(f'Questions about training? {a("Contact IBA Education")}', 14, SOFT, "margin:12px 0 0 0;")
           + '</td></tr></table>')
    add(row(edu, pad="6px 32px 28px 32px"))

    res = "".join(f'<!-- RESOURCE -->\n<tr><td width="32" valign="top" style="font-family:{FONT};font-size:18px;line-height:1.5;">{e}</td>'
                  f'<td style="padding:0 0 12px 0;font-family:{FONT};font-size:16px;line-height:1.5;color:{BODY};">'
                  f'<strong style="color:{INK};">{n}:</strong> {txt} {a(lk)}</td></tr>' for e, n, txt, lk in c["resources"])
    add('<!-- USEFUL RESOURCES (copy a RESOURCE row to add one) -->')
    add(row(kicker("&#129520; Useful resources") + f'<table {T} style="margin-top:6px;">{res}</table>', pad="0 32px 18px 32px"))

    add(note("SPONSOR AD 5"))
    add(ad(*c["ads"][4]))

    add(note("SIGN-OFF AND FOOTER (Constant Contact adds the legal footer with address and unsubscribe)"))
    add(row(f'<table {T}><tr><td bgcolor="{WASH}" style="background:{WASH};border-radius:16px;padding:22px 24px;">'
            + p(f'<strong style="color:{INK};">&#128227; Your turn:</strong> What would make Bank Note essential to you? '
                + a("Tell us in one question"), 16)
            + p(f'&#128140; {c["signoff"]}', 16, BODY, "margin:0 0 6px 0;")
            + p('Send news to <a href="mailto:editor@iowabankers.com" style="color:#0054a6;font-weight:600;">'
                'editor@iowabankers.com</a>. Published by the Iowa Bankers Association.', 13, SOFT, "margin:0;")
            + '</td></tr></table>', pad="0 32px 32px 32px"))

    body = "\n".join(B)
    return f'''<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>Bank Note</title>
<!--[if mso]><style>table,td,p,a,h2,span{{font-family:'Segoe UI',Arial,sans-serif !important;}}</style><![endif]-->
<style>
  body {{ margin:0 !important; padding:0 !important; width:100% !important; background:{PAGE}; }}
  table {{ border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt; }}
  img {{ -ms-interpolation-mode:bicubic; }}
  a {{ color:{BLUE}; }}
  @media only screen and (max-width:620px) {{
    .container {{ width:100% !important; border-radius:0 !important; }}
    .pad {{ padding-left:18px !important; padding-right:18px !important; }}
    .stack {{ display:block !important; width:100% !important; max-width:100% !important; padding:0 0 12px 0 !important; }}
    .stack img {{ max-width:220px !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background:{PAGE};">
<!-- PREHEADER: the gray preview line in the inbox. Custom code emails have no preheader field, so it lives here. -->
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{c["preheader"]}&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;</div>
<table {T} bgcolor="{PAGE}" style="background:{PAGE};">
<tr><td align="center" style="padding:24px 10px;">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:#ffffff;border-radius:14px;overflow:hidden;">
{body}
</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr>
</table>
</body>
</html>
'''


def ph(w, h, text):
    return f"{PH}/{w}x{h}/e3e7ee/5b6577/png?text={text.replace(' ', '+')}"


BLANK = {
    "preheader": "EDIT PREHEADER: A second reason to open. Don’t repeat the subject line.",
    "logo": ph(300, 64, "IBA logo"),
    "date": "EDIT DATE: Thursday, Month Day, 2026", "read": "3-minute read",
    "hello": "Happy Thursday, bankers.", "hello_text": "EDIT: One or two friendly sentences to open the issue.",
    "toc": [("&#127963;&#65039;", "EDIT: Top story teaser"), ("&#9889;", "EDIT: Banking briefs teaser"),
            ("&#127805;", "EDIT: Across Iowa teaser"), ("&#11088;", "EDIT: Member Spotlight: NAME, BANK"),
            ("&#128467;&#65039;", "EDIT: Dates and deadlines: X webinars next week")],
    "top": {"emoji": "&#127963;&#65039;", "hed": "EDIT HEADLINE: What happened or what to do",
            "img": ph(1072, 560, "Top story photo"), "img_alt": "EDIT PHOTO DESCRIPTION",
            "lede": "EDIT: One sentence with the news.",
            "why": "EDIT: One or two sentences on what this means for an Iowa banker.",
            "bullets": ["EDIT: Supporting detail.", "EDIT: Supporting detail."], "button": "EDIT BUTTON TEXT"},
    "ads": [(ph(1072, 179, "Sponsor ad 1"), "EDIT SPONSOR", "EDIT SPONSOR"),
            (ph(1072, 179, "Sponsor ad 2"), "EDIT SPONSOR", "EDIT SPONSOR"),
            (ph(516, 516, "Square ad 3"), "EDIT SPONSOR", "EDIT SPONSOR"),
            (ph(516, 516, "Square ad 4"), "EDIT SPONSOR", "EDIT SPONSOR"),
            (ph(1072, 179, "Sponsor ad 5"), "EDIT SPONSOR", "EDIT SPONSOR")],
    "briefs": [{"emoji": "&#128270;", "tag": "EDIT TOPIC", "hed": "EDIT HEADLINE", "body": "EDIT: One or two sentences with the news.",
                "why": "EDIT: One sentence on the impact.", "link": "EDIT LINK TEXT"},
               {"emoji": "&#128202;", "tag": "By the numbers", "stat": "00%", "hed": "EDIT HEADLINE",
                "body": "EDIT: One sentence explaining the number.", "why": "EDIT: What a banker can do about it.",
                "why_label": "Your next step:", "link": "EDIT LINK TEXT"},
               {"emoji": "&#128270;", "tag": "EDIT TOPIC", "hed": "EDIT HEADLINE", "body": "EDIT: One or two sentences with the news.",
                "why": "EDIT: One sentence on the impact.", "link": "EDIT LINK TEXT"}],
    "iba": {"emoji": "&#127942;", "tag": "Recognition", "img": ph(1072, 620, "Recognition photo"), "img_alt": "EDIT PHOTO DESCRIPTION",
            "hed": "EDIT HEADLINE", "text": "EDIT: Two or three sentences. The full story lives on the website.",
            "caption": "EDIT CAPTION: From left, NAME, BANK; NAME, BANK; and NAME, BANK.",
            "next": "EDIT: The action you want readers to take.", "link": "EDIT LINK TEXT"},
    "pp_img": ph(1072, 290, "Headshot strip"),
    "deals": ["EDIT: <strong>Bank Name</strong>, City, plans to acquire HOLDING COMPANY."],
    "moves": ["EDIT: <strong>Bank Name</strong>, City: NAME promoted to TITLE.", "EDIT: <strong>Bank Name</strong>, City: NAME hired as TITLE."],
    "community": {"img": ph(400, 300, "Community photo"), "img_alt": "EDIT PHOTO DESCRIPTION", "hed": "EDIT HEADLINE",
                  "text": "EDIT: Two sentences on what the bank did and for whom.",
                  "foot": "Iowa banks give more than $50.4 million and 300,000 volunteer hours a year."},
    "photo": {"img": ph(1072, 740, "Photo of the week"), "img_alt": "EDIT PHOTO DESCRIPTION",
              "text": "EDIT: One or two sentences about the photo."},
    "spotlight": {"img": ph(360, 450, "Headshot"), "img_alt": "EDIT NAME", "name": "EDIT NAME", "title": "EDIT Title, Bank Name",
                  "hed": "EDIT HEADLINE", "text": "EDIT: About 50 words: role, what drives them, one memorable detail.",
                  "highlight": "EDIT: One standout line or piece of advice.", "pronoun": "their", "sponsor": "EDIT SPONSOR"},
    "deadlines": [("EDIT Oct. DD", "EDIT: Survey, application or regulator event, one line.", "EDIT LINK TEXT")],
    "edu_name": "Credit Hours", "edu_tag": "Training that counts, from IBA Education",
    "featured": {"name": "EDIT FEATURED EVENT", "when": "EDIT Month DD &middot; City",
                 "text": "EDIT: One sentence on who it’s for and why to go.", "button": "EDIT: Register"},
    "web_title": "Webinars next week",
    "webinars": [("EDIT Mon., Oct. DD", [("EDIT Webinar title", False)]),
                 ("EDIT Tue., Oct. DD", [("EDIT Webinar title", False), ("EDIT All-day webinar title", True)])],
    "seminars": [("EDIT Seminar name", "EDIT Month DD, City", True), ("EDIT Seminar name", "EDIT Month DD, City", False)],
    "resources": [("&#128295;", "Training tool of the week", "EDIT: One sentence on the on-demand resource.", "EDIT LINK TEXT"),
                  ("&#128218;", "EDIT RESOURCE NAME", "EDIT: One sentence on what it helps with.", "EDIT LINK TEXT")],
    "signoff": "Thanks for reading. See you next Thursday! &mdash; The IBA communications team",
}

SAMPLE = {
    **BLANK,
    "preheader": "Plus: 8 webinars next week, a crypto kiosk operator shut down and 2 Iowa bank deals.",
    "date": "Thursday, Oct. 8, 2026",
    "hello_text": "The Fed is reshuffling how it supervises banks, 34 states just shut down a crypto kiosk operator and Education has 8 webinars lined up for next week.",
    "toc": [("&#127963;&#65039;", "The Fed is redrawing its supervision map"),
            ("&#9889;", "Briefs: Crypto kiosks, tokenized deposits and Iowa’s outlook"),
            ("&#127805;", "Across Iowa: Leaders in Advocacy grads and 2 bank deals"),
            ("&#11088;", "Member Spotlight: Kenedy Backes, Bankers Trust"),
            ("&#128467;&#65039;", "Dates and deadlines: 8 webinars next week")],
    "top": {"emoji": "&#127963;&#65039;", "hed": "The Fed is redrawing its supervision map",
            "img": ph(280, 280, "Bowman"), "img_alt": "Michelle Bowman", "side": True,
            "lede": "Fed Vice Chair for Supervision Michelle Bowman announced plans to organize bank supervision into five regions drawn along state lines, replacing the 12 Reserve Bank districts.",
            "why": "If the Fed supervises your bank or holding company, your examiners aren’t changing. The chain of command above them is.",
            "bullets": ["Each region gets one leader responsible for supervision. The Fed says that will simplify decisions and improve coordination with other regulators.",
                        "Examiners stay in their current Reserve Bank offices and keep the banks they supervise now.",
                        "Bowman announced the plan at the Community Banking Research Conference in St. Louis."],
            "button": "Read Bowman’s speech"},
    "ads": [(ph(1072, 179, "SHAZAM ad"), "SHAZAM: There’s only one you", "SHAZAM"),
            (ph(1072, 179, "BOK Financial ad"), "BOK Financial Capital Markets", "BOK Financial"),
            (ph(516, 516, "Wipfli ad"), "Wipfli", "Wipfli"), (ph(516, 516, "UBB ad"), "United Bankers’ Bank", "UBB"),
            (ph(1072, 179, "IBA Printing ad"), "IBA Printing: Save time and money on printing", "IBA Printing")],
    "briefs": [{"emoji": "&#128680;", "tag": "Fraud and compliance", "hed": "34 states shut down a crypto kiosk operator",
                "body": "State regulators, including the Iowa Division of Banking, reached a $2.5 million settlement with Coinme Inc. over Bank Secrecy Act and anti-money laundering violations. Coinme must end its kiosk operations by Jan. 1, 2027.",
                "why": "Crypto kiosks are a common tool in the scams your front line works to stop, and Iowa’s regulator was at the table.",
                "link": "Read the settlement"},
               {"emoji": "&#128202;", "tag": "By the numbers", "stat": "18%", "hed": "Community banks are lining up for tokenized deposits",
                "body": "That’s the share planning to offer tokenized deposits in the next 12 months, up from 4% today, per the Conference of State Bank Supervisors. Another 16% plan stablecoin solutions, up from 3%.",
                "why": "The IBA is one of 40 state associations in the BankChain Alliance, an industry-owned payments network targeting a 2027 launch.",
                "why_label": "Your next step:", "link": "Learn about BankChain"},
               {"emoji": "&#128200;", "tag": "Iowa economy", "hed": "Iowa’s economic outlook stays positive",
                "body": "The Iowa Business Council’s third-quarter survey of the state’s 22 largest employers rose slightly to 64.91. Anything above 50 is positive.",
                "why": "Capital spending posted the biggest gain, a good sign for commercial loan demand. Workforce challenges remain a top concern.",
                "link": "See the survey"}],
    "iba": {"emoji": "&#127891;", "tag": "Leaders in Advocacy", "img": ph(1072, 751, "Leaders in Advocacy class"),
            "img_alt": "The 2026 Leaders in Advocacy class", "hed": "Meet the 2026 Leaders in Advocacy grads",
            "text": "Eight bankers wrapped up a year of advocacy training that took them to the Iowa Capitol twice and to Washington to meet with members of Congress, Treasury Secretary Scott Bessent and federal regulators. Each closed the program with a personal advocacy plan for their bank.",
            "caption": "From left: Travis Eagle, Ohnward Bank &amp; Trust; Amy Whitaker, Mediapolis Savings Bank; Josh Craighead, Northwest Bank; Crystal Wright, Community State Bank; Mike Cisney, Lincoln Savings Bank; Nicky Simpson, Bank Midwest; Kelsey Ray, West Bank; and Heather Smith, Denver Savings Bank.",
            "next": "Know an emerging leader? Applications for the 2027 class are open.", "link": "Apply or nominate"},
    "pp_img": ph(1072, 290, "Headshots: Black, Wiersema, Stenberg, Mulholland"),
    "deals": ["<strong>Iowa State Bank</strong>, Algona, and Mid-Iowa Bancshares Co. plan to acquire Swea City Bancorporation Inc., holding company of Estherville-based Bank Plus.",
              "<strong>Blackhawk Bancorporation</strong>, Milan, Ill., plans to acquire Liberty Bancorporation, holding company of Durant-based Liberty Trust &amp; Savings Bank."],
    "moves": ["<strong>Heartland Bank</strong>, Somers: CEO Kevin Black will retire at the end of January after 43 years.",
              "<strong>Citizens First Bank</strong>, Clinton: Kristine Wiersema promoted to Morrison branch manager.",
              "<strong>Northwest Bank</strong>, Spencer: Wendy Stenberg hired as wealth advisor.",
              "<strong>Fortress Bank</strong>, Peoria, Ill.: Jarret Mulholland hired as Des Moines market director."],
    "community": {"img": ph(400, 300, "FreedomBank check"), "img_alt": "FreedomBank presents a $2,000 check",
                  "hed": "FreedomBank backs a veterans memorial",
                  "text": "FreedomBank gave $2,000 to the Giard Northeast Iowa Vietnam Veterans Memorial Park, a community project honoring Vietnam veterans from across northeast Iowa.",
                  "foot": "Iowa banks give more than $50.4 million and 300,000 volunteer hours a year."},
    "photo": {"img": ph(1072, 1020, "Photo of the week"), "img_alt": "Matt Johnson and family with Benny, their adopted puppy",
              "text": "Matt Johnson of Community Savings Bank met Benny at the IBA Annual Convention, where the Animal Rescue League was the featured nonprofit. Benny went home with the Johnsons. &#128054;"},
    "spotlight": {"img": ph(360, 450, "Kenedy Backes"), "img_alt": "Kenedy Backes", "name": "Kenedy Backes",
                  "title": "Credit portfolio manager, Bankers Trust", "hed": "Finding the story behind the numbers",
                  "text": "Backes calls herself a storyteller. Her job is explaining the gray area in the numbers. The seasoned traveler once spent 10 months teaching English in Spain.",
                  "highlight": "Best career advice she’s received: Be patient and don’t rush the season you’re in.",
                  "pronoun": "her", "sponsor": "Abrigo"},
    "deadlines": [("Oct. 13", "ABA’s Core Platform Providers Survey closes. Anonymous, about 15 minutes.", "Take the survey"),
                  ("Open now", "Applications for the 2027 Leaders in Advocacy class.", "Apply"),
                  ("Nov. 18", "FDIC webinar on disaster recovery partnerships and CRA consideration (rescheduled).", "Register")],
    "featured": {"name": "2026 IBA Technology Conference", "when": "Oct. 27-28 &middot; Des Moines",
                 "text": "Two days on artificial intelligence, cyber risk management, cybercrime and IT, with time to meet vendors and grow your network.",
                 "button": "Register"},
    "web_title": "All 8 webinars next week",
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
    "resources": [("&#128295;", "Training tool of the week", "New branch manager? IBA’s on-demand webinars cover supervisory skills and running a high-performing branch.", "See branch manager training"),
                  ("&#127909;", "Compliance Brief", "Stacy West covers digital credentials under CIP and SAR confidentiality guidance in the September video.", "Watch the brief"),
                  ("&#128737;&#65039;", "Fraud campaigns", "ABA’s new #BanksNeverAskThat and #PracticeSafeChecks videos are ready to share with customers.", "Get the materials")],
}

if __name__ == "__main__":
    for name, content in [("bank-note-template.html", BLANK), ("bank-note-sample-2026-10-08.html", SAMPLE)]:
        html = build(content)
        for bad in ("[#", "${", "<@", "<script"):
            assert bad not in html, f"{name} contains {bad!r}, which Constant Contact rejects"
        (OUT / name).write_text(html, encoding="utf-8")
        print(f"{name}: {len(html.encode('utf-8')) / 1024:.1f} KB, {html.count(chr(10)) + 1} lines")
