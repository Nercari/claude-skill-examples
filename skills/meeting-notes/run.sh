#!/usr/bin/env bash
# Reproduce: bash run.sh (Claude Code CLI logged in). Sequential, 180 s timeout per call.
cd "$(dirname "$0")"; mkdir -p measurements/with measurements/without
for f in examples/*.md; do n=$(basename $f)
 timeout 180 claude -p "Summarize these meeting notes.

$(cat $f)" </dev/null > measurements/without/$n
 timeout 180 claude -p "Follow these skill instructions exactly.

$(cat SKILL.md)

---
$(cat $f)" </dev/null > measurements/with/$n
done
python3 check.py measurements/without; python3 check.py measurements/with
