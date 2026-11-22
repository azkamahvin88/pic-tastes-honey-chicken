"""Copy the honey-glazed fried chicken entry image to the output dir.

The program locates ``entry.png`` next to this file and copies it to
``$MAKEFUN_OUTPUT_DIR/entry.png`` (or ``/output/entry.png`` when the
variable is not set). Python 3.13, standard library only, no network.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        # Fail loudly: a missing source image means the entry has no
        # picture at all, so never silently produce an empty output.
        print(f"error: entry.png not found next to main.py ({here})", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"

    shutil.copyfile(source, destination)
    size = destination.stat().st_size
    print(f"wrote {destination} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
