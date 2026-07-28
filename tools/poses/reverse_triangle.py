"""Reach pose: Reverse Triangle."""

MOVE = {
    "id": "reverse_triangle",
    "name": "Reverse Triangle",
    "layout": "static",
    "cue": "Shorten your stance before you deepen the twist.",
    "frames": [
        {
            "head": [2.9, 4.55],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.4, 4.35], [2.0, 4.15], [0, 3.5]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.5], [1.15, 1.8], [2.2, 0.15], [2.9, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.5], [-1.15, 1.8], [-2.2, 0.15], [-1.6, 0.12]]
                },
                {
                    "role": "A",
                    "pts": [[2.0, 4.15], [2.05, 2.3], [2.15, 0.4]]
                },
                {
                    "role": "A",
                    "pts": [[2.05, 4.3], [2.35, 5.85], [2.55, 7.3]]
                }
            ]
        }
    ]
}
