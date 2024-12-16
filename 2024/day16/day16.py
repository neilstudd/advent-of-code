import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer, initialise_grid
from collections import deque

def calculate_routes(grid):
    # Find the starting position 'S'
    start_x, start_y = calculate_starting_position(grid)
    
    # Queue for BFS: each element is (x, y, path, current_dir, score)
    queue = deque([(start_x, start_y, [(start_x, start_y)], ">", 0)])
    
    # Dictionary to store the lowest score for reaching each cell
    best_scores = { (start_x, start_y): 0 }
    
    # List to store all possible routes
    routes = []
    lowest_score = float('inf')
    
    while queue:
        x, y, path, current_dir, score = queue.popleft()
        
        # If we reach the end, add the path and score to the results
        if grid[y][x] == 'E':
            if score < lowest_score:
                print("New lowest score", score)
                lowest_score = score
                routes = [(path, score)]  # Reset routes with new lowest score
            elif score == lowest_score:
                print("Equals lowest score")
                routes.append((path, score))
            continue
        
        # Explore neighbors (up, down, left, right)
        for dx, dy, new_dir in [(-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v")]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and
                grid[new_y][new_x] in ['.', 'E']):
                
                new_score = score + 1
                if new_dir != current_dir:
                    new_score += 1000
                
                # Check if this path is better or equal to the best found path to this cell
                if (new_x, new_y) not in best_scores or new_score <= best_scores[(new_x, new_y)]:
                    best_scores[(new_x, new_y)] = new_score
                    queue.append((new_x, new_y, path + [(new_x, new_y)], new_dir, new_score))
    
    return routes

def calculate_starting_position(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                return x, y

def calculate_direction(current_cell, new_cell):
    x, y = current_cell
    new_x, new_y = new_cell
    if new_x > x:
        return ">"
    elif new_x < x:
        return "<"
    elif new_y > y:
        return "v"
    elif new_y < y:
        return "^"

def is_last_move_in_route(move, route):
    return move == route[-1]

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    maze = initialise_grid(data_file)
    routes = calculate_routes(maze)
    lowest_route_score = 9999999
    for route in routes:
        route_score = route[-1]
        if route_score < lowest_route_score:
            lowest_route_score = route_score
    print_and_verify_answer(mode, "one", lowest_route_score, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    maze = initialise_grid(data_file)
    routes = calculate_routes(maze)
    lowest_route_score = 9999999
    for route in routes:
        route_score = route[-1]
        if route_score < lowest_route_score:
            lowest_route_score = route_score

    # Now we know the lowest score, get all of the routes which have that score
    best_routes = [route for route in routes if route[-1] == lowest_route_score]
    for route in best_routes:
        print(route)
        print(len(route[0]))

    answer = None # <-- Change this to answer
    # -------------------------------
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 7036)
run_part_one("prod", 106512)
run_part_two("test", 0)
#run_part_two("prod")
# Now run it and watch the magic happen 🪄