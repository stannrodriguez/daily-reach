"""Reach pose: Warrior 3."""

MOVE = {
    "id": "warrior3",
    "name": "Warrior 3",
    "layout": "static",
    "cue": "Hinge forward from figure 4 or a lunge until the torso and back leg form one line parallel to the floor.",
    "frames": [
        {
            "head": [3.3, 4.05],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[2.65, 3.98], [2.2, 3.95], [0, 3.7]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [0.1, 1.9], [0.15, 0.12], [0.8, 0.1]]
                },
                {
                    "role": "L",
                    "pts": [[0, 3.7], [-1.8, 3.75], [-3.5, 3.85]]
                },
                {
                    "role": "A",
                    "pts": [[2.2, 3.95], [1.2, 3.5], [0.3, 3.1]]
                },
                {
                    "role": "a",
                    "pts": [[2.15, 3.82], [1.15, 3.35], [0.25, 2.95]]
                }
            ]
        }
    ]
}
