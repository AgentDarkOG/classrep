import { randomUUID } from "node:crypto";
import { del, list, put } from "@vercel/blob";

export const categories = new Set([
  "Motorcycles",
  "Parts",
  "Riding gear",
  "Repair service",
  "Rider learning",
]);

const itemPrefix = "catalogue/items/";
const imagePrefix = "catalogue/images/";
const maximumImageBytes = 2 * 1024 * 1024;

export class CatalogueInputError extends Error {}
export class CatalogueStorageUnavailableError extends Error {}

function blobAuth() {
  const token = process.env.BLOB_READ_WRITE_TOKEN;
  if (token) return { token };
  if (process.env.BLOB_STORE_ID) return {};
  throw new CatalogueStorageUnavailableError("Catalogue storage is not connected to this Vercel environment.");
}

function validateDetails(input) {
  const name = typeof input?.name === "string" ? input.name.trim() : "";
  const category = typeof input?.category === "string" ? input.category : "";
  const description = typeof input?.description === "string" ? input.description.trim() : "";
  const price = Number(input?.price);

  if (!name || name.length > 90) throw new CatalogueInputError("Enter an item name up to 90 characters long.");
  if (!categories.has(category)) throw new CatalogueInputError("Choose a valid listing category.");
  if (!Number.isSafeInteger(price) || price < 1) throw new CatalogueInputError("Enter a whole-number price greater than zero.");
  if (!description || description.length > 500) throw new CatalogueInputError("Enter a description up to 500 characters long.");
  return { name, category, price, description };
}

function isPublicImageUrl(value) {
  if (typeof value !== "string" || !value) return false;
  try {
    const url = new URL(value);
    return url.protocol === "https:" && url.hostname.endsWith(".public.blob.vercel-storage.com");
  } catch {
    return false;
  }
}

function publicListing(item) {
  return {
    id: item.id,
    name: item.name,
    category: item.category,
    price: item.price,
    description: item.description,
    image: isPublicImageUrl(item.image) ? item.image : "",
  };
}

export async function readCatalogue() {
  const auth = blobAuth();
  const records = [];
  let cursor;
  let hasMore = true;

  while (hasMore) {
    const page = await list({
      prefix: itemPrefix,
      limit: 1000,
      cursor,
      ...auth,
    });
    records.push(...page.blobs);
    hasMore = page.hasMore;
    cursor = page.cursor;
  }

  const items = await Promise.all(records.map(async blob => {
    const response = await fetch(blob.url, { cache: "no-store" });
    if (!response.ok) throw new Error("A catalogue record could not be loaded.");
    const item = await response.json();
    return publicListing(item);
  }));

  return items.sort((left, right) => right.id.localeCompare(left.id));
}

export async function createListing(input) {
  const auth = blobAuth();
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    throw new CatalogueInputError("Enter listing details before publishing.");
  }
  const details = validateDetails(input);
  if (details.category === "Motorcycles" && !input.imageData) {
    throw new CatalogueInputError("Add a motorcycle photo before publishing this listing.");
  }
  const id = randomUUID();
  let image = "";
  let imageUrl = "";

  if (input.imageData) {
    if (typeof input.imageData !== "string" || input.imageData.length > 3_000_000) {
      throw new CatalogueInputError("The compressed image is too large. Choose a smaller photo.");
    }
    const match = /^data:image\/(webp|jpeg);base64,([A-Za-z0-9+/]*={0,2})$/.exec(input.imageData);
    if (!match) throw new CatalogueInputError("Choose a compressed JPG or WebP photo.");
    const bytes = Buffer.from(match[2], "base64");
    if (!bytes.length || bytes.length > maximumImageBytes || bytes.toString("base64") !== match[2]) {
      throw new CatalogueInputError("The compressed photo must be smaller than 2 MB.");
    }
    const extension = match[1] === "webp" ? "webp" : "jpg";
    const contentType = match[1] === "webp" ? "image/webp" : "image/jpeg";
    const blob = await put(`${imagePrefix}${id}.${extension}`, bytes, {
      access: "public",
      addRandomSuffix: false,
      contentType,
      cacheControlMaxAge: 31_536_000,
      ...auth,
    });
    image = blob.url;
    imageUrl = blob.url;
  }

  const item = { ...details, id, image, createdAt: new Date().toISOString() };
  try {
    await put(`${itemPrefix}${id}.json`, JSON.stringify(item), {
      access: "public",
      addRandomSuffix: false,
      contentType: "application/json; charset=utf-8",
      cacheControlMaxAge: 60,
      ...auth,
    });
  } catch (error) {
    if (imageUrl) await del(imageUrl, auth).catch(() => {});
    throw error;
  }

  return publicListing(item);
}

export async function removeListing(id) {
  const auth = blobAuth();
  if (typeof id !== "string" || !/^[0-9a-f-]{36}$/i.test(id)) {
    throw new CatalogueInputError("Choose a valid catalogue item.");
  }

  const pathname = `${itemPrefix}${id}.json`;
  const result = await list({ prefix: pathname, limit: 2, ...auth });
  const record = result.blobs.find(blob => blob.pathname === pathname);
  if (!record) return false;

  const response = await fetch(record.url, { cache: "no-store" });
  if (!response.ok) throw new Error("The catalogue item could not be read before removal.");
  const item = await response.json();
  await del(record.url, auth);
  if (isPublicImageUrl(item.image)) {
    await del(item.image, auth).catch(() => {});
  }
  return true;
}
