"""Reach pose: Mountain."""

MOVE = {
    "id": "mountain",
    "name": "Mountain",
    "layout": "static",
    "cue": "Stand tall, feet grounded, arms at the sides or overhead.",
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
                    "pts": [[0, 6.7], [0.22, 5.3], [0.28, 3.95]]
                },
                {
                    "role": "a",
                    "pts": [[0, 6.7], [-0.18, 5.3], [-0.22, 3.95]]
                }
            ]
        }
    ]
}
