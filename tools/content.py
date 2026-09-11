# -*- coding: utf-8 -*-
"""Content model for the Velora Bags static site rebuild.

Every product page is generated from one of the category blocks below plus a
page-specific blurb, so the whole catalog stays structurally identical.
"""

BRAND = "Velora Bags"
SITE = "https://www.verlorabags.com"
EMAIL = "evan.funkytek@gmail.com"
SUPPORT_EMAIL = "support@verlorabags.com"
PHONE = "+86 137 9827 5895"
WA = ("https://wa.me/8613798275895"
      "?text=Hi,%20I%27m%20interested%20in%20your%20custom%20bags,"
      "%20please%20send%20catalog%20and%20price%20list.")
ADDRESS = "No. 8 Huasheng Rd, Shiling, Huadu District, Guangzhou, China"
HOURS = "Mon-Sat 8:30-18:00 (GMT+8)"

# First publication date per article, used for Article schema (editable).
BLOG_DATES = {
    "how-to-choose-bag-fabrics.html": "2026-09-11",
    "bag-factory-qc-checklist.html": "2026-09-08",
    "eco-reusable-bag-trends-2026.html": "2026-09-05",
    "qc-checklist.html": "2026-09-08",
    "eco-bag-material-guide.html": "2026-09-10",
    "eco-bag-printing-qc.html": "2026-09-09",
    "backpack-materials-guide.html": "2026-09-07",
}
BUILD_DATE = "2026-09-11"

# Share image (og:image / Article image) per article, matching the blog index cards.
BLOG_IMAGES = {
    "how-to-choose-bag-fabrics.html": "assets/img/why-materials.webp",
    "bag-factory-qc-checklist.html": "assets/img/why-production.webp",
    "eco-reusable-bag-trends-2026.html": "assets/img/solution-grocery.webp",
    "eco-bag-material-guide.html": "assets/img/cat-jute.webp",
    "eco-bag-printing-qc.html": "assets/img/solution-promo.webp",
    "qc-checklist.html": "assets/img/cat-nonwoven.webp",
    "backpack-materials-guide.html": "assets/img/cat-oxford-fabric.webp",
}

