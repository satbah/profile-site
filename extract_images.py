#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-time (well, re-runnable) refactor: pull the 13 base64-embedded
images out of index.html into assets/*.webp, and replace each data: URI
with a relative src="assets/....webp" path.

Why: index.html was ~900KB, ~90% of it base64 image data on a handful of
absurdly long lines, making it painful to edit in a plain text editor.
After this, index.html is just markup + text (~85KB) and images are
normal files a browser can cache independently.

Safe to re-run: if an image's base64 content is unchanged, its output
filename+content is identical, so re-running after unrelated text edits
is a no-op for images.
"""
import base64
import hashlib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "index.html")
ASSETS_DIR = os.path.join(HERE, "assets")

# Order matches the images' appearance in index.html (verified against
# surrounding class context before writing this).
NAMES = [
    "hero-backdrop",
    "ask-icon-research-tools",
    "ask-icon-ai-connect",
    "ask-icon-ai-llm",
    "ask-icon-sensor-iot",
    "ask-icon-debug",
    "work-mcp-server",
    "work-ai3d-character",
    "work-bluetooth-pan",
    "work-vr-headset",
    "work-messaging-bot",
    "work-industrial-line",
    "publications-archive",
]

DATA_URI_RE = re.compile(r'data:image/(\w+);base64,([A-Za-z0-9+/=]+)')


def main():
    html = open(SRC, encoding="utf-8").read()
    os.makedirs(ASSETS_DIR, exist_ok=True)

    matches = list(DATA_URI_RE.finditer(html))
    if len(matches) != len(NAMES):
        raise SystemExit(
            f"Expected {len(NAMES)} embedded images, found {len(matches)}. "
            f"The page structure changed — update NAMES in this script to match "
            f"the new order before re-running (don't guess; check context like "
            f"the original run did)."
        )

    # Replace back-to-front so earlier match spans stay valid as we edit.
    for name, m in zip(reversed(NAMES), reversed(matches)):
        ext, b64 = m.group(1), m.group(2)
        data = base64.b64decode(b64)
        fname = f"{name}.{ext}"
        with open(os.path.join(ASSETS_DIR, fname), "wb") as f:
            f.write(data)
        html = html[:m.start()] + f"assets/{fname}" + html[m.end():]

    with open(SRC, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"wrote {len(NAMES)} files to assets/, index.html is now {len(html)} bytes "
          f"(was {sum(m.end()-m.start() for m in matches) + len(html)} bytes)")


if __name__ == "__main__":
    main()
