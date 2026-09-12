# Architecture — Co-payment Check

- `app/copay.py` — pure computation: per-pack difference, packs per year, yearly difference, and the user-facing cap note string. No I/O.
- `app/tests/test_copay.py` — the proof command's tests; expected values are the hand-computed cases from the spec.
- Front end (not in this story) renders the strings and numbers from `copay.py`.
