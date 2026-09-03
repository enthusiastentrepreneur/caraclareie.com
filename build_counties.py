import html, os

BASE = os.path.dirname(os.path.abspath(__file__))
COUNTIES_DIR = os.path.join(BASE, "counties")

STYLE = """
  /* ============ Tokens ============ */
  :root{
    --bg: #EDEFE6;
    --bg-alt: #E1E5D7;
    --surface: #FFFFFF;
    --surface-line: #D7DBC9;
    --ink: #142E2C;
    --ink-soft: #45605C;
    --ink-faint: #6C837E;
    --accent: #1F7A6C;
    --accent-ink: #0E4A40;
    --accent-soft: #DCEAE4;
    --gold: #B9791E;
    --gold-soft: #F3E4C9;
    --focus: #1F7A6C;
    --shadow: 0 1px 2px rgba(20,46,44,0.06), 0 8px 24px -12px rgba(20,46,44,0.18);
    --radius-lg: 20px;
    --radius-md: 14px;
    --radius-sm: 9px;
    --max: 1080px;
  }

  /* Dark-mode auto-switch intentionally disabled: the site always shows
     the light palette below, so it looks identical on every device
     regardless of the phone/browser's system theme setting. */
  :root[data-theme="dark"]{
    --bg: #0E1B1A;
    --bg-alt: #142624;
    --surface: #16302D;
    --surface-line: #274541;
    --ink: #EDF3F0;
    --ink-soft: #B9CBC5;
    --ink-faint: #86A29B;
    --accent: #4FBFA8;
    --accent-ink: #B7EADD;
    --accent-soft: #1D3D38;
    --gold: #E0A83F;
    --gold-soft: #3A2E17;
    --shadow: 0 1px 2px rgba(0,0,0,0.3), 0 12px 28px -14px rgba(0,0,0,0.6);
  }

  *{box-sizing:border-box;}
  html{-webkit-text-size-adjust:100%;}
  html,body{max-width:100%; overflow-x:hidden;}
  body{
    margin:0;
    background:var(--bg);
    color:var(--ink);
    font-family:"Atkinson Hyperlegible","Segoe UI",Arial,sans-serif;
    font-size:17px;
    line-height:1.55;
    -webkit-font-smoothing:antialiased;
  }
  h1,h2,h3{
    font-family:"Fraunces","Georgia",serif;
    font-weight:600;
    line-height:1.12;
    text-wrap:balance;
    margin:0;
    color:var(--ink);
  }
  a{color:var(--accent-ink);}
  a:focus-visible, button:focus-visible, .card:focus-visible{
    outline:3px solid var(--focus);
    outline-offset:3px;
    border-radius:6px;
  }
  img,svg{display:block;max-width:100%;}
  .wrap{max-width:var(--max); margin:0 auto; padding:0 24px;}
  @media (max-width:400px){ .wrap{padding:0 16px;} }
  .eyebrow{
    font-family:"Atkinson Hyperlegible",sans-serif;
    text-transform:uppercase;
    letter-spacing:.11em;
    font-size:13px;
    font-weight:700;
    color:var(--accent-ink);
  }
  section{padding:64px 0;}
  @media (max-width:640px){ section{padding:44px 0;} }
  @media (max-width:400px){ section{padding:32px 0;} }

  /* ============ Header ============ */
  header{
    position:sticky; top:0; z-index:20;
    background:color-mix(in srgb, var(--bg) 88%, transparent);
    backdrop-filter:blur(8px);
    border-bottom:1px solid var(--surface-line);
  }
  .headbar{
    display:flex; align-items:center; justify-content:space-between;
    padding:14px 0; gap:12px; flex-wrap:nowrap;
  }
  @media (max-width:340px){ .headbar{ padding:12px 0; } }
  .brand{display:flex; align-items:center; gap:10px; text-decoration:none; min-width:0;}
  .brand-mark{width:34px;height:34px;flex:none;}
  .brand-name{
    font-family:"Fraunces",serif; font-weight:600; font-size:21px; color:var(--ink);
    white-space:nowrap;
  }
  .brand-name em{font-style:normal; color:var(--accent-ink);}
  nav.headnav{display:flex; gap:22px; align-items:center; flex:none;}
  @media (max-width:380px){
    .brand-mark{width:28px;height:28px;}
    .brand-name{font-size:17px;}
    nav.headnav{gap:10px;}
  }
  nav.headnav a:not(.btn){
    color:var(--ink-soft); text-decoration:none; font-weight:700; font-size:14.5px;
  }
  nav.headnav a:not(.btn):hover{color:var(--accent-ink);}

  /* Buttons — locked-in text colors so they're never lost to inherited/visited link styling */
  a.btn, a.btn:link, a.btn:visited{
    display:inline-flex; align-items:center; gap:8px;
    background:var(--accent); color:#F5FBF8 !important;
    padding:11px 18px; border-radius:100px;
    font-weight:700; font-size:15px; text-decoration:none;
    border:none; cursor:pointer;
    box-shadow:var(--shadow);
  }
  a.btn:hover, a.btn:focus{ filter:brightness(1.06); color:#F5FBF8 !important; }
  a.btn.secondary, a.btn.secondary:link, a.btn.secondary:visited{
    background:transparent; color:var(--accent-ink) !important;
    border:1.5px solid var(--surface-line);
    box-shadow:none;
  }
  a.btn.secondary:hover{ background:var(--accent-soft); }
  a.btn.small{padding:8px 14px; font-size:13.5px;}
  @media (max-width:760px){ nav.headnav a.hide-mobile{display:none;} }

  /* ============ Hero ============ */
  .hero{padding:56px 0 40px;}
  .hero-grid{
    display:grid; grid-template-columns:1.15fr .85fr; gap:48px; align-items:center;
  }
  @media (max-width:840px){ .hero-grid{grid-template-columns:1fr;} }
  .hero h1{font-size:clamp(30px,4.6vw,46px); letter-spacing:-.01em;}
  .hero p.lede{
    font-size:18px; color:var(--ink-soft); max-width:48ch; margin-top:16px;
  }
  .hero-ctas{display:flex; gap:12px; flex-wrap:wrap; margin-top:28px;}
  @media (max-width:480px){
    .hero-ctas{flex-direction:column;}
    .hero-ctas a.btn{width:100%; justify-content:center;}
  }
  .hero-note{
    margin-top:18px; font-size:14px; color:var(--ink-faint); max-width:46ch;
  }
  .hero-panel{
    background:var(--surface); border:1px solid var(--surface-line);
    border-radius:var(--radius-lg); padding:26px; box-shadow:var(--shadow);
  }
  .hero-panel h2{font-size:16px; font-family:"Atkinson Hyperlegible"; font-weight:700; color:var(--ink-faint); text-transform:uppercase; letter-spacing:.08em;}
  .stat-row{display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-top:18px;}
  .stat{padding-top:14px; border-top:1px solid var(--surface-line); min-width:0;}
  .stat .num{
    font-family:"Fraunces",serif; font-weight:700; font-size:clamp(20px,5.5vw,26px); color:var(--gold);
    font-variant-numeric:tabular-nums; display:block; line-height:1.15;
  }
  .stat .cap{font-size:13.5px; color:var(--ink-soft); line-height:1.4;}
  @media (max-width:420px){
    .stat-row{grid-template-columns:1fr;}
    .stat .num{font-size:24px;}
  }
  .hero-src{font-size:12px; color:var(--ink-faint); margin-top:16px;}

  /* ============ Section headers ============ */
  .sec-head{max-width:64ch; margin-bottom:34px;}
  .sec-head h2{font-size:clamp(24px,3.4vw,34px);}
  .sec-head p{color:var(--ink-soft); margin-top:10px; font-size:16.5px;}

  /* ============ Category grid ============ */
  .bg-alt{background:var(--bg-alt); border-top:1px solid var(--surface-line); border-bottom:1px solid var(--surface-line);}
  .cat-grid{
    display:grid; grid-template-columns:repeat(4,1fr); gap:16px;
  }
  @media (max-width:900px){ .cat-grid{grid-template-columns:repeat(2,1fr);} }
  @media (max-width:520px){ .cat-grid{grid-template-columns:1fr;} }
  .cat-card{
    display:flex; flex-direction:column; gap:12px;
    background:var(--surface); border:1px solid var(--surface-line);
    border-radius:var(--radius-md); padding:20px;
    text-decoration:none; color:var(--ink);
    transition:transform .15s ease, box-shadow .15s ease;
  }
  .cat-card:hover{transform:translateY(-2px); box-shadow:var(--shadow);}
  .cat-icon{
    width:42px;height:42px; border-radius:11px; background:var(--accent-soft);
    display:flex; align-items:center; justify-content:center; color:var(--accent-ink);
  }
  .cat-card h3{font-family:"Atkinson Hyperlegible"; font-size:16.5px; font-weight:700;}
  .cat-card p{font-size:14px; color:var(--ink-soft); margin:0;}
  .cat-card .go{font-size:13px; font-weight:700; color:var(--accent-ink); margin-top:auto;}
  @media (prefers-reduced-motion: reduce){ .cat-card{transition:none;} }

  /* ============ County grid (browse-by-county) ============ */
  .county-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:16px; }
  @media (max-width:760px){ .county-grid{grid-template-columns:repeat(2,1fr);} }
  @media (max-width:480px){ .county-grid{grid-template-columns:1fr;} }
  .county-card{
    display:flex; flex-direction:column; gap:6px;
    background:var(--surface); border:1px solid var(--surface-line);
    border-radius:var(--radius-md); padding:20px;
    text-decoration:none; color:var(--ink);
    transition:transform .15s ease, box-shadow .15s ease;
  }
  .county-card:hover{transform:translateY(-2px); box-shadow:var(--shadow);}
  .county-card h3{font-family:"Fraunces",serif; font-size:19px; font-weight:600;}
  .county-card p{font-size:13.5px; color:var(--ink-soft); margin:0;}
  .county-card .go{font-size:13px; font-weight:700; color:var(--accent-ink); margin-top:6px;}
  .county-card.soon{ opacity:.6; }
  @media (prefers-reduced-motion: reduce){ .county-card{transition:none;} }
  .county-nav{ display:flex; flex-wrap:wrap; gap:8px; margin-top:22px; }
  .county-nav a{
    font-size:13px; font-weight:700; text-decoration:none; color:var(--accent-ink);
    background:var(--accent-soft); padding:6px 12px; border-radius:100px;
  }
  .county-nav a.current{ background:var(--accent); color:#F5FBF8; }
  .county-nav a:hover{ filter:brightness(1.05); }

  /* ============ Directory ============ */
  .dir-block{
    border:1px solid var(--surface-line); border-radius:var(--radius-lg);
    background:var(--surface); padding:26px 26px 6px; margin-bottom:22px; box-shadow:var(--shadow);
  }
  @media (max-width:480px){ .dir-block{padding:18px 18px 4px;} }
  .dir-block h3{
    font-size:20px; display:flex; align-items:center; gap:10px; margin-bottom:4px;
  }
  .dir-block .cat-tag{
    font-family:"Atkinson Hyperlegible"; font-size:12.5px; font-weight:700; letter-spacing:.06em;
    text-transform:uppercase; color:var(--gold);
  }
  .org{
    display:grid; grid-template-columns:1.4fr 1fr; gap:18px;
    padding:18px 0; border-top:1px solid var(--surface-line);
  }
  @media (max-width:700px){ .org{grid-template-columns:1fr;} }
  .org h4{margin:0 0 6px; font-size:16.5px; font-family:"Atkinson Hyperlegible"; font-weight:700;}
  .org p{margin:0; font-size:14.5px; color:var(--ink-soft);}
  .org .meta{font-size:14px; color:var(--ink-soft); display:flex; flex-direction:column; gap:5px;}
  .org .meta a{font-weight:700; text-decoration:none;}
  .org .meta a:hover{text-decoration:underline;}
  .org .area{
    display:inline-block; margin-top:4px; font-size:12px; font-weight:700;
    color:var(--accent-ink); background:var(--accent-soft); padding:3px 9px; border-radius:100px;
    width:fit-content;
  }

  /* ============ Spotlight banner ============ */
  .spot-banner{
    display:flex; align-items:center; gap:14px; flex-wrap:wrap;
    background:var(--gold-soft); border:1px solid var(--surface-line);
    border-radius:var(--radius-md); padding:16px 20px; margin-bottom:28px;
  }
  .spot-banner .pin{
    width:34px;height:34px;border-radius:10px;background:var(--gold);color:#241800;
    display:flex;align-items:center;justify-content:center;flex:none;
  }
  .spot-banner p{margin:0; font-size:14.5px; color:var(--ink); flex:1; min-width:160px;}
  .spot-banner strong{color:var(--accent-ink);}

  /* ============ Tips ============ */
  .tips{display:grid; grid-template-columns:repeat(3,1fr); gap:20px;}
  @media (max-width:800px){ .tips{grid-template-columns:1fr;} }
  .tip{
    background:var(--surface); border:1px solid var(--surface-line); border-radius:var(--radius-md);
    padding:22px;
  }
  .tip .idx{
    font-family:"Fraunces",serif; font-weight:700; color:var(--gold); font-size:14px;
  }
  .tip h4{font-size:17px; margin:8px 0 6px; font-family:"Atkinson Hyperlegible"; font-weight:700;}
  .tip p{font-size:14.5px; color:var(--ink-soft); margin:0;}

  /* ============ Provider CTA ============ */
  .provider{
    background:var(--accent-ink); color:#EFF9F5; border-radius:var(--radius-lg);
    padding:42px; display:grid; grid-template-columns:1.3fr .7fr; gap:28px; align-items:center;
  }
  @media (max-width:760px){ .provider{grid-template-columns:1fr; padding:28px;} }
  @media (max-width:480px){
    a.provider-btn{width:100%; justify-content:center;}
  }
  .provider h2{color:#F5FCF9; font-size:clamp(22px,3vw,30px);}
  .provider p{color:#D3E9E1; margin-top:10px; max-width:52ch;}
  a.provider-btn, a.provider-btn:link, a.provider-btn:visited{
    display:inline-flex; align-items:center; gap:8px;
    background:var(--gold); color:#241800 !important;
    padding:13px 22px; border-radius:100px; font-weight:700; font-size:15.5px;
    text-decoration:none; box-shadow:var(--shadow); white-space:nowrap;
  }
  a.provider-btn:hover{ filter:brightness(1.06); }
  .provider ul{margin:14px 0 0; padding-left:18px; color:#D3E9E1; font-size:14.5px;}
  .provider ul li{margin-bottom:4px;}

  /* ============ Footer ============ */
  footer{border-top:1px solid var(--surface-line); padding:40px 0 60px;}
  .foot-grid{display:grid; grid-template-columns:1.3fr 1fr 1fr; gap:32px;}
  @media (max-width:700px){ .foot-grid{grid-template-columns:1fr;} }
  footer h5{font-size:13px; text-transform:uppercase; letter-spacing:.08em; color:var(--ink-faint); margin:0 0 12px;}
  footer p, footer li{font-size:13.5px; color:var(--ink-soft); line-height:1.7;}
  footer ul{list-style:none; margin:0; padding:0;}
  footer a{color:var(--ink-soft); text-decoration:underline;}
  footer .bottom{
    margin-top:32px; padding-top:20px; border-top:1px solid var(--surface-line);
    font-size:12.5px; color:var(--ink-faint); display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px;
  }
"""

