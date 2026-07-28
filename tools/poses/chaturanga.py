"""Reach pose: Plank Shift-Forward Lower."""

MOVE = {
    "id": "chaturanga",
    "name": "Plank Shift-Forward Lower",
    "layout": "two",
    "cue": "Elbows brush the ribs. Lower knees first if the chest drops faster than the hips.",
    "frames": [
        {
            "head": [1.06, 3.2],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.75, 3.1], [0, 2.9], [-2.7, 2.2]]
                },
                {
                    "role": "A",
                    "pts": [[0, 2.9], [0.03, 1.5], [0.05, 0.12]]
                },
                {
                    "role": "a",
                    "pts": [[-0.22, 2.85], [-0.2, 1.5], [-0.18, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[-2.7, 2.2], [-4.5, 1.4], [-6.2, 0.6], [-6.6, 0.15]]
                }
            ]
        },
        {
            "head": [1.05, 1.72],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.72, 1.6], [0, 1.5], [-2.75, 1.35]]
                },
                {
                    "role": "A",
                    "pts": [[0, 1.5], [-1.0, 0.7], [-0.85, 0.12]]
                },
                {
                    "role": "a",
                    "pts": [[-0.2, 1.42], [-1.18, 0.65], [-1.05, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[-2.75, 1.35], [-4.5, 1.1], [-6.2, 0.7], [-6.6, 0.12]]
                }
            ]
        }
    ]
}
