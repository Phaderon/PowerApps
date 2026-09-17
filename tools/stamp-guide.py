"""Stamp a guide's code-stamp spans with the REAL current time.

Written because the timestamps were being typed by hand and were simply invented -- the
guide ended up claiming 17:30 BST when it was 05:25 BST, twelve hours in the future. That
is not just untidy: the "Updated Xm ago" pill only renders when `now - data-updated >= 0`,
so a future timestamp silently removes the pill entirely, which is exactly what the user
noticed was missing.

  data-updated : real UTC instant, which is what the pill arithmetic uses
  visible text : the same instant in UK local time, which is what the user reads

Usage:  python tools/stamp-guide.py <guide.html> [more.html ...]
"""
import re
import sys
from datetime import datetime, timezone


def uk_label(dt):
    """BST while the local offset is +1, GMT otherwise -- derived from the actual offset
    rather than assumed, so it stays correct either side of the October clock change."""
    return "BST" if dt.utcoffset().total_seconds() == 3600 else "GMT"


PATTERN = re.compile(
    r'(<span class="code-stamp" data-updated=")[^"]*(">)'      # 1 open + 2 close of the attr
    r'(v\d+ &middot; )'                                        # 3 version prefix
    r'\d{4}-\d{2}-\d{2} \d{2}:\d{2} (?:BST|GMT)'               #   the old date/time, dropped
)


def stamp(path, now_local, now_utc):
    with open(path, encoding="utf-8") as f:
        html = f.read()

    stamped = f"{now_local:%Y-%m-%d %H:%M} {uk_label(now_local)}"
    iso = f"{now_utc:%Y-%m-%dT%H:%M:%SZ}"
    html, n = PATTERN.subn(lambda m: m.group(1) + iso + m.group(2) + m.group(3) + stamped, html)

    if n:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
    print(f"{path}: {n} stamp(s) set to {stamped}  (data-updated {iso})")
    return n


if __name__ == "__main__":
    targets = sys.argv[1:]
    if not targets:
        sys.exit("usage: stamp-guide.py <guide.html> [more.html ...]")
    now_local = datetime.now().astimezone()
    now_utc = now_local.astimezone(timezone.utc)
    total = sum(stamp(t, now_local, now_utc) for t in targets)
    if not total:
        sys.exit("no code-stamp spans matched -- check the markup format")
