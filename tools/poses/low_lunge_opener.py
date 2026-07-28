"""Reach pose: Low Lunge Hip Opener."""

MOVE = {
    "id": "low_lunge_opener",
    "name": "Low Lunge Hip Opener",
    "layout": "static",
    "cue": "Tuck the tailbone slightly \u2014 the stretch moves from the low back into the hip.",
    "frames": [
        {
            "head": [0.28, 6.35],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[0.25, 5.75], [0.15, 5.3], [0, 2.4]]
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
                    "pts": [[0.15, 5.3], [0.75, 3.7], [1.3, 1.95]]
                },
                {
                    "role": "a",
                    "pts": [[0.02, 5.24], [0.6, 3.65], [1.15, 1.9]]
                }
            ]
        }
    ]
}
