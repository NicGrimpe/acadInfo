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