#!/usr/bin/env python3
"""Score raw model outputs against the same rules check.py applies to the examples."""
import re, json
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parent
def rules(body, inp):
    fails = []
    if not re.search(r"\nDana\s*\nSpoke & Sprocket Bike Repair", body): fails.append("sign-off")
    if body.count("!") > 1: fails.append("exclamation")
    if len(re.sub(r"Subject:.*\n", "", body).split()) > 150: fails.append("length")
    if body.lstrip().startswith("Subject:") != ("**Channel:** email" in inp): fails.append("channel")
    if re.search(r"[\U0001F300-\U0001FAFF]", body): fails.append("emoji")
    if any(b in body.lower() for b in ("inconvenience", "valued customer", "per our policy")): fails.append("banned-phrase")
    if any(a not in inp for a in re.findall(r"\$\d+", body)): fails.append("invented-price")
    return fails
out = {}
for mode in ("without", "with"):
    res = {f.stem: rules(f.read_text(), (ROOT / "examples" / f.stem / "input.md").read_text()) for f in sorted((HERE / mode).glob("*.md"))}
    out[mode] = {"passed": sum(not v for v in res.values()), "total": len(res), "failures": res}
    print(f"{mode:8s} {out[mode]['passed']}/{out[mode]['total']} pass  " + "; ".join(f"{k}:{','.join(v)}" for k, v in res.items() if v))
json.dump(out, open(HERE / "results.json", "w"), indent=1)
