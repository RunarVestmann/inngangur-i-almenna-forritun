import random
from grid import GRID_WIDTH, GRID_HEIGHT

class Food:
    def __init__(self):
        self.x = random.randint(0, GRID_WIDTH-1)
        self.y = random.randint(0, GRID_HEIGHT-1)

    def draw(self, grid):
        grid.array[self.y][self.x] = "F"

    def respawn(self):
        self.__init__()
