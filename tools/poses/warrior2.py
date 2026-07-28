"""Reach pose: Warrior 2 (bespoke gradient skeleton)."""

MOVE = {
    "id": "warrior2",
    "name": "Warrior 2",
    "layout": "static",
    "cue": "Sink into the front knee; reach through both hands at once.",
    "frames": [
        {
            "head": [0.04, 6.3],
            "head_r": 0.44,
            "ground": True,
            "chains": [
                {
                    "role": "L", "widths": [0.235, 0.15, 0.085, 0.05],
                    "pts": [[0.0, 2.85], [1.5, 1.6], [1.7, 0.2], [2.42, 0.15]]
                },
                {
                    "role": "L", "widths": [0.235, 0.145, 0.085, 0.05],
                    "pts": [[-0.04, 2.85], [-1.3, 1.5], [-2.6, 0.24], [-3.28, 0.2]]
                },
                {
                    "role": "S", "widths": [0.235, 0.185, 0.15],
                    "pts": [[0.0, 2.9], [0.0, 4.4], [0.0, 5.5]]
                },
                {
                    "role": "A", "widths": [0.13, 0.1, 0.05],
                    "pts": [[0.0, 5.45], [1.5, 5.58], [2.85, 5.62]]
                },
                {
                    "role": "A", "widths": [0.13, 0.1, 0.05],
                    "pts": [[0.0, 5.45], [-1.5, 5.58], [-2.85, 5.62]]
                }
            ],
            "dash": [[[-2.85, 5.62], [2.85, 5.62]]],
            "arrows": [[-3.1, 5.85, -1.0, 0.0], [3.1, 5.85, 1.0, 0.0]]
        }
    ]
}