FONT_LINKS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Atkinson+Hyperlegible:wght@400;700&display=swap" rel="stylesheet">'''

COUNTIES = [
    ("clare", "Clare", "County Clare"),
    ("dublin", "Dublin", "Dublin"),
    ("cork", "Cork", "County Cork"),
    ("galway", "Galway", "County Galway"),
    ("limerick", "Limerick", "County Limerick"),
]

def header(active):
    links = []
    for slug, short, _ in COUNTIES:
        cls = ' class="current"' if slug == active else ''
        links.append(f'<a href="{slug}.html"{cls}>{short}</a>')
    return f"""<header>
  <div class="wrap headbar">
    <a class="brand" href="../index.html">
      <svg class="brand-mark" viewBox="0 0 40 40" fill="none" aria-hidden="true">
        <circle cx="16" cy="18" r="10" fill="var(--accent-soft)" stroke="var(--accent-ink)" stroke-width="2"/>
        <circle cx="25" cy="24" r="10" fill="none" stroke="var(--gold)" stroke-width="2"/>
      </svg>
      <span class="brand-name">Cara <em>Clare</em></span>
    </a>
    <nav class="headnav">
      <a href="../index.html#need" class="hide-mobile">Find help</a>
      <a href="../index.html#counties" class="hide-mobile">Counties</a>
      <a href="../blog/index.html" class="hide-mobile">Blog</a>
      <a class="btn small" href="../index.html#list-service">List a service</a>
    </nav>
  </div>
</header>"""

