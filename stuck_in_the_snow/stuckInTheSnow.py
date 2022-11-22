import gym
from gym.envs.toy_text.frozen_lake import generate_random_map

map = generate_random_map(8, 0.8)
env = gym.make('FrozenLake-v1', desc=map, is_slippery=False, render_mode="human")
observation, info = env.reset(seed=42)
reward = 0

globalMemory = None

def init_system():
    return None

def calculate_next_step(observation, info, reward):
    action = env.action_space.sample()
    return action

moves = 0
deathCounter = 0
maxMoves = 200
if __name__ == "__main__":
    globalMemory = init_system()
    for _ in range(maxMoves):
        action = calculate_next_step(observation, info, reward)
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            if reward == 1:
                print("Win!!")
                moves = _
                break
            else:
                deathCounter = deathCounter + 1
                observation, info = env.reset()
            
    env.close()
    print(f"Took {moves} moves and {deathCounter} lutins")