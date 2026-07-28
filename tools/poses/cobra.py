"""Reach pose: Cobra."""

MOVE = {
    "id": "cobra",
    "name": "Cobra",
    "layout": "static",
    "cue": "Lead with the sternum, not the chin.",
    "frames": [
        {
            "head": [2.95, 3.2],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.62, 2.75], [2.2, 2.4], [0.9, 1.2], [0, 0.55]]
                },
                {
                    "role": "L",
                    "pts": [[0, 0.55], [-1.9, 0.38], [-3.7, 0.28], [-4.3, 0.15]]
                },
                {
                    "role": "l",
                    "pts": [[0.05, 0.42], [-1.85, 0.26], [-3.6, 0.16], [-4.2, 0.05]]
                },
                {
                    "role": "A",
                    "pts": [[2.2, 2.4], [2.15, 1.3], [2.4, 0.12]]
                }
            ]
        }
    ]
}
