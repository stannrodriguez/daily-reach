"""Reach pose: Desk / Table Inverted Row."""

MOVE = {
    "id": "inverted_row",
    "name": "Desk / Table Inverted Row",
    "layout": "two",
    "cue": "Lie under a sturdy table, grip the edge, body straight, and pull the chest to the underside.",
    "frames": [
        {
            "head": [-1.05, 1.0],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-0.65, 0.95], [0.05, 0.9], [2.85, 0.7]]
                },
                {
                    "role": "A",
                    "pts": [[0.05, 0.9], [0.05, 2.1], [0.02, 3.28]]
                },
                {
                    "role": "a",
                    "pts": [[0.28, 0.88], [0.28, 2.08], [0.25, 3.26]]
                },
                {
                    "role": "L",
                    "pts": [[2.85, 0.7], [4.6, 0.55], [6.35, 0.42], [6.85, 0.8]]
                }
            ],
            "props": [[[-1.25, 3.35], [1.25, 3.35]]]
        },
        {
            "head": [-1.07, 2.76],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-0.68, 2.68], [0, 2.5], [2.7, 1.9]]
                },
                {
                    "role": "A",
                    "pts": [[0, 2.5], [0.9, 1.75], [0.05, 3.28]]
                },
                {
                    "role": "a",
                    "pts": [[0.25, 2.45], [1.12, 1.72], [0.28, 3.26]]
                },
                {
                    "role": "L",
                    "pts": [[2.7, 1.9], [4.5, 1.35], [6.3, 0.5], [6.8, 0.85]]
                }
            ],
            "props": [[[-1.25, 3.35], [1.25, 3.35]]]
        }
    ]
}
