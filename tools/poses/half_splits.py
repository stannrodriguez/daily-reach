"""Reach pose: Half Splits."""

MOVE = {
    "id": "half_splits",
    "name": "Half Splits",
    "layout": "static",
    "cue": "Square the hips first, then fold. Depth is not the point.",
    "frames": [
        {
            "head": [1.05, 1.75],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.45, 1.95], [0.1, 2.1], [-1.4, 2.15]]
                },
                {
                    "role": "L",
                    "pts": [[-1.4, 2.15], [0.35, 1.15], [2.05, 0.15], [2.2, 1.0]]
                },
                {
                    "role": "L",
                    "pts": [[-1.4, 2.15], [-1.6, 1.0], [-1.65, 0.3], [-3.35, 0.24]]
                },
                {
                    "role": "A",
                    "pts": [[0.1, 2.1], [0.5, 1.1], [0.75, 0.18]]
                },
                {
                    "role": "a",
                    "pts": [[-0.02, 2.02], [0.35, 1.05], [0.58, 0.14]]
                }
            ]
        }
    ]
}
