#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes one line of text roasting a smart fridge that refuses to open
after midnight, to /output/entry.txt. The line is a fixed, hand-written
roast: the fridge locks itself at midnight and flashes a little moon
icon, as if the leftovers filed a restraining order against its owner.
"""

import os

ROAST = (
    "My fridge locks itself at midnight and flashes a little moon icon, "
    "as if the leftovers filed a restraining order against me."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
