"""Reach pose: Lizard."""

MOVE = {
    "id": "lizard",
    "name": "Lizard",
    "layout": "static",
    "cue": "Front foot outside the same-side hand, back knee down or lifted.",
    "frames": [
        {
            "head": [1.5, 1.72],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.85, 1.78], [0.55, 1.8], [-0.9, 1.55]]
                },
                {
                    "role": "L",
                    "pts": [[-0.9, 1.55], [1.5, 1.6], [2.15, 0.15], [2.85, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[-0.9, 1.55], [-1.9, 0.55], [-2.6, 0.28], [-4.15, 0.2]]
                },
                {
                    "role": "A",
                    "pts": [[0.55, 1.8], [0.75, 0.4], [1.75, 0.25]]
                },
                {
                    "role": "a",
                    "pts": [[0.42, 1.68], [0.6, 0.3], [1.6, 0.15]]
                }
            ]
        }
    ]
}
