"""Reach pose: Five-Pointed Star."""

MOVE = {
    "id": "star",
    "name": "Five-Pointed Star",
    "layout": "static",
    "cue": "Feet wide, legs straight, arms wide at shoulder height.",
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
                    "pts": [[0, 3.7], [-1.15, 1.9], [-2.2, 0.12], [-2.7, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [1.15, 1.9], [2.2, 0.12], [2.7, 0.1]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [-1.55, 7.0], [-3.05, 7.3]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [1.55, 7.0], [3.05, 7.3]]
                }
            ]
        }
    ]
}
