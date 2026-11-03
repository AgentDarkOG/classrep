import {
  CatalogueStorageUnavailableError,
  readCatalogue,
} from "../lib/catalogue-store.mjs";

const headers = {
  "Cache-Control": "public, no-store, max-age=0",
  "Content-Type": "application/json; charset=utf-8",
  "X-Content-Type-Options": "nosniff",
};

function jsonResponse(value, status = 200, head = false) {
  return new Response(head ? null : JSON.stringify(value), { status, headers });
}

export default {
  async fetch(request) {
    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method not allowed.", {
        status: 405,
        headers: { ...headers, Allow: "GET, HEAD" },
      });
    }

    if (request.method === "HEAD") return jsonResponse(null, 200, true);
    try {
      return jsonResponse(await readCatalogue());
    } catch (error) {
      const message = error instanceof CatalogueStorageUnavailableError
        ? error.message
        : "The catalogue is temporarily unavailable.";
      return jsonResponse({ error: message }, 503);
    }
  },
};
