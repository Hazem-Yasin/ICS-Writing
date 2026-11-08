#!/usr/bin/env python3
"""Rebuild reference/ICS_Rigged_Sphere_MASTER_REFERENCE.md from the repo's .md files.

Every story/design/canon .md file is copied in verbatim (CRLF -> LF only), wrapped in
BEGIN/END FILE markers, grouped into nine parts, with an index of line numbers.
Appendix A is read from reference/appendix_a_recovered.md.

    python3 tools/build_master.py

Python standard library only. Reads the repo, writes only the one reference file.
Left out on purpose: reference/ (this file's home), tools/, and the generated
meta/INDEX, ENTITIES, LINKS and FACTS files (rebuild those with tools/build_index.py).
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "reference"
OUT = REF / "ICS_Rigged_Sphere_MASTER_REFERENCE.md"
APPENDIX = REF / "appendix_a_recovered.md"
GENERATED = {"meta/INDEX.md", "meta/ENTITIES.md", "meta/LINKS.md", "meta/FACTS.md", "meta/THREADS.md",
             "meta/OPEN.md", "meta/ACCESS.md", "meta/TIMELINE.md", "meta/LOOKUP.md"}

# Part 1 order: these first, then the rest of design/, meta/ and story/ in name order, trailers.md last.
FIRST = ["README.md", "design/DESIGN.md", "story/STORY.md", "story/EXTENDED.md", "meta/HANDOFF_CARTOGRAPHER.md"]
LAST = ["story/trailers.md"]

PARTS = [
    ("Part 1 - Core documents and game design", "PART 1 - CORE DOCUMENTS AND GAME DESIGN"),
    ("Part 2 - In-world documents (2.01-2.62)", "PART 2 - IN-WORLD DOCUMENTS (2.01-2.62)"),
    ("Part 3 - Characters", "PART 3 - CHARACTERS"),
    ("Part 4 - Facility", "PART 4 - FACILITY"),
    ("Part 5 - Scenes and scene notes", "PART 5 - SCENES AND SCENE NOTES"),
    ("Part 6 - Enemies", "PART 6 - ENEMIES"),
    ("Part 7 - Weapons and tools", "PART 7 - WEAPONS AND TOOLS"),
    ("Part 8 - Trailer scripts", "PART 8 - TRAILER SCRIPTS"),
    ("Part 9 - Internal communications", "PART 9 - INTERNAL COMMUNICATIONS"),
]
FOLDERS = [["canon/documents"], ["canon/characters"], ["canon/facility"], ["story/scenes", "story/scene-notes"],
           ["canon/enemies"], ["canon/weapons"], ["story/trailers"], ["canon/internal-communications"]]


def md_in(folder):
    return sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / folder).rglob("*.md"))


def collect():
    core = ["README.md"] + md_in("design") + md_in("meta") + ["story/STORY.md", "story/EXTENDED.md", "story/trailers.md"]
    core = [f for f in core if (ROOT / f).is_file() and f not in GENERATED]
    first = [f for f in FIRST if f in core]
    last = [f for f in LAST if f in core]
    mid = [f for f in core if f not in first and f not in last]
    groups = [first + mid + last]
    for folders in FOLDERS:
        groups.append([f for folder in folders for f in md_in(folder)])
    return groups


def read(rel):
    return (ROOT / rel).read_bytes().decode("utf-8", errors="replace").replace("\r\n", "\n").lstrip("﻿").rstrip("\n")


def header(groups, line_of):
    L = [
        "# ICS - Rigged Sphere - MASTER REFERENCE", "",
        "*One file holding everything written about the game. It replaces `WORLD.md` and `ICS - Rigged Sphere.md`, "
        "both of which were retired after a line-by-line comparison showed that their only unique text is now in Appendix A.*", "",
        "## How this file is built", "",
        "- Every story, design, canon and meta file in the repo is included **verbatim**, in the order of the index below. "
        "Nothing is paraphrased or shortened. Paths are relative to the repo root.",
        "- Each file starts with a marker line `<!-- BEGIN FILE: path -->` and ends with `<!-- END FILE: path -->`, "
        "so a file can be located or split back out.",
        "- The generated lookup files (`meta/INDEX.md`, `ENTITIES.md`, `LINKS.md`, `FACTS.md`) are not included; they are rebuilt from the files here.",
        "- `story/trailers.md` repeats the scripts that also exist one-per-file under `story/trailers/`. Both are kept.",
        "- Canon is tagged **Canon**; anything new is tagged **[PROPOSAL]** inside the files themselves.",
        "- **This file is a snapshot.** Regenerate it with `python3 tools/build_master.py`. "
        "Never edit it by hand; edit the files themselves. The lookup tools skip it so nothing is counted twice.", "",
        "## Naming rule", "",
        "**EOD** is always called EOD. Other names appear only in square brackets: [Executioner of Despair], "
        "[Envoy of Devotion], [Subjugator], [The Willbreaker], [Harmony]. 'Subjugator' is also the ARM-27 equipment codename.", "",
        "## Index (file, then line number in this master file)", "",
    ]
    for (title, _), files in zip(PARTS, groups):
        L += ["", f"**{title}**", ""]
        L += [f"- `{rel}` - line {line_of.get(rel, 0)}" for rel in files]
    L += ["", "**Appendix A - recovered text from the retired files**", "", "---", ""]
    return L


def main():
    groups = collect()
    bodies = {rel: read(rel) for g in groups for rel in g}
    appendix = read_appendix()
    line_of = {}
    for _ in range(2):  # pass 1 measures, pass 2 writes the right line numbers into the index
        L = header(groups, line_of)
        for (title, banner), files in zip(PARTS, groups):
            L += ["# " + banner, ""]
            for rel in files:
                line_of[rel] = len(L) + 1
                L += [f"<!-- BEGIN FILE: {rel} -->", ""] + bodies[rel].split("\n") + ["", f"<!-- END FILE: {rel} -->", "", "---", ""]
        L += appendix.split("\n") + [""]
    OUT.write_bytes("\n".join(L).encode("utf-8"))
    print(f"master built: {sum(len(g) for g in groups)} files, {len(L)} lines, {OUT.stat().st_size} bytes")


def read_appendix():
    return APPENDIX.read_bytes().decode("utf-8", errors="replace").replace("\r\n", "\n").lstrip("﻿").rstrip("\n")


if __name__ == "__main__":
    sys.exit(main())
