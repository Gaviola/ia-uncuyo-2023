from code import Environment

class Agent:

    def __init__(self, posX: int, posY: int) -> None:
        self.posX = posX
        self.posY = posY
        self.life = 1000

    def clean(self, environment: Environment) -> None:
        
        return