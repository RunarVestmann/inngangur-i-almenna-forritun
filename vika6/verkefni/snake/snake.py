from grid import GRID_WIDTH, GRID_HEIGHT

class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, x, y):
        self.segments = [Segment(x, y)]

    def draw(self, grid):
        for i in range(1, len(self.segments)):
            grid.array[self.segments[i].y][self.segments[i].x] = "S"
        head = self.segments[0]
        grid.array[head.y][head.x] = "H"

    def move(self, direction_str):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].x = self.segments[i-1].x
            self.segments[i].y = self.segments[i-1].y

        head = self.segments[0]
        if direction_str == "w":
            head.y = (head.y - 1) % GRID_HEIGHT
        elif direction_str == "s":
            head.y = (head.y + 1) % GRID_HEIGHT
        elif direction_str == "d":
            head.x = (head.x + 1) % GRID_WIDTH
        elif direction_str == "a":
            head.x = (head.x - 1) % GRID_WIDTH

    def is_colliding_with(self, other):
        head = self.segments[0]
        return head.x == other.x and head.y == other.y

    def is_colliding_with_self(self):
        for i in range(1, len(self.segments)):
            if self.is_colliding_with(self.segments[i]):
                return True
        return False

    def grow(self):
        self.segments.append(Segment(0, 0))