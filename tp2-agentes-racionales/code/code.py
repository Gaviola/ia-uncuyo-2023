from actions import Action
from agent import Agent

class Environment:

    def __init__(self,sizeX:int,sizeY:int,init_posX:int,init_posY:int,dirt_rate:float) -> None:
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.init_posX = init_posX
        self.init_posY = init_posY
        self.dirt_rate = dirt_rate
        return self
        
    def accept_actions(self,action:Action) -> None:
        if (action is Action):
            if (action == Action.Up):
                if (self.posX + 1 <= self.sizeX):
                    self.posX =+ 1
            if (action == Action.Down):
                if (self.posX - 1 >= 0):
                    self.posX =- 1
            if (action == Action.Right):
                if (self.posY + 1 <= self.sizeY):
                    self.posY =+ 1
            if (action == Action.Left):
                if (self.posY - 1 >= 0):
                    self.posY =- 1
            if (action == Action.Clean):
                pass
        return

    def is_dirty(self, agent: Agent) -> None:
        
        return

    def get_performance(self) -> None:
        return

    def print_environment(self) -> None:
        return