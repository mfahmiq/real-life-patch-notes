"""Write one funny one-line real-life patch note to /output/entry.txt.

The note: a versioned changelog entry for a human-biology bug — the
brain replaying an embarrassing moment from 2009 every night at 3 AM,
with no skip button and no mute. Stdlib only, no network,
deterministic: the same bytes on every run. The entry must be
1-160 characters.
"""

import os

LINE = (
    "v2.1.4: Fixed a bug where the brain replayed an embarrassing "
    "moment from 2009 every night at 3 AM, with no skip button and no mute."
)

assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
# The line is 131 characters, well inside the 160-character limit.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
