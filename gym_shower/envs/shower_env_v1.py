from gymnasium import Env
from gymnasium.spaces import Discrete, Box
import numpy as np
import random


class ShowerEnv(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        self.action_space = Discrete(3)
        # Temperature array
        self.observation_space = Box(low=np.array(
            [0]), high=np.array([100]), dtype=np.float64)
        # Set start temp
        self.state = 38 + random.randint(-3, 3)
        self.state = np.array([self.state], dtype='float64')  # 1d-array
        # Set shower length
        self.shower_length = 60
        # optimum temperature for info
        self.state_optimum = 38

    def _get_obs(self):
        return self.state

    def _get_info(self):
        return {"distance": self.state_optimum - self.state[0]}

    def step(self, action):
        # Apply action
        # 0 -1 = -1 temperature
        # 1 -1 = 0
        # 2 -1 = 1 temperature
        self.state += action - 1
        self.state = self.state.astype('float64')
        # print(self.state, self.state.shape)
        # Reduce shower length by 1 second
        self.shower_length -= 1

        # Calculate reward
        if self.state[0] >= 37 and self.state[0] <= 39:
            reward = 1
        else:
            reward = -1

        # Check if shower is done
        if self.shower_length <= 0:
            terminated = True
        else:
            terminated = False

        # Apply temperature noise
        # self.state += random.randint(-1,1)

        # get observation
        # observation = self._get_obs()
        # Set placeholder for info
        info = self._get_info()

        # time limit
        truncated = False

        # Return step information
        return self.state, reward, terminated, truncated, info

    def render(self):
        # Implement viz
        pass

    def reset(self, seed=None, options=None):
        # set seed
        super().reset(seed=seed)
        # Reset shower temperature
        self.state = 38 + random.randint(-3, 3)
        self.state = np.array([self.state], dtype='float64')
        # Reset shower time
        self.shower_length = 60

        info = self._get_info()

        return self.state, info
