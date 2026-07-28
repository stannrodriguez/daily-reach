"""Reach pose: Neck Side Stretch."""

MOVE = {
    "id": "neck_side",
    "name": "Neck Side Stretch",
    "layout": "static",
    "cue": "Sit or stand tall, drop one ear toward the shoulder and rest the same-side hand lightly on the head.",
    "frames": [
        {
            "head": [0.85, 7.45],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.45, 6.95], [0, 6.7], [0, 3.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [-0.3, 1.85], [-0.4, 0.12], [-0.85, 0.08]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [0.3, 1.85], [0.4, 0.12], [0.85, 0.08]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [1.35, 7.05], [1.5, 8.0]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [-0.55, 5.3], [-0.65, 3.95]]
                }
            ]
        }
    ]
}
