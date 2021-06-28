def initialize_grid(grid):
    grid['1'] = ' '
    grid['2'] = ' '
    grid['3'] = ' '
    grid['4'] = ' '
    grid['5'] = ' '
    grid['6'] = ' '
    grid['7'] = ' '
    grid['8'] = ' '
    grid['9'] = ' '

def print_grid(grid):
    print(f"{grid['7']}|{grid['8']}|{grid['9']}")
    print('-+-+-')
    print(f"{grid['4']}|{grid['5']}|{grid['6']}")
    print('-+-+-')
    print(f"{grid['1']}|{grid['2']}|{grid['3']}")

def check_for_horizontal_win(grid):
    top_row = grid['7'] == grid['8'] == grid['9'] and grid['9'] != ' '
    mid_row = grid['4'] == grid['5'] == grid['6'] and grid['6'] != ' '
    bottom_row = grid['1'] == grid['2'] == grid['3'] and grid['3'] != ' '
    return top_row or mid_row or bottom_row

def check_for_vertical_win(grid):
    left_col = grid['1'] == grid['4'] == grid['7'] and grid['7'] != ' '
    mid_col = grid['2'] == grid['5'] == grid['8'] and grid['8'] != ' '
    right_col = grid['3'] == grid['6'] == grid['9'] and grid['9'] != ' '
    return left_col or mid_col or right_col

def check_for_diagonal_win(grid):
    bottom_left_to_top_right = grid['1'] == grid['5'] == grid['9'] and grid['9'] != ' '
    bottom_right_to_top_left = grid['3'] == grid['5'] == grid['7'] and grid['7'] != ' '
    return bottom_left_to_top_right or bottom_right_to_top_left

def is_game_won(grid):
    return check_for_horizontal_win(grid) or check_for_vertical_win(grid) or check_for_diagonal_win(grid)

def can_a_move_be_played(grid):
    for key in grid:
        if grid[key] == ' ':
            return True
    return False

def get_choice(grid):
    choice = input("Enter your choice: ")
    while choice not in grid:
        print("Please enter a number from 1-9")
        choice = input("Enter your choice: ")
    while grid[choice] != " ":
        print(f"Slot {choice} has already been filled out")
        choice = input("Enter your choice: ")
        while choice not in grid:
            print("Please enter a number from 1-9")
            choice = input("Enter your choice: ")
    return choice

def main():
    grid = {}
    initialize_grid(grid)    
    
    current_symbol = 'X'

    while not is_game_won(grid) and can_a_move_be_played(grid):
        print_grid(grid)
        choice = get_choice(grid)
        grid[choice] = current_symbol
        if current_symbol == 'X':
            current_symbol = 'O'
        else:
            current_symbol = 'X'

    print_grid(grid)
    if is_game_won(grid):
        if current_symbol == 'X':
            print("O won the game")
        else:
            print("X won the game")
    else:
        print("It's a tie")

main()