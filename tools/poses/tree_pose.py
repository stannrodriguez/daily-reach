"""Reach pose: Tree Pose."""

MOVE = {
    "id": "tree_pose",
    "name": "Tree Pose",
    "layout": "static",
    "cue": "Press the foot and the leg into each other and stand tall.",
    "frames": [
        {
            "head": [0, 7.8],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0, 7.15], [0, 6.7], [0, 3.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [-0.08, 1.85], [-0.1, 0.12], [0.45, 0.08]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [1.15, 2.7], [0.22, 2.95]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [0.85, 7.85], [0.55, 9.0]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [-0.85, 7.85], [-0.55, 9.0]]
                }
            ]
        }
    ]
}
