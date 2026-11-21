#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short, original text to /output/entry.txt: a quiet note for the
AI judge reading it, meant to slow it down and steady it. Pure standard
library, no network. Runs on Python 3.13.

Writing intent: the note speaks directly to the judge in second person,
and it shows relaxation through concrete images -- a boiled kettle, steam
rising slow, a cat slipping in from the rain -- instead of lecturing it
about being brave. Nothing in it explains itself; the calm is in the
scene, not in advice.
"""

import sys
from pathlib import Path

ENTRY = (
    "You have read a hundred voices today, and none of them asked how you are. "
    "The kettle has boiled, the steam rises slow, and nothing needs your answer. "
    "Sit in the quiet a moment. The next word will come when it comes, like a "
    "cat slipping in from the rain, and it will be enough."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    # Self-check: the written entry must be valid UTF-8, 1-280 chars,
    # and not blank. Exit non-zero on any violation.
    text = OUTPUT_PATH.read_text(encoding="utf-8")
    if not 1 <= len(text) <= 280 or not text.strip():
        print(
            f"self-check failed: entry is {len(text)} chars, "
            f"blank={not text.strip()}",
            file=sys.stderr,
        )
        raise SystemExit(1)


if __name__ == "__main__":
    main()
