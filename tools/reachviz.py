#!/usr/bin/env python3
"""Reach illustration library — gradient-body figures on annotated plates.

Figures are volumetric ribbons (tapered closed shapes) over pose skeletons
in figure-local coordinates (y up, ground at y = 0). The body carries a
radial gradient anchored at the pelvis: darkest at the core, fading to
lavender at the extremities. Far-side limbs render as pale flat shapes.

Each move renders twice:
  images/<id>.png        800x500 plate with title + cue annotations (player)
  images/thumbs/<id>.png 800x500 figure only, larger in frame (small slots)
"""

import math
from xml.sax.saxutils import escape

W, H = 800, 500
INK = "#1B1C16"
PAPER = "#F3F5EF"
PURPLE = "#6D4AA0"
PURPLE_DK = "#5A3C87"
LAV_MID = "#C5B4E0"
LAV_PALE = "#E4DDF1"
GRAY = "#8A8E7E"
HATCH = "#C9CDBC"

MONO = "DejaVu Sans Mono, monospace"

# half-width profiles per chain role, hip/root end first
PROFILES = {
    "S": [0.235, 0.19, 0.145],     # spine: hip -> shoulders (auto-oriented)
    "L": [0.215, 0.13, 0.075, 0.048],
    "l": [0.215, 0.13, 0.075, 0.048],
    "A": [0.115, 0.088, 0.052],
    "a": [0.115, 0.088, 0.052],
    "H": [0.06, 0.045],            # hand / thin end segment
    "h": [0.06, 0.045],
}
FAR_ROLES = ("l", "a", "h")
HEAD_R = 0.55


def _cr(p0, p1, p2, p3, t):
    t2, t3 = t * t, t * t * t
    return (
        0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t
               + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
               + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3),
        0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t
               + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
               + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3),
    )


def sample_chain(pts, per=26):
    if len(pts) == 2:
        return [(pts[0][0] + (pts[1][0] - pts[0][0]) * i / per,
                 pts[0][1] + (pts[1][1] - pts[0][1]) * i / per, i / per)
                for i in range(per + 1)]
    p = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    nseg = len(pts) - 1
    for i in range(1, len(p) - 2):
        for k in range(per):
            t = k / per
            x, y = _cr(p[i - 1], p[i], p[i + 1], p[i + 2], t)
            out.append((x, y, (i - 1 + t) / nseg))
    out.append((pts[-1][0], pts[-1][1], 1.0))
    return out


def resample_profile(profile, n):
    if n <= 1:
        return [profile[0]]
    out = []
    for i in range(n):
        t = i / (n - 1) * (len(profile) - 1)
        j = min(int(t), len(profile) - 2)
        f = t - j
        out.append(profile[j] * (1 - f) + profile[j + 1] * f)
    return out


def frame_bbox(frame):
    xs, ys = [], []
    for ch in frame["chains"]:
        pad = max(PROFILES.get(ch.get("role", "A"), [0.1])[0],
                  max(ch.get("widths", [0])) if ch.get("widths") else 0)
        for (x, y) in ch["pts"]:
            xs += [x - pad, x + pad]
            ys += [y - pad, y + pad]
    for prop in frame.get("props", []):
        for (x, y) in prop:
            xs.append(x)
            ys.append(y)
    hx, hy = frame["head"]
    r = frame.get("head_r", HEAD_R)
    xs += [hx - r, hx + r]
    ys += [hy - r, hy + r]
    if frame.get("ground"):
        ys.append(0.0)
    return min(xs), max(xs), min(ys), max(ys)


