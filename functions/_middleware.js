/**
 * Verlorabags edge request filter (Cloudflare Pages middleware).
 *
 * Cloudflare Pages picks up /functions/_middleware.js automatically and runs it
 * for every request, including the *.pages.dev preview domain. It needs no WAF
 * and no paid plan, so it works on the free tier.
 *
 * Goal: flag visitors whose browser language is Chinese while their IP sits
 * outside the home country - the pattern behind overseas-based copycats and
 * scrapers that browse with Chinese-language chrome from rented servers.
 *
 * Two modes:
 *   "observe" - never blocks. Adds an X-Ver-Filter response header and writes a
 *               JSON line to the Pages real-time log so you can measure the
 *               traffic first (wrangler pages deployment tail).
 *   "block"   - returns 403 for matching page views.
 *
 * Only page navigations (GET/HEAD + Accept: text/html) are evaluated, so the
 * lead endpoint, CSS, JS and images keep working for everyone. Search engine
 * crawlers are always allowed.
 */

const MODE = "observe"; // "observe" | "block"

// "primary" = only the browser's first/UI language counts (fewest false positives).
// "any"     = flag as soon as zh appears anywhere in Accept-Language (catches
//             English-UI browsers that still prefer Chinese content).
const LANGUAGE_MATCH = "primary";

const LANGUAGE_PREFIXES = ["zh"]; // matches zh, zh-CN, zh-TW, zh-Hans, ...
const HOME_COUNTRIES = ["CN"]; // visitors in these countries are never flagged
const EXEMPT_PATHS = [/^\/api\//i, /^\/\.well-known\//i];

const SEARCH_BOT_RE =
  /(googlebot|google-inspectiontool|bingbot|msnbot|yandexbot|duckduckbot|baiduspider|applebot|slurp|petalbot|sogou)/i;

function parseLanguages(header) {
  return String(header || "")
    .split(",")
    .map(function (part, index) {
      const pieces = part.trim().split(";");
      const tag = pieces[0].trim().toLowerCase();
      let q = 1;
      for (let i = 1; i < pieces.length; i++) {
        const m = /^\s*q\s*=\s*([0-9.]+)\s*$/i.exec(pieces[i]);
        if (m) q = parseFloat(m[1]);
      }
      return { tag: tag, q: isNaN(q) ? 1 : q, index: index };
    })
    .filter(function (item) {
      return item.tag;
    })
    .sort(function (a, b) {
      return b.q - a.q || a.index - b.index;
    });
}

function isChineseTag(tag) {
  return LANGUAGE_PREFIXES.some(function (prefix) {
    return tag === prefix || tag.indexOf(prefix + "-") === 0;
  });
}

function isChineseLanguage(header) {
  const languages = parseLanguages(header);
  if (!languages.length) return false;
  if (LANGUAGE_MATCH === "primary") return isChineseTag(languages[0].tag);
  return languages.some(function (item) {
    return isChineseTag(item.tag);
  });
}

function isPageView(request) {
  if (request.method !== "GET" && request.method !== "HEAD") return false;
  const accept = request.headers.get("Accept") || "";
  const dest = request.headers.get("Sec-Fetch-Dest") || "";
  return accept.indexOf("text/html") !== -1 || dest === "document";
}

function classify(request) {
  const url = new URL(request.url);
  for (let i = 0; i < EXEMPT_PATHS.length; i++) {
    if (EXEMPT_PATHS[i].test(url.pathname)) return { flag: false, reason: "exempt-path" };
  }
  if (!isPageView(request)) return { flag: false, reason: "not-a-page-view" };
  if (SEARCH_BOT_RE.test(request.headers.get("User-Agent") || "")) {
    return { flag: false, reason: "search-bot" };
  }

  const language = request.headers.get("Accept-Language") || "";
  const country =
    (request.cf && request.cf.country) || request.headers.get("CF-IPCountry") || "";

  if (!isChineseLanguage(language)) return { flag: false, reason: "other-language" };
  if (!country) return { flag: false, reason: "unknown-country" };
  if (HOME_COUNTRIES.indexOf(country) !== -1) return { flag: false, reason: "home-country" };

  return {
    flag: true,
    reason: "zh-language-overseas",
    country: country,
    language: language.slice(0, 60),
  };
}

export async function onRequest(context) {
  const { request, next } = context;

  let verdict;
  try {
    verdict = classify(request);
  } catch (err) {
    return next();
  }

  if (!verdict.flag) return next();

  const info = {
    event: "ver-filter",
    mode: MODE,
    reason: verdict.reason,
    country: verdict.country,
    language: verdict.language,
    path: new URL(request.url).pathname,
    referer: request.headers.get("Referer") || "",
    ip: request.headers.get("CF-Connecting-IP") || "",
    userAgent: (request.headers.get("User-Agent") || "").slice(0, 160),
    at: new Date().toISOString(),
  };
  console.log(JSON.stringify(info));

  if (MODE !== "block") {
    const response = await next();
    const patched = new Response(response.body, response);
    patched.headers.set("X-Ver-Filter", "observe:" + verdict.reason);
    return patched;
  }

  return new Response(
    "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">" +
      "<meta name=\"robots\" content=\"noindex\"><title>403 Forbidden</title>" +
      "<style>body{font:16px/1.6 Georgia,serif;margin:14vh auto;max-width:34rem;padding:0 1.5rem;" +
      "color:#3c3226;background:#faf7f2}h1{font-size:1.5rem}</style></head><body>" +
      "<h1>Access denied</h1><p>This website is not available for your current browser " +
      "language and location combination.</p>" +
      "<p>If you are a genuine buyer, please email " +
      "<a href=\"mailto:evan.funkytek@gmail.com\">evan.funkytek@gmail.com</a> or reach us on " +
      "<a href=\"https://wa.me/8613798275895\">WhatsApp</a>.</p></body></html>",
    {
      status: 403,
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Cache-Control": "no-store",
        "X-Robots-Tag": "noindex",
      },
    }
  );
}
