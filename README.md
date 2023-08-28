# A custom Gymnasium environment - gym-shower

This is a custom gym environment for registering local env. This env is based on repo https://github.com/nicknochnack/OpenAI-Reinforcement-Learning-with-Custom-Environment.

# Usage

### clone this repo

```
git clone https://github.com/alex-yue-wu/gym-shower.git
```

### install env (restart RunTime if on Colab)

```
cd gym-shower && pip install -e .
```

### example of initiating env

```
import gymnasium
import gym_shower
env = gymnasium.make('gym-shower-v1')
```
