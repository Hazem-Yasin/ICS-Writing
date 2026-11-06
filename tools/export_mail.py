#!/usr/bin/env python3
"""Export series A-D to one JSON file for the game, with the device slices of design/DEVICES.md.

Usage: python3 tools/export_mail.py [OUTPUT.json]
Usage: export_mail.py <output.json>  (default: mail.json next to the repo root)
Writer's notes (the closing [PROPOSAL] note and the '-> See' lines) are cut from the body.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMMS = ROOT / "canon" / "internal-communications"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "mail.json"

sys.path.insert(0, str(ROOT / "tools"))
from mail_index import MAILBOXES  # noqa: E402

def parse(path):
    text = path.read_text(encoding="utf-8").replace("\r", "")
    head, body, in_head = {}, [], True
    for ln in text.split("\n"):
        m = re.match(r"\*\*(From|To|Cc|Subject|Date|Status|Attachment|Thread kept by):\*\*\s*(.*)", ln)
        if in_head and m:
            head[m.group(1).lower()] = m.group(2).strip()
            continue
        if in_head and ln.strip() == "---" and head:
            in_head = False
            continue
        if not in_head or (not head and ln.strip()):
            in_head = False if head else in_head
            body.append(ln)
    # cut writer's notes
    out = []
    for ln in body:
        if ln.startswith("*[PROPOSAL]") or ln.startswith("*→ See"):
            continue
        out.append(ln)
    s = "\n".join(out).strip()
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"\n---\s*$", "", s).strip()
    return head, s

def main():
    msgs, index = [], {}
    for f in sorted(COMMS.glob("*/*.md")):
        code = f.name.split(" ")[0]
        head, body = parse(f)
        frm = head.get("from", "")
        to = head.get("to", "")
        cc = head.get("cc", "")
        hdr = f"**From:** {frm}\n**To:** {to}\n**Cc:** {cc}"
        msgs.append({
            "code": code,
            "series": code[0],
            "from": frm, "to": to, "cc": cc,
            "subject": head.get("subject", f.stem),
            "date": head.get("date", ""),
            "status": head.get("status", ""),
            "body": body,
            "_hdr": hdr,
        })
        index[code] = len(msgs) - 1

    def by_mailbox(name):
        rx = next(r for n, _, r in MAILBOXES if n == name)
        return [m["code"] for m in msgs if re.search(rx, m["_hdr"])]

    def series(letter, pred=lambda m: True):
        return [m["code"] for m in msgs if m["series"] == letter and pred(m)]

    devices = {
        "manager": {
            "title": "Earth Branch Manager - Level 2 terminal",
            "account": "Earth Branch Manager (Branch Director tier)",
            "user": "manager@e349.ics",
            "password": "smiling-man",
            "hint": "",
            "codes": by_mailbox("Earth Branch Manager"),
        },
        "k7": {
            "title": "K-7 - Level 5 workstation",
            "account": "PTKW employee",
            "user": "k-7@e349.ics",
            "password": "156-mondays",
            "hint": "",
            "codes": series("B"),
        },
        "director": {
            "title": "Branch Director - Level 2 desk machine",
            "account": "Branch Director",
            "user": "director@e349.ics",
            "password": "",
            "hint": "",
            "codes": series("C"),
        },
        "desk": {
            "title": "Work Floor B - desk 14",
            "account": "Standard employee",
            "user": "e-03702@e349.ics",
            "password": "",
            "hint": "",
            "codes": series("A", lambda m: m["status"].upper().startswith("SENT")),
        },
    }
    for d in devices.values():
        d["codes"] = [c for c in d["codes"]]
    for m in msgs:
        m.pop("_hdr")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"messages": msgs, "devices": [dict(id=k, **v) for k, v in devices.items()]},
                              ensure_ascii=False), encoding="utf-8")
    print(f"{len(msgs)} messages -> {OUT} ({OUT.stat().st_size // 1024} KB)")
    for k, v in devices.items():
        print(f"  {k:9} {len(v['codes']):>3} messages")

if __name__ == "__main__":
    main()
