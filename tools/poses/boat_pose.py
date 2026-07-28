"""Reach pose: Boat Pose."""

MOVE = {
    "id": "boat_pose",
    "name": "Boat Pose",
    "layout": "static",
    "cue": "Long spine, chest open, legs reaching away.",
    "frames": [
        {
            "head": [-2.05, 4.25],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-1.85, 3.78], [-1.6, 3.2], [0, 0.8]]
                },
                {
                    "role": "L",
                    "pts": [[0, 0.8], [1.5, 2.0], [2.75, 3.25], [3.1, 3.55]]
                },
                {
                    "role": "l",
                    "pts": [[0, 0.8], [1.4, 1.85], [2.6, 3.05], [2.95, 3.35]]
                },
                {
                    "role": "A",
                    "pts": [[-1.6, 3.2], [-0.2, 3.3], [1.2, 3.35]]
                },
                {
                    "role": "a",
                    "pts": [[-1.62, 3.05], [-0.25, 3.15], [1.1, 3.2]]
                }
            ]
        }
    ]
}
