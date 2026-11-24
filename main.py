#!/usr/bin/env python3
"""Write one original office joke to /output/entry.txt."""

JOKE = "I hit reply-all to ask everyone to stop replying all, and now 400 people are replying all to agree with me."

OUTPUT_PATH = "/output/entry.txt"


def validate(joke: str) -> str:
    text = joke.strip()
    if not text:
        raise ValueError("joke must not be empty")
    if len(text) > 200:
        raise ValueError("joke must be at most 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    return text


def write_entry(text: str) -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    write_entry(validate(JOKE))


if __name__ == "__main__":
    main()
