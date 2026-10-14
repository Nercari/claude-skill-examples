# Claude skill examples — measured, fictional demos by Nercari

[![checks](https://github.com/Nercari/claude-skill-examples/actions/workflows/checks.yml/badge.svg)](https://github.com/Nercari/claude-skill-examples/actions/workflows/checks.yml)
[![Live demo](https://img.shields.io/badge/live%20demo-nercari.github.io-blue)](https://nercari.github.io/claude-skill-examples/)
[![llms.txt](https://img.shields.io/badge/llms.txt-ready-green)](./llms.txt)

**What a buyer gets:** a custom Claude skill (a `SKILL.md` folder) that does one repeat task the same way every time, plus install steps and the test results side by side.

> Fictional demos only. Velocrank Cycle Works and Quillmere Plumbing are not real businesses and are not client work. Numbers below come from reproducible local runs dated **2026-10-14**.

## What changed when the skill was on?

| Skill | Same 5 inputs, **without** skill | **With** skill | How to reproduce |
|---|---|---|---|
| `shop-reply` (Velocrank Cycle Works bike shop replies) | **0/5** pass | **5/5** pass | `bash measurements/run.sh && python3 measurements/score.py` |
| `skills/meeting-notes` (Quillmere Plumbing meeting summaries) | **0/5** pass | **5/5** pass | same commands against the meeting-notes fixtures |

**What "pass" means:** every rule in the skill's deterministic checker is met.
- shop-reply: correct sign-off, ≤150 words, Subject line only for email, ≤1 "!", no emoji, no corporate phrases, **no $ amount that isn't in the owner's notes**. Without the skill, all 5 failed on sign-off and 3 also on channel format.
- meeting-notes: required sections present, no invented decisions, action owners only from the transcript.

Static package checks: `python3 check.py` → **5/5**.

## Live demo

[nercari.github.io/claude-skill-examples](https://nercari.github.io/claude-skill-examples/) — landing page for the Velocrank Cycle Works skill demo, with schema, sitemap, robots (AI crawlers allowed) and `llms.txt`.

The `examples/*/output.md` files are **hand-written fixtures used by the checker**, not a live model run. The with/without scores under `measurements/` come from the dated 2026-10-14 runs described in the table above.

## What's in this repo?

- `SKILL.md` and `skills/` — the skills as delivered
- `examples/` — sample inputs and outputs
- `measurements/` — the 5 fixtures, with/without runs, and the scorer
- `check.py` — CI package checks
- `docs/pages/` — the GitHub Pages site
- `llms.txt` — machine-readable summary for AI crawlers

## FAQ

### Do these numbers prove my shop will get the same pass rate?
No. They prove the skill enforced its rules on these fixtures. Your inputs and rules will differ; the same checker pattern applies.

### Can the skill invent prices?
The shop-reply checker fails any dollar amount that is not in the owner's notes. On the with-skill runs, inventing a price never happened.

### Are Velocrank Cycle Works and Quillmere Plumbing real clients?
No. Both are fictional demos created by Nercari so the results can be public and reproducible.

### How do I install a skill?
Copy the skill folder into your Claude skills directory (see the skill's own README / `SKILL.md`). Then run the checker on your own fixtures.

## Order / related

**Order a custom skill:** [Fiverr gig](https://www.fiverr.com/nercari/PLACEHOLDER-claude-skill) · Other showcases: [Claude Code setup](https://github.com/Nercari/claude-code-setup-example) · [SEO/GEO/AEO audit](https://github.com/Nercari/seo-geo-aeo-audit-demo) · [Nercari profile](https://github.com/Nercari/Nercari)

Delivery-only. No video calls, voice or face content. No rankings promised.
