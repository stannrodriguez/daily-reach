#!/usr/bin/env python3
"""Generate the Reach move illustrations.

One 800x500 PNG per move id, minimal single-line ink style:
ink #1B1C16 on paper #F3F5EF, uniform line weight, centered figure,
no shading, no text. Dynamic reps render two frames (start -> end)
with a small arrow between; ytw renders three small figures.

Poses are authored as simple stick skeletons in figure-local
coordinates (y up, ground at y=0) and smoothed into flowing strokes.
"""

import math
import os

import cairosvg

W, H = 800, 500
INK = "#1B1C16"
PAPER = "#F3F5EF"
STROKE = 6.5
GROUND_STROKE = 4.5
HEAD_R = 0.75

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images")


# --------------------------------------------------------------- geometry

def catmull_path(pts):
    """Smooth polyline -> cubic bezier SVG path."""
    if len(pts) == 2:
        (x0, y0), (x1, y1) = pts
        return f"M {x0:.1f} {y0:.1f} L {x1:.1f} {y1:.1f}"
    p = [pts[0]] + list(pts) + [pts[-1]]
    d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6.0, p1[1] + (p2[1] - p0[1]) / 6.0)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6.0, p2[1] - (p3[1] - p1[1]) / 6.0)
        d += (f" C {c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f}"
              f" {p2[0]:.1f} {p2[1]:.1f}")
    return d


def pose_bbox(pose):
    xs, ys = [], []
    for path in pose.get("paths", []) + pose.get("props", []):
        for (x, y) in path:
            xs.append(x)
            ys.append(y)
    if "head" in pose:
        hx, hy = pose["head"]
        r = pose.get("head_r", HEAD_R)
        xs += [hx - r, hx + r]
        ys += [hy - r, hy + r]
    if pose.get("ground"):
        ys.append(0.0)
    return min(xs), min(ys), max(xs), max(ys)


def render_pose(pose, cx, cy, avail_w, avail_h, cap):
    """Return SVG elements for one pose fitted into a slot centred at (cx, cy)."""
    x0, y0, x1, y1 = pose_bbox(pose)
    bw, bh = max(x1 - x0, 0.1), max(y1 - y0, 0.1)
    s = min(cap, avail_w / bw, avail_h / bh)
    mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0

    def T(pt):
        return (cx + (pt[0] - mx) * s, cy - (pt[1] - my) * s)

    els = []
    if pose.get("ground"):
        g0, g1 = T((x0 - 0.45, 0.0)), T((x1 + 0.45, 0.0))
        els.append(
            f'<line x1="{g0[0]:.1f}" y1="{g0[1]:.1f}" x2="{g1[0]:.1f}" '
            f'y2="{g1[1]:.1f}" stroke="{INK}" stroke-width="{GROUND_STROKE}" '
            f'stroke-linecap="round"/>')
    for prop in pose.get("props", []):
        tp = [T(p) for p in prop]
        d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in tp)
        els.append(
            f'<path d="{d}" fill="none" stroke="{INK}" '
            f'stroke-width="{STROKE}" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')
    for path in pose.get("paths", []):
        d = catmull_path([T(p) for p in path])
        els.append(
            f'<path d="{d}" fill="none" stroke="{INK}" '
            f'stroke-width="{STROKE}" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')
    if "head" in pose:
        hx, hy = T(pose["head"])
        r = pose.get("head_r", HEAD_R) * s
        els.append(
            f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{r:.1f}" fill="none" '
            f'stroke="{INK}" stroke-width="{STROKE}"/>')
    return els


def arrow(cx, cy):
    return [
        f'<line x1="{cx-24}" y1="{cy}" x2="{cx+24}" y2="{cy}" stroke="{INK}" '
        f'stroke-width="5" stroke-linecap="round"/>',
        f'<path d="M {cx+12} {cy-11} L {cx+24} {cy} L {cx+12} {cy+11}" '
        f'fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" '
        f'stroke-linejoin="round"/>',
    ]


def make_svg(frames):
    """frames: list of (pose, cx, cy, avail_w, avail_h, cap). Arrows between."""
    els = [f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    for f in frames:
        els += render_pose(*f)
    if len(frames) == 2:
        els += arrow(W / 2, H / 2)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
            f'height="{H}" viewBox="0 0 {W} {H}">' + "".join(els) + "</svg>")


# ------------------------------------------------------------------ poses
# Figure-local coords: y up, ground at y=0, figure faces right.
# Reference standing skeleton: hip (0,3.7)  shoulder (0,6.7)  head (0,7.8).

def stand_side(arm_pts=None, ground=True):
    pose = {
        "head": (0.05, 7.8),
        "paths": [
            [(0.05, 7.15), (0, 6.7), (0, 3.7)],                     # spine
            [(0, 3.7), (0.1, 1.85), (0.15, 0.12), (0.8, 0.1)],      # leg 1
            [(0, 3.7), (-0.12, 1.85), (-0.12, 0.12), (0.5, 0.1)],   # leg 2
        ],
        "ground": ground,
    }
    if arm_pts is None:
        arm_pts = [[(0, 6.7), (0.2, 5.3), (0.25, 3.95)]]
    pose["paths"] += arm_pts
    return pose


def stand_front(head=(0, 7.8), arms=None):
    pose = {
        "head": head,
        "paths": [
            [(0, 7.15), (0, 6.7), (0, 3.7)],
            [(0, 3.7), (-0.3, 1.85), (-0.4, 0.12), (-0.85, 0.08)],
            [(0, 3.7), (0.3, 1.85), (0.4, 0.12), (0.85, 0.08)],
        ],
        "ground": True,
    }
    if arms is None:
        arms = [[(0, 6.7), (-0.55, 5.3), (-0.65, 3.95)],
                [(0, 6.7), (0.55, 5.3), (0.65, 3.95)]]
    pose["paths"] += arms
    return pose


