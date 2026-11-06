#!/usr/bin/env python3
"""Count which mailbox each message belongs to, from the From/To/Cc/Status lines.

Reads canon/internal-communications/*/*.md (series A-D). Prints a table and, with --json,
writes tools/mail_index.json. Addresses follow design/DEVICES.md section 2.
Run from anywhere: python3 tools/mail_index.py [--json]
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMMS = ROOT / "canon" / "internal-communications"

# (mailbox, address, regex matched against the From/To/Cc lines)
MAILBOXES = [
    ("Earth Branch Manager", "manager@e349.ics", r"Earth Branch Manager|Earth Branch Operations|Branch Manager"),
    ("K-7", "k-7@e349.ics", r"\bK-7\b"),
    ("K-12", "k-12@e349.ics", r"\bK-12\b"),
    ("TOR-9", "tor-9@e349.ics", r"\bTOR-9\b"),
    ("VAH-3", "vah-3@e349.ics", r"\bVAH-?3\b"),
    ("PTKW Duty Officer", "ptkw-duty@e349.ics", r"Duty Officer"),
    ("PTKW Investigation Team", "ptkw-investigation@e349.ics", r"Investigation Team"),
    ("PTKW Oversight Unit", "ptkw-oversight@hq.ics", r"Oversight Unit"),
    ("Branch Director", "director@e349.ics", r"Branch Director|Maren Voss"),
    ("Regional Sector Lead", "sector-lead@hq.ics", r"Regional Sector Lead|Brant"),
    ("EOD Research Team", "eod-research@hq.ics", r"EOD Research Team|Interplanetary Research Division"),
    ("Interplanetary HQ", "hq@hq.ics", r"Interplanetary HQ"),
    ("Facilities Management", "facilities@e349.ics", r"Facilities Management"),
    ("Design Team", "design@e349.ics", r"Design Div|Behavioral Architect|Environmental Design|Behavioral Analytics|BES Architect|Dr\. Selin Akar"),
]

def header(text):
    lines = []
    for ln in text.replace("\r", "").split("\n"):
        if ln.startswith(("**From:**", "**To:**", "**Cc:**")):
            lines.append(ln)
    return "\n".join(lines)

def main():
    counts = {m[0]: [] for m in MAILBOXES}
    assets = {}
    files = sorted(COMMS.glob("*/*.md"))
    for f in files:
        h = header(f.read_text(encoding="utf-8"))
        code = f.name.split(" ")[0]
        for name, _, rx in MAILBOXES:
            if re.search(rx, h):
                counts[name].append(code)
        for e in re.findall(r"\bE-\d{5}\b", h):
            assets.setdefault(e, []).append(code)
    print(f"{len(files)} messages in series A-D\n")
    print(f"{'Mailbox':26} {'Address':30} {'n':>3}")
    for name, addr, _ in MAILBOXES:
        print(f"{name:26} {addr:30} {len(counts[name]):>3}")
    print(f"\n{len(assets)} staff mailboxes by asset number, e.g. e-03615@e349.ics")
    if "--json" in sys.argv:
        out = {"mailboxes": {n: {"address": a, "messages": counts[n]} for n, a, _ in MAILBOXES},
               "staff": {f"{k.lower()}@e349.ics": v for k, v in sorted(assets.items())}}
        (ROOT / "tools" / "mail_index.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
        print("wrote tools/mail_index.json")

if __name__ == "__main__":
    main()
