"""Reach pose: Sphinx."""

MOVE = {
    "id": "sphinx",
    "name": "Sphinx",
    "layout": "static",
    "cue": "Forearms down, chest forward and up, shoulders soft.",
    "frames": [
        {
            "head": [2.4, 2.65],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.1, 2.25], [1.7, 1.9], [0.75, 1.05], [0, 0.55]]
                },
                {
                    "role": "L",
                    "pts": [[0, 0.55], [-1.9, 0.38], [-3.7, 0.28], [-4.3, 0.15]]
                },
                {
                    "role": "l",
                    "pts": [[0.05, 0.42], [-1.85, 0.26], [-3.6, 0.16], [-4.2, 0.05]]
                },
                {
                    "role": "A",
                    "pts": [[1.7, 1.9], [1.85, 0.2], [3.2, 0.15]]
                }
            ]
        }
    ]
}