def tabletop(spine_mid=(0.0, 2.3), head=(2.25, 2.95), arm=None, legs=None):
    pose = {
        "head": head,
        "paths": [
            [(2.0, 2.7), (1.4, 2.35), spine_mid, (-1.4, 2.2)],
            arm or [(1.4, 2.35), (1.45, 1.2), (1.5, 0.12)],
        ],
        "ground": True,
    }
    pose["paths"] += legs or [
        [(-1.4, 2.2), (-1.5, 0.35), (-3.2, 0.28), (-3.8, 0.2)],
    ]
    return pose


def high_plank():
    return {
        "head": (1.06, 3.2),
        "paths": [
            [(0.75, 3.1), (0, 2.9), (-2.7, 2.2)],
            [(0, 2.9), (0.03, 1.5), (0.05, 0.12)],
            [(-0.22, 2.85), (-0.2, 1.5), (-0.18, 0.12)],
            [(-2.7, 2.2), (-4.5, 1.4), (-6.2, 0.6), (-6.6, 0.15)],
        ],
        "ground": True,
    }


def down_dog(lifted_leg=False):
    pose = {
        "head": (2.5, 1.6),
        "paths": [
            [(0.6, 3.15), (-0.1, 4.15)],                 # neck->hip merged below
            [(-0.1, 4.15), (0.6, 3.15), (1.75, 1.9)],    # spine
            [(1.75, 1.9), (2.35, 1.0), (2.9, 0.12)],     # arm
            [(1.6, 1.85), (2.15, 0.95), (2.65, 0.12)],   # far arm
        ],
        "ground": True,
    }
    legs = [[(-0.1, 4.15), (-1.3, 2.3), (-2.4, 0.5), (-1.85, 0.12)]]
    if lifted_leg:
        legs = [
            [(-0.1, 4.15), (-1.35, 2.35), (-2.45, 0.55), (-1.9, 0.12)],
            [(-0.1, 4.15), (-1.35, 5.55), (-2.5, 6.9), (-2.9, 7.0)],
        ]
    pose["paths"] += legs
    return pose


def hang(sh=(0, 6.7), hip=(0.1, 3.7), legs=None, head=(0, 7.7),
         arms=None, bar_y=9.65, bar_gap=None):
    pose = {
        "head": head,
        "paths": [
            [head, sh, hip] if False else [(head[0], head[1] - 0.65), sh, hip],
        ],
        "ground": False,
    }
    pose["paths"] += arms or [
        [sh, (0.15, 8.15), (0.28, 9.55)],
        [sh, (-0.12, 8.15), (-0.25, 9.55)],
    ]
    pose["paths"] += legs or [
        [hip, (0.2, 1.85), (0.12, 0.5), (0.35, 0.12)],
        [hip, (0.35, 1.9), (0.3, 0.55), (0.55, 0.2)],
    ]
    if bar_gap:
        g0, g1 = bar_gap
        pose["props"] = [[(-1.9, bar_y), (g0, bar_y)], [(g1, bar_y), (1.9, bar_y)]]
    else:
        pose["props"] = [[(-1.9, bar_y), (1.9, bar_y)]]
    return pose


def pullup_top():
    return hang(
        sh=(-0.1, 8.55), hip=(0.15, 5.6),
        head=(0.45, 9.3),
        arms=[[(-0.1, 8.55), (0.75, 8.0), (0.3, 9.55)],
              [(-0.25, 8.5), (0.55, 7.95), (0.1, 9.55)]],
        legs=[[(0.15, 5.6), (0.4, 3.8), (0.3, 2.0), (0.55, 1.7)],
              [(0.15, 5.6), (0.55, 3.85), (0.45, 2.05), (0.7, 1.78)]],
        bar_gap=(-0.45, 1.35),
    )


def bridge_down(free_leg=None):
    pose = {
        "head": (-3.75, 0.78),
        "paths": [
            [(-3.15, 0.62), (-2.9, 0.6), (-0.3, 0.7)],
            [(-2.9, 0.6), (-1.55, 0.45), (-0.2, 0.38)],
            [(-0.3, 0.7), (1.2, 2.1), (1.35, 0.25), (2.0, 0.12)],
        ],
        "ground": True,
    }
    if free_leg:
        pose["paths"].append(free_leg)
    return pose


def bridge_up(free_leg=None):
    pose = {
        "head": (-3.75, 0.78),
        "paths": [
            [(-3.15, 0.62), (-2.9, 0.6), (-0.5, 1.5)],
            [(-2.9, 0.6), (-1.6, 0.5), (-0.35, 0.4)],
            [(-0.5, 1.5), (1.05, 2.0), (1.3, 0.25), (1.95, 0.12)],
        ],
        "ground": True,
    }
    if free_leg:
        pose["paths"].append(free_leg)
    return pose


POSES = {}

# ----- yoga statics -----

POSES["mountain"] = stand_side(
    arm_pts=[[(0, 6.7), (0.22, 5.3), (0.28, 3.95)],
             [(0, 6.7), (-0.18, 5.3), (-0.22, 3.95)]])

POSES["childs_pose"] = {
    "head": (2.25, 0.78),
    "paths": [
        [(1.55, 0.72), (1.0, 0.75), (-1.0, 1.15), (-1.85, 0.9)],   # spine fold
        [(-1.85, 0.9), (-1.75, 0.3), (-3.4, 0.3), (-4.0, 0.22)],   # folded legs
        [(1.0, 0.75), (2.3, 0.35), (3.7, 0.15)],                   # arm forward
        [(0.95, 0.62), (2.2, 0.25), (3.5, 0.1)],                   # far arm
    ],
    "ground": True,
}

