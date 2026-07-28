"""Reach pose: Wall Chest Opener."""

MOVE = {
    "id": "wall_chest",
    "name": "Wall Chest Opener",
    "layout": "static",
    "cue": "Forearm flat on a wall or doorframe at shoulder height, then turn the chest away from that arm until the front of the shoulder opens.",
    "frames": [
        {
            "head": [0.15, 7.75],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.1, 7.1], [0, 6.7], [0, 3.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [0.12, 1.85], [0.18, 0.12], [0.85, 0.1]]
                },
                {
                    "role": "l",
                    "pts": [[0, 3.7], [-0.15, 1.85], [-0.15, 0.12], [0.5, 0.1]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [-1.0, 6.75], [-1.85, 6.8]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.7], [0.5, 5.35], [0.55, 4.0]]
                }
            ],
            "props": [[[-2.05, 0.0], [-2.05, 8.6]], [[-1.85, 6.8], [-1.85, 7.9]]]
        }
    ]
}
