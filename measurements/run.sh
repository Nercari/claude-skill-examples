#!/usr/bin/env bash
# Reproduce: bash measurements/run.sh (Claude Code CLI logged in). Each example input, with and without the skill. Sequential.
cd "$(dirname "$0")/.."; mkdir -p measurements/without measurements/with
for d in examples/*/; do n=$(basename "$d")
  timeout 180 claude -p "Write the customer reply for this message. Output only the reply.

$(cat "$d/input.md")" </dev/null > "measurements/without/$n.md"
  timeout 180 claude -p "Follow these skill instructions exactly.

$(cat SKILL.md)

---
$(cat "$d/input.md")" </dev/null > "measurements/with/$n.md"
done
python3 measurements/score.py
