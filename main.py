#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt
(or the path in ENTRY_OUTPUT). Standard library only.

The word is validated against the competition gate before anything is
written: 1-30 characters, a single word with no whitespace, plain ASCII.
"""

import os
import sys

WORD = "Blackhole"

MAX_CHARS = 30


def validate(word: str) -> None:
    """Fail loudly if the entry would not pass the gate."""
    if not word or len(word) > MAX_CHARS:
        sys.exit(f"entry must be 1-{MAX_CHARS} characters, got {len(word)}")
    if any(ch.isspace() for ch in word):
        sys.exit("entry must be a single word with no whitespace")
    if not word.isascii():
        sys.exit("entry must be plain ASCII")


def main() -> None:
    validate(WORD)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