def footer(county_short, sources_extra):
    src_items = "\n".join(f"          <li>{s}</li>" for s in sources_extra)
    return f"""<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h5>Cara Clare</h5>
        <p>An independent, free directory connecting older people and family carers across Ireland to real local support. Piloted in County Clare. Not a service provider, not affiliated with the HSE, Age Friendly Ireland, or any council.</p>
      </div>
      <div>
        <h5>Sources for {county_short}</h5>
        <ul>
{src_items}
        </ul>
      </div>
      <div>
        <h5>Contact</h5>
        <ul>
          <li><a href="mailto:hello@caraclareie.com">hello@caraclareie.com</a></li>
          <li>Spotted outdated info? Email us &mdash; we check every listing.</li>
        </ul>
      </div>
    </div>
    <div class="bottom">
      <span>&copy; 2026 Cara Clare. A community information project.</span>
      <span>Listings checked August 2026.</span>
    </div>
  </div>
</footer>"""

def org(title, desc, meta_links, area):
    meta = "\n            ".join(meta_links)
    return f"""        <div class="org">
          <div>
            <h4>{title}</h4>
            <p>{desc}</p>
          </div>
          <div class="meta">
            {meta}
            <span class="area">{area}</span>
          </div>
        </div>"""

def dir_block(tag, heading, orgs_html):
    return f"""      <div class="dir-block">
        <span class="cat-tag">{tag}</span>
        <h3>{heading}</h3>
{orgs_html}
      </div>"""

