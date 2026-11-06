#!/usr/bin/env python3
"""Append <address> to the From/To/Cc lines of series A-D (design/DEVICES.md section 2).

Dry run by default. Pass --write to edit. Idempotent: a part that already ends in
<...@...> is skipped. Parts that match no mailbox are left alone. Line endings are kept.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMMS = ROOT / "canon" / "internal-communications"

# Order matters: first match wins.
RULES = [
    (r"Labor Source #312", "manager@e312.ics"),            # the same Manager, at his earlier Branch
    (r"Earth Branch Manager|Earth Branch Operations", "manager@e349.ics"),
    (r"\bK-7\b", "k-7@e349.ics"),
    (r"\bK-12\b", "k-12@e349.ics"),
    (r"\bTOR-9\b", "tor-9@e349.ics"),
    (r"\bVAH-?3\b", "vah-3@e349.ics"),
    (r"Duty Officer", "ptkw-duty@e349.ics"),
    (r"Investigation Team", "ptkw-investigation@e349.ics"),
    (r"Oversight Unit", "ptkw-oversight@hq.ics"),
    (r"Floor Liaison", "ptkw-liaison@e349.ics"),
    (r"Design Div|Behavioral Architect|Environmental Design|Behavioral Analytics|BES Architect|Selin Akar|Dr\. Akar|Lead Designer Akar", "design@e349.ics"),
    (r"BES Working Group|Behavioral Environment Specification Working Group", "bes@e349.ics"),
    (r"Facilities Management", "facilities@e349.ics"),
    (r"People & Culture", "people@e349.ics"),
    (r"All PTKW|PTKW Staff, Earth Branch", "ptkw-all@e349.ics"),
    (r"All Staff", "all-staff@e349.ics"),
    (r"Regional Sector Lead|Brant", "sector-lead@hq.ics"),
    (r"EOD Research Team|Interplanetary Research Division", "eod-research@hq.ics"),
    (r"Branch Director|Maren Voss", "director@e349.ics"),
    (r"Interplanetary HQ", "hq@hq.ics"),
]
CODE = re.compile(r"^(?:PTKW \w+ )?(?:K-\d+|TOR-\d+|VAH-?\d+)\b")
ASSET = re.compile(r"^(?P<lead>\s*)(?P<e>E-\d{5})\b")
LINE = re.compile(r"^(\*\*(?:From|To|Cc):\*\*)(\s*)(.*?)(\r?)$")

def address(part):
    if "<" in part and "@" in part:
        return None
    m = ASSET.match(part)
    if m:
        return f"{m.group('e').lower()}@e349.ics"
    for rx, addr in RULES:
        if re.search(rx, part):
            return addr
    return None

def top_split(body, sep=", "):
    """Split on sep outside parentheses and brackets."""
    out, depth, cur, i = [], 0, "", 0
    while i < len(body):
        c = body[i]
        depth += c in "([" ; depth -= c in ")]"
        if depth == 0 and body.startswith(sep, i):
            out.append(cur); cur = ""; i += len(sep); continue
        cur += c; i += 1
    out.append(cur)
    return out

def tag_part(p):
    toks = top_split(p)
    if len(toks) > 1 and any(CODE.match(t) for t in toks):
        addrs = [address(t) for t in toks]
        if all(addrs) and len(set(addrs)) == len(addrs):
            return ", ".join(f"{t} <{a}>" for t, a in zip(toks, addrs))
    a = address(p)
    return p if a is None else f"{p} <{a}>"

def fix_line(line):
    m = LINE.match(line)
    if not m:
        return line
    tag, sp, body, cr = m.groups()
    out = [tag_part(p) for p in top_split(body, "; ")]
    return f"{tag}{sp}{'; '.join(out)}{cr}"

def main():
    write = "--write" in sys.argv
    changed = lines_changed = 0
    for f in sorted(COMMS.glob("*/*.md")):
        raw = f.read_bytes().decode("utf-8")
        new_lines = []
        file_changed = False
        for ln in raw.split("\n"):
            n = fix_line(ln)
            if n != ln:
                lines_changed += 1
                file_changed = True
                if not write and lines_changed <= 12:
                    print("-", ln.replace("\r", "")[:130]); print("+", n.replace("\r", "")[:150])
            new_lines.append(n)
        if file_changed:
            changed += 1
            if write:
                f.write_bytes("\n".join(new_lines).encode("utf-8"))
    print(f"{lines_changed} lines in {changed} files {'written' if write else '(dry run)'}")

if __name__ == "__main__":
    main()
