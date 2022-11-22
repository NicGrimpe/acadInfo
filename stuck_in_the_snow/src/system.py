import random
import copy

from src.position import Position

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

