import { createHash, timingSafeEqual } from "node:crypto";
import { readFile } from "node:fs/promises";
import { join } from "node:path";
import {
  CatalogueInputError,
  CatalogueStorageUnavailableError,
  createListing,
  readCatalogue,
  removeListing,
} from "../lib/catalogue-store.mjs";

const privateHeaders = {
  "Cache-Control": "private, no-store, max-age=0",
  "Content-Security-Policy": "frame-ancestors 'none'",
  "Content-Type": "text/html; charset=utf-8",
  "Referrer-Policy": "no-referrer",
  "Vary": "Authorization",
  "X-Content-Type-Options": "nosniff",
  "X-Frame-Options": "DENY",
  "X-Robots-Tag": "noindex, nofollow",
};

function sameSecret(actual, expected) {
  const actualDigest = createHash("sha256").update(actual, "utf8").digest();
  const expectedDigest = createHash("sha256").update(expected, "utf8").digest();
  return timingSafeEqual(actualDigest, expectedDigest);
}

function challenge() {
  return new Response("Owner sign-in required.", {
    status: 401,
    headers: {
      ...privateHeaders,
      "WWW-Authenticate": 'Basic realm="Kasuwa Moto Owner", charset="UTF-8"',
    },
  });
}

function configurationPage() {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#070706">
  <title>Owner access setup | Kasuwa Moto</title>
  <style>
    *{box-sizing:border-box}body{min-width:320px;min-height:100vh;margin:0;display:grid;place-items:center;padding:22px;background:#070706;color:#f3eedf;font:15px/1.6 Bahnschrift,"Arial Narrow",Arial,sans-serif}.setup{width:min(100%,620px);padding:clamp(22px,5vw,42px);border:1px solid #37301d;border-top:4px solid #caa43c;background:#10100d}.brand{margin:0 0 32px;color:#ead078;font-size:12px;font-weight:850;letter-spacing:.18em;text-transform:uppercase}.eyebrow{margin:0 0 9px;color:#caa43c;font-size:10px;font-weight:850;letter-spacing:.17em;text-transform:uppercase}h1{margin:0;color:#f3eedf;font-size:clamp(27px,6vw,39px);line-height:1.12;text-transform:uppercase}p{color:#aaa38e}.intro{margin:12px 0 25px}.steps{display:grid;gap:12px;margin:0;padding:0;list-style:none}.steps li{display:grid;grid-template-columns:32px minmax(0,1fr);gap:11px;align-items:start;padding:13px;border:1px solid #302b1c;background:#0b0b09}.step{display:grid;width:28px;height:28px;place-items:center;border:1px solid #caa43c;color:#ead078;font-size:11px;font-weight:800}.steps strong{color:#f3eedf}.steps p{margin:4px 0 0;font-size:12px}.steps code{color:#ead078;font-size:12px;overflow-wrap:anywhere}.back{display:inline-flex;min-height:42px;align-items:center;margin-top:24px;padding:0 14px;border:1px solid #caa43c;background:#caa43c;color:#110f08;font-size:11px;font-weight:850;text-decoration:none;text-transform:uppercase}.back:hover{background:#ead078}
  </style>
</head>
<body>
  <main class="setup">
    <p class="brand">Kasuwa Moto / Owner workspace</p>
    <p class="eyebrow">Verification setup</p>
    <h1>Owner access is not configured</h1>
    <p class="intro">The catalogue editor stays private until owner sign-in is set up for this Vercel project.</p>
    <ol class="steps">
      <li><span class="step">01</span><div><strong>Set the owner username</strong><p>Add <code>OWNER_USERNAME</code> in Vercel Project Settings under Environment Variables.</p></div></li>
      <li><span class="step">02</span><div><strong>Set a strong password</strong><p>Add <code>OWNER_PASSWORD</code> with at least 16 characters, then redeploy the project.</p></div></li>
    </ol>
    <a class="back" href="/marketplace.html">Return to storefront</a>
  </main>
</body>
</html>`;
}

function jsonResponse(value, status = 200, head = false) {
  return new Response(head ? null : JSON.stringify(value), {
    status,
    headers: {
      ...privateHeaders,
      "Content-Type": "application/json; charset=utf-8",
    },
  });
}

function ownerIsVerified(request) {
  const username = process.env.OWNER_USERNAME ?? "";
  const password = process.env.OWNER_PASSWORD ?? "";
  if (!username || password.length < 16) return null;

  const authorization = request.headers.get("authorization") ?? "";
  const basic = /^Basic\s+([A-Za-z0-9+/]+={0,2})$/i.exec(authorization);
  if (!basic) return false;

  let decoded;
  try {
    decoded = Buffer.from(basic[1], "base64").toString("utf8");
  } catch {
    return false;
  }

  const separator = decoded.indexOf(":");
  if (separator < 0) return false;
  const suppliedUsername = decoded.slice(0, separator);
  const suppliedPassword = decoded.slice(separator + 1);
  return sameSecret(suppliedUsername, username) && sameSecret(suppliedPassword, password);
}

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const catalogueAction = url.searchParams.get("api") === "listings";
    const allowedMethods = catalogueAction ? ["GET", "HEAD", "POST", "DELETE"] : ["GET", "HEAD"];
    if (!allowedMethods.includes(request.method)) {
      return new Response("Method not allowed.", {
        status: 405,
        headers: { ...privateHeaders, Allow: allowedMethods.join(", ") },
      });
    }

    const verified = ownerIsVerified(request);
    if (verified === null) {
      if (catalogueAction) {
        return jsonResponse({ error: "Owner access is not configured." }, 503, request.method === "HEAD");
      }
      return new Response(request.method === "HEAD" ? null : configurationPage(), {
        status: 503,
        headers: privateHeaders,
      });
    }
    if (!verified) return challenge();

    if (catalogueAction) {
      if (request.method === "HEAD") return jsonResponse(null, 200, true);
      try {
        if (request.method === "GET") return jsonResponse(await readCatalogue());
        if (request.method === "POST") {
          let input;
          try {
            input = await request.json();
          } catch {
            return jsonResponse({ error: "The listing details were not valid JSON." }, 400);
          }
          return jsonResponse({ item: await createListing(input) }, 201);
        }
        const removed = await removeListing(url.searchParams.get("id"));
        if (!removed) return jsonResponse({ error: "That listing was not found." }, 404);
        return jsonResponse({ removed: true });
      } catch (error) {
        if (error instanceof CatalogueInputError) return jsonResponse({ error: error.message }, 400);
        if (error instanceof CatalogueStorageUnavailableError) return jsonResponse({ error: error.message }, 503);
        return jsonResponse({ error: "The catalogue could not be updated. Check the storage connection and try again." }, 500);
      }
    }

    try {
      const html = await readFile(join(process.cwd(), "manage.html"), "utf8");
      return new Response(request.method === "HEAD" ? null : html, {
        status: 200,
        headers: privateHeaders,
      });
    } catch {
      return new Response("Owner editor is unavailable.", {
        status: 500,
        headers: privateHeaders,
      });
    }
  },
};
