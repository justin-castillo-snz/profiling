"""Check relative Markdown links and heading anchors in AGENTS.md and wiki/, and that every wiki page is indexed.

Run from the repository root:  python .github/skills/ingest-source/check_links.py
Exit code 1 if any problem is found.
"""
import glob
import os
import re
import sys
from urllib.parse import unquote

LINK = re.compile(r"\]\(<?([^)>\s]+)>?\)")


def slug(heading):
    text = re.sub(r"^#+", "", heading).strip().lower()
    text = re.sub(r"[`*_]", "", text)
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path, cache={}):
    if path not in cache:
        with open(path, encoding="utf-8") as fh:
            cache[path] = {slug(l) for l in fh.read().splitlines() if l.startswith("#")}
    return cache[path]


def main():
    files = ["AGENTS.md"] + glob.glob("wiki/**/*.md", recursive=True)
    problems, count = [], 0
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        for m in LINK.finditer(text):
            link = m.group(1)
            if re.match(r"^[a-z]+:", link):
                continue
            count += 1
            path, _, anchor = unquote(link).partition("#")
            target = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
            if not os.path.exists(target):
                problems.append(f"BROKEN  {f}: {link}")
            elif anchor and target.endswith(".md") and anchor not in anchors(target):
                problems.append(f"ANCHOR  {f}: {link}")

    with open("wiki/index.md", encoding="utf-8") as fh:
        index = unquote(fh.read())
    for page in glob.glob("wiki/**/*.md", recursive=True):
        rel = os.path.relpath(page, "wiki").replace("\\", "/")
        if rel not in ("index.md", "log.md") and rel not in index:
            problems.append(f"UNINDEXED  {page}")

    print("\n".join(problems) if problems else "OK", f"({count} links checked)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
