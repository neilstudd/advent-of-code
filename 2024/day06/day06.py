import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def initialise_map(data_file):
    return [list(line.strip()) for line in data_file]

def get_guard_direction(map, x, y):
    directions = {"^": "up", "v": "down", "<": "left", ">": "right"}
    return directions.get(map[x][y])

def get_next_character(map, x, y, direction):
    if direction == "up":
        return map[x-1][y]
    if direction == "down":
        return map[x+1][y]
    if direction == "left":
        return map[x][y-1]
    if direction == "right":
        return map[x][y+1]

def at_exit(map, x, y, direction):
    return (direction == "up" and x == 0) or \
           (direction == "down" and x == len(map) - 1) or \
           (direction == "left" and y == 0) or \
           (direction == "right" and y == len(map[0]) - 1)

def do_the_walk(map):
    squares_visited = [['.' for _ in range(len(map[0]))] for _ in range(len(map))]
    been_here_before = set() # Build this as we need it (most of it won't be needed 💡)

    guard_position_x, guard_position_y = None, None
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[x][y] in "^v<>":
                guard_position_x, guard_position_y = x, y
                break
        if guard_position_x is not None:
            break

    while guard_position_x is not None:
        current_direction = get_guard_direction(map, guard_position_x, guard_position_y)
        squares_visited[guard_position_x][guard_position_y] = 'X'  # Mark initial position as visited
        if at_exit(map, guard_position_x, guard_position_y, current_direction):
            break

        if (guard_position_x, guard_position_y, current_direction) in been_here_before:
            return -1

        squares_visited[guard_position_x][guard_position_y] = 'X'
        next_character = get_next_character(map, guard_position_x, guard_position_y, current_direction)

        # Change current guard position back to dot
        map[guard_position_x][guard_position_y] = "."
        been_here_before.add((guard_position_x, guard_position_y, current_direction))

        if next_character == "#": # Turn to the right
            turn_right = {"up": "right", "right": "down", "down": "left", "left": "up"}
            new_direction = turn_right[current_direction]
            map[guard_position_x][guard_position_y] = {"up": "^", "down": "v", "left": "<", "right": ">"}[new_direction]
        elif next_character == ".": # Move into that cell
            move_delta = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
            delta_x, delta_y = move_delta[current_direction]
            guard_position_x += delta_x
            guard_position_y += delta_y
            map[guard_position_x][guard_position_y] = {"up": "^", "down": "v", "left": "<", "right": ">"}[current_direction]

    return sum(row.count('X') for row in squares_visited)

def run_part_one(mode, expected = None):
    data_file = open_file(mode + ".txt")
    map = initialise_map(data_file)
    total_squares = do_the_walk(map)
    print_and_verify_answer(mode, "one", total_squares, expected)

def run_part_two(mode, expected = None):
    data_file = open_file(mode + ".txt")
    temp_map = initialise_map(data_file)
    looping_obstructions = 0
    for row_index, row in enumerate(temp_map):
        for cell_index, cell in enumerate(row):
            map = initialise_map(data_file)
            map[row_index][cell_index] = "#"
            number_of_steps = do_the_walk(map)
            if number_of_steps == -1: # We successfully forced a loop
                looping_obstructions += 1           
    print_and_verify_answer(mode, "two", looping_obstructions, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 41)
run_part_one("prod", 4982)
run_part_two("test", 6)
run_part_two("prod", 1663)
# Now run it and watch the magic happen 🪄