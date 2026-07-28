"""Reach pose: Wide Straddle Fold."""

MOVE = {
    "id": "straddle_fold",
    "name": "Wide Straddle Fold",
    "layout": "static",
    "cue": "Seated, legs wide, toes up.",
    "frames": [
        {
            "head": [0, 0.95],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0, 1.7], [0, 2.1], [0, 2.55]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.55], [-2.2, 1.05], [-4.2, 0.15], [-4.5, 0.72]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.55], [2.2, 1.05], [4.2, 0.15], [4.5, 0.72]]
                },
                {
                    "role": "A",
                    "pts": [[0, 2.1], [-1.05, 1.15], [-1.4, 0.35]]
                },
                {
                    "role": "A",
                    "pts": [[0, 2.1], [1.05, 1.15], [1.4, 0.35]]
                }
            ]
        }
    ]
}
