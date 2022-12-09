import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

print_grid = lambda: (print("".join(row)) for row in grid)

def mark_visited(x, y):
    grid[y][x] = "#"

def determine_tail_movement():
    if cur_h["x"] == cur_t["x"] and cur_h["y"] == cur_t["y"]:
        return # H covers T
    elif abs(cur_h["y"] - cur_t["y"]) <= 1 and abs(cur_h["x"] - cur_t["x"]) <= 1:
        return # already touching
    elif cur_h["x"] == cur_t["x"]:
        if cur_h["y"] > cur_t["y"]:
            cur_t["y"] += 1
        else:
            cur_t["y"] -= 1
    elif cur_h["y"] == cur_t["y"]:
        if cur_h["x"] > cur_t["x"]:
            cur_t["x"] += 1
        else:
            cur_t["x"] -= 1
    else: # Diagonal?
        if cur_h["x"] > cur_t["x"]:
            if cur_h["y"] > cur_t["y"]:
                cur_t["x"] += 1
                cur_t["y"] += 1
            else:
                cur_t["x"] += 1
                cur_t["y"] -= 1
        else:
            if cur_h["y"] > cur_t["y"]:
                cur_t["x"] -= 1
                cur_t["y"] += 1
            else:
                cur_t["x"] -= 1
                cur_t["y"] -= 1

# Build a grid with all squares unvisited
grid = [["." for x in range(1000)] for y in range(1000)]

cur_h = {"x": 0, "y": 0}
cur_t = {"x": 0, "y": 0}

for line in open_file("input.txt"):
    dir, steps = line.strip().split(" ")
    for i in range(int(steps)):
        cur_h["x"] += 1 if dir == "R" else -1 if dir == "L" else 0
        cur_h["y"] += 1 if dir == "D" else -1 if dir == "U" else 0
        determine_tail_movement()
        mark_visited(cur_t["x"], cur_t["y"])

print(sum(row.count("#") for row in grid)) # 6044