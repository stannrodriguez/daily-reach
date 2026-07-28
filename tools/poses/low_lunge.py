"""Reach pose: Low Lunge."""

MOVE = {
    "id": "low_lunge",
    "name": "Low Lunge",
    "layout": "static",
    "cue": "Back knee down, hips sinking forward and down.",
    "frames": [
        {
            "head": [0.28, 6.35],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.25, 5.75], [0.15, 5.3], [0, 2.4]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.4], [1.4, 1.6], [1.5, 0.15], [2.2, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.4], [-1.6, 0.5], [-3.2, 0.3], [-3.8, 0.18]]
                },
                {
                    "role": "A",
                    "pts": [[0.15, 5.3], [0.45, 6.7], [0.6, 8.1]]
                },
                {
                    "role": "a",
                    "pts": [[0.15, 5.3], [0.05, 6.75], [0.1, 8.15]]
                }
            ]
        }
    ]
}
