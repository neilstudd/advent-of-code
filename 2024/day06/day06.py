import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def get_guard_direction(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "^":
                return "up"
            if map[x][y] == "v":
                return "down"
            if map[x][y] == "<":
                return "left"
            if map[x][y] == ">":
                return "right"

def get_guard_position(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[x][y] == "^":
                return (x, y)
            if map[x][y] == "v":
                return (x, y)
            if map[x][y] == "<":
                return (x, y)
            if map[x][y] == ">":
                return (x, y)

def get_next_character(map, x, y, direction):
    if direction == "up":
        return map[x-1][y]
    if direction == "down":
        return map[x+1][y]
    if direction == "left":
        return map[x][y-1]
    if direction == "right":
        return map[x][y+1]

def at_exit(map):
    return get_guard_direction(map) == "up" and get_guard_position(map)[0] == 0 or \
              get_guard_direction(map) == "down" and get_guard_position(map)[0] == len(map) - 1 or \
                get_guard_direction(map) == "left" and get_guard_position(map)[1] == 0 or \
                    get_guard_direction(map) == "right" and get_guard_position(map)[1] == len(map[0]) - 1

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    map = []
    for line in data_file:
        this_row = []
        for c in line.strip():
            this_row.append(c)
        map.append(this_row)

    squares_visited = []
    for x in range(len(map)):
        this_row = []
        for y in range(len(map[x])):
            this_row.append('.')
        squares_visited.append(this_row)

    while not at_exit(map):
        current_direction = get_guard_direction(map)
        guard_position_x, guard_position_y = get_guard_position(map)
        squares_visited[guard_position_x][guard_position_y] = 'X'
        next_character = get_next_character(map, guard_position_x, guard_position_y, current_direction)

        # Change current guard position back to dot
        map[guard_position_x][guard_position_y] = "."

        if next_character == "#": # Turn to the right
            if current_direction == "up":
                map[guard_position_x][guard_position_y] = ">"
            elif current_direction == "down":
                map[guard_position_x][guard_position_y] = "<"
            elif current_direction == "left":
                map[guard_position_x][guard_position_y] = "^"
            elif current_direction == "right":
                map[guard_position_x][guard_position_y] = "v"
        elif next_character == ".": # Move into that cell
            if current_direction == "up":
                map[guard_position_x-1][guard_position_y] = "^"
                squares_visited[guard_position_x-1][guard_position_y] = 'X'
            elif current_direction == "down":
                map[guard_position_x+1][guard_position_y] = "v"
                squares_visited[guard_position_x+1][guard_position_y] = 'X'
            elif current_direction == "left":
                map[guard_position_x][guard_position_y-1] = "<"
                squares_visited[guard_position_x][guard_position_y-1] = 'X'
            elif current_direction == "right":
                map[guard_position_x][guard_position_y+1] = ">"
                squares_visited[guard_position_x][guard_position_y+1] = 'X'

    total_squares = sum([row.count('X') for row in squares_visited])
    print_and_verify_answer(mode, "one", total_squares, expected)

def run_part_two(mode, expected = None):

    data_file = open_file( mode + ".txt")

    # -------------------------------
    # Part Two code goes here

    answer = None # <-- Change this to answer
    # -------------------------------
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 41)
run_part_one("prod", 4982)
run_part_two("test", 0)
run_part_two("prod")
# Now run it and watch the magic happen 🪄