"""Reach pose: Standing Forward Fold."""

MOVE = {
    "id": "forward_fold",
    "name": "Standing Forward Fold",
    "layout": "static",
    "cue": "This is the daily toe-touch rep. Time under tension does the work.",
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
        }
    ]
}
