# -*- coding: utf-8 -*-
"""Stylesheet assembly and page chrome (header / footer)."""
import re
from common import (rp, read, write, esc, CSS_VERSION, LOGO_VERSION,
                    BRAND, ADDRESS, PHONE, EMAIL, HOURS, WA)

TOKENS = """/* ============================================================
   Verlora Bags - design tokens
   ============================================================ */
:root{
  --green:#315522;--green-hover:#26441a;--accent:#dca63b;
  --ink:#111812;--muted:#667065;--muted-light:#7b8278;
  --sand:#f6f1e9;--line:#e7e5de;--white:#fff;
  --radius:12px;--container:1380px;
  --font-head:Georgia,'Times New Roman',serif;
  --font-body:Inter,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
  /* legacy scale kept for backwards compatibility with older class names */
  --ink-950:#111812;--ink-900:#1b241c;--ink-800:#2b332c;--ink-700:#3f493e;
  --camel-200:#e6ecdf;--camel-300:#cbd8c0;--camel-400:#4c7439;--camel-500:#315522;
  --camel-600:#315522;--camel-700:#26441a;
  --cream-50:#ffffff;--cream-100:#f7f6f2;--cream-200:#f1ece3;
  --shadow-sm:0 2px 12px rgba(17,24,18,.06);
  --shadow-md:0 16px 38px rgba(17,24,18,.12);
  --shadow:0 16px 38px rgba(17,24,18,.12);
  --shadow-lg:0 30px 60px rgba(17,24,18,.14);
}
"""

