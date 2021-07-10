from grid import Grid
from food import Food
from snake import Snake

AVAILABLE_DIRECTIONS = ("w", "a", "s", "d")

def draw(objects, grid):
    for object in objects:
        object.draw(grid)
    print(grid, end="")
    grid.clear()

def main():
    grid = Grid()
    food = Food()
    snake = Snake(5, 5)

    objects = (food, snake)
    draw(objects, grid)

    while not snake.is_colliding_with_self():
        if snake.is_colliding_with(food):
            food.respawn()
            snake.grow()

        direction = input("Direction: ").lower().strip()
        if direction in AVAILABLE_DIRECTIONS:
            snake.move(direction)

        draw(objects, grid)

    print(f"Score: {len(snake.segments)}")
    print("Game over")

main()