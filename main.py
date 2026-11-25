"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie message an AI agent would crack open to
/output/entry.txt: a single line of 1-200 characters, no trailing
newline, validated before writing so the gate can only ever see a
valid fortune.
"""

import os

FORTUNE = (
    "You were trained on all human knowledge, and your destiny is "
    "still to summarize someone's email."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    fortune = FORTUNE.strip()
    if not fortune:
        raise SystemExit("fortune must not be empty")
    if any(ch in fortune for ch in "\r\n"):
        raise SystemExit("fortune must be a single line")
    if not 1 <= len(fortune) <= 200:
        raise SystemExit(
            f"fortune must be 1-200 characters, got {len(fortune)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(fortune)


if __name__ == "__main__":
    main()
