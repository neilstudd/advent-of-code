import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def initialise_map(data_file):
    return [list(line.strip()) for line in data_file]

def find_trailheads(map):
    trailheads = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[x][y] == "0":
                trailheads.append((x, y))
    return trailheads

def find_summits(map):
    summits = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[x][y] == "9":
                summits.append((x, y))
    return summits

def is_touching_number(map, x, y, number, direction):
    if direction == "up":
        if x > 0 and map[x-1][y] == str(number):
            return x-1, y
    if direction == "down":
        if x < len(map) - 1 and map[x+1][y] == str(number):
            return x+1, y
    if direction == "left":
        if y > 0 and map[x][y-1] == str(number):
            return x, y-1
    if direction == "right":
        if y < len(map[0]) - 1 and map[x][y+1] == str(number):
            return x, y+1
    return None, None

def calculate_trailhead_score(map, trailhead):
    cells_visited = set()
    cells_visited.add(trailhead)
    for number_to_check in range(1, 10):
        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[x][y] == ".": # For the examples
                    continue
                if map[x][y] == str(number_to_check-1):
                    if (x, y) in cells_visited:
                        cells_visited.add((x, y))
                        for direction in ["up", "down", "left", "right"]:
                            touching_x, touching_y = is_touching_number(map, x, y, number_to_check, direction)
                            if touching_x is not None:
                                cells_visited.add((touching_x, touching_y))
    return sum(1 for summit in find_summits(map) if summit in cells_visited)

# This method wouldn't exist without some AI help
def dfs(current_position, current_value, visited, grid, movements, ends, unique_routes):
    if current_position in ends:
        unique_routes[0] += 1
        return
    visited.add(current_position)
    for movement in movements:
        new_i, new_j = current_position[0] + movement[0], current_position[1] + movement[1]
        if (0 <= new_i < len(grid)) and (0 <= new_j < len(grid[0])):  # Within grid boundaries
            new_value = grid[new_i][new_j]
            if new_value.isdigit() and int(new_value) == current_value + 1:  # Valid move (upward increment of 1)
                if (new_i, new_j) not in visited:
                    dfs((new_i, new_j), int(new_value), visited, grid, movements, ends, unique_routes)
    visited.remove(current_position)  # Backtrack

def part2_count_unique_routes(grid, trailhead):
    ends = find_summits(grid)
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    unique_routes = [0]
    dfs(trailhead, 0, set(), grid, movements, ends, unique_routes)
    return unique_routes[0]

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    map = initialise_map(data_file)
    trailheads = find_trailheads(map)
    total_score = 0
    for trailhead in trailheads:
        total_score += calculate_trailhead_score(map, trailhead)
    print_and_verify_answer(mode, "one", total_score, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    map = initialise_map(data_file)
    unique_routes = 0
    trailheads = find_trailheads(map)
    for trailhead in trailheads:
        unique_routes += part2_count_unique_routes(map, trailhead)
    print_and_verify_answer(mode, "two", unique_routes, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 36)
run_part_one("prod", 468)
run_part_two("test", 81)
run_part_two("prod", 966)
# Now run it and watch the magic happen 🪄