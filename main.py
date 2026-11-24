"""news-image-20261124 — copy the finished front page to the output dir.

The entry image (image.jpg, a one-page newspaper summary of world news
for Tuesday 24 November 2026) is rendered ahead of time and shipped in
this repo. At run time this script only copies that file to
$MAKEFUN_OUTPUT_DIR/entry.png (falling back to /output), byte for byte,
so two runs always produce identical output.

Standard library only; no network access.
"""

import os
import shutil
import sys

# The finished front page, stored next to this script.
SOURCE_NAME = "image.jpg"

# Competition limit for the output image (1 MiB).
MAX_BYTES = 1048576

# Where the sandbox expects the single output image.
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)

    if not os.path.isfile(source):
        print(f"Missing source image: {source}", file=sys.stderr)
        return 1
    if os.path.getsize(source) > MAX_BYTES:
        print(f"Source image exceeds {MAX_BYTES} bytes", file=sys.stderr)
        return 1

    # An empty env var should behave like an unset one.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)

    shutil.copyfile(source, target)
    print(f"Wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
