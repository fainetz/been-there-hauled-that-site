"""New posts (2026-11-18) and city pages. Every local fee, rule and address here comes from the
source linked in that post's "sources" list (checked 2026-11-18). Re-check fees each year.
No prices of our own are promised: quotes come from a photo. Typical prices are cited ranges."""

D = "2026-11-18"

# reusable sources
S_RZ = ("Dakota County: The Recycling Zone", "https://dakotacountymn.gov/residents/recycling-waste/recycling-zone-locations/recycling-zone")
S_DC_STUFF = ("Dakota County: Get rid of stuff", "https://dakotacountymn.gov/residents/recycling-waste/get-rid-of-stuff")
S_HEN_DROP = ("Hennepin County: drop-off facilities", "https://www.hennepincounty.gov/residents/recycling-hazardous-waste/drop-off-facilities")
S_HEN_MATT = ("Hennepin County Green Disposal Guide: mattresses", "https://www.hennepincounty.gov/green-disposal-guide/items/mattresses")
S_SCOTT = ("Scott County: what it will cost", "https://www.scottcountymn.gov/1139/What-Will-It-Cost")
S_BRIDGING = ("Bridging: give stuff", "https://bridging.org/give-stuff/")
S_RESTORE = ("Twin Cities Habitat ReStore: donation guidelines", "https://restore.tchabitat.org/donation-guidelines")
S_GOODWILL = ("Goodwill-Easterseals Minnesota", "https://www.goodwilleasterseals.org/contact-us")
S_GOTJUNK = ("1-800-GOT-JUNK: pricing guide", "https://1800gotjunk.com/us_en/blog/pricing")
S_ANGI_MPLS = ("Angi: junk removal cost in Minneapolis", "https://www.angi.com/articles/how-much-does-junk-removal-cost/mn/minneapolis")
S_APPL_LAW = ("Minn. Stat. 115A.9561 (major appliances)", "https://www.revisor.mn.gov/statutes/cite/115A.9561")
S_CRT_LAW = ("Minn. Stat. 115A.9565 (CRT electronics)", "https://www.revisor.mn.gov/statutes/cite/115A.9565")
S_DVR = ("Dakota Valley Recycling: hard-to-dispose items", "https://www.dakotavalleyrecycling.org/component/tags/tag/50-hard-to-dispose")
S_EAGAN = ("City of Eagan: recycling", "https://cityofeagan.com/recycling")
S_BURNS = ("City of Burnsville: recycling & garbage", "https://burnsvillemn.gov/1483/Recycling-Garbage")
S_AV = ("City of Apple Valley: trash & recycling", "https://www.applevalleymn.gov/126/Trash-Recycling")
S_LV = ("City of Lakeville: waste haulers", "https://www.lakevillemn.gov/631/Waste-Haulers")
S_SHAK = ("City of Shakopee: Clean Up Day", "https://www.shakopeemn.gov/residents/my_property/garbage_recycling/clean_up_day.php")
S_HEN_PIANO = ("Hennepin County Green Disposal Guide: pianos and organs", "https://hennepin.us/green-disposal-guide/items/pianos-and-organs")

RZ_LINE = ('<a href="/blog/what-junk-removal-cant-take-dakota-county/">The Recycling Zone</a> (3365 Dodd Rd, Eagan; '
           'Wed 9–8, Thu 12–8, Fri 9–5, Sat 8–5; ID required, open to residents of the 7 metro counties)')


def table(rows, head=("What", "Typical price")):
    return ('<div class="tbl"><table><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>" +
            "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")


PRICE_ROWS = [("Single item (mattress, recliner, TV)", "about $55–$150"),
              ("Couch / sofa", "about $125 on average"),
              ("Refrigerator", "about $130 on average"),
              ("⅛–¼ truckload", "about $107–$396"),
              ("¼–½ truckload", "about $396–$600"),
              ("½–full truckload", "about $600–$1,099")]
