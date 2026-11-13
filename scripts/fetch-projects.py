#!/usr/bin/env python3
"""Refresh project stats, and optionally images, for the projects page.

Reads the cards in content/pages/projects.md, fetches GitHub stars and crates.io
downloads/versions, and writes data/projects.json. By default each card keeps the
image already recorded there, so scheduled runs only touch the stats.

With --images it also rebuilds every card's image from an explicit `image` URL, a
local capture in scripts/captures/ (`image = "captures/name.png"`), or the site's
og:image. Stills become WebP and animated GIFs become looping MP4s, written to
static/projects/. Run this locally after adding a card or changing an image.

Requires `gh` (authenticated) for GitHub data, plus `cwebp` and `ffmpeg` for
--images. Run from the repo root:

    python3 scripts/fetch-projects.py [--images]
"""

import argparse
import json
import re
import subprocess
import tempfile
import tomllib
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "content/pages/projects.md"
DATA = ROOT / "data/projects.json"
IMAGES = ROOT / "static/projects"
CAPTURES = ROOT / "scripts/captures"
SITE = "https://www.joshka.net"
UA = {"User-Agent": "joshka.net projects page (https://www.joshka.net)"}


def front_matter():
    text = PAGE.read_text()
    return tomllib.loads(text.split("+++")[1])


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read()


def github(repo_url):
    slug = repo_url.removeprefix("https://github.com/")
    out = subprocess.run(
        ["gh", "api", f"repos/{slug}", "--jq", "{stars: .stargazers_count, pushed: .pushed_at}"],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)


def crate(name):
    c = json.loads(get(f"https://crates.io/api/v1/crates/{name}"))["crate"]
    return {"downloads": c["downloads"], "version": c["max_stable_version"] or c["max_version"]}


def og_image(url):
    html = get(url).decode("utf-8", "replace")
    m = re.search(r'<meta[^>]+(?:property|name)="(?:og|twitter):image"[^>]+content="([^"]+)"', html)
    return m and m.group(1)


def save_image(name, source):
    if source.startswith("captures/"):
        src = CAPTURES / source.removeprefix("captures/")
    else:
        src = Path(tempfile.mkdtemp()) / (Path(source.split("?")[0]).name or "image.png")
        src.write_bytes(get(source))
    if src.suffix.lower() == ".gif":
        # Animated demos become looping MP4s: roughly a tenth of the GIF's size.
        out = IMAGES / f"{name}.mp4"
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(src),
               "-vf", "fps=12,scale=720:-2:flags=lanczos", "-an", "-c:v", "libx264",
               "-pix_fmt", "yuv420p", "-crf", "28", "-movflags", "+faststart", str(out)]
    else:
        out = IMAGES / f"{name}.webp"
        cmd = ["cwebp", "-quiet", "-q", "82", "-resize", "1200", "0", str(src), "-o", str(out)]
    subprocess.run(cmd, check=True)
    return f"projects/{out.name}"


def short(n):
    for div, unit in ((1_000_000, "M"), (1_000, "k")):
        if n >= div:
            return f"{n / div:.1f}".rstrip("0").rstrip(".") + unit
    return str(n)


def short_floor(n):
    """Round down to a headline figure, e.g. 70844368 -> 70M+."""
    for div, unit in ((1_000_000, "M"), (1_000, "k")):
        if n >= div:
            return f"{n // div}{unit}+"
    return str(n)


def fetch(card, shared_repos, previous, images):
    name = card["name"]
    entry = {}
    if "repo" in card and card["repo"].startswith("https://github.com/"):
        entry.update(github(card["repo"]))
        if card["repo"] in shared_repos:
            # Stars belong to the whole repo, not this crate.
            entry.pop("stars")
    if "crate" in card:
        entry.update(crate(card["crate"]))
    for key in ("stars", "downloads"):
        if key in entry:
            entry[f"{key}_short"] = short(entry[key])
            entry[f"{key}_floor"] = short_floor(entry[key])
    if not images:
        if "image" in previous:
            entry["image"] = previous["image"]
        print(f"{name}: {entry}")
        return entry
    image = card.get("image")
    if not image and card.get("url"):
        url = card["url"] if card["url"].startswith("http") else SITE + card["url"]
        image = og_image(url)
    if image:
        entry["image"] = save_image(re.sub(r"\W+", "-", name.lower()), image)
    print(f"{name}: {entry}")
    return entry


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--images", action="store_true", help="rebuild card images too")
    args = parser.parse_args()
    previous = json.loads(DATA.read_text()) if DATA.exists() else {}
    fm = front_matter()
    IMAGES.mkdir(parents=True, exist_ok=True)
    DATA.parent.mkdir(parents=True, exist_ok=True)
    cards = [fm["extra"]["ratatui"]] + [c for g in fm["extra"]["groups"] for c in g.get("cards", [])]
    repos = [c.get("repo") for c in cards]
    shared = {r for r in repos if r and repos.count(r) > 1}
    data = {}
    for c in cards:
        prev = previous.get(c["name"], {})
        try:
            data[c["name"]] = fetch(c, shared, prev, args.images)
        except Exception as e:  # keep the last good entry rather than failing the whole refresh
            print(f"{c['name']}: kept previous entry ({e})")
            data[c["name"]] = prev
    DATA.write_text(json.dumps(data, indent=2) + "\n")


if __name__ == "__main__":
    main()
