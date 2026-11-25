#!/usr/bin/env python3
"""Midnight Fridge Roast — one-line roast entry.

Writes a single roast line for a smart fridge that refuses to open
after midnight to /output/entry.txt (UTF-8, one line, under 200 chars).
No network, no external files, no arguments.
"""

import os

LINE = (
    "At 12:03 my fridge beeped, locked, and displayed a tiny padlock, "
    "like a nightclub bouncer guarding three yogurts and a jar of pickles."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
