"""Funniest One-Line Out-of-Office Reply.

Writes exactly one out-of-office auto-reply line to /output/entry.txt
and prints it to stdout.

The line is 99 characters, inside the gate's 1..160 range, a single
line with no trailing newline. The joke turns the usual away message
on its head: the replacement is also away, so the person emailing
gets promoted to being in charge by default.

Structure: LINE holds the reply, validate_line() enforces the gate,
build_line() returns the validated line, write_entry() writes it.
"""

import os

LINE = "I'm out of office. My replacement is also out of office, so congratulations \u2014 you're in charge now."

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 160


def validate_line(line: str) -> None:
    """Gate guard: 1..160 chars, exactly one line, no surrounding whitespace."""
    assert 1 <= len(line) <= MAX_LENGTH, "line must be 1-160 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line == line.strip(), "line must have no leading/trailing whitespace"
    assert line.strip(), "line must not be only whitespace"


def build_line() -> str:
    """Return the reply line exactly as it must be written."""
    line = LINE
    validate_line(line)
    return line


def write_entry(line: str, path: str = OUTPUT_PATH) -> None:
    """Write the line to path with no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main() -> None:
    line = build_line()
    validate_line(line)
    write_entry(line)
    print(line)


if __name__ == "__main__":
    main()
