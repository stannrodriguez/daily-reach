"""Reach pose: Single-Leg Bridge."""

MOVE = {
    "id": "single_leg_bridge",
    "name": "Single-Leg Bridge",
    "layout": "two",
    "cue": "Bridge with one foot on the floor and the other knee drawn in.",
    "frames": [
        {
            "head": [-3.75, 0.78],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-3.15, 0.62], [-2.9, 0.6], [-0.3, 0.7]]
                },
                {
                    "role": "A",
                    "pts": [[-2.9, 0.6], [-1.55, 0.45], [-0.2, 0.38]]
                },
                {
                    "role": "L",
                    "pts": [[-0.3, 0.7], [1.2, 2.1], [1.35, 0.25], [2.0, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[-0.3, 0.7], [1.35, 1.5], [2.9, 2.3], [3.25, 2.55]]
                }
            ]
        },
        {
            "head": [-3.75, 0.78],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-3.15, 0.62], [-2.9, 0.6], [-0.5, 1.5]]
                },
                {
                    "role": "A",
                    "pts": [[-2.9, 0.6], [-1.6, 0.5], [-0.35, 0.4]]
                },
                {
                    "role": "L",
                    "pts": [[-0.5, 1.5], [1.05, 2.0], [1.3, 0.25], [1.95, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[-0.5, 1.5], [1.15, 2.1], [2.75, 2.68], [3.1, 2.92]]
                }
            ]
        }
    ]
}