OVERRIDES = """
/* ============================================================
   v2.0 - navigation, layout and components used by the live markup
   ============================================================ */
body{background:#fff}
.container{max-width:var(--container)}

/* ---------- header ---------- */
.header-inner{height:80px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.site-header{position:sticky;top:0;z-index:2000;background:rgba(255,255,255,.96);-webkit-backdrop-filter:blur(15px);backdrop-filter:blur(15px);border-bottom:1px solid var(--line)}
.site-header.is-scrolled{box-shadow:var(--shadow-sm)}
.brand{display:flex;align-items:center;flex:none}
.brand img{height:42px;width:auto}
.site-nav{display:flex;align-items:center;gap:30px}
.site-nav>.nav-item{position:relative;padding:28px 0;display:flex;align-items:center;font-size:14px;font-weight:650;color:var(--ink);cursor:pointer}
.site-nav>.nav-item::after{content:"";position:absolute;left:0;right:100%;bottom:22px;height:2px;background:var(--green);transition:right .2s ease}
.site-nav>.nav-item:hover::after{right:0}
.site-nav>.nav-item::before{content:"";position:absolute;top:100%;left:-20px;right:-20px;height:20px;z-index:10}
.nav-panel{position:absolute;top:100%;left:50%;transform:translateX(-50%) translateY(10px);background:#fff;border:1px solid var(--line);border-radius:12px;box-shadow:0 30px 60px rgba(0,0,0,.12);opacity:0;visibility:hidden;pointer-events:none;transition:all .2s;z-index:2100;padding:12px}
.site-nav>.nav-item:hover .nav-panel{opacity:1;visibility:visible;pointer-events:auto;transform:translateX(-50%) translateY(0)}
.mega-menu{width:600px;display:grid;grid-template-columns:repeat(2,1fr);gap:4px}
.slim-dropdown{width:230px;display:flex;flex-direction:column;gap:2px}
.menu-link{display:flex;align-items:center;gap:12px;padding:10px 14px;border-radius:8px;font-size:13.5px;font-weight:700;color:#3f493e}
.menu-link:hover{background:#f0f4ee;color:var(--green)}
.menu-link svg{width:20px!important;height:20px!important;flex:none;stroke-width:2}
.mega-menu .menu-all{grid-column:1/-1;justify-content:center;color:var(--green);border-top:1px solid var(--line);border-radius:0 0 8px 8px;margin-top:6px;padding-top:12px}
.site-nav>.btn{margin-left:10px;flex:none}
.nav-toggle{display:none;flex-direction:column;justify-content:center;gap:5px;background:none;border:0;cursor:pointer;padding:10px}
.nav-toggle span{width:24px;height:2px;background:var(--ink);border-radius:2px;transition:transform .3s,opacity .3s}
.nav-toggle[aria-expanded="true"] span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.nav-toggle[aria-expanded="true"] span:nth-child(2){opacity:0}
.nav-toggle[aria-expanded="true"] span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}

/* ---------- buttons ---------- */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 30px;border-radius:999px;font-weight:700;font-size:.95rem;line-height:1;letter-spacing:.02em;border:1px solid transparent;cursor:pointer;text-align:center;transition:transform .2s,box-shadow .2s,background .2s,color .2s}
.btn:hover{transform:translateY(-2px)}
.btn-primary{background:var(--green);color:#fff;box-shadow:0 10px 24px rgba(49,85,34,.26)}
.btn-primary:hover{background:var(--green-hover);color:#fff}
.btn-camel{background:var(--green);color:#fff}
.btn-camel:hover{color:#fff}
.btn-whatsapp{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:14px 30px;border-radius:999px;background:#25d366;color:#fff;font-weight:800;font-size:.88rem;letter-spacing:.04em;text-transform:uppercase;transition:transform .2s,box-shadow .2s}
.btn-whatsapp:hover{color:#fff;transform:translateY(-2px);box-shadow:0 12px 26px rgba(37,211,102,.35)}
.btn-lg{padding:16px 36px;font-size:1rem}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-top:26px}

/* ---------- home hero ---------- */
.hero-section{padding:88px 0;background:#fbf9f5}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:60px;align-items:center;padding:0}
.hero-copy h1{font-size:clamp(2.2rem,4.4vw,3.4rem);margin:14px 0 20px}
.hero-point{display:flex;align-items:center;gap:10px;font-weight:600;color:var(--ink-700);font-size:.95rem}
.hero-visual-container{position:relative;display:grid;grid-template-columns:1fr 220px;gap:20px;align-items:start}
.hero-visual img{width:100%;height:auto;border-radius:12px;box-shadow:var(--shadow)}
.hero-sidebar{display:flex;flex-direction:column;gap:12px}
.sidebar-item{background:#fff;padding:15px;border-radius:10px;border:1px solid var(--line);display:flex;align-items:center;gap:12px;transition:all .2s}
.sidebar-item:hover{transform:translateX(5px);box-shadow:var(--shadow-sm)}
.sidebar-icon{width:36px;height:36px;border:1px solid #cbd7c5;border-radius:50%;color:var(--green);font-size:9px;font-weight:900;display:flex;align-items:center;justify-content:center;flex:none}
.sidebar-copy{display:flex;flex-direction:column;line-height:1.2}
.sidebar-copy b{font-size:13px;color:var(--ink)}
.sidebar-copy span{font-size:11px;color:var(--muted)}

/* ---------- cards / catalog ---------- */
.category-card{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;transition:transform .25s,box-shadow .25s;display:flex;flex-direction:column}
.category-card:hover{transform:translateY(-5px);box-shadow:var(--shadow-md)}
.category-media{background:#f1ece3;aspect-ratio:1.15;padding:15px;display:flex;align-items:center;justify-content:center}
.category-media img{width:100%;height:100%;object-fit:contain}
.category-body{padding:22px;display:flex;justify-content:space-between;align-items:center;gap:14px;background:#fff;flex:1}
.category-body h3{font-size:1.05rem;margin:0}
.category-link{font-size:12px;font-weight:800;color:var(--green);text-transform:uppercase;white-space:nowrap}
.p-item{display:flex}
.tabs{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:40px}
.cat-chip{display:inline-block;font-size:.72rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--green);background:var(--cream-100);border:1px solid var(--line);border-radius:999px;padding:5px 12px}
.empty-state{display:none;text-align:center;color:var(--muted);padding:40px 0}
.empty-state.show{display:block}

/* ---------- product detail ---------- */
.product-detail{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:start}
.detail-media{background:linear-gradient(165deg,var(--cream-100),var(--cream-200));border:1px solid var(--line);border-radius:20px;padding:24px}
.detail-media img{width:100%;height:auto;object-fit:contain;border-radius:12px}
.detail-copy h1{font-size:clamp(1.9rem,3.4vw,2.7rem);margin:10px 0 14px}
.detail-copy .lead{margin-bottom:10px}
.product-facts{display:grid;gap:2px;background:var(--line);border:1px solid var(--line);border-radius:14px;overflow:hidden;margin:24px 0}
.product-fact-row{display:grid;grid-template-columns:24px 92px 1fr;gap:12px;align-items:center;background:#fff;padding:13px 16px}
.product-fact-row svg{width:20px;height:20px;stroke:var(--green);flex:none}
.product-fact-row dt{color:var(--muted);font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;font-weight:700}
.product-fact-row dd{color:var(--ink);font-weight:600;font-size:.94rem;margin:0}
.tag-list{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}
.tag-list span{display:inline-block;font-size:.7rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--green);background:var(--cream-100);border:1px solid var(--line);border-radius:999px;padding:6px 14px}
.attr-grid{margin-top:8px}
.check-list li strong{color:var(--ink)}
.xf-pagination,.xf-page-note,.xf-page-btn{display:none}

/* ---------- trust strip, quote strip, footer ---------- */
.trust-strip{background:#fff;padding:26px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.trust-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:20px}
.trust-item{display:flex;align-items:center;gap:12px}
.trust-icon{width:44px;height:44px;border:1px solid #cbd7c5;border-radius:50%;color:var(--green);font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;flex:none;letter-spacing:.02em}
.trust-copy strong{display:block;font-size:14px;color:var(--ink);margin-bottom:2px}
.trust-copy small{display:block;font-size:11px;color:var(--muted-light)}
.quote-strip{background:var(--green);color:#fff;padding:26px 0}
.quote-strip b{font-family:var(--font-head);font-size:1.3rem;display:block}
.quote-strip .btn{background:#fff;color:var(--green)}
.quote-strip .btn:hover{background:#fff;color:var(--green)}
.site-footer{background:#f7f6f2;color:var(--muted);border-top:1px solid var(--line);margin-top:0}
.footer-main{display:grid;grid-template-columns:1.6fr 1fr 1fr 1.3fr;gap:48px;padding:72px 0 52px;background:transparent;border-top:0}
.footer-main h4{color:var(--ink);font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:18px;font-family:var(--font-body)}
.footer-brand img{height:40px;margin-bottom:16px}
.footer-brand p{font-size:.92rem;color:var(--muted);max-width:320px}
.footer-main .footer-links{list-style:none;display:grid;gap:10px}
.footer-main .footer-links a{color:var(--muted);font-size:.94rem}
.footer-main .footer-links a:hover{color:var(--green)}
.footer-main .footer-links li{color:var(--muted);font-size:.94rem}
.footer-bottom{border-top:1px solid var(--line);padding:20px 0;font-size:.82rem;color:var(--muted-light);display:block}
.footer-bottom .container{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap}
.footer-bottom a{color:var(--muted)}

/* ---------- floating WhatsApp ---------- */
.wa-float{position:fixed;bottom:34px;right:34px;width:92px;height:92px;z-index:9000;animation:wa-pulse 2.5s infinite;transition:transform .3s ease}
.wa-float:hover{transform:scale(1.08)}
.wa-float img{width:100%;height:100%;object-fit:contain;filter:drop-shadow(0 10px 25px rgba(0,0,0,.18))}
@keyframes wa-pulse{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-10px) scale(1.03)}}

/* ---------- responsive ---------- */
@media(max-width:1280px){
  .hero-visual-container{grid-template-columns:1fr}
  .hero-sidebar{flex-direction:row;flex-wrap:wrap}
  .hero-sidebar .sidebar-item{flex:1 1 220px}
}
@media(max-width:1100px){
  .nav-toggle{display:flex;margin-left:auto}
  .site-nav{display:none;position:absolute;top:80px;left:0;right:0;background:#fff;border-bottom:1px solid var(--line);box-shadow:var(--shadow-md);flex-direction:column;align-items:stretch;gap:2px;padding:14px 20px 20px;max-height:calc(100vh - 80px);overflow:auto}
  .site-nav.open{display:flex}
  .site-nav>.nav-item{display:block;padding:12px 10px;border-radius:10px;font-size:1rem}
  .site-nav>.nav-item::after,.site-nav>.nav-item::before{display:none}
  .nav-panel{position:static;transform:none;opacity:1;visibility:visible;pointer-events:auto;box-shadow:none;border:0;padding:4px 0 8px 12px;width:auto;display:grid;grid-template-columns:1fr;gap:2px}
  .mega-menu{width:auto}
  .site-nav>.btn{margin:12px 0 0;width:100%}
  .product-detail,.hero-grid{grid-template-columns:1fr}
  .trust-grid{grid-template-columns:repeat(3,1fr);gap:30px}
}
@media(max-width:768px){
  .trust-grid{grid-template-columns:repeat(2,1fr)}
  .hero-section{padding:56px 0}
  .wa-float{width:72px;height:72px;bottom:18px;right:18px}
  .footer-main{grid-template-columns:1fr;gap:36px;padding:52px 0 36px}
  .product-fact-row{grid-template-columns:22px 78px 1fr;font-size:.88rem}
}
@media(max-width:520px){
  .trust-grid{grid-template-columns:1fr}
}

/* ---------- inquiry form feedback ---------- */
.hp-field{position:absolute!important;left:-9999px!important;width:1px!important;height:1px!important;overflow:hidden!important}
.form-status{margin-top:18px;padding:16px 18px;border-radius:10px;font-size:.92rem;font-weight:650;line-height:1.55}
.form-status[hidden]{display:none}
.form-status.is-ok{background:#eef5e9;border:1px solid #cfe0c3;color:#2c4a20}
.form-status.is-error{background:#fdf1ee;border:1px solid #f0cfc7;color:#8a2f1e}
.form-status a{color:inherit;text-decoration:underline}
form.is-sending button[type=submit]{opacity:.7;cursor:progress}
"""


