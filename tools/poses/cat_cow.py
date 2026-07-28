"""Reach pose: Cat / Cow."""

MOVE = {
    "id": "cat_cow",
    "name": "Cat / Cow",
    "layout": "two",
    "cue": "Let the breath lead the spine, not the other way around.",
    "frames": [
        {
            "head": [2.35, 3.25],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.0, 2.7], [1.4, 2.35], [0.0, 1.85], [-1.4, 2.2]]
                },
                {
                    "role": "A",
                    "pts": [[1.4, 2.35], [1.45, 1.2], [1.5, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[-1.4, 2.2], [-1.5, 0.35], [-3.2, 0.28], [-3.8, 0.2]]
                }
            ]
        },
        {
            "head": [2.1, 2.3],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.0, 2.7], [1.4, 2.35], [0.0, 2.95], [-1.4, 2.2]]
                },
                {
                    "role": "A",
                    "pts": [[1.4, 2.35], [1.45, 1.2], [1.5, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[-1.4, 2.2], [-1.5, 0.35], [-3.2, 0.28], [-3.8, 0.2]]
                }
            ]
        }
    ]
}
