import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def determine_valid_moves(x, y, char):
    if y < len(terrain) - 1:
        if ord(terrain[y + 1][x]["char"]) - ord(char) <= 1:
            terrain[y][x]["valid_moves"].append((x, y + 1))
    if y > 0:
        if  ord(terrain[y - 1][x]["char"]) - ord(char) <= 1:
            terrain[y][x]["valid_moves"].append((x, y - 1))
    if x < len(terrain[y]) - 1:
        if ord(terrain[y][x + 1]["char"]) - ord(char) <= 1:
            terrain[y][x]["valid_moves"].append((x + 1, y))
    if x > 0:
        if ord(terrain[y][x - 1]["char"]) - ord(char) <= 1:
            terrain[y][x]["valid_moves"].append((x - 1, y))

# COPILOT_ASSIST: Having built the terrain grid and determined the required moves,
# Copilot came along and wrote almost all of this function for me.
# (With the exception of `move not in new_queue` - there was an infinite loop until I added it)
def determine_shortest_route(start, end):
    steps = 0
    queue = [start]
    while len(queue) > 0:
        new_queue = []
        for x, y in queue:
            terrain[y][x]["visited"] = True
            if (x, y) == end:
                return steps
            for move in terrain[y][x]["valid_moves"]:
                if not terrain[move[1]][move[0]]["visited"] and move not in new_queue:
                    new_queue.append(move)
        steps += 1
        queue = new_queue

def clear_visited():
    for y, line in enumerate(terrain):
        for x, char in enumerate(line):
                terrain[y][x]["visited"] = False

terrain = []
for line in open_file("input.txt"):
    this_line = []
    for char in line.strip():
        this_line.append({"char": char, "valid_moves": [], "visited": False})
    terrain.append(this_line)

# Locate the start and end points
for y, line in enumerate(terrain):
    for x, char in enumerate(line):
        if char["char"] == "S":
            start_point = (x,y)
            terrain[y][x]["char"] = "a"
        if char["char"] == "E":
            end_point = (x,y)
            terrain[y][x]["char"] = "z"

# Iterate over terrain and determine valid moves for each char
for y, line in enumerate(terrain):
    for x, char in enumerate(line):
        determine_valid_moves(x, y, char["char"])

# PART 1: Find shortest route from start to end
# HINT_RECEIVED: Kudos to Paul Martin for introducing me to Dijksta's algorithm - 
# after learning about this, it was just a question of building all the components
# necessary to construct the route-finder.
print(f"Part 1: {determine_shortest_route(start_point, end_point)} steps") # 408

# PART 2: Do the same again, but from all the "a" starting points
min_steps = sys.maxsize
for y, line in enumerate(terrain):
    for x, char in enumerate(line):
        if char["char"] == "a":
            clear_visited()
            this_steps = determine_shortest_route((x,y), end_point)
            if this_steps != None and this_steps < min_steps:
                min_steps = this_steps
print(f"Part 2: {min_steps} steps") # 399