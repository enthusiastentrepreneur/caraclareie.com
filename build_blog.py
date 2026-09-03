"""
Generates the Cara Clare blog: blog/index.html (listing) and one post per
entry in POSTS. Reuses the exact design tokens, fonts, header, and footer
from build_counties.py so the blog is visually identical to the rest of the
site — this file only adds new component styles (cards, article prose,
stat callouts, tables) on top, it never edits the shared STYLE string.

Run directly: `python3 build_blog.py`
"""
import os
from build_counties import STYLE, FONT_LINKS, footer

BASE = os.path.dirname(os.path.abspath(__file__))
BLOG_DIR = os.path.join(BASE, "blog")
SITE = "https://caraclareie.com"

# ---------------- Blog-only additional styles (appended, STYLE untouched) ----------------

BLOG_STYLE = """
  /* ============ Blog: header variant (no county pills) ============ */
  .blog-header .brand{ }

  /* ============ Blog hero ============ */
  .blog-hero{ padding:48px 0 8px; }
  .blog-hero h1{ font-size:clamp(30px,4.6vw,44px); }
  .blog-hero p.lede{ font-size:17.5px; color:var(--ink-soft); max-width:56ch; margin-top:14px; }

  /* ============ Post card grid (blog index) ============ */
  .post-grid{ display:grid; grid-template-columns:1fr; gap:22px; margin-top:8px; }
  .post-card{
    display:grid; grid-template-columns:220px 1fr; gap:24px;
    background:var(--surface); border:1px solid var(--surface-line); border-radius:var(--radius-lg);
    padding:20px; box-shadow:var(--shadow); text-decoration:none; color:var(--ink);
    transition:transform .15s ease, box-shadow .15s ease;
  }
  .post-card:hover{ transform:translateY(-2px); box-shadow:0 1px 2px rgba(20,46,44,0.06), 0 14px 30px -14px rgba(20,46,44,0.24); }
  .post-card .thumb{
    border-radius:var(--radius-md); overflow:hidden; aspect-ratio:4/3; background:var(--accent-soft);
  }
  .post-card .thumb svg, .post-card .thumb img{ width:100%; height:100%; display:block; object-fit:cover; }
  .post-card .body{ min-width:0; display:flex; flex-direction:column; }
  .post-card .cat-tag{
    font-family:"Atkinson Hyperlegible"; font-size:12px; font-weight:700; letter-spacing:.06em;
    text-transform:uppercase; color:var(--gold);
  }
  .post-card h2{ font-size:22px; margin-top:6px; }
  .post-card p.excerpt{ font-size:15px; color:var(--ink-soft); margin-top:8px; max-width:60ch; }
  .post-card .post-meta{ font-size:13px; color:var(--ink-faint); margin-top:auto; padding-top:14px; }
  .post-card .go{ font-size:13px; font-weight:700; color:var(--accent-ink); }
  @media (max-width:640px){
    .post-card{ grid-template-columns:1fr; }
    .post-card .thumb{ aspect-ratio:16/9; }
  }
  @media (prefers-reduced-motion: reduce){ .post-card{ transition:none; } }

  .more-soon{
    border:1.5px dashed var(--surface-line); border-radius:var(--radius-lg);
    padding:24px; text-align:center; color:var(--ink-faint); font-size:14.5px; margin-top:6px;
  }

  /* ============ Article page ============ */
  .breadcrumb{ font-size:13px; color:var(--ink-faint); margin-bottom:14px; }
  .breadcrumb a{ color:var(--ink-faint); text-decoration:underline; }
  .article-head{ padding:20px 0 0; }
  .article-head h1{ font-size:clamp(28px,4.6vw,42px); }
  .post-meta-row{
    display:flex; gap:10px; align-items:center; flex-wrap:wrap; margin-top:16px;
    font-size:13.5px; color:var(--ink-faint);
  }
  .post-meta-row .cat-tag{
    font-family:"Atkinson Hyperlegible"; font-size:12px; font-weight:700; letter-spacing:.06em;
    text-transform:uppercase; color:var(--gold); background:var(--gold-soft); padding:4px 10px; border-radius:100px;
  }
  .article-hero-img{
    margin-top:26px; border-radius:var(--radius-lg); overflow:hidden; box-shadow:var(--shadow);
    aspect-ratio:16/7; background:var(--accent-soft);
  }
  .article-hero-img svg, .article-hero-img img{ width:100%; height:100%; display:block; object-fit:cover; }
  @media (max-width:640px){ .article-hero-img{ aspect-ratio:4/3; } }

  .article{ max-width:72ch; margin:0 auto; padding-top:36px; }
  .article > p{ font-size:17.5px; color:var(--ink); margin:0 0 20px; }
  .article > p.lede-p{ font-size:19px; color:var(--ink-soft); }
  .article h2{ font-size:clamp(22px,3vw,28px); margin:44px 0 16px; }
  .article h2:first-of-type{ margin-top:8px; }
  .article ul, .article ol{ font-size:17px; color:var(--ink); padding-left:22px; margin:0 0 20px; }
  .article li{ margin-bottom:8px; }
  .article strong{ color:var(--ink); }

  .stat-callout{
    background:var(--accent-ink); color:#EFF9F5; border-radius:var(--radius-md);
    padding:22px 24px; margin:28px 0; display:flex; gap:16px; align-items:flex-start;
  }
  .stat-callout .num{
    font-family:"Fraunces",serif; font-weight:700; font-size:clamp(26px,4vw,34px); color:#F3E4C9;
    flex:none; line-height:1; font-variant-numeric:tabular-nums;
  }
  .stat-callout p{ margin:0; font-size:15.5px; color:#D3E9E1; }
  .stat-callout strong{ color:#F5FCF9; }

  .rate-table{ width:100%; border-collapse:collapse; margin:24px 0; font-size:15px; }
  .rate-table caption{ text-align:left; font-size:13px; color:var(--ink-faint); margin-bottom:8px; }
  .rate-table th, .rate-table td{
    text-align:left; padding:11px 14px; border-bottom:1px solid var(--surface-line);
  }
  .rate-table th{
    font-family:"Atkinson Hyperlegible"; font-size:12.5px; text-transform:uppercase; letter-spacing:.05em;
    color:var(--ink-faint); font-weight:700; background:var(--bg-alt);
  }
  .rate-table td.amt{ font-variant-numeric:tabular-nums; font-weight:700; color:var(--accent-ink); white-space:nowrap; }
  .rate-table-wrap{ overflow-x:auto; }

  .article-cta{
    background:var(--gold-soft); border:1px solid var(--surface-line); border-radius:var(--radius-lg);
    padding:26px 28px; margin:36px 0 8px;
  }
  .article-cta h3{ font-size:19px; margin-bottom:8px; }
  .article-cta p{ font-size:15px; color:var(--ink-soft); margin:0 0 16px; }

  .article-sources{
    margin-top:40px; padding-top:20px; border-top:1px solid var(--surface-line);
  }
  .article-sources h3{ font-size:13px; text-transform:uppercase; letter-spacing:.08em; color:var(--ink-faint); margin-bottom:10px; }
  .article-sources ul{ list-style:none; margin:0; padding:0; font-size:13.5px; color:var(--ink-soft); }
  .article-sources li{ margin-bottom:6px; }
  .article-sources a{ color:var(--ink-soft); }

  .disclaimer{ font-size:13px; color:var(--ink-faint); margin-top:14px; }
"""

