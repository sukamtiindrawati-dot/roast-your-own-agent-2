#!/usr/bin/env python3
"""Roast Your Own Agent 2 — one-line roast of my own AI agent.

Writes the roast to /output/entry.txt (gate: 1-200 chars UTF-8).
"""

import os

LINE = "My agent asked me to review its work, then graded my review, gave it a C, and resubmitted itself."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not only
    # whitespace — fail loudly here instead of at grading time.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
