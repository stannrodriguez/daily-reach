"""Reach pose: Tabletop Arm & Leg Extensions."""

MOVE = {
    "id": "tabletop_ext",
    "name": "Tabletop Arm & Leg Extensions",
    "layout": "two",
    "cue": "Long, not high \u2014 reach out through the fingers and the heel.",
    "frames": [
        {
            "head": [2.25, 2.95],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.0, 2.7], [1.4, 2.35], [0.0, 2.3], [-1.4, 2.2]]
                },
                {
                    "role": "A",
                    "pts": [[1.4, 2.35], [1.45, 1.2], [1.5, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[-1.4, 2.2], [-1.5, 0.35], [-3.2, 0.28], [-3.8, 0.2]]
                }
            ]
        },
        {
            "head": [2.25, 2.95],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.0, 2.7], [1.4, 2.35], [0.0, 2.3], [-1.4, 2.2]]
                },
                {
                    "role": "A",
                    "pts": [[1.4, 2.35], [2.8, 2.48], [4.2, 2.58]]
                },
                {
                    "role": "L",
                    "pts": [[-1.4, 2.2], [-3.2, 2.32], [-5.0, 2.42]]
                },
                {
                    "role": "L",
                    "pts": [[-1.4, 2.2], [-1.5, 0.35], [-3.2, 0.28], [-3.8, 0.2]]
                },
                {
                    "role": "A",
                    "pts": [[1.28, 2.3], [1.35, 1.2], [1.42, 0.12]]
                }
            ]
        }
    ]
}