def build_css():
    base = read(rp("tools", "base-design-system.css"))
    base = re.sub(r"^:root\{.*?\}\s*", "", base, count=1, flags=re.S)
    header = "/* ============================================================\n   Verlora Bags - recovered component system (base layer)\n   ============================================================ */\n"
    write(rp("assets", "css", "style.css"), TOKENS + header + base + OVERRIDES)


# ---------------------------------------------------------------- templates

NAV_PRODUCTS = [
    ("jute-bags", "Jute Bags", '<rect x="3" y="7" width="18" height="12" rx="2"/><path d="M9 7v-2a3 3 0 0 1 6 0v2"/>'),
    ("canvas-bags", "Canvas Bags", '<path d="M4 7h16l-1 13H5L4 7z"/><path d="M9 7V5a3 3 0 0 1 6 0v2"/>'),
    ("non-woven-bags", "Non-Woven Bags", '<rect x="4" y="7" width="16" height="13" rx="2"/><path d="M9 7V6a3 3 0 0 1 6 0v1"/>'),
    ("woven-pp-bags", "Woven PP Bags", '<path d="M4 6h16v14H4z"/><path d="M4 10h16M4 14h16M9 6v14M15 6v14"/>'),
    ("drawstring-bags", "Drawstring", '<circle cx="12" cy="13" r="8"/><path d="M8 5l4 3 4-3"/>'),
    ("cooler-bags", "Cooler Bags", '<rect x="4" y="6" width="16" height="14" rx="2"/><path d="M12 2l3 2h-6l3-2z"/><path d="M9 11v4M15 11v4"/>'),
    ("mesh-bags", "Mesh Bags", '<path d="M12 2v20M4 6l16 12M20 6L4 18M2 12h20"/>'),
    ("tyvek-bags", "Tyvek &amp; Paper", '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/>'),
    ("felt-bags", "Felt Bags", '<rect x="6" y="9" width="12" height="12" rx="2"/><path d="M12 3v6M8 9c0-3 2-5 4-5s4 2 4 5"/>'),
    ("oxford-bags", "Oxford Bags", '<path d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z"/><path d="M8 12l3 3 5-6"/>'),
    ("paper-bags", "Paper Bags", '<path d="M5 8h14l-1 13H6L5 8z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>'),
    ("backpack", "Backpacks", '<path d="M6 8a6 6 0 0 1 12 0v12H6z"/><path d="M9 20v-6h6v6"/>'),
]


