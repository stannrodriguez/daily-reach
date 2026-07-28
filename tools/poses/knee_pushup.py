"""Reach pose: Knee Push-Up."""

MOVE = {
    "id": "knee_pushup",
    "name": "Knee Push-Up",
    "layout": "two",
    "cue": "Knees down, ankles crossed, hips forward so the line runs crown to knees.",
    "frames": [
        {
            "head": [3.05, 3.05],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.72, 2.9], [2.0, 2.75], [-0.75, 2.1]]
                },
                {
                    "role": "A",
                    "pts": [[2.0, 2.75], [2.05, 1.45], [2.1, 0.12]]
                },
                {
                    "role": "a",
                    "pts": [[1.78, 2.7], [1.83, 1.42], [1.88, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[-0.75, 2.1], [-2.0, 0.4], [-3.7, 0.35], [-4.05, 0.8]]
                }
            ]
        },
        {
            "head": [2.72, 1.62],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.4, 1.5], [1.7, 1.4], [-0.85, 1.9]]
                },
                {
                    "role": "A",
                    "pts": [[1.7, 1.4], [1.1, 2.0], [2.1, 0.12]]
                },
                {
                    "role": "a",
                    "pts": [[1.48, 1.35], [0.88, 1.94], [1.88, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[-0.85, 1.9], [-2.0, 0.4], [-3.7, 0.35], [-4.05, 0.8]]
                }
            ]
        }
    ]
}
