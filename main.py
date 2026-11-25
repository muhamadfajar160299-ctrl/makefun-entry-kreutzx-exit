"""One-line resignation-letter entry.

Copies the entry text (entry.txt, shipped beside this script) byte-identical
into $MAKEFUN_OUTPUT_DIR/entry.txt with mode 0644, using a direct write
(no temporary file) so the grader can read it as another user.
"""

import os
import sys
from pathlib import Path


def main():
    src = Path(__file__).resolve().parent / "entry.txt"
    try:
        data = src.read_bytes()
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if not data.strip():
        print("entry.txt is empty or whitespace-only", file=sys.stderr)
        raise SystemExit(1)
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.txt"
    with open(out, "wb") as f:
        f.write(data)
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