def header(p):
    links = "\n".join(
        '        <a href="{p}products/{slug}.html" class="menu-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor">{icon}</svg> {name}</a>'.format(
            p=p, slug=slug, icon=icon, name=name)
        for slug, name, icon in NAV_PRODUCTS)
    return """<header class="site-header" data-header>
  <div class="container header-inner">
    <a href="{p}index.html" class="brand"><img src="{p}assets/svg/logo.svg?v={lv}" alt="{brand}" height="42"></a>
    <button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav" aria-label="Open navigation"><span></span><span></span><span></span></button>
    <nav class="site-nav" id="site-nav" data-nav>
      <a href="{p}index.html" class="nav-item">Home</a>
      <div class="nav-item">
        Products <svg width="10" height="10" style="margin-left:4px;stroke-width:3" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M6 9l6 6 6-6"/></svg>
        <div class="nav-panel mega-menu">
{links}
          <a href="{p}products.html" class="menu-link menu-all">View all product catalog &rarr;</a>
        </div>
      </div>
      <a href="{p}industries.html" class="nav-item">Solutions</a>
      <a href="{p}factory-tour.html" class="nav-item">Factory</a>
      <div class="nav-item">
        Resources <svg width="10" height="10" style="margin-left:4px;stroke-width:3" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M6 9l6 6 6-6"/></svg>
        <div class="nav-panel slim-dropdown">
          <a href="{p}blog.html" class="menu-link">Buying Guides</a>
          <a href="{p}certifications.html" class="menu-link">Certifications</a>
          <a href="{p}europe.html" class="menu-link">Europe &amp; EU Shipping</a>
          <a href="{p}eu-compliance.html" class="menu-link">EU Packaging Compliance</a>
          <a href="{p}about.html" class="menu-link">About Us</a>
        </div>
      </div>
      <a href="{p}contact.html" class="nav-item">Contact</a>
      <a class="btn btn-primary" href="{p}quote.html">Get a Quote</a>
    </nav>
  </div>
</header>
""".format(p=p, brand=BRAND, lv=LOGO_VERSION, links=links)


