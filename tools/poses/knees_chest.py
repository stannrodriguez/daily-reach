"""Reach pose: Knees to Chest."""

MOVE = {
    "id": "knees_chest",
    "name": "Knees to Chest",
    "layout": "static",
    "cue": "Hug both knees in, low back pressing into the floor.",
    "frames": [
        {
            "head": [-2.75, 0.85],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-2.2, 0.72], [-1.75, 0.7], [0.2, 0.75]]
                },
                {
                    "role": "L",
                    "pts": [[0.2, 0.75], [0.9, 2.0], [-0.35, 2.5]]
                },
                {
                    "role": "l",
                    "pts": [[0.2, 0.62], [1.15, 1.8], [-0.1, 2.35]]
                },
                {
                    "role": "A",
                    "pts": [[-1.75, 0.7], [-0.85, 1.6], [0.05, 2.15]]
                }
            ]
        }
    ]
}