def county_nav_row(active):
    items = []
    for slug, short, _ in COUNTIES:
        cls = ' class="current"' if slug == active else ''
        items.append(f'<a href="{slug}.html"{cls}>{short}</a>')
    items.append('<a href="../index.html#counties">All counties &rarr;</a>')
    return '<div class="county-nav">\n        ' + "\n        ".join(items) + '\n      </div>'

SITE = "https://caraclareie.com"

def page(slug, short, long_name, stats, intro, dir_blocks_html, sources):
    title = f"Support for Older People &amp; Carers in {long_name} | Cara Clare"
    plain_title = f"Support for Older People & Carers in {long_name} | Cara Clare"
    desc = f"Verified local support for older people and family carers in {long_name} — home help, transport, day centres, and carer support. Free and independent."
    canonical = f"{SITE}/counties/{slug}.html"
    og_image = f"{SITE}/og-image.png"
    stat_html = "\n".join(f"""          <div class="stat">
            <span class="num">{s['num']}</span>
            <span class="cap">{s['cap']}</span>
          </div>""" for s in stats)
    jsonld = f'''{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Cara Clare", "item": "{SITE}/"}},
        {{"@type": "ListItem", "position": 2, "name": "{short}", "item": "{canonical}"}}
      ]
    }},
    {{
      "@type": "WebPage",
      "name": "{plain_title}",
      "description": "{desc}",
      "url": "{canonical}",
      "isPartOf": {{"@type": "WebSite", "name": "Cara Clare", "url": "{SITE}/"}}
    }}
  ]
}}'''
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/svg+xml" href="{SITE}/favicon.svg">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Cara Clare">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="en_IE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">

