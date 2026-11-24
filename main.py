#!/usr/bin/env python3
"""Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production, to /output/entry.txt (1-200 characters, UTF-8).
"""

import os

EXCUSE = "The bug isn't new \u2014 production just ran the code path I swore was unreachable."

OUTPUT_PATH = "/output/entry.txt"

# The house gate requires /output/entry.txt to hold UTF-8 text of
# 1 to 200 characters, not only white space. Check the line against
# the same rule before writing it, so a bad line fails loudly here
# instead of silently scoring 0 in the sandbox.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"excuse is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("excuse must not be only white space")


def main() -> None:
    validate(EXCUSE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(f"Wrote {len(EXCUSE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
