#!/usr/bin/env python3
"""CI check: fail if docs/debates/backlog.md is out of date with debates/backlog.yaml.

Usage:
    python scripts/check_backlog_freshness.py

Exit codes:
    0 — backlog.md matches what render_backlog.py would produce
    1 — backlog.md is stale; re-run: python scripts/render_backlog.py
"""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
BACKLOG_MD = REPO_ROOT / "docs" / "debates" / "backlog.md"

# Import the renderer
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from render_backlog import render  # noqa: E402


def main():
    # Capture current content
    current = BACKLOG_MD.read_text() if BACKLOG_MD.exists() else ""

    # Render fresh
    render()
    fresh = BACKLOG_MD.read_text()

    if current == fresh:
        print("OK: backlog.md is up to date with backlog.yaml")
        sys.exit(0)
    else:
        # Restore original so the check is non-destructive
        BACKLOG_MD.write_text(current)
        print("FAIL: backlog.md is stale. Run: python scripts/render_backlog.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
