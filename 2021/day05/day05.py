import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def process_line(line):
    left_x = line.strip().split(" -> ")[0].split(",")[0]
    left_y = line.strip().split(" -> ")[0].split(",")[1]
    right_x = line.strip().split(" -> ")[1].split(",")[0]
    right_y = line.strip().split(" -> ")[1].split(",")[1]
    return (int(left_x), int(left_y), int(right_x), int(right_y))

def calculate_grid_size():
    max_x = 0
    max_y = 0
    for line in open_file("input.txt"): 
        left_x, left_y, right_x, right_y = process_line(line.strip())
        if left_x > max_x: max_x = left_x
        if left_y > max_y: max_y = left_y
        if right_x > max_x: max_x = right_x
        if right_y > max_y: max_y = right_y
    return (max_x, max_y)

def fill_grid(part_two = False):
    for line in open_file("input.txt"): 
        left_x, left_y, right_x, right_y = process_line(line.strip())

         # Process horizontal lines
        if left_y == right_y:
            if left_x > right_x: left_x, right_x = right_x, left_x
            for x in range(left_x, right_x+1): grid[left_y][x] += 1
        
        # Process vertical lines
        if left_x == right_x:
            if left_y > right_y: left_y, right_y = right_y, left_y
            for y in range(left_y, right_y+1): grid[y][left_x] += 1

        # In part two, also process diagonal lines
        if part_two:
            if left_x < right_x and left_y < right_y:
                for x in range(left_x, right_x+1):
                    grid[left_y][x] += 1
                    left_y += 1
            elif left_x < right_x and left_y > right_y:
                for x in range(left_x, right_x+1):
                    grid[left_y][x] += 1
                    left_y -= 1
            elif left_x > right_x and left_y < right_y:
                for x in range(left_x, right_x-1, -1):
                    grid[left_y][x] += 1
                    left_y += 1
            elif left_x > right_x and left_y > right_y:
                for x in range(left_x, right_x-1, -1):
                    grid[left_y][x] += 1
                    left_y -= 1

def calculate_overlaps():
    overlaps = 0
    for row in grid:
        for column in row:
            if column >= 2: overlaps += 1
    return overlaps

max_x, max_y = calculate_grid_size()
grid = [[0 for x in range(max_x+1)] for y in range(max_y+1)]
fill_grid()
print(f"Part 1: {calculate_overlaps()}") # 7436

# Part 2: Recreate grid
grid = [[0 for x in range(max_x+1)] for y in range(max_y+1)]
fill_grid(True)
print(f"Part 2: {calculate_overlaps()}") # 21104