import sys, os, common
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer, initialise_grid

def find_trailheads(map):
    return [(x, y) for y in range(len(map)) for x in range(len(map[y])) if map[x][y] == "0"]

def find_summits(map):
    return [(x, y) for y in range(len(map)) for x in range(len(map[y])) if map[x][y] == "9"]

def is_touching_number(map, x, y, number, direction):
    dx, dy = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}[direction]
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < len(map) and 0 <= new_y < len(map[0]) and map[new_x][new_y] == str(number):
        return new_x, new_y
    return None, None

def calculate_trailhead_score(map, trailhead):
    cells_visited = set()
    cells_visited.add(trailhead)
    for number_to_check in range(1, 10):
        for x in range(len(map)):
            for y in range(len(map[x])):
                if map[x][y] == str(number_to_check - 1) and (x, y) in cells_visited:
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
    map = initialise_grid(data_file)
    trailheads = find_trailheads(map)
    total_score = 0
    for trailhead in trailheads:
        total_score += calculate_trailhead_score(map, trailhead)
    print_and_verify_answer(mode, "one", total_score, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    map = initialise_grid(data_file)
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