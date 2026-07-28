"""Reach pose: Side Plank."""

MOVE = {
    "id": "side_plank",
    "name": "Side Plank",
    "layout": "static",
    "cue": "On one forearm, feet stacked or staggered, hips lifted in a straight line.",
    "frames": [
        {
            "head": [1.0, 3.35],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.68, 3.22], [0, 2.95], [-2.6, 2.0]]
                },
                {
                    "role": "L",
                    "pts": [[-2.6, 2.0], [-4.3, 1.05], [-5.9, 0.25], [-6.5, 0.12]]
                },
                {
                    "role": "A",
                    "pts": [[0, 2.95], [0, 1.5], [0, 0.12]]
                },
                {
                    "role": "A",
                    "pts": [[0, 2.95], [0.06, 4.4], [0.1, 5.85]]
                }
            ]
        }
    ]
}
