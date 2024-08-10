import gym
from gym import spaces
import numpy as np
import mujoco

class RobotEnv(gym.Env):
    def __init__(self):
        super(RobotEnv, self).__init__()
        
        # Load the MuJoCo model
        self.model = mujoco.MjModel.from_xml_path("models/robot_model.xml")
        self.data = mujoco.MjData(self.model)

        # Define action and observation space
        self.action_space = spaces.Box(low=-1, high=1, shape=(2,), dtype=np.float32)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(4,), dtype=np.float32)

    def step(self, action):
        # Apply action
        self.data.ctrl[:] = action

        # Simulate one step
        mujoco.mj_step(self.model, self.data)

        # Get observation
        obs = self._get_obs()

        # Calculate reward (example: negative distance to a goal)
        reward = -np.linalg.norm(obs[:2] - np.array([1, 1]))

        # Check if episode is done
        done = bool(reward > -0.1)

        return obs, reward, done, {}

    def reset(self):
        mujoco.mj_resetData(self.model, self.data)
        return self._get_obs()

    def render(self):
        # Implement rendering if needed
        pass

    def _get_obs(self):
        return np.concatenate([
            self.data.qpos.flat,
            self.data.qvel.flat
        ])