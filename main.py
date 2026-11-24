#!/usr/bin/env python3
"""Write the entry sentence to /output/entry.txt."""
import os

SENTENCE = (
    "Imagine one post office for the whole world whose clerks run on lightning: "
    "a letter to China arrives in a heartbeat, and the same counter lends books, "
    "sells goods and carries your voice."
)


def main() -> None:
    assert SENTENCE.strip(), "entry must not be blank"
    assert 1 <= len(SENTENCE) <= 200, f"entry is {len(SENTENCE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)
    print(len(SENTENCE))


if __name__ == "__main__":
    main()