class FrameRenderer:
    def __init__(self, frame, cx, cy, avail_w, avail_h, gid, scale=None):
        self.f = frame
        x0, x1, y0, y1 = frame_bbox(frame)
        self.s = scale or min(avail_w / max(x1 - x0, 0.1),
                              avail_h / max(y1 - y0, 0.1))
        self.cx = cx - (x0 + x1) / 2 * self.s
        self.cy = cy + (y0 + y1) / 2 * self.s
        self.gid = gid

    def T(self, p):
        return (self.cx + p[0] * self.s, self.cy - p[1] * self.s)

    def ribbon_d(self, pts_local, widths):
        pts = [self.T(p) for p in pts_local]
        ws = [w * self.s for w in widths]
        smp = sample_chain(pts)
        nw = len(ws)
        left, right = [], []
        for j, (x, y, u) in enumerate(smp):
            j0 = min(int(u * (nw - 1)), nw - 2) if nw > 1 else 0
            f = u * (nw - 1) - j0 if nw > 1 else 0.0
            w = ws[j0] * (1 - f) + (ws[j0 + 1] if nw > 1 else ws[0]) * f
            a = smp[max(j - 1, 0)]
            b = smp[min(j + 1, len(smp) - 1)]
            dx, dy = b[0] - a[0], b[1] - a[1]
            n = math.hypot(dx, dy) or 1.0
            nx, ny = -dy / n, dx / n
            left.append((x + nx * w, y + ny * w))
            right.append((x - nx * w, y - ny * w))
        poly = left + right[::-1]
        return "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in poly) + " Z"

    def spine_hip_end(self):
        """Hip end of the spine chain = gradient anchor."""
        for ch in self.f["chains"]:
            if ch.get("role") == "S":
                pts = ch["pts"]
                hx, hy = self.f["head"]
                d0 = math.hypot(pts[0][0] - hx, pts[0][1] - hy)
                d1 = math.hypot(pts[-1][0] - hx, pts[-1][1] - hy)
                return pts[-1] if d0 < d1 else pts[0], (pts[0] if d0 < d1 else pts[-1])
        first = self.f["chains"][0]["pts"]
        return first[0], first[-1]

    def chain_widths(self, ch):
        if ch.get("widths"):
            return ch["widths"]
        role = ch.get("role", "A")
        prof = PROFILES.get(role, PROFILES["A"])
        ws = resample_profile(prof, len(ch["pts"]))
        if role == "S":
            # orient: head end thin
            hip, _ = self.spine_hip_end()
            if ch["pts"][0] != hip:
                ws = ws[::-1]
        return ws

    def gradient_def(self):
        hip, _ = self.spine_hip_end()
        gx, gy = self.T(hip)
        r = 5.5 * self.s
        return (f'<radialGradient id="{self.gid}" gradientUnits="userSpaceOnUse" '
                f'cx="{gx:.0f}" cy="{gy:.0f}" r="{r:.0f}">'
                f'<stop offset="0" stop-color="{PURPLE_DK}"/>'
                f'<stop offset="0.45" stop-color="{PURPLE}"/>'
                f'<stop offset="1" stop-color="{LAV_MID}"/></radialGradient>')

    def render(self):
        els = []
        f = self.f
        fill = f"url(#{self.gid})"

        if f.get("ground"):
            gy = self.T((0, 0))[1]
            x0, x1, _, _ = frame_bbox(f)
            g0 = self.T((x0 - 0.35, 0))[0]
            g1 = self.T((x1 + 0.35, 0))[0]
            # shadow under the body's floor contacts
            contacts = [p[0] for ch in f["chains"] for p in ch["pts"] if p[1] < 0.4]
            if contacts:
                a = self.T((min(contacts) - 0.3, 0))[0]
                b = self.T((max(contacts) + 0.3, 0))[0]
                els.append(f'<ellipse cx="{(a + b) / 2:.0f}" cy="{gy + 13:.0f}" '
                           f'rx="{max((b - a) / 2, 30):.0f}" ry="10" fill="{LAV_PALE}"/>')
            els.append(f'<line x1="{g0:.0f}" y1="{gy:.0f}" x2="{g1:.0f}" '
                       f'y2="{gy:.0f}" stroke="{GRAY}" stroke-width="2.4"/>')
            for edge, step in ((g0 + 8, 1), (g1 - 62, 1)):
                hx = edge
                while hx < edge + 54:
                    els.append(f'<line x1="{hx:.0f}" y1="{gy + 4:.0f}" '
                               f'x2="{hx - 10:.0f}" y2="{gy + 14:.0f}" '
                               f'stroke="{HATCH}" stroke-width="1.2"/>')
                    hx += 22

        for prop in f.get("props", []):
            pts = [self.T(p) for p in prop]
            d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
            els.append(f'<path d="{d}" fill="none" stroke="{INK}" '
                       f'stroke-width="3.4" stroke-linecap="round" '
                       f'stroke-linejoin="round"/>')

        far = [c for c in f["chains"] if c.get("role") in FAR_ROLES]
        near = [c for c in f["chains"] if c.get("role") not in FAR_ROLES]
        for ch in far:
            els.append(f'<path d="{self.ribbon_d(ch["pts"], self.chain_widths(ch))}" '
                       f'fill="{LAV_PALE}"/>')
        for ch in near:
            els.append(f'<path d="{self.ribbon_d(ch["pts"], self.chain_widths(ch))}" '
                       f'fill="{fill}"/>')

        # neck: from the spine's head end toward the head circle
        hip, neck_end = self.spine_hip_end()
        hx, hy = f["head"]
        r = f.get("head_r", HEAD_R)
        dx, dy = hx - neck_end[0], hy - neck_end[1]
        dist = math.hypot(dx, dy)
        if dist > r * 1.02:
            stop = 1 - (r + 0.1) / dist
            nk = [neck_end, (neck_end[0] + dx * stop, neck_end[1] + dy * stop)]
            els.append(f'<path d="{self.ribbon_d(nk, [0.115, 0.095])}" fill="{fill}"/>')

        cx_, cy_ = self.T((hx, hy))
        els.append(f'<circle cx="{cx_:.1f}" cy="{cy_:.1f}" r="{r * self.s:.1f}" '
                   f'fill="{fill}"/>')

        for (a, b) in f.get("dash", []):
            p0, p1 = self.T(a), self.T(b)
            els.append(f'<line x1="{p0[0]:.0f}" y1="{p0[1]:.0f}" x2="{p1[0]:.0f}" '
                       f'y2="{p1[1]:.0f}" stroke="{PURPLE_DK}" stroke-width="2" '
                       f'stroke-dasharray="1 9" stroke-linecap="round" opacity="0.85"/>')

        for (ax, ay, ddx, ddy) in f.get("arrows", []):
            x0, y0 = self.T((ax, ay))
            n = math.hypot(ddx, ddy) or 1.0
            ux, uy = ddx / n, -ddy / n
            x1, y1 = x0 + ux * 44, y0 + uy * 44
            ang = math.atan2(y1 - y0, x1 - x0)
            a1, a2 = ang + math.radians(150), ang - math.radians(150)
            els.append(
                f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
                f'stroke="{PURPLE}" stroke-width="4" stroke-linecap="round"/>'
                f'<path d="M {x1 + 12 * math.cos(a1):.1f} {y1 + 12 * math.sin(a1):.1f} '
                f'L {x1:.1f} {y1:.1f} L {x1 + 12 * math.cos(a2):.1f} '
                f'{y1 + 12 * math.sin(a2):.1f}" fill="none" stroke="{PURPLE}" '
                f'stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')

        return els


