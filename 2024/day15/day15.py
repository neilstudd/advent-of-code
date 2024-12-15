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
    dx, dy = {"<": -1, ">": 1, "^": 0, "v": 0}[direction], {"<": 0, ">": 0, "^": -1, "v": 1}[direction]
    new_x, new_y = x + dx, y + dy
    if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
        return False
    return grid[new_y][new_x] == "."

def is_touching_wall(grid, position, direction):
    x, y = position
    dx, dy = {"<": -1, ">": 1, "^": 0, "v": 0}[direction], {"<": 0, ">": 0, "^": -1, "v": 1}[direction]
    new_x, new_y = x + dx, y + dy
    if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
        return True
    return grid[new_y][new_x] == "#"

def get_pushable_region(grid, position, direction):
    x, y = position
    squares = []
    dx, dy = {"<": -1, ">": 1, "^": 0, "v": 0}[direction], {"<": 0, ">": 0, "^": -1, "v": 1}[direction]
    while 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
        x, y = x + dx, y + dy
        if grid[y][x] == "#":
            break
        squares.append([x, y, grid[y][x]])
    return [] if "." not in [grid[y][x] for x, y, _ in squares] else squares

def calculate_impacted_area(grid, position, direction):
    x, y = position
    impacted_cells = []
    if direction == "^":
        grid_above = grid[y-1][x]
        if grid_above == "[":
            impacted_cells.append([x, y-1, "["])
            impacted_cells.append([x+1, y-1, "]"])
        elif grid_above == "]":
            impacted_cells.append([x-1, y-1, "["])
            impacted_cells.append([x, y-1, "]"])
        hit_wall = False
        for cell in impacted_cells:
            x, y, _ = cell
            if grid[y-1][x] == "#":
                hit_wall = True
            elif grid[y-1][x] in ["[", "]"]:
                if grid[y-1][x] == "[":
                    impacted_cells.append([x, y-1, "["])
                    impacted_cells.append([x+1, y-1, "]"])
                elif grid[y-1][x] == "]":
                    impacted_cells.append([x-1, y-1, "["])
                    impacted_cells.append([x, y-1, "]"])
    if direction == "v":
        grid_below = grid[y+1][x]
        if grid_below == "[":
            impacted_cells.append([x, y+1, "["])
            impacted_cells.append([x+1, y+1, "]"])
        elif grid_below == "]":
            impacted_cells.append([x-1, y+1, "["])
            impacted_cells.append([x, y+1, "]"])
        hit_wall = False        
        for cell in impacted_cells:
            x, y, _ = cell
            if grid[y+1][x] == "#":
                hit_wall = True
            elif grid[y+1][x] in ["[", "]"]:
                if grid[y+1][x] == "[":
                    impacted_cells.append([x, y+1, "["])
                    impacted_cells.append([x+1, y+1, "]"])
                elif grid[y+1][x] == "]":
                    impacted_cells.append([x-1, y+1, "["])
                    impacted_cells.append([x, y+1, "]"])
    return [] if hit_wall else impacted_cells

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
            index_square = next((i for i, square in enumerate(squares_in_front) if square[2] == "."), None)
            if index_square is None:
                continue
            x, y = robot_position
            grid[y][x] = "." # Remove robot from current position
            for i in range(index_square + 1):
                temp_x, temp_y, temp_val = squares_in_front[i]
                grid[temp_y][temp_x] = "@" if i == 0 else squares_in_front[i-1][2]
    final_box_positions = [(x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == "O"]
    total = sum((y * 100) + x for x, y in final_box_positions)
    print_and_verify_answer(mode, "one", total, expected)

def run_part_two(mode, expected = None):
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
                modified_line = line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
                grid.append(list(modified_line))
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
            if move in "<>":
                squares_in_front = get_pushable_region(grid, robot_position, move)
                if not squares_in_front:
                    continue
                index_square = next((i for i, square in enumerate(squares_in_front) if square[2] == "."), None)
                if index_square is None:
                    continue
                new_list_of_squares_in_front = [[temp_x, temp_y, "@" if index == 0 else squares_in_front[index-1][2]] 
                                                for index, (temp_x, temp_y, _) in enumerate(squares_in_front[:index_square+1])]
                x, y = robot_position
                grid[y][x] = "."  # Remove robot from current position
                for x, y, val in new_list_of_squares_in_front:
                    grid[y][x] = val
            elif move == "v":
                x, y = robot_position
                impacted_area = calculate_impacted_area(grid, robot_position, "v")
                if impacted_area:
                    grid[y][x] = "."                    
                    if grid[y+1][x] == "[":
                        grid[y+1][x+1] = "."
                    elif grid[y+1][x] == "]":
                        grid[y+1][x-1] = "."
                    grid[y+1][x] = "@"  # robot moves down
                    temp_changes = [[x, y+1, val] for x, y, val in impacted_area if y < len(grid)-2 and val != "."]
                    for x, y, val in temp_changes:
                        grid[y][x] = val
                    for x, y, val in impacted_area:
                        if not any(t[0] == x and t[1] == y-1 for t in impacted_area) and grid[y][x] != "@":
                            grid[y][x] = "."
            else:  # move up
                x, y = robot_position
                impacted_area = calculate_impacted_area(grid, robot_position, "^")
                if impacted_area:
                    grid[y][x] = "."                    
                    if grid[y-1][x] == "[":
                        grid[y-1][x+1] = "."
                    elif grid[y-1][x] == "]":
                        grid[y-1][x-1] = "."                    
                    grid[y-1][x] = "@"  # robot moves up
                    temp_changes = [[x, y-1, val] for x, y, val in impacted_area if y > 0 and val != "."]                    
                    for x, y, val in temp_changes:
                        grid[y][x] = val
                    for x, y, val in impacted_area:
                        if not any(t[0] == x and t[1] == y+1 for t in impacted_area) and grid[y][x] != "@":
                            grid[y][x] = "."
    score = sum((row_index * 100) + col_index for row_index, row in enumerate(grid) for col_index, col in enumerate(row) if col == "[")
    print_and_verify_answer(mode, "two", score, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 2028)
run_part_one("test2", 10092)
run_part_one("prod", 1497888)
run_part_two("test2", 9021)
run_part_two("prod", 1522420)
# Now run it and watch the magic happen 🪄