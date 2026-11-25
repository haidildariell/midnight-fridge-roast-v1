#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes one line of text roasting a smart fridge that refuses to open
after midnight, to /output/entry.txt. The line is a fixed, hand-written
roast: the fridge locks itself at midnight and flashes a little moon
icon, as if the leftovers filed a restraining order against its owner.

The roast is assembled from a setup and a punchline so each half can be
checked on its own, then the finished line is validated against the
competition gate (1-200 UTF-8 characters, one line, not blank) before
it is written.
"""

import os

SETUP = "My fridge locks itself at midnight and flashes a little moon icon,"
PUNCHLINE = "as if the leftovers filed a restraining order against me."

OUTPUT_PATH = "/output/entry.txt"


def build_roast():
    """Join setup and punchline into the single roast line."""
    return SETUP + " " + PUNCHLINE


def validate(line):
    """Check the line against the competition gate before writing it."""
    if not line.strip():
        raise ValueError("roast line is blank")
    if "\n" in line:
        raise ValueError("roast line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("roast line must be 1-200 characters, got %d" % len(line))
    return line


def main():
    line = validate(build_roast())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
