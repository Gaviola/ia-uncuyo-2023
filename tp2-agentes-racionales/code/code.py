from actions import Action
from agent import Agent
import numpy as np
import matplotlib.pyplot as plt

class Environment:

    def __init__(self,sizeX: int, sizeY: int, dirt_rate: float) -> None:
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.dirt_rate = dirt_rate
        self.grid = self.init_grid(sizeX,sizeX,dirt_rate)
        self.agent = Agent(np.random.randint(0,sizeX),np.random.randint(0,sizeY),self.grid)
        self.performance = 0
        
    def accept_actions(self,action: Action) -> None:
        if (action == Action.Up.value):
            if (self.agent.posX + 1 <= self.sizeX -1):
                self.agent.up()
        if (action == Action.Down.value):
            if (self.agent.posX - 1 >= 0):
                self.agent.down()
        if (action == Action.Right.value):
            if (self.agent.posY + 1 <= self.sizeY -1):
                self.agent.right()
        if (action == Action.Left.value):
            if (self.agent.posY - 1 >= 0):
                self.agent.left()
        if (action == Action.Nothing.value):
            self.agent.idle()
        if (action == Action.Clean.value):
            if (self.agent.perspective()):
                self.performance += 1
                self.agent.suck()

            

    def is_dirty(self) -> bool:
        is_dirty = False
        for slot in np.nditer(self.grid):
            if slot == 1:
                is_dirty = True
        return is_dirty

    def get_performance(self) -> (int,float):
        movements: int = 1000 - self.agent.life
        movements_per_slot_clean = 0
        if self.performance != 0:
            movements_per_slot_clean = movements/self.performance
            print(f"""
Movements per slot clean: {movements_per_slot_clean}\n
Movements invested to clean: {movements}
 """)
        else:
            print("The environment was clean at the beginning")
        if (self.agent.life == 0):
            print("The Agent could not clean the environment")
        return movements, movements_per_slot_clean

    def print_environment(self) -> None:
        print(f"""
Size: {self.sizeX}x{self.sizeY}\n
Initial Position: {self.agent.posX},{self.agent.posY}\n
Dirt rate: {self.dirt_rate} \n
Grid: \n
{self.grid}
""")
    
    def init_grid(self, sizeX: int, sizeY: int, dirt_rate: float):
        return np.random.choice([0,1],size=(sizeX,sizeY),p=[1-dirt_rate, dirt_rate])
    
    @staticmethod
    def execute(sizeX: int, sizeY: int, dirt_rate: float, attempts: int, random: bool):
        n: int = 0
        movements = []
        movements_per_slot_clean = []
        slots_clean = []
        result = tuple()
        while n < attempts:
            env = Environment(sizeX,sizeY,dirt_rate)
            env.print_environment()
            while env.is_dirty() and env.agent.life != 0:
                if not(random):
                    if env.agent.perspective():
                        action = 5
                    else:
                        action = np.random.randint(0,4)
                else:
                    action = np.random.randint(0,6)
                env.accept_actions(action)
            result = env.get_performance()
            n += 1
            movements.append(result[0])
            movements_per_slot_clean.append(result[1])
            slots_clean.append(env.performance)
        movements = np.array(movements)
        movements_per_slot_clean = np.array(movements_per_slot_clean)
        return movements,movements_per_slot_clean
    
    @staticmethod
    def plot_performance(movements: int, movements_per_slot_clean: int, attempts:int, super_title: str):
        attempts = [x for x in range(10)]
        plt.subplot(1,2,1)
        plt.xlabel("Attempt")
        plt.ylabel("Movements by Attempt")
        plt.title("Total Movements by Attempt")
        plt.grid(axis= "y", linestyle= "--", linewidth = 0.6)
        plt.bar(attempts,movements)

        plt.subplot(1,2,2)
        plt.xlabel("Attempt")
        plt.ylabel("Movements Per Slot Cleaned")
        plt.title("Average Slot Cleaned Per Movement by Attempt")
        plt.grid(axis= "y", linestyle= "--", linewidth = 0.6)
        plt.bar(attempts,movements_per_slot_clean)
        plt.suptitle(super_title)

        plt.show()

    @staticmethod
    def simulate(sizeX: int, sizeY: int, attempts: int, random: bool):
        movements = []
        movements_per_slot = []
        for i in range(4):
            if (i==0):
                result = Environment.execute(sizeX,sizeY,0.1,attempts,random)
                super_title = f"Grid {sizeX}x{sizeY} Dirt_rate: 0.1 " 
            elif (i==1):
                result = Environment.execute(sizeX,sizeY,0.2,attempts,random)
                super_title =f"Grid {sizeX}x{sizeY} Dirt_rate: 0.2"
            elif (i==2):
                result = Environment.execute(sizeX,sizeY,0.4,attempts,random)
                super_title = f"Grid {sizeX}x{sizeY} Dirt_rate: 0.4"
            elif (i==3):
                result = Environment.execute(sizeX,sizeY,0.8,attempts,random)
                super_title = f"Grid {sizeX}x{sizeY} Dirt_rate: 0.8"
            Environment.plot_performance(result[0],result[1],attempts,super_title)
            movements.append(result[0])
            movements_per_slot.append(result[1])
        return movements, movements_per_slot


if __name__ == '__main__':
    attempts = 10
    random = True
    grid2x2 = Environment.simulate(2,2,attempts,random)
    grid4x4 = Environment.simulate(4,4,attempts,random)
    grid8x8 = Environment.simulate(8,8,attempts,random)
    grid16x16 = Environment.simulate(16,16,attempts,random)
    grid32x32 = Environment.simulate(32,32,attempts,random)
    grid64x64 = Environment.simulate(64,64,attempts,random)
    grid128x128 = Environment.simulate(128,128,attempts,random)



