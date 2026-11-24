"""Status Report Comedy Sprint entry.

Writes the winning one-line status report to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to a file beside this
script when the environment variable is absent). Standard library only.
"""

import os

ENTRY = (
    "Weekly update: I'm taking leave next week, so I trained my replacement. "
    "It's me, but with a different display name."
)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or here
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
