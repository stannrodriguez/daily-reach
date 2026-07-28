"""Reach pose: Pigeon (bespoke gradient skeleton)."""

MOVE = {
    "id": "pigeon",
    "name": "Pigeon",
    "layout": "static",
    "cue": "Front shin forward, back leg long - let the hips settle.",
    "frames": [
        {
            "head": [0.32, 3.8],
            "head_r": 0.44,
            "ground": True,
            "chains": [
                {
                    "role": "a", "widths": [0.09, 0.075, 0.05],
                    "pts": [[0.02, 3.0], [0.3, 1.85], [0.52, 0.14]]
                },
                {
                    "role": "L", "widths": [0.235, 0.145, 0.085, 0.05],
                    "pts": [[-0.05, 0.82], [-1.6, 0.5], [-3.1, 0.24], [-3.62, 0.4]]
                },
                {
                    "role": "L", "widths": [0.235, 0.15, 0.07],
                    "pts": [[0.0, 0.85], [1.15, 0.62], [0.5, 0.2]]
                },
                {
                    "role": "S", "widths": [0.24, 0.185, 0.15],
                    "pts": [[0.0, 0.9], [0.18, 2.2], [0.25, 3.1]]
                },
                {
                    "role": "A", "widths": [0.11, 0.085, 0.05],
                    "pts": [[0.25, 3.05], [0.62, 1.9], [0.92, 0.16]]
                }
            ],
            "dash": [[[-0.05, 0.82], [-3.55, 0.35]]],
            "arrows": [[-0.75, 1.9, 0.0, -1.0], [-3.35, 1.0, -1.0, -0.3]]
        }
    ]
}
