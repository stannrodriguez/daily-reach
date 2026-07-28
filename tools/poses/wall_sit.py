"""Reach pose: Wall Sit."""

MOVE = {
    "id": "wall_sit",
    "name": "Wall Sit",
    "layout": "static",
    "cue": "Back flat to a wall, slide down until the knees are near 90 degrees.",
    "frames": [
        {
            "head": [-0.2, 6.05],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-0.22, 5.42], [-0.3, 4.9], [-0.3, 2.0]]
                },
                {
                    "role": "L",
                    "pts": [[-0.3, 2.0], [1.6, 2.05], [1.65, 0.15], [2.35, 0.1]]
                },
                {
                    "role": "l",
                    "pts": [[-0.3, 2.0], [1.45, 1.9], [1.5, 0.12], [2.2, 0.08]]
                },
                {
                    "role": "A",
                    "pts": [[-0.3, 4.9], [0.35, 3.6], [0.95, 2.4]]
                }
            ],
            "props": [[[-0.8, 0.0], [-0.8, 6.9]]]
        }
    ]
}
