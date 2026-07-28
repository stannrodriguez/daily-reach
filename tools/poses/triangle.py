"""Reach pose: Triangle."""

MOVE = {
    "id": "triangle",
    "name": "Triangle",
    "layout": "static",
    "cue": "Straighten the front leg, reach forward, then set the bottom hand on the shin or a block and open the top arm to the sky.",
    "frames": [
        {
            "head": [3.35, 5.4],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[3.0, 5.22], [2.6, 4.9], [0, 3.5]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.5], [1.15, 1.8], [2.2, 0.15], [2.9, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.5], [-1.15, 1.8], [-2.2, 0.15], [-2.85, 0.12]]
                },
                {
                    "role": "A",
                    "pts": [[2.6, 4.9], [2.5, 3.4], [2.35, 2.0]]
                },
                {
                    "role": "A",
                    "pts": [[2.6, 4.9], [2.7, 6.4], [2.78, 7.85]]
                }
            ]
        }
    ]
}
