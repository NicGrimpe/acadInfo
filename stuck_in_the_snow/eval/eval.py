import gym
from maps import maps, optimalSteps

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

points = 0

if __name__ == "__main__":

    for i in range(10):
        try:
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

            bestPathCount = 999
            bestPathCounter = 0
            while moveCounter < 20000:
                action = calculate_next_step(observation, info, reward)
                moveCounter+=1
                bestPathCounter+=1
                observation, reward, terminated, truncated, info = env.step(action)

                if reward == 1:
                    if bestPathCount > bestPathCounter:
                        print(f"New path of length {bestPathCounter}")
                        bestPathCount = bestPathCounter
                    bestPathCounter=0
            
                if terminated or truncated:
                    if reward == 1 and gotFirstPoint == False:
                        print("Got a path!")
                        points += 1
                        gotFirstPoint = True
                    else:
                        deathCounter += 1
                        if deathCounter == 20:
                            break
                    
                    observation, info = env.reset()
                    
            env.close()
            print(f"Best path found is of lenght {bestPathCount}")
            print(f"Optimal path is of lenght {optimalSteps[i]}")

            print(f"Killed {deathCounter} lutins")
            env.reset()
            if bestPathCount <= optimalSteps[i]:
                points += 1
        except:
            print("oops")

    print(f"Got {points} points")
