import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

horizontal = 0
depth = 0
for line in open_file("input.txt"):
    direction, distance = line.strip().split()[0], int(line.strip().split()[1])
    if direction == "forward": horizontal += distance
    elif direction == "down": depth += distance
    elif direction == "up": depth -= distance

print(f"Part 1: {horizontal * depth}") # 2117664

horizontal = 0
depth = 0
aim = 0
for line in open_file("input.txt"):
    direction, distance = line.strip().split()[0], int(line.strip().split()[1])
    if direction == "down": aim += distance
    elif direction == "up": aim -= distance
    elif direction == "forward":
        horizontal += distance
        depth += (aim * distance)
print(f"Part 2: {horizontal * depth}") # 2073416724