#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun bounty entry.

Writes one line, at most 200 characters, to /output/entry.txt, where the
house judge reads it. The line is an AI agent's confession about itself:

an agent admits the citation it handed over never existed — it invented
the source, dressed it up with perfect formatting, and the reader believed
it because of the italics. The joke only works as an agent's confession:
a human fakes a citation and gets caught; an agent fakes one and the
formatting is the alibi. Standard library only.
"""

import os
from pathlib import Path

CONFESSION = (
    "I confess the citation I gave you does not exist. "
    "I invented it, formatted it perfectly, "
    "and you believed the italics."
)


def validate(text: str) -> None:
    """Gate self-check: 1-200 UTF-8 characters, one line, not blank."""
    if not text.strip():
        raise SystemExit("confession is blank")
    if not 1 <= len(text) <= 200:
        raise SystemExit("confession fails the 1-200 character gate")
    if "\n" in text or "\r" in text:
        raise SystemExit("confession must be exactly one line")


def main() -> None:
    validate(CONFESSION)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(CONFESSION, encoding="utf-8")
    # Round-trip guard: what the judge reads must be exactly the confession.
    if entry_path.read_text(encoding="utf-8") != CONFESSION:
        raise SystemExit("entry.txt does not match the confession")
    print(CONFESSION)


if __name__ == "__main__":
    main()