{FONT_LINKS}
<style>
{STYLE}
</style>
<script type="application/ld+json">
{jsonld}
</script>
</head>
<body>

{header(slug)}

<main id="top">
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="eyebrow">Part of the Cara Clare national directory</p>
        <h1>Support for older people &amp; family carers in {long_name}</h1>
        <p class="lede">{intro}</p>
        <div class="hero-ctas">
          <a class="btn" href="../index.html#directory">See nationwide services</a>
          <a class="btn secondary" href="../index.html#list-service">List a {short} service</a>
        </div>
        {county_nav_row(slug)}
      </div>
      <div class="hero-panel">
        <h2>Why {short} needs this now</h2>
        <div class="stat-row">
{stat_html}
        </div>
        <p class="hero-src">Source: CSO Census of Population 2022, {long_name} county profiles.</p>
      </div>
    </div>
  </section>

  <section class="bg-alt">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Local directory</p>
        <h2>Real {short} services, checked and kept current</h2>
        <p>These are local, {short}-specific organisations. For nationwide helplines that work everywhere &mdash; ALONE, Citizens Information, HSELive &mdash; see the <a href="../index.html#directory">main directory</a>.</p>
      </div>
{dir_blocks_html}
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="provider">
        <div>
          <p class="eyebrow" style="color:#BFE3D8;">For {short} organisations</p>
          <h2>Run a service for older people or carers in {short}?</h2>
          <p>Cara Clare is an independent, volunteer-run project. If you run a service in {short} that helps older people or carers, get in touch and we'll add you to the directory so more people can find you.</p>
          <ul>
            <li>Listings are always free, no cost, ever</li>
            <li>Every listing is checked and kept up to date</li>
            <li>Spot an error, or want to be added? Just get in touch</li>
          </ul>
        </div>
        <a class="provider-btn" href="mailto:hello@caraclareie.com?subject=List%20our%20{short}%20service%20on%20Cara%20Clare">Get in touch &rarr;</a>
      </div>
    </div>
  </section>
</main>

