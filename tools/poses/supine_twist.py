"""Reach pose: Supine Twist."""

MOVE = {
    "id": "supine_twist",
    "name": "Supine Twist",
    "layout": "static",
    "cue": "On the back, draw one knee in and guide it across the body.",
    "frames": [
        {
            "head": [-3.1, 0.78],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-2.65, 0.68], [-2.2, 0.6], [0.3, 0.7]]
                },
                {
                    "role": "L",
                    "pts": [[0.3, 0.7], [1.95, 0.95], [1.45, 0.25]]
                },
                {
                    "role": "l",
                    "pts": [[0.35, 0.85], [2.1, 1.15], [1.6, 0.4]]
                },
                {
                    "role": "A",
                    "pts": [[-2.2, 0.6], [-3.4, 1.5], [-4.55, 0.9]]
                }
            ]
        }
    ]
}
