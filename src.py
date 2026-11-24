#!/usr/bin/env python3
"""The One-Line Laugh — make.fun program/v1 entry.

Writes one funny line to /output/entry.txt (or MAKEFUN_OUTPUT_DIR
outside the grader). Deterministic: identical bytes on every run.
"""

import os

LINE = "I told my smartwatch I wanted to get fit, so now it congratulates me every time I walk to the fridge like I've climbed a mountain."


def write_entry() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    write_entry()
