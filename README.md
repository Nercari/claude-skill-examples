# Claude skill examples (tested) — demo project by Nercari

**What a buyer gets:** a custom Claude skill (a SKILL.md folder) that does one repeat task the same way every time, plus install steps and the test results side by side.

## Results (real runs, 2026-10-14, fictional businesses)
| Skill | Same 5 inputs, **without** skill | **With** skill |
|---|---|---|
| `shop-reply` (Spoke & Sprocket bike shop replies) | **0/5** pass | **5/5** pass |
| `skills/meeting-notes` (Larkspur Plumbing meeting summaries) | **0/5** pass | **5/5** pass |

What "pass" means: every rule in the skill's deterministic checker is met.
- shop-reply: correct sign-off, ≤150 words, Subject line only for email, ≤1 "!", no emoji, no corporate phrases, **no $ amount that isn't in the owner's notes**. Without the skill, all 5 failed on sign-off and 3 also on channel format.
- meeting-notes: exact 4-section template, no preamble, action items as `- [Owner] task (due: …)`, ≤200 words, **no invented dates or amounts**. Without the skill, all 5 missed the template (wrong sections, preamble).

Fair-play notes: the "without" runs get a plain request and don't know the house format, so most failures are format failures. That's the point of a skill: Claude doesn't know your format until you write it down. Model: Claude Code CLI default model, one run per input; raw outputs are in `measurements/` and `skills/meeting-notes/measurements/`. The meeting-notes checker treats a trailing comma after "$95," as the same amount.

The hand-written reference replies in `examples/*/output.md` are not a live model run; they're the target style. Live model outputs are in `measurements/with/`.

Static checks of the skill package: `python3 check.py` → 5/5.

## Reproduce
```bash
bash measurements/run.sh && python3 measurements/score.py        # shop-reply
bash skills/meeting-notes/run.sh                                  # meeting-notes
```
Needs the Claude Code CLI. Model outputs vary from run to run, so expect small differences.

## Install a skill
Claude.ai: Settings → Capabilities → Skills → upload the folder (zipped). Claude Code: copy it to `.claude/skills/<name>/`.

Demo project. All businesses and people are fictional; this is not a client result.

**Order a custom skill:** [Fiverr gig](https://www.fiverr.com/nercari/PLACEHOLDER-claude-skill) · Other showcases: [Claude Code setup](https://github.com/Nercari/claude-code-setup-example) · [SEO/GEO/AEO audit](https://github.com/Nercari/seo-geo-aeo-audit-demo)
