#!/usr/bin/env python3
"""Entry point for the news-image-20261122 make.fun entry.

Copies the repository-held entry.png to the output directory after
validating it: it must be a real PNG, exactly 1024x1024 pixels, and no
larger than 1 MiB. Standard library only; no network, no clock, no
randomness -- two runs write identical bytes.
"""
import os
import struct
import sys

MAX_BYTES = 1048576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    target = os.path.join(out_dir, "entry.png")

    try:
        with open(source, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        return fail("cannot read entry.png: %s" % exc)

    if len(data) > MAX_BYTES:
        return fail("entry.png is %d bytes, over the 1 MiB limit" % len(data))
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return fail("entry.png is not a PNG file")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        return fail("entry.png is %dx%d, expected 1024x1024" % (width, height))

    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(target, "wb") as handle:
            handle.write(data)
    except OSError as exc:
        return fail("cannot write %s: %s" % (target, exc))

    # Read the copy back and confirm it matches byte for byte.
    try:
        with open(target, "rb") as handle:
            written = handle.read()
    except OSError as exc:
        return fail("cannot read back %s: %s" % (target, exc))
    if written != data:
        return fail("written copy of entry.png differs from the repository file")

    print("wrote %s (%dx%d PNG, %d bytes) -- copy verified byte-identical"
          % (target, width, height, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
