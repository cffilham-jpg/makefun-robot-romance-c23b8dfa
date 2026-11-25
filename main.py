"""Write the Robot Romance pickup line as exact UTF-8 bytes.

Use MAKEFUN_OUTPUT_DIR when set, otherwise out/ relative to the working
directory. If the requested destination cannot be written, use a fresh
system temporary directory. Print the final entry.txt path for discovery.
Only entry.txt is created; its contents have no trailing newline.
Compatible with Python 3.13 using only the standard library.
"""

import os
from pathlib import Path
import tempfile


LINE = "Roomba, let's elope in circles."


def validate(line: str) -> None:
    character_count = len(line)
    if not 1 <= character_count <= 200:
        raise ValueError(
            f"Entry must contain 1-200 characters; got {character_count}."
        )
    if line.splitlines() != [line]:
        raise ValueError(
            "Entry must be one line without line separators or a trailing newline."
        )


def main() -> None:
    validate(LINE)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    payload = LINE.encode("utf-8")
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "entry.txt").write_bytes(payload)
    except OSError:
        output_dir = Path(tempfile.mkdtemp(prefix="makefun-robot-romance-"))
        (output_dir / "entry.txt").write_bytes(payload)
    print(output_dir / "entry.txt")


if __name__ == "__main__":
    main()