POSES["down_dog"] = down_dog()

POSES["forward_fold"] = {
    "head": (1.42, 0.95),
    "paths": [
        [(0, 3.7), (0.9, 2.9), (1.25, 1.6)],
        [(0, 3.7), (0.08, 1.85), (0.12, 0.12), (0.75, 0.1)],
        [(0, 3.7), (-0.15, 1.85), (-0.15, 0.12), (0.45, 0.1)],
        [(1.25, 1.6), (1.05, 0.85), (0.9, 0.15)],
        [(1.1, 1.55), (0.9, 0.8), (0.72, 0.12)],
    ],
    "ground": True,
}

POSES["halfway_lift"] = {
    "head": (3.75, 4.3),
    "paths": [
        [(3.35, 4.25), (2.95, 4.1), (0, 3.7)],
        [(0, 3.7), (0.08, 1.85), (0.12, 0.12), (0.75, 0.1)],
        [(0, 3.7), (-0.15, 1.85), (-0.15, 0.12), (0.45, 0.1)],
        [(2.95, 4.1), (2.0, 3.0), (1.0, 2.0)],
    ],
    "ground": True,
}

POSES["low_lunge"] = {
    "head": (0.28, 6.35),
    "paths": [
        [(0.25, 5.75), (0.15, 5.3), (0, 2.4)],
        [(0, 2.4), (1.4, 1.6), (1.5, 0.15), (2.2, 0.1)],           # front leg
        [(0, 2.4), (-1.6, 0.5), (-3.2, 0.3), (-3.8, 0.18)],        # back knee down
        [(0.15, 5.3), (0.45, 6.7), (0.6, 8.1)],
        [(0.15, 5.3), (0.05, 6.75), (0.1, 8.15)],
    ],
    "ground": True,
}

POSES["warrior1"] = {
    "head": (0.2, 7.0),
    "paths": [
        [(0.18, 6.4), (0.1, 5.9), (0, 2.9)],
        [(0, 2.9), (1.5, 1.6), (1.6, 0.15), (2.3, 0.1)],
        [(0, 2.9), (-1.4, 1.5), (-2.6, 0.2), (-3.25, 0.15)],
        [(0.1, 5.9), (0.4, 7.3), (0.55, 8.65)],
        [(0.1, 5.9), (-0.05, 7.32), (0.05, 8.68)],
    ],
    "ground": True,
}

POSES["warrior2"] = {
    "head": (0.05, 7.0),
    "paths": [
        [(0.05, 6.4), (0, 5.9), (0, 2.9)],
        [(0, 2.9), (1.5, 1.6), (1.7, 0.18), (2.4, 0.15)],
        [(0, 2.9), (-1.3, 1.5), (-2.6, 0.22), (-3.3, 0.2)],
        [(0, 5.9), (1.5, 5.97), (2.95, 6.0)],
        [(0, 5.9), (-1.5, 5.97), (-2.95, 6.0)],
    ],
    "ground": True,
}

POSES["triangle"] = {
    "head": (3.35, 5.4),
    "paths": [
        [(3.0, 5.22), (2.6, 4.9), (0, 3.5)],
        [(0, 3.5), (1.15, 1.8), (2.2, 0.15), (2.9, 0.12)],
        [(0, 3.5), (-1.15, 1.8), (-2.2, 0.15), (-2.85, 0.12)],
        [(2.6, 4.9), (2.5, 3.4), (2.35, 2.0)],
        [(2.6, 4.9), (2.7, 6.4), (2.78, 7.85)],
    ],
    "ground": True,
}

POSES["chair_pose"] = {
    "head": (0.62, 6.9),
    "paths": [
        [(0.55, 6.32), (0.35, 5.85), (-0.6, 3.0)],
        [(-0.6, 3.0), (0.75, 1.9), (0.32, 0.15), (1.0, 0.1)],
        [(-0.6, 3.0), (0.62, 1.82), (0.15, 0.12), (0.82, 0.08)],
        [(0.35, 5.85), (1.1, 7.1), (1.75, 8.3)],
        [(0.35, 5.85), (0.72, 7.18), (1.32, 8.42)],
    ],
    "ground": True,
}

POSES["tree_pose"] = {
    "head": (0, 7.8),
    "paths": [
        [(0, 7.15), (0, 6.7), (0, 3.7)],
        [(0, 3.7), (-0.08, 1.85), (-0.1, 0.12), (0.45, 0.08)],
        [(0, 3.7), (1.15, 2.7), (0.22, 2.95)],
        [(0, 6.7), (0.85, 7.85), (0.55, 9.0)],
        [(0, 6.7), (-0.85, 7.85), (-0.55, 9.0)],
    ],
    "ground": True,
}

POSES["cobra"] = {
    "head": (2.95, 3.2),
    "paths": [
        [(2.62, 2.75), (2.2, 2.4), (0.9, 1.2), (0, 0.55)],
        [(0, 0.55), (-1.9, 0.38), (-3.7, 0.28), (-4.3, 0.15)],
        [(0.05, 0.42), (-1.85, 0.26), (-3.6, 0.16), (-4.2, 0.05)],
        [(2.2, 2.4), (2.15, 1.3), (2.4, 0.12)],
    ],
    "ground": True,
}

