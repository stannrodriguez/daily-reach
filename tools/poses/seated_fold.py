"""Reach pose: Seated Forward Fold."""

MOVE = {
    "id": "seated_fold",
    "name": "Seated Forward Fold",
    "layout": "static",
    "cue": "Legs long in front, sit up on the sit bones, hinge from the hips and walk the hands down the legs.",
    "frames": [
        {
            "head": [1.72, 2.3],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[1.35, 2.32], [0.9, 2.2], [-0.7, 1.9], [-1.5, 0.75]]
                },
                {
                    "role": "L",
                    "pts": [[-1.5, 0.75], [0.3, 0.55], [2.0, 0.45], [2.3, 1.05]]
                },
                {
                    "role": "l",
                    "pts": [[-1.45, 0.62], [0.3, 0.42], [1.95, 0.32], [2.25, 0.9]]
                },
                {
                    "role": "A",
                    "pts": [[0.9, 2.2], [1.6, 1.5], [2.15, 0.85]]
                }
            ]
        }
    ]
}