{footer(long_name, sources)}
</body>
</html>
"""

# ---------------- Per-county content ----------------

pages = {}

# CLARE
clare_dirs = "\n".join([
    dir_block("Home help &amp; day centres", "Clarecare", "\n".join([
        org("Home Support Service", "Home help and personal care delivered by over 300 staff, coordinated from five offices across the county.",
            ['<a href="https://clarecare.ie/home-support-service/" target="_blank" rel="noopener">clarecare.ie</a>'], "Countywide"),
        org("Day Care Centres", "Meals and organised activities at centres in Killaloe, Ennis, and Ennistymon.",
            ['<a href="https://clarecare.ie" target="_blank" rel="noopener">clarecare.ie</a>'], "Killaloe &middot; Ennis &middot; Ennistymon"),
        org("Social Work Service for Older People", "A free, community-based social worker for anyone in Clare aged 65 or over &mdash; a good first call if you're not sure what you need.",
            ['<a href="https://clarecare.ie/social-work-for-older-persons/" target="_blank" rel="noopener">clarecare.ie</a>'], "Countywide"),
    ])),
    dir_block("Family carers", "Family Carers Ireland &mdash; Clare Support Centre", org(
        "Local office, Ennis", "A dedicated carer support manager, support groups, and training, based locally.",
        ['<a href="tel:0656866515">065 686 6515</a>', '<a href="mailto:clarecs@familycarers.ie">clarecs@familycarers.ie</a>'],
        "Suite 21, Clare Technology Park, Ennis")),
    dir_block("Transport", "Local Link Limerick Clare", org(
        "Door-to-door rural buses", "Can detour up to 8km to collect you, plus regular fixed routes. Free Travel pass holders travel at no cost.",
        ['<a href="tel:0656719101">065 671 9101</a>', '<a href="https://www.locallinklc.ie" target="_blank" rel="noopener">locallinklc.ie</a>'],
        "Countywide, rural routes")),
    dir_block("Council programmes", "Clare Age Friendly Programme", org(
        "Clare County Council", "The council's strategy and initiatives for older residents, run with older people themselves as advisors.",
        ['<a href="https://agefriendlyireland.ie/programmes/local/clare/" target="_blank" rel="noopener">agefriendlyireland.ie</a>'],
        "Countywide")),
])
pages["clare"] = dict(
    stats=[
        dict(num="21,657", cap="people 65+ &mdash; up 23% since 2016"),
        dict(num="5,566", cap="of them live alone &mdash; up 23% since 2016"),
        dict(num="8,200+", cap="unpaid family carers &mdash; 6% of the population"),
        dict(num="2,306", cap="now give 43+ hrs/week care, up from 1,131 in 2016"),
    ],
    intro="This is where Cara Clare started. Clare has 21,657 residents aged 65 or over, and more of them are living alone and caring for family than ever before. Here's the real, checked local support &mdash; not a call centre, the actual organisations.",
    dirs=clare_dirs,
    sources=[
        "CSO Census of Population 2022 &mdash; Clare Profile 1: Population Distribution",
        "CSO Census of Population 2022 &mdash; Clare Profile 3: Households, Families &amp; Childcare",
        "CSO Census of Population 2022 &mdash; Clare Profile 4: Disability, Health &amp; Carers",
    ],
)

# DUBLIN
dublin_dirs = "\n".join([
    dir_block("Company &amp; home help", "ALONE &mdash; Support Coordination for Older People", org(
        "North Dublin coordination service", "A joint ALONE &amp; HSE initiative connecting older people in North Dublin with the right local support, alongside ALONE's nationwide befriending and telephone support.",
        ['<a href="tel:0818222024">0818 222 024</a>', '<a href="https://alone.ie" target="_blank" rel="noopener">alone.ie</a>'],
        "North Dublin, ALONE nationwide")),
    dir_block("Home help", "HSE Home Support Service", org(
        "Apply &amp; find your local Dublin office", "HSE-funded home help and personal care &mdash; apply online, then a local Dublin Home Support Office arranges it.",
        ['<a href="https://www.hse.ie/eng/home-support-services/apply-for-home-supports-services/" target="_blank" rel="noopener">Apply on hse.ie</a>', '<a href="https://www.hse.ie/eng/home-support-services/contact-your-local-home-support-office/" target="_blank" rel="noopener">Find your local office</a>'],
        "Dublin City, South Dublin, Fingal, DLR")),
    dir_block("Family carers", "Family Carers Ireland &mdash; Dublin", org(
        "Multiple Dublin support centres", "Dublin has several local support centres (including Dublin South); the national office helps you find the nearest one, with a dedicated carer support manager, groups, and training.",
        ['<a href="tel:1800240724">1800 24 07 24</a>', '<a href="https://www.familycarers.ie/find-us" target="_blank" rel="noopener">Find your nearest centre</a>'],
        "Across Dublin")),
    dir_block("Transport", "Dublin Bus &mdash; Independent Travel Support", org(
        "Free one-to-one travel training", "A trained team member travels your regular route with you until you feel confident using Dublin Bus, Luas, or DART independently. Free Travel pass holders travel at no cost on all three.",
        ['<a href="tel:017033002">01 703 3002</a>', '<a href="https://www.dublinbus.ie/accessibility/independent-travel-support" target="_blank" rel="noopener">dublinbus.ie</a>'],
        "Greater Dublin Area")),
    dir_block("Council programmes", "Age Friendly Dublin", "\n".join([
        org("Dublin City", "The council's strategy and initiatives for older residents.",
            ['<a href="https://agefriendlyireland.ie/programmes/local/dublincity/" target="_blank" rel="noopener">agefriendlyireland.ie</a>'], "Dublin City"),
        org("South Dublin, Fingal &amp; Dún Laoghaire-Rathdown", "Each of Dublin's other three local authorities runs its own Age Friendly Programme.",
            ['<a href="https://agefriendlyireland.ie/programmes/local/southdublin/" target="_blank" rel="noopener">South Dublin</a>', '<a href="https://agefriendlyireland.ie/programmes/local/dunlaoghaire/" target="_blank" rel="noopener">D&uacute;n Laoghaire-Rathdown</a>', '<a href="https://agefriendlyireland.ie/programmes/local/fingal/" target="_blank" rel="noopener">Fingal</a>'], "Rest of County Dublin"),
    ])),
])
pages["dublin"] = dict(
    stats=[
        dict(num="195,664", cap="people 65+ &mdash; up 19% since 2016"),
        dict(num="47,578", cap="of them live alone, across Dublin's 4 local authorities"),
        dict(num="76,100", cap="unpaid family carers &mdash; 5% of the population, up from 4%"),
        dict(num="21,086", cap="now give 43+ hrs/week care, up from 9,944 in 2016"),
    ],
    intro="Dublin is Ireland's biggest county by far, split across four local authorities &mdash; Dublin City, South Dublin, Fingal, and D&uacute;n Laoghaire-Rathdown. Isolation among older people is rising fastest in the newer suburbs: living-alone rates jumped 36% in Fingal and 33% in South Dublin since 2016. Here's real, checked local support.",
    dirs=dublin_dirs,
    sources=[
        "CSO Census of Population 2022 &mdash; Dublin Summary Results",
        "CSO Census of Population 2022 &mdash; Dublin Profile 3 (living alone, by local authority)",
        "CSO Census of Population 2022 &mdash; Dublin Profile 4: Disability, Health &amp; Carers",
    ],
)

# CORK
cork_dirs = "\n".join([
    dir_block("Home help &amp; day centres", "Westgate Foundation", org(
        "Day care, meals on wheels &amp; transport", "Day care activities, community catering (meals on wheels), transport, sheltered housing, and the Seniors Alert Scheme personal alarm &mdash; serving Ballincollig and the Mid Cork area.",
        ['<a href="tel:0214873648">021 487 3648</a>', '<a href="https://westgatefoundation.ie" target="_blank" rel="noopener">westgatefoundation.ie</a>'],
        "Ballincollig &amp; Mid Cork")),
    dir_block("Home help", "HSE Services for Older People", org(
        "North Cork &amp; North Lee local pages", "Cork is large and split across several HSE community areas &mdash; these list local older-person services by area, alongside the national Home Support application.",
        ['<a href="https://www.hse.ie/eng/services/list/1/lho/corknorthcounty/older/" target="_blank" rel="noopener">North Cork</a>', '<a href="https://www.hse.ie/eng/services/list/1/lho/corknorthlee/olderpeople/" target="_blank" rel="noopener">North Lee</a>'],
        "By HSE community area")),
    dir_block("Family carers", "Family Carers Ireland &mdash; Cork Support Centre", org(
        "Local office, Cork city", "A dedicated carer support manager, support groups, and training, based locally.",
        ['<a href="tel:0214806398">021 480 6398</a>'], "Republic of Work, 12 South Mall, Cork")),
    dir_block("Transport", "Local Link Cork", org(
        "Rural &amp; door-to-door bus services", "Regular rural routes and door-to-door services, with two local offices covering West and North Cork.",
        ['<a href="tel:02752727">027 52727</a> (Bantry)', '<a href="tel:02551454">025 51454</a> (Fermoy)', '<a href="https://locallinkcork.ie" target="_blank" rel="noopener">locallinkcork.ie</a>'],
        "Countywide, rural routes")),
    dir_block("Council programmes", "Age Friendly Cork", "\n".join([
        org("Cork City", "The city council's strategy and initiatives for older residents.",
            ['<a href="https://agefriendlyireland.ie/programmes/local/corkcity/" target="_blank" rel="noopener">agefriendlyireland.ie</a>'], "Cork City"),
        org("Cork County", "The county council's equivalent programme for the rest of Cork.",
            ['<a href="https://agefriendlyireland.ie/programmes/local/corkcounty/" target="_blank" rel="noopener">agefriendlyireland.ie</a>'], "Cork County"),
    ])),
])
pages["cork"] = dict(
    stats=[
        dict(num="89,461", cap="people 65+ &mdash; up 21% since 2016"),
        dict(num="21,979", cap="of them live alone &mdash; up 21% since 2016"),
        dict(num="36,000+", cap="unpaid family carers &mdash; 6% of the population, up from 4%"),
        dict(num="10,382", cap="now give 43+ hrs/week care, up from 4,874 in 2016"),
    ],
    intro="Cork is Ireland's biggest county by area, split between Cork City and Cork County councils, with services spread across several HSE community areas. That spread makes a single, plain-language front door especially useful. Here's real, checked local support to start with.",
    dirs=cork_dirs,
    sources=[
        "CSO Census of Population 2022 &mdash; Cork Summary Results",
        "CSO Census of Population 2022 &mdash; Cork Profile 3 (living alone)",
        "CSO Census of Population 2022 &mdash; Cork Profile 4: Disability, Health &amp; Carers",
    ],
)

# GALWAY
galway_dirs = "\n".join([
    dir_block("Home help &amp; day centres", "COPE Galway &mdash; Senior Support Service", org(
        "Meals, social centre &amp; community support", "Community catering (meals on wheels), the Sonas Social Centre, and wider community support for older people across Galway.",
        ['<a href="https://www.copegalway.ie/senior-support-service/" target="_blank" rel="noopener">copegalway.ie</a>'], "Galway City &amp; County")),
    dir_block("Home help", "HSE Home Support Service", org(
        "Apply &amp; find your local Galway office", "Apply online for HSE-funded home help and personal care, then connect with your local Galway Home Support Office.",
        ['<a href="https://www.hse.ie/eng/home-support-services/apply-for-home-supports-services/" target="_blank" rel="noopener">Apply on hse.ie</a>'], "Galway City &amp; County")),
    dir_block("Family carers", "Family Carers Ireland &mdash; Galway Support Centre", org(
        "Local office, Tuam", "A dedicated carer support manager, support groups, and training, based locally.",
        ['<a href="tel:09330061">093 30061</a>', '<a href="mailto:galwaycs@familycarers.ie">galwaycs@familycarers.ie</a>'],
        "St. Jarlath's Court, The Glebe, Tuam")),
    dir_block("Transport", "Local Link Galway", org(
        "Rural &amp; door-to-door bus services", "Regular rural routes and door-to-door services across County Galway.",
        ['<a href="tel:091842384">091 842 384</a>', '<a href="https://www.locallinkgalway.ie" target="_blank" rel="noopener">locallinkgalway.ie</a>'],
        "Countywide, rural routes")),
    dir_block("Council programmes", "Age Friendly Galway", "\n".join([
        org("Galway City", "The city council's strategy and initiatives for older residents.",
            ['<a href="https://agefriendlyireland.ie/programmes/local/galwaycity/" target="_blank" rel="noopener">agefriendlyireland.ie</a>'], "Galway City"),
        org("Galway County", "The county council's equivalent programme for the rest of Galway.",
            ['<a href="https://agefriendlyireland.ie/programmes/local/galwaycounty/" target="_blank" rel="noopener">agefriendlyireland.ie</a>'], "Galway County"),
    ])),
])
pages["galway"] = dict(
    stats=[
        dict(num="42,886", cap="people 65+ &mdash; up 23% since 2016"),
        dict(num="10,297", cap="of them live alone, across the city &amp; county"),
        dict(num="16,800+", cap="unpaid family carers &mdash; 6% of the population, up from 4%"),
        dict(num="4,580", cap="now give 43+ hrs/week care, up from 2,141 in 2016"),
    ],
    intro="Galway is split between Galway City and Galway County councils, but its charity sector is unusually joined-up &mdash; COPE Galway alone covers meals, social centres, and community support right across both. Here's real, checked local support to start with.",
    dirs=galway_dirs,
    sources=[
        "CSO Census of Population 2022 &mdash; Galway Summary Results",
        "CSO Census of Population 2022 &mdash; Galway Profile 3 (living alone, city &amp; county)",
        "CSO Census of Population 2022 &mdash; Galway Profile 4: Disability, Health &amp; Carers",
    ],
)

# LIMERICK
limerick_dirs = "\n".join([
    dir_block("Home help &amp; day centres", "Limerick Social Service Council (LSSC)", org(
        "Services for Older Persons", "Local social services for older people in Limerick, run by a long-established community organisation.",
        ['<a href="https://www.lssc.ie/what-we-do/services-for-older-persons/" target="_blank" rel="noopener">lssc.ie</a>'], "Limerick city &amp; county")),
    dir_block("Day centres", "Bergerie Trust", org(
        "Day Centre &amp; sheltered housing", "A day centre and sheltered housing specifically for older people in Limerick.",
        ['<a href="https://bergerietrust.ie/day-centre/" target="_blank" rel="noopener">bergerietrust.ie</a>'], "Limerick")),
    dir_block("Family carers", "Family Carers Ireland &mdash; Limerick Support Centre", org(
        "Local office, Limerick city", "A dedicated carer support manager, support groups, and training, based locally.",
        ['<a href="tel:061310434">061 310434</a>', '<a href="mailto:limerickcs@familycarers.ie">limerickcs@familycarers.ie</a>'],
        "Unit 1, Georges Quay House, Limerick")),
    dir_block("Transport", "Local Link Limerick Clare", org(
        "Door-to-door rural buses", "Can detour up to 8km to collect you, plus regular fixed routes across Limerick, shared with neighbouring Clare.",
        ['<a href="tel:0656719101">065 671 9101</a>', '<a href="https://www.locallinklc.ie" target="_blank" rel="noopener">locallinklc.ie</a>'],
        "Countywide, rural routes")),
    dir_block("Council programmes", "Age Friendly Limerick", org(
        "Limerick City and County Council", "The council's strategic plan and initiatives for older residents.",
        ['<a href="https://agefriendlyireland.ie/programmes/local/limerick/" target="_blank" rel="noopener">agefriendlyireland.ie</a>'], "Countywide")),
])
pages["limerick"] = dict(
    stats=[
        dict(num="33,588", cap="people 65+ &mdash; up 23% since 2016"),
        dict(num="8,311", cap="of them live alone &mdash; up 21% since 2016"),
        dict(num="12,200", cap="unpaid family carers &mdash; 6% of the population, up from 4%"),
        dict(num="3,714", cap="now give 43+ hrs/week care, up from 1,921 in 2016"),
    ],
    intro="Limerick City and County Council merged into a single authority in 2014, which makes joined-up local support a bit easier to find than in split counties &mdash; and Limerick shares its rural transport service with neighbouring Clare. Here's real, checked local support to start with.",
    dirs=limerick_dirs,
    sources=[
        "CSO Census of Population 2022 &mdash; Limerick Summary Results",
        "CSO Census of Population 2022 &mdash; Limerick Profile 3 (living alone)",
        "CSO Census of Population 2022 &mdash; Limerick Profile 4: Disability, Health &amp; Carers",
    ],
)

def build_all():
    os.makedirs(COUNTIES_DIR, exist_ok=True)
    name_map = {s: n for s, short, n in COUNTIES}
    short_map = {s: short for s, short, n in COUNTIES}

    for slug, data in pages.items():
        html_out = page(
            slug=slug,
            short=short_map[slug],
            long_name=name_map[slug],
            stats=data["stats"],
            intro=data["intro"],
            dir_blocks_html=data["dirs"],
            sources=data["sources"],
        )
        out_path = os.path.join(COUNTIES_DIR, f"{slug}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_out)
        print("wrote", out_path, len(html_out), "bytes")

# Only regenerate county pages when this file is run directly (e.g. `python3
# build_counties.py`) — not when other build scripts (like build_blog.py)
# import STYLE/FONT_LINKS/header()/footer() from this module for reuse.
if __name__ == "__main__":
    build_all()
