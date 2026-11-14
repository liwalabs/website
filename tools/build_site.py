#!/usr/bin/env python3
"""Generate projects.html and projects/<slug>.html from the PROJECTS data below.

Run from the repository root:  python3 tools/build_site.py

To add an intro video, put the file at assets/video/<slug>.mp4 (and optionally a
poster at assets/video/<slug>.jpg) and run this script again. Pages without a
video show an "Intro video coming soon" panel in the same place.
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATS = {
    "ai": "AI",
    "gov": "Government",
    "fin": "FinTech",
    "web3": "Web3",
    "mob": "Mobile",
}

MZ_FACT = ("Website", '<a href="https://mulazimai.com" target="_blank" rel="noopener">mulazimai.com</a>')

PROJECTS = [
    {
        "slug": "mulazim-ai", "name": "Mulazim AI", "cat": "ai", "flag": True,
        "brief": "Private AI that answers from your organisation's own databases and documents, and cites the source behind every answer.",
        "facts": [("For", "Government departments and enterprises"), ("Runs on", "Your servers, fully offline or with a hosted model"), ("Website", '<a href="https://mulazimai.com" target="_blank" rel="noopener">mulazimai.com</a>')],
        "overview": "Public chatbots have never seen your records, and anything pasted into them leaves your control. Mulazim is installed inside your organisation, connects to your systems and answers questions from your own data, showing where every figure and quote came from.",
        "features": [
            ("Data analyst", "Ask in plain language. It queries your ERP and databases and shows the numbers behind the answer."),
            ("Document answers", "Search across laws, rules, policies and files, with the clause or page cited."),
            ("Reports and decks", "Findings written up as reports, spreadsheets and slide decks you can edit."),
            ("Video analysis", "Counts and tracks what appears in recorded or live camera footage, processed on site."),
            ("Read-only by design", "It reaches your databases through a read-only account. The database itself refuses any change."),
            ("Access by role", "Each person sees only what their role allows. Database passwords and keys never reach the AI."),
        ],
        "steps": [
            ("Install", "Mulazim is installed on your servers and connected to your databases and document stores."),
            ("Ask", "Staff ask questions in plain language, by chat."),
            ("Answer with sources", "Mulazim plans the queries, reads the results and writes the answer, citing the rows and pages it used."),
        ],
        "extra": ("Two ways to run it", [
            ("Blackbox", "The whole platform, including the AI models, runs on your own GPU server. It can work with no internet connection at all."),
            ("Networked", "Runs on your servers and sends each question, with the passages or rows used to answer it, to a hosted model you choose."),
        ]),
        "stack": ["Rust", "Qdrant", "Postgres", "Next.js", "Local or hosted LLMs"],
    },
    {
        "slug": "mulazim-studio", "name": "Mulazim Studio", "cat": "ai",
        "brief": "A team of AI engineering specialists that takes a product brief to blueprints, CAD models, analysis and renders, with an approval gate at every step.",
        "facts": [("For", "Automotive and product engineering teams"), ("Part of", "The Mulazim platform")],
        "overview": "Give Studio a brief and reference designs. It plans the work as a graph of specialist roles, runs each one with real engineering tools, and stops for an engineer's sign-off before anything moves on.",
        "features": [
            ("Plans the work", "Reads the brief, sets the goal, researches and plans which specialist roles run, in what order."),
            ("Specialist roles", "Body design, chassis, powertrain, aerodynamics, cost and homologation, picked per project."),
            ("Real engineering output", "STEP and STL files, 3D models, FEA, renders and dimensioned drawings."),
            ("Approval gates", "Every step stops for sign-off. Send it back with comments and that role reworks it."),
            ("Checked numbers", "Calculated figures must cite the tool run that produced them. Open review findings need a written waiver."),
            ("Your materials", "Designs use your own catalogue of materials and processes, ranked by availability."),
        ],
        "steps": [
            ("Brief", "You give the brief, reference designs and any existing models."),
            ("Plan", "Studio interprets the brief, sets the goal, researches and plans the graph of roles."),
            ("Build and review", "Each role produces its part. You approve it, or send it back with comments."),
        ],
        "stack": ["CadQuery", "gmsh", "CalculiX", "Blender", "Next.js"],
    },
    {
        "slug": "e-dfa", "name": "e-DFA", "cat": "gov", "live": True,
        "brief": "Drafting, review, approval and printing of official letters for a Government of Sindh directorate.",
        "facts": [("For", "Drafters, reviewing officers and approving authorities"), ("Runs on", "The department's own server, on the office network")],
        "overview": "Before e-DFA, a drafter kept the Word file on their own PC, printed it, and the paper walked up the hierarchy. Corrections came back as pen marks, some were missed, and two copies of a letter could exist with different mistakes. e-DFA keeps one copy on the server and makes both failures impossible.",
        "shot": ("assets/shots/e-dfa-desk.jpg", "The desk: every letter with its number, status and how long it has waited. Demo data."),
        "features": [
            ("One copy, every version kept", "The server holds the only copy, numbers every version and links each to the last. An approved letter can never be changed."),
            ("No missed corrections", "Every comment stays open until it is resolved. A draft cannot go back up while any comment is open."),
            ("Mulazim AI built in", "Grammar checks as you type, shorter or more formal wording, a chat about the document and a private summariser. Nothing changes until the officer presses Apply."),
            ("Letters ready to sign", "PDF and Word output on the official letterhead, from the department's own templates."),
            ("Works on a phone", "Officers can review and approve from a phone on the office network."),
            ("Simple to run", "A one-file installer, nightly backups with a tamper check, and updates the IT officer applies."),
        ],
        "steps": [
            ("Draft", "The drafter writes the letter in the browser, from a template."),
            ("Review", "It goes up to the reviewing officer, who comments or passes it on."),
            ("Approve", "The approving authority approves it, or returns it with comments."),
            ("Print", "The approved letter prints on the letterhead, ready to sign."),
        ],
        "stack": ["Fastify", "React", "SQLite or Postgres", "TipTap", "Gemma, on site"],
    },
    {
        "slug": "e-dms", "name": "e-DMS", "cat": "gov", "live": True,
        "brief": "Capture, text search, filing and sharing of a department's paper documents, on the department's own server.",
        "facts": [("For", "Officers and administrators"), ("Runs on", "The department's own server, beside e-DFA")],
        "overview": "Officers kept paper, and photos of paper, on their own phones and PCs. Nothing was searchable or backed up, and when a person left, their documents left with them. e-DMS puts every captured document on the server, with text that can be searched.",
        "features": [
            ("Capture anywhere", "Phone camera or PC upload, including existing images and PDFs. Captures made without a connection wait on the phone and upload later."),
            ("Searchable text", "Text is read on the department's server, never in the cloud. Every scan becomes a searchable PDF, and the text can be corrected."),
            ("Folders and search", "Each officer files documents in their own folders and finds them by name or by what they say."),
            ("Personal stays personal", "A personal document is seen only by its owner and the people they share it with, not even by an administrator."),
            ("Handover built in", "When an officer moves on, the administrator transfers their official documents to the successor."),
            ("Originals never edited", "The original file is stored once and served as stored. Nothing overwrites it."),
        ],
        "steps": [
            ("Capture", "Photograph the page with a phone, or upload it from a PC."),
            ("Read", "The server reads the text and makes a searchable PDF."),
            ("File and find", "File it in a folder, then find it later by any word it contains."),
        ],
        "stack": ["Fastify", "React, installable app", "SQLite or Postgres", "Tesseract OCR"],
    },
    {
        "slug": "callwala", "name": "Callwala", "cat": "ai",
        "brief": "An AI representative for contact centres that qualifies leads and handles calls.",
        "facts": [("For", "Contact centres")],
        "features": [
            ("Qualifies leads", "Talks to callers and works out who is a real prospect."),
            ("Handles calls", "Answers and routes calls intelligently, without a person on every line."),
            ("Lower running costs", "Cuts the cost of a contact centre without cutting the conversation."),
        ],
    },
    {
        "slug": "aitells", "name": "Aitells", "cat": "ai",
        "brief": "A conversational AI platform, built before today's large language models, that answers questions in natural language.",
        "features": [
            ("Natural language", "Understands questions as people ask them."),
            ("Conversational answers", "Responds in plain language, in a chat."),
            ("Early work", "Built before large language models were widely available."),
        ],
    },
    {
        "slug": "oro-gold", "name": "Oro Gold", "cat": "fin",
        "brief": "An on-chain ecosystem built on a fully gold-backed digital token.",
        "features": [
            ("Gold-backed token", "Every token is backed by gold."),
            ("Invest and trade", "Buy, sell and hold gold instantly, on-chain."),
            ("Earn and borrow", "Put holdings to work, or borrow against them."),
        ],
    },
    {
        "slug": "liquid-prop", "name": "Liquid Prop", "cat": "fin",
        "brief": "Fractional ownership of U.S. real estate, on the blockchain.",
        "features": [
            ("Fractional ownership", "Own a share of a U.S. property, not the whole building."),
            ("Recorded on-chain", "Ownership is recorded transparently on the blockchain."),
            ("Open to more investors", "Makes property investment accessible to people who could not buy outright."),
        ],
    },
    {
        "slug": "zar", "name": "Zar", "cat": "fin",
        "brief": "A digital wallet that turns cash into digital dollars, spent worldwide with Visa cards.",
        "features": [
            ("Cash to digital dollars", "Convert cash into a dollar balance in the app."),
            ("Visa cards", "Virtual and physical cards linked to the wallet."),
            ("Spend globally", "Pay anywhere Visa is accepted."),
        ],
    },
    {
        "slug": "honeycomb-protocol", "name": "Honeycomb Protocol", "cat": "web3",
        "brief": "A foundational platform on Solana that gives decentralised projects essential utilities and speeds up development for game creators.",
        "features": [
            ("Shared utilities", "Ready-made building blocks for projects on Solana."),
            ("For game creators", "Streamlines development of on-chain games."),
            ("Core infrastructure", "Other projects build on top of it."),
        ],
    },
    {
        "slug": "ocean-explorers", "name": "Ocean Explorers", "cat": "web3",
        "brief": "A strategy game on Solana that combines NFT ownership with on-chain missions.",
        "features": [
            ("Own your crew", "Players own their explorers as NFTs."),
            ("Strategic missions", "Send them on missions and plan each move."),
            ("On-chain play", "Missions and results are recorded on-chain."),
        ],
    },
]

NEW = {
"after:mulazim-studio": [
    {"slug": "vakel-ai", "name": "Vakel AI", "cat": "ai", "mz": True,
     "brief": "Legal research on Mulazim: statutes and judgments, with every answer citing the law.",
     "facts": [("For", "Legal and risk teams"), ("Part of", "The Mulazim platform"), MZ_FACT],
     "features": [("Statutes and judgments", "Searches the law and past judgments together."),
                  ("Cited and clickable", "Every answer cites the law it relies on, and each citation opens the source."),
                  ("Less time searching", "Research that took hours of reading comes back in minutes.")]},
    {"slug": "ustad", "name": "Ustad", "cat": "ai", "mz": True,
     "brief": "Learning and compliance on Mulazim: courses checked against current standards, and exams set and graded to one rubric.",
     "facts": [("For", "Learning and compliance teams"), ("Part of", "The Mulazim platform"), MZ_FACT],
     "features": [("Courses kept current", "Checks course material against the current standards."),
                  ("Exams you can trust", "Sets exams and grades every answer to the same rubric."),
                  ("One place for training", "Material, exams and results stay inside your organisation.")]},
    {"slug": "rcs", "name": "RCS", "cat": "ai", "mz": True,
     "brief": "A secretary for every executive, on Mulazim: schedules without clashes, live KPI answers and decisions tracked.",
     "facts": [("For", "Executives and their offices"), ("Part of", "The Mulazim platform"), MZ_FACT],
     "features": [("Schedules without clashes", "Plans meetings and keeps the calendar clear of conflicts."),
                  ("Live KPI answers", "Ask about a number and get the current figure from your own systems."),
                  ("Decisions tracked", "Records what was decided and follows it up.")]},
    {"slug": "aats", "name": "AATS", "cat": "ai", "mz": True,
     "brief": "Operations on Mulazim: manuals, incidents and sensor history in one place, with failures forecast before they happen.",
     "facts": [("For", "Plant and operations teams"), ("Part of", "The Mulazim platform"), MZ_FACT],
     "features": [("Ask the plant", "Answers from manuals, incident reports and sensor history."),
                  ("Forecasts failures", "Spots the pattern before a machine breaks down."),
                  ("Stays on site", "Plant data is read inside your organisation.")]},
    {"slug": "shahid", "name": "Shahid", "cat": "ai", "mz": True,
     "brief": "Site security on Mulazim that runs on the camera itself, with no streaming and no cloud.",
     "facts": [("For", "Sites and security teams"), ("Part of", "The Mulazim platform"), MZ_FACT],
     "features": [("Runs on the camera", "Analysis happens on the device at each corner."),
                  ("No streaming, no cloud", "Footage is not sent anywhere to be analysed."),
                  ("A witness on every corner", "Each camera reports what it sees.")]},
    {"slug": "assembly-os", "name": "Assembly OS", "cat": "gov", "mz": True,
     "brief": "Sixteen applications for a legislative assembly, for its members, officers and staff, each seeing only what their role allows.",
     "facts": [("For", "Members, officers and staff of an assembly"), ("Languages", "Urdu, Sindhi and English, by voice or text"), ("Part of", "The Mulazim platform")],
     "overview": "Assembly OS works from the assembly's own rules, records and proceedings. It runs inside the assembly, can work without the internet, and keeps an audit record of every action.",
     "features": [("Bills, start to finish", "Research, a first draft and a legal check against existing law, for the Law branch to finalise."),
                  ("Questions and replies", "Members' questions sorted by subject, sent to the right minister and tracked until answered."),
                  ("Approvals and dashboards", "Files arrive summarised, ready to decide, and the whole assembly is visible at a glance."),
                  ("Proceedings journal", "A searchable record of every sitting."),
                  ("Translator and summariser", "Any document explained or translated in Urdu, Sindhi or English, by voice or text."),
                  ("Paper to digital", "Old files scanned into a permanent, searchable archive.")],
     "extra": ("Who uses what", [
         ("Members and executives", "Bill drafting and scrutiny, proceedings journal, approvals, dashboards and reports, meetings and schedule."),
         ("Officers", "Rules and precedents, questions and replies, drafting assistant, correspondence, deadlines and alerts, digital records."),
         ("Everyone", "Translator, document summariser, staff helpdesk, HR self-service and smart search.")])},
],
"after:aitells": [
    {"slug": "eve", "name": "Eve", "cat": "ai",
     "brief": "Anti-harassment technology providing tools for user safety and security, and the foundation of the official Zainab Alert app.",
     "features": [("Safety tools", "Tools that help users stay safe and raise an alarm."),
                  ("Security by design", "Built around protecting the people who use it."),
                  ("Behind Zainab Alert", "The technology the official Zainab Alert app is built on.")]},
    {"slug": "swift-me", "name": "Swift Me", "cat": "mob",
     "brief": "A one-window app for the restaurants of a shopping mall or food street, for ordering and discovery.",
     "features": [("One window", "Every restaurant in a mall or food street in one app."),
                  ("Discover", "Browse what is on offer before choosing where to eat."),
                  ("Order", "Place the order from the app.")]},
],
"after:honeycomb-protocol": [
    {"slug": "sol-patrol", "name": "Sol Patrol", "cat": "web3",
     "brief": "A real-time multiplayer strategy game on Solana where players build cities, form guilds and send NFTs on missions to conquer the grid.",
     "features": [("Build cities", "Grow a city on the grid."),
                  ("Form guilds", "Team up with other players."),
                  ("NFT missions", "Send NFTs on missions to conquer territory.")]},
],
"after:ocean-explorers": [
    {"slug": "rfrsh", "name": "RFRSH", "cat": "web3",
     "brief": "An all-in-one platform for Solana NFTs: portfolio tracking, wallet analytics, trading tools and market data.",
     "features": [("Portfolio tracking", "See every NFT you hold in one place."),
                  ("Wallet analytics", "Understand any wallet's holdings and activity."),
                  ("Trading tools and data", "Market data and tools for buying and selling.")]},
    {"slug": "bright-switch", "name": "Bright Switch", "cat": "web3",
     "brief": "A burn-to-mint platform on Solana that lets users exchange old NFT collections for new ones.",
     "features": [("Burn to mint", "Burn an old NFT and mint a new one in its place."),
                  ("Refresh collections", "Gives outdated holdings a new life."),
                  ("On Solana", "Runs entirely on-chain.")]},
    {"slug": "pooks", "name": "Pooks", "cat": "web3",
     "brief": "A digital collectible that serves as an online avatar and grants membership to the Pooks community.",
     "features": [("Online avatar", "Each Pook is a character to use online."),
                  ("Membership", "Holding one grants entry to the Pooks community."),
                  ("On-chain", "Ownership is recorded on the blockchain.")]},
],
}

for _key, _items in NEW.items():
    _after = _key.split(":", 1)[1]
    _i = next(i for i, x in enumerate(PROJECTS) if x["slug"] == _after)
    PROJECTS[_i + 1:_i + 1] = _items

E = html.escape


def video_exists(slug):
    return os.path.exists(os.path.join(ROOT, "assets", "video", slug + ".mp4"))


def head(title, desc, pre):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/png" href="{pre}assets/favicon.png">
<link rel="stylesheet" href="{pre}assets/fonts/fonts.css">
<link rel="stylesheet" href="{pre}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header" id="top">
  <div class="wrap nav">
    <a class="brand" href="{pre}index.html" aria-label="Liwa Labs home">
      <img src="{pre}assets/liwa-mark.png" alt="" width="34" height="34">
      <span class="brand-word">LIWA <span>LABS</span></span>
    </a>
    <button class="menu-btn" id="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav-links" id="nav-links" aria-label="Main">
      <a href="{pre}projects.html" aria-current="page">Projects</a>
      <a href="{pre}index.html#mulazim">Mulazim</a>
      <a href="{pre}index.html#services">Services</a>
      <a href="{pre}index.html#team">Team</a>
      <a class="btn btn-primary" href="{pre}index.html#contact">Contact us</a>
    </nav>
  </div>
</header>
<main id="main">
'''


def foot(pre):
    return f'''</main>
<footer class="site-footer">
  <div class="wrap foot">
    <span>© <span id="year">2026</span> Liwa Labs. Karachi, Pakistan. · <a href="https://mulazimai.com" target="_blank" rel="noopener">mulazimai.com</a></span>
    <div class="social">
      <a href="https://www.instagram.com/liwalabs" target="_blank" rel="noopener" aria-label="Liwa Labs on Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
      <a href="https://x.com/liwalabs" target="_blank" rel="noopener" aria-label="Liwa Labs on X"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
    </div>
  </div>
</footer>
<script src="{pre}assets/site.js"></script>
</body>
</html>
'''


def tags(p):
    t = []
    if p.get("flag"):
        t.append('<span class="tag flag">Flagship</span>')
    t.append(f'<span class="tag {p["cat"]}">{CATS[p["cat"]]}</span>')
    if p.get("mz") or p["slug"].startswith("mulazim"):
        t.append('<span class="tag mzt">Mulazim</span>')
    if p.get("live"):
        t.append('<span class="live"><i></i>In use</span>')
    return '<div class="tags">' + "".join(t) + "</div>"


SWOOSH = '<svg class="poster-arcs" viewBox="0 0 400 360" aria-hidden="true"><path d="M10 70 C 170 50, 320 110, 392 230"/><path d="M10 150 C 165 140, 295 200, 380 305"/><path d="M70 222 C 185 222, 275 262, 335 335"/></svg>'


def poster(p, big=True):
    """The intro video, or a designed panel in its place."""
    slug = p["slug"]
    if big and video_exists(slug):
        pst = f"../assets/video/{slug}.jpg"
        pattr = f' poster="{pst}"' if os.path.exists(os.path.join(ROOT, "assets", "video", slug + ".jpg")) else ""
        return f'<div class="video"><video controls preload="metadata" playsinline{pattr}><source src="../assets/video/{slug}.mp4" type="video/mp4"></video></div>'
    inner = f'<span class="poster-cat">{CATS[p["cat"]]}</span><span class="poster-name">{E(p["name"])}</span>'
    if big:
        inner += '<span class="poster-soon"><span class="play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="currentColor"/></svg></span><span class="soon-pill">Intro video coming soon</span></span>'
    if big:
        attrs = 'role="img" aria-label="Intro video for ' + E(p["name"]) + ', coming soon"'
    else:
        attrs = 'aria-hidden="true"'
    cls = "poster c-" + p["cat"] + (" big" if big else "")
    return f'<div class="{cls}" {attrs}>{SWOOSH}{inner}</div>'


def projects_page():
    rows = []
    for p in PROJECTS:
        rows.append(f'''      <a class="prow reveal" data-c="{p["cat"]}{" mulazim" if (p.get("mz") or p["slug"].startswith("mulazim")) else ""}" href="projects/{p["slug"]}.html">
        {poster(p, big=False)}
        <div class="prow-body">{tags(p)}<h2>{E(p["name"])}</h2><p>{E(p["brief"])}</p></div>
        <span class="prow-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a>''')
    body = f'''<section class="section page-top t-mist">
  <div class="wrap">
    <div class="head reveal">
      <p class="label">Projects</p>
      <h1 class="page-title">Every project, in brief.</h1>
      <p class="lede">Every product we have built. Open one for its intro video and the details.</p>
    </div>
    <div class="filters" role="group" aria-label="Filter projects">
      <button class="filter" type="button" data-f="all" aria-pressed="true">All</button>
      <button class="filter" type="button" data-f="mulazim" aria-pressed="false">Mulazim</button>
      <button class="filter" type="button" data-f="ai" aria-pressed="false">AI</button>
      <button class="filter" type="button" data-f="gov" aria-pressed="false">Government</button>
      <button class="filter" type="button" data-f="fin" aria-pressed="false">FinTech</button>
      <button class="filter" type="button" data-f="web3" aria-pressed="false">Web3</button>
      <button class="filter" type="button" data-f="mob" aria-pressed="false">Mobile</button>
    </div>
    <div class="plist">
{chr(10).join(rows)}
    </div>
  </div>
</section>
'''
    return head("Projects · Liwa Labs", "Every Liwa Labs project in brief: AI, government software, fintech and Web3.", "") + body + foot("")


def project_page(i, p):
    pre = "../"
    facts = [("Category", CATS[p["cat"]])] + p.get("facts", [])
    if p.get("live"):
        facts.append(("Status", "In use"))
    dl = "".join(f"<dt>{E(k)}</dt><dd>{v if '<a ' in v else E(v)}</dd>" for k, v in facts)
    feats = "".join(f'<li class="reveal"><h3>{E(t)}</h3><p>{E(d)}</p></li>' for t, d in p["features"])
    parts = []
    if p.get("overview"):
        parts.append(f'<section class="block"><h2>Overview</h2><p class="lede">{E(p["overview"])}</p></section>')
    if p.get("shot"):
        src, cap = p["shot"]
        parts.append(f'<figure class="shot reveal"><img src="{pre}{src}" alt="Screenshot of {E(p["name"])}" loading="lazy"><figcaption>{E(cap)}</figcaption></figure>')
    parts.append(f'<section class="block"><h2>What it does</h2><ul class="fgrid">{feats}</ul></section>')
    if p.get("steps"):
        st = "".join(f'<li class="reveal"><span class="n">{n}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for n, (t, d) in enumerate(p["steps"], 1))
        parts.append(f'<section class="block"><h2>How it works</h2><ol class="steps">{st}</ol></section>')
    if p.get("extra"):
        h, items = p["extra"]
        it = "".join(f'<li class="reveal"><h3>{E(t)}</h3><p>{E(d)}</p></li>' for t, d in items)
        parts.append(f'<section class="block"><h2>{E(h)}</h2><ul class="fgrid two">{it}</ul></section>')
    if p.get("stack"):
        ch = "".join(f"<li>{E(x)}</li>" for x in p["stack"])
        parts.append(f'<section class="block"><h2>Built with</h2><ul class="stack">{ch}</ul></section>')
    prev_p = PROJECTS[i - 1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    body = f'''<section class="detail-top c-{p["cat"]}">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{pre}projects.html">Projects</a><span aria-hidden="true">/</span><span>{E(p["name"])}</span></nav>
    {poster(p, big=True)}
  </div>
</section>
<section class="section detail">
  <div class="wrap detail-grid">
    <div class="detail-main">
      <header class="detail-head reveal">
        {tags(p)}
        <h1 class="page-title">{E(p["name"])}</h1>
        <p class="lede">{E(p["brief"])}</p>
      </header>
      {"".join(parts)}
    </div>
    <aside class="detail-side">
      <dl class="facts-card reveal">{dl}</dl>
      <div class="cta-card reveal"><p>Interested in {E(p["name"])}?</p><a class="btn btn-primary" href="{pre}index.html#contact">Talk to us</a></div>
    </aside>
  </div>
</section>
<nav class="pager t-mist" aria-label="More projects">
  <div class="wrap pager-row">
    <a href="{prev_p["slug"]}.html"><span class="label">Previous</span><b>{E(prev_p["name"])}</b></a>
    <a href="{pre}projects.html" class="all">All projects</a>
    <a href="{next_p["slug"]}.html" class="next"><span class="label">Next</span><b>{E(next_p["name"])}</b></a>
  </div>
</nav>
'''
    return head(f'{p["name"]} · Liwa Labs', p["brief"], pre) + body + foot(pre)


def main():
    os.makedirs(os.path.join(ROOT, "projects"), exist_ok=True)
    with open(os.path.join(ROOT, "projects.html"), "w") as f:
        f.write(projects_page())
    for i, p in enumerate(PROJECTS):
        with open(os.path.join(ROOT, "projects", p["slug"] + ".html"), "w") as f:
            f.write(project_page(i, p))
    print(f"wrote projects.html and {len(PROJECTS)} project pages")


if __name__ == "__main__":
    main()

