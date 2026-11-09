#!/usr/bin/env python3
"""Generate the ICS Earth Branch mark (Document 2.32) as SVG, and optionally PNG.

Python stdlib only.

    python tools/make_logo.py          write SVGs to design/brand/
    python tools/make_logo.py --png    also render PNGs (needs Edge or Chrome)

Geometry is the single source of truth for design/brand/ and design/LOGO.md.
"""
import math
import os
import struct
import subprocess
import sys
import tempfile
from dataclasses import dataclass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "design", "brand")

BLUE = "#1A2E52"   # ICS Deep Blue, Doc 2.32
GOLD = "#C9A84C"   # ICS Warm Gold, Doc 2.32
PAPER = "#F4EEE1"  # beige paper, design/HEARTH.md
WHITE = "#FFFFFF"
C = 200.0          # centre of the 400 x 400 mark box


@dataclass
class Spec:
    ring_r: float = 100
    ring_w: float = 18
    arc_w: float = 14
    gap: float = 5        # clear space between the arc tip and the ring: they never touch
    th0: float = 105      # arc start (the tail): 105 = below the ring, a little left of the base
    th1: float = 470      # arc end (the head): 470 = 110, curling back toward the base
    th_turn: float = 320  # where the arc stops following its outer radius and dives inward
    r0: float = 172       # radius of the sweep, outside the ring
    k: float = 3.0        # dive profile: higher = later, steeper hook

    @property
    def r1(self):
        """Radius of the arc centreline at the tip: resting against the ring, clear by `gap`."""
        return self.ring_r + self.ring_w / 2 + self.arc_w / 2 + self.gap


STD = Spec()
SMALL = Spec(ring_w=30, arc_w=26, gap=8, r0=186)


def arc_pts(s, n=140):
    """Tail at th0, constant radius r0 round the top and down the right side, then an
    ease-in dive so the head meets the ring's base head-on. The arc never crosses the ring."""
    pts = []
    for i in range(n + 1):
        th = s.th0 + (s.th1 - s.th0) * i / n
        if th <= s.th_turn:
            r = s.r0
        else:
            u = (th - s.th_turn) / (s.th1 - s.th_turn)
            r = s.r0 - (s.r0 - s.r1) * u ** s.k
        a = math.radians(th)
        pts.append((C + r * math.cos(a), C + r * math.sin(a)))
    return pts


def smooth_path(pts):
    """Catmull-Rom through pts, written as cubic Beziers."""
    d = "M%.2f %.2f" % pts[0]
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else pts[i + 1]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += " C%.2f %.2f %.2f %.2f %.2f %.2f" % (c1 + c2 + p2)
    return d


def bbox(s, ring=True, arc=True):
    xs, ys = [], []
    if arc:
        h = s.arc_w / 2
        for x, y in arc_pts(s):
            xs += [x - h, x + h]
            ys += [y - h, y + h]
    if ring:
        e = s.ring_r + s.ring_w / 2
        xs += [C - e, C + e]
        ys += [C - e, C + e]
    return min(xs), min(ys), max(xs), max(ys)


def mark(uid, s, ring_col, arc_col, ring=True, arc=True):
    """Return (defs, body) for the mark in the 400-unit box."""
    defs, body = "", ""
    if ring:
        body += '<circle cx="%g" cy="%g" r="%g" fill="none" stroke="%s" stroke-width="%g"/>' % (
            C, C, s.ring_r, ring_col, s.ring_w)
    if arc:
        body += '<path d="%s" fill="none" stroke="%s" stroke-width="%g" stroke-linecap="round" stroke-linejoin="round"/>' % (
            smooth_path(arc_pts(s)), arc_col, s.arc_w)
    return defs, body


WM_W = 14  # wordmark stroke, in wordmark units


def wordmark(col, w=WM_W):
    """ICS as monoline strokes with round caps. No sharp angles, no font dependency.
    Local box: x -w/2 .. 234+w/2, y -w/2 .. 100+w/2. Cap height 100 on the centreline."""
    return (
        '<g fill="none" stroke="%s" stroke-width="%g" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M0 0V100"/>'
        '<path transform="translate(46 0)" d="M88.3 17.9A50 50 0 1 0 88.3 82.1"/>'
        '<path transform="translate(176 0)" d="M51.4 8.9A28 25 0 1 0 30 50A28 25 0 1 1 8.6 91.1"/>'
        "</g>" % (col, w)
    )


