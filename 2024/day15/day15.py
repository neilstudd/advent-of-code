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
    
    # if there are no '.' then there are no spaces to move things into; return empty list
    if "." not in [grid[y][x] for x, y, val in squares]:
        return []
    return squares

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
        new_cells_added = True
        while new_cells_added and not hit_wall:
            new_cells_added = False
            for cell in impacted_cells:
                x, y, val = cell
                if grid[y-1][x] == "#":
                    hit_wall = True
                elif grid[y-1][x] == ".":
                    new_cells_added = False
                else:
                    if grid[y-1][x] == "[":
                        impacted_cells.append([x, y-1, "["])
                        impacted_cells.append([x+1, y-1, "]"])
                        new_cells_added = True
                    elif grid[y-1][x] == "]":
                        impacted_cells.append([x-1, y-1, "["])
                        impacted_cells.append([x, y-1, "]"])
                        new_cells_added = True        
    if direction == "v":
        grid_below = grid[y+1][x]
        if grid_below == "[":
            impacted_cells.append([x, y+1, "["])
            impacted_cells.append([x+1, y+1, "]"])
        elif grid_below == "]":
            impacted_cells.append([x-1, y+1, "["])
            impacted_cells.append([x, y+1, "]"])
        hit_wall = False
        new_cells_added = True
        while new_cells_added and not hit_wall:
            new_cells_added = False
            for cell in impacted_cells:
                x, y, val = cell
                if grid[y+1][x] == "#":
                    hit_wall = True
                elif grid[y+1][x] == ".":
                    new_cells_added = False
                else:
                    if grid[y+1][x] == "[":
                        impacted_cells.append([x, y+1, "["])
                        impacted_cells.append([x+1, y+1, "]"])
                    elif grid[y+1][x] == "]":
                        impacted_cells.append([x-1, y+1, "["])
                        impacted_cells.append([x, y+1, "]"])

    if hit_wall:
        return []

    return impacted_cells

def contains_empty_row(data):
    return index_of_first_empty_row(data) != -1

def index_of_first_empty_row(data):
    # Create a dictionary to group values by y
    y_groups = {}
    
    for x, y, val in data:
        if y not in y_groups:
            y_groups[y] = []
        y_groups[y].append(val)
    
    # Check each group to find the first one that contains only '.'
    for y, vals in y_groups.items():
        if all(val == '.' for val in vals):
            return y
    
    return -1  # Return None if no such group is found

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
    grid = []
    moves = []
    finished_grid = False
    for line in data_file:
        line = line.strip()
        if not finished_grid:
            if not line:
                finished_grid = True
            else:
                # Process the line
                modified_line = ""
                for char in line:
                    if char == "#":
                        modified_line += "##"
                    elif char == "O":
                        modified_line += "[]"
                    elif char == "@":
                        modified_line += "@."
                    else:
                        modified_line += ".."
                grid.append(list(modified_line))
        else:
            moves.extend(line)

    for move in moves: 
        robot_position = get_robot_position(grid)
        if is_touching_space(grid, robot_position, move):
            # If there's a space, then it's the same as part 1
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
            if move == "<" or move == ">":
                # Moving left/right is technically the same as part 1
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
            elif move == "v":
                x, y = robot_position
                impacted_area = calculate_impacted_area(grid, robot_position, "v")
                if len(impacted_area) > 0:
                    x, y = robot_position
                    grid[y][x] = "."
                    
                    # Depends which character is below
                    if grid[y+1][x] == "[":
                        grid[y+1][x+1] = "."
                    elif grid[y+1][x] == "]":
                        grid[y+1][x-1] = "."
                    
                    grid[y+1][x] = "@" # robot moves down
                    temp_changes = []
                    max_y_to_change = index_of_first_empty_row(impacted_area) if index_of_first_empty_row(impacted_area) != -1 else len(grid)-1
                    for x, y, val in impacted_area:                        
                        if y < len(grid)-2 and y < max_y_to_change and val != ".":
                            temp_changes.append([x, y+1, val])

                            # if the cell above this one isn't in impacted_area, we need to add it as a dot
                            if not any(t[0] == x and t[1] == y-1 for t in impacted_area):
                                if grid[y][x] != "@":
                                    temp_changes.append([x, y, "."])
                    
                    for x, y, val in temp_changes:
                        grid[y][x] = val
                
            else: # move up
                x, y = robot_position
                impacted_area = calculate_impacted_area(grid, robot_position, "^")
                if len(impacted_area) > 0:
                    x, y = robot_position
                    grid[y][x] = "."

                    if grid[y-1][x] == "[":
                        grid[y-1][x+1] = "."
                    elif grid[y-1][x] == "]":
                        grid[y-1][x-1] = "."

                    grid[y-1][x] = "@" # robot moves up
                    temp_changes = []
                    for x, y, val in impacted_area:
                        if y > 0 and val != ".":
                            temp_changes.append([x, y-1, val])

                        # if the cell below this one isn't in impacted_area, we need to add it as a dot
                        if not any(t[0] == x and t[1] == y+1 for t in impacted_area):
                            if grid[y][x] != "@":
                                temp_changes.append([x, y, "."])

                    for x, y, val in temp_changes:
                        grid[y][x] = val
                        
    score = sum((row_index * 100) + col_index for row_index, row in enumerate(grid) for col_index, col in enumerate(row) if col == "[")
    print_and_verify_answer(mode, "two", score, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 2028)
run_part_one("test2", 10092)
run_part_one("prod", 1497888)
run_part_two("test2", 9021)
run_part_two("prod", 1522420)
# Now run it and watch the magic happen 🪄