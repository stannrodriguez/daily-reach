"""Reach pose: Gentle Standing Backbend."""

MOVE = {
    "id": "standing_backbend",
    "name": "Gentle Standing Backbend",
    "layout": "static",
    "cue": "Hands to the low back, elbows drawing together, lift the chest and lean back a few degrees.",
    "frames": [
        {
            "head": [-0.55, 7.6],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-0.4, 7.0], [-0.15, 6.6], [0.15, 5.2], [0, 3.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [0.05, 1.85], [0.1, 0.12], [0.75, 0.1]]
                },
                {
                    "role": "l",
                    "pts": [[0, 3.7], [-0.18, 1.85], [-0.18, 0.12], [0.45, 0.1]]
                },
                {
                    "role": "A",
                    "pts": [[-0.1, 6.4], [-0.85, 5.3], [-0.35, 4.05]]
                },
                {
                    "role": "a",
                    "pts": [[0.05, 6.35], [-0.7, 5.25], [-0.2, 4.0]]
                }
            ]
        }
    ]
}