PRICE_NOTE = ('<p class="small-note">Typical national figures from the 1-800-GOT-JUNK 2025 pricing guide; Angi lists Minneapolis jobs at roughly '
              '$80–$135 for ⅛ of a truck up to $630–$840 for a full truck. Our price comes from a photo of your items, before any work starts.</p>')

NEW_POSTS = [
{
"slug": "mattress-disposal-dakota-county",
"date": D,
"title": "How to Get Rid of a Mattress in Eagan and Dakota County (2026)",
"desc": "Every way to get rid of an old mattress in Eagan, Burnsville, Apple Valley and Lakeville: what the Recycling Zone takes, drop-off fees, donation rules and junk removal prices.",
"answer": "Dakota County's Recycling Zone in Eagan does not take mattresses or box springs, so in the South Metro your options are a paid drop-off (Hennepin County's Brooklyn Park site charges $25 per piece), a city cleanup day (Shakopee charges $30 per piece), donating a clean one to Bridging, extra-fee bulky pickup through your trash hauler, or a junk removal pickup, which typically runs about $55 to $150 for one mattress.",
"body": """
<h2>Your options, side by side</h2>
""" + table([
    ("Recycling Zone, Eagan", "Not accepted", "Mattresses and box springs are on the county's not-accepted list"),
    ("Hennepin County, Brooklyn Park", "$25 per piece", "A split box spring counts as two; no bed-bug or soiled mattresses"),
    ("Shakopee Clean Up Day", "$30 per piece", "Residents only, on the city's cleanup day"),
    ("Donate to Bridging", "Pickup $160 per booking", "Twin through king, no stains or rips"),
    ("Your trash hauler", "Extra fee, varies", "Eagan, Burnsville, Apple Valley and Lakeville use private haulers"),
    ("Junk removal pickup", "about $55–$150", "Carried out from any room"),
], head=("Option", "Cost", "Notes")) + """

<h2>Can I donate my mattress?</h2>
<p>Only if it's clean. Bridging accepts twin through king mattresses with no stains or rips. Habitat ReStore and Goodwill do not take mattresses or box springs. Cribs, air mattresses and sleeper sofas are refused at Bridging too.</p>

<h2>Can I put a mattress out with the trash?</h2>
<p>Not with regular weekly trash. Eagan, Burnsville, Apple Valley and Lakeville don't run city garbage service; you contract with a licensed private hauler, and bulky items like mattresses are an extra-fee pickup you schedule with them. Ask your hauler for their price before you set it out.</p>

<h2>Is there a mattress law in Minnesota?</h2>
<p>Not yet. As of 2026 Minnesota has no mattress ban or recycling fee in force. A bill for a $5 mattress fee was heard in committee in March 2026 and did not pass.</p>

<h2>The easiest option</h2>
<p>Text a photo of the mattress to us and you'll get a price up front. We carry it out from upstairs or the basement, donate it if it qualifies, and 10–20% of the job goes to a local homeless shelter <em>or</em> dog rescue. We serve {areas}.</p>
""",
"faq": [("Does the Recycling Zone in Eagan take mattresses?", "No. Dakota County's Recycling Zone does not accept mattresses or box springs."),
        ("How much does it cost to get rid of a mattress in the Twin Cities?", "Drop-off fees run about $25 to $30 per piece (Hennepin County, Shakopee Clean Up Day). Junk removal pickup typically costs about $55 to $150."),
        ("Can I donate a used mattress in the Twin Cities?", "Yes, if it has no stains or rips. Bridging accepts twin through king. Habitat ReStore and Goodwill do not take mattresses."),
        ("Is a box spring charged separately?", "Usually. Drop-off sites charge per piece, and Hennepin County counts a split box spring as two pieces.")],
"sources": [S_RZ, S_HEN_MATT, S_SHAK, S_BRIDGING, S_RESTORE, S_GOODWILL, S_GOTJUNK,
            ("Minnesota HF 3713 (2026)", "https://www.revisor.mn.gov/bills/94/2026/0/HF/3713")],
},
{
"slug": "refrigerator-appliance-disposal-minnesota",
"date": D,
"title": "Can You Throw Away a Refrigerator in Minnesota? Appliance Disposal in the South Metro",
"desc": "Minnesota law bans major appliances from the trash. Here's where to take a fridge, washer, dryer or stove in Dakota County, what it costs, and how pickup works.",
"answer": "No. Minnesota Statute 115A.9561 bans major appliances like refrigerators, freezers, washers, dryers, stoves and water heaters from the trash and landfills; they must be recycled or reused. In the South Metro you can use an appliance recycler, a county drop-off ($15 at Hennepin County, $10 at Scott County), a bulky pickup through your hauler, or a junk removal company, which typically charges around $130 for a fridge.",
"body": """
<h2>What counts as a major appliance</h2>
<p>Under Minnesota law: refrigerators, freezers, washers, dryers, stoves and ranges, dishwashers, water heaters, furnaces, air conditioners, dehumidifiers and similar household units. Fridges, freezers and AC units also hold refrigerant that has to be removed by a recycler before the metal is scrapped.</p>

<h2>Where to take an appliance near Eagan</h2>
""" + table([
    ("Recycling Zone, Eagan", "Not for large appliances", "Takes small appliances; refuses appliances, water heaters and microwaves"),
    ("Hennepin County drop-off (Bloomington, Brooklyn Park)", "$15", "Large appliances"),
    ("Scott County HHW, Jordan", "$10", "Household appliances"),
    ("Appliance recyclers (Certified Recycling, Burnsville; JR's Advanced Recyclers, Inver Grove Heights)", "Call for pricing", "Listed by Dakota Valley Recycling"),
    ("Junk removal pickup", "about $130 for a fridge", "We carry it out and take it to a recycler"),
], head=("Where", "Cost", "Notes")) + """

<h2>Can I donate a working appliance?</h2>
<p>Sometimes. Goodwill-Easterseals Minnesota doesn't take large appliances, so working units usually go to a reuse store or a resale listing. If it still works, tell us when you send the photo and we'll try to place it before recycling it.</p>

<h2>Why you can't just set it on the curb</h2>
<p>Haulers can't legally put it in the trash, so a fridge at the curb either sits there or becomes an extra-fee pickup. Old fridges can also be a hazard for kids if the door is left on.</p>

<h2>Getting it out of the house</h2>
<p>The hard part is usually the stairs. We carry appliances out from basements, kitchens and garages anywhere in {areas}, get them to a recycler, and send 10–20% of the job to a local homeless shelter <em>or</em> dog rescue.</p>
""",
"faq": [("Is it illegal to throw a refrigerator in the trash in Minnesota?", "Yes. Minn. Stat. 115A.9561 bans major appliances from mixed municipal solid waste and landfills; they must be recycled or reused."),
        ("Does the Recycling Zone in Eagan take refrigerators?", "No. The Recycling Zone takes small appliances but not large appliances, water heaters or microwaves."),
        ("How much does it cost to get rid of an old fridge?", "County drop-offs charge about $10 to $15. Junk removal pickup averages around $130."),
        ("Do I need to remove the refrigerant myself?", "No. Recyclers recover refrigerant. Don't cut lines yourself.")],
"sources": [S_APPL_LAW, S_RZ, S_HEN_DROP, S_SCOTT, S_DVR, S_GOODWILL, S_GOTJUNK],
},
{
"slug": "bulk-trash-pickup-eagan-burnsville-apple-valley-lakeville",
"date": D,
"title": "Does My City Have Bulk Trash Pickup? Eagan, Burnsville, Apple Valley and Lakeville",
"desc": "How large-item and bulky trash pickup works in Eagan, Burnsville, Apple Valley, Lakeville and Shakopee, plus where to drop off furniture, mattresses and appliances.",
"answer": "Eagan, Burnsville, Apple Valley and Lakeville do not run city garbage or bulk pickup. Each licenses private haulers, so large items go through your own hauler for an extra fee, a Dakota Valley Recycling bulky-item event, a drop-off site, or a junk removal company. Shakopee is different: it has one city hauler, Dick's Sanitation, which does bulk pickup for an added fee, plus an annual Clean Up Day.",
"body": """
<h2>City by city</h2>
""" + table([
    ("Eagan", "No. \"The City does not provide garbage service.\"", "Ask your licensed hauler; DVR events"),
    ("Burnsville", "No. \"The City does not handle pickup or negotiate pricing.\"", "Ask your licensed hauler; DVR events"),
    ("Apple Valley", "No, private licensed haulers", "Bulky pickup through your hauler for a fee; DVR events"),
    ("Lakeville", "No, pick from five licensed haulers", "Ask your hauler; DVR events"),
    ("Shakopee", "One city hauler (Dick's Sanitation)", "Bulk pickup for added fees; Clean Up Day ($30 per mattress)"),
], head=("City", "City bulk pickup?", "What to do")) + """

<h2>What is Dakota Valley Recycling?</h2>
<p>Dakota Valley Recycling (DVR) is the shared recycling staff for Apple Valley, Burnsville, Eagan and Lakeville. It runs bulky-item collection events during the year, some free and some with small fees. Check its site for the next date.</p>

<h2>Drop-off options</h2>
<ul>
<li>""" + RZ_LINE + """: hazardous waste, electronics ($10 per TV), small appliances, scrap metal. <b>Not</b> furniture, mattresses or large appliances.</li>
<li><b>Hennepin County</b> drop-offs in Bloomington and Brooklyn Park: large appliances $15, TVs $10; mattresses $25 at Brooklyn Park only. No furniture.</li>
<li><b>Burnsville Landfill</b> (2650 Cliff Rd W) and transfer stations: call for fees; landfills usually charge by weight with a minimum.</li>
</ul>

<h2>When a junk removal pickup makes more sense</h2>
<p>If you have more than one or two items, don't have a truck, or it's in a basement, one pickup is usually simpler than a hauler fee plus trips to several drop-offs. We take furniture, mattresses and appliances in a single visit across {areas}, and donate what we can.</p>
""",
"faq": [("Does Eagan have bulk trash pickup?", "No. Eagan doesn't provide garbage service; residents schedule bulky pickup with their licensed private hauler or use a junk removal company."),
        ("Does Burnsville pick up large items?", "No. Burnsville licenses private haulers and does not handle pickup; ask your hauler about bulky-item fees."),
        ("Does Apple Valley have a cleanup day?", "Apple Valley, Burnsville, Eagan and Lakeville share Dakota Valley Recycling, which runs bulky-item collection events during the year."),
        ("Where can I drop off furniture in Dakota County?", "The Recycling Zone doesn't take furniture. Donate usable pieces to Bridging or Habitat ReStore, or use a landfill, transfer station or junk removal pickup.")],
"sources": [S_EAGAN, S_BURNS, S_AV, S_LV, ("City of Shakopee: garbage & recycling", "https://www.shakopeemn.gov/residents/my_property/garbage_recycling/index.php"),
            S_SHAK, S_DVR, S_RZ, S_HEN_DROP, S_DC_STUFF],
},
{
"slug": "tv-electronics-recycling-dakota-county",
"date": D,
"title": "Where to Recycle a TV or Electronics Near Eagan (Dakota County 2026)",
"desc": "Old TV, monitor or computer? Recycling Zone fees, Minnesota's CRT trash ban, donation rules and pickup options in Eagan, Burnsville, Apple Valley and Lakeville.",
"answer": "Take TVs and monitors to Dakota County's Recycling Zone at 3365 Dodd Rd in Eagan for $10 each; most other electronics are free there. Minnesota law bans tube (CRT) TVs and monitors from the trash. Flat-screen TVs 65 inches or smaller in working order can be donated to Bridging, and a junk removal pickup typically costs around $94 per TV.",
"body": """
<h2>Fees at a glance</h2>
""" + table([
    ("Recycling Zone, Eagan", "$10 per TV or monitor", "Other electronics free; ID required"),
    ("Hennepin County drop-offs", "$10 for TVs, monitors, laptops", "Bloomington and Brooklyn Park"),
    ("Donate to Bridging", "Free", "Working flat panels 65″ or smaller; no tube TVs"),
    ("Junk removal pickup", "about $94 per TV", "Carried out, including heavy tube TVs"),
], head=("Option", "Cost", "Notes")) + """

<h2>Can I throw an old TV in the trash?</h2>
<p>Not a tube TV or monitor. Minn. Stat. 115A.9565 says a person may not put an electronic product containing a cathode-ray tube in the trash, and that's been the law since 2006. Recycling every TV is the safe choice either way.</p>

<h2>The Recycling Zone, step by step</h2>
<p>""" + RZ_LINE + """. Bring your ID, pay $10 per TV or monitor, and leave computers, printers and small electronics for free. Wipe or remove hard drives first.</p>

<h2>Big console or tube TV?</h2>
<p>Those can weigh well over 100 pounds. If it's stuck in a basement, text us a photo. We carry it out, get it to a recycler, and 10–20% of the job goes to a local homeless shelter <em>or</em> dog rescue. Serving {areas}.</p>
""",
"faq": [("How much does the Recycling Zone charge for a TV?", "$10 per TV or monitor. Most other electronics are accepted free."),
        ("Is it illegal to throw away a TV in Minnesota?", "TVs and monitors with cathode-ray tubes are banned from the trash under Minn. Stat. 115A.9565."),
        ("Where can I donate a TV near Eagan?", "Bridging accepts working flat-panel TVs 65 inches or smaller. It does not take tube TVs."),
        ("Who can use the Recycling Zone?", "Residents of Anoka, Carver, Dakota, Hennepin, Ramsey, Scott and Washington counties, with ID.")],
"sources": [S_RZ, S_CRT_LAW, S_HEN_DROP, S_BRIDGING, S_GOTJUNK],
},
{
"slug": "hot-tub-removal-cost-minnesota",
"date": D,
"title": "Hot Tub Removal in the South Metro: Cost and What to Do Before Pickup",
"desc": "What hot tub removal costs in Eagan, Burnsville, Apple Valley and Lakeville, how to get it ready, and why most tubs are cut up rather than carried out whole.",
"answer": "Hot tub removal typically costs about $200 to $600, depending on size, access and whether it has to be cut apart. Before pickup, turn off the power at the breaker and have an electrician disconnect the hard-wired circuit, then drain the water. Most tubs are cut into pieces so they fit through gates and into a truck.",
"body": """
<h2>What changes the price</h2>
<ul>
<li><b>Size:</b> a 2-person tub vs. an 8-person swim spa.</li>
<li><b>Access:</b> a clear path from the patio to the driveway vs. a fenced backyard, stairs or a deck.</li>
<li><b>Whole or cut up:</b> cutting the shell takes time but avoids damage to fences and lawns.</li>
<li><b>Extras:</b> steps, cover, cover lifter and any surrounding decking.</li>
</ul>
""" + table([("Hot tub removal (typical)", "about $200–$600")]) + """

<h2>Before we arrive</h2>
<ol>
<li><b>Kill the power</b> at the breaker. Hot tubs are usually hard-wired; have an electrician disconnect the circuit.</li>
<li><b>Drain it</b> a day ahead with the drain spigot or a sump pump.</li>
<li><b>Clear a path</b> and unlock gates.</li>
</ol>

<h2>Where does it go?</h2>
<p>Metal, motors and pumps are recycled where possible; the shell and frame usually go to a landfill. A working tub in good shape can sometimes be resold.</p>

<p>Send us a photo of the tub and the path out, and you'll get a price before any work starts. 10–20% of every job goes to a local homeless shelter <em>or</em> dog rescue. Serving {areas}.</p>
""",
"faq": [("How much does hot tub removal cost in Minnesota?", "Typically about $200 to $600 depending on size, access and whether it has to be cut apart."),
        ("Do I need to drain my hot tub before removal?", "Yes. Drain it a day ahead and turn off the power at the breaker."),
        ("Do you need an electrician to remove a hot tub?", "Most hot tubs are hard-wired. Have an electrician disconnect the circuit before pickup.")],
"sources": [("Angi: hot tub, piano and mattress removal ranges", "https://www.angi.com/articles/how-much-does-junk-removal-cost/co/denver")],
},
{
"slug": "piano-removal-minnesota",
"date": D,
"title": "How to Get Rid of an Old Piano in Minnesota",
"desc": "Can you donate an old piano? What piano removal costs in the Twin Cities, how to try to rehome it first, and what happens when nobody wants it.",
"answer": "Most old upright pianos can't be donated, because tuning, moving and repairs cost more than they're worth. Try a free listing first, and if no one takes it, a junk removal or piano mover will haul it; typical prices run about $200 to $550, with a national average around $431.",
"body": """
<h2>Step 1: try to rehome it</h2>
<p>List it free online with clear photos and the brand. Schools, churches and community centers occasionally take a piano that's in good shape. Be honest about tuning and condition, and give the buyer a deadline.</p>

<h2>Step 2: if no one wants it</h2>
""" + table([("Piano removal (typical range)", "about $150–$550"), ("National average", "about $431")]) + """
<p>The price depends on stairs, distance to the truck and whether it's an upright, a spinet or a grand.</p>

<h2>Why is piano removal expensive?</h2>
<p>Uprights often weigh 300 to 800 pounds and are top-heavy. Moving one safely takes several people and the right equipment, especially from a basement.</p>

<h2>What happens to it</h2>
<p>The metal plate, strings and hardware can be recycled; wood and the rest are disposed of properly. Usable benches and stools are donated.</p>

<p>Text us a photo and where the piano sits. We'll quote it up front, and 10–20% of the job goes to a local homeless shelter <em>or</em> dog rescue. Serving {areas}.</p>
""",
"faq": [("Can I donate an old piano in Minnesota?", "Sometimes, if it's in good shape. Most old uprights aren't accepted because repairs and moving cost more than they're worth."),
        ("How much does it cost to remove a piano?", "Typically about $150 to $550, with a national average around $431, depending on stairs and access."),
        ("How heavy is an upright piano?", "Many uprights weigh roughly 300 to 800 pounds.")],
"sources": [S_HEN_PIANO, S_GOTJUNK],
},
{
"slug": "dumpster-vs-junk-removal-vs-landfill-south-metro",
"date": D,
"title": "Dumpster vs Junk Removal vs Hauling It Yourself: What's Cheapest in the South Metro?",
"desc": "Comparing a dumpster rental, a junk removal pickup and hauling to the Burnsville landfill or Recycling Zone yourself, for Eagan, Burnsville, Apple Valley and Lakeville.",
"answer": "For a few bulky items or a single room, junk removal is usually cheapest once you count your time, because the price includes the labor and the disposal fees. Hauling it yourself only wins if you have a truck and the items are accepted at a drop-off you can reach. A dumpster makes sense for multi-day remodels where you'll fill it slowly over a week.",
"body": """
<h2>Quick comparison</h2>
""" + table([
    ("Haul it yourself", "Drop-off fees + your truck and time", "A few items, you have a truck, and the drop-off accepts them"),
    ("Junk removal", "about $107–$396 for a small load", "Furniture, appliances and cleanouts you want gone in one visit"),
    ("Dumpster / bag", "Rental fee + weight limits", "Remodels and long projects you fill yourself over days"),
], head=("Option", "What you pay", "Best for")) + """

<h2>Hauling it yourself: the catch</h2>
<ul>
<li>""" + RZ_LINE + """ doesn't take furniture, mattresses or large appliances.</li>
<li>Landfills like Burnsville Landfill (2650 Cliff Rd W) and Pine Bend charge by weight, often with a minimum charge; Pine Bend's minimum is 1 ton. Call ahead for fees.</li>
<li>Mattresses and appliances go to separate places with separate fees.</li>
</ul>

<h2>Dumpsters: the catch</h2>
<p>You still do all the lifting, there are weight limits and banned items (appliances, mattresses, electronics), and your driveway is blocked for days. Some cities require a permit for street placement.</p>

<h2>Junk removal: the catch</h2>
<p>Price depends on how much space your items take in the truck, so get a quote first. With us, a photo gets you an up-front price, we carry everything out, donate what's usable, and 10–20% goes to a local homeless shelter <em>or</em> dog rescue.</p>
""" + table(PRICE_ROWS) + PRICE_NOTE + """
<p>Serving {areas}.</p>
""",
"faq": [("Is it cheaper to rent a dumpster or hire junk removal?", "For a few items or one room, junk removal is usually cheaper once labor and disposal fees are included. Dumpsters suit multi-day remodels."),
        ("Can I take junk to the Burnsville landfill myself?", "Yes, Burnsville Landfill at 2650 Cliff Rd W accepts self-haul loads. Call for current fees and accepted items."),
        ("What can't go in a dumpster?", "Typically appliances, mattresses, electronics, tires and hazardous waste, which need separate disposal.")],
"sources": [S_DC_STUFF, S_RZ, S_GOTJUNK, S_ANGI_MPLS],
},
]