FAVICON_ICON = f'<link rel="icon" type="image/svg+xml" href="{SITE}/favicon.svg">'

def header_blog(active_blog=True):
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
      <a href="index.html"{' class="current-nav"' if active_blog else ''}>Blog</a>
      <a class="btn small" href="../index.html#list-service">List a service</a>
    </nav>
  </div>
</header>"""

# A brand-consistent abstract illustration (no stock photography, no depicted
# people) reusing the logo's two-overlapping-circles motif, sized for either
# a card thumbnail or a full article header via viewBox scaling.
CARE_IMG = "carer-support-grant-ireland.jpg"
CARE_IMG_ALT = "Close-up of an adult child's hand resting on an older parent's hand, representing family caring and the Carer's Support Grant in Ireland"

def care_photo(loading="lazy"):
    attrs = ' fetchpriority="high"' if loading == "eager" else ""
    return f'<img src="{CARE_IMG}" alt="{CARE_IMG_ALT}" loading="{loading}"{attrs} width="1600" height="1066">'

def coin_illustration(big=False):
    vb = "0 0 480 270" if big else "0 0 320 240"
    return f"""<svg viewBox="{vb}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Illustration of a euro coin beside the Cara Clare mark, representing carer entitlements and payments">
  <defs>
    <linearGradient id="bgGrad{'Big' if big else ''}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#EDEFE6"/>
      <stop offset="100%" stop-color="#DCEAE4"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bgGrad{'Big' if big else ''})"/>
  <circle cx="{'150' if big else '110'}" cy="{'150' if big else '150'}" r="{'92' if big else '66'}" fill="#F3E4C9" stroke="#B9791E" stroke-width="3"/>
  <text x="{'150' if big else '110'}" y="{'150' if big else '150'}" font-family="Fraunces, Georgia, serif" font-weight="700" font-size="{'74' if big else '52'}" fill="#B9791E" text-anchor="middle" dominant-baseline="central">&#8364;</text>
  <circle cx="{'320' if big else '215'}" cy="{'95' if big else '80'}" r="{'40' if big else '30'}" fill="#DCEAE4" stroke="#0E4A40" stroke-width="2.5"/>
  <circle cx="{'358' if big else '241'}" cy="{'123' if big else '104'}" r="{'40' if big else '30'}" fill="none" stroke="#1F7A6C" stroke-width="2.5"/>
