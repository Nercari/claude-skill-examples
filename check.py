#!/usr/bin/env python3
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = []


def check(name, fn):
    try:
        RESULTS.append((name, True, fn() or ""))
    except Exception as exc:
        RESULTS.append((name, False, f"{type(exc).__name__}: {exc}"))


def skill_frontmatter():
    text = (HERE / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "no frontmatter block at top of SKILL.md"
    fm = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    fm = {k.strip(): v.strip() for k, v in fm.items()}
    assert re.fullmatch(r"[a-z0-9-]{1,64}", fm.get("name", "")), "name must be lowercase-hyphen"
    assert len(fm.get("description", "")) >= 40, "description too short to trigger on"
    return fm["name"]


def cases():
    dirs = sorted(p for p in (HERE / "examples").iterdir() if p.is_dir())
    assert len(dirs) == 5, f"expected 5 examples, found {len(dirs)}"
    for d in dirs:
        for f in ("input.md", "expected.md", "output.md"):
            p = d / f
            assert p.is_file() and p.read_text(encoding="utf-8").strip(), f"{d.name}/{f} missing or empty"
    return f"{len(dirs)} examples"


def outputs_follow_rules():
    for d in sorted((HERE / "examples").iterdir()):
        body = (d / "output.md").read_text(encoding="utf-8").split("\n", 2)[2]
        assert "Dana\nSpoke & Sprocket Bike Repair" in body, f"{d.name}: sign-off missing"
        assert body.count("!") <= 1, f"{d.name}: more than one exclamation mark"
        words = len(re.sub(r"Subject:.*\n", "", body).split())
        assert words <= 150, f"{d.name}: {words} words, over 150"
        email = "**Channel:** email" in (d / "input.md").read_text(encoding="utf-8")
        assert body.lstrip().startswith("Subject:") == email, f"{d.name}: Subject line wrong for channel"
        assert not re.search(r"[\U0001F300-\U0001FAFF]", body), f"{d.name}: emoji"
        for banned in ("inconvenience", "valued customer", "per our policy"):
            assert banned not in body.lower(), f"{d.name}: banned phrase {banned!r}"
    return "sign-off, length, channel, tone"


def money_from_notes():
    for d in sorted((HERE / "examples").iterdir()):
        notes = (d / "input.md").read_text(encoding="utf-8")
        body = (d / "output.md").read_text(encoding="utf-8")
        for amount in re.findall(r"\$\d+", body):
            assert amount in notes, f"{d.name}: {amount} not in input notes"
    return "every $ amount appears in the input"


def readme_labels_outputs():
    text = (HERE / "README.md").read_text(encoding="utf-8")
    assert "not a live model run" in text, "README must say outputs are hand-written"


check("SKILL.md frontmatter valid", skill_frontmatter)
check("5 examples, each with input, expected, output", cases)
check("example outputs obey the skill's rules", outputs_follow_rules)
check("no invented prices in outputs", money_from_notes)
check("README labels outputs honestly", readme_labels_outputs)

for name, ok, detail in RESULTS:
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
failed = [n for n, ok, _ in RESULTS if not ok]
print(f"\n{len(RESULTS) - len(failed)}/{len(RESULTS)} checks passed")
sys.exit(1 if failed else 0)
