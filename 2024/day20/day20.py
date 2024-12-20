import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer, initialise_grid
from collections import deque

def calculate_starting_position(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                return x, y

def calculate_ending_position(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'E':
                return x, y

# Repurposed (and modified) from day 18, which in turn came from day 16
def calculate_routes(grid):
    start_x, start_y = calculate_starting_position(grid)
    end_x, end_y = calculate_ending_position(grid)
    queue = deque([(start_x, start_y, 0)])
    best_scores = { (start_x, start_y): 0 }
    while queue:
        x, y, score = queue.popleft()
        if x == end_x and y == end_y:
            return score
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] in ['.', 'E']):
                new_score = score + 1
                if (new_x, new_y) not in best_scores or new_score < best_scores[(new_x, new_y)]:
                    #print("moving at ", new_x, new_y, "with score", new_score)
                    best_scores[(new_x, new_y)] = new_score
                    queue.append((new_x, new_y, new_score))
    return None  # Return None if no route is found

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    grid = initialise_grid(data_file)
    default_solve_time = calculate_routes(grid)
    hashes = [(x, y) for y in range(1, len(grid) - 1) for x in range(1, len(grid[0]) - 1) if grid[y][x] == "#"]

    big_savings = 0
    for hash in enumerate(hashes):
        grid = initialise_grid(data_file)
        # Change hash to dot
        x, y = hash
        grid[y][x] = "."
        shortest_route = calculate_routes(grid)
        time_saved = default_solve_time - shortest_route
        if shortest_route and time_saved >= 100:
            big_savings += 1
    print_and_verify_answer(mode, "one", big_savings, expected)

def run_part_two(mode, expected = None):

    data_file = open_file( mode + ".txt")
    grid = initialise_grid(data_file)
    default_solve_time = calculate_routes(grid)

    answer = None # <-- Change this to answer
    # -------------------------------
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
#run_part_one("test", 0)
#run_part_one("prod", 1502)
run_part_two("test", 0)
#run_part_two("prod")
# Now run it and watch the magic happen 🪄