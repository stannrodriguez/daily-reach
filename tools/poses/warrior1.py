"""Reach pose: Warrior 1."""

MOVE = {
    "id": "warrior1",
    "name": "Warrior 1",
    "layout": "static",
    "cue": "Front knee bends, back heel roots, arms reach tall.",
    "frames": [
        {
            "head": [0.2, 7.0],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.18, 6.4], [0.1, 5.9], [0, 2.9]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.9], [1.5, 1.6], [1.6, 0.15], [2.3, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.9], [-1.4, 1.5], [-2.6, 0.2], [-3.25, 0.15]]
                },
                {
                    "role": "A",
                    "pts": [[0.1, 5.9], [0.4, 7.3], [0.55, 8.65]]
                },
                {
                    "role": "a",
                    "pts": [[0.1, 5.9], [-0.05, 7.32], [0.05, 8.68]]
                }
            ]
        }
    ]
}
