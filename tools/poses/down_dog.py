"""Reach pose: Downward Dog (bespoke gradient skeleton + callouts)."""

MOVE = {
    "id": "down_dog",
    "name": "Downward Dog",
    "layout": "static",
    "cue": "Heels are a destination, not a requirement.",
    "frames": [
        {
            "head": [1.7, 0.75],
            "head_r": 0.44,
            "ground": True,
            "chains": [
                {
                    "role": "l", "widths": [0.16, 0.11, 0.07, 0.045],
                    "pts": [[-0.18, 4.15], [-1.5, 2.1], [-2.6, 0.3], [-2.0, 0.14]]
                },
                {
                    "role": "a", "widths": [0.1, 0.08, 0.05],
                    "pts": [[1.62, 1.6], [2.18, 0.78], [2.6, 0.12]]
                },
                {
                    "role": "S",
                    "widths": [0.065, 0.1, 0.155, 0.235, 0.27, 0.155, 0.09, 0.045],
                    "pts": [[3.0, 0.14], [2.5, 0.95], [1.85, 1.8], [0.95, 3.2],
                            [0.0, 4.4], [-1.1, 2.3], [-2.08, 0.28], [-1.5, 0.1]]
                }
            ],
            "dash": [[[0.0, 4.4], [3.0, 0.14]]],
            "arrows": [[-0.42, 4.95, -0.62, 0.85], [-2.6, 1.05, 0.0, -1.0]]
        }
    ],
    "callouts": [
        {"anchor": [0.0, 4.4], "at": [512, 118], "align": "start",
         "lines": ["Hips press up and back"]},
        {"anchor": [2.45, 1.05], "at": [592, 300], "align": "start",
         "lines": ["Spine and arms make", "one straight line"]},
        {"anchor": [1.7, 0.75], "at": [556, 430], "align": "start",
         "lines": ["Head hangs heavy"]},
        {"anchor": [-2.08, 0.4], "at": [182, 318], "align": "end",
         "lines": ["Heels reach", "for the floor"]}
    ]
}
