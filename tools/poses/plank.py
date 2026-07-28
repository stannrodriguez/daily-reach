"""Reach pose: Plank."""

MOVE = {
    "id": "plank",
    "name": "Plank",
    "layout": "static",
    "cue": "Push the floor away \u2014 don't sag between the shoulder blades.",
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
        }
    ]
}
