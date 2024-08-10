import numpy as np

class RobotController:
    def __init__(self):
        self.target = np.array([1.0, 1.0])

    def update(self, observation):
        position = observation[:2]
        velocity = observation[2:]

        # Simple proportional control
        direction = self.target - position
        action = np.clip(direction, -1, 1)

        return action