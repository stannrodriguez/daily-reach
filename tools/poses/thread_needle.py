"""Reach pose: Thread the Needle."""

MOVE = {
    "id": "thread_needle",
    "name": "Thread the Needle",
    "layout": "static",
    "cue": "From hands and knees, slide the right arm under the left, shoulder and temple to the mat.",
    "frames": [
        {
            "head": [1.85, 0.75],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[1.3, 0.85], [0.9, 1.15], [0, 2.0], [-1.4, 2.2]]
                },
                {
                    "role": "L",
                    "pts": [[-1.4, 2.2], [-1.5, 0.35], [-3.2, 0.28], [-3.8, 0.2]]
                },
                {
                    "role": "A",
                    "pts": [[0.9, 1.15], [1.5, 0.3], [2.8, 0.2]]
                },
                {
                    "role": "A",
                    "pts": [[0.95, 1.3], [1.1, 2.5], [1.55, 3.5]]
                }
            ]
        }
    ]
}
