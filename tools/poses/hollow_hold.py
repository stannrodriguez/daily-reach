"""Reach pose: Hollow Hold."""

MOVE = {
    "id": "hollow_hold",
    "name": "Hollow Hold",
    "layout": "static",
    "cue": "If the low back lifts, raise the legs higher \u2014 the floor should never see daylight.",
    "frames": [
        {
            "head": [-3.55, 2.1],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-3.15, 1.72], [-2.7, 1.5], [0, 0.9]]
                },
                {
                    "role": "L",
                    "pts": [[0, 0.9], [1.8, 1.35], [3.5, 1.85], [4.1, 2.05]]
                },
                {
                    "role": "l",
                    "pts": [[0.05, 0.78], [1.85, 1.2], [3.55, 1.7], [4.15, 1.9]]
                },
                {
                    "role": "A",
                    "pts": [[-2.7, 1.5], [-4.05, 1.95], [-5.35, 2.4]]
                },
                {
                    "role": "a",
                    "pts": [[-2.75, 1.36], [-4.1, 1.8], [-5.4, 2.25]]
                }
            ]
        }
    ]
}
