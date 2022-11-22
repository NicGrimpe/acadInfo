import gym
from maps import maps, optimalSteps

points = 0

if __name__ == "__main__":

    for i in range(10):
        env = gym.make('FrozenLake-v1', desc=maps[i], is_slippery=False, render_mode="ansi")
        observation, info = env.reset(seed=42)
        reward = 0

        BEST_PATH = []
        globalMemory = None

        def init():     
            return None

        def calculate_next_step(observation, info, reward):
            action = env.action_space.sample()
            return action

        globalMemory = init()

        deathCounter = 0
        moveCounter = 0
        gotFirstPoint = False
        while moveCounter < 20000:
            action = calculate_next_step(observation, info, reward)
            moveCounter+=1
            observation, reward, terminated, truncated, info = env.step(action)

            if terminated or truncated:
                if reward == 1 and gotFirstPoint == False:
                    points += 1
                    gotFirstPoint = True
                else:
                    deathCounter += 1
                    if deathCounter == 20:
                        break
                
                observation, info = env.reset()
                
        env.close()
        print(f"Best path {BEST_PATH} is of lenght {len(BEST_PATH)}")
        print(f"Killed {deathCounter} lutins")
        env.reset()
        for step in BEST_PATH:
            observation, reward, terminated, truncated, info = env.step(step)
        if reward == 1 and len(BEST_PATH) <= optimalSteps[i]:
            points += 1

    print(f"Got {points} points")
