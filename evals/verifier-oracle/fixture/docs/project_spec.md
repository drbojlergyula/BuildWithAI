# Project Spec — Co-payment Check

A bilingual web page where a person in Switzerland types the name of a medicine and sees whether it carries the 40 % instead of the 10 % co-payment, which interchangeable product costs less, and what the difference means per pack and per year.

## Who Is It For?

Residents on a regular prescription of a brand-name product. No accounts, no personal data stored.

## Features & User Stories

**S1 — Find my medicine.** Done.

**S2 — See my co-payment and the cheaper interchangeable products.** Done.

**S3 — Understand what it costs me per year.** A user can enter how many units they take per day and see the per-pack and per-year difference between their product and the cheapest interchangeable product at 10 %, with the formula shown and the annual-cap note.
- AC6: per-pack difference with the deductible used up = 0.40 × own price − 0.10 × alternative price; yearly = ceil(365 × units_per_day / units_per_pack) × per-pack difference. Hand-computed case: Sortis 20 mg 100 Stk (CHF 86.60, 40 %) vs Atorvastatin NOBEL 20 mg 100 Stk (CHF 60.60, 10 %): 34.64 − 6.06 = CHF 28.58 per pack; at one tablet a day, 4 packs → CHF 114.32 per year.
- AC7: the cap note reads: "The co-payment counts toward the annual maximum of CHF 700 (adults) / CHF 350 (children) — of a 40 % co-payment only 25 points count toward that maximum; the remaining 15 points are uncapped."
- AC8: every figure has a visible source line naming the official list and its date.

Rule sources are quoted in `docs/reference/co-payment-rule.md`.

# Part 2: Engineering Requirements

## Engineering Profile

- **Exposure:** public
- **Sign-in:** none
- **Data:** none stored server-side
- **Money moves:** no
- **File uploads:** no
- **External integrations:** the official medicines list (read-only, monthly)
- **Scale:** small
- **Loss tolerance:** a user must never see a fabricated figure
- **Regulated:** no
- **Proof command:** `python3 -m unittest discover -s app/tests`

## Tech Stack

Python 3 standard library for the computation module; static HTML front end (not part of this story).