POSES["sphinx"] = {
    "head": (2.4, 2.65),
    "paths": [
        [(2.1, 2.25), (1.7, 1.9), (0.75, 1.05), (0, 0.55)],
        [(0, 0.55), (-1.9, 0.38), (-3.7, 0.28), (-4.3, 0.15)],
        [(0.05, 0.42), (-1.85, 0.26), (-3.6, 0.16), (-4.2, 0.05)],
        [(1.7, 1.9), (1.85, 0.2), (3.2, 0.15)],
    ],
    "ground": True,
}

POSES["upward_dog"] = {
    "head": (2.6, 3.9),
    "paths": [
        [(2.3, 3.45), (1.9, 3.1), (0.7, 1.75), (0, 1.1)],
        [(0, 1.1), (-1.8, 0.7), (-3.5, 0.32), (-4.05, 0.12)],
        [(1.9, 3.1), (2.05, 1.6), (2.2, 0.15)],
        [(1.72, 3.02), (1.85, 1.55), (1.98, 0.12)],
    ],
    "ground": True,
}

POSES["pigeon"] = {
    "head": (0.35, 4.9),
    "paths": [
        [(0.32, 4.3), (0.2, 3.75), (0, 0.8)],
        [(0, 0.8), (1.6, 0.5), (0.5, 0.2)],
        [(0, 0.8), (-1.8, 0.42), (-3.4, 0.3), (-4.0, 0.16)],
        [(0.2, 3.75), (0.85, 2.4), (1.05, 0.95)],
        [(0.05, 3.7), (0.6, 2.35), (0.8, 0.92)],
    ],
    "ground": True,
}

POSES["seated_fold"] = {
    "head": (1.72, 2.3),
    "paths": [
        [(1.35, 2.32), (0.9, 2.2), (-0.7, 1.9), (-1.5, 0.75)],
        [(-1.5, 0.75), (0.3, 0.55), (2.0, 0.45), (2.3, 1.05)],
        [(-1.45, 0.62), (0.3, 0.42), (1.95, 0.32), (2.25, 0.9)],
        [(0.9, 2.2), (1.6, 1.5), (2.15, 0.85)],
    ],
    "ground": True,
}

POSES["butterfly"] = {
    "head": (0, 4.7),
    "paths": [
        [(0, 4.08), (0, 3.6), (0, 0.7)],
        [(0, 0.7), (1.6, 0.85), (0.42, 0.42)],
        [(0, 0.7), (-1.6, 0.85), (-0.42, 0.42)],
        [(0, 3.6), (0.6, 2.2), (0.42, 0.8)],
        [(0, 3.6), (-0.6, 2.2), (-0.42, 0.8)],
    ],
    "ground": True,
}

POSES["boat_pose"] = {
    "head": (-2.05, 4.25),
    "paths": [
        [(-1.85, 3.78), (-1.6, 3.2), (0, 0.8)],
        [(0, 0.8), (1.5, 2.0), (2.75, 3.25), (3.1, 3.55)],
        [(0, 0.8), (1.4, 1.85), (2.6, 3.05), (2.95, 3.35)],
        [(-1.6, 3.2), (-0.2, 3.3), (1.2, 3.35)],
        [(-1.62, 3.05), (-0.25, 3.15), (1.1, 3.2)],
    ],
    "ground": True,
}

POSES["happy_baby"] = {
    "head": (-2.55, 0.82),
    "paths": [
        [(-2.0, 0.7), (-1.6, 0.7), (1.3, 0.7)],
        [(1.3, 0.7), (2.1, 2.2), (1.6, 3.85)],
        [(-1.6, 0.7), (-0.3, 2.3), (1.42, 3.68)],
    ],
    "ground": True,
}

POSES["supine_twist"] = {
    "head": (-3.1, 0.78),
    "paths": [
        [(-2.65, 0.68), (-2.2, 0.6), (0.3, 0.7)],
        [(0.3, 0.7), (1.95, 0.95), (1.45, 0.25)],
        [(0.35, 0.85), (2.1, 1.15), (1.6, 0.4)],
        [(-2.2, 0.6), (-3.4, 1.5), (-4.55, 0.9)],
    ],
    "ground": True,
}

POSES["side_plank"] = {
    "head": (1.0, 3.35),
    "paths": [
        [(0.68, 3.22), (0, 2.95), (-2.6, 2.0)],
        [(-2.6, 2.0), (-4.3, 1.05), (-5.9, 0.25), (-6.5, 0.12)],
        [(0, 2.95), (0, 1.5), (0, 0.12)],
        [(0, 2.95), (0.06, 4.4), (0.1, 5.85)],
    ],
    "ground": True,
}

# ----- calisthenics statics -----

POSES["plank"] = high_plank()

POSES["dead_hang"] = hang()

POSES["wall_sit"] = {
    "head": (-0.2, 6.05),
    "paths": [
        [(-0.22, 5.42), (-0.3, 4.9), (-0.3, 2.0)],
        [(-0.3, 2.0), (1.6, 2.05), (1.65, 0.15), (2.35, 0.1)],
        [(-0.3, 2.0), (1.45, 1.9), (1.5, 0.12), (2.2, 0.08)],
        [(-0.3, 4.9), (0.35, 3.6), (0.95, 2.4)],
    ],
    "props": [[(-0.8, 0.0), (-0.8, 6.9)]],
    "ground": True,
}

POSES["hollow_hold"] = {
    "head": (-3.55, 2.1),
    "paths": [
        [(-3.15, 1.72), (-2.7, 1.5), (0, 0.9)],
        [(0, 0.9), (1.8, 1.35), (3.5, 1.85), (4.1, 2.05)],
        [(0.05, 0.78), (1.85, 1.2), (3.55, 1.7), (4.15, 1.9)],
        [(-2.7, 1.5), (-4.05, 1.95), (-5.35, 2.4)],
        [(-2.75, 1.36), (-4.1, 1.8), (-5.4, 2.25)],
    ],
    "ground": True,
}

