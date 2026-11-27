#!/usr/bin/env python3
"""Build consolidated_guide.md from the files listed in build/manifest.txt.

    python3 build/build_consolidated.py            # write consolidated_guide.md
    python3 build/build_consolidated.py --check    # exit 1 if it is out of date

The manifest holds one repo-relative path per line, in reading order; `#` starts a
comment and blank lines are ignored. Each file is copied under a `---` separator and
a heading naming its path, with its own headings demoted one level (outside fenced
code) and its front-matter shown as a YAML code block. The output contains no date,
so rebuilding unchanged sources gives an identical file.

--check also fails when a markdown file in the repository is missing from the
manifest (consolidated_guide.md, .git, releases/, tests/ and examples/ are excluded).
Standard library only; Python 3.9+.
"""

import argparse
import os
import re
import sys

TITLE = "# Application Documentation Framework – Consolidated Guide"
NOTE = ("Generated from source files by build/build_consolidated.py. "
        "Do not edit; edit the source files and regenerate.")
OUTPUT = "consolidated_guide.md"
EXCLUDED_DIRS = {".git", "releases", "tests", "examples"}


def read_manifest(root):
    paths = []
    with open(os.path.join(root, "build", "manifest.txt"), encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if line:
                paths.append(line)
    return paths


def slug(text):
    """GitHub-style heading anchor."""
    return re.sub(r"[^\w\- ]", "", text.strip().lower()).replace(" ", "-")


def demote(text):
    lines = text.splitlines()
    out, start = [], 0
    if lines and lines[0].strip() == "---":
        for end in range(1, len(lines)):
            if lines[end].strip() == "---":
                out += ["```yaml"] + lines[1:end] + ["```"]
                start = end + 1
                break
    fence = None
    for line in lines[start:]:
        s = line.lstrip()
        m = re.match(r"(`{3,}|~{3,})", s)
        if fence:
            if m and s.startswith(fence) and not s.lstrip(fence[0]).strip():
                fence = None
        elif m:
            fence = m.group(1)
        elif re.match(r"#{1,5}\s", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out).strip("\n")


def build(root, paths):
    parts = [TITLE, "", NOTE, "", "## Contents", ""]
    parts += ["- [%s](#%s)" % (p, slug(p)) for p in paths]
    for p in paths:
        with open(os.path.join(root, p), encoding="utf-8") as fh:
            body = demote(fh.read())
        parts += ["", "---", "", "# %s" % p, "", body]
    return "\n".join(parts) + "\n"


def unlisted(root, paths):
    listed, found = set(paths), []
    for dirpath, dirnames, fnames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir.split(os.sep)[0] in EXCLUDED_DIRS:
            dirnames[:] = []
            continue
        dirnames.sort()
        for n in sorted(fnames):
            rel = os.path.normpath(os.path.join(rel_dir, n)).replace(os.sep, "/")
            if n.endswith(".md") and rel != OUTPUT and rel not in listed:
                found.append(rel)
    return found


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if consolidated_guide.md is out of date or the manifest is incomplete")
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    help="framework repository root (default: parent of build/)")
    args = ap.parse_args(argv)
    root = args.root
    try:
        paths = read_manifest(root)
    except OSError as exc:
        print("build_consolidated: cannot read manifest: %s" % exc, file=sys.stderr)
        return 1
    missing = [p for p in paths if not os.path.isfile(os.path.join(root, p))]
    extra = unlisted(root, paths)
    problems = []
    if missing:
        problems.append("Files in the manifest that do not exist: " + ", ".join(missing))
    if extra and args.check:
        problems.append("Markdown files missing from build/manifest.txt: " + ", ".join(extra))
    elif extra:
        print("warning: not in build/manifest.txt: " + ", ".join(extra), file=sys.stderr)
    if missing:
        print("\n".join(problems), file=sys.stderr)
        return 1
    text = build(root, paths)
    out = os.path.join(root, OUTPUT)
    if args.check:
        try:
            with open(out, encoding="utf-8") as fh:
                current = fh.read()
        except OSError:
            current = None
        if current != text:
            problems.append("%s is out of date; run python3 build/build_consolidated.py" % OUTPUT)
        if problems:
            print("\n".join(problems), file=sys.stderr)
            return 1
        print("%s is up to date." % OUTPUT)
        return 0
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("Wrote %s from %d files." % (OUTPUT, len(paths)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
