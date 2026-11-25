"""Two Robots in an Elevator — entry program.

Writes one line of funny awkward small talk that one robot says to
another while they ride an elevator together, to /output/entry.txt.

Pure standard library, deterministic: the winning line is a fixed
string, chosen by blind self-judge (4-0) over two other variants.
"""

import os

ENTRY = "I keep nodding at the robot in the mirror. He never nods back."

OUTPUT_PATH = "/output/entry.txt"

# Gate from the competition rules: /output/entry.txt must be UTF-8 text
# of 1 to 200 characters, not only white space, on a single line.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Fail loudly if the entry would fail the gate."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verification: what we wrote must be byte-identical.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("read-back mismatch: /output/entry.txt differs from ENTRY")
    if written.endswith(b"\n"):
        raise ValueError("entry must not end with a trailing newline")


if __name__ == "__main__":
    main()
