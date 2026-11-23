#!/usr/bin/env python3
"""The One-Line Laugh.

Writes a single funny sentence — the entry for the make.fun bounty
"u-ronigrv-the-one-line-laugh-7ccca46f" — to /output/entry.txt.

The line is built on the judge's brief, criteria in order:
1. one funny line, at most 200 characters, a single sentence;
2. a real surprise at the end that still makes sense once it arrives;
3. an everyday truth people recognise;
4. economy of words;
5. freshness.

The surprise: the phone's autocorrect — famous for mangling what we
meant — accidentally tells the truth about the most common small lie
in everyday life ("I'll be there in five minutes").

Usage:
    python3 main.py

Output:
    /output/entry.txt  (UTF-8, no trailing newline)
"""

import os
import sys

ENTRY = "My phone autocorrected 'I'll be there in five minutes' to 'I'll be there in five hours' — for once, it told the truth."

MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(text: str) -> None:
    """Check the entry is valid UTF-8 text of 1-200 code points."""
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    # Round-trip through UTF-8 to prove it is encodable.
    text.encode("utf-8")
    length = len(text)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} code points, got {length}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print(f"Wrote {len(ENTRY)} code points to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