# ---------------- city pages ----------------
CITIES = [
{"slug": "junk-removal-eagan-mn", "city": "Eagan", "county": "Dakota County",
 "trash": "Eagan does not provide city garbage service. Residents pick a licensed private hauler, and large items are an extra-fee pickup you schedule with that hauler. Dakota Valley Recycling, which Eagan shares with Apple Valley, Burnsville and Lakeville, runs bulky-item events during the year.",
 "trash_src": S_EAGAN,
 "local": "The Recycling Zone is right here in Eagan at 3365 Dodd Rd (Hwy 149). It takes paint, batteries, electronics ($10 per TV), small appliances and scrap metal, but not furniture, mattresses or large appliances. For those, use Bridging in Bloomington for donations, a recycler for appliances, or a pickup."},
{"slug": "junk-removal-burnsville-mn", "city": "Burnsville", "county": "Dakota County",
 "trash": "Burnsville licenses private haulers and \"does not handle pickup or negotiate pricing.\" Bulky items go through your hauler for an extra fee, a Dakota Valley Recycling event, or a junk removal pickup.",
 "trash_src": S_BURNS,
 "local": "Burnsville Landfill (2650 Cliff Rd W) and the Freeway Transfer Station (1020 W Black Dog Rd) accept self-haul loads; call for fees. Certified Recycling in Burnsville takes appliances. Hazardous waste and electronics go to the Recycling Zone in Eagan."},
{"slug": "junk-removal-apple-valley-mn", "city": "Apple Valley", "county": "Dakota County",
 "trash": "Apple Valley licenses private haulers instead of running city trash service, and bulky curbside pickup goes through your hauler for an added fee. Dakota Valley Recycling runs bulky-item events for Apple Valley residents during the year.",
 "trash_src": S_AV,
 "local": "Apple Valley residents use the Recycling Zone in Eagan for hazardous waste and electronics, appliance recyclers for fridges and washers, and Bridging in Bloomington for clean furniture and mattresses."},
{"slug": "junk-removal-lakeville-mn", "city": "Lakeville", "county": "Dakota County",
 "trash": "Lakeville residents choose from five licensed waste haulers; the city doesn't pick up trash or bulky items itself. Ask your hauler about bulky-item fees, or watch for Dakota Valley Recycling collection events.",
 "trash_src": S_LV,
 "local": "From Lakeville, the closest options are the Recycling Zone in Eagan for hazardous waste and electronics, Burnsville Landfill for self-haul loads, and Pine Bend Landfill in Inver Grove Heights, which has a 1-ton minimum charge."},
]