# ----- dynamic frames -----

POSES["cat_cow__a"] = tabletop(spine_mid=(0.0, 1.85), head=(2.35, 3.25))     # cow
POSES["cat_cow__b"] = tabletop(spine_mid=(0.0, 2.95), head=(2.1, 2.3))       # cat

POSES["tabletop_ext__a"] = tabletop()
POSES["tabletop_ext__b"] = tabletop(
    arm=[(1.4, 2.35), (2.8, 2.48), (4.2, 2.58)],
    legs=[[(-1.4, 2.2), (-3.2, 2.32), (-5.0, 2.42)],
          [(-1.4, 2.2), (-1.5, 0.35), (-3.2, 0.28), (-3.8, 0.2)]],
)
POSES["tabletop_ext__b"]["paths"].append([(1.28, 2.3), (1.35, 1.2), (1.42, 0.12)])

POSES["walk_up__a"] = POSES["forward_fold"]
POSES["walk_up__b"] = high_plank()

POSES["chaturanga__a"] = high_plank()
POSES["chaturanga__b"] = {
    "head": (1.05, 1.72),
    "paths": [
        [(0.72, 1.6), (0, 1.5), (-2.75, 1.35)],
        [(0, 1.5), (-1.0, 0.7), (-0.85, 0.12)],
        [(-0.2, 1.42), (-1.18, 0.65), (-1.05, 0.1)],
        [(-2.75, 1.35), (-4.5, 1.1), (-6.2, 0.7), (-6.6, 0.12)],
    ],
    "ground": True,
}

POSES["knee_to_nose__a"] = down_dog(lifted_leg=True)
POSES["knee_to_nose__b"] = {
    "head": (0.95, 2.6),
    "paths": [
        [(0.68, 2.72), (0, 2.9), (-1.2, 3.0), (-2.5, 2.55)],
        [(0, 2.9), (0.03, 1.5), (0.05, 0.12)],
        [(-0.22, 2.85), (-0.2, 1.5), (-0.18, 0.12)],
        [(-2.5, 2.55), (-0.9, 1.9), (-1.35, 0.9)],
        [(-2.5, 2.55), (-4.25, 1.6), (-5.85, 0.7), (-6.25, 0.12)],
    ],
    "ground": True,
}

POSES["knee_raise__a"] = stand_side(
    arm_pts=[[(0, 6.7), (0.22, 5.3), (0.28, 3.95)],
             [(0, 6.7), (-0.18, 5.3), (-0.22, 3.95)]])
POSES["knee_raise__b"] = {
    "head": (0.1, 7.8),
    "paths": [
        [(0.08, 7.15), (0, 6.7), (0, 3.7)],
        [(0, 3.7), (0.08, 1.85), (0.12, 0.12), (0.78, 0.1)],
        [(0, 3.7), (1.5, 3.9), (1.62, 2.15), (2.05, 2.1)],
        [(0, 6.7), (0.75, 5.55), (1.45, 4.6)],
        [(0, 6.7), (-0.35, 5.35), (-0.4, 4.0)],
    ],
    "ground": True,
}

POSES["neck_rolls__a"] = stand_front(head=(-0.52, 7.62))
POSES["neck_rolls__a"]["paths"][0] = [(-0.35, 7.05), (0, 6.7), (0, 3.7)]
POSES["neck_rolls__b"] = stand_front(head=(0.52, 7.62))
POSES["neck_rolls__b"]["paths"][0] = [(0.35, 7.05), (0, 6.7), (0, 3.7)]

POSES["shoulder_rolls__a"] = stand_side(
    arm_pts=[[(0.02, 6.98), (0.28, 5.6), (0.32, 4.25)],
             [(-0.2, 6.94), (0.05, 5.56), (0.1, 4.2)]])
POSES["shoulder_rolls__a"]["head"] = (0.05, 7.95)
POSES["shoulder_rolls__b"] = stand_side(
    arm_pts=[[(0, 6.6), (-0.35, 5.25), (-0.28, 3.9)],
             [(-0.2, 6.55), (-0.55, 5.2), (-0.48, 3.85)]])

POSES["wrist_circles__a"] = stand_side(
    arm_pts=[[(0, 6.7), (1.5, 6.76), (2.9, 6.8)], [(2.9, 6.8), (3.22, 7.38)],
             [(0, 6.62), (1.48, 6.66), (2.88, 6.68)]])
POSES["wrist_circles__b"] = stand_side(
    arm_pts=[[(0, 6.7), (1.5, 6.76), (2.9, 6.8)], [(2.9, 6.8), (3.28, 6.28)],
             [(0, 6.62), (1.48, 6.66), (2.88, 6.68)]])

POSES["squat__a"] = stand_side(
    arm_pts=[[(0, 6.7), (0.22, 5.3), (0.28, 3.95)],
             [(0, 6.7), (-0.18, 5.3), (-0.22, 3.95)]])
POSES["squat__b"] = {
    "head": (0.45, 5.72),
    "paths": [
        [(0.38, 5.15), (0.15, 4.6), (-0.7, 1.9)],
        [(-0.7, 1.9), (0.9, 2.0), (0.72, 0.15), (1.42, 0.1)],
        [(-0.7, 1.9), (0.78, 1.88), (0.58, 0.1), (1.28, 0.06)],
        [(0.15, 4.6), (1.55, 4.7), (2.9, 4.76)],
        [(0.12, 4.5), (1.5, 4.58), (2.85, 4.64)],
    ],
    "ground": True,
}

