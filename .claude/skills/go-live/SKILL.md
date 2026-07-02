---
name: go-live
description: Pre-launch readiness check — verifies the product, docs, security basics, and operations are ready before deploying or showing the project to the world. Produces a Go / No-Go report. Use before any launch or deployment.
---

# /go-live — Launch Readiness Check

Runs the checks a careful engineer would run before putting a product in front of real users, and turns them into a plain-English Go / No-Go report. Designed so a non-technical owner can launch with confidence.

## Steps

1. **Establish what "live" means here.** Read `docs/project_spec.md` and `docs/architecture.md`. If the deployment target is unclear (hosting, domain, how users reach it), ask the user one question to pin it down.

2. **Run the checklist.** For each area, actually inspect the repo — do not take the docs' word for it:

   **Product**
   - Do the MVP user stories in the spec have working implementations?
   - Does every user-facing flow have an error path (failed submit, empty state, bad input)?
   - Is there a sensible first-time experience (what a brand-new user sees)?

   **Security & secrets**
   - Scan the repo for committed secrets: API keys, passwords, tokens, `.env` files. Check `.gitignore` covers env and data files.
   - Are admin/owner areas actually protected (auth in place, no default passwords)?
   - Are inputs validated on the server side, not just the browser?

   **Operations**
   - Are required environment variables documented (e.g. `.env.example`)?
   - Is there any way for the owner to know the product is down (uptime monitor, alert)? If not, recommend a free one.
   - Is data backed up, or at least recoverable? Say what would happen if the database were lost today.

   **House rules**
   - Re-read `docs/house_rules.md` and verify the launch candidate honours every rule (budget of chosen hosting, never-do list, always rules). A house-rule violation is an automatic blocker.

   **Docs & housekeeping**
   - `docs/project_status.md` reflects reality; `docs/changelog.md` has an entry for the launch candidate.
   - No placeholder text left anywhere a user or teammate could see.

   **Launch convenience** *(when the product is a deployable web app)*
   - Offer to add a one-click deploy path to the project's README (e.g. a Vercel/Netlify deploy button) and a short "how to deploy" section, so launching and re-launching never requires remembering steps.

3. **Produce the report:**

   ```
   Go-Live Report — [project name]

   Verdict: GO / NO-GO (with the one-line reason)

   Blockers (must fix before launch)
   - ...

   Strongly recommended (fix in the first week)
   - ...

   Ready
   - ...
   ```

   Order blockers by risk. Every item gets a concrete action, not just a finding.

4. **Offer to fix.** Ask which blockers to tackle now, and work through them. Re-run the relevant check after each fix so the verdict is earned, not assumed.

## Rules

- A NO-GO verdict is a favour, not a failure — deliver it plainly and kindly.
- Verify by looking at code and running things, never by assuming the docs are accurate.
- Keep the report shareable: the owner should be able to paste it to a partner or client as-is.
