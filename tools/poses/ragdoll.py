"""Reach pose: Ragdoll Fold."""

MOVE = {
    "id": "ragdoll",
    "name": "Ragdoll Fold",
    "layout": "static",
    "cue": "Feet hip-width, knees softly bent, fold and take hold of opposite elbows.",
    "frames": [
        {
            "head": [1.45, 1.1],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0, 3.3], [0.95, 2.6], [1.28, 1.75]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.3], [0.92, 2.05], [0.25, 0.12], [0.9, 0.1]]
                },
                {
                    "role": "l",
                    "pts": [[0, 3.3], [0.62, 1.98], [0.0, 0.12], [0.6, 0.1]]
                },
                {
                    "role": "A",
                    "pts": [[1.28, 1.75], [1.18, 0.95], [1.08, 0.2]]
                },
                {
                    "role": "a",
                    "pts": [[1.14, 1.66], [1.02, 0.88], [0.92, 0.15]]
                }
            ]
        }
    ]
}