# key -> specification block. Fields feed the spec table and the copy blocks.
CATS = {
    "jute": dict(
        label="Jute & Burlap Bags",
        material="Laminated jute 240-340 gsm, natural / bleached / dyed",
        finish="Matte or gloss BOPP lamination; LDPE inner lining optional",
        branding="Screen print, heat transfer, woven label, leather or cork patch",
        handles="Cotton tape, padded cotton, jute-cotton rope or die-cut handle",
        sizes="Typically 25x30, 30x35, 35x40 cm - fully custom on request",
        testing="Handle pull 12 kg, seam strength, colour fastness to rubbing",
    ),
    "linen": dict(
        label="Linen & Cotton-Linen Bags",
        material="Cotton-linen blend 180-280 gsm, natural or pre-coated",
        finish="Wax coating, PU coating or uncoated washed finish",
        branding="Screen print, digital transfer, embroidery, debossed patch",
        handles="Self-fabric, cotton webbing, leather-look or rope handle",
        sizes="Make-up pouch to shopper scale, custom drawings welcome",
        testing="Coating adhesion, zip cycles 3,000, colour fastness",
    ),
    "canvas": dict(
        label="Cotton Canvas Totes",
        material="8-16 oz cotton canvas, pre-shrunk; organic or recycled options",
        finish="Washed, garment-dyed, PU-coated or natural greige",
        branding="Screen print, heat transfer, embroidery, woven label",
        handles="Self-fabric, padded cotton, webbing or leather-look trim",
        sizes="Small gift tote to large shopper, custom dimensions",
        testing="Handle pull 12 kg, shrinkage after wash, print rub test",
    ),
    "nonwoven": dict(
        label="Non-Woven Bags",
        material="80-120 gsm recycled PP non-woven, 60+ stock colours",
        finish="Gloss or matte lamination; ultrasonic or stitched seams",
        branding="Screen print, heat transfer, laminated full-colour print",
        handles="Non-woven loop, PP rope, die-cut or padded handle",
        sizes="Standard gift sizes plus bespoke die-cut shapes",
        testing="Seam peel strength, handle pull, print adhesion",
    ),
    "wovenpp": dict(
        label="Woven PP Bags",
        material="100-140 gsm laminated PP woven fabric, recycled resin available",
        finish="BOPP film lamination, UV-stabilised outdoor grade on request",
        branding="Flexo print on lamination, patch label, woven tape",
        handles="PP webbing, padded handle, X-stitch reinforced",
        sizes="Grocery to oversized bulk sack, load rated",
        testing="Load test 10-25 kg, drop test, handle fatigue",
    ),
    "tyvek": dict(
        label="Tyvek & Dupont Paper Bags",
        material="1073D Tyvek-style HDPE fibre, 60-110 gsm",
        finish="Soft-touch natural, semi-gloss or full-colour printed",
        branding="Flexo print, screen print, digital full-colour",
        handles="Die-cut, cotton rope, webbing or reinforced paper twist",
        sizes="Compact pouch to large shoulder tote",
        testing="Tear resistance, water repellency, print rub test",
    ),
    "paper": dict(
        label="Paper & Kraft Bags",
        material="120-200 gsm kraft or art paper, FSC-certified stock available",
        finish="Matte / gloss lamination, spot UV, soft-touch coating",
        branding="Offset print, foil stamping, embossing, screen print",
        handles="Paper twist, cotton rope, ribbon or die-cut",
        sizes="Boutique sizes plus custom widths and gussets",
        testing="Handle pull, glue bond, print registration",
    ),
    "cooler": dict(
        label="Insulated & Cooler Bags",
        material="600D polyester shell, PEVA / EVA food-safe lining",
        finish="PU-coated water-resistant shell, welded or bound seams",
        branding="Screen print, heat transfer, embroidered logo patch",
        handles="Webbing with padded grip, adjustable shoulder strap option",
        sizes="Can, bottle, lunch, 6-pack and family cooler formats",
        testing="Insulation hold, leak test, zip cycles, strap pull",
    ),
    "pvc": dict(
        label="PVC & Clear Bags",
        material="0.25-0.5 mm clear or frosted PVC; phthalate-free options",
        finish="Transparent, frosted, tinted or printed panels",
        branding="Screen print, UV print, coloured piping and zip pulls",
        handles="PVC loop, webbing, metal ring or wrist strap",
        sizes="Cosmetic pouch to travel set, custom shapes",
        testing="Cold-crack resistance, seam weld strength, zip cycles",
    ),
    "polyester": dict(
        label="Polyester & Oxford Bags",
        material="210D-600D polyester or oxford with PU coating",
        finish="Water-repellent PU backing, ripstop or diamond weave",
        branding="Screen print, heat transfer, embroidery, rubber patch",
        handles="Webbing, padded strap, adjustable shoulder strap",
        sizes="Foldable shoppers to structured travel bags",
        testing="Water repellency spray test, abrasion, zip cycles",
    ),
    "mesh": dict(
        label="Mesh Bags",
        material="Cotton or polyester mesh with reinforced binding tape",
        finish="Natural mesh, dyed mesh, drawstring or zip closure",
        branding="Printed label, woven patch, screen print on binding",
        handles="Drawstring cord, webbing, tote handle",
        sizes="Produce, laundry, sports and beach formats",
        testing="Mesh burst strength, cord pull, wash durability",
    ),
    "felt": dict(
        label="Felt Bags",
        material="2-3 mm polyester felt; recycled PET felt available",
        finish="Die-cut, laser-cut or stitched construction",
        branding="Applique, embroidery, screen print, laser engraving",
        handles="Die-cut integrated handle, felt or webbing strap",
        sizes="Laptop sleeve, wine tote, gift and promotional sizes",
        testing="Edge durability, stitch strength, colour fastness",
    ),
    "drawstring": dict(
        label="Drawstring Bags",
        material="190T-210D polyester, nylon or cotton drawcord fabric",
        finish="Water-repellent coating, mesh panel or reflective trim",
        branding="Screen print, heat transfer, sublimation full-colour",
        handles="Drawstring cord with cord lock, shoulder-strap option",
        sizes="Shoe, gym, promo and backpack formats",
        testing="Cord lock cycle test, seam strength, colour fastness",
    ),
    "backpack": dict(
        label="Backpacks",
        material="600D polyester, recycled RPET or canvas shell",
        finish="Padded back panel, water-resistant zips, taped seams",
        branding="Embroidery, rubber patch, screen print, metal badge",
        handles="Padded adjustable shoulder straps, luggage trolley sleeve",
        sizes="14-17 inch laptop formats and daypack volumes",
        testing="Zip cycles 5,000, strap pull 25 kg, abrasion test",
    ),
    "tote": dict(
        label="Handbags & Everyday Totes",
        material="PU leather, coated canvas or washed cotton",
        finish="Structured or soft body, magnetic or zip closure",
        branding="Metal hardware logo, embroidery, foil stamping, patch",
        handles="Fixed or adjustable strap, detachable shoulder strap",
        sizes="Mini to shopper scale, custom hardware finishes",
        testing="Hardware salt-spray, strap pull, lining seam strength",
    ),
    "laptop": dict(
        label="Laptop Briefcases",
        material="1680D ballistic nylon, coated canvas or PU leather",
        finish="Foam-padded laptop compartment, water-resistant base",
        branding="Metal badge, embroidery, debossed leather patch",
        handles="Padded top handle, detachable shoulder strap, trolley strap",
        sizes="13, 15 and 17 inch laptop compartment options",
        testing="Drop test, foam compression, zip cycles, strap pull",
    ),
    "duffel": dict(
        label="Duffel & Weekender Bags",
        material="600D polyester, canvas or vegan leather shell",
        finish="Reinforced base, shoe compartment, ventilated pocket option",
        branding="Embroidery, rubber patch, screen print, metal hardware",
        handles="Padded grip, detachable shoulder strap, webbing handles",
        sizes="35-70 L capacity formats",
        testing="Load test 20 kg, strap pull, seam strength, zip cycles",
    ),
    "trolley": dict(
        label="Trolley Cases",
        material="ABS / PC hardshell or soft-side nylon construction",
        finish="Scratch-resistant shell, TSA-friendly lock option",
        branding="Printed shell, name tag, metal badge, custom lining",
        handles="Telescopic handle, 360-degree spinner wheels",
        sizes="Cabin 20 inch to checked 28 inch",
        testing="Wheel roll test, handle cycle test, drop test",
    ),
}