WM_X0, WM_X1 = -WM_W / 2, 234 + WM_W / 2
WM_Y0, WM_Y1 = -WM_W / 2, 100 + WM_W / 2


def doc(vb, inner, width=None, title="ICS Earth Branch mark"):
    x, y, w, h = vb
    if width is None:
        width = w
    height = width * h / w
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="%.1f %.1f %.1f %.1f" width="%.1f" height="%.1f">'
        "<title>%s</title>%s</svg>\n" % (x, y, w, h, width, height, title, inner)
    )


def solo(uid, s, ring_col, arc_col, pad=20, **kw):
    defs, body = mark(uid, s, ring_col, arc_col, **kw)
    x0, y0, x1, y1 = bbox(s, kw.get("ring", True), kw.get("arc", True))
    vb = (x0 - pad, y0 - pad, x1 - x0 + 2 * pad, y1 - y0 + 2 * pad)
    return vb, "<defs>%s</defs>%s" % (defs, body)


def lockup_h(uid, s, ring_col, arc_col, word_col, pad=24, k=1.15):
    defs, body = mark(uid, s, ring_col, arc_col)
    x0, y0, x1, y1 = bbox(s)
    wx = x1 + 56 - WM_X0 * k
    wy = C - 50 * k
    word = '<g transform="translate(%.1f %.1f) scale(%g)">%s</g>' % (wx, wy, k, wordmark(word_col))
    right = wx + WM_X1 * k
    vb = (x0 - pad, y0 - pad, right - x0 + 2 * pad, y1 - y0 + 2 * pad)
    return vb, "<defs>%s</defs>%s%s" % (defs, body, word)


def lockup_v(uid, s, ring_col, arc_col, word_col, pad=24, k=0.95):
    defs, body = mark(uid, s, ring_col, arc_col)
    x0, y0, x1, y1 = bbox(s)
    ww = (WM_X1 - WM_X0) * k
    wx = C - ww / 2 - WM_X0 * k
    wy = y1 + 52 - WM_Y0 * k
    word = '<g transform="translate(%.1f %.1f) scale(%g)">%s</g>' % (wx, wy, k, wordmark(word_col))
    left = min(x0, C - ww / 2)
    right = max(x1, C + ww / 2)
    bottom = wy + WM_Y1 * k
    vb = (left - pad, y0 - pad, right - left + 2 * pad, bottom - y0 + 2 * pad)
    return vb, "<defs>%s</defs>%s%s" % (defs, body, word)


def write(name, vb, inner, width=None):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(doc(vb, inner, width))
    return path


# ---------------------------------------------------------------- sheet

FONT = "font-family=\"Segoe UI, Helvetica, Arial, sans-serif\""
_n = [0]


def uid():
    _n[0] += 1
    return "m%d" % _n[0]


def place(x, y, w, vb_inner):
    vb, inner = vb_inner
    h = w * vb[3] / vb[2]
    return '<svg x="%g" y="%g" width="%g" height="%g" viewBox="%.1f %.1f %.1f %.1f">%s</svg>' % (
        x, y, w, h, vb[0], vb[1], vb[2], vb[3], inner), h


def label(x, y, text, col="#57606a", size=15, anchor="start", weight="400"):
    return '<text x="%g" y="%g" %s font-size="%g" fill="%s" text-anchor="%s" font-weight="%s">%s</text>' % (
        x, y, FONT, size, col, anchor, weight, text)


