"""Reach pose: Glute Bridge."""

MOVE = {
    "id": "glute_bridge",
    "name": "Glute Bridge",
    "layout": "two",
    "cue": "On the back, knees bent, feet flat and hip-width.",
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
                }
            ]
        }
    ]
}
