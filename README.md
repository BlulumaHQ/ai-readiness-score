# Bluluma AI Readiness Score

Quiz funnel live at https://score.bluluma.com/en and https://score.bluluma.com/zh

- Static site in `public/` served by a Cloudflare Worker (static assets, SPA fallback).
- Backend: Supabase project `bluluma-central-cms`, table `quiz_leads`, edge function `quiz-api`.
- Payment: Stripe Payment Links (Bluluma Design) set in `PAYLINK` inside `public/index.html`.
- Deploy: Cloudflare Workers → Import repo, deploy command `npx wrangler deploy`.

Source files for editing live in `src/` (`v3.html` + `build.py` inline the data and logo).
