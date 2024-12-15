import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def get_robot_position(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                return x, y

def is_touching_space(grid, position, direction):
    x, y = position
    if direction == "<":
        if x == 0:
            return False
        return grid[y][x-1] == "."
    elif direction == ">":
        if x == len(grid[y])-1:
            return False
        return grid[y][x+1] == "."
    elif direction == "^":
        if y == 0:
            return False
        return grid[y-1][x] == "."
    elif direction == "v":
        if y == len(grid)-1:
            return False
        return grid[y+1][x] == "."

def is_touching_wall(grid, position, direction):
    x, y = position
    if direction == "<":
        if x == 0:
            return True
        return grid[y][x-1] == "#"
    elif direction == ">":
        if x == len(grid[y])-1:
            return True
        return grid[y][x+1] == "#"
    elif direction == "^":
        if y == 0:
            return True
        return grid[y-1][x] == "#"
    elif direction == "v":
        if y == len(grid)-1:
            return True
        return grid[y+1][x] == "#"

def get_pushable_region(grid, position, direction):
    x, y = position
    squares = []
    if direction == "<":
        for x in range(x-1, -1, -1):
            if grid[y][x] == "#":
                break
            squares.append([x, y, grid[y][x]])
    elif direction == ">":
        for x in range(x+1, len(grid[y])):
            if grid[y][x] == "#":
                break
            squares.append([x, y, grid[y][x]])
    elif direction == "^":
        for y in range(y-1, -1, -1):
            if grid[y][x] == "#":
                break
            squares.append([x, y, grid[y][x]])
    elif direction == "v":
        for y in range(y+1, len(grid)):
            if grid[y][x] == "#":
                break
            squares.append([x, y, grid[y][x]])
    
    # if therare no '.' then there are no spaces to move things into; return empty list
    if "." not in [grid[y][x] for x, y, val in squares]:
        return []
    return squares

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    grid = []
    moves = []
    finished_grid = False
    for line in data_file:
        line = line.strip()
        if not finished_grid:
            if not line:
                finished_grid = True
            else:
                grid.append(list(line))
        else:
            moves.extend(line)

    for move in moves:  
        robot_position = get_robot_position(grid)
        if is_touching_space(grid, robot_position, move):
            x, y = robot_position
            grid[y][x] = "."
            if move == "<":
                x -= 1
            elif move == ">":
                x += 1
            elif move == "^":
                y -= 1
            elif move == "v":
                y += 1
            grid[y][x] = "@"
        elif not is_touching_wall(grid, robot_position, move):
            squares_in_front = get_pushable_region(grid, robot_position, move)
            if not squares_in_front:
                continue

            # Find index of first '.'
            index_square = next((i for i, square in enumerate(squares_in_front) if square[2] == "."), None)
            if index_square is None:
                continue

            new_list_of_squares_in_front = []
            next_val = "@"
            for index, (temp_x, temp_y, temp_val) in enumerate(squares_in_front):
                if index > index_square:
                    break
                new_list_of_squares_in_front.append([temp_x, temp_y, next_val])
                next_val = temp_val

            # Set current square to '.'
            x, y = robot_position
            grid[y][x] = "."

            # Apply all changes from new_list_of_squares_in_front
            for x, y, val in new_list_of_squares_in_front:
                grid[y][x] = val

    final_box_positions = [(x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == "O"]
    total = sum((y * 100) + x for x, y in final_box_positions)
    print_and_verify_answer(mode, "one", total, expected)

def run_part_two(mode, expected = None):

    data_file = open_file( mode + ".txt")

    # -------------------------------
    # Not attempted this yet!
    # Challenge: Boxes are double-width, so the "move" logic needs to be much more complex
    # (need to allow for a 'chain reaction' which will push boxes which aren't on the current line)

    answer = None # <-- Change this to answer
    # -------------------------------
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 2028)
run_part_one("test2", 10092)
run_part_one("prod", 1497888)
# run_part_two("test", 0)
# run_part_two("prod")
# Now run it and watch the magic happen 🪄