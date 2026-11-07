#!/usr/bin/env python3
"""Build the research indexes for the ICS-Writing repo.

Reads every .md file and writes, into meta/:
  INDEX.md     one row per file: id, title, access, flags, size, summary
  ENTITIES.md  every character/place/thing -> its aliases -> every file that mentions it
  LINKS.md     which file points to which; broken references, orphans, one-way links
  FACTS.md     recurring numbers and where each value appears; flags differing values
  graph.html   clickable map of the files and their links (open in a browser)

Run from anywhere:   python3 tools/build_index.py
Quick lookups:       python3 tools/build_index.py --who EOD
                     python3 tools/build_index.py --links C-24
                     python3 tools/build_index.py --find "Level 7"      (plain text/regex)

Edit tools/entities.json and tools/facts.json to teach it new names and numbers.
The outputs are generated: do not edit them by hand, they are overwritten on every run.
Nothing here changes a story file.
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "meta"
SKIP_DIRS = {".git", ".obsidian", "node_modules", "tools", "__pycache__"}
GENERATED = {"meta/INDEX.md", "meta/ENTITIES.md", "meta/LINKS.md", "meta/FACTS.md"}
# Pasted snapshot of the whole project. Listed in the index but left out of counts and links,
# because it repeats everything and would drown the real files.
SNAPSHOTS = {"reference/ICS_Rigged_Sphere_MASTER_REFERENCE.md"}
# Files that quote other files; left out of the facts check only.
FACTS_SKIP_PREFIX = ("meta/", "reference/")

WORDNUM = {"thirteen": "13", "sixteen": "16", "twenty": "20", "thirty": "30", "forty": "40", "fifty": "50",
           "eight": "8", "nine": "9", "ten": "10", "eighth": "8th", "ninth": "9th", "tenth": "10th",
           "thirty-one": "31", "nineteen": "19"}


# ----------------------------------------------------------------------------- reading

def read(p):
    return p.read_text(encoding="utf-8", errors="replace")


def rel(p):
    return p.relative_to(ROOT).as_posix()


def all_md():
    out = []
    for p in sorted(ROOT.rglob("*.md")):
        parts = set(p.relative_to(ROOT).parts[:-1])
        if parts & SKIP_DIRS:
            continue
        if rel(p) in GENERATED:
            continue
        out.append(p)
    return out


def file_id(p):
    n = p.name
    m = re.match(r"([A-D]-\d{2,3})\b", n)
    if m:
        return m.group(1)
    m = re.match(r"(\d\.\d{2})\b", n)
    if m:
        return m.group(1)
    return None


def section_of(path):
    parts = path.split("/")
    if parts[0] == "canon" and len(parts) > 2:
        return "/".join(parts[:2])
    return parts[0]


def clean(s):
    s = re.sub(r"[*_`>\[\]]+", "", s)
    return re.sub(r"\s+", " ", s).strip()


def title_of(text, p):
    m = re.search(r"^\*\*Subject:\*\*\s*(.+)$", text, re.M)
    if m:
        return clean(m.group(1))
    for line in text.splitlines()[:25]:
        if line.startswith("#"):
            return clean(line.lstrip("#"))
    return p.stem


def summary_of(text, title):
    lines = text.splitlines()
    for line in lines[:60]:
        s = line.strip()
        if len(s) < 50 or s.startswith(("|", "#", "---", "- ", "* ", "**From", "**To", "**Cc", "**Date", "**Status", "**Subject", "*→")):
            continue
        c = clean(s)
        if c.lower() == title.lower() or len(c) < 40:
            continue
        return c[:150] + ("…" if len(c) > 150 else "")
    return ""


def access_of(text, path):
    head = [l for l in text.splitlines()[:16] if re.search(r"Status|Classification|Access|Readers", l, re.I)]
    h = " ".join(head).upper()
    if "SEALED" in h:
        return "Sealed"
    if "BOARD ACCESS" in h or "BOARD ONLY" in h or "ACCESS: BOARD" in h or "BOARD — RESTRICTED" in h:
        return "Board"
    if "PTKW" in h:
        return "PTKW"
    if "BRANCH DIRECTOR" in h:
        return "Branch Director"
    if any(k in h for k in ("ALL-STAFF", "GLOBAL", "PUBLIC")):
        return "Global"
    if "/employee/" in "/" + path:
        return "Employee"
    return "—"


def flags_of(text):
    f = []
    if "[PROPOSAL]" in text:
        f.append("proposal")
    if re.search(r"Status:.{0,40}(DRAFT|UNSENT|NOT SENT)", text[:1500], re.I):
        f.append("draft")
    if "\u00e2\u20ac" in text:
        f.append("encoding damage")
    return f


class Doc:
    pass


def load():
    docs = []
    for p in all_md():
        d = Doc()
        d.path = rel(p)
        d.p = p
        d.text = read(p)
        d.id = file_id(p)
        d.title = title_of(d.text, p)
        d.label = d.id or p.stem
        d.access = access_of(d.text, d.path)
        d.flags = flags_of(d.text)
        d.words = len(d.text.split())
        d.summary = summary_of(d.text, d.title)
        d.section = section_of(d.path)
        d.snapshot = d.path in SNAPSHOTS
        docs.append(d)
    return docs


def link(path):
    return f"[{path.split('/')[-1]}](<../{path}>)" if False else f"`{path}`"


# ----------------------------------------------------------------------------- entities

def compile_entities(cfg):
    out = []
    for e in cfg["entities"]:
        aliases = sorted(set(e["aliases"]), key=len, reverse=True)
        pat = "|".join(re.escape(a) for a in aliases)
        rx = re.compile(r"(?<![\w])(" + pat + r")(?![\w])")
        out.append((e, rx))
    return out


def scan_entities(docs, ents):
    res = {e["name"]: {} for e, _ in ents}
    for d in docs:
        for e, rx in ents:
            c = collections.Counter(m.group(1) for m in rx.finditer(d.text))
            if c:
                res[e["name"]][d.path] = c
    return res


# ----------------------------------------------------------------------------- links

MAIL_RE = re.compile(r"(?<![\w-])([A-D])-(\d{2,3})(?![\w-])")
RANGE_RE = re.compile(r"(?<![\w-])([A-D])-(\d{2,3})\s*(?:to|through|–|—)\s*(?:[A-D]-)?(\d{2,3})(?![\w-])")
DOC_RE = re.compile(r"(?:Documents?|Docs?)\s+((?:\d\.\d{2}\b(?:\s*(?:,|and|&|to|through)\s*)?)+)")
BARE_DOC_RE = re.compile(r"(?<!Section )(?<!Sections )(?<![\w.])(\d\.\d{2})(?![\w.])")
TICK_RE = re.compile(r"`([^`\n]+\.md)`")
SEE_RE = re.compile(r"^\s*\*?→\s*See:?(.*)$", re.M)


def build_maps(docs):
    by_id, by_path, by_stem = {}, {}, collections.defaultdict(list)
    for d in docs:
        by_path[d.path] = d
        if d.id:
            by_id[d.id] = d
        by_stem[d.p.stem.lower()].append(d)
    return by_id, by_path, by_stem


def refs_in(chunk, by_id, by_path, bare_docs=False):
    found, unresolved = set(), set()
    for m in RANGE_RE.finditer(chunk):
        a, b = int(m.group(2)), int(m.group(3))
        if 0 < b - a <= 12:
            for n in range(a, b + 1):
                found.add(f"{m.group(1)}-{n:02d}")
    for m in MAIL_RE.finditer(chunk):
        found.add(f"{m.group(1)}-{m.group(2)}")
    for m in DOC_RE.finditer(chunk):
        for n in re.findall(r"\d\.\d{2}", m.group(1)):
            found.add(n)
    if bare_docs:
        for m in BARE_DOC_RE.finditer(chunk):
            found.add(m.group(1))
    targets = set()
    for i in found:
        if i in by_id:
            targets.add(by_id[i].path)
        else:
            unresolved.add(i)
    for m in TICK_RE.finditer(chunk):
        t = m.group(1)
        if t in by_path:
            targets.add(t)
        else:
            hits = [p for p in by_path if p.endswith("/" + t) or p == t]
            if len(hits) == 1:
                targets.add(hits[0])
            else:
                unresolved.add(t)
    return targets, unresolved


def scan_links(docs):
    by_id, by_path, by_stem = build_maps(docs)
    out_see = collections.defaultdict(set)
    out_text = collections.defaultdict(set)
    broken = collections.defaultdict(set)
    for d in docs:
        if d.snapshot:
            continue
        see_lines = SEE_RE.findall(d.text)
        see_blob = "\n".join(see_lines)
        t, u = refs_in(see_blob, by_id, by_path, bare_docs=True)
        t.discard(d.path)
        out_see[d.path] = t
        broken[d.path] |= {x for x in u if x != d.id}
        body = SEE_RE.sub("", d.text)
        t2, _ = refs_in(body, by_id, by_path)
        t2.discard(d.path)
        out_text[d.path] = t2 - t
    inc = collections.defaultdict(set)
    for src in out_see:
        for tgt in out_see[src] | out_text[src]:
            inc[tgt].add(src)
    return by_id, by_path, out_see, out_text, inc, broken


# ----------------------------------------------------------------------------- facts

def scan_facts(docs, cfg):
    res = []
    for f in cfg["facts"]:
        pats = [re.compile(p) for p in f["patterns"]]
        pf = re.compile(f["paths"]) if f.get("paths") else None
        vals = collections.defaultdict(list)
        for d in docs:
            if d.snapshot or d.path.startswith(FACTS_SKIP_PREFIX):
                continue
            if pf and not pf.search(d.path):
                continue
            for n, line in enumerate(d.text.splitlines(), 1):
                for rx in pats:
                    for m in rx.finditer(line):
                        v = (m.group(1) or "").strip().lower()
                        v = WORDNUM.get(v, v)
                        if v:
                            ctx = clean(line)
                            i = ctx.lower().find(m.group(0).strip().lower()[:12])
                            ctx = ctx[max(0, i - 50): i + 90] if i >= 0 else ctx[:140]
                            if not any(x[0] == d.path and x[1] == n for x in vals[v]):
                                vals[v].append((d.path, n, ctx))
        res.append((f, vals))
    return res


# ----------------------------------------------------------------------------- writers

def md_link(d):
    return f"[{d.label}](<../{d.path}>)"


def write_index(docs):
    groups = collections.defaultdict(list)
    for d in docs:
        groups[d.section].append(d)
    lines = ["# Index of every file", "",
             "*Generated by `tools/build_index.py`. Do not edit by hand. Titles come from each file's heading or Subject line; "
             "summaries are the first prose line and are only a guide. Access is read from the header "
             "(Status / Classification / Access lines); “—” means the file states none. Flags: `proposal` = contains [PROPOSAL] material, "
             "`draft` = an unsent draft.*", "",
             f"**{len(docs)} files.** Sections: " + ", ".join(f"`{k}` ({len(v)})" for k, v in sorted(groups.items())), ""]
    for sec in sorted(groups):
        lines += [f"## {sec}", "", "| ID / name | Title | Access | Flags | Words | Summary |", "|---|---|---|---|---|---|"]
        for d in sorted(groups[sec], key=lambda x: x.path):
            t = d.title.replace("|", "/")
            s = d.summary.replace("|", "/")
            fl = ", ".join(d.flags + (["snapshot"] if d.snapshot else []))
            lines.append(f"| {md_link(d)} | {t[:90]} | {d.access} | {fl} | {d.words} | {s} |")
        lines.append("")
    (META / "INDEX.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_entities(docs, ents, scan):
    by_path = {d.path: d for d in docs}
    lines = ["# Entities: who and what appears where", "",
             "*Generated by `tools/build_index.py` from `tools/entities.json`. Each entity lists every alias it was searched under, "
             "then every file that mentions it, most mentions first. Counts exclude the pasted snapshot "
             "`reference/ICS_Rigged_Sphere_MASTER_REFERENCE.md` (shown separately). A file marked **weak** matched only an ambiguous alias "
             "(for example “Harmony”, an ordinary word), so check it. This is a text match: it does not catch “he”, “the entity” or "
             "other unnamed references.*", "",
             "| Entity | Kind | Files | Mentions | In snapshot |", "|---|---|---|---|---|"]
    snap_counts = {}
    for d in docs:
        if d.snapshot:
            for e, rx in ents:
                snap_counts[e["name"]] = len(rx.findall(d.text))
    anchors = {}
    for e, _ in ents:
        a = re.sub(r"[^a-z0-9 -]", "", e["name"].lower()).replace(" ", "-")
        anchors[e["name"]] = a
    for e, _ in ents:
        hits = {p: c for p, c in scan[e["name"]].items() if not by_path[p].snapshot}
        n = sum(sum(c.values()) for c in hits.values())
        lines.append(f"| [{e['name']}](#{anchors[e['name']]}) | {e['kind']} | {len(hits)} | {n} | {snap_counts.get(e['name'], 0)} |")
    lines.append("")
    for e, _ in ents:
        hits = {p: c for p, c in scan[e["name"]].items() if not by_path[p].snapshot}
        amb = set(e.get("ambiguous", []))
        tot = collections.Counter()
        for c in hits.values():
            tot.update(c)
        lines += [f"## {e['name']}", "", f"*{e['kind']}*" + (f". {e['note']}" if e.get("note") else ""), "",
                  "Aliases found: " + (", ".join(f"`{a}` ×{n}" + (" (ambiguous)" if a in amb else "") for a, n in tot.most_common()) or "none"), ""]
        if not hits:
            lines += ["No files.", ""]
            continue
        lines += ["| Mentions | File | Access | Aliases in this file |", "|---|---|---|---|"]
        for p, c in sorted(hits.items(), key=lambda kv: (-sum(kv[1].values()), kv[0])):
            d = by_path[p]
            weak = amb and set(c) <= amb
            al = ", ".join(f"{a}×{n}" for a, n in c.most_common())
            lines.append(f"| {sum(c.values())} | {md_link(d)} {d.title[:60].replace('|', '/')}" + (" **weak**" if weak else "") + f" | {d.access} | {al} |")
        lines.append("")
    (META / "ENTITIES.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_links(docs, maps):
    by_id, by_path, out_see, out_text, inc, broken = maps
    D = {d.path: d for d in docs}
    real = [d for d in docs if not d.snapshot]
    lab = lambda p: D[p].label  # noqa: E731
    n_see = sum(len(v) for v in out_see.values())
    n_text = sum(len(v) for v in out_text.values())
    lines = ["# Links between files", "",
             "*Generated by `tools/build_index.py`. “See” links come from the `→ See:` lines at the foot of a file. “Text” links are any other "
             "mention of a file id (C-24, Document 2.49, a backticked path) in the body. Ids written another way (“the Hallvik report”) are not caught.*", "",
             f"**{len(real)} files, {n_see} See links, {n_text} further text links.**", ""]

    bl = [(p, sorted(v)) for p, v in broken.items() if v]
    lines += ["## Broken See references", "",
              "A `→ See:` line names an id or path that matches no file. Most are typos, renamed files, or files that do not exist yet.", ""]
    if bl:
        for p, v in sorted(bl):
            lines.append(f"- {md_link(D[p])}: {', '.join('`' + x + '`' for x in v)}")
    else:
        lines.append("None.")
    lines.append("")

    orph = [d for d in real if not out_see[d.path] and not out_text[d.path] and not inc.get(d.path)]
    lines += ["## Orphans", "", "Files with no links in or out. Not an error, but nothing connects them to the rest.", ""]
    lines += [f"- {md_link(d)} {d.title[:70]}" for d in sorted(orph, key=lambda x: x.path)] or ["None."]
    lines.append("")

    lines += ["## Most linked-to", "", "| Links in | File |", "|---|---|"]
    for p, s in sorted(inc.items(), key=lambda kv: -len(kv[1]))[:25]:
        lines.append(f"| {len(s)} | {md_link(D[p])} {D[p].title[:70].replace('|', '/')} |")
    lines.append("")

    oneway = collections.defaultdict(list)
    for src, tgts in out_see.items():
        for t in tgts:
            if src not in (out_see[t] | out_text[t]):
                oneway[t].append(src)
    total = sum(len(v) for v in oneway.values())
    lines += ["## One-way See links", "",
              f"{total} See links point at a file that never mentions the file pointing at it. This is normal for a document cited by many "
              "(a glossary, a profile). It matters when two files are about the same event and only one knows about the other. Listed by the file being pointed at; the 40 most-cited first.", ""]
    for t, srcs in sorted(oneway.items(), key=lambda kv: -len(kv[1]))[:40]:
        lines.append(f"- {md_link(D[t])} is cited by {len(srcs)} that it does not cite back: " + ", ".join(lab(s) for s in sorted(srcs)[:12]) + (" …" if len(srcs) > 12 else ""))
    lines.append("")

    lines += ["## File by file", "", "`→` = this file points at; `←` = pointed at by. Bold = a See link, plain = a text mention.", ""]
    for d in sorted(real, key=lambda x: x.path):
        o = [f"**{lab(p)}**" for p in sorted(out_see[d.path])] + [lab(p) for p in sorted(out_text[d.path])]
        i = sorted(lab(p) for p in inc.get(d.path, ()))
        if not o and not i:
            continue
        lines.append(f"- {md_link(d)} {d.title[:60]}")
        if o:
            lines.append(f"  - → {', '.join(o)}")
        if i:
            lines.append(f"  - ← {', '.join(i)}")
    (META / "LINKS.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_facts(results):
    lines = ["# Recurring facts and their values", "",
             "*Generated by `tools/build_index.py` from `tools/facts.json`. For each fact, every value found with the file and line. "
             "**Values differ** means the files give more than one value. That is sometimes a real contradiction and sometimes two different "
             "things (a single salvo against a total), so read the context. The snapshot, `meta/` and `reference/` are skipped because they quote the others.*", ""]
    for f, vals in results:
        lines.append(f"## {f['name']}")
        lines.append("")
        if f.get("note"):
            lines += [f"*Known: {f['note']}*", ""]
        if not vals:
            lines += ["No matches.", ""]
            continue
        flag = len(vals) > 1 and not f.get("expect_variety")
        lines.append("**Values differ.**" if flag else ("Several values, expected (they describe different things)." if len(vals) > 1 else "One value."))
        lines.append("")
        for v, locs in sorted(vals.items(), key=lambda kv: -len(kv[1])):
            lines.append(f"- **{v}** ×{len(locs)}")
            for p, n, ctx in locs[:6]:
                lines.append(f"  - `{p}:{n}` … {ctx} …")
            if len(locs) > 6:
                lines.append(f"  - … and {len(locs) - 6} more")
        lines.append("")
    (META / "FACTS.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


GRAPH_HTML = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ICS-Writing file map</title>
<style>
:root{--bg:#f6f5f1;--fg:#1c1b19;--mut:#6b6860;--line:#8a877c;--card:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#161614;--fg:#ecebe6;--mut:#9a978e;--line:#7a776c;--card:#22221f}}
html,body{margin:0;height:100%;background:var(--bg);color:var(--fg);font:14px system-ui,sans-serif}
#bar{position:fixed;top:0;left:0;right:0;padding:10px 16px;display:flex;gap:12px;flex-wrap:wrap;align-items:center;background:var(--bg);border-bottom:1px solid var(--line);z-index:2}
#bar input{padding:6px 8px;font:inherit;min-width:220px;background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:6px}
#legend span{margin-right:12px;white-space:nowrap}#legend i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:4px}
#info{position:fixed;left:16px;bottom:12px;right:16px;padding:8px 12px;background:var(--card);border:1px solid var(--line);border-radius:8px;min-height:20px;z-index:2}
canvas{position:fixed;top:0;left:0}
</style></head><body>
<div id="bar"><b>File map</b><input id="q" placeholder="Find a file (C-24, EOD, Level 7)…"><span id="legend"></span><span style="color:var(--mut)">Drag to move, scroll to zoom, click a dot to highlight its links.</span></div>
<canvas id="c"></canvas><div id="info">Hover or click a dot.</div>
<script>
const DATA=__DATA__;
const cv=document.getElementById('c'),ctx=cv.getContext('2d'),info=document.getElementById('info');
let W,H;function rs(){W=cv.width=innerWidth;H=cv.height=innerHeight}rs();addEventListener('resize',rs);
const pal=['#2f6f9f','#c0562b','#4d8f4d','#8a5aa8','#b08a1e','#2a8f8f','#a8456b','#6b6b6b','#7a5c3a','#3b5fc0'];
const secs=[...new Set(DATA.nodes.map(n=>n.s))].sort();const col=s=>pal[secs.indexOf(s)%pal.length];
document.getElementById('legend').innerHTML=secs.map(s=>`<span><i style="background:${col(s)}"></i>${s}</span>`).join('');
const N=DATA.nodes.map((n,i)=>({...n,i,x:Math.random()*W,y:Math.random()*H,vx:0,vy:0,deg:0}));
const E=DATA.edges.map(([a,b,t])=>({a:N[a],b:N[b],t}));E.forEach(e=>{e.a.deg++;e.b.deg++});
const adj=N.map(()=>new Set());E.forEach(e=>{adj[e.a.i].add(e.b.i);adj[e.b.i].add(e.a.i)});
let sel=-1,hov=-1,k=1,ox=0,oy=0,heat=300,drag=null,pan=null,match=null;
function step(){const r=heat>0?1:0;if(!r)return;heat--;
 for(let i=0;i<N.length;i++){const a=N[i];for(let j=i+1;j<N.length;j++){const b=N[j];let dx=a.x-b.x,dy=a.y-b.y,d=dx*dx+dy*dy+.01;if(d<40000){const f=900/d;dx*=f;dy*=f;a.vx+=dx;a.vy+=dy;b.vx-=dx;b.vy-=dy}}}
 E.forEach(e=>{let dx=e.b.x-e.a.x,dy=e.b.y-e.a.y;const d=Math.sqrt(dx*dx+dy*dy)+.01,f=(d-60)*.012;dx=dx/d*f;dy=dy/d*f;e.a.vx+=dx;e.a.vy+=dy;e.b.vx-=dx;e.b.vy-=dy});
 N.forEach(n=>{n.vx+=(W/2-n.x)*.002;n.vy+=(H/2-n.y)*.002;if(n!==drag){n.x+=n.vx*.5;n.y+=n.vy*.5}n.vx*=.8;n.vy*=.8})}
function draw(){step();ctx.clearRect(0,0,W,H);ctx.save();ctx.translate(ox,oy);ctx.scale(k,k);
 const act=sel>=0?sel:hov;
 E.forEach(e=>{const on=act>=0&&(e.a.i===act||e.b.i===act);ctx.globalAlpha=act<0?.18:(on?.9:.04);ctx.strokeStyle=on?'#c0562b':getComputedStyle(document.body).color;ctx.lineWidth=(e.t?1.4:.6)/k;ctx.beginPath();ctx.moveTo(e.a.x,e.a.y);ctx.lineTo(e.b.x,e.b.y);ctx.stroke()});
 N.forEach(n=>{const near=act<0||n.i===act||adj[act].has(n.i);const m=match?match.has(n.i):true;ctx.globalAlpha=(near&&m)?1:.12;ctx.fillStyle=col(n.s);ctx.beginPath();ctx.arc(n.x,n.y,3+Math.min(7,Math.sqrt(n.deg)),0,7);ctx.fill();
  if(n.i===act||(match&&match.has(n.i))||(act>=0&&adj[act].has(n.i))||k>2){ctx.globalAlpha=1;ctx.fillStyle=getComputedStyle(document.body).color;ctx.font=(11/k)+'px system-ui';ctx.fillText(n.l,n.x+6/k,n.y-6/k)}});
 ctx.restore();requestAnimationFrame(draw)}
const at=(mx,my)=>{const x=(mx-ox)/k,y=(my-oy)/k;let b=-1,bd=1e9;N.forEach(n=>{const d=(n.x-x)**2+(n.y-y)**2;if(d<bd&&d<(10/k)**2){bd=d;b=n.i}});return b};
const show=i=>{if(i<0){info.textContent='Hover or click a dot.';return}const n=N[i];info.innerHTML=`<b>${n.l}</b> ${n.t} <span style="color:var(--mut)">· ${n.p} · ${n.a} · ${adj[i].size} links</span>`};
cv.onmousemove=ev=>{if(drag){drag.x=(ev.clientX-ox)/k;drag.y=(ev.clientY-oy)/k;heat=60;return}if(pan){ox=pan.ox+ev.clientX-pan.x;oy=pan.oy+ev.clientY-pan.y;return}hov=at(ev.clientX,ev.clientY);if(sel<0)show(hov)};
cv.onmousedown=ev=>{const i=at(ev.clientX,ev.clientY);if(i>=0){drag=N[i];sel=i;show(i)}else{sel=-1;pan={x:ev.clientX,y:ev.clientY,ox,oy}}};
addEventListener('mouseup',()=>{drag=null;pan=null});
cv.onwheel=ev=>{ev.preventDefault();const f=ev.deltaY<0?1.12:.9,mx=ev.clientX,my=ev.clientY;ox=mx-(mx-ox)*f;oy=my-(my-oy)*f;k*=f};
document.getElementById('q').oninput=ev=>{const v=ev.target.value.trim().toLowerCase();match=v?new Set(N.filter(n=>(n.l+' '+n.t+' '+n.p).toLowerCase().includes(v)).map(n=>n.i)):null};
draw();
</script></body></html>
"""


