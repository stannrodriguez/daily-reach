"""Reach pose: Halfway Lift."""

MOVE = {
    "id": "halfway_lift",
    "name": "Halfway Lift",
    "layout": "static",
    "cue": "Flat back over straight legs \u2014 bend the knees to get there.",
    "frames": [
        {
            "head": [3.75, 4.3],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[3.35, 4.25], [2.95, 4.1], [0, 3.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [0.08, 1.85], [0.12, 0.12], [0.75, 0.1]]
                },
                {
                    "role": "l",
                    "pts": [[0, 3.7], [-0.15, 1.85], [-0.15, 0.12], [0.45, 0.1]]
                },
                {
                    "role": "A",
                    "pts": [[2.95, 4.1], [2.0, 3.0], [1.0, 2.0]]
                }
            ]
        }
    ]
}