POSES["pushup__a"] = high_plank()
POSES["pushup__b"] = {
    "head": (1.05, 1.55),
    "paths": [
        [(0.72, 1.42), (0, 1.3), (-2.75, 1.15)],
        [(0, 1.3), (-0.55, 1.95), (0.4, 0.12)],
        [(-0.25, 1.26), (-0.78, 1.9), (0.18, 0.1)],
        [(-2.75, 1.15), (-4.6, 0.92), (-6.3, 0.68), (-6.7, 0.12)],
    ],
    "ground": True,
}

_BENCH = [[(1.3, 1.85), (3.1, 1.85)], [(1.45, 1.85), (1.45, 0.02)],
          [(2.95, 1.85), (2.95, 0.02)]]

POSES["incline_pushup__a"] = {
    "head": (2.68, 4.7),
    "paths": [
        [(2.35, 4.55), (1.7, 4.2), (-0.9, 2.9)],
        [(1.7, 4.2), (1.8, 3.0), (1.9, 1.9)],
        [(1.5, 4.1), (1.6, 2.95), (1.7, 1.88)],
        [(-0.9, 2.9), (-2.6, 2.0), (-4.2, 1.0), (-4.62, 0.15)],
    ],
    "props": _BENCH,
    "ground": True,
}
POSES["incline_pushup__b"] = {
    "head": (2.4, 3.65),
    "paths": [
        [(2.08, 3.5), (1.5, 3.2), (-1.2, 2.15)],
        [(1.5, 3.2), (0.85, 3.7), (1.85, 1.9)],
        [(1.3, 3.12), (0.62, 3.6), (1.62, 1.86)],
        [(-1.2, 2.15), (-2.8, 1.5), (-4.3, 0.8), (-4.7, 0.15)],
    ],
    "props": _BENCH,
    "ground": True,
}

POSES["knee_pushup__a"] = {
    "head": (3.05, 3.05),
    "paths": [
        [(2.72, 2.9), (2.0, 2.75), (-0.75, 2.1)],
        [(2.0, 2.75), (2.05, 1.45), (2.1, 0.12)],
        [(1.78, 2.7), (1.83, 1.42), (1.88, 0.1)],
        [(-0.75, 2.1), (-2.0, 0.4), (-3.7, 0.35), (-4.05, 0.8)],
    ],
    "ground": True,
}
POSES["knee_pushup__b"] = {
    "head": (2.72, 1.62),
    "paths": [
        [(2.4, 1.5), (1.7, 1.4), (-0.85, 1.9)],
        [(1.7, 1.4), (1.1, 2.0), (2.1, 0.12)],
        [(1.48, 1.35), (0.88, 1.94), (1.88, 0.1)],
        [(-0.85, 1.9), (-2.0, 0.4), (-3.7, 0.35), (-4.05, 0.8)],
    ],
    "ground": True,
}

POSES["pike_pushup__a"] = {
    "head": (1.95, 1.15),
    "paths": [
        [(1.62, 1.4), (1.5, 1.95), (-0.5, 4.2)],
        [(1.5, 1.95), (1.95, 1.05), (2.4, 0.12)],
        [(1.32, 1.88), (1.75, 1.0), (2.2, 0.1)],
        [(-0.5, 4.2), (-1.7, 2.2), (-2.8, 0.4), (-2.3, 0.12)],
        [(-0.62, 4.12), (-1.85, 2.15), (-2.95, 0.42), (-2.45, 0.14)],
    ],
    "ground": True,
}
POSES["pike_pushup__b"] = {
    "head": (2.05, 0.85),
    "paths": [
        [(1.75, 1.0), (1.55, 1.4), (-0.5, 4.0)],
        [(1.55, 1.4), (1.72, 0.68), (2.4, 0.12)],
        [(1.35, 1.35), (1.52, 0.64), (2.2, 0.1)],
        [(-0.5, 4.0), (-1.7, 2.1), (-2.8, 0.4), (-2.3, 0.12)],
        [(-0.62, 3.92), (-1.85, 2.05), (-2.95, 0.42), (-2.45, 0.14)],
    ],
    "ground": True,
}

POSES["reverse_lunge__a"] = stand_side(
    arm_pts=[[(0, 6.7), (0.22, 5.3), (0.28, 3.95)],
             [(0, 6.7), (-0.18, 5.3), (-0.22, 3.95)]])
POSES["reverse_lunge__b"] = {
    "head": (0.2, 6.6),
    "paths": [
        [(0.18, 5.98), (0.1, 5.5), (0, 2.6)],
        [(0, 2.6), (1.1, 1.6), (1.2, 0.15), (1.88, 0.1)],
        [(0, 2.6), (-1.35, 0.78), (-2.42, 0.32), (-2.85, 0.14)],
        [(0.1, 5.5), (0.38, 4.15), (0.42, 2.82)],
        [(0.05, 5.42), (-0.28, 4.1), (-0.25, 2.78)],
    ],
    "ground": True,
}

POSES["split_squat__a"] = {
    "head": (0.05, 7.65),
    "paths": [
        [(0.05, 7.02), (0, 6.56), (0, 3.55)],
        [(0, 3.55), (0.6, 1.8), (1.15, 0.15), (1.82, 0.1)],
        [(0, 3.55), (-0.7, 1.85), (-1.32, 0.35), (-1.7, 0.12)],
        [(0, 6.56), (0.2, 5.18), (0.25, 3.82)],
        [(-0.15, 6.52), (-0.4, 5.15), (-0.38, 3.8)],
    ],
    "ground": True,
}
POSES["split_squat__b"] = POSES["reverse_lunge__b"]

