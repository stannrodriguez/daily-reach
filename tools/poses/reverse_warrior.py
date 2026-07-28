"""Reach pose: Reverse Warrior."""

MOVE = {
    "id": "reverse_warrior",
    "name": "Reverse Warrior",
    "layout": "static",
    "cue": "Lengthen the side body before you lean.",
    "frames": [
        {
            "head": [0.2, 6.95],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.1, 6.35], [-0.05, 5.9], [0, 2.9]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.9], [1.5, 1.6], [1.7, 0.18], [2.4, 0.15]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.9], [-1.3, 1.5], [-2.6, 0.22], [-3.3, 0.2]]
                },
                {
                    "role": "A",
                    "pts": [[-0.05, 5.9], [-0.75, 7.15], [-1.35, 8.3]]
                },
                {
                    "role": "A",
                    "pts": [[-0.1, 5.8], [-1.0, 4.55], [-1.7, 3.4]]
                }
            ]
        }
    ]
}
