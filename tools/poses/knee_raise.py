"""Reach pose: Standing Knee Raise."""

MOVE = {
    "id": "knee_raise",
    "name": "Standing Knee Raise",
    "layout": "two",
    "cue": "From standing split, draw the lifted knee in toward the chest and stand up tall.",
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
        },
        {
            "head": [0.1, 7.8],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.08, 7.15], [0, 6.7], [0, 3.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [0.08, 1.85], [0.12, 0.12], [0.78, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [1.5, 3.9], [1.62, 2.15], [2.05, 2.1]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [0.75, 5.55], [1.45, 4.6]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [-0.35, 5.35], [-0.4, 4.0]]
                }
            ]
        }
    ]
}
