"""Everyday Wonder — one sentence of everyday wonder.

Writes a single sentence about a small moment of wonder in everyday
life to /output/entry.txt, then reads it back and asserts the content
matches exactly (round-trip check). Stdlib only, deterministic.
"""

import os

ENTRY = (
    "The elevator doors opened on the wrong floor, and a toddler in "
    "dinosaur pajamas waved at me like we had known each other for years."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY, "round-trip mismatch in entry.txt"
    assert 1 <= len(content) <= 200, "entry must be 1-200 characters"
    assert content.strip(), "entry must not be only whitespace"
    assert "\n" not in content, "entry must be a single line"
    assert content.endswith(".") and content.count(".") == 1, (
        "entry must be exactly one sentence"
    )


if __name__ == "__main__":
    main()
