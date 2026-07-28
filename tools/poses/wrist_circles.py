"""Reach pose: Wrist Circles & Flexor Stretch."""

MOVE = {
    "id": "wrist_circles",
    "name": "Wrist Circles & Flexor Stretch",
    "layout": "two",
    "cue": "Circle the wrists both ways, then extend one arm, palm up, and gently draw the fingers back with the other hand.",
    "frames": [
        {
            "head": [0.05, 7.8],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.05, 7.15], [0, 6.7], [0, 3.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [0.1, 1.85], [0.15, 0.12], [0.8, 0.1]]
                },
                {
                    "role": "l",
                    "pts": [[0, 3.7], [-0.12, 1.85], [-0.12, 0.12], [0.5, 0.1]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [1.5, 6.76], [2.9, 6.8]]
                },
                {
                    "role": "H",
                    "pts": [[2.9, 6.8], [3.22, 7.38]]
                },
                {
                    "role": "a",
                    "pts": [[0, 6.62], [1.48, 6.66], [2.88, 6.68]]
                }
            ]
        },
        {
            "head": [0.05, 7.8],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.05, 7.15], [0, 6.7], [0, 3.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [0.1, 1.85], [0.15, 0.12], [0.8, 0.1]]
                },
                {
                    "role": "l",
                    "pts": [[0, 3.7], [-0.12, 1.85], [-0.12, 0.12], [0.5, 0.1]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [1.5, 6.76], [2.9, 6.8]]
                },
                {
                    "role": "H",
                    "pts": [[2.9, 6.8], [3.28, 6.28]]
                },
                {
                    "role": "a",
                    "pts": [[0, 6.62], [1.48, 6.66], [2.88, 6.68]]
                }
            ]
        }
    ]
}
