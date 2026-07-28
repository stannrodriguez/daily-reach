"""Reach pose: Forearm Plank."""

MOVE = {
    "id": "plank_hold",
    "name": "Forearm Plank",
    "layout": "static",
    "cue": "Elbows under the shoulders, forearms parallel, hips level with the shoulders.",
    "frames": [
        {
            "head": [1.0, 2.65],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.7, 2.55], [0, 2.4], [-2.7, 1.85]]
                },
                {
                    "role": "A",
                    "pts": [[0, 2.4], [0.05, 1.3], [0.05, 0.12]]
                },
                {
                    "role": "A",
                    "pts": [[0.05, 0.15], [0.85, 0.12], [1.5, 0.1]]
                },
                {
                    "role": "a",
                    "pts": [[-0.22, 2.35], [-0.18, 1.28], [-0.15, 0.12]]
                },
                {
                    "role": "a",
                    "pts": [[-0.15, 0.12], [0.65, 0.1], [1.3, 0.08]]
                },
                {
                    "role": "L",
                    "pts": [[-2.7, 1.85], [-4.4, 1.15], [-6.0, 0.5], [-6.4, 0.12]]
                }
            ]
        }
    ]
}