def sheet():
    W, H = 1600, 1180
    o = ['<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H)]
    # row 1: primary on paper, reversed on blue
    o.append('<rect x="0" y="0" width="800" height="440" fill="%s"/>' % PAPER)
    o.append('<rect x="800" y="0" width="800" height="440" fill="%s"/>' % BLUE)
    s, _ = place(80, 60, 640, lockup_h(uid(), STD, BLUE, GOLD, BLUE))
    o.append(s)
    s, _ = place(880, 60, 640, lockup_h(uid(), STD, PAPER, GOLD, PAPER))
    o.append(s)
    o.append(label(40, 412, "PRIMARY on beige paper #F4EEE1", PAPER and "#57606a"))
    o.append(label(840, 412, "REVERSED on ICS Deep Blue", "#c8cfdc"))

    # row 2 panel A: stacked + mono
    o.append('<rect x="0" y="440" width="800" height="360" fill="#ffffff"/>')
    s, h = place(60, 470, 190, lockup_v(uid(), STD, BLUE, GOLD, BLUE))
    o.append(s)
    s, h = place(300, 470, 190, solo(uid(), STD, BLUE, BLUE))
    o.append(s)
    o.append('<rect x="520" y="470" width="240" height="240" fill="%s"/>' % BLUE)
    s, h = place(540, 490, 200, solo(uid(), STD, WHITE, WHITE))
    o.append(s)
    o.append(label(60, 760, "Stacked", anchor="start"))
    o.append(label(300, 760, "One colour, blue"))
    o.append(label(520, 760, "One colour, white"))

    # row 2 panel B: size ladder
    o.append('<rect x="800" y="440" width="800" height="360" fill="%s"/>' % PAPER)
    x = 830
    for px in (192, 96, 64, 48, 32):
        spec = SMALL if px <= 48 else STD
        s, h = place(x, 480, px, solo(uid(), spec, BLUE, GOLD))
        o.append(s)
        o.append(label(x + px / 2, 480 + 200, "%d px" % px, size=13, anchor="middle"))
        x += px + 28
    x = 830
    for px in (24, 16):
        s, h = place(x, 720, px, solo(uid(), SMALL, BLUE, GOLD))
        o.append(s)
        o.append(label(x + px / 2, 720 + 44, "%d px" % px, size=13, anchor="middle"))
        x += px + 40
    o.append(label(1040, 735, "STD up to 64 px. SMALL (heavier strokes) at 48 px and below.", size=13))

    # row 3: blur test, readings
    o.append('<rect x="0" y="800" width="800" height="380" fill="#ffffff"/>')
    o.append('<defs><filter id="bl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5"/></filter></defs>')
    s, h = place(60, 840, 200, solo(uid(), STD, BLUE, GOLD))
    o.append('<g filter="url(#bl)">%s</g>' % s)
    s, h = place(300, 840, 200, solo(uid(), STD, BLUE, GOLD))
    o.append(s)
    o.append('<defs><filter id="bl2"><feGaussianBlur stdDeviation="9"/></filter></defs>')
    s, h = place(540, 840, 200, solo(uid(), STD, BLUE, BLUE))
    o.append('<g filter="url(#bl2)">%s</g>' % s)
    o.append(label(60, 1100, "Blur test (Rand)"))
    o.append(label(300, 1100, "Unblurred"))
    o.append(label(540, 1100, "Heavy blur, one colour"))

    o.append('<rect x="800" y="800" width="800" height="380" fill="#ffffff"/>')
    # readings: arc isolated; ring with head and tail marked
    s, h = place(830, 840, 220, solo(uid(), STD, BLUE, GOLD, ring=False))
    o.append(s)
    o.append(label(830, 1100, "The arc alone: a fishhook"))
    s, h = place(1090, 840, 220, solo(uid(), STD, BLUE, GOLD))
    o.append(s)
    # head and tail markers on the 220 px placement of the std box
    vb, _ = solo("x", STD, BLUE, GOLD)
    sc = 220 / vb[2]
    pts = arc_pts(STD)
    tail, head = pts[0], pts[-1]
    def tx(p):
        return 1090 + (p[0] - vb[0]) * sc, 840 + (p[1] - vb[1]) * sc
    (ax, ay), (bx, by) = tx(tail), tx(head)
    o.append('<circle cx="%.1f" cy="%.1f" r="5" fill="none" stroke="#c9302c" stroke-width="1.5"/>' % (ax, ay))
    o.append('<circle cx="%.1f" cy="%.1f" r="5" fill="none" stroke="#c9302c" stroke-width="1.5"/>' % (bx, by))
    o.append(label(ax - 12, ay + 24, "tail", "#c9302c", 13, "end"))
    o.append(label(bx + 14, by + 30, "head", "#c9302c", 13))
    o.append(label(1090, 1100, "Tail and head: the arc bites toward its own start"))
    o.append(label(1350, 880, "Diagnostic only.", "#57606a", 13))
    o.append(label(1350, 900, "Not a brand mark.", "#57606a", 13))
    return (0, 0, W, H), "".join(o)


# ---------------------------------------------------------------- render

def find_browser():
    for p in (
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ):
        if os.path.exists(p):
            return p
    return None


def png_size(path):
    with open(path, "rb") as f:
        b = f.read(24)
    return struct.unpack(">II", b[16:24])


def render(name, vb, inner, px_w, transparent=True):
    exe = find_browser()
    if not exe:
        print("no Edge or Chrome found, skipping PNG for", name)
        return
    px_h = round(px_w * vb[3] / vb[2])
    tmp = os.path.join(tempfile.gettempdir(), "ics_logo_render.svg")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(doc(vb, inner, width=px_w))
    png = os.path.join(OUT, name)
    bg = "00000000" if transparent else "ffffffff"
    subprocess.run(
        [exe, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
         "--default-background-color=" + bg, "--window-size=%d,%d" % (px_w, px_h),
         "--screenshot=" + png, "file:///" + tmp.replace("\\", "/")],
        check=True, timeout=90, capture_output=True)
    print("png", name, png_size(png), "wanted", (px_w, px_h))


# ---------------------------------------------------------------- emblem
# The detailed form: a certificate seal. Same ring and arc, with a text band, a guilloche
# field and 349 ticks. Lettering is monoline strokes (round caps, round joins), so the SVG
# needs no font. Glyphs are drawn on a 100-unit-high grid; entries are (path, width).

GLYPHS = {
    "A": ("M4 100L32 0L60 100M14 68H50", 64),
    "B": ("M6 0V100M6 0H32C50 0 50 48 32 48H6M32 48C56 48 56 100 30 100H6", 56),
    "C": ("M52 16A30 50 0 1 0 52 84", 60),
    "E": ("M44 0H6V100H44M6 50H36", 48),
    "H": ("M6 0V100M54 0V100M6 50H54", 60),
    "I": ("M6 0V100", 12),
    "L": ("M6 0V100H42", 44),
    "M": ("M6 100V0L38 62L70 0V100", 76),
    "N": ("M6 100V0L54 100V0", 60),
    "O": ("M35 0A31 50 0 1 0 35 100A31 50 0 1 0 35 0", 70),
    "P": ("M6 100V0H30C52 0 52 54 30 54H6", 54),
    "R": ("M6 100V0H30C52 0 52 54 30 54H6M30 54L52 100", 58),
    "S": ("M46 18C40 -2 6 -2 6 26C6 52 46 46 46 74C46 104 10 104 4 80", 52),
    "T": ("M2 0H54M28 0V100", 56),
    "U": ("M6 0V62C6 108 52 108 52 62V0", 58),
    "V": ("M2 0L30 100L58 0", 60),
    "W": ("M2 0L21 100L42 30L63 100L82 0", 84),
    "Y": ("M2 0L29 54L56 0M29 54V100", 58),
    "'": ("M7 0V26", 14),
    " ": ("", 34),
}


def glyph_run(text, centre_deg, r_mid, H, gap, top, col, sw=10):
    """Text along a circle. top=True reads clockwise over the top, letters standing outward;
    top=False reads left to right along the bottom, letters standing inward."""
    u = H / 100.0
    advs = [GLYPHS[ch][1] * u for ch in text]
    total = sum(advs) + gap * u * (len(text) - 1)
    s = -total / 2
    out = ['<g fill="none" stroke="%s" stroke-width="%g" stroke-linecap="round" stroke-linejoin="round">' % (col, sw)]
    for ch, adv in zip(text, advs):
        d, w = GLYPHS[ch]
        mid = s + adv / 2
        s += adv + gap * u
        if not d:
            continue
        ang = math.degrees(mid / r_mid)
        th = centre_deg + ang if top else centre_deg - ang
        rb = r_mid - H / 2 if top else r_mid + H / 2
        phi = th + 90 if top else th - 90
        px = C + rb * math.cos(math.radians(th))
        py = C + rb * math.sin(math.radians(th))
        out.append('<path transform="translate(%.2f %.2f) rotate(%.2f) scale(%.4f) translate(%g -100)" d="%s"/>' % (
            px, py, phi, u, -w / 2, d))
    out.append("</g>")
    return "".join(out), math.degrees(total / r_mid)


def guilloche(r, amp, n, phase, col, w=0.8, op=0.22, steps=900):
    pts = []
    for i in range(steps + 1):
        t = 2 * math.pi * i / steps
        rr = r + amp * math.sin(n * t + phase)
        pts.append("%.2f,%.2f" % (C + rr * math.cos(t), C + rr * math.sin(t)))
    return '<polyline points="%s" fill="none" stroke="%s" stroke-width="%g" opacity="%g"/>' % (" ".join(pts), col, w, op)


LAND = os.path.join(ROOT, "tools", "earth_land_110m.json")  # Natural Earth 110m land, public domain
GLOBE_LON, GLOBE_LAT = 15.0, 18.0  # Africa and Europe face the viewer (Accra, Kai's home, is on the near side)


def globe_land(cx, cy, r, lon0=GLOBE_LON, lat0=GLOBE_LAT):
    """Land as one SVG path in orthographic projection. Points on the far side are pushed to the
    limb so every polygon stays closed; the caller clips to the globe circle."""
    import json
    with open(LAND, encoding="utf-8") as f:
        feats = json.load(f)["features"]
    l0, p0 = math.radians(lon0), math.radians(lat0)
    d = []
    for ft in feats:
        g = ft["geometry"]
        polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        for poly in polys:
            for ring in poly:
                pts, vis = [], False
                for lon, lat in ring:
                    la, lo = math.radians(lat), math.radians(lon) - l0
                    x = math.cos(la) * math.sin(lo)
                    y = math.cos(p0) * math.sin(la) - math.sin(p0) * math.cos(la) * math.cos(lo)
                    z = math.sin(p0) * math.sin(la) + math.cos(p0) * math.cos(la) * math.cos(lo)
                    if z >= 0:
                        vis = True
                    else:
                        n = math.hypot(x, y) or 1.0
                        x, y = x / n, y / n
                    pts.append((cx + r * x, cy - r * y))
                if vis:
                    d.append("M" + "L".join("%.2f %.2f" % q for q in pts) + "Z")
    return "".join(d)


def title_ics(cx, cy, h, fill, halo, sw, halo_w):
    """ICS across the middle, in the monoline glyphs, with a halo so it reads over land and sea."""
    u = h / 100.0
    gap = 16 * u
    ws = [GLYPHS[c][1] * u for c in "ICS"]
    x = cx - (sum(ws) + 2 * gap) / 2
    out = []
    for width, col in ((halo_w, halo), (sw, fill)):
        out.append('<g fill="none" stroke="%s" stroke-width="%g" stroke-linecap="round" stroke-linejoin="round">' % (col, width))
        xx = x
        for c, w in zip("ICS", ws):
            out.append('<path transform="translate(%.2f %.2f) scale(%.4f)" d="%s"/>' % (
                xx, cy - h / 2, u, GLYPHS[c][0]))
            xx += w + gap
        out.append("</g>")
    return "".join(out)


def emblem(uid, mono=False):
    blue, gold, paper = BLUE, GOLD, PAPER
    o = []
    H, R_MID = 20, 172
    top_txt, bot_txt = "INTERPLANETARY CORPORATE", "SOLUTIONS"
    GR = 112  # globe radius

    if not mono:
        o.append('<circle cx="200" cy="200" r="195" fill="none" stroke="%s" stroke-width="2.5"/>' % gold)
        o.append('<circle cx="200" cy="200" r="170" fill="none" stroke="%s" stroke-width="38"/>' % blue)
        o.append('<circle cx="200" cy="200" r="151" fill="%s"/>' % paper)
        o.append('<circle cx="200" cy="200" r="187" fill="none" stroke="%s" stroke-width="1.2"/>' % gold)
        o.append('<circle cx="200" cy="200" r="153" fill="none" stroke="%s" stroke-width="1.2"/>' % gold)
        txt_col, ink, tick_col = paper, blue, blue
    else:
        o.append('<circle cx="200" cy="200" r="195" fill="none" stroke="%s" stroke-width="3"/>' % blue)
        o.append('<circle cx="200" cy="200" r="187" fill="none" stroke="%s" stroke-width="1.6"/>' % blue)
        o.append('<circle cx="200" cy="200" r="153" fill="none" stroke="%s" stroke-width="1.6"/>' % blue)
        txt_col, ink, tick_col = blue, blue, blue

    t1, span_t = glyph_run(top_txt, 270, R_MID, H, 8, True, txt_col, sw=9)
    t2, span_b = glyph_run(bot_txt, 90, R_MID, H, 40, False, txt_col, sw=9)
    o += [t1, t2]

    # separators in the two gaps between the runs
    a, b = span_t / 2, span_b / 2
    for sep in (180 + (b - a) / 2, (a - b) / 2):
        for off, rad in ((-6, 1.6), (0, 3.2), (6, 1.6)):
            ang = math.radians(sep + off * 1.0)
            o.append('<circle cx="%.2f" cy="%.2f" r="%g" fill="%s"/>' % (
                C + R_MID * math.cos(ang), C + R_MID * math.sin(ang), rad, ink if mono else gold))

    # 349 ticks: 348 Labor Sources before Earth, and Earth. The last, longer, sits at the base under the globe.
    n = 349
    for i in range(n):
        th = math.radians(90 + (i - (n - 1)) * 360.0 / n)
        last = i == n - 1
        r1, r2 = (136, 150) if last else (141, 148)
        col = (ink if mono else gold) if last else tick_col
        o.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="%s" stroke-width="%g" stroke-linecap="round"/>' % (
            C + r1 * math.cos(th), C + r1 * math.sin(th), C + r2 * math.cos(th), C + r2 * math.sin(th),
            col, 1.6 if last else 0.7))

    # a banknote weave in the ring between the globe and the ticks
    if not mono:
        def band(mid, amp, n, count, col, w, op):
            for k in range(count):
                o.append(guilloche(mid, amp, n, 2 * math.pi * k / (n * count) * n, col, w=w, op=op, steps=1600))
        band(128, 5, 48, 10, blue, 0.35, 0.40)
        band(128, 5, 48, 4, gold, 0.5, 0.55)

    # the globe: Earth in orthographic projection, then the title across its middle
    clip = "gl" + uid
    o.append('<defs><clipPath id="%s"><circle cx="200" cy="200" r="%g"/></clipPath></defs>' % (clip, GR))
    land = globe_land(200, 200, GR)
    if not mono:
        o.append('<circle cx="200" cy="200" r="%g" fill="%s"/>' % (GR, blue))
        o.append('<path clip-path="url(#%s)" d="%s" fill="%s" stroke="%s" stroke-width="0.8" stroke-linejoin="round"/>' % (clip, land, paper, paper))
        o.append('<circle cx="200" cy="200" r="%g" fill="none" stroke="%s" stroke-width="3"/>' % (GR + 2, gold))
        o.append(title_ics(200, 200, 62, gold, blue, 13, 27))
    else:
        o.append('<circle cx="200" cy="200" r="%g" fill="none" stroke="%s" stroke-width="3"/>' % (GR, blue))
        o.append('<path clip-path="url(#%s)" d="%s" fill="%s"/>' % (clip, land, blue))
        o.append(title_ics(200, 200, 62, blue, "#ffffff", 13, 27))
    return (0, 0, 400, 400), "".join(o)



