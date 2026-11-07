#!/usr/bin/env python3
"""Repair mojibake (text saved with the wrong encoding) in the repo's .md files.

Four sequences are known damage, each the UTF-8 bytes of a real character shown as Windows-1252:
    em dash, right arrow, en dash, degree sign
Only those four are replaced. Line endings (CRLF or LF) are kept exactly as they are.

    python3 tools/fix_encoding.py            list the files that have damage (changes nothing)
    python3 tools/fix_encoding.py --write    repair them

Skips .git, the generated meta files (INDEX, ENTITIES, LINKS, FACTS) and the pasted master
reference; rebuild those with tools/build_index.py and tools/build_master.py instead.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Left side: the damaged text. Right side: the character it should be.
FIXES = {
    "â€”": "—",  # em dash
    "â†’": "→",  # right arrow
    "â€“": "–",  # en dash
    "Â°": "°",        # degree sign
}
SKIP = {"meta/HANDOFF_CARTOGRAPHER.md",  # describes the damage in prose; edited by hand
        "meta/INDEX.md", "meta/ENTITIES.md", "meta/LINKS.md", "meta/FACTS.md",
        "reference/ICS_Rigged_Sphere_MASTER_REFERENCE.md"}


def main():
    write = "--write" in sys.argv
    total = 0
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if ".git" in p.parts or rel in SKIP:
            continue
        raw = p.read_bytes()
        text = raw.decode("utf-8")
        new, n = text, 0
        for bad, good in FIXES.items():
            c = new.count(bad)
            if c:
                n += c
                new = new.replace(bad, good)
        if n:
            total += n
            print(f"{n:4d}  {rel}")
            if write:
                p.write_bytes(new.encode("utf-8"))  # bytes, so CRLF is untouched
    print(f"{total} damaged sequences" + (" repaired" if write else " found (run with --write to repair)"))


if __name__ == "__main__":
    main()