# ------------------------------------------------------------------- text

def text_el(x, y, s, size=13, fill=INK, spacing=2, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" '
            f'fill="{fill}" letter-spacing="{spacing}" '
            f'text-anchor="{anchor}">{escape(s)}</text>')


def wrap_text(s, max_chars):
    words = s.split()
    lines, cur = [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > max_chars:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


# ------------------------------------------------------------------ moves

def midframe_arrow(cx, cy):
    return (f'<line x1="{cx - 26}" y1="{cy}" x2="{cx + 26}" y2="{cy}" '
            f'stroke="{PURPLE}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M {cx + 13} {cy - 12} L {cx + 26} {cy} L {cx + 13} {cy + 12}" '
            f'fill="none" stroke="{PURPLE}" stroke-width="5" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


SLOTS = {
    # layout: [(cx, cy, avail_w, avail_h)], arrow positions
    "static": {"full": [(400, 268, 620, 320)], "thumb": [(400, 252, 690, 420)]},
    "two": {"full": [(212, 268, 292, 300), (588, 268, 292, 300)],
            "thumb": [(206, 252, 328, 390), (594, 252, 328, 390)]},
    "tri": {"full": [(152, 268, 206, 300), (400, 268, 206, 300), (648, 268, 206, 300)],
            "thumb": [(146, 252, 224, 380), (400, 252, 224, 380), (654, 252, 224, 380)]},
}


def render_move(move, annotated=True):
    layout = move.get("layout", "static")
    slots = SLOTS[layout]["full" if annotated else "thumb"]
    frames = move["frames"]

    renderers = []
    shared = None
    if len(frames) > 1:
        # same scale across frames so the figure doesn't jump sizes
        shared = min(
            FrameRenderer(f, *slot, gid=f"g{i}").s
            for i, (f, slot) in enumerate(zip(frames, slots))
        )
    for i, (f, slot) in enumerate(zip(frames, slots)):
        renderers.append(FrameRenderer(f, *slot, gid=f"g{i}", scale=shared))
    if len(renderers) > 1 and all(f.get("ground") for f in frames):
        base = max(r.T((0, 0))[1] for r in renderers)
        for r in renderers:
            r.cy += base - r.T((0, 0))[1]

    defs = "".join(r.gradient_def() for r in renderers)
    els = []
    for r in renderers:
        els += r.render()

    if len(frames) == 2:
        els.append(midframe_arrow(400, slots[0][1]))
    if layout == "tri" and annotated:
        for label, (cx, cy, _, _) in zip(("Y", "T", "W"), slots):
            els.append(text_el(cx, 472, label, 17, GRAY, 3, "middle"))

    if annotated:
        els.append(text_el(56, 60, move["name"].upper(), 17, INK, 3.5))
        cue = move.get("cue", "")
        if cue:
            lines = wrap_text(cue.upper(), 60)[:2]
            base_y = 462 - (len(lines) - 1) * 22
            for i, ln in enumerate(lines):
                els.append(text_el(56, base_y + i * 22, ln, 15, GRAY, 2))
        for co in move.get("callouts", []):
            els += render_callout(renderers[0], co)

    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}"><defs>{defs}</defs>'
            f'<rect width="{W}" height="{H}" fill="{PAPER}"/>'
            + "".join(els) + "</svg>")


def render_callout(r, co):
    """co: {"anchor": (x,y) figure-local, "at": (tx,ty) canvas,
            "lines": [...], "align": "start"|"end"}"""
    ax, ay = r.T(co["anchor"])
    tx, ty = co["at"]
    align = co.get("align", "start")
    join_x = tx - 8 if align == "start" else tx + 8
    off = 16 if tx > ax else -16
    route = [(ax + off, ay), (join_x + (-14 if align == "start" else 14), ty - 4),
             (join_x, ty - 4)]
    d = "M " + " L ".join(f"{x:.0f} {y:.0f}" for x, y in route)
    els = [f'<path d="{d}" fill="none" stroke="{GRAY}" stroke-width="1.1"/>']
    for i, ln in enumerate(co["lines"]):
        fill = INK if i == 0 else GRAY
        els.append(text_el(tx, ty + i * 20, ln.upper(), 14.5, fill, 1.5, align))
    return els
