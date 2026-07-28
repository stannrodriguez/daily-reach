"""Reach pose: Walk Feet to Hands."""

MOVE = {
    "id": "walk_up",
    "name": "Walk Feet to Hands",
    "layout": "two",
    "cue": "From Downward Dog, step or walk the feet forward to meet the hands.",
    "frames": [
        {
            "head": [1.42, 0.95],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0, 3.7], [0.9, 2.9], [1.25, 1.6]]
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
                    "pts": [[1.25, 1.6], [1.05, 0.85], [0.9, 0.15]]
                },
                {
                    "role": "a",
                    "pts": [[1.1, 1.55], [0.9, 0.8], [0.72, 0.12]]
                }
            ]
        },
        {
            "head": [1.06, 3.2],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.75, 3.1], [0, 2.9], [-2.7, 2.2]]
                },
                {
                    "role": "A",
                    "pts": [[0, 2.9], [0.03, 1.5], [0.05, 0.12]]
                },
                {
                    "role": "a",
                    "pts": [[-0.22, 2.85], [-0.2, 1.5], [-0.18, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[-2.7, 2.2], [-4.5, 1.4], [-6.2, 0.6], [-6.6, 0.15]]
                }
            ]
        }
    ]
}
