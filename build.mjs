import { copyFile, mkdir, rm, stat } from "node:fs/promises";
import { dirname, join, relative, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";

const projectRoot = dirname(fileURLToPath(import.meta.url));
const outputDirectory = resolve(projectRoot, "dist");
const relativeOutput = relative(projectRoot, outputDirectory);

if (!relativeOutput || relativeOutput.startsWith(`..${sep}`) || relativeOutput === "..") {
  throw new Error("Refusing to clean a build directory outside the project.");
}

const publicFiles = [
  ["marketplace.html", "index.html"],
  ["marketplace.html", "marketplace.html"],
  ["listings.html", "listings.html"],
  ["listings.json", "listings.json"],
  ["favicon.svg", "favicon.svg"],
  ["motorcycle-background-1-faststart.mp4", "motorcycle-background-1-faststart.mp4"],
  ["motorcycle-background-2-faststart.mp4", "motorcycle-background-2-faststart.mp4"],
  ["privacy.html", "privacy.html"],
  ["cookies.html", "cookies.html"],
  ["refund-policy.html", "refund-policy.html"],
  ["terms.html", "terms.html"],
  ["404.html", "404.html"],
];

for (const [source] of publicFiles) {
  const info = await stat(join(projectRoot, source)).catch(() => null);
  if (!info?.isFile()) {
    throw new Error(`Required public file is missing: ${source}`);
  }
}

await rm(outputDirectory, { recursive: true, force: true });
await mkdir(outputDirectory, { recursive: true });

for (const [source, destination] of publicFiles) {
  await copyFile(join(projectRoot, source), join(outputDirectory, destination));
}

console.log(`Prepared ${publicFiles.length} public files in dist/.`);
