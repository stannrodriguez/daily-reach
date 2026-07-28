"""Reach pose: Supine Hamstring Stretch."""

MOVE = {
    "id": "supine_ham",
    "name": "Supine Hamstring Stretch",
    "layout": "static",
    "cue": "On the back, loop a towel or belt around one foot and lift that leg toward straight.",
    "frames": [
        {
            "head": [-3.5, 0.82],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[-2.95, 0.7], [-2.5, 0.68], [0, 0.72]]
                },
                {
                    "role": "L",
                    "pts": [[0, 0.72], [0.25, 2.35], [0.5, 3.95]]
                },
                {
                    "role": "L",
                    "pts": [[0, 0.72], [1.75, 0.5], [3.45, 0.42]]
                },
                {
                    "role": "A",
                    "pts": [[-2.5, 0.68], [-1.5, 1.15], [-0.55, 1.7]]
                }
            ],
            "props": [[[-0.55, 1.7], [0.5, 3.95]], [[-0.35, 1.58], [0.66, 3.86]]]
        }
    ]
}
