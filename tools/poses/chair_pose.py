"""Reach pose: Chair Pose."""

MOVE = {
    "id": "chair_pose",
    "name": "Chair Pose",
    "layout": "static",
    "cue": "Sit back into the heels, chest lifting away from the thighs.",
    "frames": [
        {
            "head": [0.62, 6.9],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.55, 6.32], [0.35, 5.85], [-0.6, 3.0]]
                },
                {
                    "role": "L",
                    "pts": [[-0.6, 3.0], [0.75, 1.9], [0.32, 0.15], [1.0, 0.1]]
                },
                {
                    "role": "l",
                    "pts": [[-0.6, 3.0], [0.62, 1.82], [0.15, 0.12], [0.82, 0.08]]
                },
                {
                    "role": "A",
                    "pts": [[0.35, 5.85], [1.1, 7.1], [1.75, 8.3]]
                },
                {
                    "role": "a",
                    "pts": [[0.35, 5.85], [0.72, 7.18], [1.32, 8.42]]
                }
            ]
        }
    ]
}
