"""Reach pose: Extended Side Angle."""

MOVE = {
    "id": "side_angle",
    "name": "Extended Side Angle",
    "layout": "static",
    "cue": "From Warrior 2, set the front forearm on the front thigh (or fingertips to the floor) and sweep the top arm over the ear.",
    "frames": [
        {
            "head": [2.05, 5.15],
            "head_r": 0.435,
            "ground": True,
            "chains": [
                {
                    "role": "S",
                    "pts": [[1.6, 4.95], [1.2, 4.75], [0, 2.9]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.9], [1.5, 1.6], [1.7, 0.18], [2.4, 0.15]]
                },
                {
                    "role": "L",
                    "pts": [[0, 2.9], [-1.3, 1.5], [-2.6, 0.22], [-3.3, 0.2]]
                },
                {
                    "role": "A",
                    "pts": [[1.2, 4.75], [1.55, 3.5], [1.9, 2.35]]
                },
                {
                    "role": "A",
                    "pts": [[1.3, 4.9], [2.4, 6.05], [3.4, 7.05]]
                }
            ]
        }
    ]
}
