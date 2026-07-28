"""Reach pose: Standing Figure 4."""

MOVE = {
    "id": "figure4_standing",
    "name": "Standing Figure 4",
    "layout": "static",
    "cue": "Cross one ankle above the opposite knee and sit the hips back like a one-legged chair.",
    "frames": [
        {
            "head": [0.5, 6.75],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.45, 6.15], [0.3, 5.7], [-0.7, 3.1]]
                },
                {
                    "role": "L",
                    "pts": [[-0.7, 3.1], [0.55, 1.95], [0.25, 0.15], [0.95, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[-0.7, 3.1], [1.35, 2.9], [0.6, 1.85]]
                },
                {
                    "role": "A",
                    "pts": [[0.3, 5.7], [0.95, 4.4], [1.35, 3.35]]
                },
                {
                    "role": "a",
                    "pts": [[0.15, 5.62], [0.8, 4.35], [1.2, 3.3]]
                }
            ]
        }
    ]
}
