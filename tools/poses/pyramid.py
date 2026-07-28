"""Reach pose: Pyramid."""

MOVE = {
    "id": "pyramid",
    "name": "Pyramid",
    "layout": "static",
    "cue": "Hamstring stretch lives in the length of the spine, not the depth of the fold.",
    "frames": [
        {
            "head": [2.75, 1.95],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.15, 2.25], [1.75, 2.55], [0, 3.5]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.5], [1.1, 1.8], [2.1, 0.15], [2.75, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.5], [-1.1, 1.8], [-2.1, 0.15], [-1.5, 0.12]]
                },
                {
                    "role": "A",
                    "pts": [[1.75, 2.55], [1.95, 1.35], [2.15, 0.18]]
                },
                {
                    "role": "a",
                    "pts": [[1.6, 2.48], [1.8, 1.3], [2.0, 0.15]]
                }
            ]
        }
    ]
}
