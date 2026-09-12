# -*- coding: utf-8 -*-
"""Content for the Europe / EU market pages.

Written for European and Eastern European B2B search intent: import terms,
customs paperwork and the national packaging-compliance schemes that decide
whether a bag can legally be placed on the market. Every page carries its own
copy, FAQ and structured data - none of these are templated duplicates.
"""

CHECK = ('<svg viewBox="0 0 24 24" fill="none" stroke-width="1.8">'
         '<path d="M20 6L9 17l-5-5"/></svg>')

PAGES = [
    # ------------------------------------------------------------------ hub
    dict(
        slug="europe.html",
        crumb="Europe & the EU",
        title="Custom Bags for European Importers | Verlora Bags",
        desc="OEM tote and reusable bag production for European importers: DDP delivery, EORI and VAT paperwork, EPR-ready materials. MOQ 300 pcs per style.",
        image="assets/img/hero-bags-full.webp",
        main="""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Europe &amp; the EU</span>
    <h1>Bag Manufacturing for European Importers</h1>
    <p class="lead">Custom totes, shoppers and promotional bags built in Guangzhou for brands across Europe, with the import paperwork, compliance documentation and delivery terms EU buyers actually ask for.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">How an order runs</span><h2>From Tech Pack to Your European Warehouse</h2><p class="lead">One account manager, English-language communication, and a schedule you can build a retail calendar around.</p></div>
    <div class="steps">
      <div class="step reveal"><h3>Quote &amp; spec review</h3><p>Send drawings, target price and volume. We reply within one business day with costing options and the fabric that fits your price position.</p></div>
      <div class="step reveal delayed-1"><h3>Sampling</h3><p>A pre-production sample in 7&ndash;10 days, shipped by DHL or FedEx so your buyer can approve it in days rather than weeks.</p></div>
      <div class="step reveal delayed-2"><h3>Bulk production</h3><p>15&ndash;25 days after sample approval, with in-line checks, an AQL final inspection and photo reports before the cartons are sealed.</p></div>
      <div class="step reveal delayed-3"><h3>Delivery</h3><p>Sea, rail or air into your warehouse under DDP, or DAP and FOB if you would rather use your own forwarder.</p></div>
    </div>
  </div>
</section>
<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container split">
    <div class="split-copy reveal">
      <span class="eyebrow">Delivery terms</span>
      <h2>Shipping Terms European Buyers Ask For</h2>
      <p class="lead">Most European programmes want one landed number. Tell us your warehouse and we will quote that way.</p>
      <ul>
        <li><strong>DDP</strong> to your warehouse, with freight duty and import clearance handled for you</li>
        <li><strong>DAP or FOB</strong> Ningbo and Shenzhen when you use your own forwarder</li>
        <li>Sea freight into Hamburg, Rotterdam, Antwerp, Gda&#324;sk, Le Havre and Constan&#539;a</li>
        <li>Rail via the China&ndash;Europe corridor as an 18&ndash;25 day transit option</li>
        <li>Air freight for samples, launch stock and replenishment runs</li>
      </ul>
      <a class="btn btn-primary" href="quote.html">Request a DDP Quote</a>
    </div>
    <div class="split-media reveal delayed-1"><img src="assets/img/hero-bags-full.webp" alt="Custom reusable bags produced for European importers" width="560" height="460" loading="lazy"></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Import paperwork</span><h2>The Documentation Pack We Prepare</h2><p class="lead">Your customs broker and your compliance team both need data from the supplier. We prepare it at order stage rather than on request.</p></div>
    <ul class="check-list reveal">
      <li>%s<span><strong>Commercial invoice and packing list</strong> issued in the format your broker expects, with your EORI reference.</span></li>
      <li>%s<span><strong>Correct HS codes</strong> for tote, shopping, promotional and insulated bags so duty is assessed properly.</span></li>
      <li>%s<span><strong>Material composition and weights</strong> per SKU, the input your EPR registration depends on.</span></li>
      <li>%s<span><strong>REACH and OEKO-TEX documentation</strong> for fabric, webbing, lining and trims.</span></li>
      <li>%s<span><strong>Recycled-content evidence</strong> with GRS transaction certificates where recycled material is used.</span></li>
      <li>%s<span><strong>Carton data</strong> including weights, dimensions, polybag material and units per carton.</span></li>
    </ul>
  </div>
</section>
<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Country guides</span><h2>Working With Us Market by Market</h2><p class="lead">National packaging rules and import habits differ more than most buyers expect. Start with your market.</p></div>
    <div class="product-grid">
      <a class="category-card reveal" href="markets/germany.html"><h3>Germany</h3><p>VerpackG and LUCID registration, dual-system licensing, and the QC documentation German retailers expect.</p><span class="cat-chip">Read the guide</span></a>
      <a class="category-card reveal delayed-1" href="markets/france.html"><h3>France</h3><p>AGEC, the Triman sorting logo and French-language labelling for consumer-facing packaging.</p><span class="cat-chip">Read the guide</span></a>
      <a class="category-card reveal delayed-2" href="markets/netherlands.html"><h3>Netherlands</h3><p>Afvalfonds packaging fees, short sea transit and buyers who lead on recycled content.</p><span class="cat-chip">Read the guide</span></a>
      <a class="category-card reveal" href="markets/poland.html"><h3>Poland</h3><p>BDO registration, Gda&#324;sk routing and one of the fastest-growing retail markets in the EU.</p><span class="cat-chip">Read the guide</span></a>
      <a class="category-card reveal delayed-1" href="markets/czechia.html"><h3>Czechia</h3><p>EKO-KOM compliance, Prague and Brno delivery, and a strong promotional gift market.</p><span class="cat-chip">Read the guide</span></a>
      <a class="category-card reveal delayed-2" href="markets/romania.html"><h3>Romania</h3><p>EPR obligations, Constan&#539;a sea routing and cost-engineered programmes for a growing market.</p><span class="cat-chip">Read the guide</span></a>
    </div>
    <p style="text-align:center;margin-top:44px"><a class="btn btn-primary" href="eu-compliance.html">EU Packaging Compliance Explained</a></p>
  </div>
</section>
""" % (CHECK, CHECK, CHECK, CHECK, CHECK, CHECK),
        faq_head=("Common questions", "European Buyers Ask Us"),
        faq=[
            ("Do you ship DDP into the EU?",
             "Yes. We quote DDP to your warehouse in most EU countries, which means we arrange freight, duty and import clearance and you receive one landed price. If you would rather control the import yourself we also quote DAP and FOB Ningbo or Shenzhen."),
            ("Can you supply the data we need for EPR registration?",
             "Yes. EPR reporting is based on the packaging you place on the market, so we provide per-SKU material composition, unit and packaging weights, and carton data at order stage. See our EU packaging compliance guide for what each national scheme asks for."),
            ("Do you charge EU VAT?",
             "No. We are a China-based manufacturer without an EU VAT number, so we do not charge EU VAT on export orders. Import VAT is settled by the importer, or by our freight partner when the order is shipped DDP."),
            ("What is the minimum order for a European programme?",
             "MOQ is 300 pcs per style for most bag types, and 100 pcs on selected promotional lines. Mixed colourways can be combined within one style to reach the minimum."),
        ],
        cta=("The next step", "Get a Landed Cost for Your European Programme",
             "Send your spec, target price and destination warehouse. We will come back within one business day with costing and a realistic delivery window.",
             "Request a Quote", "quote.html"),
    ),
    # ------------------------------------------------------- compliance guide
    dict(
        slug="eu-compliance.html",
        crumb="EU Packaging Compliance",
        title="EU Packaging Compliance for Bags: PPWR & EPR | Verlora Bags",
        desc="How PPWR, EPR registration, VerpackG, LUCID, AGEC and Triman affect imported bags, and the compliance documentation Verlora supplies with each order.",
        image="assets/img/why-materials.webp",
        main="""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">EU compliance</span>
    <h1>EU Packaging Compliance for Imported Bags</h1>
    <p class="lead">Packaging rules are being harmonised across Europe and extended to reusable bags. Here is what the obligations ask for, and the documentation we hand you to support your registration and reporting.</p>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="split-copy reveal">
      <span class="eyebrow">PPWR</span>
      <h2>What the Packaging Regulation Changes</h2>
      <p class="lead">The EU Packaging and Packaging Waste Regulation replaced much of the previous patchwork of national rules with one framework. It applies from 2026, with further requirements phasing in to 2030.</p>
      <p>The obligations land on the producer: the business that places the bag on the EU market. That is normally you, the brand or importer, not the factory. What you need from a supplier is therefore <strong>data</strong>, not a certificate.</p>
      <ul>
        <li>Recyclability requirements for packaging placed on the market</li>
        <li>Minimum recycled content thresholds for plastic packaging</li>
        <li>Harmonised labelling and material marking</li>
        <li>Reuse and refill targets that cover reusable carrier bags</li>
        <li>Mandatory EPR registration in every member state you sell into</li>
      </ul>
      <a class="btn btn-primary" href="quote.html">Ask for the Data Pack</a>
    </div>
    <div class="split-media reveal delayed-1"><img src="assets/img/why-materials.webp" alt="Bag material samples prepared for EU compliance assessment" width="560" height="460" loading="lazy"></div>
  </div>
</section>
<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">EPR by country</span><h2>Where You Have to Register</h2><p class="lead">Extended producer responsibility is still administered nationally. These are the registration routes that matter most to bag programmes.</p></div>
    <ul class="check-list reveal">
      <li>%s<span><strong>Germany</strong> &mdash; registration in the LUCID packaging register, then licensing through a dual system under the VerpackG.</span></li>
      <li>%s<span><strong>France</strong> &mdash; EPR under the AGEC law, via an approved scheme, plus the Triman sorting mark on consumer-facing packaging.</span></li>
      <li>%s<span><strong>Netherlands</strong> &mdash; packaging fee and reporting through the Afvalfonds Verpakkingen.</span></li>
      <li>%s<span><strong>Poland</strong> &mdash; entry in the BDO register before packaging is placed on the market.</span></li>
      <li>%s<span><strong>Czechia</strong> &mdash; compliance and reporting through the EKO-KOM scheme.</span></li>
      <li>%s<span><strong>Romania</strong> &mdash; national EPR obligations for packaging placed on the market.</span></li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Our part</span><h2>The Compliance Data We Supply</h2><p class="lead">Registration and reporting are yours to file. The figures they are built on come from us.</p></div>
    <ul class="check-list reveal">
      <li>%s<span><strong>Per-SKU material breakdown</strong> covering fabric, lining, webbing, thread, hardware and printed decoration.</span></li>
      <li>%s<span><strong>Unit and packaging weights</strong> separated into the product and the packaging that carries it.</span></li>
      <li>%s<span><strong>Recyclability input</strong> such as mono-material construction options and removable trim.</span></li>
      <li>%s<span><strong>Recycled content evidence</strong> with GRS transaction certificates where recycled fibre is specified.</span></li>
      <li>%s<span><strong>REACH SVHC statements</strong> and OEKO-TEX test reports for the materials in your bill.</span></li>
      <li>%s<span><strong>Artwork support</strong> if you need the Triman mark, material codes or sorting text built into the print layout.</span></li>
    </ul>
  </div>
</section>
<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container split">
    <div class="split-copy reveal">
      <span class="eyebrow">Restricted substances</span>
      <h2>REACH, PFAS and Food Contact</h2>
      <p class="lead">Substance rules bite earlier than packaging rules, because they apply to the material itself.</p>
      <ul>
        <li>REACH SVHC screening of fabric, webbing, lining and trim</li>
        <li>PFAS-free water-repellent finishes as the default option</li>
        <li>Food-contact compliant linings for coolers and grocery programmes on request</li>
        <li>Nickel-safe and lead-free hardware</li>
        <li>Phthalate and heavy-metal testing to the limits your market applies</li>
      </ul>
      <a class="btn btn-primary" href="certifications.html">See Certifications</a>
    </div>
    <div class="split-media reveal delayed-1"><img src="assets/img/why-production.webp" alt="Material compliance testing at the Verlora bag factory" width="560" height="460" loading="lazy"></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <p class="lead" style="max-width:860px;margin:0 auto;text-align:center;color:var(--muted)">This page is written to help you ask the right questions of a supplier. Registration schemes, thresholds and deadlines change, and they differ by member state. Please confirm your own obligations with the relevant national scheme or a compliance adviser before you place a product on the market.</p>
  </div>
</section>
""" % (CHECK, CHECK, CHECK, CHECK, CHECK, CHECK, CHECK, CHECK, CHECK, CHECK, CHECK, CHECK),
        faq_head=("Common questions", "Compliance Questions We Get Asked"),
        faq=[
            ("Are reusable bags covered by packaging EPR?",
             "In most member states, reusable bags placed on the market are treated as packaging or as a single-use plastic item with its own obligations, so producer responsibility applies. Because the scope differs by country, check the national scheme for the markets you sell into."),
            ("Can you print the Triman logo for France?",
             "Yes. If you supply the artwork or confirm the sorting instructions that apply to your bag, we will place the mark in the print layout and include it in the proof you approve before bulk production."),
            ("Do you provide a certificate of recyclability?",
             "We supply material composition, weights and recycled-content evidence, which is what a recyclability assessment is built on. The formal assessment for a specific national scheme is normally issued by your compliance provider."),
            ("Which recycled content options do you have?",
             "Recycled content is available in rPET fabrics, recycled PP non-woven and recycled cotton blends, with GRS transaction certificates where certified material is used. We will tell you what percentage is achievable at your target price."),
        ],
        cta=("Documentation", "Get Your Compliance Data Pack",
             "Tell us the markets you sell into and we will compile the material, weight and testing documentation those schemes ask for.",
             "Request the Data Pack", "quote.html"),
    ),
    # --------------------------------------------------------------- Germany
    dict(
        slug="markets/germany.html",
        crumb="Germany",
        parent="Europe & the EU",
        title="Custom Bags for German Brands: DDP & LUCID | Verlora Bags",
        desc="Custom tote, shopper and promotional bag production for German brands, with VerpackG and LUCID data, DDP delivery into Hamburg and AQL inspection reports.",
        image="assets/img/solution-retail.webp",
        main="""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Germany</span>
    <h1>Custom Bag Manufacturing for Brands in Germany</h1>
    <p class="lead">German buyers audit the paperwork as closely as the sample. We build custom totes, shoppers and promotional bags with the specification discipline and documentation that retail programmes there require.</p>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="split-copy reveal">
      <span class="eyebrow">Why German buyers work with us</span>
      <h2>Specification First, Price Second</h2>
      <p class="lead">A German programme usually starts with a signed-off sample and a documented bill of materials. That suits how we work.</p>
      <ul>
        <li>Every material, weight and trim fixed in writing before sampling closes</li>
        <li>Colour fastness, handle pull and seam strength tested and reported</li>
        <li>Photographic QC report before the cartons are sealed</li>
        <li>Honest lead times rather than optimistic ones</li>
      </ul>
      <a class="btn btn-primary" href="../quote.html">Request a German Programme Quote</a>
    </div>
    <div class="split-media reveal delayed-1"><img src="../assets/img/solution-retail.webp" alt="Custom branded bags produced for German retail programmes" width="560" height="460" loading="lazy"></div>
  </div>
</section>
<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Compliance</span><h2>VerpackG, LUCID and Material Rules</h2><p class="lead">German packaging law is the most detailed in the EU. Here is what we can support and what stays with you.</p></div>
    <ul class="check-list reveal">
      <li>%s<span><strong>LUCID registration data</strong> &mdash; per-SKU material types and weights so you can register and report accurately.</span></li>
      <li>%s<span><strong>Dual-system licensing input</strong> covering the bag itself and the polybag and carton that carry it.</span></li>
      <li>%s<span><strong>REACH SVHC statements</strong> for fabric, webbing, lining, thread and hardware.</span></li>
      <li>%s<span><strong>PFAS-free finishes</strong> as standard, for buyers already screening water-repellent treatments.</span></li>
      <li>%s<span><strong>Food-contact linings</strong> available for grocery and cooler programmes where the bag meets food directly.</span></li>
      <li>%s<span><strong>Test reports and declarations</strong> issued as PDFs your compliance team can file without chasing us.</span></li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Logistics</span><h2>Getting the Goods to Germany</h2></div>
    <div class="steps">
      <div class="step reveal"><h3>Sea freight</h3><p>Ningbo or Shenzhen to Hamburg and Bremerhaven, then onward by truck or rail to your warehouse. Typically 30&ndash;38 days port to door.</p></div>
      <div class="step reveal delayed-1"><h3>Rail</h3><p>China&ndash;Europe corridor services run 18&ndash;25 days into Duisburg and Hamburg, a useful middle option on larger orders.</p></div>
      <div class="step reveal delayed-2"><h3>Air</h3><p>7&ndash;10 days door to door for samples, launch quantities and replenishment when a retail date cannot move.</p></div>
      <div class="step reveal delayed-3"><h3>Terms</h3><p>We quote DDP to your German warehouse, or DAP and FOB if your forwarder handles the import.</p></div>
    </div>
  </div>
</section>
""" % (CHECK, CHECK, CHECK, CHECK, CHECK, CHECK),
        faq_head=("Common questions", "German Programme Questions"),
        faq=[
            ("Can you deliver DDP to a German warehouse?",
             "Yes. We quote DDP to your warehouse address in Germany, covering freight, duty and import clearance so you receive one landed price in EUR or USD."),
            ("What do you need from us for LUCID reporting?",
             "Your registration number if you already have one, and the packaging you place on the market. We supply the per-SKU material types, unit weights and outer packaging weights that the report is built from."),
            ("How do you handle German quality expectations?",
             "Against an approved golden sample, with AQL inspection before shipment and a photographic report. If you nominate a third-party inspector such as SGS or Intertek we will host the inspection at our factory."),
        ],
        cta=("Germany", "Start a German Retail Programme",
             "Send your spec and target landed cost. We will reply within one business day with costing, MOQ and a delivery window to your German warehouse.",
             "Request a Quote", "quote.html"),
    ),
    # ---------------------------------------------------------------- France
    dict(
        slug="markets/france.html",
        crumb="France",
        parent="Europe & the EU",
        title="Custom Bags for French Brands: AGEC & Triman | Verlora Bags",
        desc="Custom bag manufacturing for French brands: AGEC and Triman support, French-language labelling guidance, EPR data and DDP delivery into Le Havre.",
        image="assets/img/solution-beauty.webp",
        main="""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">France</span>
    <h1>Custom Bag Manufacturing for Brands in France</h1>
    <p class="lead">French programmes combine a design-led brief with strict consumer information rules. We build the bag and help you get the labelling right.</p>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="split-copy reveal">
      <span class="eyebrow">Why French buyers work with us</span>
      <h2>Design Detail Without Losing the Schedule</h2>
      <p class="lead">Boutique and cosmetic labels in France care how the bag feels and folds. We sample until the shape is right, then protect the dates.</p>
      <ul>
        <li>Hardware, lining and interlining sourced to your price position</li>
        <li>Coating, embossing and foil options sampled before bulk</li>
        <li>Print proofs matched against Pantone references</li>
        <li>Small accessory runs combined within one style across colourways</li>
      </ul>
      <a class="btn btn-primary" href="../quote.html">Request a French Programme Quote</a>
    </div>
    <div class="split-media reveal delayed-1"><img src="../assets/img/solution-beauty.webp" alt="Custom cosmetic and boutique bags made for French brands" width="560" height="460" loading="lazy"></div>
  </div>
</section>
<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Compliance</span><h2>AGEC, Triman and French Labelling</h2><p class="lead">France ties packaging, sorting information and consumer language together under one law.</p></div>
    <ul class="check-list reveal">
      <li>%s<span><strong>AGEC and EPR data</strong> &mdash; material composition and weights per SKU for your scheme reporting.</span></li>
      <li>%s<span><strong>Triman mark placement</strong> built into the print layout when you supply the sorting instruction that applies.</span></li>
      <li>%s<span><strong>French-language consumer information</strong> &mdash; we reserve space in the artwork so your French text fits without redesign.</span></li>
      <li>%s<span><strong>Material marking</strong> for the fabric and trim so sorting instructions match the actual construction.</span></li>
      <li>%s<span><strong>REACH and OEKO-TEX documentation</strong> for the materials in your bill of materials.</span></li>
      <li>%s<span><strong>Recycled content options</strong> with GRS certificates where you are making a recycled claim.</span></li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Logistics</span><h2>Getting the Goods to France</h2></div>
    <div class="steps">
      <div class="step reveal"><h3>Sea freight</h3><p>Ningbo or Shenzhen into Le Havre, Fos-sur-Mer and Marseille, then onward by road. Typically 30&ndash;38 days port to door.</p></div>
      <div class="step reveal delayed-1"><h3>Rail</h3><p>Corridor services terminate in Duisburg and Lyon, both practical for onward French distribution on larger runs.</p></div>
      <div class="step reveal delayed-2"><h3>Air</h3><p>7&ndash;10 days door to door via Paris CDG for launch stock and high-value accessories.</p></div>
      <div class="step reveal delayed-3"><h3>Terms</h3><p>DDP to your French warehouse, or DAP and FOB if you prefer your own customs broker.</p></div>
    </div>
  </div>
</section>
""" % (CHECK, CHECK, CHECK, CHECK, CHECK, CHECK),
        faq_head=("Common questions", "French Programme Questions"),
        faq=[
            ("Do you handle the Triman logo?",
             "Yes. Send us the mark and the sorting instruction that applies to your bag and we will place it in the artwork, then show it on the print proof you approve before production starts."),
            ("Does the bag need French text?",
             "Consumer-facing information on packaging sold in France is generally expected in French. We reserve artwork space for your French wording and can lay it out with the rest of the print so nothing has to be redesigned later."),
            ("What are your MOQs for a boutique programme?",
             "300 pcs per style for most constructions, with mixed colourways counting toward the same style. Selected promotional lines start at 100 pcs."),
        ],
        cta=("France", "Start a French Programme",
             "Send your brief, artwork direction and target cost. We will come back within one business day with a sampled route to market.",
             "Request a Quote", "quote.html"),
    ),
    # ----------------------------------------------------------- Netherlands
    dict(
        slug="markets/netherlands.html",
        crumb="Netherlands",
        parent="Europe & the EU",
        title="Custom Bags for Dutch Brands: Rotterdam DDP | Verlora Bags",
        desc="Custom tote and reusable bag production for Dutch brands, with Afvalfonds packaging data, short sea transit via Rotterdam and DDP delivery to your warehouse.",
        image="assets/img/solution-grocery.webp",
        main="""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Netherlands</span>
    <h1>Custom Bag Manufacturing for Brands in the Netherlands</h1>
    <p class="lead">Dutch buyers tend to move first on recycled content and material honesty. We build reusable bags that stand up to a circularity claim rather than just carrying the logo.</p>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="split-copy reveal">
      <span class="eyebrow">Why Dutch buyers work with us</span>
      <h2>Circular Claims That Hold Up</h2>
      <p class="lead">A recycled claim is only worth what the documentation behind it proves. We supply the certificates, not just the wording.</p>
      <ul>
        <li>rPET, recycled PP and recycled cotton options with GRS certificates</li>
        <li>Mono-material constructions that are easier to recycle</li>
        <li>Removable trim so hardware can be separated at end of life</li>
        <li>Reinforced base and handles for grocery loads and repeat use</li>
      </ul>
      <a class="btn btn-primary" href="../quote.html">Request a Dutch Programme Quote</a>
    </div>
    <div class="split-media reveal delayed-1"><img src="../assets/img/solution-grocery.webp" alt="Reusable grocery bags produced for Dutch retail programmes" width="560" height="460" loading="lazy"></div>
  </div>
</section>
<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Compliance</span><h2>Packaging Fees and Material Data</h2><p class="lead">The Dutch system is administered through a single packaging fund, so the data you need is specific and predictable.</p></div>
    <ul class="check-list reveal">
      <li>%s<span><strong>Afvalfonds reporting data</strong> &mdash; material types, unit weights and outer packaging weights per SKU.</span></li>
      <li>%s<span><strong>Recycled content evidence</strong> with GRS transaction certificates for fibre and non-woven inputs.</span></li>
      <li>%s<span><strong>Material marking</strong> so sorting information matches the construction of the bag.</span></li>
      <li>%s<span><strong>REACH SVHC statements</strong> for fabric, webbing, lining, thread and hardware.</span></li>
      <li>%s<span><strong>PFAS-free finishes</strong> as the default on water-repellent treatments.</span></li>
      <li>%s<span><strong>Durability test data</strong> covering handle pull and seam strength, useful when reuse is part of the claim.</span></li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Logistics</span><h2>Getting the Goods to the Netherlands</h2></div>
    <div class="steps">
      <div class="step reveal"><h3>Sea freight</h3><p>Ningbo or Shenzhen into Rotterdam, the shortest onward leg in the EU. Typically 28&ndash;35 days port to door.</p></div>
      <div class="step reveal delayed-1"><h3>Short sea and rail</h3><p>Rotterdam also takes feeders and rail from the corridor, which helps when you split delivery across Benelux.</p></div>
      <div class="step reveal delayed-2"><h3>Air</h3><p>7&ndash;9 days door to door via Schiphol for launch and replenishment quantities.</p></div>
      <div class="step reveal delayed-3"><h3>Terms</h3><p>DDP to your Dutch warehouse, or DAP and FOB if your forwarder clears the import.</p></div>
    </div>
  </div>
</section>
""" % (CHECK, CHECK, CHECK, CHECK, CHECK, CHECK),
        faq_head=("Common questions", "Dutch Programme Questions"),
        faq=[
            ("Can you supply recycled content with certificates?",
             "Yes. Recycled fibre and non-woven options are available with GRS transaction certificates, and we will state the achievable percentage at your target price before sampling starts."),
            ("What is the transit time to Rotterdam?",
             "Sea freight typically runs 28&ndash;35 days door to door into the Netherlands, air freight 7&ndash;9 days. We confirm the window for your specific sailing when we quote."),
            ("Do you deliver DDP in the Netherlands?",
             "Yes, DDP to your warehouse is our usual term for Dutch programmes, with freight, duty and import clearance included in one landed price."),
        ],
        cta=("Netherlands", "Start a Dutch Programme",
             "Send your spec and target landed cost. We will reply within one business day with costing and the recycled content options available.",
             "Request a Quote", "quote.html"),
    ),
    # ---------------------------------------------------------------- Poland
    dict(
        slug="markets/poland.html",
        crumb="Poland",
        parent="Europe & the EU",
        title="Custom Bags for Polish Brands: EPR & BDO | Verlora Bags",
        desc="Custom bag manufacturing for Polish brands and importers: BDO registration data, EPR support, Gdansk sea routing and MOQ from 300 pcs per style.",
        image="assets/img/solution-promo.webp",
        main="""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Poland</span>
    <h1>Custom Bag Manufacturing for Brands in Poland</h1>
    <p class="lead">Poland is one of the fastest-moving retail markets in the EU, and buyers there expect European quality at a sharper cost. That is exactly the brief we build to.</p>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="split-copy reveal">
      <span class="eyebrow">Why Polish buyers work with us</span>
      <h2>Cost Engineered, Not Value Engineered</h2>
      <p class="lead">We take cost out of the construction deliberately, and tell you what each change does to the bag, rather than quietly downgrading it.</p>
      <ul>
        <li>Substrate selection matched to your retail price point</li>
        <li>Print method chosen for run length, not habit</li>
        <li>Carton and polybag optimisation to cut freight cost per unit</li>
        <li>Volume breaks quoted at 300, 1,000 and 5,000 pcs</li>
      </ul>
      <a class="btn btn-primary" href="../quote.html">Request a Polish Programme Quote</a>
    </div>
    <div class="split-media reveal delayed-1"><img src="../assets/img/solution-promo.webp" alt="Promotional and retail bags produced for Polish brands" width="560" height="460" loading="lazy"></div>
  </div>
</section>
<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Compliance</span><h2>BDO Registration and EPR</h2><p class="lead">Poland registers producers centrally, so the registration step comes before the shipment, not after.</p></div>
    <ul class="check-list reveal">
      <li>%s<span><strong>BDO reporting data</strong> &mdash; packaging mass by material type per SKU and per shipment.</span></li>
      <li>%s<span><strong>EPR documentation</strong> covering both the bag and the packaging that protects it.</span></li>
      <li>%s<span><strong>Material marking</strong> so the declared composition matches the physical product.</span></li>
      <li>%s<span><strong>REACH SVHC statements</strong> for fabric, webbing, lining, thread and hardware.</span></li>
      <li>%s<span><strong>Test reports</strong> for handle pull, seam strength and colour fastness on request.</span></li>
      <li>%s<span><strong>Recycled content options</strong> with GRS certificates where the programme calls for them.</span></li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Logistics</span><h2>Getting the Goods to Poland</h2></div>
    <div class="steps">
      <div class="step reveal"><h3>Sea freight</h3><p>Ningbo or Shenzhen into Gda&#324;sk and Gdynia, with good onward road links across central Poland. Typically 30&ndash;38 days port to door.</p></div>
      <div class="step reveal delayed-1"><h3>Rail</h3><p>Corridor services via Ma&#322;aszewicze run 16&ndash;22 days, often the fastest overland route into Poland.</p></div>
      <div class="step reveal delayed-2"><h3>Air</h3><p>7&ndash;10 days door to door via Warsaw for launch quantities and promotional deadlines.</p></div>
      <div class="step reveal delayed-3"><h3>Terms</h3><p>DDP to your Polish warehouse, or DAP and FOB if you clear the import yourself.</p></div>
    </div>
  </div>
</section>
""" % (CHECK, CHECK, CHECK, CHECK, CHECK, CHECK),
        faq_head=("Common questions", "Polish Programme Questions"),
        faq=[
            ("Do we need a BDO entry before importing?",
             "Entities that introduce packaging to the Polish market are required to register in the BDO system. We supply the packaging mass and material data your registration and reporting is built on."),
            ("What is the transit time to Gdansk?",
             "Sea freight typically runs 30&ndash;38 days door to door into Poland, and rail via Ma&#322;aszewicze 16&ndash;22 days. We confirm the schedule when we quote."),
            ("Can you hit a lower unit price than European suppliers?",
             "Usually yes on labour-intensive constructions, which is most sewn bags. Where a European converter is genuinely competitive we will say so rather than quote a price we cannot hold."),
        ],
        cta=("Poland", "Start a Polish Programme",
             "Send your spec and target unit cost. We will reply within one business day with volume breaks at 300, 1,000 and 5,000 pcs.",
             "Request a Quote", "quote.html"),
    ),
    # --------------------------------------------------------------- Czechia
    dict(
        slug="markets/czechia.html",
        crumb="Czechia",
        parent="Europe & the EU",
        title="Custom Bags for Czech Brands: EKO-KOM & EPR | Verlora Bags",
        desc="Custom bag production for Czech brands with EKO-KOM compliance data, Prague and Brno delivery, and promotional and retail programmes from 300 pcs.",
        image="assets/img/solution-gifts.webp",
        main="""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Czechia</span>
    <h1>Custom Bag Manufacturing for Brands in Czechia</h1>
    <p class="lead">Czech buyers sit close to the German market and expect a comparable standard of documentation. We build promotional, retail and gift bags to that bar.</p>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="split-copy reveal">
      <span class="eyebrow">Why Czech buyers work with us</span>
      <h2>Gift and Promotional Runs That Look Considered</h2>
      <p class="lead">A corporate gift bag is judged in the hand. We sample the finish, not just the print.</p>
      <ul>
        <li>Felt, jute, canvas and paper options for gift and seasonal programmes</li>
        <li>Foil, emboss and deboss finishes sampled before bulk</li>
        <li>Short seasonal windows planned backwards from your launch date</li>
        <li>Mixed-item gift sets packed and labelled to your instruction</li>
      </ul>
      <a class="btn btn-primary" href="../quote.html">Request a Czech Programme Quote</a>
    </div>
    <div class="split-media reveal delayed-1"><img src="../assets/img/solution-gifts.webp" alt="Gift and promotional bags produced for Czech brands" width="560" height="460" loading="lazy"></div>
  </div>
</section>
<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Compliance</span><h2>EKO-KOM and Packaging Reporting</h2><p class="lead">Czech packaging compliance runs through a single authorised scheme, which keeps the data requirement straightforward.</p></div>
    <ul class="check-list reveal">
      <li>%s<span><strong>EKO-KOM reporting data</strong> &mdash; material type and weight for each packaging component.</span></li>
      <li>%s<span><strong>Separated product and packaging weights</strong> so the bag and its outer packaging are reported correctly.</span></li>
      <li>%s<span><strong>Material marking</strong> matching the declared composition of the bag.</span></li>
      <li>%s<span><strong>REACH SVHC statements</strong> for fabric, webbing, lining, thread and hardware.</span></li>
      <li>%s<span><strong>OEKO-TEX documentation</strong> where textile safety is part of your tender requirement.</span></li>
      <li>%s<span><strong>Recycled content evidence</strong> with GRS certificates on request.</span></li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Logistics</span><h2>Getting the Goods to Czechia</h2></div>
    <div class="steps">
      <div class="step reveal"><h3>Sea and rail</h3><p>Most Czech programmes route through Hamburg or Gda&#324;sk, or arrive overland by rail via Ma&#322;aszewicze. Typically 28&ndash;36 days door to door.</p></div>
      <div class="step reveal delayed-1"><h3>Road</h3><p>From Hamburg or Gda&#324;sk, Prague and Brno are 6&ndash;10 hours by truck, which keeps the onward leg predictable.</p></div>
      <div class="step reveal delayed-2"><h3>Air</h3><p>7&ndash;10 days door to door via Prague for seasonal deadlines that cannot move.</p></div>
      <div class="step reveal delayed-3"><h3>Terms</h3><p>DDP to your Czech warehouse, or DAP and FOB if you prefer your own forwarder.</p></div>
    </div>
  </div>
</section>
""" % (CHECK, CHECK, CHECK, CHECK, CHECK, CHECK),
        faq_head=("Common questions", "Czech Programme Questions"),
        faq=[
            ("Can you meet a Christmas promotional deadline?",
             "Yes, if the artwork is approved by early September. Production runs 15&ndash;25 days after sample approval and sea transit adds roughly 30 days, so we plan the calendar backwards from your in-store date."),
            ("Do you supply EKO-KOM reporting data?",
             "We provide the material type and weight for each packaging component you place on the market, which is the input your EKO-KOM reporting is built from."),
            ("Can you pack mixed gift sets?",
             "Yes. We can assemble mixed-item sets, apply your labels and carton them to your instruction, provided the components are all produced within the same order."),
        ],
        cta=("Czechia", "Start a Czech Programme",
             "Send your brief and in-store date. We will reply within one business day with a schedule that works backwards from your launch.",
             "Request a Quote", "quote.html"),
    ),
    # --------------------------------------------------------------- Romania
    dict(
        slug="markets/romania.html",
        crumb="Romania",
        parent="Europe & the EU",
        title="Custom Bags for Romanian Brands: EPR & DDP | Verlora Bags",
        desc="Custom bag manufacturing for Romanian brands: EPR obligations, Constanta sea freight, DDP delivery and cost-engineered programmes from 300 pcs per style.",
        image="assets/img/solution-corporate.webp",
        main="""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Romania</span>
    <h1>Custom Bag Manufacturing for Brands in Romania</h1>
    <p class="lead">Romania combines a fast-growing retail sector with sharp price sensitivity. We engineer the bag to your shelf price and keep the compliance paperwork in order.</p>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="split-copy reveal">
      <span class="eyebrow">Why Romanian buyers work with us</span>
      <h2>Sharp Pricing Without a Weak Bag</h2>
      <p class="lead">Cutting cost by making a bag worse is a false saving. We take cost out of the construction and tell you where it came from.</p>
      <ul>
        <li>Substrate and gsm chosen against your target shelf price</li>
        <li>Print method selected for the run length you actually need</li>
        <li>Freight optimised through Constan&#539;a and the Black Sea corridor</li>
        <li>Volume breaks from 300 pcs upward, with mixed colourways counted together</li>
      </ul>
      <a class="btn btn-primary" href="../quote.html">Request a Romanian Programme Quote</a>
    </div>
    <div class="split-media reveal delayed-1"><img src="../assets/img/solution-corporate.webp" alt="Custom corporate and retail bags produced for Romanian brands" width="560" height="460" loading="lazy"></div>
  </div>
</section>
<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Compliance</span><h2>EPR and Packaging Reporting in Romania</h2><p class="lead">Romania applies national producer responsibility to packaging placed on the market, alongside the EU framework.</p></div>
    <ul class="check-list reveal">
      <li>%s<span><strong>EPR reporting data</strong> &mdash; packaging mass by material type for each SKU you place on the market.</span></li>
      <li>%s<span><strong>Product and packaging weights</strong> reported separately so the figures are defensible.</span></li>
      <li>%s<span><strong>Material marking</strong> consistent with the declared composition.</span></li>
      <li>%s<span><strong>REACH SVHC statements</strong> for fabric, webbing, lining, thread and hardware.</span></li>
      <li>%s<span><strong>Recycled content options</strong> with GRS certificates where a recycled claim is made.</span></li>
      <li>%s<span><strong>Test reports</strong> for handle pull, seam strength and colour fastness on request.</span></li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Logistics</span><h2>Getting the Goods to Romania</h2></div>
    <div class="steps">
      <div class="step reveal"><h3>Sea freight</h3><p>Ningbo or Shenzhen direct into Constan&#539;a on the Black Sea, which avoids the congestion surcharges of northern Europe. Typically 28&ndash;35 days port to door.</p></div>
      <div class="step reveal delayed-1"><h3>Onward road</h3><p>Constan&#539;a to Bucharest is under four hours by truck, and the national network reaches most of the country within a day.</p></div>
      <div class="step reveal delayed-2"><h3>Air</h3><p>7&ndash;10 days door to door via Bucharest for launch quantities and replenishment.</p></div>
      <div class="step reveal delayed-3"><h3>Terms</h3><p>DDP to your Romanian warehouse, or DAP and FOB if your forwarder clears the import.</p></div>
    </div>
  </div>
</section>
""" % (CHECK, CHECK, CHECK, CHECK, CHECK, CHECK),
        faq_head=("Common questions", "Romanian Programme Questions"),
        faq=[
            ("Do you ship directly to Constanta?",
             "Yes. We route Black Sea services into Constan&#539;a, which is often faster and less congested than transhipping through northern European ports. Transit is typically 28&ndash;35 days door to door."),
            ("What do you need from us for EPR reporting?",
             "The packaging you place on the market and your registration details. We supply packaging mass by material type per SKU, with product and outer packaging weights separated."),
            ("Can you produce to a very tight unit cost?",
             "Yes, at a defined quality level. We will show you which specification changes reduce cost and what each one does to handle strength, print quality and lifespan, so the trade-off is your decision."),
        ],
        cta=("Romania", "Start a Romanian Programme",
             "Send your target shelf price and volume. We will reply within one business day with a construction that lands on it.",
             "Request a Quote", "quote.html"),
    ),
]
