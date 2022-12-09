import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

print_tail_grid = lambda: (print("".join(row)) for row in tail_grid)

def mark_tail_location():
    x = rope[-1]["x"]
    y = rope[-1]["y"]
    tail_grid[y][x] = "#"

def move_whole_rope():
    for i in range(1, len(rope)):
        move_this_link(rope[i-1], rope[i])
    mark_tail_location()

def move_this_link(a, b):
    if a["x"] == b["x"] and a["y"] == b["y"]:
        return # a covers b
    elif abs(a["y"] - b["y"]) <= 1 and abs(a["x"] - b["x"]) <= 1:
        return # already touching
    elif a["x"] == b["x"]:
        if a["y"] > b["y"]:
            b["y"] += 1
        else:
            b["y"] -= 1
    elif a["y"] == b["y"]:
        if a["x"] > b["x"]:
            b["x"] += 1
        else:
            b["x"] -= 1
    else: # Diagonal?
        if a["x"] > b["x"]:
            if a["y"] > b["y"]:
                b["x"] += 1
                b["y"] += 1
            else:
                b["x"] += 1
                b["y"] -= 1
        else:
            if a["y"] > b["y"]:
                b["x"] -= 1
                b["y"] += 1
            else:
                b["x"] -= 1
                b["y"] -= 1 

# Build a grid with all squares unvisited
tail_grid = [["." for x in range(1000)] for y in range(1000)]

# Hardcode the rope
rope = [{"x": 0, "y": 0},{"x": 0, "y": 0},{"x": 0, "y": 0},{"x": 0, "y": 0},{"x": 0, "y": 0},{"x": 0, "y": 0},{"x": 0, "y": 0},{"x": 0, "y": 0},{"x": 0, "y": 0},{"x": 0, "y": 0}]

for line in open_file("input.txt"):
    dir, steps = line.strip().split(" ")
    for i in range(int(steps)):
        rope[0]["x"] += 1 if dir == "R" else -1 if dir == "L" else 0
        rope[0]["y"] -= 1 if dir == "U" else -1 if dir == "D" else 0
        move_whole_rope()

print(sum(row.count("#") for row in tail_grid))   # 2384 