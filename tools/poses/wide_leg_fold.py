"""Reach pose: Wide-Leg Forward Fold."""

MOVE = {
    "id": "wide_leg_fold",
    "name": "Wide-Leg Forward Fold",
    "layout": "static",
    "cue": "Feet wide and parallel, hinge at the hips and fold.",
    "frames": [
        {
            "head": [0, 0.95],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0, 1.7], [0, 2.7], [0, 3.9]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.9], [-1.75, 2.1], [-3.4, 0.12], [-3.85, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.9], [1.75, 2.1], [3.4, 0.12], [3.85, 0.1]]
                },
                {
                    "role": "A",
                    "pts": [[0, 2.7], [-1.5, 1.75], [-2.0, 0.15]]
                },
                {
                    "role": "A",
                    "pts": [[0, 2.7], [1.5, 1.75], [2.0, 0.15]]
                }
            ]
        }
    ]
}
