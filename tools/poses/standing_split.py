"""Reach pose: Standing Split."""

MOVE = {
    "id": "standing_split",
    "name": "Standing Split",
    "layout": "static",
    "cue": "Four corners of the foot, hips level, buoyant through the knee \u2014 let your crown fall off.",
    "frames": [
        {
            "head": [1.55, 0.95],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0, 3.7], [0.95, 2.85], [1.35, 1.6]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [0.1, 1.85], [0.15, 0.12], [0.8, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [-0.95, 5.4], [-1.8, 7.05], [-2.05, 7.55]]
                },
                {
                    "role": "A",
                    "pts": [[1.35, 1.6], [0.9, 0.95], [0.6, 0.22]]
                },
                {
                    "role": "a",
                    "pts": [[1.2, 1.5], [0.75, 0.85], [0.45, 0.15]]
                }
            ]
        }
    ]
}
