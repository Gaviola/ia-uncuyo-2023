import numpy as np
class Agent:

    def __init__(self, posX: int, posY: int, grid: np.ndarray) -> None:
        self.posX = posX
        self.posY = posY
        self.grid = grid
        self.life = 1000
    
    def up(self) -> None:
        self.posX += 1
        self.life -= 1
    
    def down(self) -> None:
        self.posX -= 1
        self.life -= 1
    
    def left(self) -> None:
        self.posY -= 1
        self.life -= 1
    
    def right(self) -> None:
        self.posY += 1
        self.life -= 1
    
    def idle(self) -> None:
        self.life -= 1
  
    def suck(self) -> None:
        if self.perspective():
            self.grid[self.posX][self.posY] = 0
            self.life -= 1
    
    def perspective(self) -> bool:
        return self.grid[self.posX][self.posY] == 1
    