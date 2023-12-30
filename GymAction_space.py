import gymnasium as gym
env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()

for _ in range(100):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, truncated,terminated, info = env.step(action)

    if truncated or terminated:
        observation, info = env.reset()

env.close()
# action_space
# continuous action represents set of continuous action such as robotic movements etc
# discrete action represents set of discrete action such as chess movement etc
