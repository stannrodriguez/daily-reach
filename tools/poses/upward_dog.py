"""Reach pose: Upward Dog."""

MOVE = {
    "id": "upward_dog",
    "name": "Upward Dog",
    "layout": "static",
    "cue": "Press the floor away, thighs off the mat, chest through the arms.",
    "frames": [
        {
            "head": [2.6, 3.9],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.3, 3.45], [1.9, 3.1], [0.7, 1.75], [0, 1.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 1.1], [-1.8, 0.7], [-3.5, 0.32], [-4.05, 0.12]]
                },
                {
                    "role": "A",
                    "pts": [[1.9, 3.1], [2.05, 1.6], [2.2, 0.15]]
                },
                {
                    "role": "a",
                    "pts": [[1.72, 3.02], [1.85, 1.55], [1.98, 0.12]]
                }
            ]
        }
    ]
}