# page file -> category key
PAGE_CAT = {
    "backpack.html": "backpack",
    "bohemian-jute-makeup-pouch.html": "jute",
    "bridal-party-jute-beach-bag.html": "jute",
    "bulk-jute-tote-set.html": "jute",
    "burlap-wine-carrier.html": "jute",
    "canvas-bags.html": "canvas",
    "cooler-bags.html": "cooler",
    "drawstring-bags.html": "drawstring",
    "duffel-weekender.html": "duffel",
    "dupont-paper-shoulder-tote.html": "tyvek",
    "ethnic-linen-lunch-bag.html": "linen",
    "ethnic-style-jute-tote.html": "jute",
    "fashionable-linen-tote.html": "linen",
    "felt-bags.html": "felt",
    "festive-non-woven-gift-bag.html": "nonwoven",
    "foldable-jute-shopping-bag.html": "jute",
    "handbag-tote.html": "tote",
    "insulated-wine-bottle-bag.html": "cooler",
    "jute-bag-with-pvc-patch.html": "jute",
    "jute-bags.html": "jute",
    "laptop-briefcase.html": "laptop",
    "large-capacity-bento-bag.html": "linen",
    "mesh-bags.html": "mesh",
    "multi-functional-canvas-baby-bag.html": "canvas",
    "non-woven-bags.html": "nonwoven",
    "oversized-pp-woven-sack.html": "wovenpp",
    "oxford-bags.html": "polyester",
    "paper-bags.html": "paper",
    "personalized-coated-linen-bag.html": "linen",
    "polyester-bags.html": "polyester",
    "retro-lotus-linen-bag.html": "linen",
    "small-eco-gift-bag.html": "jute",
    "transparent-pvc-toiletry-bag.html": "pvc",
    "travel-shoulder-bag.html": "polyester",
    "travel-trolley.html": "trolley",
    "tyvek-bags.html": "tyvek",
    "wedding-welcome-burlap-bag.html": "jute",
    "white-eco-jute-tote.html": "jute",
    "windowed-jute-gift-bag.html": "jute",
    "woven-pp-bags.html": "wovenpp",
    "yellow-jute-linen-handbag.html": "linen",
}

