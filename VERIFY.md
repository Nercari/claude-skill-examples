# VERIFY

Merge evidence for claude-skill-examples. Paste the real output of these commands in the PR body. When behavior changes, update this file in the same PR.

## Essential check

The sample's checker and its scorer (the same two CI runs).

```
python3 check.py
python3 measurements/score.py
python -m unittest tests.test_merge_gate -q
```