def footer(p):
    return """<footer class="site-footer">
  <div class="container footer-main">
    <div class="footer-brand">
      <img src="{p}assets/svg/logo.svg?v={lv}" alt="{brand}" height="40">
      <p>Custom reusable bag manufacturer since 2009. Guangzhou-based OEM/ODM factory supporting brand programmes in 60+ countries.</p>
    </div>
    <div>
      <h4>Products</h4>
      <ul class="footer-links">
        <li><a href="{p}products/jute-bags.html">Jute Bags</a></li>
        <li><a href="{p}products/canvas-bags.html">Canvas Totes</a></li>
        <li><a href="{p}products/non-woven-bags.html">Non-Woven Bags</a></li>
        <li><a href="{p}products/woven-pp-bags.html">Woven PP Bags</a></li>
        <li><a href="{p}products/backpack.html">Backpacks</a></li>
        <li><a href="{p}products.html">All Products</a></li>
      </ul>
    </div>
    <div>
      <h4>Company</h4>
      <ul class="footer-links">
        <li><a href="{p}about.html">About Us</a></li>
        <li><a href="{p}factory-tour.html">Factory Tour</a></li>
        <li><a href="{p}certifications.html">Certifications</a></li>
        <li><a href="{p}europe.html">Europe &amp; EU Shipping</a></li>
        <li><a href="{p}eu-compliance.html">EU Packaging Compliance</a></li>
        <li><a href="{p}industries.html">Industries</a></li>
        <li><a href="{p}blog.html">Buying Guides</a></li>
        <li><a href="{p}contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Get in Touch</h4>
      <ul class="footer-links">
        <li>{address}</li>
        <li><a href="https://wa.me/8613798275895">{phone}</a> (WhatsApp)</li>
        <li><a href="mailto:{email}">{email}</a></li>
        <li>{hours}</li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <span>&copy; <span data-year>2026</span> {brand} Co., Ltd. All rights reserved.</span>
      <span><a href="{p}index.html">Home</a> &middot; <a href="{p}products.html">Products</a> &middot; <a href="{p}quote.html">Quote</a> &middot; <a href="{p}privacy.html">Privacy</a> &middot; <a href="{p}terms.html">Terms</a> &middot; <a href="{p}sitemap.xml">Sitemap</a></span>
    </div>
  </div>
</footer>
<script src="{p}assets/js/main.js"></script>
<a href="{wa}" class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><img src="{p}assets/img/wa-float.png" alt="WhatsApp"></a>
""".format(p=p, brand=BRAND, lv=LOGO_VERSION, address=esc(ADDRESS),
           phone=PHONE, email=EMAIL, hours=HOURS, wa=WA)
