def init():
    import random
    import copy
    
    class Position():
        def __init__(self, squarreNumber) -> None:
            self.x = squarreNumber % 8
            self.y = squarreNumber // 8

        def isXLeaning(self):
            return self.x > self.y

        def moveStep(self, step):
            if step == 0:
                self.gauche()
            elif step == 1:
                self.bas()
            elif step == 2:
                self.droite()
            else:
                self.haut()

        def droite(self):
            self.x = self.x + 1

        def bas(self):
            self.y = self.y + 1

        def gauche(self):
            self.x = self.x - 1

        def haut(self):
            self.y = self.y - 1

        def __str__(self) -> str:
            return f"x: {self.x} y: {self.y}"

        def __eq__(self, __o: object) -> bool:
            return self.x == __o.x and self.y == __o.y

    class System():
        def __init__(self) -> None:
            self.currentPath = []
            self.holes = []
            self.position = Position(0)

        def reset(self):
            self.currentPath = []
            self.position = Position(0)

        def resetPath(self):
            self.currentPath = []

        def wasItAHole(self, position):
            return self.position != position

        def wasItAWin(self, position, reward):
            return self.wasItAHole(position) and reward == 1

        def saveIfIsBestPath(self, bestPath):
            if len(self.currentPath) < len(bestPath) or len(bestPath) == 0:
                return self.currentPath
            return None

        def rememberHole(self):
            print(f"new hole {self.position}")
            self.holes.append(self.position)
            self.position = Position(0)

        def evaluateNextStep(self, currentPosition):
            isViablePosition = False
            while not isViablePosition:
                pos = copy.copy(currentPosition)
                
                step = random.randint(0,100)
                if step <= 40:
                    step = 1
                elif step <= 80:
                    step = 2
                elif step <= 90:
                    step = 0
                else:
                    step = 3

                pos.moveStep(step)
                if self.isValidPosition(pos):
                    self.position = pos
                    self.currentPath.append(step)
                    return step

        def isValidPosition(self, position):
            for hole in self.holes:
                if hole == position:
                    return False

            if position.x > 7 or position.x < 0:
                return False

            if position.y > 7 or position.y < 0:
                return False

            return True
            
    return System()

def calculate_next_step(observation, info, reward):
    class Position():
        def __init__(self, squarreNumber) -> None:
            self.x = squarreNumber % 8
            self.y = squarreNumber // 8

        def isXLeaning(self):
            return self.x > self.y

        def moveStep(self, step):
            if step == 0:
                self.gauche()
            elif step == 1:
                self.bas()
            elif step == 2:
                self.droite()
            else:
                self.haut()

        def droite(self):
            self.x = self.x + 1

        def bas(self):
            self.y = self.y + 1

        def gauche(self):
            self.x = self.x - 1

        def haut(self):
            self.y = self.y - 1

        def __str__(self) -> str:
            return f"x: {self.x} y: {self.y}"

        def __eq__(self, __o: object) -> bool:
            return self.x == __o.x and self.y == __o.y
            
    position = Position(observation)

    global BEST_PATH
    if globalMemory.wasItAWin(position, reward):
        path = globalMemory.saveIfIsBestPath(BEST_PATH)
        if path:
            pathLen = len(path)
            BEST_PATH = path
            print(f"New path {path} of len {pathLen}")
        globalMemory.reset()

    if globalMemory.wasItAHole(position):
        globalMemory.rememberHole()
        globalMemory.resetPath()

    action = globalMemory.evaluateNextStep(position)
    return action