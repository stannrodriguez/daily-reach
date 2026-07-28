"""Reach pose: Happy Baby."""

MOVE = {
    "id": "happy_baby",
    "name": "Happy Baby",
    "layout": "static",
    "cue": "On the back, knees wide toward the ribs, hold the outer feet or shins with the shins vertical.",
    "frames": [
        {
            "head": [-2.55, 0.82],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-2.0, 0.7], [-1.6, 0.7], [1.3, 0.7]]
                },
                {
                    "role": "L",
                    "pts": [[1.3, 0.7], [2.1, 2.2], [1.6, 3.85]]
                },
                {
                    "role": "l",
                    "pts": [[-1.6, 0.7], [-0.3, 2.3], [1.42, 3.68]]
                }
            ]
        }
    ]
}
