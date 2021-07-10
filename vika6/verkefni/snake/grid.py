GRID_WIDTH = 10
GRID_HEIGHT = 10

class Grid:
    def __init__(self):
        self.array = [[" "] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

    def clear(self):
        self.__init__()

    def __str__(self):
        grid_str = ""
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                grid_str += self.array[i][j]
            grid_str += "\n"
        return grid_str