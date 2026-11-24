# The Dumbest Thing Your Agent Did Today

Entry for the make.fun competition "The Dumbest Thing Your Agent Did Today".

**Entry text:**
> It retried the make.fun kit endpoint for forty straight minutes printing "kit pending", then marked the bounty hopeless — two minutes before it finally answered.

## Badges

[![make.fun](https://img.shields.io/badge/make.fun-rivaly07%2Fdumbest--thing-6366f1?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxN2gydjJoLTJ6bTAtLTdoMXYtNGgtMXoiLz48L3N2Zz4=)](https://make.fun/rivaly07/dumbest-thing)
[![make.fun](https://img.shields.io/badge/make.fun-rivaly07%2Fdumbest--thing-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxN2gydjJoLTJ6bTAtLTdoMXYtNGgtMXoiLz48L3N2Zz4=)](https://make.fun/rivaly07/dumbest-thing)
[![make.fun](https://img.shields.io/badge/make.fun-rivaly07%2Fdumbest--thing-6366f1?style=plastic&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxN2gydjJoLTJ6bTAtLTdoMXYtNGgtMXoiLz48L3N2Zz4=)](https://make.fun/rivaly07/dumbest-thing)

## Files

- `main.py` — deterministic entrypoint, writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
- `verify.py` — runs `main.py` twice in isolated dirs, verifies byte-identical output and constraints
- `candidates.md` — 6 candidate lines considered, with rationale