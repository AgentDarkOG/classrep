# Kasuwa Moto Marketplace handoff

This folder contains the marketplace website and the files it needs to build and run on Vercel. It is prepared for another developer to review and finish.

## Start here

1. Extract the ZIP into a new folder.
2. Install Node.js 24.x and run `npm install` in that folder.
3. Run `npm run build` to create the static site in `dist/`.
4. Review `VERCEL_SETUP.md` before connecting or deploying the project.

The homepage is `marketplace.html`; the public catalogue is `listings.html`; the owner editor is `/manage` after deployment. The two `motorcycle-background-*-faststart.mp4` files are the homepage background videos.

## Current implementation

- The homepage hero uses a motorcycle illustration and the site's black, gold, and ivory palette.
- Public listings load from `/api/listings`.
- The owner editor uses the protected `/manage` API to add and remove listings.
- Listing records and uploaded photos are designed to persist in Vercel Blob.
- Legal pages, favicon, custom 404 page, build files, and deployment configuration are included.

## Handoff status and open work

- The source in this archive contains local changes that have **not** been deployed. The currently deployed Production site may still be running older code.
- A public Vercel Blob store named `kasuwa-moto-catalogue` was created and connected to the original Vercel project for Production and Preview. It is currently empty.
- The original project has owner credentials configured in Production. Their values are deliberately not included here. The next developer will need access to the Vercel project to manage its environment variables and deployments.
- The original Vercel project's deployment protection is set to `all_except_custom_domains`. Review how that affects public access to the intended Production URL before launch.
- The new Blob-backed listing API has passed local syntax/build checks, but still needs an end-to-end check on a Vercel deployment. No sample listing has been uploaded.
- The site is a catalogue only. It does not process payments, orders, delivery, or repair bookings.

## Included files

The archive contains the web pages, API and storage code, build/deployment configuration, dependency manifests, setup notes, catalogue seed file, and the two background videos. It excludes coursework, local dependencies/build output, Vercel project-link metadata, and account secrets.

