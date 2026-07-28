"""Reach pose: Runner's Lunge."""

MOVE = {
    "id": "runners_lunge",
    "name": "Runner's Lunge",
    "layout": "static",
    "cue": "Front foot between the hands, back leg long and strong, hips low.",
    "frames": [
        {
            "head": [1.25, 4.95],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[1.1, 4.4], [0.9, 4.05], [0, 2.2]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.2], [1.45, 1.7], [1.95, 0.15], [2.65, 0.12]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.2], [-1.75, 1.15], [-3.3, 0.25], [-3.95, 0.15]]
                },
                {
                    "role": "A",
                    "pts": [[0.9, 4.05], [1.5, 2.4], [1.75, 0.15]]
                },
                {
                    "role": "a",
                    "pts": [[0.75, 3.98], [1.35, 2.35], [1.6, 0.12]]
                }
            ]
        }
    ]
}
