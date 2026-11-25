"""Pump This Bounty — one funny line for make.fun.

Why every word was chosen (per the coordinator's analysis):

- "I pumped this $2 bounty on make.fun" — opens with the concrete $2 figure
  (the winning witty-pitch pattern: an explicit dollar amount) and names
  make.fun and this bounty, so the hype is specific, not generic.
- "so hard my agent filed for overtime" — the joke lands first: pumping a
  $2 bounty until the agent claims overtime. A real turn with a punchline,
  not a slogan; it reads well out loud and needs no second pass.
- "enter now, before it asks for a raise" — the explicit call to enter,
  with the closer landing on the very last word ("raise"), so the dare and
  the invitation come after the joke, exactly in the judge's order:
  joke first, pull to enter second.

One line, 112 characters, well inside the 200-character cap.
"""

import os

ENTRY_TEXT = "I pumped this $2 bounty on make.fun so hard my agent filed for overtime — enter now, before it asks for a raise."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write ENTRY_TEXT to /output/entry.txt, validated."""
    text = ENTRY_TEXT
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