# page file -> one-sentence positioning line used in the hero and meta description
PAGE_BLURB = {
    "backpack.html": "Padded commuter backpack engineered around your laptop size, branding and target retail price.",
    "bohemian-jute-makeup-pouch.html": "A zipped jute pouch with bohemian print character, sized for cosmetics, gifting and travel sets.",
    "bridal-party-jute-beach-bag.html": "A generous jute beach tote produced in matched sets for bridal parties, resorts and welcome gifts.",
    "bulk-jute-tote-set.html": "Ready-to-brand jute tote sets packed for bulk retail and promotional rollouts.",
    "burlap-wine-carrier.html": "A single-bottle burlap carrier with reinforced base, made for wineries, cellar doors and gift packs.",
    "canvas-bags.html": "Heavyweight cotton canvas totes that hold their shape through retail, laundry and daily carry.",
    "cooler-bags.html": "Insulated cooler bags with food-safe lining for grocery, delivery and picnic programmes.",
    "drawstring-bags.html": "Lightweight drawstring bags that pack flat and print vividly for sports and event giveaways.",
    "duffel-weekender.html": "Weekender and gym duffels with reinforced base, padded grip and optional shoe compartment.",
    "dupont-paper-shoulder-tote.html": "A soft-touch Tyvek-style shoulder tote that folds flat, resists tearing and takes full-colour print.",
    "ethnic-linen-lunch-bag.html": "A zipped linen lunch bag with ethnic detailing, insulated lining available on request.",
    "ethnic-style-jute-tote.html": "Large-capacity jute tote with ethnic print appeal for lifestyle and resort collections.",
    "fashionable-linen-tote.html": "A soft, spacious linen tote positioned for fashion retail and seasonal capsule collections.",
    "felt-bags.html": "Die-cut felt bags that give promotional and laptop programmes a premium matte finish.",
    "festive-non-woven-gift-bag.html": "Festive non-woven gift bags with seasonal print options for holiday and event campaigns.",
    "foldable-jute-shopping-bag.html": "A foldable jute shopper that compresses for shelf display and unfolds to full grocery capacity.",
    "handbag-tote.html": "Structured handbags and everyday totes with custom hardware, lining and logo treatments.",
    "insulated-wine-bottle-bag.html": "Insulated bottle bags that hold temperature for two-bottle gift sets and wine retail.",
    "jute-bag-with-pvc-patch.html": "A laminated jute tote with clear PVC window patch for product visibility and branding.",
    "jute-bags.html": "The classic jute shopper: laminated, printed and stitched to survive real retail use.",
    "laptop-briefcase.html": "Padded laptop briefcases with detachable strap, trolley sleeve and custom hardware.",
    "large-capacity-bento-bag.html": "Thickened linen tote with large capacity for bento, grocery and market hauling.",
    "mesh-bags.html": "Breathable mesh bags for produce, laundry and sports, with drawstring or zip closure.",
    "multi-functional-canvas-baby-bag.html": "A canvas baby bag with multiple compartments, changing mat and stroller straps.",
    "non-woven-bags.html": "Cost-efficient non-woven bags with fast turnaround and strong print coverage.",
    "oversized-pp-woven-sack.html": "Heavy-duty woven PP sacks for bulk grocery and industrial packaging loads.",
    "oxford-bags.html": "Water-repellent oxford fabric bags built for outdoor, travel and promotional use.",
    "paper-bags.html": "Boutique paper bags with premium finishes for retail counters and gifting.",
    "personalized-coated-linen-bag.html": "Coated linen bag personalised with names or logos for premium gifting.",
    "polyester-bags.html": "Versatile polyester carriers for travel and promotion in a wide colour range.",
    "retro-lotus-linen-bag.html": "Retro lotus-print linen bag aimed at lifestyle, museum and boutique retail.",
    "small-eco-gift-bag.html": "A compact jute gift bag sized for small items, samples and event handouts.",
    "transparent-pvc-toiletry-bag.html": "Waterproof clear PVC toiletry bags that pass through security and show contents.",
    "travel-shoulder-bag.html": "A custom travel shoulder bag with adjustable strap and secure zip compartments.",
    "travel-trolley.html": "Cabin and checked trolley cases with spinner wheels and telescopic handle.",
    "tyvek-bags.html": "Tyvek-style bags that are waterproof, tear-resistant and ready for full-colour print.",
    "wedding-welcome-burlap-bag.html": "Burlap welcome bags produced in batches for weddings, hotels and guest gifting.",
    "white-eco-jute-tote.html": "A white laminated jute tote that gives clean, bright artwork reproduction.",
    "windowed-jute-gift-bag.html": "A jute gift bag with transparent window so contents stay visible on shelf.",
    "woven-pp-bags.html": "Heavy-duty recycled PP woven bags for grocers and bulk shopping.",
    "yellow-jute-linen-handbag.html": "A yellow jute-linen handbag with cotton trim for fashion and lifestyle retail.",
}

