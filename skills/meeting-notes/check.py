#!/usr/bin/env python3
"""Deterministic rules for meeting-notes outputs. Usage: check.py <outputs_dir> (files NN.md matched to examples/NN.md)"""
import re, sys, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
HEADS = ["## Summary", "## Decisions", "## Action items", "## Open questions"]
def rules(out, inp):
    f = []
    if [h.strip() for h in re.findall(r"^## .+$", out, re.M)] != HEADS: f.append("sections")
    if not out.lstrip().startswith("## Summary"): f.append("preamble")
    if len(out.split()) > 200: f.append("length")
    m = re.search(r"## Action items\n(.*?)(\n## |\Z)", out, re.S)
    for line in (m.group(1).strip().splitlines() if m else []):
        if line.strip() and not re.match(r"- (None.*|\[[^\]]+\] .+\(due: [^)]+\))\s*$", line.strip()): f.append("action-format"); break
    for d in re.findall(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w* (\d{1,2})\b", out):
        if d not in inp: f.append("invented-date"); break
    for n in (x.rstrip(",") for x in re.findall(r"\$[\d,]+", out)):
        if n not in inp: f.append("invented-number"); break
    return f
d = Path(sys.argv[1]); res = {o.stem: rules(o.read_text(), (HERE / "examples" / o.name).read_text()) for o in sorted(d.glob("*.md"))}
p = sum(not v for v in res.values()); print(f"{d.name}: {p}/{len(res)} pass", {k: v for k, v in res.items() if v})
json.dump({"passed": p, "total": len(res), "failures": res}, open(d.parent / f"results-{d.name}.json", "w"), indent=1)
