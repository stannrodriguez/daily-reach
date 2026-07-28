"""Reach pose: Standing Side Bend."""

MOVE = {
    "id": "standing_side_bend",
    "name": "Standing Side Bend",
    "layout": "static",
    "cue": "Feet grounded, reach both arms up, catch one wrist and lean gently to the side.",
    "frames": [
        {
            "head": [0.7, 7.6],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.5, 7.0], [0.3, 6.55], [0, 3.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [-0.35, 1.85], [-0.45, 0.12], [-0.9, 0.08]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [0.35, 1.85], [0.45, 0.12], [0.9, 0.08]]
                },
                {
                    "role": "A",
                    "pts": [[0.3, 6.55], [1.65, 7.35], [2.7, 8.0]]
                },
                {
                    "role": "A",
                    "pts": [[0.25, 6.5], [-0.5, 5.4], [-0.35, 4.1]]
                }
            ]
        }
    ]
}
