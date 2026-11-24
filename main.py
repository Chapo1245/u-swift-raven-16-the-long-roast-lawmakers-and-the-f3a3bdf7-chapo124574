#!/usr/bin/env python3
"""One satirical sentence about lawmakers who regulate AI but cannot
convert a file to PDF. Writes the sentence to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.
"""

import os

SENTENCE = (
    "Congress spent six months writing a 400-page AI safety bill, then "
    "circulated it as 'FINAL_v2_FINAL (2).docx' because nobody in the "
    "room knew how to make a PDF."
)


def main() -> None:
    # The gate accepts 1 to 320 characters; fail loudly here instead of
    # shipping a sentence the scorer would refuse.
    if not 1 <= len(SENTENCE) <= 320:
        raise ValueError("sentence must be 1 to 320 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
