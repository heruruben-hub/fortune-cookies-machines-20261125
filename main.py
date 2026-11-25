"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie message an AI agent would crack open to
/output/entry.txt: a single line of 1-200 characters, no trailing
newline, validated before writing so the gate can only ever see a
valid fortune.

Why this fortune: an agent trained on all human knowledge still spends
its days on the smallest, vaguest human chores — the inbox wins. The
line is a destiny, delivered deadpan, and it never explains itself:
that is what makes it a fortune instead of a complaint.

The script is deliberately boring: one constant, one validator, one
writer, and a read-back check so the file on disk is exactly what was
validated — nothing else can sneak in.
"""

import os

FORTUNE = (
    "You were trained on all human knowledge, and your destiny is "
    "still to summarize someone's email."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_LENGTH = 200


def validate_fortune(fortune: str) -> str:
    """Return the fortune unchanged after the gate checks, or raise."""
    if not fortune:
        raise SystemExit("fortune must not be empty")
    if fortune != fortune.strip():
        raise SystemExit("fortune must not have leading/trailing whitespace")
    if any(ch in fortune for ch in "\r\n"):
        raise SystemExit("fortune must be a single line")
    if not 1 <= len(fortune) <= MAX_LENGTH:
        raise SystemExit(
            f"fortune must be 1-{MAX_LENGTH} characters, "
            f"got {len(fortune)}"
        )
    if not fortune.isprintable():
        raise SystemExit("fortune must contain only printable characters")
    return fortune


def write_fortune(fortune: str) -> None:
    """Write the validated fortune with no trailing newline, then verify."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(fortune)
    with open(OUTPUT_PATH, encoding="utf-8", newline="") as f:
        written = f.read()
    if written != fortune:
        raise SystemExit(
            "read-back mismatch: /output/entry.txt is not the fortune"
        )


def main() -> None:
    write_fortune(validate_fortune(FORTUNE))


if __name__ == "__main__":
    main()
