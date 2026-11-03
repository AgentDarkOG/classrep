# Kasuwa Moto Vercel setup

## Storage

The owner catalogue stores listing records and their photos in Vercel Blob. Create a **public** Blob store for this project, because shoppers need to load listing photos. The owner write API remains protected by owner sign-in.

```text
vercel storage create kasuwa-moto-catalogue --type blob --access public
vercel storage connect kasuwa-moto-catalogue --environment production --environment preview --yes
```

The project uses Vercel's OIDC connection for Blob. Connecting the store adds the store identity to those environments; Vercel issues short-lived credentials to its Functions automatically. No long-lived Blob secret needs to be copied into the code or archive.

## Owner access

Set these Vercel project environment variables for Production. Add them to Preview too if you want to use the owner page on preview deployments:

- `OWNER_USERNAME`: the owner sign-in name.
- `OWNER_PASSWORD`: a strong password with at least 16 characters.

The owner editor is served at `/manage`. Listing details and uploaded photos are public, while catalogue changes require the owner credentials.

## Public storefront

Set Vercel Authentication to protect Preview deployments only. The Production domain must be public for shoppers. Keep the `/manage` Basic Authentication enabled; it is separate from Vercel deployment protection.

## Build and deploy

```text
npm install
npm run build
vercel deploy --prod
```

The homepage is `/` or `/marketplace.html`; the public catalogue is `/listings.html`.

This project displays public goods and services. It does not process payments, orders, delivery, or repair bookings.
