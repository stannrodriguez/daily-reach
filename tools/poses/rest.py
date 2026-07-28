"""Reach pose: Quiet Rest."""

MOVE = {
    "id": "rest",
    "name": "Quiet Rest",
    "layout": "static",
    "cue": "The last pose is the one the body keeps.",
    "frames": [
        {
            "head": [-3.6, 0.85],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-3.0, 0.72], [-2.5, 0.7], [0, 0.68]]
                },
                {
                    "role": "L",
                    "pts": [[0, 0.68], [1.9, 0.55], [3.7, 0.45]]
                },
                {
                    "role": "l",
                    "pts": [[0.05, 0.55], [1.95, 0.42], [3.75, 0.32]]
                },
                {
                    "role": "A",
                    "pts": [[-2.5, 0.7], [-1.6, 0.3], [-0.7, 0.2]]
                }
            ]
        }
    ]
}
