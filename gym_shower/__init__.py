from gymnasium.envs.registration import register

# Register the environment
register(
    id='gym-shower-v1',
    entry_point='gym_shower.envs:ShowerEnv',
)
