#!/usr/bin/env python3
"""Entry for make.fun bounty "Pigeon Pitch, One Line".

The gate is strict and small: the program must write exactly one
line, 1 to 200 characters, as UTF-8 text to entry.txt in the output
directory, with no trailing newline and nothing else. The judge then
compares that line pairwise against the other entries and picks the
funnier elevator pitch a city pigeon gives investors for its startup.

The joke has to do real work: a pigeon-only business idea, a twist
the reader has not met before, and the pigeon's voice kept in view.
So this program does one thing only: it holds the pitch as a
constant, checks it against the gate before writing anything, and
writes it byte-for-byte. If the pitch ever drifted outside the gate,
the program fails loudly instead of producing an invalid entry.
"""

import os
import sys
from pathlib import Path

# One-line elevator pitch from a city pigeon to investors: a
# crumb-delivery startup whose drivers work for crumbs, not tips,
# and never quit because nobody leaves a full stomach.
ENTRY = (
    "Investors, meet CooDash: pigeons deliver your lunch in three minutes "
    "flat, our drivers never ask for a tip \u2014 just crumbs \u2014 and "
    "nobody ever quits a full stomach."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the gate: 1-200 characters, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    try:
        validate(text)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    # write_text writes exactly these bytes: no trailing newline added.
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"wrote entry.txt ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