def write_graph(docs, maps):
    by_id, by_path, out_see, out_text, inc, broken = maps
    nodes = [d for d in docs if not d.snapshot]
    idx = {d.path: i for i, d in enumerate(nodes)}
    edges = []
    for src in out_see:
        for t in out_see[src]:
            edges.append([idx[src], idx[t], 1])
        for t in out_text[src]:
            edges.append([idx[src], idx[t], 0])
    data = {"nodes": [{"l": d.label, "t": d.title[:80], "p": d.path, "s": d.section, "a": d.access} for d in nodes], "edges": edges}
    (META / "graph.html").write_text(GRAPH_HTML.replace("__DATA__", json.dumps(data, ensure_ascii=False)), encoding="utf-8", newline="\n")


# ----------------------------------------------------------------------------- command line

def find_entity(ents, q):
    ql = q.lower()
    for e, _ in ents:
        if e["name"].lower() == ql or ql in (a.lower() for a in e["aliases"]):
            return e
    for e, _ in ents:
        if ql in e["name"].lower():
            return e
    return None


def cli_who(docs, ents, q):
    e = find_entity(ents, q)
    by = {d.path: d for d in docs}
    if e:
        rx = dict((x["name"], r) for x, r in ents)[e["name"]]
        print(f"{e['name']} ({e['kind']}), aliases: {', '.join(e['aliases'])}")
        rows = []
        for d in docs:
            if d.snapshot:
                continue
            c = collections.Counter(m.group(1) for m in rx.finditer(d.text))
            if c:
                rows.append((sum(c.values()), d.path, c))
    else:
        rx = re.compile(q, re.I)
        print(f"No entity named {q!r}; plain search instead.")
        rows = []
        for d in docs:
            if d.snapshot:
                continue
            n = len(rx.findall(d.text))
            if n:
                rows.append((n, d.path, {q: n}))
    rows.sort(key=lambda r: (-r[0], r[1]))
    for n, p, c in rows:
        print(f"{n:4d}  {by[p].access:<15} {p}")
    print(f"-- {len(rows)} files, snapshot excluded")


