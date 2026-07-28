"""Reach pose: Butterfly."""

MOVE = {
    "id": "butterfly",
    "name": "Butterfly",
    "layout": "static",
    "cue": "Soles of the feet together, knees wide.",
    "frames": [
        {
            "head": [0, 4.7],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0, 4.08], [0, 3.6], [0, 0.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 0.7], [1.6, 0.85], [0.42, 0.42]]
                },
                {
                    "role": "l",
                    "pts": [[0, 0.7], [-1.6, 0.85], [-0.42, 0.42]]
                },
                {
                    "role": "A",
                    "pts": [[0, 3.6], [0.6, 2.2], [0.42, 0.8]]
                },
                {
                    "role": "a",
                    "pts": [[0, 3.6], [-0.6, 2.2], [-0.42, 0.8]]
                }
            ]
        }
    ]
}