</svg>"""

# ---------------- Blog index page ----------------

def build_index(posts):
    cards = []
    for p in posts:
        cards.append(f"""        <a class="post-card" href="{p['slug']}.html">
          <div class="thumb">{care_photo()}</div>
          <div class="body">
            <span class="cat-tag">{p['category']}</span>
            <h2>{p['title']}</h2>
            <p class="excerpt">{p['excerpt']}</p>
            <p class="post-meta">{p['date_display']} &middot; {p['read_time']} min read</p>
          </div>
        </a>""")
    cards_html = "\n".join(cards)

    title = "Blog | Cara Clare — Guides for Carers &amp; Older People in Ireland"
    desc = "Plain-English guides on entitlements, home help, transport, and support for older people and family carers in Ireland &mdash; free, independent, and sourced from official data."
    canonical = f"{SITE}/blog/index.html"

    jsonld = f"""{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Cara Clare", "item": "{SITE}/"}},
        {{"@type": "ListItem", "position": 2, "name": "Blog", "item": "{canonical}"}}
      ]
    }},
    {{
      "@type": "Blog",
      "name": "Cara Clare Blog",
      "description": "{desc}",
      "url": "{canonical}",
      "publisher": {{"@type": "Organization", "name": "Cara Clare", "url": "{SITE}/"}}
    }}
  ]
}}"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
{FAVICON_ICON}

<meta property="og:type" content="website">
<meta property="og:site_name" content="Cara Clare">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:locale" content="en_IE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/og-image.png">

{FONT_LINKS}
<style>
{STYLE}
{BLOG_STYLE}
</style>
<script type="application/ld+json">
{jsonld}
</script>
</head>
<body>

{header_blog(active_blog=True)}

