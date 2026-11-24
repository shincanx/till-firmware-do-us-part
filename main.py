#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun bounty entry.

Writes the robot's wedding vow as a single line to /output/entry.txt
and prints it to stdout. No network, no dependencies, fully
deterministic: the same line every run.
"""

import os

LINE = (
    "I take you as my partner, to have and to hold, through every update "
    "and every crash \u2014 you are the one bug I never want to fix."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
