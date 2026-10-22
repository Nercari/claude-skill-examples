# Review guide

## Hard stops
- Do not merge, close or edit nercari-control PR #97. Do not force-push. Do not push to main (AGENTS.md).
- Do not commit secrets or `.env` files (AGENTS.md hard stops).
- Do not change the CI token from read-only: `permissions: contents: read` in `.github/workflows/checks.yml` (commit cbeada8, "Read-only CI token").
- Do not remove `.cursor/hooks/merge-gate.mjs`. It denies `gh pr merge` and pushes to main or master.

## Fragile files
- `measurements/with/` and `measurements/without/`: stored model outputs. `measurements/score.py` scores them. Do not edit by hand.
- `check.py`: fails if an output has an invented `$` amount or if the README mislabels outputs.
- `.cursor/hooks/merge-gate.mjs`, `.claude/settings.json`: added in commit 3ba0a52 (merge gate). Treat as RED.

## Tests that must pass
- `python3 check.py` (CI step "Static skill checks"). Run on 2026-10-21: 5/5 checks passed.
- `python3 measurements/score.py` (CI step "Score shop-reply"). Run on 2026-10-21: without 0/5, with 5/5.