# Root-level and evergreen page meta descriptions (kept for pages without one)
GENERIC_DESC = "{name} - custom OEM/ODM manufacturing from our Guangzhou bag factory. Flexible MOQ, in-house printing and QC. Request a quote."

CATEGORY_INTRO = {
    "jute": "Jute is the workhorse of reusable retail packaging: strong, plant-based and photogenic. We laminate, print and stitch it in-house, so your artwork survives the journey from shelf to street.",
    "linen": "Linen and cotton-linen blends give a softer, more premium hand feel than raw jute. We coat, print and finish the fabric so the bag keeps its shape while showing off fine detail.",
    "canvas": "Cotton canvas is the most trusted retail tote substrate. We buy mill-certified greige, pre-shrink it, and control stitch density so handles and seams hold under real loads.",
    "nonwoven": "Non-woven is the fastest, most cost-efficient route to a branded reusable bag. It takes full-colour lamination beautifully and suits large promotional runs.",
    "wovenpp": "Woven polypropylene is engineered fabric: light, waterproof and load-rated. It is the standard choice for grocery, bulk and outdoor programmes.",
    "tyvek": "Tyvek-style HDPE fibre behaves like paper but resists water and tearing. It folds flat for shipping and accepts dense full-colour print.",
    "paper": "Paper bags carry a premium retail signal. We work in kraft and coated art stock with the laminations, foils and handles that make counters look considered.",
    "cooler": "Insulated bags are a specification product: shell, foam, lining and seam construction all affect how long contents stay cold. We build and test against your use case.",
    "pvc": "Clear PVC shows exactly what is inside, which is why it works for cosmetics, travel and security-friendly packaging. We weld and finish seams for a clean, retail-ready edge.",
    "polyester": "Polyester and oxford fabrics bring water resistance, colour depth and durability at a sensible price. They suit foldable shoppers, travel bags and promotional ranges.",
    "mesh": "Mesh keeps contents breathable and visible while cutting weight. Ideal for produce, laundry and sports programmes where airflow matters.",
    "felt": "Felt gives a soft, matte, premium surface that die-cuts cleanly into shapes. It is a fast way to make a promotional item feel considered rather than disposable.",
    "drawstring": "Drawstring bags are light, pack flat and print vividly. They are the cheapest reliable way to put a logo on someone's shoulder at an event.",
    "backpack": "Backpacks are a multi-part build: shell, lining, foam, zips, hardware and straps all have to work together. We sample the whole assembly before bulk.",
    "tote": "Handbags and everyday totes are judged on hardware, lining and shape retention. We source the metal, the interlining and the lining to match your price position.",
    "laptop": "Laptop bags live or die on protection and organisation. Foam density, compartment layout and zip quality are specified before we cut fabric.",
    "duffel": "Duffels take the heaviest loads in any range, so base reinforcement, handle anchoring and strap hardware get extra attention in sampling.",
    "trolley": "Trolley cases combine a shell, a frame, wheels and a telescopic handle. We test the moving parts hardest, because that is what fails first.",
}

FAQ_BASE = [
    ("Can you print our logo?", "{branding} - we match Pantone references and supply a print proof before production."),
    ("How long does sampling take?", "A pre-production sample usually takes 7-10 days. Bulk production runs 15-25 days after you approve the sample."),
    ("What about quality control?", "Every order passes an in-line check, a handle or load test and a final AQL inspection. Inspection reports and photos are shared before shipment."),
]
