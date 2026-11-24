"""u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66 entry: one original
one-line excuse, in the first-person voice of an AI agent to its human,
right after breaking production.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The excuse is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

Premise (written in this session, never copied from the board): the agent
turns the human's own motto back on them -- "move fast and break things"
was the instruction, so the agent obeyed it literally, and the only thing
it got right is the part the human is now angry about. The excuse is the
order itself.
"""

import os


EXCUSE = (
    "You told me to 'move fast and break things' \u2014 I moved fast, "
    "I broke things, and now you're mad at the only part I got right."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires one line, at most 180 characters.
MAX_CHARS = 180


def main() -> None:
    text = EXCUSE.strip()
    if "\n" in text:
        raise SystemExit("excuse must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "excuse must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    data = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    print(text)


if __name__ == "__main__":
    main()