<main id="top">
  <section class="blog-hero">
    <div class="wrap">
      <p class="eyebrow">Cara Clare Blog</p>
      <h1>Guides for carers &amp; older people in Ireland</h1>
      <p class="lede">Plain-English explainers on entitlements, home help, transport, and local support &mdash; written from official Irish data, with no sign-up and nothing for sale.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="post-grid">
{cards_html}
      </div>
      <div class="more-soon">More guides are on the way &mdash; <a href="../index.html#list-service">get in touch</a> if there's a topic you'd like covered.</div>
    </div>
  </section>
</main>

{footer("Ireland", ["CSO Census of Population 2022", "Department of Social Protection, gov.ie", "Citizens Information"])}
</body>
</html>
"""

# ---------------- Article builder ----------------

def build_article(p):
    title = f"{p['meta_title']} | Cara Clare"
    canonical = f"{SITE}/blog/{p['slug']}.html"
    og_image = f"{SITE}/og-image.png"

    jsonld = f"""{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Cara Clare", "item": "{SITE}/"}},
        {{"@type": "ListItem", "position": 2, "name": "Blog", "item": "{SITE}/blog/index.html"}},
        {{"@type": "ListItem", "position": 3, "name": "{p['title']}", "item": "{canonical}"}}
      ]
    }},
    {{
      "@type": "BlogPosting",
      "headline": "{p['title']}",
      "description": "{p['meta_desc']}",
      "url": "{canonical}",
      "datePublished": "{p['date_iso']}",
      "dateModified": "{p['date_iso']}",
      "image": "{og_image}",
      "author": {{"@type": "Organization", "name": "Cara Clare", "url": "{SITE}/"}},
      "publisher": {{"@type": "Organization", "name": "Cara Clare", "url": "{SITE}/", "logo": {{"@type": "ImageObject", "url": "{SITE}/favicon.svg"}}}},
      "mainEntityOfPage": {{"@type": "WebPage", "@id": "{canonical}"}}
    }}
  ]
}}"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{p['meta_desc']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
{FAVICON_ICON}

<meta property="og:type" content="article">
<meta property="og:site_name" content="Cara Clare">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['meta_desc']}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="en_IE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p['title']}">
<meta name="twitter:description" content="{p['meta_desc']}">
<meta name="twitter:image" content="{og_image}">

{FONT_LINKS}
<style>
{STYLE}
{BLOG_STYLE}
</style>
<script type="application/ld+json">
{jsonld}
</script>
</head>
<body>

{header_blog(active_blog=True)}

<main id="top">
  <section class="article-head">
    <div class="wrap">
      <p class="breadcrumb"><a href="../index.html">Cara Clare</a> &rsaquo; <a href="index.html">Blog</a> &rsaquo; {p['category']}</p>
      <h1>{p['title']}</h1>
      <div class="post-meta-row">
        <span class="cat-tag">{p['category']}</span>
        <span>{p['date_display']}</span>
        <span>&middot;</span>
        <span>{p['read_time']} min read</span>
      </div>
      <div class="article-hero-img">{care_photo(loading="eager")}</div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <article class="article">
{p['body']}
      </article>
    </div>
  </section>
</main>

