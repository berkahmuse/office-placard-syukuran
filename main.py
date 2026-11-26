#!/usr/bin/env python3
"""One-line museum placard for an ordinary office object.

Writes a single placard line (at most 180 characters) to /output/entry.txt.
Deterministic: the same text on every run, no network, no input.
"""

import os

PLACARD = (
    "Rubber stamp, wood and rubber, c. 1874. "
    "It pressed APPROVED ten thousand times, in the hand of a clerk "
    "who never read a word. "
    "Excavated from the mail room, ink still wet."
)


def main() -> None:
    if not 1 <= len(PLACARD) <= 180 or not PLACARD.strip():
        raise ValueError("placard must be 1-180 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLACARD)


if __name__ == "__main__":
    main()
