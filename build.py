"""Builds the whole site: home page (index.template.html) + blog + sitemap + llms.txt.

To rename the business: edit site_config.json, then run  python3 build.py  and push.
Every page, schema tag and blog post picks up the new name. See NAME_TRACKER.md for
the places outside this repo (Facebook, LLC, Render) that need a manual rename.
"""
import json, os, html

INDEXNOW_KEY = "63b214ba1506a151b641df80ffdd5573"  # key file 63b214ba1506a151b641df80ffdd5573.txt at site root; ping with: python3 build.py --ping
CFG = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site_config.json")))

SITE = CFG["site_url"]
FB = CFG["facebook_url"]
DATE = "2026-11-17"
AREAS = ", ".join(CFG["areas"][:-1]) + " and " + CFG["areas"][-1]
NAME = CFG["name"]
PHONE, PHONE_TEL, EMAIL = CFG["phone_display"], CFG["phone_tel"], CFG["email"]
NAME_HTML = f'{CFG["name_part_1"]} <span>{CFG["name_part_2"]}</span>'

POSTS = [
{
"slug": "same-day-junk-removal-south-metro",
"title": "Same-Day Junk Removal in Eagan and the South Metro",
"desc": "How same-day junk removal works in Eagan, Burnsville, Apple Valley, Lakeville and nearby: how to book it, what to have ready, and what it costs.",
"answer": "Yes, same-day junk removal is available in Eagan and the South Metro when the schedule allows. Message a photo of what's going early in the day; you'll get an up-front price and, if a slot is open, the items can be gone the same day.",
"body": """
<h2>How to get same-day removal</h2>
<ol>
<li><b>Message us early</b> with a photo of the items and where they are (basement, garage, upstairs).</li>
<li><b>Get your price</b> up front before anything is lifted.</li>
<li><b>Pick a time</b> from the open slots that day.</li>
<li><b>We load it and haul it</b>; you don't need to move anything to the curb.</li>
</ol>

<h2>When same-day helps most</h2>
<ul>
<li>Move-outs and closing dates</li>
<li>Estate cleanouts after a sale</li>
<li>Landlord turnovers between tenants</li>
<li>A new couch or appliance arriving and the old one has to go</li>
</ul>

<h2>Does same-day cost more?</h2>
<p>Pricing is based on how much you have and what it is. See <a href="/blog/junk-removal-cost-south-metro/">how much junk removal costs in the South Metro</a>.</p>

<h2>Still gives back</h2>
<p>Same-day jobs work like every other job: 10–20% goes to one local homeless shelter <em>or</em> dog rescue, and you get a photo and video of who it helped. We serve {areas}.</p>
""",
"faq": [("Can I get junk removed today in Eagan?", "Often, yes. Message a photo early in the day to check same-day availability."),
        ("Do I need to be home for same-day junk removal?", "Not always. If items are outside or in an open garage and payment is arranged, pickup can often happen without you there.")],
},
{
"slug": "junk-removal-cost-south-metro",
"title": "How Much Does Junk Removal Cost in Eagan and the South Metro?",
"desc": "Typical junk removal prices for single items, partial loads and full loads, what changes the price, and how to get a quote in Eagan, Burnsville, Apple Valley and Lakeville.",
"answer": "Most junk removal jobs in the U.S. cost about $150 to $350, with national averages around $225 to $250. A single item like a mattress often runs $60 to $150, and a full truckload commonly runs $600 to $800. Your exact price depends on how much you have and what it is, so the fastest way to know is to send a photo for an up-front quote.",
"body": """
<h2>Typical junk removal prices</h2>
<p>Published 2026 cost guides land in similar ranges. These are national figures; South Metro quotes vary with the job:</p>
<ul>
<li><b>Single item</b> (mattress, recliner, small appliance): about $60 to $150</li>
<li><b>Large appliance</b> (fridge, washer): about $50 to $150 per item</li>
<li><b>Small or partial load:</b> about $75 to $500 depending on size</li>
<li><b>Full truckload:</b> about $600 to $800</li>
</ul>
<p>Sources: <a href="https://www.lawnstarter.com/blog/cost/junk-removal-price/" rel="nofollow">LawnStarter</a>, <a href="https://www.hireahelper.com/advice/how-much-does-junk-removal-cost/" rel="nofollow">HireAHelper</a>, <a href="https://www.1800gotjunk.com/us_en/blog/pricing" rel="nofollow">1-800-GOT-JUNK</a>.</p>

<h2>What changes the price?</h2>
<ul>
<li><b>Volume:</b> how much of the van it fills is the biggest factor.</li>
<li><b>Weight and type:</b> heavy debris and appliances cost more to dispose of.</li>
<li><b>Access:</b> basements, attics and stairs take more time.</li>
<li><b>Disposal fees:</b> some items carry landfill or recycling fees.</li>
</ul>

<h2>How to get a quote</h2>
<p>Message us a photo of what's going and where it is in the house. We'll give you a price before we lift anything, and <b>same-day removal</b> is often available if you message early. We serve {areas}.</p>

<h2>Where your money goes</h2>
<p>10–20% of every job goes to one local organization: a homeless shelter <em>or</em> a dog rescue. Afterward we text you a photo and video of who your job helped.</p>
""",
"faq": [("How much does it cost to remove one couch?", "Single bulky items like a couch commonly cost about $60 to $150 nationally; send a photo for an exact quote."),
        ("Is junk removal cheaper than renting a dumpster?", "For small or medium jobs it often is, because junk removal includes the labor and you only pay for the space you use.")],
},
{
"slug": "get-rid-of-old-couch-eagan-burnsville-apple-valley",
"title": "How to Get Rid of an Old Couch in Eagan, Burnsville or Apple Valley",
"desc": "Four ways to get rid of an old couch in the South Metro: donate it, ask your garbage hauler, sell or give it away, or book junk removal.",
"answer": "You have four main options: donate it if it's in good shape, ask your garbage hauler about bulky-item pickup, list it free online, or book a junk removal company to carry it out. Note that Dakota County's Recycling Zone in Eagan does not accept furniture or mattresses.",
"body": """
<h2>1. Donate it (if it's in good shape)</h2>
<p>Clean couches without rips, stains or pet damage can often be donated. Call ahead, since many donation centers are picky about upholstered furniture.</p>

<h2>2. Ask your garbage hauler</h2>
<p>Many South Metro cities use private garbage haulers, and many haulers offer bulky-item pickup for a fee. Check your hauler's website or call them.</p>

<h2>3. Give it away online</h2>
<p>Listing it free on Facebook Marketplace or a neighborhood group can work, but you'll need to coordinate pickup and may get no-shows.</p>

<h2>4. Book junk removal</h2>
<p>We'll carry it out from anywhere in the house, so you don't have to move it to the curb, often the same day you message us. If it's donatable, we'll donate it.</p>

<h2>Where not to take it</h2>
<p>Dakota County's <a href="https://dakotacountymn.gov/residents/recycling-waste/recycling-zone-locations/recycling-zone" rel="nofollow">Recycling Zone</a> in Eagan handles household hazardous waste and electronics, but does not take furniture or mattresses.</p>
""",
"faq": [("Does the Recycling Zone in Eagan take couches?", "No. Dakota County's Recycling Zone does not accept furniture or mattresses."),
        ("Will a junk removal company take a couch from my basement?", "Yes. We carry items out from basements, upstairs rooms and garages.")],
},
{
"slug": "what-junk-removal-cant-take-dakota-county",
"title": "What Junk Removal Can't Take (and Where It Goes in Dakota County)",
"desc": "Paint, chemicals, fuel, batteries and other hazardous items can't go in a junk removal load. Here's where Dakota County residents can take them.",
"answer": "Junk removal companies generally can't take hazardous materials like paint, solvents, pesticides, fuel, propane tanks, asbestos or medical waste. Dakota County residents can bring many household hazardous wastes to The Recycling Zone at 3365 Dodd Road in Eagan, where most items are free for residents.",
"body": """
<h2>Items we can't haul</h2>
<ul>
<li>Paint, stains and solvents</li>
<li>Pesticides and pool chemicals</li>
<li>Gasoline, motor oil and propane tanks</li>
<li>Asbestos and medical waste</li>
</ul>

<h2>Where they go: The Recycling Zone in Eagan</h2>
<p>Dakota County's <a href="https://dakotacountymn.gov/residents/recycling-waste/recycling-zone-locations/recycling-zone" rel="nofollow">Recycling Zone</a> (3365 Dodd Road, Eagan) accepts household hazardous waste from residents, and most items are free. It also takes items like batteries and electronics (some electronics have a fee). It does <b>not</b> take furniture, mattresses, appliances, carpet, lumber or yard waste. Check the county's page or call before you go, since lists and hours change.</p>

<h2>What we can take</h2>
<p>Furniture, mattresses, appliances, garage and basement clutter, yard debris and light construction debris. We serve {areas}.</p>
""",
"faq": [("Where can I drop off old paint in Dakota County?", "Residents can bring household hazardous waste like paint to The Recycling Zone at 3365 Dodd Road in Eagan."),
        ("Does junk removal take paint cans?", "Not liquid paint or chemicals. Those should go to a household hazardous waste site like The Recycling Zone.")],
},
{
"slug": "where-does-your-junk-go",
"title": "Where Does Your Junk Go After a Junk Removal Pickup?",
"desc": "What happens to your stuff after we haul it: donation first, recycling, proper disposal, and a share of every job going to a homeless shelter or dog rescue.",
"answer": "After a pickup, usable items get donated, old towels and blankets go to dog shelters, and what's left is recycled or disposed of properly. On top of that, 10–20% of every job's payment goes to one local homeless shelter or dog rescue, and you get a photo and video of who it helped.",
"body": """
<h2>Step 1: Donate what's usable</h2>
<p>Furniture and household goods in good shape go to donation centers instead of the landfill.</p>

<h2>Step 2: Towels and blankets to dog shelters</h2>
<p>Shelters always need old towels and blankets for bedding and bath time, so we set them aside.</p>

<h2>Step 3: Recycle or dispose of the rest properly</h2>
<p>Whatever can't be reused is recycled where possible and disposed of properly.</p>

<h2>Step 4: Your job helps a person or a dog</h2>
<p>10–20% of each job's payment goes to one South Metro organization: a homeless shelter <em>or</em> a dog rescue. We text you a photo and video of who your job helped, and it's yours to share. Photos and videos of people are only taken and shared with their permission.</p>
""",
"faq": [("Do junk removal companies donate items?", "Many do. We donate usable furniture and household goods and give old towels and blankets to dog shelters."),
        ("Will I see who my junk removal job helped?", "Yes. We send a photo and video of the person or shelter dog your job went toward.")],
},
{
"slug": "garage-cleanout-checklist-minnesota",
"title": "Garage Cleanout Checklist for Minnesota Homeowners (Before Winter)",
"desc": "A simple garage cleanout checklist for South Metro homeowners: sort, set aside hazardous items, plan for winter storage, and haul the rest.",
"answer": "Clear your garage before the snow: pull everything into keep, donate and toss piles; set aside paint and chemicals for a hazardous waste drop-off; make room for the car, snow blower and shovels; then have the toss pile hauled away in one trip.",
"body": """
<h2>The checklist</h2>
<ol>
<li><b>Pick a dry day</b> and pull everything out to the driveway.</li>
<li><b>Sort into three piles:</b> keep, donate, toss.</li>
<li><b>Set aside hazardous items</b> like paint, oil and chemicals for <a href="/blog/what-junk-removal-cant-take-dakota-county/">a hazardous waste drop-off</a>.</li>
<li><b>Plan winter space:</b> car, snow blower, shovels, salt and boots near the door.</li>
<li><b>Go vertical:</b> shelves and wall hooks free up floor space.</li>
<li><b>Haul the toss pile</b> in one trip so it doesn't creep back in.</li>
</ol>

<h2>Want help?</h2>
<p>We do garage cleanouts across {areas}. Send a photo for a quote.</p>
""",
"faq": [("When is the best time to clean out a garage in Minnesota?", "Fall, before snow, so the car and snow equipment fit for winter."),
        ("Can junk removal take everything from a garage cleanout?", "Almost everything except hazardous materials like paint, fuel and chemicals.")],
},
{
"slug": "estate-cleanout-after-estate-sale-south-metro",
"title": "Estate Cleanouts: What to Do With Everything Left After the Estate Sale",
"desc": "How families and estate sale companies in the South Metro can clear what's left after an estate sale, from donations to final haul-away.",
"answer": "After an estate sale, set aside anything the family wants to keep, then have a junk removal company clear the rest in one visit. Usable items can be donated, and hazardous items need a separate drop-off.",
"body": """
<h2>1. Do a final family walk-through</h2>
<p>Pull out photos, papers and keepsakes before anything leaves.</p>

<h2>2. Separate hazardous items</h2>
<p>Paint, chemicals and medications need special disposal. See <a href="/blog/what-junk-removal-cant-take-dakota-county/">what junk removal can't take</a>.</p>

<h2>3. Clear the rest in one visit</h2>
<p>We carry out furniture, appliances and leftovers from every room, donate what's usable and leave the house ready for the next step. Tight closing date? Ask about same-day removal.</p>

<h2>For estate sale companies</h2>
<p>We work with estate sale companies and families across {areas}. Message us to set up cleanouts after your sales.</p>
""",
"faq": [("What happens to items that don't sell at an estate sale?", "They're typically donated, hauled away by a junk removal company, or both."),
        ("How long does an estate cleanout take?", "Many can be cleared in a single visit, depending on the size of the home.")],
},
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{site}/images/cover.jpg">
<link rel="icon" href="/images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;0,9..144,900;1,9..144,500;1,9..144,700&family=Inter:wght@400;500;600;800&display=swap" rel="stylesheet">
{ld}
<link rel="stylesheet" href="/styles.css?v=16">
</head>
<body>
<header class="nav">
  <div class="wrap nav-inner">
    <a href="/" class="brand">__NAME_HTML__<small>Junk Removal</small></a>
    <nav>
      <a href="/#services">Services</a>
      <a href="/#giving">Giving back</a>
      <a href="/blog/">Blog</a>
      <a href="/about/">About</a>
      <a href="tel:{tel}" class="btn btn-sm">Contact us</a>
    </nav>
  </div>
</header>
<main>
"""

FOOT = """
</main>
<section class="section quote">
  <div class="wrap quote-inner">
    <div>
      <h2>Need junk removal in the South Metro?</h2>
      <p class="lead">Call or text {phone} for a free quote. Same-day removal available. Every job helps a person <em>or</em> a dog, and you'll get a photo and video of who.</p>
    </div>
    <div class="quote-btns">
      <a class="btn btn-light" href="tel:{tel}">Contact us</a>
      <a class="btn btn-outline-light" href="sms:{tel}">Text us a photo</a>
      <a class="btn btn-outline-light" href="mailto:{email}">Email us</a>
    </div>
  </div>
</section>
<footer class="foot">
  <div class="wrap foot-inner">
    <p class="brand">__NAME_HTML__</p>
    <p>Junk removal · Eagan & the South Metro</p>
    <p class="small">Serving {areas}.</p>
    <p class="small"><a href="tel:{tel}">{phone}</a> · <a href="mailto:{email}">{email}</a></p>
    <p class="small"><a href="/">Home</a> · <a href="/blog/">Blog</a> · <a href="/about/">About</a> · <a href="{fb}">Facebook</a></p>
  </div>
</footer>
<div class="callbar"><a class="btn" href="tel:{tel}">Call us</a><a class="btn btn-ghost" href="sms:{tel}">Text a photo</a></div>
</body>
</html>
"""

from more_posts import NEW_POSTS, CITIES, city_page, D as more_D
POSTS = POSTS + NEW_POSTS

BIZ = {"@type": "LocalBusiness", "@id": SITE + "/#business", "name": "__NAME__", "url": SITE + "/", "telephone": PHONE_TEL, "email": EMAIL}
BIZ_FULL = {"@context": "https://schema.org", "@type": ["LocalBusiness", "HomeAndConstructionBusiness"], "@id": SITE + "/#business", "name": "__NAME__",
            "url": SITE + "/", "telephone": PHONE_TEL, "email": EMAIL, "image": SITE + "/images/cover.jpg", "sameAs": [FB],
            "description": "Junk removal in Eagan and the South Metro of the Twin Cities. 10-20% of every job goes to a local homeless shelter or dog rescue.",
            "address": {"@type": "PostalAddress", "addressLocality": CFG["home_city"], "addressRegion": "MN", "addressCountry": "US"},
            "areaServed": [{"@type": "City", "name": a + ", MN"} for a in CFG["areas"]], "priceRange": "$$", "paymentAccepted": "Cash, payment apps"}
OWNER = CFG.get("owner_name", "").strip()
AUTHOR = ({"@type": "Person", "name": OWNER, "url": SITE + "/about/", "worksFor": {"@id": SITE + "/#business"}} if OWNER
          else {"@type": "Organization", "name": "__NAME__", "url": SITE + "/about/"})
BYLINE = (f'<a href="/about/">{html.escape(OWNER)}</a>, owner of __NAME__' if OWNER else '<a href="/about/">__NAME__</a>')

def ld_tags(data):
    # One <script> per schema object: Google reads arrays, but many AI-visibility scanners only read single objects.
    items = data if isinstance(data, list) else [data]
    return "\n".join('<script type="application/ld+json">' + json.dumps(i).replace("<", "\\u003c") + "</script>" for i in items if i)

def nice(d):
    import datetime
    x = datetime.date.fromisoformat(d)
    return x.strftime("%B ") + str(x.day) + x.strftime(", %Y")

def page(title, desc, url, ld, body):
    return HEAD.format(title=html.escape(title), desc=html.escape(desc), url=url, site=SITE, fb=FB, tel=PHONE_TEL, phone=PHONE,
                       ld=ld_tags(ld)) + body + FOOT.format(fb=FB, areas=AREAS, tel=PHONE_TEL, phone=PHONE, email=EMAIL)

def fill(text):
    return text.replace("__NAME_HTML__", NAME_HTML).replace("__NAME__", NAME)

def build_home():
    t = open("index.template.html").read()
    t = (t.replace("{{NAME_1}}", CFG["name_part_1"]).replace("{{NAME_2}}", CFG["name_part_2"])
          .replace("{{NAME}}", NAME).replace("{{SITE}}", SITE).replace("{{FB}}", FB)
          .replace("{{PHONE_TEL}}", PHONE_TEL).replace("{{PHONE}}", PHONE).replace("{{EMAIL}}", EMAIL))
    open("index.html", "w").write(t)

EXTRA_URLS = []  # (url, lastmod) for standalone pages added below

def build_about():
    url = SITE + "/about/"
    faq = [("Who owns __NAME__?", (f"{OWNER} owns and runs __NAME__, " if OWNER else "__NAME__ is ") + "a junk removal business based in Eagan, Minnesota."),
           ("Where does __NAME__ work?", f"Junk removal across the South Metro of the Twin Cities: {AREAS}, plus nearby cities on request."),
           ("How does __NAME__ give back?", "10-20% of every job goes to one local organization, a homeless shelter or a dog rescue, and the customer gets a photo and video of who it helped. Usable items are donated, and old towels and blankets go to dog shelters."),
           ("How do I get a quote?", f"Call or text a photo to {PHONE}, or email {EMAIL}. Quotes are free and given before any work starts.")]
    ld = [{"@context": "https://schema.org", "@type": "AboutPage", "url": url, "name": "About __NAME__", "about": {"@id": SITE + "/#business"}},
          BIZ_FULL,
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    who = (f"<p>__NAME__ is run by <b>{html.escape(OWNER)}</b>, who lives in the South Metro and does the hauling.</p>" if OWNER else "")
    body = f"""
<article class="post wrap narrow">
  <nav class="crumbs"><a href="/">Home</a> / About</nav>
  <p class="kicker">About <span>· Eagan & South Metro</span></p>
  <h1>About __NAME__</h1>
  <div class="answer">__NAME__ is a local junk removal business based in Eagan, Minnesota, serving {AREAS}. We haul furniture, appliances and cleanouts, donate what's usable, and send 10–20% of every job to a local homeless shelter <em>or</em> a dog rescue.</div>
  {who}
  <h2>Why we started</h2>
  <p>Most junk removal ends at the landfill. We wanted every haul to do some good for the South Metro: a share of every job goes to people experiencing homelessness or to dogs waiting for homes, and you get a photo and video of who your job helped.</p>
  <h2>What we haul</h2>
  <p>Furniture, mattresses, appliances, garage and basement cleanouts, estate and move-out cleanouts, yard debris and light construction debris. We carry it out from anywhere in the house.</p>
  <h2>How it works</h2>
  <ol><li>Text a photo of what's going.</li><li>Get a price up front.</li><li>We load it and haul it, often the same day.</li><li>You get a photo and video of who your job helped.</li></ol>
  <h2>Contact</h2>
  <p>Call or text <a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{FB}">Facebook</a></p>
  <h2>Questions people ask</h2>
  {"".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>" for q, a in faq)}
</article>
"""
    os.makedirs("about", exist_ok=True)
    open("about/index.html", "w").write(fill(page("About __NAME__ | Junk Removal in Eagan, MN", f"__NAME__ is a junk removal business in Eagan, MN serving {AREAS}. 10-20% of every job goes to a local homeless shelter or dog rescue.", url, ld, body)))

def build_cities():
    for c in CITIES:
        url = f"{SITE}/{c['slug']}/"
        answer, faq, body = city_page(c, AREAS, [o for o in CITIES if o is not c], POSTS)
        body = body.replace("{BYLINE}", BYLINE).replace("{NICE}", nice(more_D)).replace("{TEL}", PHONE_TEL).replace("{PHONE}", PHONE)
        biz = dict(BIZ_FULL, **{"@id": SITE + "/#business"})
        ld = [{"@context": "https://schema.org", "@type": "WebPage", "url": url, "name": f"Junk removal in {c['city']}, MN",
               "dateModified": more_D, "about": {"@id": SITE + "/#business"}},
              {"@context": "https://schema.org", "@type": "Service", "serviceType": "Junk removal", "name": f"Junk removal in {c['city']}, MN",
               "url": url, "provider": {"@id": SITE + "/#business"}, "areaServed": {"@type": "City", "name": c["city"] + ", MN"}},
              biz,
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                  {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                  {"@type": "ListItem", "position": 2, "name": f"Junk removal in {c['city']}", "item": url}]}]
        os.makedirs(c["slug"], exist_ok=True)
        open(f"{c['slug']}/index.html", "w").write(fill(page(f"Junk Removal {c['city']}, MN: Prices & Same-Day Pickup | __NAME__",
            f"Junk removal in {c['city']}, MN: typical prices, {c['city']}'s bulk pickup rules, where to drop things off, and same-day pickup. 10-20% of every job helps a local shelter or dog rescue.", url, ld, body)))
        EXTRA_URLS.append((url, more_D))

def build():
    build_home()
    build_about()
    build_cities()
    for p in POSTS:
        url = f"{SITE}/blog/{p['slug']}/"
        pub, upd = p.get("date", DATE), p.get("updated", p.get("date", DATE))
        ld = [
            {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["desc"],
             "datePublished": pub, "dateModified": upd, "mainEntityOfPage": url, "url": url, "image": SITE + "/images/cover.jpg",
             "author": AUTHOR, "publisher": BIZ, "about": {"@id": SITE + "/#business"}},
            BIZ_FULL,
            {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
                {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]},
        ]
        # visible Q&A (not collapsed) so crawlers and AI read the same text as the FAQ schema
        faq_html = "".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>" for q, a in p["faq"])
        sources_html = ("<h2>Sources</h2><ul class=\"sources\">" + "".join(f'<li><a href="{u}">{html.escape(t)}</a></li>' for t, u in p["sources"]) + "</ul>") if p.get("sources") else ""
        others = "".join(f'<li><a href="/blog/{o["slug"]}/">{html.escape(o["title"])}</a></li>' for o in POSTS if o is not p)
        body = f"""
<article class="post wrap narrow">
  <nav class="crumbs"><a href="/">Home</a> / <a href="/blog/">Blog</a></nav>
  <p class="kicker">Junk Removal <span>· South Metro</span></p>
  <h1>{html.escape(p['title'])}</h1>
  <p class="meta">By {BYLINE} · <time datetime="{upd}">{"Updated " if upd != pub else ""}{nice(upd)}</time></p>
  <div class="answer"><b>Short answer:</b> {p['answer']}</div>
  {p['body'].format(areas=AREAS)}
  <h2>About __NAME__</h2>
  <p>__NAME__ is a junk removal business based in Eagan, Minnesota, serving {AREAS}. __NAME__ hauls furniture, appliances and cleanouts, donates what's usable, and sends 10–20% of every job to a local homeless shelter <em>or</em> a dog rescue. Text a photo to {PHONE} for an up-front price.</p>
  <h2>Questions people ask</h2>
  {faq_html}
  {sources_html}
  <h2>More from the blog</h2>
  <ul class="more">{others}</ul>
</article>
"""
        os.makedirs(f"blog/{p['slug']}", exist_ok=True)
        open(f"blog/{p['slug']}/index.html", "w").write(fill(page(p["title"] + " | __NAME__", p["desc"], url, ld, body)))

    cards = "".join(f'<a class="post-card" href="/blog/{p["slug"]}/"><h2>{html.escape(p["title"])}</h2><p>{html.escape(p["desc"])}</p><span>Read →</span></a>' for p in POSTS)
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": "__NAME__ Blog", "url": SITE + "/blog/", "publisher": BIZ,
          "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{SITE}/blog/{p['slug']}/"} for p in POSTS]}
    body = f"""
<section class="section">
  <div class="wrap">
    <p class="kicker">Junk Removal <span>· Blog</span></p>
    <h1>Junk removal tips for Eagan & the South Metro.</h1>
    <p class="lead">Straight answers on prices, what to do with old stuff, and where things go in Dakota County.</p>
    <div class="post-grid">{cards}</div>
  </div>
</section>
"""
    os.makedirs("blog", exist_ok=True)
    open("blog/index.html", "w").write(fill(page("Junk Removal Blog | Eagan & South Metro | __NAME__",
        "Junk removal tips, prices and local disposal answers for Eagan, Burnsville, Apple Valley, Lakeville and the South Metro.", SITE + "/blog/", ld, body)))

    newest = max(p.get("updated", p.get("date", DATE)) for p in POSTS)
    urls = [(SITE + "/", newest), (SITE + "/blog/", newest), (SITE + "/about/", newest)] + [(f"{SITE}/blog/{p['slug']}/", p.get("updated", p.get("date", DATE))) for p in POSTS] + EXTRA_URLS
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"  <url><loc>{u}</loc><lastmod>{m}</lastmod></url>\n" for u, m in urls) + "</urlset>\n")
    bots = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "PerplexityBot", "ClaudeBot", "Claude-SearchBot", "Applebot", "Google-Extended"]
    open("robots.txt", "w").write("".join(f"User-agent: {x}\nAllow: /\n\n" for x in bots) + f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open("llms.txt", "w").write(fill(
        "# __NAME__\n\n"
        "> Junk removal in Eagan and the South Metro of the Twin Cities, Minnesota. 10-20% of every job goes to one local homeless shelter or dog rescue, and customers get a photo and video of who their job helped.\n\n"
        f"- Service area: {AREAS}\n- Services: furniture, appliances, garage and basement cleanouts, estate and move-out cleanouts, yard debris, light construction debris\n"
        f"- Quotes: free, up front, from a photo. Call/text: {PHONE} · Email: {EMAIL} · Facebook: {FB}\n- Payment: cash or payment app\n\n## Pages\n" +
        "".join(f"- [Junk removal in {c['city']}, MN]({SITE}/{c['slug']}/)\n" for c in CITIES) + f"- [About]({SITE}/about/)\n\n## Blog\n" +
        "".join(f"- [{p['title']}]({SITE}/blog/{p['slug']}/): {p['desc']}\n" for p in POSTS)))

def ping():
    import urllib.request
    urls = [u for u, _ in [(SITE + "/", 0), (SITE + "/blog/", 0), (SITE + "/about/", 0)]] + [f"{SITE}/blog/{p['slug']}/" for p in POSTS] + [u for u, _ in EXTRA_URLS]
    data = json.dumps({"host": SITE.split("//")[1], "key": INDEXNOW_KEY, "keyLocation": f"{SITE}/{INDEXNOW_KEY}.txt", "urlList": urls}).encode()
    r = urllib.request.urlopen(urllib.request.Request("https://api.indexnow.org/indexnow", data=data, headers={"Content-Type": "application/json; charset=utf-8"}))
    print("IndexNow:", r.status, len(urls), "urls")

if __name__ == "__main__":
    import sys
    build()
    if "--ping" in sys.argv:
        ping()
    print("built", len(POSTS), "posts")
