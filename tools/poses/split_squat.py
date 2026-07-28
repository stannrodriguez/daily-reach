"""Reach pose: Split Squat."""

MOVE = {
    "id": "split_squat",
    "name": "Split Squat",
    "layout": "two",
    "cue": "Stagger the feet a stride apart and lower straight down until the back knee kisses the floor.",
    "frames": [
        {
            "head": [0.05, 7.65],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.05, 7.02], [0, 6.56], [0, 3.55]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.55], [0.6, 1.8], [1.15, 0.15], [1.82, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.55], [-0.7, 1.85], [-1.32, 0.35], [-1.7, 0.12]]
                },
                {
                    "role": "A",
                    "pts": [[0, 6.56], [0.2, 5.18], [0.25, 3.82]]
                },
                {
                    "role": "a",
                    "pts": [[-0.15, 6.52], [-0.4, 5.15], [-0.38, 3.8]]
                }
            ]
        },
        {
            "head": [0.2, 6.6],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.18, 5.98], [0.1, 5.5], [0, 2.6]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.6], [1.1, 1.6], [1.2, 0.15], [1.88, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.6], [-1.35, 0.78], [-2.42, 0.32], [-2.85, 0.14]]
                },
                {
                    "role": "A",
                    "pts": [[0.1, 5.5], [0.38, 4.15], [0.42, 2.82]]
                },
                {
                    "role": "a",
                    "pts": [[0.05, 5.42], [-0.28, 4.1], [-0.25, 2.78]]
                }
            ]
        }
    ]
}