def main():
    want_png = "--png" in sys.argv
    files = []

    def add(name, vb_inner, png_w=None, transparent=True):
        vb, inner = vb_inner
        files.append((name, vb, inner, png_w, transparent))

    add("ics-mark.svg", solo("a", STD, BLUE, GOLD), 1024)
    add("ics-mark-reversed.svg", solo("b", STD, PAPER, GOLD))
    add("ics-mark-mono-blue.svg", solo("c", STD, BLUE, BLUE))
    add("ics-mark-mono-white.svg", solo("d", STD, WHITE, WHITE))
    add("ics-mark-small.svg", solo("e", SMALL, BLUE, GOLD), 256)
    add("ics-lockup-horizontal.svg", lockup_h("f", STD, BLUE, GOLD, BLUE), 2000)
    add("ics-lockup-horizontal-reversed.svg", lockup_h("g", STD, PAPER, GOLD, PAPER))
    add("ics-lockup-stacked.svg", lockup_v("h", STD, BLUE, GOLD, BLUE), 1000)
    add("ics-ring-only.svg", solo("i", STD, BLUE, GOLD, arc=False))
    add("ics-arc-only.svg", solo("j", STD, BLUE, GOLD, ring=False))
    add("ics-emblem.svg", emblem("em1"), 1600)
    add("ics-emblem-mono.svg", emblem("em2", mono=True), 1200)
    add("ics-logo-sheet.svg", sheet(), 1600, False)

    for name, vb, inner, png_w, transparent in files:
        path = write(name, vb, inner)
        print("svg", os.path.relpath(path, ROOT))
        if want_png and png_w:
            render(name[:-4] + ".png", vb, inner, png_w, transparent)


if __name__ == "__main__":
    main()
