#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (UTF-8, 1-120 characters, no trailing newline so the
file content is exactly the line). Deterministic: no input, no clock,
no randomness, no network — every run writes the same bytes.
"""

import os

LINE = "Every TODO you leave behind is a letter to a stranger who shares your name."


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
