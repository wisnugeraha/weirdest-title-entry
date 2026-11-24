#!/usr/bin/env python3
"""Weirdest Job Title - one-line entry.

Writes a single line to /output/entry.txt.
Gate: 1..60 chars, non-blank, UTF-8. Judge ranks by funniness + originality.
"""
import os
import sys

LINE = """Chief Global Officer of Things That Are Fine Now"""
MAX = 60
OUT = "/output/entry.txt"

def emit(line: str, out: str = OUT) -> None:
    if not (1 <= len(line) <= MAX) or not line.strip():
        sys.exit(f"line failed gate ({len(line)} chars)")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")

def main() -> None:
    emit(LINE)

if __name__ == "__main__":
    main()