def city_page(c, areas, other_cities, posts):
    city = c["city"]
    answer = (f"Junk removal in {city}, MN typically costs about $55–$150 for a single item and $107–$396 for a small load. "
              f"{city} has no city bulk pickup, so most residents use their private hauler for an extra fee, a drop-off site, or a junk removal pickup. "
              f"__NAME__ is based in Eagan and hauls furniture, mattresses, appliances and cleanouts in {city}, often the same day, "
              f"and sends 10–20% of every job to a local homeless shelter or dog rescue.")
    faq = [(f"How much does junk removal cost in {city}?", f"Typically about $55 to $150 for a single item and $107 to $396 for a small load; send a photo for an exact up-front quote."),
           (f"Does {city} have bulk trash pickup?", c["trash"]),
           (f"Where can I drop off hazardous waste near {city}?", "At Dakota County's Recycling Zone, 3365 Dodd Rd in Eagan (Wed 9-8, Thu 12-8, Fri 9-5, Sat 8-5, ID required)."),
           (f"Do you offer same-day junk removal in {city}?", "Yes, when the schedule allows. Text a photo early in the day."),
           (f"What happens to my junk in {city}?", "Usable items are donated, appliances and metal are recycled, and the rest goes to a licensed disposal site.")]
    body = f"""
<article class="post wrap narrow">
  <nav class="crumbs"><a href="/">Home</a> / {city}</nav>
  <p class="kicker">Junk Removal <span>· {city}, MN</span></p>
  <h1>Junk Removal in {city}, MN</h1>
  <p class="meta">By {{BYLINE}} · <time datetime="{D}">Reviewed {{NICE}}</time></p>
  <div class="answer"><b>Short answer:</b> {answer}</div>
  <p><a class="btn" href="tel:{{TEL}}">Call or text {{PHONE}}</a></p>

  <h2>What we haul in {city}</h2>
  <ul><li>Couches, mattresses, dressers and recliners</li><li>Fridges, washers, dryers and stoves</li><li>Garage, basement and estate cleanouts</li><li>Hot tubs, pianos, yard debris and light construction debris</li></ul>

  <h2>Junk removal prices in {city}</h2>
  {table(PRICE_ROWS)}
  {PRICE_NOTE}

  <h2>Does {city} pick up large items?</h2>
  <p>{c['trash']} (<a href="{c['trash_src'][1]}">source</a>)</p>

  <h2>Where things go near {city}</h2>
  <p>{c['local']}</p>
  <ul>
    <li><a href="/blog/mattress-disposal-dakota-county/">Mattresses in Dakota County</a></li>
    <li><a href="/blog/refrigerator-appliance-disposal-minnesota/">Fridges and appliances (Minnesota law)</a></li>
    <li><a href="/blog/tv-electronics-recycling-dakota-county/">TVs and electronics</a></li>
    <li><a href="/blog/bulk-trash-pickup-eagan-burnsville-apple-valley-lakeville/">Bulk pickup rules by city</a></li>
  </ul>

  <h2>Every {city} job gives back</h2>
  <p>10–20% of every job goes to one local organization, a homeless shelter <em>or</em> a dog rescue, and we text you a photo and video of who your job helped. Usable furniture will be donated, and old towels and blankets set aside for dog shelters.</p>

  <h2>Questions people ask</h2>
  {"".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in faq)}

  <h2>Nearby</h2>
  <p>We also serve {", ".join(f'<a href="/{o["slug"]}/">{o["city"]}</a>' for o in other_cities)} and the rest of the South Metro: {areas}.</p>
</article>
"""
    return answer, faq, body
