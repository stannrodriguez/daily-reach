"""Reach pose: Supine Figure 4."""

MOVE = {
    "id": "figure4_supine",
    "name": "Supine Figure 4",
    "layout": "static",
    "cue": "On the back, cross one ankle over the opposite knee and draw the bottom thigh toward the chest.",
    "frames": [
        {
            "head": [-2.95, 0.85],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-2.4, 0.72], [-1.95, 0.7], [0.1, 0.75]]
                },
                {
                    "role": "L",
                    "pts": [[0.1, 0.75], [1.2, 2.2], [0.1, 3.0]]
                },
                {
                    "role": "L",
                    "pts": [[0.1, 0.75], [1.95, 1.45], [0.7, 1.6]]
                },
                {
                    "role": "A",
                    "pts": [[-1.95, 0.7], [-0.75, 1.6], [0.55, 2.35]]
                }
            ]
        }
    ]
}