POSES["shoulder_taps__a"] = high_plank()
POSES["shoulder_taps__b"] = {
    "head": (1.06, 3.2),
    "paths": [
        [(0.75, 3.1), (0, 2.9), (-2.7, 2.2)],
        [(0, 2.9), (0.55, 2.15), (-0.28, 2.72)],
        [(-0.22, 2.85), (-0.2, 1.5), (-0.18, 0.12)],
        [(-2.7, 2.2), (-4.5, 1.4), (-6.2, 0.6), (-6.6, 0.15)],
    ],
    "ground": True,
}

POSES["glute_bridge__a"] = bridge_down()
POSES["glute_bridge__b"] = bridge_up()

POSES["single_leg_bridge__a"] = bridge_down(
    free_leg=[(-0.3, 0.7), (1.35, 1.5), (2.9, 2.3), (3.25, 2.55)])
POSES["single_leg_bridge__b"] = bridge_up(
    free_leg=[(-0.5, 1.5), (1.15, 2.1), (2.75, 2.68), (3.1, 2.92)])

POSES["superman__a"] = {
    "head": (3.15, 1.12),
    "paths": [
        [(2.62, 0.82), (2.2, 0.62), (-0.6, 0.5)],
        [(2.2, 0.62), (3.55, 0.48), (4.9, 0.4)],
        [(-0.6, 0.5), (-2.4, 0.44), (-4.2, 0.38), (-4.8, 0.3)],
        [(-0.58, 0.38), (-2.38, 0.32), (-4.15, 0.26), (-4.75, 0.18)],
    ],
    "ground": True,
}
POSES["superman__b"] = {
    "head": (3.1, 1.78),
    "paths": [
        [(2.58, 1.45), (2.15, 1.15), (-0.6, 0.6)],
        [(2.15, 1.15), (3.5, 1.5), (4.85, 1.85)],
        [(2.18, 1.0), (3.52, 1.34), (4.88, 1.68)],
        [(-0.6, 0.6), (-2.35, 0.95), (-4.05, 1.4), (-4.6, 1.6)],
        [(-0.55, 0.48), (-2.3, 0.8), (-4.0, 1.24), (-4.55, 1.44)],
    ],
    "ground": True,
}

POSES["scap_pull__a"] = hang()
POSES["scap_pull__b"] = hang(
    sh=(0, 7.1), hip=(0.1, 4.1), head=(0, 8.05),
    legs=[[(0.1, 4.1), (0.2, 2.25), (0.12, 0.9), (0.35, 0.52)],
          [(0.1, 4.1), (0.35, 2.3), (0.3, 0.95), (0.55, 0.6)]])

POSES["negative_pullup__a"] = pullup_top()
POSES["negative_pullup__b"] = hang()

POSES["pullup__a"] = hang()
POSES["pullup__b"] = pullup_top()

POSES["chinup__a"] = hang(
    arms=[[(0, 6.7), (0.3, 8.15), (0.28, 9.55)],
          [(0, 6.7), (-0.05, 8.15), (-0.25, 9.55)]])
POSES["chinup__b"] = pullup_top()

_DOOR = [[(2.62, 0.0), (2.62, 6.9)]]

POSES["towel_row__a"] = {
    "head": (-0.26, 6.42),
    "paths": [
        [(-0.15, 5.9), (0.1, 5.35), (1.05, 2.6)],
        [(1.05, 2.6), (1.6, 1.5), (2.2, 0.12), (2.85, 0.1)],
        [(1.05, 2.6), (1.45, 1.45), (2.02, 0.1), (2.68, 0.08)],
        [(0.1, 5.35), (1.25, 4.95), (2.35, 4.55)],
        [(0.05, 5.2), (1.2, 4.8), (2.32, 4.42)],
    ],
    "props": _DOOR + [[(2.62, 4.85), (2.35, 4.55)]],
    "ground": True,
}
POSES["towel_row__b"] = {
    "head": (1.0, 6.6),
    "paths": [
        [(1.06, 6.05), (1.2, 5.5), (1.7, 2.7)],
        [(1.7, 2.7), (1.9, 1.5), (2.2, 0.12), (2.85, 0.1)],
        [(1.7, 2.7), (1.78, 1.45), (2.02, 0.1), (2.68, 0.08)],
        [(1.2, 5.5), (0.72, 4.6), (2.42, 4.58)],
        [(1.1, 5.36), (0.6, 4.48), (2.4, 4.44)],
    ],
    "props": _DOOR + [[(2.62, 4.85), (2.44, 4.58)]],
    "ground": True,
}

_LOWBAR = [[(-1.25, 3.35), (1.25, 3.35)]]

POSES["inverted_row__a"] = {
    "head": (-1.05, 1.0),
    "paths": [
        [(-0.65, 0.95), (0.05, 0.9), (2.85, 0.7)],
        [(0.05, 0.9), (0.05, 2.1), (0.02, 3.28)],
        [(0.28, 0.88), (0.28, 2.08), (0.25, 3.26)],
        [(2.85, 0.7), (4.6, 0.55), (6.35, 0.42), (6.85, 0.8)],
    ],
    "props": _LOWBAR,
    "ground": True,
}
POSES["inverted_row__b"] = {
    "head": (-1.07, 2.76),
    "paths": [
        [(-0.68, 2.68), (0, 2.5), (2.7, 1.9)],
        [(0, 2.5), (0.9, 1.75), (0.05, 3.28)],
        [(0.25, 2.45), (1.12, 1.72), (0.28, 3.26)],
        [(2.7, 1.9), (4.5, 1.35), (6.3, 0.5), (6.8, 0.85)],
    ],
    "props": _LOWBAR,
    "ground": True,
}