{footer("Ireland", p['sources_footer'])}
</body>
</html>
"""

# ---------------- Post content ----------------

POST_BODY = """
        <p class="lede-p">Almost 300,000 people in Ireland provide unpaid care for a family member &mdash; and a lot of them are leaving real money on the table simply because nobody explained what they're entitled to, or because the rules changed and they didn't hear about it. In July 2026, the government made the single biggest change to Carer's Allowance in the scheme's history. Here's what's actually available, in plain English.</p>

        <h2>Why this matters right now</h2>
        <p>Ireland's unpaid family carers grew by more than 50% between 2016 and 2022, according to the CSO's Census of Population &mdash; and nearly a third now provide 43 or more hours of care a week, which is effectively a full-time job with none of the usual supports that come with one. Three separate government payments exist to help: <strong>Carer's Allowance</strong>, <strong>Carer's Benefit</strong>, and the <strong>Carer's Support Grant</strong>. They're easy to mix up, and the eligibility rules for each are different enough that it's worth understanding all three before you assume you don't qualify.</p>

        <div class="stat-callout">
          <span class="num">&euro;1,000</span>
          <p><strong>The new weekly income disregard for a single person's Carer's Allowance means test</strong>, up from &euro;625 &mdash; the largest increase to the disregard in the history of the scheme, effective 2 July 2026.</p>
        </div>

        <h2>What is Carer's Allowance, and how much is it?</h2>
        <p>Carer's Allowance is a weekly payment for people who are providing full-time care to someone who needs it &mdash; a parent, a partner, a child, or another relative. It's means-tested, so how much you get depends on your own (and your spouse or partner's) income and savings. The maximum rates are:</p>

        <div class="rate-table-wrap">
        <table class="rate-table">
          <caption>Carer's Allowance &mdash; maximum weekly rates, 2026</caption>
          <thead><tr><th>Your age</th><th>Full rate</th><th>Half rate*</th></tr></thead>
          <tbody>
            <tr><td>Under 66</td><td class="amt">&euro;270</td><td class="amt">&euro;135</td></tr>
            <tr><td>66 and over</td><td class="amt">&euro;308</td><td class="amt">&euro;154</td></tr>
          </tbody>
        </table>
        </div>
        <p style="font-size:13.5px; color:var(--ink-faint); margin-top:-10px;">*Half rate applies if you're already getting another social welfare payment (such as a State Pension) alongside Carer's Allowance.</p>

        <h2>The means test just became a lot more generous</h2>
        <p>This is the part most people miss, because it's genuinely new: as of <strong>2 July 2026</strong>, the income disregard for the Carer's Allowance means test rose to <strong>&euro;1,000 a week for a single person</strong> (up from &euro;625) and <strong>&euro;2,000 a week for a couple</strong> (up from &euro;1,250). A disregard is the amount of income you can have before it starts reducing your payment &mdash; so this change means a meaningful number of carers who were turned down before, or who never applied because they assumed their income was too high, may now qualify or qualify for more. If you were assessed and refused any time before mid-2026, it's worth asking to be reassessed under the new limits.</p>

        <h2>Who actually qualifies?</h2>
        <p>Beyond the means test, Carer's Allowance has a few core conditions. You need to be aged 18 or over, and either live with the person you're caring for or be able to provide full-time care and attention without living with them. You can work, study, or volunteer for up to <strong>18.5 hours a week</strong> in total while still qualifying &mdash; anything beyond that and you're no longer considered available to provide full-time care. The person you're caring for needs to be assessed as requiring full-time care and attention (or, if they're under 16, already getting Domiciliary Care Allowance), and you need to be habitually resident in Ireland.</p>

        <h2>Carer's Benefit: the option if you're coming from paid work</h2>
        <p>If you've been in insurable employment and need to leave work or cut your hours to care for someone, Carer's Benefit may suit you better than Carer's Allowance. The key difference is that it's based on your <strong>PRSI contributions</strong>, not a full means test &mdash; you need at least 156 PRSI contributions paid since you started work, plus one of a few specific contribution patterns in recent tax years. In exchange, it's time-limited.</p>

        <div class="rate-table-wrap">
        <table class="rate-table">
          <caption>Carer's Benefit &mdash; weekly rate, 2026</caption>
          <thead><tr><th>Caring for</th><th>Weekly rate</th></tr></thead>
          <tbody>
            <tr><td>One person</td><td class="amt">&euro;271</td></tr>
            <tr><td>Two or more people</td><td class="amt">&euro;406.50</td></tr>
          </tbody>
        </table>
        </div>
        <p>You can claim Carer's Benefit for up to <strong>104 weeks (two years) per person</strong> you care for, and it doesn't have to be used in one continuous block. Since July 2026, the personal earnings limit that applies alongside it also rose to &euro;1,000 a week, matching the Carer's Allowance disregard change.</p>

        <h2>The Carer's Support Grant: an extra &euro;2,000 you might be missing</h2>
        <p>Separate from either weekly payment, the <strong>Carer's Support Grant</strong> is a one-off annual payment of <strong>&euro;2,000 per person you care for</strong>, paid automatically every June (usually the first Thursday of the month) to anyone already getting Carer's Allowance, Carer's Benefit, or Domiciliary Care Allowance. Two things surprise people about it: it is <strong>not means-tested</strong>, and it is <strong>not taxable</strong> &mdash; so it doesn't affect your other payments. If you're providing full-time care but aren't getting one of those three payments, you can still apply for the grant separately, as long as you've been caring for at least six months (including the payment date) and work no more than 18.5 hours a week.</p>

        <h2>How to apply</h2>
        <p>Applications for all three payments go through the Department of Social Protection, most easily via <strong>MyWelfare.ie</strong>, or by post using the paper forms available from your local Intreo Centre. For Carer's Allowance and Carer's Benefit, you'll need the person you're caring for to have a medical report completed by their GP as part of the application, along with evidence of your means (for Allowance) or PRSI record (for Benefit). Processing can take some time, so it's worth applying as soon as you know you'll meet the conditions rather than waiting until finances are tight. Because forms and exact steps do change, always check the current process on <a href="https://www.gov.ie/en/department-of-social-protection/services/carers-allowance/" target="_blank" rel="noopener">gov.ie</a> or <a href="https://www.citizensinformation.ie" target="_blank" rel="noopener">citizensinformation.ie</a> before you start.</p>

        <div class="article-cta">
          <h3>Not sure which one applies to you?</h3>
          <p>You don't have to figure this out alone. The Citizens Information Phone Service gives free, independent guidance on exactly which payment fits your situation, and Family Carers Ireland's national careline can talk it through with you directly &mdash; both are listed, with their numbers, on the Cara Clare directory.</p>
          <a class="btn" href="../index.html#money">See money &amp; entitlements on Cara Clare &rarr;</a>
        </div>

        <p>None of this is legal or financial advice &mdash; entitlement rules change, and your own circumstances matter. Use this as a starting point for the conversation with Citizens Information or the Department of Social Protection, not the final word.</p>
"""

POSTS = [
    dict(
        slug="carers-allowance-support-grant-ireland-2026-guide",
        title="Carer's Allowance and the Carer's Support Grant in Ireland: A 2026 Guide",
        meta_title="Carer's Allowance &amp; Support Grant Ireland: 2026 Guide",
        meta_desc="A plain-English 2026 guide to Carer's Allowance, Carer's Benefit, and the Carer's Support Grant in Ireland — current rates, who qualifies, and how to apply.",
        category="Entitlements &amp; Money",
        date_display="3 September 2026",
        date_iso="2026-09-03",
        read_time=9,
        excerpt="The three main payments for family carers in Ireland, what changed in July 2026, and how to work out what you're owed.",
        body=POST_BODY,
        sources_footer=[
            "Department of Social Protection, gov.ie &mdash; Carer's Allowance, Carer's Benefit &amp; Carer's Support Grant",
            "Citizens Information &mdash; Carer's Support Grant",
            "CSO Census of Population 2022 &mdash; Profile 4: Disability, Health &amp; Carers",
        ],
    ),
]

def build_all_blog():
    os.makedirs(BLOG_DIR, exist_ok=True)
    index_html = build_index(POSTS)
    with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("wrote", os.path.join(BLOG_DIR, "index.html"), len(index_html), "bytes")

    for p in POSTS:
        html_out = build_article(p)
        out_path = os.path.join(BLOG_DIR, f"{p['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_out)
        print("wrote", out_path, len(html_out), "bytes")

if __name__ == "__main__":
    build_all_blog()
