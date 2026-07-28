"""Reach pose: Plank Shoulder Taps."""

MOVE = {
    "id": "shoulder_taps",
    "name": "Plank Shoulder Taps",
    "layout": "two",
    "cue": "From a high plank with the feet wide, lift one hand and tap the opposite shoulder.",
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
                    "pts": [[0, 2.9], [0.55, 2.15], [-0.28, 2.72]]
                },
                {
                    "role": "A",
                    "pts": [[-0.22, 2.85], [-0.2, 1.5], [-0.18, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[-2.7, 2.2], [-4.5, 1.4], [-6.2, 0.6], [-6.6, 0.15]]
                }
            ]
        }
    ]
}