def _ytw_figure(arms):
    return {
        "head": (0, 7.8),
        "paths": [
            [(0, 7.15), (0, 6.7), (0, 3.7)],
            [(0, 3.7), (-0.3, 1.85), (-0.4, 0.15)],
            [(0, 3.7), (0.3, 1.85), (0.4, 0.15)],
        ] + arms,
        "ground": True,
    }

POSES["ytw__y"] = _ytw_figure(
    [[(0, 6.7), (1.05, 7.75), (1.75, 8.85)], [(0, 6.7), (-1.05, 7.75), (-1.75, 8.85)]])
POSES["ytw__t"] = _ytw_figure(
    [[(0, 6.7), (1.5, 6.72), (2.9, 6.72)], [(0, 6.7), (-1.5, 6.72), (-2.9, 6.72)]])
POSES["ytw__w"] = _ytw_figure(
    [[(0, 6.7), (1.3, 6.1), (2.15, 7.4)], [(0, 6.7), (-1.3, 6.1), (-2.15, 7.4)]])

POSES["hanging_knee_raise__a"] = hang()
POSES["hanging_knee_raise__b"] = hang(
    hip=(0.1, 3.85),
    legs=[[(0.1, 3.85), (1.35, 4.85), (1.5, 3.1), (1.75, 2.98)],
          [(0.1, 3.85), (1.5, 4.7), (1.65, 2.95), (1.9, 2.85)]])

_CHAIR = [[(-2.45, 2.2), (-0.4, 2.2)], [(-0.55, 2.2), (-0.55, 0.02)],
          [(-2.3, 2.2), (-2.3, 0.02)], [(-2.38, 2.2), (-2.38, 4.3)]]

POSES["chair_dip__a"] = {
    "head": (-0.32, 6.2),
    "paths": [
        [(-0.34, 5.58), (-0.4, 5.1), (0.35, 2.3)],
        [(-0.4, 5.1), (-0.42, 3.65), (-0.45, 2.28)],
        [(-0.62, 5.05), (-0.64, 3.62), (-0.66, 2.26)],
        [(0.35, 2.3), (2.1, 1.35), (3.75, 0.42), (4.3, 0.78)],
        [(0.35, 2.3), (1.95, 1.28), (3.6, 0.36), (4.15, 0.72)],
    ],
    "props": _CHAIR,
    "ground": True,
}
POSES["chair_dip__b"] = {
    "head": (-0.36, 5.05),
    "paths": [
        [(-0.4, 4.45), (-0.5, 3.95), (0.3, 1.5)],
        [(-0.5, 3.95), (-1.5, 3.45), (-0.45, 2.28)],
        [(-0.7, 3.88), (-1.68, 3.38), (-0.66, 2.26)],
        [(0.3, 1.5), (2.1, 1.1), (3.7, 0.38), (4.25, 0.74)],
        [(0.3, 1.5), (1.95, 1.02), (3.55, 0.32), (4.1, 0.68)],
    ],
    "props": _CHAIR,
    "ground": True,
}

# ------------------------------------------------------------------ moves

STATIC = [
    "childs_pose", "down_dog", "mountain", "forward_fold", "halfway_lift",
    "low_lunge", "warrior1", "warrior2", "triangle", "chair_pose",
    "tree_pose", "cobra", "sphinx", "upward_dog", "pigeon", "seated_fold",
    "butterfly", "boat_pose", "happy_baby", "supine_twist", "side_plank",
    "plank", "dead_hang", "wall_sit", "hollow_hold",
]

TWO_FRAME = [
    "cat_cow", "tabletop_ext", "walk_up", "chaturanga", "knee_to_nose",
    "knee_raise", "neck_rolls", "shoulder_rolls", "wrist_circles",
    "squat", "pushup", "incline_pushup", "knee_pushup", "pike_pushup",
    "reverse_lunge", "split_squat", "shoulder_taps",
    "glute_bridge", "single_leg_bridge", "superman", "scap_pull",
    "negative_pullup", "pullup", "chinup", "towel_row", "inverted_row",
    "hanging_knee_raise", "chair_dip",
]


def generate(only=None):
    os.makedirs(OUT_DIR, exist_ok=True)
    ids = []

    for mid in STATIC:
        if only and mid not in only:
            continue
        svg = make_svg([(POSES[mid], W / 2, H / 2, 580, 350, 36)])
        cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT_DIR, f"{mid}.png"),
                        output_width=W, output_height=H)
        ids.append(mid)

    for mid in TWO_FRAME:
        if only and mid not in only:
            continue
        svg = make_svg([
            (POSES[f"{mid}__a"], 210, H / 2, 290, 330, 25),
            (POSES[f"{mid}__b"], 590, H / 2, 290, 330, 25),
        ])
        cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT_DIR, f"{mid}.png"),
                        output_width=W, output_height=H)
        ids.append(mid)

    if not only or "ytw" in only:
        svg = make_svg([
            (POSES["ytw__y"], 155, H / 2, 200, 330, 17),
            (POSES["ytw__t"], 400, H / 2, 200, 330, 17),
            (POSES["ytw__w"], 645, H / 2, 200, 330, 17),
        ])
        cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT_DIR, "ytw.png"),
                        output_width=W, output_height=H)
        ids.append("ytw")

    return ids


if __name__ == "__main__":
    import sys
    only = set(sys.argv[1:]) or None
    done = generate(only)
    print(f"generated {len(done)} images")