def cli_links(docs, maps, q):
    by_id, by_path, out_see, out_text, inc, broken = maps
    ql = q.lower()
    hits = [d for d in docs if not d.snapshot and (d.id and d.id.lower() == ql or ql in d.path.lower())]
    if not hits:
        print("No such file.")
        return
    for d in hits[:5]:
        print(f"{d.path}  [{d.access}]")
        print("  see   ->", ", ".join(by_path[p].label for p in sorted(out_see[d.path])) or "-")
        print("  text  ->", ", ".join(by_path[p].label for p in sorted(out_text[d.path])) or "-")
        print("  from  <-", ", ".join(by_path[p].label for p in sorted(inc.get(d.path, ()))) or "-")
        if broken[d.path]:
            print("  broken:", ", ".join(sorted(broken[d.path])))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--who", help="list files mentioning an entity (name or alias) or a plain search term")
    ap.add_argument("--links", help="show what a file points at and what points at it (id or part of the name)")
    ap.add_argument("--find", help="regex search, files ranked by hits")
    a = ap.parse_args()

    docs = load()
    ents = compile_entities(json.loads((ROOT / "tools" / "entities.json").read_text(encoding="utf-8")))
    if a.who:
        return cli_who(docs, ents, a.who)
    if a.find:
        return cli_who(docs, [], a.find)
    maps = scan_links(docs)
    if a.links:
        return cli_links(docs, maps, a.links)

    META.mkdir(exist_ok=True)
    facts_cfg = json.loads((ROOT / "tools" / "facts.json").read_text(encoding="utf-8"))
    write_index(docs)
    write_entities(docs, ents, scan_entities(docs, ents))
    write_links(docs, maps)
    write_facts(scan_facts(docs, facts_cfg))
    write_graph(docs, maps)
    n_edges = sum(len(v) for v in maps[2].values()) + sum(len(v) for v in maps[3].values())
    print(f"{len(docs)} files, {n_edges} links. Wrote meta/INDEX.md, ENTITIES.md, LINKS.md, FACTS.md, graph.html")


if __name__ == "__main__":
    sys.exit(main())
