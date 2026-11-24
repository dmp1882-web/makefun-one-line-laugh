#!/usr/bin/env python3
"""The One-Line Laugh entry (make.fun program/v1, Python 3.13, standard library only).

Writes the entry text to /output/entry.txt. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The program is deterministic: it writes the same bytes on every run.
"""

import os

TEXT = "I told my smartwatch I wanted to get fit, so now it congratulates me every time I walk to the fridge like I've climbed a mountain."

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
