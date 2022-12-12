import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def determine_valid_directions(x, y, char):
    if y < len(terrain) - 1:
        if ord(terrain[y + 1][x]["char"]) - ord(char) <= 1:
            terrain[y][x]["directions"] += "S"
    if y > 0:
        if  ord(terrain[y - 1][x]["char"]) - ord(char) <= 1:
            terrain[y][x]["directions"] += "N"
    if x < len(terrain[y]) - 1:
        if ord(terrain[y][x + 1]["char"]) - ord(char) <= 1:
            terrain[y][x]["directions"] += "E"
    if x > 0:
        if ord(terrain[y][x - 1]["char"]) - ord(char) <= 1:
            terrain[y][x]["directions"] += "W"

terrain = []
for line in open_file("input.txt"):
    this_line = []
    for char in line.strip():
        this_line.append({"char": char, "directions": ""})
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

# Iterate over terrain and determine valid directions for each char
for y, line in enumerate(terrain):
    for x, char in enumerate(line):
        determine_valid_directions(x, y, char["char"])

print(terrain)

# FAILED_CHALLENGE
# We have a start_point, an end_point, and each char has a list of valid directions
# Need to algorithmically determine the shortest path from start to end