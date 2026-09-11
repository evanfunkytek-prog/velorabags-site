/**
 * Lead intake endpoint for the Verlora Bags inquiry forms.
 *
 * Deployed automatically by Cloudflare Pages (any file under /functions).
 * The front end POSTs JSON to /api/quote and falls back to email if this
 * endpoint is unavailable, so a missing provider never loses a lead.
 *
 * Configure ONE of these environment variables in the Cloudflare Pages
 * dashboard (Settings -> Environment variables) to start receiving leads:
 *
 *   RESEND_API_KEY + LEAD_TO   send the lead by email through Resend
 *   LEAD_WEBHOOK_URL           POST the lead JSON to Zapier / Make / n8n / Slack
 *
 * Optional: LEAD_FROM (verified sender, e.g. "Quotes <quotes@verlorabags.com>").
 * Without a provider the endpoint answers 503 and the browser opens the
 * visitor's email app instead.
 */

const MAX_BODY = 64 * 1024;

function json(status, payload, origin) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
      "Access-Control-Allow-Origin": origin || "*",
      "Access-Control-Allow-Headers": "Content-Type",
    },
  });
}

function escapeHtml(value) {
  return String(value == null ? "" : value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

export async function onRequestOptions(context) {
  const origin = context.request.headers.get("Origin") || "*";
  return new Response(null, {
    status: 204,
    headers: {
      "Access-Control-Allow-Origin": origin,
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    },
  });
}

export async function onRequestPost(context) {
  const { request, env } = context;
  const origin = request.headers.get("Origin");

  let payload;
  try {
    const raw = await request.text();
    if (raw.length > MAX_BODY) return json(413, { error: "Payload too large" }, origin);
    payload = JSON.parse(raw);
  } catch (err) {
    return json(400, { error: "Invalid JSON body" }, origin);
  }

  const fields = payload && typeof payload.fields === "object" && payload.fields ? payload.fields : {};
  const email = String(fields.Email || fields.email || "").trim();
  const message = String(payload.message || "").trim();
  if (!fields.Company && !email) return json(400, { error: "Missing contact details" }, origin);

  const lead = {
    subject: payload.subject || "RFQ from website",
    fields,
    email,
    message,
    page: payload.page || "",
    referrer: payload.referrer || "",
    sentAt: payload.sentAt || new Date().toISOString(),
    country: request.headers.get("CF-IPCountry") || "",
    userAgent: request.headers.get("User-Agent") || "",
  };

  const to = env.LEAD_TO || env.EMAIL || "evan.funkytek@gmail.com";
  const from = env.LEAD_FROM || "Verlora Bags Website <onboarding@resend.dev>";

  try {
    if (env.RESEND_API_KEY) {
      const rows = Object.keys(fields)
        .map((k) => "<tr><td style=\"padding:6px 14px 6px 0;color:#667065\"><b>" +
          escapeHtml(k) + "</b></td><td style=\"padding:6px 0\">" + escapeHtml(fields[k]) + "</td></tr>")
        .join("");
      const html = "<h2 style=\"font-family:Georgia,serif\">" + escapeHtml(lead.subject) + "</h2>" +
        "<table cellpadding=\"0\" cellspacing=\"0\" style=\"font:14px/1.5 Arial,sans-serif\">" + rows + "</table>" +
        "<p style=\"font:12px/1.6 Arial,sans-serif;color:#667065\">Page: " + escapeHtml(lead.page) +
        "<br>Country: " + escapeHtml(lead.country) + "<br>Sent: " + escapeHtml(lead.sentAt) + "</p>";
      const res = await fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: {
          Authorization: "Bearer " + env.RESEND_API_KEY,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          from,
          to: [to],
          reply_to: email || undefined,
          subject: lead.subject,
          html,
          text: message,
        }),
      });
      if (!res.ok) {
        const detail = await res.text();
        return json(502, { error: "Email provider rejected the request", detail: detail.slice(0, 300) }, origin);
      }
      return json(200, { ok: true, delivered: "email" }, origin);
    }

    if (env.LEAD_WEBHOOK_URL) {
      const res = await fetch(env.LEAD_WEBHOOK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(lead),
      });
      if (!res.ok) return json(502, { error: "Webhook rejected the request" }, origin);
      return json(200, { ok: true, delivered: "webhook" }, origin);
    }
  } catch (err) {
    return json(502, { error: "Delivery failed" }, origin);
  }

  return json(503, { error: "No lead provider configured" }, origin);
}
