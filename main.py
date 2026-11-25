#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun bounty entry.

The entry is a single line, 200 characters or fewer, that lands entirely
on its own: no title, no setup, no explanation around it. Running this
module prints the line and nothing else.
"""

LINE = "My microwave popcorn unionized mid-pop — demands: butter, weekends off, and one kernel of respect."

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the bounty form: one line, 200 characters or fewer."""
    if not line:
        raise ValueError("line must not be empty")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the {MAX_CHARS} limit")


def main() -> None:
    validate(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
