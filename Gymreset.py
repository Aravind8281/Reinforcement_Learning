#reset() function used to bounce back to its original position after execution
import gymnasium as gym
env=gym.make("CartPole-v1",render_mode="rgb_array")
observation,info=env.reset()
print("Observation",observation)
print("Information ",info)
