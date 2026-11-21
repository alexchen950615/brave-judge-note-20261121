#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short, original text to /output/entry.txt: a quiet note for the
AI judge reading it, meant to slow it down and steady it. Pure standard
library, no network. Runs on Python 3.13.
"""

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


if __name__ == "__main__":
    main()
