import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer, initialise_grid
from collections import deque

# BFS assistance from AI 🤖
def calculate_routes(grid):
    start_x, start_y = calculate_starting_position(grid)
    queue = deque([(start_x, start_y, [(start_x, start_y)], ">", 0)])
    best_scores = { (start_x, start_y): 0 }
    routes = []
    lowest_score = float('inf')    
    while queue:
        x, y, path, current_dir, score = queue.popleft()        
        if grid[y][x] == 'E':
            if score < lowest_score:
                lowest_score = score
                routes = [(path, score)]
            elif score == lowest_score:
                routes.append((path, score))
            continue      
        for dx, dy, new_dir in [(-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v")]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and
                grid[new_y][new_x] in ['.', 'E']):                
                turn_penalty = 1000 if new_dir != current_dir else 0
                new_score = score + 1 + turn_penalty
                if (new_x, new_y) not in best_scores or new_score <= best_scores[(new_x, new_y)]:
                    best_scores[(new_x, new_y)] = new_score
                    queue.append((new_x, new_y, path + [(new_x, new_y)], new_dir, new_score))    
    return lowest_score

# Part 2, more BFS assistance from AI 🤖 (these can probably be refactored into a single method)
def calculate_all_routes_with_lowest_score(grid, lowest_score):
    start_x, start_y = calculate_starting_position(grid)
    end_x, end_y = calculate_ending_position(grid)
    queue = deque([(start_x, start_y, [(start_x, start_y)], 0, 0, 0)])
    distinct_cells = set()
    visited = {}
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    while queue:
        x, y, path, current_dir, current_score, turn_penalties = queue.popleft()
        total_score = current_score + turn_penalties
        if total_score > lowest_score: # Not optimal route
            continue
        if (x, y) == (end_x, end_y) and total_score == lowest_score:
            distinct_cells.update(path)
            continue
        if ((x, y), current_dir) in visited and visited[((x, y), current_dir)] < total_score:
            continue
        visited[((x, y), current_dir)] = total_score        
        for new_dir, (dy, dx) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and
                grid[new_y][new_x] in ['.', 'E']):
                new_turn_penalties = turn_penalties + (1000 if new_dir != current_dir else 0)
                new_total_score = current_score + 1 + new_turn_penalties
                if new_total_score <= lowest_score:
                    queue.append((new_x, new_y, path + [(new_x, new_y)], new_dir, current_score + 1, new_turn_penalties))
    return len(distinct_cells)

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
    lowest_route_score = calculate_routes(maze)
    print_and_verify_answer(mode, "one", lowest_route_score, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    maze = initialise_grid(data_file)
    lowest_route_score = calculate_routes(maze)
    cells_visited_on_best_routes = calculate_all_routes_with_lowest_score(maze, lowest_route_score)
    print_and_verify_answer(mode, "two", cells_visited_on_best_routes, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 7036)
run_part_one("prod", 106512)
run_part_two("test", 45)
run_part_two("prod", 563)
# Now run it and watch the magic happen 🪄