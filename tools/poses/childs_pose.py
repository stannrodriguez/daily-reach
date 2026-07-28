"""Reach pose: Child's Pose."""

MOVE = {
    "id": "childs_pose",
    "name": "Child's Pose",
    "layout": "static",
    "cue": "Nothing to achieve here \u2014 just let the floor hold you.",
    "frames": [
        {
            "head": [2.25, 0.78],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[1.55, 0.72], [1.0, 0.75], [-1.0, 1.15], [-1.85, 0.9]]
                },
                {
                    "role": "L",
                    "pts": [[-1.85, 0.9], [-1.75, 0.3], [-3.4, 0.3], [-4.0, 0.22]]
                },
                {
                    "role": "A",
                    "pts": [[1.0, 0.75], [2.3, 0.35], [3.7, 0.15]]
                },
                {
                    "role": "a",
                    "pts": [[0.95, 0.62], [2.2, 0.25], [3.5, 0.1]]
                }
            ]
        }
    ]
}
