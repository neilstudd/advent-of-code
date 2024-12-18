import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer
from collections import deque

def create_byte_list(data_file):
    falling_bytes = []
    for line in data_file:
        x, y = line.strip().split(",")
        falling_bytes.append((int(x), int(y)))
    return falling_bytes

def create_empty_grid(width, height):
    return [["." for _ in range(0, width)] for _ in range(0, height)]

# Repurposed (and modified) from day 16
def calculate_routes(grid):
    start_x, start_y = 0, 0
    end_x = len(grid[0]) - 1
    end_y = len(grid) - 1
    queue = deque([(start_x, start_y, 0)])
    best_scores = { (start_x, start_y): 0 }
    while queue:
        x, y, score = queue.popleft()
        if x == end_x and y == end_y:
            return score
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] == '.'):
                new_score = score + 1
                if (new_x, new_y) not in best_scores or new_score < best_scores[(new_x, new_y)]:
                    best_scores[(new_x, new_y)] = new_score
                    queue.append((new_x, new_y, new_score))
    return None  # Return None if no route is found

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    falling_bytes = create_byte_list(data_file)
    width, height, bytes_to_fall = (7, 7, 12) if mode == "test" else (71, 71, 1024)
    grid = create_empty_grid(width, height)
    bytes_fallen = 0
    for byte in falling_bytes:
        x, y = byte
        grid[y][x] = "#"
        bytes_fallen += 1
        if bytes_fallen == bytes_to_fall:
            break   
    shortest_route = calculate_routes(grid)
    print_and_verify_answer(mode, "one", shortest_route, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    falling_bytes = create_byte_list(data_file)
    width, height = (7, 7) if mode == "test" else (71, 71)
    grid = create_empty_grid(width, height)
    for byte in falling_bytes:
        x, y = byte
        grid[y][x] = "#"
        shortest_route = calculate_routes(grid)
        if shortest_route == None:
            break # This is the first byte that's blocked the exit
    first_blocked_byte = ",".join([str(x) for x in byte])
    print_and_verify_answer(mode, "two", first_blocked_byte, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 22)
run_part_one("prod", 280)
run_part_two("test", "6,1")
run_part_two("prod", "28,56")
# Now run it and watch the magic happen 🪄