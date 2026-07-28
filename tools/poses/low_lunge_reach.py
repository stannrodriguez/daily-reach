"""Reach pose: Low Lunge with Overhead Reach."""

MOVE = {
    "id": "low_lunge_reach",
    "name": "Low Lunge with Overhead Reach",
    "layout": "static",
    "cue": "Low lunge, back knee down, both arms sweep overhead.",
    "frames": [
        {
            "head": [0.6, 6.4],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.4, 5.82], [0.15, 5.3], [0, 2.4]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.4], [1.4, 1.6], [1.5, 0.15], [2.2, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.4], [-1.6, 0.5], [-3.2, 0.3], [-3.8, 0.18]]
                },
                {
                    "role": "A",
                    "pts": [[0.15, 5.3], [-0.45, 6.6], [-0.95, 7.95]]
                },
                {
                    "role": "a",
                    "pts": [[0.15, 5.3], [-0.22, 6.78], [-0.62, 8.2]]
                }
            ]
        }
    ]
}
