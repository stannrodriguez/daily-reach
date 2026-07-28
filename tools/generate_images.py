#!/usr/bin/env python3
"""Generate the Reach move illustrations (gradient plate style).

Each move id in tools/poses/ renders twice:
  images/<id>.png        annotated plate for the player view
  images/thumbs/<id>.png figure-only render for small slots

Usage: python3 generate_images.py [move_id ...]
"""

import importlib
import os
import sys

import cairosvg

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
IMG_DIR = os.path.join(ROOT, "images")
THUMB_DIR = os.path.join(IMG_DIR, "thumbs")

sys.path.insert(0, TOOLS)
import reachviz  # noqa: E402


def discover():
    moves = {}
    poses_dir = os.path.join(TOOLS, "poses")
    for fn in sorted(os.listdir(poses_dir)):
        if fn.endswith(".py") and not fn.startswith("_"):
            mod = importlib.import_module(f"poses.{fn[:-3]}")
            moves[mod.MOVE["id"]] = mod.MOVE
    return moves


def generate(only=None):
    os.makedirs(THUMB_DIR, exist_ok=True)
    done = []
    for mid, move in discover().items():
        if only and mid not in only:
            continue
        plate = reachviz.render_move(move, annotated=True)
        cairosvg.svg2png(bytestring=plate.encode(), scale=1.5,
                         write_to=os.path.join(IMG_DIR, f"{mid}.png"))
        thumb = reachviz.render_move(move, annotated=False)
        cairosvg.svg2png(bytestring=thumb.encode(),
                         write_to=os.path.join(THUMB_DIR, f"{mid}.png"))
        done.append(mid)
    return done


if __name__ == "__main__":
    only = set(sys.argv[1:]) or None
    print(f"generated {len(generate(only))} moves")
